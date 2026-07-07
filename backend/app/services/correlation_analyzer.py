import pandas as pd


def analyze_correlations(
    dataframe: pd.DataFrame,
    column_types: dict,
) -> dict:
    numerical_columns = column_types["numerical"]

    if len(numerical_columns) < 2:
        return {
            "correlation_matrix": {},
            "strong_correlations": [],
        }

    correlation_matrix = (
        dataframe[numerical_columns]
        .corr()
        .round(2)
    )

    matrix_result = {
        column: {
            related_column: float(value)
            for related_column, value
            in correlation_matrix[column].items()
        }
        for column in correlation_matrix.columns
    }

    strong_correlations = []

    for index, column in enumerate(numerical_columns):
        for related_column in numerical_columns[index + 1:]:
            correlation_value = correlation_matrix.loc[
                column,
                related_column,
            ]

            if pd.isna(correlation_value):
                continue

            if abs(correlation_value) >= 0.7:
                strong_correlations.append({
                    "column_1": column,
                    "column_2": related_column,
                    "correlation": float(correlation_value),
                    "strength": "strong",
                    "direction": (
                        "positive"
                        if correlation_value > 0
                        else "negative"
                    ),
                })

    return {
        "correlation_matrix": matrix_result,
        "strong_correlations": strong_correlations,
    }