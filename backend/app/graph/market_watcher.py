"""
Market Watcher Node (Stub)

Fetches live market benchmarks via Tavily search, with fallback to curated data.
Stub: returns hardcoded benchmarks. Real logic in Phase 6.
"""

from app.graph.state import GraphState


def fetch_benchmarks(state: GraphState) -> GraphState:
    """Fetch current market benchmarks. STUB — returns hardcoded data."""
    state["benchmarks"] = [
        {
            "metric_name": "Average Home Loan Interest Rate (India)",
            "current_value": 8.75,
            "source_url": None,
            "fetched_via": "fallback_table",
        },
        {
            "metric_name": "Average Term Insurance Premium (Age 30, ₹1Cr)",
            "current_value": 12000.0,
            "source_url": None,
            "fetched_via": "fallback_table",
        },
    ]
    return state
