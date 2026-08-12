"""
FinLens API Routes

Stub routes for upload, profile, analyze, and results.
Will be fully implemented in Phase 2.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
async def api_status():
    """API status check."""
    return {"status": "ok", "message": "FinLens API routes are active."}


# Phase 2:
# POST /api/upload      — accept 2–5 PDF files
# POST /api/profile     — accept UserProfile JSON
# POST /api/analyze     — trigger LangGraph pipeline
# GET  /api/results/{session_id} — return analysis results
