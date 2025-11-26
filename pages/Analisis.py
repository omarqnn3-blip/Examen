import streamlit as st
from utils.load_data import load_exam_data, filtros, grafica
import pandas as pd
import numpy as np
exam_data = load_exam_data()
st.markdown('<h1 style="text-align:center;"><b>Visualizaciones y comparación</b></h1>', unsafe_allow_html=True)

managers_all = exam_data["Manager"].unique().tolist()
managers=st.sidebar.multiselect('Manager', options= managers_all)
category_all = exam_data["Category"].unique().tolist()
category=st.sidebar.multiselect('Categorias', options=category_all)

df_f = filtros(
    exam_data,
    Category=category,
    Manager=managers,
)
fig = grafica(
    df_f,
    x="BudgetThousands",
    y="PercentComplete",
    color="State",
    hover_data=["ProjectName", "Manager", "Category", "Country", "State"],
    title="Presupuesto vs Avance"
)
st.plotly_chart(fig, use_container_width=True)

