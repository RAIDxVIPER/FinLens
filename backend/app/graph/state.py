"""
LangGraph Shared State Model

Defines the TypedDict that flows through all graph nodes.
This is a stub — will be fully typed in Phase 1.
"""

from typing import TypedDict, Any


class GraphState(TypedDict, total=False):
    """Shared state passed between all LangGraph nodes."""
    # Raw inputs
    document_paths: list[str]
    user_profile: dict[str, Any]

    # Classifier output
    classifications: list[dict[str, Any]]

    # Extractor output
    extractions: list[dict[str, Any]]

    # Market Watcher output
    benchmarks: list[dict[str, Any]]

    # Trade-off Engine output
    match_results: list[dict[str, Any]]

    # Metadata
    session_id: str
    errors: list[str]
