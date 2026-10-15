# Classification: Hotel Booking Cancellation Prediction

## 1. Project Overview

Hotel cancellations can result in lost revenue, inefficient room allocation, and difficulties in planning hotel operations. This project applies supervised machine learning classification algorithms to predict whether a hotel booking will be cancelled based on information available at the time of booking.

The goal is to compare different classification models, evaluate their predictive performance, and identify how machine learning can support hotel revenue management and operational planning.

**Business question:** Given the information available when a reservation is made, can we predict whether the booking will be cancelled?

**Target variable:** `is_canceled`

- `0` — Booking was not cancelled.
- `1` — Booking was cancelled.

## 2. Dataset

**Dataset:** Hotel Booking Demand

**Original publication:** Antonio, Almeida, and Nunes (2019), *Hotel Booking Demand Datasets*, Data in Brief.

The dataset contains hotel booking records from a city hotel and a resort hotel in Portugal, covering 2015–2017.

| Attribute | Description |
|---|---|
| Original dataset | 119,390 rows × 32 columns |
| Cleaned dataset | 86,637 rows × 34 columns |
| Target variable | `is_canceled` |
| Cancellation rate | Approximately 27.7% |
| Prediction task | Binary classification |

**Data source and licensing:** The dataset is commonly distributed through Kaggle. Verify the licence and attribution requirements of the exact source from which the dataset was downloaded before redistributing the data.

## 3. Data Preparation

The original dataset was cleaned and transformed before model training.

### Cleaning and preprocessing

- Removed 31,994 duplicate records.
- Removed 759 invalid or implausible records, including bookings with zero guests, zero nights, or negative/extreme average daily rates.
- Removed `reservation_status`, `reservation_status_date`, and `assigned_room_type` to reduce target leakage and avoid using information unavailable at prediction time.
- Handled missing values in `children`, `country`, and `agent`.
- Retained a missingness indicator for `company`, which has approximately 94% missing values.
- Added engineered features to improve the information available to the models.

The cleaned dataset contains 86,637 records and 34 columns.

**Important:** The feature engineering and preprocessing steps should be fitted using training data where appropriate to prevent data leakage into the test set.

## 4. Machine Learning Models

Four classification approaches were evaluated.

1. **Majority-Class Baseline** — Predicts the most frequent class and establishes a reference performance level.
2. **Logistic Regression** — A linear classification model used as an interpretable baseline.
3. **Random Forest** — An ensemble of decision trees that captures nonlinear relationships and feature interactions.
4. **Hist Gradient Boosting** — A boosting algorithm that builds trees sequentially to improve predictive performance.

Hyperparameter tuning was performed with a limited random-search budget to keep the computational requirements manageable on a single CPU.

## 5. Model Evaluation

Models were compared using five-fold cross-validation on the training set. Final metrics were calculated on a held-out test set of 17,328 bookings, which was used once for the final evaluation.

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Majority-Class Baseline | 0.723 | 0.000 | 0.000 | 0.000 | 0.500 |
| Logistic Regression (Tuned) | 0.758 | 0.543 | 0.795 | 0.646 | 0.850 |
| **Random Forest (Tuned)** | **0.825** | 0.649 | **0.803** | **0.718** | 0.906 |
| Hist Gradient
