"""
FinLens Database Setup

SQLite engine, session factory, and table creation helper.
Stub — will be fully implemented in Phase 2.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite-specific
    echo=settings.ENVIRONMENT == "development",
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_tables():
    """Create all database tables. Called on app startup."""
    from app.db import models as _  # noqa: F401 — import to register models
    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency: yields a DB session, closes it after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
