# Hotel Booking Cancellation Prediction

## Project Overview

This project uses machine learning classification algorithms to predict whether a hotel booking will be canceled. The goal is to identify booking patterns associated with cancellations and evaluate how well different classification models can distinguish between canceled and non-canceled reservations.

This project is part of my Data Analytics and Machine Learning portfolio, applying Python, data preprocessing, feature engineering, and model evaluation to a real-world hotel booking dataset.

## Objectives

- Prepare and validate a cleaned hotel booking dataset for machine learning.
- Explore the target variable and understand the distribution of canceled and non-canceled bookings.
- Separate the features from the target variable.
- Apply preprocessing techniques to numerical and categorical features.
- Train and compare multiple classification algorithms.
- Evaluate model performance using accuracy, precision, recall, F1-score, and classification reports.
- Identify the strengths and limitations of the models in predicting booking cancellations.

## Dataset

The project uses the Hotel Booking Demand dataset, which contains hotel reservations from a city hotel and a resort hotel.

The cleaned dataset used for this project contains **86,637 booking records**.

| Item | Description |
|---|---|
| Dataset | Hotel Booking Demand |
| Records | 86,637 |
| Target variable | `is_canceled` |
| Problem type | Binary classification |
| Class 0 | Booking not canceled |
| Class 1 | Booking canceled |

### Target Variable Distribution

The target variable `is_canceled` indicates whether a reservation was canceled.

| Booking status | Records | Percentage |
|---|---:|---:|
| Not Canceled (0) | 62,652 | 72.32% |
| Canceled (1) | 23,985 | 27.68% |
| **Total** | **86,637** | **100%** |

The dataset has an imbalanced target distribution because non-canceled bookings are more common than canceled bookings. Therefore, model evaluation considers precision, recall, and F1-score in addition to accuracy.

## Project Structure

```text
classification/
├── README.md
├── notebooks/
│   └── 01_classification.ipynb
└── reports/
    └── figures/
```

The cleaned dataset is stored in the shared data directory of the main repository.

```text
data/
└── processed/
    └── hotel_bookings_clean.csv
```

## Tools and Libraries

- **Python** — data preparation and machine learning
- **Pandas** — data manipulation and analysis
- **NumPy** — numerical operations
- **Matplotlib and Seaborn** — data visualization
- **Scikit-learn** — preprocessing, model training, and evaluation
- **Jupyter Notebook** — interactive analysis and documentation
- **Git and GitHub** — version control and project collaboration

## Data Preparation

The raw dataset was cleaned before being used for machine learning. The preparation process included:

1. Removing duplicate records and rows that violated the selected data-quality rules.
2. Handling missing values in relevant columns.
3. Standardizing categorical values where necessary.
4. Checking numerical values and applying appropriate validation rules.
5. Creating additional features to represent booking characteristics.
6. Removing columns that could reveal the final booking outcome or would not be available at the intended prediction time.
7. Saving the cleaned dataset for reuse in the machine learning workflow.

### Feature Engineering

Additional features were created to provide more information about each booking.

| Feature | Description |
|---|---|
| `total_nights` | Total weekend and weekday nights booked |
| `total_guests` | Total adults, children, and babies |
| `has_kids` | Indicates whether children or babies are included |
| `arrival_month` | Month of arrival |
| `arrival_weekday` | Day of the week of arrival |
| `adr_per_guest` | Average daily rate divided by the number of guests, subject to the project's calculation rules |
| `has_agent` | Indicates whether an agent is associated with the booking |
| `has_company` | Indicates whether a company is associated with the booking |
| `has_prev_cancel` | Indicates whether the booking record contains previous cancellations |

### Preventing Target Leakage

To avoid giving the model information about the final booking outcome, the following columns were excluded from the cleaned dataset:

- `reservation_status`
- `reservation_status_date`
- `assigned_room_type`

These columns may contain information that is unavailable when predicting cancellation at the time of booking.

The target variable, `is_canceled`, is kept separately from the input features during model training.

## Machine Learning Workflow

### 1. Feature and Target Separation

The target variable is `is_canceled`, while the remaining eligible columns are used as input features.

### 2. Train-Test Split

The dataset is divided into training and testing sets using an 80:20 split.

- **Training set:** 69,309 records
- **Testing set:** 17,328 records
- **Random state:** 42
- **Stratification:** Enabled to preserve the approximate class distribution

### 3. Preprocessing

The features are divided into numerical and categorical columns.

**Numerical preprocessing**
- Identify numerical features.
- Apply the selected numerical preprocessing steps.

**Categorical preprocessing**
- Identify categorical features.
- Encode categorical variables so they can be used by machine learning algorithms.

The preprocessing transformations are fitted on the training data and applied to the test data to help prevent data leakage.

### 4. Classification Models

Five classification algorithms are trained and evaluated.

| Model | Purpose |
|---|---|
| Logistic Regression | Provides a linear classification baseline |
| Decision Tree | Learns decision rules from the input features |
| Random Forest | Combines multiple decision trees |
