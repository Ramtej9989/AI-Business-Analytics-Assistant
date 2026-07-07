from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    dataset_id: Mapped[int] = mapped_column(
        ForeignKey(
            "datasets.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    data_quality: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    cleaning_recommendations: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    eda: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    correlations: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    chart_recommendations: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )