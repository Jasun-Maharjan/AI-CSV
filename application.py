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
