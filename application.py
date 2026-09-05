'''
Libraries:-
Streamlit: Frontend
Pandas: Interaction with tabular data
Numpy: Data operations
Matplotlib: Grpahs
OpenAI: Connect to LLM
'''

import streamlit as sl
import pandas as pd
import matplotlib.pyplot as plt
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

sl.set_page_config(
    page_title = "AI-CSV",
    layout = "wide"
)

sl.title("AI-CSV")
sl.subheader("AI-powered Data Analysis Assistant")

file = sl.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if file is not None:
    df = pd.read_csv(file)
    sl.success("File Uploaded!")

    col1, col2, col3 = sl.columns(3)

    with col1:
        sl.metric("Rows", df.shape[0])

    with col2:
        sl.metric("Columns", df.shape[1])

    with col3:
        sl.metric("Missing values", df.isnull().sum().sum())

    sl.subheader("Dataset Preview")
    sl.dataframe(df)
    sl.subheader("Stat summary")
    sl.dataframe(df.describe())

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    summary = {
        "rows" : len(df),
        "columns" : len(df.columns),
        "missing_values" : int(df.isnull().sum().sum()),
        "numeric_columns" : numeric_columns
    }

    stats = df.describe().to_string()

    sl.subheader("Ask AI")

    question = sl.text_input(
        "Ask a question about your dataset:",
        placeholder="e.g. What is the average revenue?"
    )

    if numeric_columns:
        sl.subheader("Data Visualizations")
        selected_column = sl.selectbox("select a column to visualize",numeric_columns)

        fig, gph = plt.subplots()
        gph.hist(df[selected_column].dropna())
        gph.set_xlabel(selected_column)
        gph.set_ylabel("Frequency")
        gph.set_title(f"Distribution of {selected_column}")

        sl.pyplot(fig)
