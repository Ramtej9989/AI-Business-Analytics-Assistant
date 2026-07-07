import json

import pandas as pd

from app.core.gemini import client
from app.services.safe_query_executor import execute_safe_query


def prepare_dataset_context(dataframe: pd.DataFrame) -> dict:
    """
    Prepare compact dataset context for Gemini
    to understand the available data.
    """

    context = {
        "rows": len(dataframe),
        "columns": dataframe.columns.tolist(),
        "data_types": {
            column: str(dtype)
            for column, dtype in dataframe.dtypes.items()
        },
        "sample_rows": dataframe.head(5).to_dict(
            orient="records"
        ),
    }

    return context


def generate_pandas_query(
    dataframe: pd.DataFrame,
    question: str,
) -> str:
    """
    Ask Gemini to generate a Pandas expression
    for answering the user's dataset question.
    """

    dataset_context = prepare_dataset_context(dataframe)

    prompt = f"""
You are a Python Pandas data analysis assistant.

DATASET CONTEXT:
{json.dumps(dataset_context, indent=2, default=str)}

USER QUESTION:
{question}

Generate exactly one Pandas expression that answers the question.

The DataFrame variable name is:

df

RULES:
- Return only the Pandas expression.
- Do not use Markdown.
- Do not use code blocks.
- Do not include explanations.
- Do not import libraries.
- Do not modify the DataFrame.
- Do not use eval(), exec(), open(), or file operations.
- Use only existing dataset columns.
- Prefer Pandas vectorized operations.
- The expression must return a value, Series, or DataFrame.
- For grouped rate, percentage, or comparison questions,
  prefer returning both the group sample count and the calculated metric.
- For churn-rate questions where Churn contains Yes and No,
  calculate the rate using the proportion of Churn == "Yes".
- When returning grouped counts and rates, prefer a DataFrame
  with clear column names such as customer_count and churn_rate.
- Do not treat a small group as statistically reliable.
- Do not add conclusions inside the Pandas expression.

Example question:
What is the average monthly charge?

Example response:
df["MonthlyCharges"].mean()

Example grouped rate question:
What is the churn rate by support tickets?

Example response:
df.groupby("SupportTickets")["Churn"].agg(
    customer_count="count",
    churn_rate=lambda x: (x == "Yes").mean()
).reset_index()
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    if not response.text:
        raise ValueError(
            "Gemini returned an empty Pandas query."
        )

    return response.text.strip()


def execute_pandas_query(
    dataframe: pd.DataFrame,
    pandas_query: str,
):
    """
    Execute a validated Pandas expression.
    """

    return execute_safe_query(
        dataframe=dataframe,
        pandas_query=pandas_query,
    )


def serialize_query_result(result):
    """
    Convert Pandas and NumPy results
    into JSON-compatible Python objects.
    """

    if isinstance(result, pd.DataFrame):
        return result.to_dict(orient="records")

    if isinstance(result, pd.Series):
        return result.to_dict()

    if hasattr(result, "item"):
        return result.item()

    return result