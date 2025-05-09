import pandas as pd
import plotly.express as px
from preswald import Workflow, text, get_df, connect, plotly

workflow = Workflow()

@workflow.atom()
def load_data():
    connect()
    df = get_df("weather_prediction_dataset")
    return df

@workflow.atom(dependencies=["load_data"])
def visualize_all(load_data):
    df = load_data

    text("# Weather Data Visualizations")

    # Drop rows with missing DATE or humidity
    df = df.dropna(subset=["DATE", "BASEL_humidity"])

    # Sort for proper time-series display
    df = df.sort_values(by="DATE")

    # 1. Basel Humidity Over Time
    fig1 = px.line(df, x="DATE", y="BASEL_humidity", title="Basel Humidity Over Time")
    plotly(fig1)

    # 2. Humidity vs Pressure
    fig2 = px.scatter(df, x="BASEL_humidity", y="BASEL_pressure", title="Humidity vs Pressure")
    plotly(fig2)

    # 3. Global Radiation Distribution
    fig3 = px.histogram(df, x="BASEL_global_radiation", nbins=30, title="Global Radiation Distribution (Basel)")
    plotly(fig3)

workflow.execute()


