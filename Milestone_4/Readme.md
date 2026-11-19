# Milestone 4: Sentiment Analysis from Classic NLP to LLMs

> **Question:** When is a simple model good enough, and when does an LLM earn its cost?

**Author:** `<your name>` · **Course:** `<course name>` · **Date:** `<date>`

This project classifies **GitHub pull-request and commit comments** (software-engineering text) as
*positive*, *negative* or *neutral* with three approaches, then compares them on accuracy, macro-F1,
robustness on hard sentences, speed and cost.

---

## 1. Approaches

| Tier | Approach | Training? | Tools | Notebook |
|---|---|---|---|---|
| 1 | Rule-based: word-score lexicon plus a few rules | None | VADER | `02_vader` |
| 2 | Classic ML: stemmed TF-IDF (words + word pairs) and Naive Bayes (Logistic Regression as an extra) | Yes, on the training split | NLTK, scikit-learn | `03_classic_ml` |
| 3 | LLM zero-shot: instructions only, no examples | None | Claude API | `04_llm` |

## 2. Dataset

**A gold standard for polarity of emotions of software developers in GitHub** (`github_gold.csv`)
Novielli, Calefato, Dongiovanni, Girardi, Lanubile (2020). Source: <https://doi.org/10.6084/m9.figshare.11604597>

| Item | Value |
|---|---|
| Rows | over 7,000 pull-request and commit comments (exact count after cleaning: `<fill in>`) |
| Labels | positive / negative / neutral (about 43% neutral, 28% positive, 29% negative according to the MSR 2020 paper; my counts: `<fill in>`) |
| License | `<read it on the figshare page and write it here>` |

**Why this dataset:** it is real engineering communication, where words such as "kill", "crash" or
"dead code" are technical vocabulary rather than emotion. General-purpose tools are known to struggle
with exactly this, which makes the comparison meaningful.

**Citation:** N. Novielli, F. Calefato, D. Dongiovanni, D. Girardi, F. Lanubile (2020). *Can We Use
SE-specific Sentiment Analysis Tools in a Cross-Platform Setting?* Proceedings of the 17th International
Conference on Mining Software Repositories (MSR 2020).

![Class balance](results/charts/class_balance.png)

## 3. Evaluation protocol

* **Fixed split.** Stratified train/test split with seed `42`, saved once to `data/train.csv` and
  `data/test300.csv`. Duplicate texts are removed before splitting.
* **One test subset.** Every model is scored on the same **300 stratified test examples**.
* **No peeking.** The test texts are not used for training, tuning, threshold choice or prompt writing.
  Naive Bayes `alpha` and Logistic Regression `C` are chosen by 5-fold cross-validation on the training data only.
* **Hard-cases set.** 30 sentences in `data/hard_cases.csv` covering technical jargon that sounds negative,
  negation, sarcasm, mixed sentiment and review-comment tone. `<state how many are your own, e.g. "14 written or selected by me">`.
* **Metrics.** Accuracy, **macro-F1 (main metric)**, confusion matrix per model, seconds per 1,000
  predictions, dollars per 1,000 predictions, hard-cases accuracy. A 95% bootstrap interval is reported for macro-F1.

## 4. Results

> Paste the table from `results/metrics.csv` (created by notebook 05).

| Model | Accuracy | Macro-F1 | Hard-cases acc. | Sec / 1k preds | Cost / 1k preds |
|---|---|---|---|---|---|
| VADER | | | | | $0 |
| NLTK + Naive Bayes | | | | | ~$0 |
| TF-IDF + Logistic Regression (extra) | | | | | ~$0 |
| LLM zero-shot (`<model name>`) | | | | | |

![Macro-F1 per model](results/charts/macro_f1.png)
![Hard-cases accuracy per model](results/charts/hard_cases_acc.png)
![Quality vs speed](results/charts/quality_vs_speed.png)
![Confusion matrices](results/charts/confusion_matrices.png)

### Key findings
1. `<Which model has the best macro-F1, and is the gap larger than the confidence interval?>`
2. `<Which tier is best on the hard cases, and in which categories do the others fail?>`
3. `<What does each tier cost in speed and money, and what does that mean at 1,000,000 predictions?>`

## 5. Error analysis (summary)

