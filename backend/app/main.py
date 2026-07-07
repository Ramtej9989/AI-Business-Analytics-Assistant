from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.ask import router as ask_router
from app.api.upload import router as upload_router
from app.core.database import engine
from app.models.base import Base

# Import models so SQLAlchemy registers the tables.
from app.models.ai_insight import AIInsight
from app.models.analysis_result import AnalysisResult
from app.models.ask_history import AskHistory
from app.models.dataset import Dataset


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(
    title="AI Business Analytics Assistant",
    description=(
        "AI-powered dataset analysis and "
        "business insights API"
    ),
    version="1.0.0",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://ai-business-analytics-assistant.vercel.app",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload_router)
app.include_router(ask_router)


@app.get("/")
def root():
    return {
        "message": (
            "AI Business Analytics Assistant API "
            "is running"
        )
    }