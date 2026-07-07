import json


def format_query_answer(
    question: str,
    query_result,
) -> str:
    """
    Generate a readable answer from the calculated
    dataset result without making another AI request.
    """

    normalized_question = question.lower().strip()

    if isinstance(query_result, bool):
        return (
            "Yes."
            if query_result
            else "No."
        )

    if isinstance(query_result, (int, float)):
        if "rate" in normalized_question:
            percentage = query_result * 100

            return (
                f"The calculated rate is "
                f"{percentage:.2f}%."
            )

        if "average" in normalized_question:
            return (
                f"The calculated average is "
                f"{query_result:,.2f}."
            )

        if "total" in normalized_question:
            return (
                f"The calculated total is "
                f"{query_result:,.2f}."
            )

        if "count" in normalized_question:
            return (
                f"The calculated count is "
                f"{query_result:,}."
            )

        return (
            f"Based on the dataset, the calculated "
            f"result is {query_result:,.2f}."
        )

    if isinstance(query_result, str):
        if (
            "most popular" in normalized_question
            or "most common" in normalized_question
            or "highest" in normalized_question
            or "most customers" in normalized_question
        ):
            return (
                f"Based on the dataset, "
                f"{query_result} has the highest result."
            )

        return (
            f"Based on the dataset, the result is "
            f"{query_result}."
        )

    if isinstance(query_result, dict):
        if not query_result:
            return (
                "The analysis returned no matching results."
            )

        result_items = list(query_result.items())

        if len(result_items) == 1:
            key, value = result_items[0]

            return (
                f"Based on the dataset, {key} has a "
                f"calculated value of {value}."
            )

        preview_items = result_items[:5]

        formatted_items = ", ".join(
            f"{key}: {value}"
            for key, value in preview_items
        )

        return (
            "The analysis returned the following key "
            f"results: {formatted_items}."
        )

    if isinstance(query_result, list):
        if not query_result:
            return (
                "The analysis returned no matching results."
            )

        if len(query_result) == 1:
            return (
                "Based on the dataset, the calculated "
                f"result is {json.dumps(query_result[0], default=str)}."
            )

        return (
            f"The analysis returned {len(query_result)} "
            "results. Review the calculation result below "
            "for the detailed breakdown."
        )

    return (
        "The dataset analysis was completed successfully. "
        "Review the calculation result below for details."
    )