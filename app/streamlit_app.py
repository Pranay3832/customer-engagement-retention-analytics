import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import shap
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Retention Intelligence Dashboard", layout="wide")

# ---------------- LOAD DATA ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "European_Bank.csv")
df = pd.read_csv(DATA_PATH)

st.title("🏦 Customer Retention Intelligence Dashboard")

# ---------------- SIDEBAR ----------------
st.sidebar.header("Filter Controls")

geo_filter = st.sidebar.multiselect(
    "Select Geography",
    df["Geography"].unique(),
    default=df["Geography"].unique()
)

min_products = st.sidebar.slider(
    "Minimum Products",
    1,
    int(df["NumOfProducts"].max()),
    1
)

df_filtered = df[
    (df["Geography"].isin(geo_filter)) &
    (df["NumOfProducts"] >= min_products)
]

# ---------------- KPI SECTION ----------------
st.subheader("📊 Key Retention Metrics")

col1, col2, col3, col4 = st.columns(4)

churn_rate = df_filtered["Exited"].mean()
active_churn = df_filtered[df_filtered["IsActiveMember"] == 1]["Exited"].mean()
inactive_churn = df_filtered[df_filtered["IsActiveMember"] == 0]["Exited"].mean()
multi_product_rate = df_filtered[df_filtered["NumOfProducts"] >= 2]["Exited"].mean()

col1.metric("Overall Churn Rate", f"{churn_rate:.2%}")
col2.metric("Active Customer Churn", f"{active_churn:.2%}")
col3.metric("Inactive Customer Churn", f"{inactive_churn:.2%}")
col4.metric("Multi-Product Churn", f"{multi_product_rate:.2%}")

st.markdown("---")

# ---------------- ADVANCED VISUALS ----------------
st.subheader("📈 Churn by Product Count")

fig1, ax1 = plt.subplots()
sns.barplot(x="NumOfProducts", y="Exited", data=df_filtered, ax=ax1)
ax1.set_title("Churn Rate by Number of Products")
st.pyplot(fig1)

st.subheader("📍 Geography vs Churn")

fig2, ax2 = plt.subplots()
sns.barplot(x="Geography", y="Exited", data=df_filtered, ax=ax2)
ax2.set_title("Churn Rate by Geography")
st.pyplot(fig2)

st.markdown("---")

# ---------------- RELATIONSHIP STRENGTH INDEX ----------------
st.subheader("🔗 Relationship Strength Index")

df_filtered["Tenure_norm"] = df_filtered["Tenure"] / df_filtered["Tenure"].max()
df_filtered["Product_norm"] = df_filtered["NumOfProducts"] / df_filtered["NumOfProducts"].max()

df_filtered["RSI"] = (
    df_filtered["IsActiveMember"] * 0.3 +
    df_filtered["Product_norm"] * 0.3 +
    df_filtered["HasCrCard"] * 0.1 +
    df_filtered["Tenure_norm"] * 0.3
) * 100

st.metric("Average Relationship Strength Score", f"{df_filtered['RSI'].mean():.2f}")

fig3, ax3 = plt.subplots()
sns.histplot(df_filtered["RSI"], kde=True, ax=ax3)
ax3.set_title("Distribution of Relationship Strength Index")
st.pyplot(fig3)

st.markdown("---")

# ---------------- MACHINE LEARNING MODEL ----------------
st.subheader("🤖 Churn Prediction Model (Logistic Regression)")

features = [
    "CreditScore", "Age", "Tenure",
    "Balance", "NumOfProducts",
    "HasCrCard", "IsActiveMember", "EstimatedSalary"
]

X = df[features]
y = df["Exited"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
roc = roc_auc_score(y_test, model.predict_proba(X_test_scaled)[:, 1])

colA, colB = st.columns(2)
colA.metric("Model Accuracy", f"{accuracy:.2%}")
colB.metric("ROC-AUC Score", f"{roc:.2f}")

st.write("### Feature Importance")

importance = pd.DataFrame({
    "Feature": features,
    "Coefficient": model.coef_[0]
}).sort_values(by="Coefficient", ascending=False)

st.dataframe(importance)

# Predict probabilities for all customers
df["Churn_Probability"] = model.predict_proba(
    scaler.transform(df[features])
)[:, 1]

def risk_category(prob):
    if prob < 0.3:
        return "Low Risk"
    elif prob < 0.6:
        return "Medium Risk"
    else:
        return "High Risk"

df["Risk_Level"] = df["Churn_Probability"].apply(risk_category)

st.subheader("🚨 Customer Risk Ranking")

top_risk = df.sort_values(by="Churn_Probability", ascending=False).head(20)

st.dataframe(
    top_risk[
        ["CustomerId", "Geography", "Balance",
         "NumOfProducts", "IsActiveMember",
         "Churn_Probability", "Risk_Level"]
    ]
)

st.subheader("⬇ Download Risk Report")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Full Risk Report (CSV)",
    data=csv,
    file_name="Customer_Risk_Report.csv",
    mime="text/csv"
)


st.subheader("🧠 SHAP Model Explanation")

explainer = shap.LinearExplainer(model, X_train_scaled)
shap_values = explainer.shap_values(X_test_scaled)

fig_shap = plt.figure()
shap.summary_plot(shap_values, X_test, show=False)
st.pyplot(fig_shap)