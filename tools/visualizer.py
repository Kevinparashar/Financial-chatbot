import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def plot_trend(df, query):
    if not isinstance(df, pd.DataFrame):
        return "No trend to plot."
    try:
        numeric_cols = df.select_dtypes(include="number").columns
        if len(numeric_cols) < 2:
            return "Need at least 2 numeric columns."
        fig, ax = plt.subplots()
        df[numeric_cols[:2]].plot(ax=ax)
        st.pyplot(fig)
        return "Plotted basic trend."
    except Exception as e:
        return f"Error plotting trend: {str(e)}"