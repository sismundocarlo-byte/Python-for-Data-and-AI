# Hotel Booking Cancellation - ML Group Project

## Problem statement
Hotels lose revenue when guests cancel. **Classification question:** given what is known when a booking is made, will it be cancelled (`is_canceled`)? Predictions can drive overbooking and deposit policies.
(Regression and clustering parts are planned on the same cleaned dataset, e.g. regress `adr`, cluster guest profiles.)

## Dataset
Hotel Booking Demand (Antonio, Almeida & Nunes, 2019, *Data in Brief*), City Hotel + Resort Hotel in Portugal, 2015-2017; commonly distributed on Kaggle. 119,390 rows, 32 columns. Check the licence on the source page you downloaded from and cite it in your report.

**Cleaned version** `data/processed/hotel_bookings_clean.csv`: 86,637 rows x 34 columns, 27.7% cancelled. Steps: removed 31,994 duplicates, 759 impossible rows (0 guests, 0 nights, negative/extreme `adr`); dropped leaky columns (`reservation_status`, `reservation_status_date`, `assigned_room_type`); filled missing `children`/`country`/`agent`; flagged `company` (94% missing); added engineered features.

## Results (held-out test set, 17,328 bookings)
| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Baseline (majority class) | 0.723 | 0.000 | 0.000 | 0.000 | 0.500 |
| Logistic Regression (tuned) | 0.758 | 0.543 | 0.795 | 0.646 | 0.850 |
| **Random Forest (tuned)** | 0.825 | 0.649 | 0.803 | **0.718** | 0.906 |
| Hist Gradient Boosting (tuned) | 0.842 | 0.740 | 0.661 | 0.698 | 0.909 |

Models were compared with 5-fold CV on the training set (Random Forest also led there, F1 0.715 tuned); the test set was used once. Regression and clustering rows: _to be added_.

## Limitations
- Random (not time-based) split; a real deployment would be tested on later months.
- `country`/`agent` act partly like identifiers; `Non Refund` bookings cancel 96% of the time, a quirk of this data.
- Tuning was light (few random-search iterations) to run on one CPU.
- Not for automatically penalising or refusing individual guests; use for aggregate planning only.

## How to run
```bash
pip install -r requirements.txt
python src/prepare_data.py            # builds data/processed/hotel_bookings_clean.csv
python src/train_classification.py    # CV, tuning, test metrics, figures in reports/, model in models/
# or open notebooks/02_classification.ipynb and run all cells
```
Random seed is fixed at 42. Training takes roughly 8 minutes on one CPU.
