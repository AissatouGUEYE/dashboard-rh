import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Vue RH Analytics")

df = pd.read_csv("data/GOLD_DATA.csv")

# Renommage utile
df = df.rename(columns={
    "voluntary_leavers": "depart_volontaire",
    "critical_skill_coverage_rate": "couverture_competence",
    "headcount_gap": "ecart_effectif"
})

# Rotation volontaire par équipe
fig = px.bar(
    df.groupby("team_id")["depart_volontaire"].mean().reset_index(),
    x="team_id",
    y="depart_volontaire",
    title="Rotation volontaire par équipe"
)
st.plotly_chart(fig, use_container_width=True)

# Écarts d’effectifs
fig2 = px.bar(df, x="team_id", y="ecart_effectif", title="Écarts d’effectifs")
st.plotly_chart(fig2, use_container_width=True)

# Couverture compétences critiques
fig3 = px.box(df, x="job_family", y="couverture_competence",
              title="Couverture des compétences critiques par job family")
st.plotly_chart(fig3, use_container_width=True)
