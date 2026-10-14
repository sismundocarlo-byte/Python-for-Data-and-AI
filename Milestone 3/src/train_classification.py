"""Classification: predict whether a hotel booking will be cancelled (is_canceled).

Workflow: split FIRST (stratified, seed 42) -> baseline + 3 algorithms compared with
5-fold CV on the training set -> tune the candidates with RandomizedSearchCV (CV on
train only) -> evaluate the chosen models ONCE on the held-out test set.

Run:  python src/train_classification.py
"""
import json, time, warnings
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import randint, loguniform
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             roc_auc_score, confusion_matrix, ConfusionMatrixDisplay,
                             RocCurveDisplay, classification_report)
from sklearn.model_selection import (StratifiedKFold, cross_validate,
                                     RandomizedSearchCV, train_test_split)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

warnings.filterwarnings("ignore")
SEED = 42
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "hotel_bookings_clean.csv"
FIG, MODELS = ROOT / "reports", ROOT / "models"
TARGET = "is_canceled"

CAT = ["hotel", "meal", "country", "market_segment", "distribution_channel",
       "reserved_room_type", "deposit_type", "agent", "customer_type"]


def make_preprocessor(num_cols, scale):
    num = [("impute", SimpleImputer(strategy="median"))]
    if scale:
        num.append(("scale", StandardScaler()))
    return ColumnTransformer([
        ("num", Pipeline(num), num_cols),
        # rare categories (rare countries / agents) are pooled together; unseen ones are ignored
        ("cat", OneHotEncoder(handle_unknown="infrequent_if_exist", min_frequency=0.01,
                              sparse_output=False), CAT),
    ])


