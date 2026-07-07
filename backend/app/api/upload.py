from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.core.database import get_database_session
from app.core.dataset_store import dataset_store
from app.models.ai_insight import AIInsight
from app.models.analysis_result import AnalysisResult
from app.models.dataset import Dataset
from app.services.ai_insight_service import generate_dataset_insights
from app.services.data_loader import load_dataset
from app.services.dataset_analyzer import analyze_dataset


router = APIRouter(
    prefix="/upload",
    tags=["Dataset Upload"],
)


@router.post("/")
async def upload_dataset(
    file: UploadFile = File(...),
    database: Session = Depends(get_database_session),
):
    dataframe = await load_dataset(file)

    analysis = analyze_dataset(dataframe)

    ai_result = generate_dataset_insights(analysis)

    dataset_record = Dataset(
        filename=file.filename,
        rows=len(dataframe),
        columns=len(dataframe.columns),
    )

    database.add(dataset_record)
    database.flush()

    analysis_record = AnalysisResult(
        dataset_id=dataset_record.id,
        data_quality=analysis["data_quality"],
        cleaning_recommendations=analysis[
            "cleaning_recommendations"
        ],
        eda=analysis["eda_analysis"],
        correlations=analysis["correlation_analysis"],
        chart_recommendations=analysis[
            "chart_recommendations"
        ],
    )

    database.add(analysis_record)

    ai_insight_record = None

    if ai_result["status"] == "success":
        ai_insight_record = AIInsight(
            dataset_id=dataset_record.id,
            insights=ai_result["ai_insights"],
        )

        database.add(ai_insight_record)

    database.commit()

    database.refresh(dataset_record)
    database.refresh(analysis_record)

    if ai_insight_record is not None:
        database.refresh(ai_insight_record)

    dataset_store.save_dataset(
        dataframe=dataframe,
        filename=file.filename,
        dataset_id=dataset_record.id,
    )

    return {
        "message": "Dataset uploaded and analyzed successfully",
        "dataset_id": dataset_record.id,
        "analysis_id": analysis_record.id,
        "ai_insight_id": (
            ai_insight_record.id
            if ai_insight_record is not None
            else None
        ),
        "dataset": {
            "filename": file.filename,
            **analysis,
        },
        "ai_analysis": ai_result,
    }