import pandas as pd


def recommend_charts(
    dataframe: pd.DataFrame,
    column_types: dict,
) -> list:
    recommendations = []

    numerical_columns = column_types["numerical"]
    categorical_columns = column_types["categorical"]
    binary_columns = column_types["binary"]
    datetime_columns = column_types["datetime"]

    # Numerical distributions
    for column in numerical_columns:
        recommendations.append({
            "chart_type": "histogram",
            "title": f"Distribution of {column}",
            "x_axis": column,
            "y_axis": None,
            "reason": f"Shows the distribution of {column}",
        })

    # Categorical and binary distributions
    category_columns = (
        categorical_columns + binary_columns
    )

    for column in category_columns:
        unique_values = dataframe[column].nunique(
            dropna=True
        )

        if unique_values <= 20:
            recommendations.append({
                "chart_type": "bar",
                "title": f"{column} Distribution",
                "x_axis": column,
                "y_axis": "count",
                "reason": (
                    f"Compares categories in {column}"
                ),
            })

    # Numerical relationships
    for index, column in enumerate(numerical_columns):
        for related_column in numerical_columns[index + 1:]:
            correlation = dataframe[
                [column, related_column]
            ].corr().iloc[0, 1]

            if (
                pd.notna(correlation)
                and abs(correlation) >= 0.5
            ):
                recommendations.append({
                    "chart_type": "scatter",
                    "title": (
                        f"{column} vs {related_column}"
                    ),
                    "x_axis": column,
                    "y_axis": related_column,
                    "reason": (
                        "Shows the relationship between "
                        f"{column} and {related_column}"
                    ),
                })

    # Time-series charts
    for datetime_column in datetime_columns:
        for numerical_column in numerical_columns:
            recommendations.append({
                "chart_type": "line",
                "title": (
                    f"{numerical_column} over "
                    f"{datetime_column}"
                ),
                "x_axis": datetime_column,
                "y_axis": numerical_column,
                "reason": "Shows changes over time",
            })

    return recommendations