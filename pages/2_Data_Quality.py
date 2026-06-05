import streamlit as st
import pandas as pd

st.title("🧹 Vue Data Quality")

df = pd.read_csv("data/GOLD_DATA.csv")

st.subheader("📌 Valeurs manquantes")
st.write(df.isna().sum())

st.subheader("📌 Doublons")
st.write(df.duplicated().sum())

st.subheader("📌 Types de variables")
st.write(df.dtypes)

st.subheader("📌 Score qualité (simple)")
missing_score = 1 - (df.isna().sum().sum() / (df.shape[0] * df.shape[1]))
st.metric("Score qualité global", f"{round(missing_score*100,2)} %")
