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

## How It Works

AI-CSV follows a simple analysis pipeline:

``` text
CSV Upload
    ↓
Pandas loads the dataset
    ↓
Dataset information and statistics are displayed
    ↓
User asks a question
    ↓
Python/Pandas analyzes the question
    ↓
Pandas performs the calculation
    ↓
Result is sent to Llama 3.2 through Ollama
    ↓
Llama explains the result in natural language
```

The application is designed so that **Python/Pandas performs the
numerical calculations**, while the LLM is primarily responsible for
explaining the results. This helps reduce the possibility of the LLM
inventing statistical values.

## Current Supported Analysis

The current version supports questions involving:

-   Average revenue
-   Highest revenue
-   Most revenue by product
-   Missing values
-   General statistical summaries

Example questions:

``` text
What is the average revenue?

Which product has the highest revenue?

Which product generated the most revenue?

Show me the missing values.
```

The analysis functions are currently based on keyword matching, so
questions need to contain supported terms.

## Visualizations

When the uploaded dataset contains numerical columns, AI-CSV provides
two visualization options:

### Histogram

Shows the distribution of values in a selected numerical column.

### Box Plot

Shows the distribution, median, spread, and potential outliers of a
selected numerical column.

## Project Structure

``` text
AI-CSV/
│
├── application.py
├── README.md
└── venv/
```

`application.py` contains the Streamlit application, Pandas analysis
functions, Matplotlib visualizations, and Ollama integration.

## Requirements

-   Python 3.x
-   Streamlit
-   Pandas
-   NumPy
-   Matplotlib
-   Ollama
-   Llama 3.2 model

## Installation

### 1. Clone or download the project

Open a terminal in the project directory.

### 2. Create a virtual environment

``` bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:

``` bash
venv\Scripts\activate
```

### 4. Install Python dependencies

``` bash
pip install streamlit pandas numpy matplotlib ollama
```

### 5. Install Ollama

Install Ollama for your operating system.

After installation, download the Llama 3.2 model:

``` bash
ollama run llama3.2
```

This will download the model if it is not already installed.

### 6. Run the application

``` bash
streamlit run application.py
```

The application will open in your web browser.

## Example Workflow

1.  Start the Streamlit application.
2.  Upload a CSV file.
3.  Review the dataset information and preview.
4.  Check the numerical and categorical columns.
5.  Review any detected missing values.
6.  Select a visualization type and numerical column.
7.  Ask a question in the **Ask AI** section.
8.  Python/Pandas performs the supported analysis.
9.  Llama 3.2 explains the calculated result.

## Example

For a question such as:

``` text
What is the average revenue?
```

The application first performs the calculation using Pandas:

``` python
average = df["Revenue"].mean()
```

The resulting value is then passed to Llama 3.2, which produces a
natural-language explanation for the user.

## Privacy

AI-CSV uses Ollama to run the Llama 3.2 model locally. The application
is designed to avoid requiring an external LLM API for the analysis
explanation.

However, users should still avoid uploading sensitive or confidential
datasets unless they understand and have verified the local environment
in which the application is running.

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

## Author

Developed as a Python and AI/data-analysis project demonstrating the
integration of:

**Python + Pandas + Streamlit + Matplotlib + Ollama + Llama 3.2**
