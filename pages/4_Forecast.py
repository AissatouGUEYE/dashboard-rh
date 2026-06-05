import numpy as np
np.float = float
np.int = int
np.bool = bool
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔮 Vue Forecast – Prédiction des départs")

df = pd.read_csv("data/GOLD_DATA.csv")

# Renommage
df = df.rename(columns={
    "voluntary_leavers": "depart_volontaire"
})

import joblib

# Charger le modèle
model = joblib.load("model.pkl")

# Colonnes utilisées pour la prédiction
features = ["headcount_actual", "headcount_planned", "engagement_score_avg",
            "training_hours_avg", "absenteeism_rate", "critical_skill_coverage_rate",
            "total_open_positions", "avg_time_to_fill"]

# Générer les prédictions
df["pred"] = model.predict(df[features])


if "pred" in df.columns:
    st.subheader("📌 Réel vs Prédit")
    fig = px.scatter(df, x="depart_volontaire", y="pred", trendline="ols",
                     title="Réel vs Prédit")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📌 Erreur de prédiction")
    df["erreur"] = df["depart_volontaire"] - df["pred"]
    st.write(df[["team_id","site","depart_volontaire","pred","erreur"]])
else:
    st.warning("⚠️ Aucune colonne 'pred' trouvée. Ajoute tes prédictions dans la GOLD DATA.")
