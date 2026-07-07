import pandas as pd


def detect_column_types(dataframe: pd.DataFrame) -> dict:
    column_types = {
        "numerical": [],
        "categorical": [],
        "binary": [],
        "datetime": [],
        "id_columns": [],
    }

    total_rows = len(dataframe)

    for column in dataframe.columns:
        series = dataframe[column]
        column_name = column.lower()

        unique_values = series.dropna().unique()
        unique_count = series.nunique(dropna=True)

        # Detect ID columns
        if (
            "id" in column_name
            or "code" in column_name
            or (
                total_rows > 0
                and unique_count == total_rows
            )
        ):
            column_types["id_columns"].append(column)
            continue

        # Detect datetime columns
        if pd.api.types.is_datetime64_any_dtype(series):
            column_types["datetime"].append(column)
            continue

        if "date" in column_name or "time" in column_name:
            converted_series = pd.to_datetime(
                series,
                errors="coerce",
            )

            valid_percentage = converted_series.notna().mean()

            if valid_percentage >= 0.8:
                column_types["datetime"].append(column)
                continue

        # Detect binary columns
        if unique_count == 2:
            column_types["binary"].append(column)
            continue

        # Detect numerical columns
        if pd.api.types.is_numeric_dtype(series):
            column_types["numerical"].append(column)
            continue

        # Remaining columns are categorical
        column_types["categorical"].append(column)

    return column_types