def main():
    df = pd.read_csv(DATA, dtype={"agent": str})
    X, y = df.drop(columns=TARGET), df[TARGET]
    num_cols = [c for c in X.columns if c not in CAT]

    # ---- split before any fitting
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEED)
    print(f"train {X_tr.shape}  test {X_te.shape}  cancel rate train {y_tr.mean():.3f} test {y_te.mean():.3f}")
    cv = StratifiedKFold(5, shuffle=True, random_state=SEED)
    cv_tune = StratifiedKFold(3, shuffle=True, random_state=SEED)   # lighter CV for the search

    # ---- candidate pipelines
    def pipe(model, scale=False):
        return Pipeline([("prep", make_preprocessor(num_cols, scale)), ("model", model)])

    candidates = {
        "Baseline (majority)": pipe(DummyClassifier(strategy="most_frequent")),
        "Logistic Regression": pipe(LogisticRegression(max_iter=1000, class_weight="balanced"), scale=True),
        "Random Forest": pipe(RandomForestClassifier(n_estimators=100, min_samples_leaf=2, max_depth=25,
                              class_weight="balanced", n_jobs=-1, random_state=SEED)),
        "Hist Gradient Boosting": pipe(HistGradientBoostingClassifier(random_state=SEED)),
    }

    # ---- 1) cross-validated comparison on TRAIN only
    scoring = ["accuracy", "precision", "recall", "f1", "roc_auc"]
    rows = []
    for name, p in candidates.items():
        t = time.time()
        cvres = cross_validate(p, X_tr, y_tr, cv=cv, scoring=scoring, n_jobs=1)
        rows.append({"model": name, **{m: cvres[f"test_{m}"].mean() for m in scoring}})
        print(f"CV {name:<24} F1={rows[-1]['f1']:.3f} AUC={rows[-1]['roc_auc']:.3f}  ({time.time()-t:.0f}s)")
    cv_table = pd.DataFrame(rows).round(4)
    cv_table.to_csv(FIG / "classification_cv_results.csv", index=False)

    # ---- 2) hyperparameter tuning (CV on train only, optimise F1 for the cancelled class)
    searches = {
        "Logistic Regression (tuned)": (candidates["Logistic Regression"],
            {"model__C": loguniform(1e-3, 1e1)}, 5),
        "Random Forest (tuned)": (candidates["Random Forest"],
            {"model__n_estimators": randint(80, 140), "model__max_depth": randint(12, 30),
             "model__min_samples_leaf": randint(1, 8), "model__max_features": ["sqrt", 0.3]}, 4),
        "Hist Gradient Boosting (tuned)": (candidates["Hist Gradient Boosting"],
            {"model__learning_rate": loguniform(0.03, 0.3), "model__max_iter": randint(150, 450),
             "model__max_leaf_nodes": randint(15, 80), "model__min_samples_leaf": randint(10, 80),
             "model__l2_regularization": loguniform(1e-3, 10)}, 6),
    }
    tuned, best_params = {}, {}
    for name, (p, grid, n_iter) in searches.items():
        t = time.time()
        rs = RandomizedSearchCV(p, grid, n_iter=n_iter, scoring="f1", cv=cv_tune,
                                random_state=SEED, n_jobs=1, refit=True)
        rs.fit(X_tr, y_tr)
        tuned[name] = rs.best_estimator_
        best_params[name] = {k: (float(v) if isinstance(v, (np.floating, float)) else
                                 int(v) if isinstance(v, (np.integer,)) else v)
                             for k, v in rs.best_params_.items()}
        print(f"TUNE {name:<32} best CV F1={rs.best_score_:.3f} ({time.time()-t:.0f}s) {best_params[name]}")
    (FIG / "classification_best_params.json").write_text(json.dumps(best_params, indent=2))

    # ---- 3) ONE evaluation on the held-out test set
    base = candidates["Baseline (majority)"].fit(X_tr, y_tr)
    final = {"Baseline (majority)": base, **tuned}
    rows, probs = [], {}
    for name, m in final.items():
        pred = m.predict(X_te)
        proba = m.predict_proba(X_te)[:, 1]
        probs[name] = proba
        rows.append({"model": name,
                     "accuracy": accuracy_score(y_te, pred),
                     "precision": precision_score(y_te, pred, zero_division=0),
                     "recall": recall_score(y_te, pred),
                     "f1": f1_score(y_te, pred),
                     "roc_auc": roc_auc_score(y_te, proba)})
    test_table = pd.DataFrame(rows).round(4)
    test_table.to_csv(FIG / "classification_test_results.csv", index=False)
    print("\nTEST RESULTS\n", test_table.to_string(index=False))


    # ---- plots
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))
    for ax, (name, m) in zip(axes, list(final.items())[1:]):
        ConfusionMatrixDisplay.from_predictions(y_te, m.predict(X_te), display_labels=["Kept", "Cancelled"],
                                                cmap="Blues", ax=ax, colorbar=False)
        ax.set_title(name, fontsize=10)
    plt.tight_layout(); plt.savefig(FIG / "clf_confusion_matrices.png", dpi=130); plt.close()

    fig, ax = plt.subplots(figsize=(6, 5))
    for name, proba in probs.items():
        if name.startswith("Baseline"):
            continue
        RocCurveDisplay.from_predictions(y_te, proba, name=name, ax=ax)
    ax.plot([0, 1], [0, 1], "k--", label="Baseline"); ax.legend(fontsize=8); ax.set_title("ROC curves (test set)")
    plt.tight_layout(); plt.savefig(FIG / "clf_roc_curves.png", dpi=130); plt.close()

    # ---- interpretation on the gradient boosting model
    hgb = tuned["Hist Gradient Boosting (tuned)"]
    sample = X_te.sample(4000, random_state=SEED)
    pi = permutation_importance(hgb, sample, y_te.loc[sample.index], scoring="f1",
                                n_repeats=3, random_state=SEED, n_jobs=1)
    imp = pd.Series(pi.importances_mean, index=X_te.columns).sort_values()
    imp.tail(15).plot.barh(figsize=(7, 5), color="#2a6f97")
    plt.title("Permutation importance (drop in F1) - Hist Gradient Boosting")
    plt.tight_layout(); plt.savefig(FIG / "clf_feature_importance.png", dpi=130); plt.close()
    imp.sort_values(ascending=False).round(4).to_csv(FIG / "clf_feature_importance.csv", header=["importance"])
    print("\nTop features:\n", imp.sort_values(ascending=False).head(10).round(4).to_string())

    # ---- error analysis
    pred = hgb.predict(X_te)
    err = X_te.assign(actual=y_te, pred=pred)
    err["error"] = np.where((err.actual == 1) & (err.pred == 0), "missed cancellation (FN)",
                    np.where((err.actual == 0) & (err.pred == 1), "false alarm (FP)", "correct"))
    print("\nError breakdown:\n", err["error"].value_counts().to_string())
    seg = err.groupby("market_segment").apply(lambda g: pd.Series({
        "n": len(g), "cancel_rate": g.actual.mean(), "error_rate": (g.pred != g.actual).mean()})).round(3)
    dep = err.groupby("deposit_type").apply(lambda g: pd.Series({
        "n": len(g), "cancel_rate": g.actual.mean(), "error_rate": (g.pred != g.actual).mean()})).round(3)
    seg.to_csv(FIG / "clf_error_by_segment.csv"); dep.to_csv(FIG / "clf_error_by_deposit.csv")
    print("\nBy market segment:\n", seg.to_string()); print("\nBy deposit type:\n", dep.to_string())
    print("\n", classification_report(y_te, pred, target_names=["Kept", "Cancelled"]))

    joblib.dump(hgb, MODELS / "hotel_cancellation_hgb.joblib", compress=3)
    print("saved model ->", MODELS / "hotel_cancellation_hgb.joblib")


if __name__ == "__main__":
    main()
