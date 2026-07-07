import json

from google import genai
from google.genai import types

from app.core.config import settings


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def test_gemini_connection():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Reply with exactly: Gemini API connected",
    )

    return response.text


def generate_ai_insights(dataset_summary: dict) -> dict:
    """
    Generate structured AI-powered business insights
    from the analyzed dataset summary.
    """

    summary_text = json.dumps(
        dataset_summary,
        indent=2,
        default=str,
    )

    prompt = f"""
You are an expert AI Business Data Analyst.

Analyze the following dataset analysis summary.

DATASET SUMMARY:
{summary_text}

Generate clear, useful, and actionable business insights.

IMPORTANT GROUNDING RULES:
- Use only evidence explicitly available in the dataset summary.
- Never invent statistics, percentages, relationships, or business facts.
- Never claim that one customer segment has higher churn unless the summary
  explicitly contains a churn comparison for that segment.
- Correlation does not prove causation.
- Do not infer relationships between categorical columns unless the summary
  explicitly provides that relationship.
- If evidence is insufficient, clearly state that further analysis is required.
- Do not assume an industry unless the dataset columns clearly support it.
- Use simple business language.
- Keep recommendations connected to available evidence.

Return:
1. A short executive summary.
2. Exactly 5 key business insights.
3. Data quality observations.
4. Important relationships found in the data.
5. Exactly 5 actionable business recommendations.
6. Exactly 5 questions for further analysis.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema={
                "type": "object",
                "properties": {
                    "executive_summary": {
                        "type": "string"
                    },
                    "key_insights": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "data_quality_observations": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "important_relationships": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "business_recommendations": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "further_analysis_questions": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                },
                "required": [
                    "executive_summary",
                    "key_insights",
                    "data_quality_observations",
                    "important_relationships",
                    "business_recommendations",
                    "further_analysis_questions",
                ],
            },
        ),
    )

    if not response.text:
        raise ValueError(
            "Gemini returned an empty response."
        )

    return json.loads(response.text)


def explain_query_result(
    question: str,
    pandas_query: str,
    query_result,
) -> str:
    """
    Explain a verified Pandas query result
    in simple business language.
    """

    prompt = f"""
You are an AI Business Data Analyst.

USER QUESTION:
{question}

PANDAS QUERY USED:
{pandas_query}

VERIFIED QUERY RESULT:
{json.dumps(query_result, indent=2, default=str)}

Explain the verified result in clear, simple business language.

RULES:
- Use only the verified query result.
- Do not invent statistics or facts.
- Do not recalculate the result.
- Round long decimal numbers when appropriate.
- Keep the answer concise.
- Directly answer the user's question.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    if not response.text:
        raise ValueError(
            "Gemini returned an empty explanation."
        )

    return response.text.strip()