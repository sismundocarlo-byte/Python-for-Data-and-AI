# Milestone 3: Machine Learning Project

## Overview

This project explores different machine learning approaches using real-world datasets to solve business problems and generate actionable insights.

The objective is to develop, evaluate, and compare machine learning models across three major categories: classification, regression, and clustering.

Each category addresses a different analytical problem, using appropriate algorithms, evaluation metrics, and business interpretations.

## Machine Learning Projects

### 1. Classification — Hotel Booking Cancellation Prediction

**Business problem:** Hotel cancellations can lead to lost revenue and inefficient room allocation. Can we predict whether a hotel booking will be cancelled?

- **Dataset:** Hotel Booking Demand
- **Target variable:** `is_canceled`
- **Models:** Logistic Regression, Random Forest, Hist Gradient Boosting
- **Best model by F1-score:** Random Forest (0.718)
- **Best ROC-AUC:** Hist Gradient Boosting (0.909)

[**Proceed to Classification →**](Classification/README.md)

### 2. Regression — To Be Developed

**Business problem:** Predict a continuous numerical outcome using booking or customer data.

- **Dataset:** Hotel Booking Demand
- **Potential target variable:** `adr` (Average Daily Rate)
- **Status:** Planned

[Proceed to Regression →](Regression/README.md)

### 3. Clustering — To Be Developed

**Business problem:** Identify distinct customer or guest segments based on their booking characteristics.

- **Dataset:** Hotel Booking Demand
- **Approach:** Unsupervised learning
- **Status:** Planned

[Proceed to Clustering →](Clustering/README.md)

## Project Objectives

- Apply data cleaning, preprocessing, and feature engineering.
- Train and compare multiple machine learning algorithms.
- Evaluate models using appropriate performance metrics.
- Interpret results in a business context.
- Document limitations and potential real-world applications.

## Technology Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook, and Git/GitHub.

## Repository Structure

- `Classification/` — Classification models and documentation.
- `Regression/` — Regression models and documentation.
- `Clustering/` — Clustering models and documentation.

## Author

Carlo Sismundo

Part of the Python for Data and AI learning portfolio.
