import pandas as pd

def load_exam_data():
    exam_data=pd.read_csv('data/exam_data.csv')
    return exam_data

def filtros(
    df: pd.DataFrame,
    projectid: list[float] | None = None, 
    ProjectName: list[str] | None = None, 
    Manager: list[str] | None = None,
    Category: list[str] | None = None,
    Country: list[str] | None = None,
    State: list[str] | None=None,
    PercentComplete: list[float] | None=None,
    BudgetThousands: list[float] | None=None,
    StartDate: list[str] |None=None,
    CriticalFlag: bool = False,
    ) -> pd.DataFrame:
    out = df.copy()

    if projectid:
        out = out[out["ProjectID"].isin(projectid)]
    if ProjectName:
        out = out[out["ProjectName"].isin(ProjectName)]
    if Manager:
        out = out[out["Manager"].isin(Manager)]
    if Category:
        out = out[out["Category"].isin(Category)]
    if Country:
        out = out[out["Country"].isin(Country)]
    if State:
        out = out[out["State"].isin(State)]
    if PercentComplete:
        if isinstance(PercentComplete, (tuple, list)) and len(PercentComplete) == 2:
            min_pct, max_pct = PercentComplete
            out = out[(pd.to_numeric(out["PercentComplete"], errors="coerce") >= min_pct) & (pd.to_numeric(out["PercentComplete"], errors="coerce") <= max_pct)]
        else:
            out = out[out["PercentComplete"].isin(PercentComplete)]
    if BudgetThousands:
        out = out[out["BudgetThousands"].isin(BudgetThousands)]
    if StartDate:
        out = out[out["StartDate"].isin(StartDate)]
    if CriticalFlag:
        out = out[out["CriticalFlag"] == True]

    return out

import plotly.express as px

def grafica(df: pd.DataFrame, x: str, y: str, color: str = None, hover_data: list = None, title: str = "Avance vs Presupuesto"):
    color_discrete_map = None
    if color == "State":
        color_discrete_map = {
            "Pending": "#0033A0",  
            "Done": "#7EC8E3",     
            "Active": "#FF0000"    
        }
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        hover_data=hover_data,
        title=title,
        template="plotly_white",
        color_discrete_map=color_discrete_map
    )
    fig.update_traces(marker=dict(size=10, opacity=0.7))
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20), legend=dict(orientation="v", x=1.02, y=1, xanchor="left", yanchor="top"))
    return fig
