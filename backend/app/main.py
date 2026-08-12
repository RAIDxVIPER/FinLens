"""
FinLens — FastAPI Application Entrypoint

Main application setup with CORS, route mounting, and health check.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.db.database import create_tables

app = FastAPI(
    title="FinLens API",
    description="Comparative financial-document auditor — upload competing offers, get a personalized verdict.",
    version="0.1.0",
)

# CORS — allow frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    """Create database tables on startup."""
    create_tables()


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "service": "finlens-api", "version": "0.1.0"}


# Mount API routes
app.include_router(api_router, prefix="/api")
