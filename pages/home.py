import streamlit as st
from utils.load_data import load_exam_data, filtros
import pandas as pd
import numpy as np
exam_data = load_exam_data()
st.markdown('<h1 style="text-align:center;"><b>Dashboard principal de proyectos</b></h1>', unsafe_allow_html=True)


st.sidebar.header('Filtros')
states_all = exam_data["State"].unique().tolist()
category_all = exam_data["Category"].unique().tolist()
managers_all = exam_data["Manager"].unique().tolist()
pct_range_all = exam_data["PercentComplete"].tolist()
states= st.sidebar.multiselect('Estado', options=states_all)
category=st.sidebar.multiselect('Categoria',options=category_all)
managers=st.sidebar.multiselect('Manager', options= managers_all)
pct_min = float(pd.to_numeric(exam_data["PercentComplete"], errors="coerce").min() if "Percent complete" in exam_data.columns else 0.0)
pct_max = float(pd.to_numeric(exam_data["PercentComplete"], errors="coerce").max() if "Percent complete" in exam_data.columns else 100.0)
pct_range = st.sidebar.slider("Avance (%)", min_value=0.0, max_value=100.0, value=(max(0.0, pct_min), min(100.0, pct_max)), step=1.0)


df_f = filtros(
    exam_data,
    State=states,
    Category=category,
    Manager=managers,
    PercentComplete=pct_range,
    
)

with st.container(border=True):
    k1, k2, k3, k4 = st.columns(4)

    total = len(df_f)
    avg_pct = float(pd.to_numeric(df_f["PercentComplete"], errors="coerce").mean()) if total else 0.0
    managers_n = df_f["Manager"].nunique() if total else 0
    budget_mean = float(pd.to_numeric(df_f["BudgetThousands"], errors="coerce").mean()) if total else 0.0

    k1.metric("Total proyectos", f"{total:,}")
    k2.metric("Avance promedio", f"{avg_pct:,.1f}%")
    k3.metric("Managers únicos", f"{managers_n:,}")
    k4.metric("Presupuesto medio", f"${budget_mean:,.1f}K")

st.markdown("### Datos filtrados")
st.dataframe(df_f)
