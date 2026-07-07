from app.services.chart_data_generator import generate_chart_data
from app.services.chart_recommender import recommend_charts
from app.services.cleaning_recommender import (
    generate_cleaning_recommendations,
)
from app.services.column_detector import detect_column_types
from app.services.correlation_analyzer import analyze_correlations
from app.services.data_quality import analyze_data_quality
from app.services.eda_analyzer import perform_eda
from app.services.insight_generator import generate_ai_insights


def analyze_dataset(dataframe) -> dict:
    column_types = detect_column_types(dataframe)

    data_quality = analyze_data_quality(dataframe)

    cleaning_recommendations = (
        generate_cleaning_recommendations(dataframe)
    )

    eda_analysis = perform_eda(
        dataframe,
        column_types,
    )

    correlation_analysis = analyze_correlations(
        dataframe,
        column_types,
    )

    chart_recommendations = recommend_charts(
        dataframe,
        column_types,
    )

    chart_data = generate_chart_data(
        dataframe,
        chart_recommendations,
    )

    ai_insights = generate_ai_insights(
        dataframe,
        column_types,
        data_quality,
        eda_analysis,
        correlation_analysis,
    )

    dataset_info = {
        "rows": dataframe.shape[0],
        "columns": dataframe.shape[1],
        "column_names": dataframe.columns.tolist(),
        "column_types": column_types,
        "data_types": {
            column: str(dtype)
            for column, dtype in dataframe.dtypes.items()
        },
    }


    return {
        "rows": dataframe.shape[0],
        "columns": dataframe.shape[1],
        "column_names": dataframe.columns.tolist(),
        "column_types": column_types,
        "data_types": {
            column: str(dtype)
            for column, dtype in dataframe.dtypes.items()
        },
        "missing_values": {
            column: int(value)
            for column, value
            in dataframe.isnull().sum().items()
        },
        "data_quality": data_quality,
        "cleaning_recommendations": cleaning_recommendations,
        "eda_analysis": eda_analysis,
        "correlation_analysis": correlation_analysis,
        "chart_recommendations": chart_recommendations,
        "chart_data": chart_data,
        "ai_insights": ai_insights,
    }