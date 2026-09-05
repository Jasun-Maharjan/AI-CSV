# AI-CSV

AI-CSV is an AI-powered data analysis assistant built with Python. It
allows users to upload a CSV dataset, inspect its contents and
statistics, ask questions about the data, and generate basic
visualizations.

The application combines **Pandas for actual data analysis** with
**Ollama (Llama 3.2) for natural-language explanations**.

## Features

-   Upload CSV datasets through a Streamlit interface
-   Display the number of rows and columns
-   Display the total number of missing values
-   Identify numerical and categorical columns
-   Detect and display columns containing missing values
-   Preview the uploaded dataset
-   Display statistical summaries using Pandas
-   Ask natural-language questions about the dataset
-   Perform supported calculations using Python/Pandas
-   Use a local Llama 3.2 model through Ollama to explain analysis
    results
-   Display visualizations for numerical columns
-   Histogram visualization
-   Box plot visualization
-   Loading indicator while the AI processes a question
-   Error handling when Ollama cannot be reached

## Technologies Used

  -----------------------------------------------------------------------
  Technology                          Purpose
  ----------------------------------- -----------------------------------
  Python                              Main programming language

  Streamlit                           Frontend and web application
                                      interface

  Pandas                              Data loading, processing, grouping,
                                      and statistical analysis

  NumPy                               Data operations

  Matplotlib                          Data visualization

  Ollama                              Local LLM integration

  Llama 3.2                           Natural-language explanation of
                                      analysis results
  -----------------------------------------------------------------------

## Current Supported Analysis

The current version supports questions involving:

-   Average revenue
-   Highest revenue
-   Most revenue by product
-   Missing values
-   General statistical summaries

## Visualizations

When the uploaded dataset contains numerical columns, AI-CSV provides
two visualization options:

### Histogram

Shows the distribution of values in a selected numerical column.

### Box Plot

Shows the distribution, median, spread, and potential outliers of a
selected numerical column.

## Requirements

-   Python 3.x
-   Streamlit
-   Pandas
-   NumPy
-   Matplotlib
-   Ollama
-   Llama 3.2 model

## Limitations

The current version is an early-stage implementation.

-   Question understanding is currently based on predefined keywords.
-   Only a limited number of analysis operations are supported.
-   The application currently focuses on CSV files.
-   Visualizations are limited to histograms and box plots.
-   Follow-up conversational questions are not yet supported.
-   The LLM does not independently generate Pandas code for arbitrary
    questions.

## Future Improvements

Possible future improvements include:

-   LLM-based natural-language question interpretation
-   Support for more statistical operations
-   Dynamic selection of dataset columns
-   Bar charts and scatter plots
-   Automatic dataset insights
-   Outlier detection
-   Correlation analysis
-   Chat history and follow-up questions
-   Downloadable analysis reports
-   Support for additional file formats
-   Safer structured output from the LLM

**Python + Pandas + Streamlit + Matplotlib + Ollama + Llama 3.2**
