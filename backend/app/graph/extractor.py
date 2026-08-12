"""
Extractor Node (Stub)

Extracts structured financial fields from classified documents.
Stub: returns hardcoded dummy data. Real logic in Phase 5.
"""

from app.graph.state import GraphState


def extract_fields(state: GraphState) -> GraphState:
    """Extract structured data from each document. STUB — returns dummy data."""
    classifications = state.get("classifications", [])

    extractions = []
    for cls in classifications:
        if cls["doc_type"] == "loan":
            extractions.append({
                "document_id": cls["document_id"],
                "doc_type": "loan",
                "data": {
                    "lender_name": "Sample Bank",
                    "interest_rate": 8.5,
                    "rate_type": "floating",
                    "processing_fee": 10000.0,
                    "prepayment_penalty_pct": 2.0,
                    "foreclosure_charges": 5000.0,
                    "loan_tenure_years": 20.0,
                    "source_snippet": "[STUB] This is placeholder data.",
                },
            })
        else:
            extractions.append({
                "document_id": cls["document_id"],
                "doc_type": "insurance",
                "data": {
                    "insurer_name": "Sample Insurance Co.",
                    "premium_annual": 15000.0,
                    "coverage_amount": 5000000.0,
                    "exclusions": ["Pre-existing conditions"],
                    "claim_settlement_ratio": 96.5,
                    "lock_in_years": 5.0,
                    "source_snippet": "[STUB] This is placeholder data.",
                },
            })

    state["extractions"] = extractions
    return state
