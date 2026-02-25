# sme-credibility-scoring-api
SME Credibility Scoring System (API)

 Project Overview

This project builds a machine learning–powered credibility scoring system for Small and Medium Enterprises (SMEs).

The goal is to objectively assess SME financial credibility using structured financial indicators such as revenue, expenses, debt status, reporting consistency, and revenue growth.

The model predicts:

Credibility probability score (0–100)

Binary classification (Credible / Not Credible)

Problem Statement

Many SMEs struggle to access funding due to a lack of standardized financial credibility assessment.

This system provides a data-driven credibility scoring mechanism to support investor and lending decisions.

Tech Stack

Python

Scikit-learn

FastAPI

NumPy

Joblib

Excel (for data cleaning & feature engineering)

Data Preparation

Data was collected via a structured survey (Google Forms).

Cleaning and manipulation were performed in Microsoft Excel:

Removed incomplete entries

Converted financial values to numeric

Created derived features (revenue growth, consistency score)

Engineered target variable using financial rules

Final dataset size: < 40 SMEs

 Model Details

Model Type: Logistic Regression

Preprocessing: StandardScaler (inside sklearn Pipeline)

Validation Method: 5-Fold Cross Validation

Mean ROC-AUC: 0.95

Threshold: 0.5

 Cross-Validation Results

ROC-AUC Scores per Fold:

[1.00, 0.94, 1.00, 1.00, 0.80]

Mean ROC-AUC:

0.9489

Input Schema

The API expects the following JSON:

{
  "revenue": 5000000,
  "expenses": 4000000,
  "debt": 500000,
  "revenue_growth": 0.1,
  "reporting_consistency": 1,
  "impact_score": 0.7
}
 Output Schema
{
  "credibility_score": 87.45,
  "credible_class": 1
}

Where:

credibility_score = predicted probability × 100

credible_class = 1 if probability ≥ 0.5 else 0

 Running Locally

Clone repository:

git clone https://github.com/yourusername/sme-credibility-scoring-api.git
cd sme-credibility-scoring-api

Install dependencies:

pip install -r requirements.txt

Run API:

uvicorn main:app --reload

API will run at:

http://127.0.0.1:8000
 Project Structure
sme-credibility-scoring-api/
│
├── credibility_model.pkl
├── main.py
├── requirements.txt
└── README.md
 Limitations

Small dataset (< 40 samples)

Self-reported financial data

Requires retraining as the dataset grows

 Future Improvements

Larger dataset collection

Explainability using SHAP

Model retraining pipeline

Cloud deployment

Drift monitoring

