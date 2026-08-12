"""
LangGraph Pipeline Definition

Defines the stateful graph with four nodes:
Classifier → Extractor → Market Watcher → Trade-off Engine

This is a stub — nodes return dummy data. Real logic comes in Phases 4–7.
"""

from app.graph.state import GraphState
from app.graph.classifier import classify_documents
from app.graph.extractor import extract_fields
from app.graph.market_watcher import fetch_benchmarks
from app.graph.tradeoff_engine import compute_tradeoffs


def build_graph():
    """
    Build and return the LangGraph pipeline.

    Stub: Returns a simple callable that chains the four nodes sequentially.
    Will be replaced with a proper StateGraph in Phase 3.
    """

    async def run_pipeline(state: GraphState) -> GraphState:
        """Execute all four nodes in sequence."""
        state = classify_documents(state)
        state = extract_fields(state)
        state = fetch_benchmarks(state)
        state = compute_tradeoffs(state)
        return state

    return run_pipeline
