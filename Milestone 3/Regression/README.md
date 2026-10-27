# Ames Housing Price Prediction — Regression

## Project Overview

This project applies machine learning regression techniques to predict residential house sale prices using the Ames Housing dataset.

The project focuses on preparing housing data, exploring relationships between property characteristics and sale prices, preprocessing numerical and categorical features, training regression models, and evaluating their predictive performance.

The workflow compares a simple baseline model against Ridge Regression and Random Forest Regression to determine which approach provides more accurate house price predictions.

This project is part of my Data Analytics and Machine Learning portfolio, demonstrating practical skills in Python, exploratory data analysis, data preprocessing, model selection, and regression evaluation.

## Objectives

- Inspect and clean the Ames Housing dataset.
- Identify missing values, duplicate records, and potential numerical outliers.
- Explore the relationships between housing characteristics and sale prices.
- Prepare numerical and categorical features for machine learning.
- Establish a baseline for comparison.
- Train and tune Ridge Regression and Random Forest Regression models.
- Compare model performance using cross-validation and test-set evaluation.
- Analyze residuals and feature importance to better understand model behavior.

## Dataset

The project uses the **Ames Housing dataset**, which contains residential property characteristics and corresponding sale prices.

The target variable is `SalePrice`, representing the final sale price of each property.

| Item | Description |
|---|---|
| Dataset | Ames Housing |
| Prediction target | `SalePrice` |
| Problem type | Supervised learning — regression |
| Input features | Property characteristics and attributes |
| Target unit | Sale price in USD |
| Dataset file | `AmesHousing.csv` |

The dataset includes information about property size, quality, construction, basement area, garage characteristics, neighborhood-related attributes, and other housing features.

## Project Structure

The following is the intended organization for this regression project. Adjust the paths to match the actual files committed to the repository.

```text
regression/
├── README.md
├── notebooks/
│   └── ames_housing_regression.ipynb
├── data/
│   ├── AmesHousing.csv
│   └── Processed/
│       └── AmesHousing_cleaned.csv
└── reports/
    └── figures/
        └── Regression/
```

The original dataset, processed dataset, notebook, and generated figures should be stored in their appropriate locations. Large datasets can be kept outside GitHub when repository size or dataset licensing requires it.

## Tools and Libraries

- **Python** — data preparation and machine learning
- **Pandas** — data manipulation and analysis
- **NumPy** — numerical operations
- **Matplotlib** — exploratory visualizations and diagnostic plots
- **Scikit-learn** — preprocessing, model training, cross-validation, and evaluation
- **Jupyter Notebook** — interactive analysis and documentation
- **Git and GitHub** — version control and project collaboration

## Data Cleaning and Preparation

The notebook begins by loading the original dataset and inspecting its dimensions, column names, duplicate records, missing values, and sale price distribution.

The cleaning process includes:

1. Creating a separate copy of the original dataset.
2. Removing exact duplicate records.
3. Checking that `SalePrice` has no missing or non-positive values.
4. Replacing missing values in selected property-feature columns with `NoFeature` when the missing value represents the absence of that feature.
5. Treating `MS SubClass` as a categorical feature.
6. Inspecting potential outliers in selected numerical columns.
7. Checking for inconsistencies where the construction year occurs after the sale year.
8. Saving the cleaned dataset as `AmesHousing_cleaned.csv`.

Potential outliers are inspected rather than automatically removed. This preserves the opportunity to investigate unusual properties before deciding whether any observations should be excluded.

Missing values in the remaining numerical and categorical features are handled during model preprocessing.

## Exploratory Data Analysis

The notebook explores the distribution of house sale prices and the relationships between selected property characteristics and `SalePrice`.

### Visualizations

| Visualization | Purpose |
|---|---|
| Sale price distribution | Understand the spread of residential sale prices |
| Living area vs. sale price | Examine the relationship between above-ground living area and price |
| Median sale price by overall quality | Explore how overall property quality relates to sale price |
| Basement area vs. sale price | Investigate the relationship between basement size and price |
| Correlation heatmap | Examine relationships among selected numerical features |
| Residual plot | Identify prediction errors and potential model patterns |
| Random Forest feature importance | Identify features that contribute to the fitted model's predictions |

The exploratory analysis helps identify patterns in the data and provides context for interpreting the regression models.

## Feature Selection

The target variable and input features are separated before training.

- **Target (`y`):** `SalePrice`
- **Features (`X`):** The remaining eligible property characteristics

The columns `Order` and `PID` are excluded from the input features because they serve as record identifiers rather than meaningful property characteristics for this prediction task.

## Train-Test Split

The dataset is divided into training and testing sets using an 80:20 split.

| Setting | Value |
|---|---|
| Training proportion | 80% |
| Testing proportion | 20% |
| Random state | 42 |
| Cross-validation | 5-fold K-Fold |

The training data is used for model fitting, cross-validation, and hyperparameter tuning. The test set is reserved for evaluating the trained models on unseen observations.

## Data Preprocessing

The notebook uses Scikit-learn pipelines and a `ColumnTransformer` to handle numerical and categorical features.

### Numerical Features

For Ridge Regression:

- Missing values are imputed using the median.
- Features are standardized using `StandardScaler`.

For Random Forest Regression:

- Missing values are imputed using the median.
- Standardization is not applied because tree-based models generally do not require feature scaling.

### Categorical Features

