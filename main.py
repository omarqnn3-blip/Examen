import streamlit as st

st.set_page_config(
    page_title="Dashboard Examen",
    layout="wide",
    initial_sidebar_state="expanded",
)


pg_home= st.Page("pages/home.py", title="Home",icon='🏠')
pg_grafica = st.Page("pages/Analisis.py", title="Analisis de proyecto",icon="📈")

pg= st.navigation({'Inicio':[pg_home], 'Analisis':[pg_grafica]})
pg.run()