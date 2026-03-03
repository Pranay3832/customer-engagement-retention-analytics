📊 Customer Engagement & Product Utilization Analytics for Retention Strategy
🏦 Behavioral Retention Intelligence System for European Banking
📌 Project Overview

Customer churn remains one of the most critical challenges in retail banking. Traditional retention strategies often rely on financial strength indicators such as balance or salary. However, behavioral engagement and product utilization depth may be stronger predictors of long-term loyalty.

This project reframes churn analysis from a behavioral and relationship-strength perspective, integrating KPI engineering, predictive modeling, explainable AI, and an interactive decision-support dashboard.

The study uses a dataset of 10,000 European bank customers to develop an engagement-driven retention intelligence framework.

🎯 Project Objectives
Primary Objectives

Evaluate the relationship between engagement and churn

Measure retention impact of product depth

Identify disengaged yet high-value customers

Secondary Objectives

Engineer engagement-based KPIs

Build a Relationship Strength Index (RSI)

Develop churn probability scoring model

Provide explainable AI insights using SHAP

📂 Repository Structure
customer-engagement-retention-analytics/
│
├── data/
│   └── European_Bank.csv
│
├── notebooks/
│   └── 01_EDA_and_KPI_Analysis.ipynb
│
├── app/
│   └── streamlit_app.py
│
├── reports/
│   ├── Customer_Engagement_Retention_Merged_Final_Research_Paper.docx
│
├── images/
│   └── dashboard_preview.png
│
├── requirements.txt
├── README.md
└── .gitignore
📊 Dataset Description

The dataset includes 10,000 retail banking customers with the following attributes:

CreditScore

Geography (France, Spain, Germany)

Gender

Age

Tenure

Balance

NumOfProducts

HasCrCard

IsActiveMember

EstimatedSalary

Exited (Churn Indicator)

Target variable:

Exited = 1 → Customer churned
Exited = 0 → Customer retained
🧠 Key KPIs Developed
1️⃣ Engagement Retention Ratio

Compares churn rate between active and inactive customers.

2️⃣ Product Depth Index

Measures churn variation across product count tiers.

3️⃣ High-Balance Disengagement Rate

Identifies premium customers at silent churn risk.

4️⃣ Credit Card Stickiness Score

Measures retention impact of card ownership.

5️⃣ Relationship Strength Index (RSI)

Composite loyalty score calculated using:

Activity Status (30%)

Product Depth (30%)

Tenure (30%)

Credit Card Ownership (10%)

Customers classified into:

Weak

Moderate

Strong

📈 Exploratory Data Analysis Findings

Overall Churn Rate: 20.37%

Inactive Customer Churn: 26.85%

Active Customer Churn: 14.27%

Premium Inactive Churn: 30.47%

Key Insight:

Engagement level is a stronger predictor of churn than financial strength alone.

🤖 Predictive Modeling

A Logistic Regression model was implemented using:

CreditScore

Age

Tenure

Balance

NumOfProducts

HasCrCard

IsActiveMember

EstimatedSalary

Model Performance

Accuracy: 80.95%

ROC-AUC Score: 0.756

Confusion Matrix:

	Predicted 0	Predicted 1
Actual 0	1559	48
Actual 1	333	60
🧠 Explainable AI (SHAP)

SHAP (SHapley Additive exPlanations) was used to:

Identify top churn-driving features

Explain individual customer churn probability

Quantify behavioral vs financial influence

Key finding:

Behavioral engagement variables showed stronger predictive contribution than salary indicators.

💻 Streamlit Dashboard Features

The interactive dashboard includes:

📊 Executive KPI Panel

📦 Product Utilization Impact Analysis

🔗 Relationship Strength Distribution

💰 Premium Risk Detection

🚨 Customer Risk Ranking Table

📥 Downloadable Risk Report

🤖 Real-Time Churn Probability Scoring

Run locally:

streamlit run app/streamlit_app.py
🚀 Business Impact

This framework enables banks to:

Shift from reactive churn management to proactive retention intelligence

Target disengaged premium customers

Improve cross-sell strategy for single-product users

Optimize loyalty program segmentation

Enhance marketing ROI through risk prioritization

📄 Research Paper

The complete academic-style research paper includes:

Literature context

Methodology

KPI framework

Empirical results

Model evaluation

APA references

Charts and tables

Located in:

/reports/Customer_Engagement_Retention_Merged_Final_Research_Paper.docx
🛠 Tools & Technologies

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

SHAP

Streamlit

Jupyter Notebook

🎓 Skills Demonstrated

Advanced Exploratory Data Analysis

KPI Engineering

Behavioral Segmentation

Predictive Modeling

Explainable AI

Dashboard Development

Research Documentation

Business Insight Generation

📌 How to Run

Clone repository

git clone https://github.com/yourusername/customer-engagement-retention-analytics.git

Install dependencies

pip install -r requirements.txt

Run Streamlit

streamlit run app/streamlit_app.py
🏆 Author

Pranay Kudale
Behavioral Retention Analytics Consultant
2026

📜 License

This project is for educational and portfolio purposes.

⭐ Final Note

This project demonstrates how engagement-driven analytics combined with predictive modeling and explainable AI can transform customer retention strategy in modern banking environments.
