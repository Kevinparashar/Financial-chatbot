import pandas as pd

def analyze_data(df, query):
    if not isinstance(df, pd.DataFrame):
        return "Data is not tabular."
    summary = df.describe().to_dict()
    return {"summary_stats": summary}