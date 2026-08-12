"""
Trade-off Engine Node (Stub)

Scores each document 0–100 against the user profile and produces
conditional verdicts with trade-off highlights.
Stub: returns a hardcoded score of 75. Real logic in Phase 7.
"""

from app.graph.state import GraphState


def compute_tradeoffs(state: GraphState) -> GraphState:
    """Score documents and generate verdicts. STUB — returns hardcoded results."""
    extractions = state.get("extractions", [])

    match_results = []
    for i, ext in enumerate(extractions):
        match_results.append({
            "document_id": ext["document_id"],
            "document_label": ext["data"].get("lender_name", ext["data"].get("insurer_name", f"Document {i+1}")),
            "score": 75,
            "score_breakdown": {
                "interest_rate": 25,
                "flexibility": 20,
                "fees": 15,
                "tenure_fit": 10,
                "market_comparison": 5,
            },
            "highlights": [
                "[STUB] Competitive interest rate compared to market average.",
                "[STUB] Moderate prepayment flexibility.",
            ],
            "verdict": "[STUB] This is a placeholder verdict. Choose this option if you value stability.",
        })

    state["match_results"] = match_results
    return state
