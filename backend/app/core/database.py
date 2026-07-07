from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models.base import Base

import app.models


database_url = settings.DATABASE_URL

if database_url.startswith("postgresql://"):
    database_url = database_url.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1,
    )


engine = create_engine(
    database_url,
    pool_pre_ping=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_database_session():
    database = SessionLocal()

    try:
        yield database
    finally:
        database.close()


def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT version();")
        )

        return result.scalar()


def create_database_tables():
    Base.metadata.create_all(bind=engine)