from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.core.database import get_database_session
from app.core.dataset_store import dataset_store
from app.models.ask_history import AskHistory
from app.services.data_query_service import (
    execute_pandas_query,
    generate_pandas_query,
    serialize_query_result,
)
from app.services.query_answer_formatter import (
    format_query_answer,
)


router = APIRouter(
    prefix="/ask",
    tags=["Ask Your Data"],
)


class DataQuestionRequest(BaseModel):
    question: str


@router.post("/")
async def ask_dataset(
    request: DataQuestionRequest,
    database: Session = Depends(get_database_session),
):
    if not dataset_store.has_dataset():
        raise HTTPException(
            status_code=400,
            detail="No dataset uploaded. Upload a dataset first.",
        )

    dataframe = dataset_store.get_dataset()
    dataset_id = dataset_store.get_dataset_id()

    if dataset_id is None:
        raise HTTPException(
            status_code=400,
            detail=(
                "Active dataset is not connected "
                "to the database."
            ),
        )

    try:
        pandas_query = generate_pandas_query(
            dataframe=dataframe,
            question=request.question,
        )

        query_result = execute_pandas_query(
            dataframe=dataframe,
            pandas_query=pandas_query,
        )

        serialized_result = serialize_query_result(
            query_result
        )

        answer = format_query_answer(
            question=request.question,
            query_result=serialized_result,
        )

        ask_history_record = AskHistory(
            dataset_id=dataset_id,
            question=request.question,
            pandas_query=pandas_query,
            calculation_result=serialized_result,
            answer=answer,
        )

        database.add(ask_history_record)
        database.commit()
        database.refresh(ask_history_record)

        return {
            "status": "success",
            "ask_history_id": ask_history_record.id,
            "dataset_id": dataset_id,
            "filename": dataset_store.get_filename(),
            "question": request.question,
            "pandas_query": pandas_query,
            "result": serialized_result,
            "ai_answer": answer,
        }

    except HTTPException:
        database.rollback()
        raise

    except Exception as error:
        database.rollback()

        error_message = str(error)

        if (
            "429" in error_message
            or "RESOURCE_EXHAUSTED" in error_message
            or "Quota exceeded" in error_message
        ):
            raise HTTPException(
                status_code=429,
                detail=(
                    "AI request limit reached. "
                    "Please try again after the "
                    "Gemini API quota resets."
                ),
            )

        raise HTTPException(
            status_code=500,
            detail=(
                f"Failed to answer question: "
                f"{error_message}"
            ),
        )