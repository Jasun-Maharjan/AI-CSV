'''
Libraries:-
Streamlit: Frontend
Pandas: Interaction with tabular data
Numpy: Data operations
Matplotlib: Grpahs
Ollama: local free LLM
'''

import streamlit as sl
import pandas as pd
import matplotlib.pyplot as plt
import ollama


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
    if question:
        response = ollama.chat(
        model="llama3.2",
        messages=[{
                "role": "system",
                "content": """You are AI-CSV, an AI data analysis assistant.
                Explain data analysis results clearly and concisely.
                Only use the information provided to you.
                Never invent numbers or statistics."""
            },
            {
                "role": "user",
                "content": f"""
                Dataset columns: {df.columns.tolist()}
                Statistical summary:{stats}
                User question:{question}

                Explain the result to the user in a clear and useful way.
                """
            }
        ]
        )

        answer = response["message"]["content"]
        sl.write(answer)

    if numeric_columns:
        sl.subheader("Data Visualizations")
        selected_column = sl.selectbox("select a column to visualize",numeric_columns)

        fig, gph = plt.subplots()
        gph.hist(df[selected_column].dropna())
        gph.set_xlabel(selected_column)
        gph.set_ylabel("Frequency")
        gph.set_title(f"Distribution of {selected_column}")

        sl.pyplot(fig)
