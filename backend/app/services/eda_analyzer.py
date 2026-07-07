import pandas as pd


def perform_eda(
    dataframe: pd.DataFrame,
    column_types: dict,
) -> dict:
    numerical_analysis = {}
    categorical_analysis = {}
    binary_analysis = {}

    # Numerical analysis
    for column in column_types["numerical"]:
        series = dataframe[column].dropna()

        if series.empty:
            continue

        numerical_analysis[column] = {
            "count": int(series.count()),
            "mean": round(float(series.mean()), 2),
            "median": round(float(series.median()), 2),
            "std": round(float(series.std()), 2),
            "min": round(float(series.min()), 2),
            "max": round(float(series.max()), 2),
            "q1": round(float(series.quantile(0.25)), 2),
            "q3": round(float(series.quantile(0.75)), 2),
        }

    # Categorical analysis
    for column in column_types["categorical"]:
        series = dataframe[column].dropna()

        if series.empty:
            continue

        value_counts = series.value_counts().head(10)

        categorical_analysis[column] = {
            "unique_values": int(series.nunique()),
            "most_frequent_value": str(series.mode().iloc[0]),
            "most_frequent_count": int(value_counts.iloc[0]),
            "top_values": {
                str(value): int(count)
                for value, count in value_counts.items()
            },
        }

    # Binary analysis
    for column in column_types["binary"]:
        series = dataframe[column].dropna()

        if series.empty:
            continue

        value_counts = series.value_counts()

        binary_analysis[column] = {
            "unique_values": int(series.nunique()),
            "value_counts": {
                str(value): int(count)
                for value, count in value_counts.items()
            },
        }

    return {
        "numerical_analysis": numerical_analysis,
        "categorical_analysis": categorical_analysis,
        "binary_analysis": binary_analysis,
    }