import pandas as pd


def analyze_data_quality(dataframe: pd.DataFrame) -> dict:
    total_rows = len(dataframe)
    total_columns = len(dataframe.columns)
    total_cells = total_rows * total_columns

    missing_values = dataframe.isnull().sum()
    total_missing = int(missing_values.sum())

    if total_cells > 0:
        missing_percentage = round(
            (total_missing / total_cells) * 100,
            2
        )
    else:
        missing_percentage = 0.0

    duplicate_rows = int(dataframe.duplicated().sum())

    duplicate_columns = []
    columns = dataframe.columns.tolist()

    for index, column in enumerate(columns):
        for compare_column in columns[index + 1:]:
            if dataframe[column].equals(dataframe[compare_column]):
                duplicate_columns.append(compare_column)

    duplicate_columns = list(set(duplicate_columns))

    constant_columns = [
        column
        for column in dataframe.columns
        if dataframe[column].nunique(dropna=False) <= 1
    ]

    columns_with_missing_values = {
        column: {
            "missing_count": int(count),
            "missing_percentage": round(
                (count / total_rows) * 100,
                2
            ) if total_rows > 0 else 0.0,
        }
        for column, count in missing_values.items()
        if count > 0
    }

    missing_penalty = min(missing_percentage, 40)

    duplicate_percentage = (
        (duplicate_rows / total_rows) * 100
        if total_rows > 0
        else 0
    )

    duplicate_penalty = min(duplicate_percentage, 30)
    constant_penalty = min(len(constant_columns) * 5, 20)
    duplicate_column_penalty = min(len(duplicate_columns) * 5, 10)

    quality_score = round(
        100
        - missing_penalty
        - duplicate_penalty
        - constant_penalty
        - duplicate_column_penalty,
        2
    )

    quality_score = max(quality_score, 0)

    return {
        "quality_score": quality_score,
        "total_missing_values": total_missing,
        "missing_percentage": missing_percentage,
        "columns_with_missing_values": columns_with_missing_values,
        "duplicate_rows": duplicate_rows,
        "duplicate_columns": duplicate_columns,
        "constant_columns": constant_columns,
    }