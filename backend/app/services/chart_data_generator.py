import numpy as np
import pandas as pd


def generate_chart_data(
    dataframe,
    chart_recommendations,
) -> list:
    charts = []

    for recommendation in chart_recommendations:
        chart_type = recommendation.get("chart_type")
        x_axis = recommendation.get("x_axis")
        y_axis = recommendation.get("y_axis")

        chart = {
            "chart_type": chart_type,
            "title": recommendation.get("title"),
            "x_axis": x_axis,
            "y_axis": y_axis,
            "reason": recommendation.get("reason"),
            "data": [],
        }

        if chart_type == "bar":
            value_counts = (
                dataframe[x_axis]
                .fillna("Missing")
                .value_counts()
                .head(10)
            )

            chart["data"] = [
                {
                    "label": str(label),
                    "value": int(value),
                }
                for label, value in value_counts.items()
            ]

        elif chart_type == "histogram":
            column_data = (
                pd.to_numeric(
                    dataframe[x_axis],
                    errors="coerce",
                )
                .dropna()
            )

            if not column_data.empty:
                bin_counts = 10

                counts, bin_edges = np.histogram(
                    column_data,
                    bins=bin_counts,
                )

                chart["data"] = [
                    {
                        "label": (
                            f"{bin_edges[index]:.1f} - "
                            f"{bin_edges[index + 1]:.1f}"
                        ),
                        "value": int(counts[index]),
                    }
                    for index in range(len(counts))
                ]

        elif chart_type == "line":
            line_data = dataframe[
                [x_axis, y_axis]
            ].copy()

            line_data[x_axis] = pd.to_datetime(
                line_data[x_axis],
                errors="coerce",
            )

            line_data[y_axis] = pd.to_numeric(
                line_data[y_axis],
                errors="coerce",
            )

            line_data = line_data.dropna()

            if not line_data.empty:
                line_data = (
                    line_data
                    .groupby(x_axis)[y_axis]
                    .mean()
                    .reset_index()
                    .sort_values(x_axis)
                )

                chart["data"] = [
                    {
                        "label": row[x_axis].strftime(
                            "%Y-%m-%d"
                        ),
                        "value": round(
                            float(row[y_axis]),
                            2,
                        ),
                    }
                    for _, row in line_data.iterrows()
                ]

        elif chart_type == "scatter":
            scatter_data = dataframe[
                [x_axis, y_axis]
            ].copy()

            scatter_data[x_axis] = pd.to_numeric(
                scatter_data[x_axis],
                errors="coerce",
            )

            scatter_data[y_axis] = pd.to_numeric(
                scatter_data[y_axis],
                errors="coerce",
            )

            scatter_data = (
                scatter_data
                .dropna()
                .head(500)
            )

            chart["data"] = [
                {
                    "x": float(row[x_axis]),
                    "y": float(row[y_axis]),
                }
                for _, row in scatter_data.iterrows()
            ]

        charts.append(chart)

    return charts