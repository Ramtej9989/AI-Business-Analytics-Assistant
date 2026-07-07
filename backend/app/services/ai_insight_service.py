from app.core.gemini import generate_ai_insights


def generate_dataset_insights(dataset_analysis: dict) -> dict:
    """
    Generate AI-powered business insights
    from the dataset analysis result.
    """

    try:
        ai_insights = generate_ai_insights(dataset_analysis)

        return {
            "status": "success",
            "ai_insights": ai_insights,
        }

    except Exception as error:
        return {
            "status": "error",
            "message": f"Failed to generate AI insights: {str(error)}",
        }