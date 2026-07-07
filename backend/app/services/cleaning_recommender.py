import pandas as pd


def generate_cleaning_recommendations(
    dataframe: pd.DataFrame,
) -> list:
    recommendations = []

    total_rows = len(dataframe)

    # Missing value recommendations
    for column in dataframe.columns:
        missing_count = int(
            dataframe[column].isnull().sum()
        )

        if missing_count == 0:
            continue

        missing_percentage = (
            (missing_count / total_rows) * 100
            if total_rows > 0
            else 0
        )

        if missing_percentage > 50:
            recommendations.append({
                "column": column,
                "issue": "high_missing_values",
                "recommendation": (
                    "Consider dropping this column"
                ),
                "missing_count": missing_count,
                "missing_percentage": round(
                    missing_percentage,
                    2,
                ),
            })

        elif pd.api.types.is_numeric_dtype(
            dataframe[column]
        ):
            recommendations.append({
                "column": column,
                "issue": "missing_values",
                "recommendation": (
                    "Fill missing values using median"
                ),
                "missing_count": missing_count,
                "missing_percentage": round(
                    missing_percentage,
                    2,
                ),
            })

        else:
            recommendations.append({
                "column": column,
                "issue": "missing_values",
                "recommendation": (
                    "Fill missing values using mode"
                ),
                "missing_count": missing_count,
                "missing_percentage": round(
                    missing_percentage,
                    2,
                ),
            })

    # Duplicate row recommendation
    duplicate_rows = int(
        dataframe.duplicated().sum()
    )

    if duplicate_rows > 0:
        recommendations.append({
            "column": None,
            "issue": "duplicate_rows",
            "recommendation": (
                "Remove duplicate rows to prevent repeated "
                "records from affecting analysis results"
            ),
            "duplicate_count": duplicate_rows,
        })

    # Constant column recommendations
    for column in dataframe.columns:
        unique_values = dataframe[column].nunique(
            dropna=False
        )

        if unique_values <= 1:
            recommendations.append({
                "column": column,
                "issue": "constant_column",
                "recommendation": (
                    "Consider dropping this column because "
                    "it contains only one unique value"
                ),
                "unique_count": int(unique_values),
            })

    return recommendations