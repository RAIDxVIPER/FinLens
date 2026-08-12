"""
FinLens Backend Configuration

Loads environment variables and provides typed settings for the application.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from backend directory
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    """Application settings loaded from environment variables."""

    # API Keys
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./finlens.db")

    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent  # project root
    UPLOAD_DIR: Path = BASE_DIR / "data" / "uploads"
    SAMPLE_DOCS_DIR: Path = BASE_DIR / "data" / "sample_docs"
    MARKET_REFERENCE_PATH: Path = BASE_DIR / "data" / "market_reference.json"

    # Upload constraints
    MAX_UPLOAD_FILES: int = 5
    MIN_UPLOAD_FILES: int = 2
    ALLOWED_EXTENSIONS: set = {".pdf"}

    def __init__(self):
        # Ensure upload directory exists
        self.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


settings = Settings()
