import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📌 Vue Executive")

df = pd.read_csv("data/GOLD_DATA.csv")

# Renommage pour simplifier le code
df = df.rename(columns={
    "headcount_actual": "effectif_reel",
    "headcount_planned": "effectif_planifie",
    "voluntary_leavers": "depart_volontaire"
})

# KPI
col1, col2, col3 = st.columns(3)
col1.metric("Effectif réel total", df["effectif_reel"].sum())
col2.metric("Effectif planifié total", df["effectif_planifie"].sum())
col3.metric("Départs volontaires (%)", round(df["depart_volontaire"].mean()*100, 2))

# Effectif réel vs planifié par site
fig = px.bar(
    df.groupby("site")[["effectif_reel","effectif_planifie"]].sum().reset_index(),
    x="site",
    y=["effectif_reel","effectif_planifie"],
    barmode="group",
    title="Effectif réel vs planifié par site"
)
st.plotly_chart(fig, use_container_width=True)

# Tension RH = écart
df["tension"] = df["effectif_planifie"] - df["effectif_reel"]
fig2 = px.bar(df, x="site", y="tension", title="Tension RH par site")
st.plotly_chart(fig2, use_container_width=True)
