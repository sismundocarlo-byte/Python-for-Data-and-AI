"""Build the ML-ready dataset from the raw hotel bookings file.

Only *rule-based* cleaning happens here (constant fills, dropping impossible
rows, feature construction). Nothing is learned from the data, so doing this
before the train/test split cannot leak information. Scaling and encoding are
done later inside the sklearn Pipeline, fitted on the training split only.

Run:  python src/prepare_data.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "hotel_bookings.csv"
OUT = ROOT / "data" / "processed" / "hotel_bookings_clean.csv"

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], start=1)}

# Columns that reveal the outcome or only exist after it is known -> leakage.
LEAKY = ["reservation_status", "reservation_status_date", "assigned_room_type"]


def prepare(raw_path=RAW):
    df = pd.read_csv(raw_path)
    log = {"raw_rows": len(df)}

    # 1. Remove exact duplicate bookings (would otherwise sit in both train and test)
    df = df.drop_duplicates()
    log["after_dedup"] = len(df)

    # 2. Drop leaky columns
    df = df.drop(columns=LEAKY)

    # 3. Missing values
    df["children"] = df["children"].fillna(0)
    df["country"] = df["country"].fillna("Unknown")
    df["has_agent"] = df["agent"].notna().astype(int)
    df["agent"] = df["agent"].fillna(0).astype(int).astype(str)       # '0' = no agent
    df["has_company"] = df["company"].notna().astype(int)             # 94% missing -> flag only
    df = df.drop(columns="company")

    # 4. Tidy categories ('Undefined' meal is documented as the same as SC = no meal package)
    df["meal"] = df["meal"].replace("Undefined", "SC")

    # 5. Remove impossible / extreme records
    guests = df["adults"] + df["children"] + df["babies"]
    nights = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]
    df = df[(guests > 0) & (nights > 0) & (df["adr"] >= 0) & (df["adr"] <= 1000)].copy()
    log["after_rule_filters"] = len(df)

    # 6. Feature engineering
    df["total_nights"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]
    df["total_guests"] = df["adults"] + df["children"] + df["babies"]
    df["has_kids"] = ((df["children"] + df["babies"]) > 0).astype(int)
    df["arrival_month"] = df["arrival_date_month"].map(MONTHS)
    arrival = pd.to_datetime(dict(year=df["arrival_date_year"], month=df["arrival_month"],
                                  day=df["arrival_date_day_of_month"]))
    df["arrival_weekday"] = arrival.dt.dayofweek
    df["adr_per_guest"] = df["adr"] / df["total_guests"]
    df["has_prev_cancel"] = (df["previous_cancellations"] > 0).astype(int)

    # arrival year/day dropped: year cannot generalise to the future, day-of-month is noise
    df = df.drop(columns=["arrival_date_year", "arrival_date_month", "arrival_date_day_of_month"])

    df = df.reset_index(drop=True)
    log["final_rows"] = len(df)
    log["final_cols"] = df.shape[1]
    return df, log


if __name__ == "__main__":
    clean, log = prepare()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    clean.to_csv(OUT, index=False)
    for k, v in log.items():
        print(f"{k:>20}: {v}")
    print("class balance:\n", clean["is_canceled"].value_counts(normalize=True).round(3))
    print("saved ->", OUT)