`<3-5 sentences: which class is hardest for each model, two or three concrete mistakes with the reason,
and what the texts that every model gets wrong have in common. The full analysis is in the report.>`

## 6. Conclusion: which model, and when?

`<Your recommendation in a short paragraph. Mention the conditions: labelled data available, prediction
volume, latency limit, budget, and privacy (can the text be sent to an external API?). Say when you would
switch to a different tier.>`

## 7. Repository layout

```
README.md
requirements.txt
prompts.md              prompts used for the LLM (read by the code, so it is always in sync)
data/
  README.md             dataset notes, license, citation
  hard_cases.csv        the 30-sentence hard set
  raw/                  downloaded dataset (not committed)
  train.csv, test300.csv   fixed splits, created once by notebook 01
notebooks/              01_data, 02_vader, 03_classic_ml, 04_llm, 05_compare
src/
  config.py             all settings (seed, paths, model name, prices)
  utils.py              data loading, splits, preprocessing, metrics, plots
  llm.py                Claude API calls, cache, token and cost tracking
  download_data.py      downloads the dataset from figshare
  make_demo_data.py     synthetic data for checking the setup only
results/                metrics.csv, charts/, preds/, run_stats.json, llm_cache.jsonl
report/                 report_template.md  (final report: report.pdf)
```

## 8. How to run

1. **Environment** (Python 3.10+):
   ```bash
   python -m venv .venv
   source .venv/bin/activate          # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. **Data:**
   ```bash
   python -m src.download_data
   ```
   This saves the dataset to `data/raw/dataset.csv`. If it fails, download the file from the DOI link above
   and save it under that name. The loader detects the text and label columns automatically; check the
   line "columns used" printed by notebook 01. Column names, label mapping and file options can be set in `src/config.py`.
3. **LLM settings.** Store your key in an environment variable (never in code or in git):
   ```bash
   export ANTHROPIC_API_KEY="..."     # Windows PowerShell: $env:ANTHROPIC_API_KEY="..."
   ```
   Then set `LLM_MODEL`, `PRICE_PER_MTOK_INPUT` and `PRICE_PER_MTOK_OUTPUT` in `src/config.py`, using the
   current values from Anthropic's documentation.
4. **Run the notebooks in order** (`jupyter lab`, open `notebooks/`):
   `01_data` → `02_vader` → `03_classic_ml` → `04_llm` → `05_compare`.
   Notebook 05 writes `results/metrics.csv` and the charts in `results/charts/`.

## 9. Reproducibility notes

* Seed, split sizes and the model name live in `src/config.py`.
* The splits are created once and reused; delete `data/train.csv` and `data/test300.csv` only if you want to start over.
* Every LLM answer is cached in `results/llm_cache.jsonl`, so re-running notebook 04 costs nothing and gives
  identical answers. Latency and token counts in the table come from the original live calls.
* Prompts are stored in `prompts.md`, with an iteration log.

## 10. Limitations

* 300 test examples give wide confidence intervals, so small differences between models are not conclusive.
* Labels were assigned by human annotators and contain some noise and subjectivity.
* One dataset, one LLM and one prompt style; results may differ on other platforms (e.g. Stack Overflow or Jira) or with few-shot prompts.
* The hard-cases set is small and hand-picked, so its scores show patterns rather than precise accuracy.
* LLM speed and cost depend on the model, the prompt length, network conditions and current pricing.

## 11. References

* Novielli, N., Calefato, F., Dongiovanni, D., Girardi, D., Lanubile, F. (2020). Can We Use SE-specific Sentiment Analysis Tools in a Cross-Platform Setting? *MSR 2020*.
* Novielli et al. (2020). A gold standard for polarity of emotions of software developers in GitHub. figshare. <https://doi.org/10.6084/m9.figshare.11604597>
* Hutto, C. J., Gilbert, E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. *ICWSM*.
* Bird, S., Klein, E., Loper, E. (2009). *Natural Language Processing with Python* (NLTK). O'Reilly.
* Pedregosa et al. (2011). Scikit-learn: Machine Learning in Python. *JMLR* 12.
* Anthropic. Claude API documentation. <https://docs.claude.com>

*AI-assistance statement (if your course requires one): `<describe how you used AI tools, e.g. help drafting code, which parts you wrote and verified yourself>`.*
