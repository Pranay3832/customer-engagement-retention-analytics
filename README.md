# 📊 Customer Engagement & Product Utilization Analytics for Retention Strategy

## 🏦 Behavioral Retention Intelligence System for European Banking

---

## 📌 Project Overview

Customer churn remains one of the most critical challenges in retail banking. Traditional retention strategies often rely on financial strength indicators such as balance or salary. However, behavioral engagement and product utilization depth may be stronger predictors of long-term loyalty.

This project reframes churn analysis from a behavioral and relationship-strength perspective, integrating KPI engineering, predictive modeling, explainable AI, and an interactive decision-support dashboard.

The study uses a dataset of 10,000 European bank customers to develop an engagement-driven retention intelligence framework.

---

## 🎯 Project Objectives

### Primary Objectives
- Evaluate the relationship between engagement and churn
- Measure retention impact of product depth
- Identify disengaged yet high-value customers

### Secondary Objectives
- Engineer engagement-based KPIs
- Build a Relationship Strength Index (RSI)
- Develop churn probability scoring model
- Provide explainable AI insights using SHAP

---

## 📂 Repository Structure

customer-engagement-retention-analytics\
│
├── data/
│   └── European_Bank.csv
│
├── notebooks\
│   └── 01_EDA_and_KPI_Analysis.ipynb
│
├── app\
│   └── streamlit_app.py
│
├── reports\
│   └── Customer_Engagement_Retention_Merged_Final_Research_Paper.docx
│
├── images\
│   └── dashboard_preview.png
│
├── requirements.txt
├── README.md
└── .gitignore

---

## 📊 Dataset Description

The dataset includes 10,000 retail banking customers with attributes such as CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, and Exited (Churn Indicator).

Exited = 1 → Customer churned  
Exited = 0 → Customer retained

---

## 🧠 Key KPIs Developed

1. Engagement Retention Ratio  
2. Product Depth Index  
3. High-Balance Disengagement Rate  
4. Credit Card Stickiness Score  
5. Relationship Strength Index (RSI)

RSI Components:
- Activity Status (30%)
- Product Depth (30%)
- Tenure (30%)
- Credit Card Ownership (10%)

---

## 📈 Empirical Findings

- Overall Churn Rate: 20.37%
- Inactive Customer Churn: 26.85%
- Active Customer Churn: 14.27%
- Premium Inactive Churn: 30.47%

Model Performance:
- Accuracy: 80.95%
- ROC-AUC Score: 0.756

---

## 🤖 Predictive Modeling & Explainability

Logistic Regression model implemented using financial and behavioral predictors.

SHAP (SHapley Additive exPlanations) used to:
- Identify top churn-driving features
- Explain individual churn probabilities
- Quantify behavioral vs financial influence

---

## 💻 Streamlit Dashboard Features

- Executive KPI Panel
- Product Utilization Impact Analysis
- Relationship Strength Distribution
- Premium Risk Detection
- Customer Risk Ranking Table
- Downloadable Risk Report
- Real-Time Churn Probability Scoring

Run locally:

streamlit run app/streamlit_app.py

---

## 🛠 Tools & Technologies

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, SHAP, Streamlit, Jupyter Notebook

---

## 🏆 Skills Demonstrated

- Advanced EDA
- KPI Engineering
- Behavioral Segmentation
- Predictive Modeling
- Explainable AI
- Dashboard Development
- Research Documentation
- Business Insight Generation

---

## 📌 How to Run

1. Clone repository  
git clone https://github.com/yourusername/customer-engagement-retention-analytics.git

2. Install dependencies  
pip install -r requirements.txt

3. Run Streamlit  
streamlit run app/streamlit_app.py

---

## 👤 Author

Pranay Kudale  
Behavioral Retention Analytics Consultant  
2026

---

⭐ This project demonstrates how engagement-driven analytics combined with predictive modeling and explainable AI can transform customer retention strategy in modern banking environments.