- Missing values are replaced with the category `Missing`.
- `OneHotEncoder` converts categorical features into numerical representations.
- `handle_unknown="ignore"` allows the pipeline to handle categories that appear in the test set but were not observed during training.

The preprocessing steps are incorporated into model pipelines so that transformations are fitted on the training data within the cross-validation process.

## Regression Models

Three approaches are evaluated.

### 1. Median Baseline

A `DummyRegressor` using the median strategy predicts the median sale price from the training data for every observation.

This provides a simple benchmark to determine whether the machine learning models improve on a basic prediction strategy.

### 2. Ridge Regression

Ridge Regression is a linear regression model with L2 regularization. It helps model relationships between housing features and sale price while penalizing excessively large coefficients.

The notebook evaluates the following regularization strengths:

- `alpha = 1.0`
- `alpha = 10.0`

Numerical features are standardized, and categorical features are one-hot encoded within the preprocessing pipeline.

### 3. Random Forest Regression

Random Forest Regression combines predictions from multiple decision trees to capture nonlinear relationships and interactions between housing characteristics.

The notebook uses `GridSearchCV` to compare the following hyperparameter settings:

| Hyperparameter | Values tested |
|---|---|
| `n_estimators` | 40 |
| `max_depth` | `None`, 20 |
| `min_samples_leaf` | 1, 2 |
| `max_features` | 0.5, 1.0 |

The best configuration is selected using five-fold cross-validation and negative root mean squared error as the scoring metric.

## Model Evaluation

The models are compared using cross-validation on the training data and evaluated on the held-out test set.

### Evaluation Metrics

**Mean Absolute Error (MAE)**

Measures the average absolute difference between actual and predicted sale prices. It is expressed in the same currency unit as the target.

**Root Mean Squared Error (RMSE)**

Measures the square root of the average squared prediction errors. It penalizes larger errors more heavily than MAE.

**R² Score**

Measures how well the model explains the variation in sale prices relative to a mean-based reference. A higher value generally indicates better predictive performance on the evaluated dataset.

### Model Selection

The notebook compares the cross-validation RMSE of Ridge Regression and Random Forest Regression and selects the model with the lower average cross-validation RMSE.

The selected model is then evaluated on the test set using MAE, RMSE, and R².

The median baseline is also evaluated to measure the improvement achieved by the machine learning models.

## Results and Interpretation

The notebook generates the following outputs:

- Cross-validation RMSE comparison.
- Test-set MAE, RMSE, and R² comparison.
- Selected model based on cross-validation RMSE.
- RMSE improvement over the median baseline.
- Residual plot for the selected model.
- Top 15 Random Forest feature importances.

**Final performance metrics should be reported after running the notebook.** The results depend on the dataset and fitted models, so this README does not assume specific MAE, RMSE, or R² values.

### Residual Analysis

Residuals are calculated as:

`Residual = Actual Sale Price - Predicted Sale Price`

The residual plot helps assess whether errors are centered around zero, whether the model tends to overpredict or underpredict certain properties, and whether prediction errors show patterns across different predicted prices.

### Feature Importance

Random Forest feature importance is used to identify which encoded input features contribute most to the fitted forest's predictive decisions.

These importance values describe the fitted model and should not be interpreted as proof of causation.

## Key Learnings

This project provides practical experience with:

- Cleaning and validating a real-world tabular dataset.
- Understanding missing values and distinguishing absent property features from unknown values.
- Exploring numerical relationships and correlations.
- Preparing mixed numerical and categorical data.
- Building preprocessing and modeling pipelines.
- Establishing a baseline before evaluating more complex models.
- Applying cross-validation and hyperparameter tuning.
- Comparing regression models using multiple metrics.
- Interpreting residual plots and feature importance.
- Using a held-out test set to assess generalization.

## Limitations and Future Improvements

Potential next steps include:

- Report the final cross-validation and test-set metrics in the README.
- Explore additional regression algorithms, such as Gradient Boosting or other tree-based ensemble models.
- Expand the hyperparameter search while managing computational cost.
- Investigate the effects of skewed sale prices and consider target transformations where appropriate.
- Examine influential observations and potential outliers in greater detail.
- Compare feature importance with permutation importance or other interpretation techniques.
- Evaluate whether a chronological or grouped split is appropriate for the intended deployment scenario.
- Improve reproducibility by documenting the dataset source, version, and exact environment dependencies.

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Install the dependencies

```bash
pip install pandas numpy matplotlib scikit-learn jupyter
```

### 3. Check the dataset path

The current notebook uses a local Windows path to load `AmesHousing.csv`. Update the path to match the dataset location in your cloned repository or project folder before running it on another computer.

### 4. Run the notebook

Open `ames_housing_regression.ipynb` in Visual Studio Code or Jupyter Notebook and execute the cells in order.

The notebook will perform data inspection, cleaning, exploratory analysis, preprocessing, model training, hyperparameter tuning, and evaluation.

## Conclusion

This project demonstrates a complete regression workflow for estimating residential house sale prices using the Ames Housing dataset.

By comparing a median baseline, Ridge Regression, and Random Forest Regression, the project evaluates both a regularized linear approach and a nonlinear ensemble method. Cross-validation supports model selection, while test-set metrics, residual analysis, and feature importance provide additional insight into model performance.

The main objective is not simply to produce predictions, but to build a reproducible workflow and evaluate how effectively different regression methods estimate house prices on unseen data.
