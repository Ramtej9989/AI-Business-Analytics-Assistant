import json

from app.core.gemini import client


def generate_business_summary(
    dataset_info: dict,
    data_quality: dict,
    eda: dict,
    correlations: dict,
    cleaning_recommendations: list,
    ai_insights: dict,
) -> dict:
    """
    Generate a complete AI-powered business summary.

    If Gemini is unavailable or quota is reached,
    return a safe response without failing dataset upload.
    """

    analysis_context = {
        "dataset_info": dataset_info,
        "data_quality": data_quality,
        "eda": eda,
        "correlations": correlations,
        "cleaning_recommendations": cleaning_recommendations,
        "ai_insights": ai_insights,
    }

    prompt = f"""
You are a senior business data analyst.

Analyze the following dataset analysis results.

ANALYSIS CONTEXT:
{json.dumps(analysis_context, indent=2, default=str)}

Generate one complete AI-powered business analysis summary.

The summary must:
- Be one detailed professional paragraph.
- Explain what the dataset represents when it can be inferred.
- Mention important dataset size and data quality information.
- Highlight meaningful patterns found in the analysis.
- Explain important business risks.
- Identify realistic business opportunities.
- Mention important correlations only when useful.
- Give practical business interpretation.
- Use actual facts from the provided analysis context.
- Do not invent numbers or business facts.
- Do not use bullet points.
- Do not use Markdown.
- Do not use headings.
- Do not mention JSON.
- Do not mention that you are an AI.
- Do not say "based on the provided context".
- Keep the summary between 180 and 300 words.

Write the summary as if a professional data analyst
is explaining the complete dataset analysis to a
business decision-maker.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        if not response.text:
            return {
                "status": "unavailable",
                "summary": None,
                "message": (
                    "AI business summary is temporarily "
                    "unavailable."
                ),
            }

        return {
            "status": "success",
            "summary": response.text.strip(),
            "message": None,
        }

    except Exception as error:
        error_message = str(error)

        if (
            "429" in error_message
            or "RESOURCE_EXHAUSTED" in error_message
            or "Quota exceeded" in error_message
        ):
            return {
                "status": "quota_exceeded",
                "summary": None,
                "message": (
                    "AI request limit reached. "
                    "Business summary is temporarily "
                    "unavailable."
                ),
            }

        return {
            "status": "error",
            "summary": None,
            "message": (
                "Unable to generate the AI business "
                "summary at this time."
            ),
        }