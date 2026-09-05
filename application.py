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

def analyze_dataset(df, question):
    question = question.lower()

    result = ""

    if "average revenue" in question:
        if "Revenue" in df.columns:
            average = df["Revenue"].mean()
            result = f"Average revenue: {average:.2f}"

    elif "most revenue" in question or "highest revenue" in question:
        if "Product" in df.columns and "Revenue" in df.columns:
            revenue_by_product = df.groupby("Product")["Revenue"].sum()
            top_product = revenue_by_product.idxmax()
            top_revenue = revenue_by_product.max()

            result = (
                f"Revenue by product:\n"
                f"{revenue_by_product.to_string()}\n\n"
                f"Top product: {top_product}\n"
                f"Total revenue: {top_revenue:.2f}"
            )

    elif "missing" in question:
        missing = df.isnull().sum()
        result = f"Missing values:\n{missing.to_string()}"

    else:
        result = df.describe().to_string()

    return result

def data_visualization(chart_type):
    selected_column = sl.selectbox("select a column to visualize",numeric_columns)
    if chart_type == "Histogram":
        fig, gph = plt.subplots()
        gph.hist(df[selected_column].dropna())
        gph.set_xlabel(selected_column)
        gph.set_ylabel("Frequency")
        gph.set_title(f"Distribution of {selected_column}")
        sl.pyplot(fig)

    elif chart_type == "Box Plot":
        fig, gph = plt.subplots()
        gph.boxplot(df[selected_column].dropna())
        gph.set_ylabel(selected_column)
        gph.set_title(f"Box Plot of {selected_column}")
        sl.pyplot(fig)


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

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(
        include="object"
    ).columns.tolist()

    sl.write(f"Numerical columns: {len(numeric_columns)}")
    sl.write(f"Categorical columns: {len(categorical_columns)}")

    if df.isnull().sum().sum()!=0:
        missing_values = df.isnull().sum()

        for column, count in missing_values.items():

            if count > 0:
                sl.write(f"• {column} contains {count} missing values")

    sl.subheader("Dataset Preview")
    sl.dataframe(df)
    sl.subheader("Stat summary")
    sl.dataframe(df.describe())

    

    stats = df.describe().to_string()

    sl.subheader("Ask AI")

    question = sl.text_input(
        "Ask a question about your dataset:",
        placeholder="e.g. What is the average revenue?"
    )
    if question:
        with sl.spinner("Analyzing your dataset..."):
            try:
                analysis_result = analyze_dataset(df, question)
                response = ollama.chat(
                model="llama3.2",
                messages=[{
                        "role": "system",
                        "content": """You are AI-CSV, an AI data analysis assistant.

                        Explain the analysis result clearly and concisely.

                        Only use the information provided.
                        Never invent numbers or statistics.
                        Python/Pandas has already performed the calculations.
                        Your job is to explain the result in natural language.

                        Do not use backticks, code formatting, or Markdown styling.
                        Use plain text only."""
                    },
                    {
                        "role": "user",
                        "content": f"""
                        Dataset columns: {df.columns.tolist()}
                        Statistical summary:{stats}
                        User question:{question}
                        Analysis performed by Python/Pandas:{analysis_result}

                        Explain the result to the user in a clear and useful way.
                        """
                    }
                ]
                )

                answer = response["message"]["content"]
                answer = answer.replace("`", "")
                sl.write(answer)

            except Exception:
                sl.error("Could not connect to Ollama")

    if numeric_columns:
        sl.subheader("Data Visualizations")
        chart_type = sl.selectbox(
            "Choose visualization",
            ["Histogram", "Box Plot"]
        )
        data_visualization(chart_type)
