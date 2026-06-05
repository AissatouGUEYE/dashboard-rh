import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard RH",
    layout="wide"
)

st.title("📊 Dashboard RH – GOLD DATA")

st.write("""
Bienvenue dans le tableau de bord RH.  
Utilisez le menu à gauche pour naviguer entre les vues.
""")

df = pd.read_csv("data/GOLD_DATA.csv")

st.dataframe(df.head())
