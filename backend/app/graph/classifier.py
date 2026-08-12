"""
Classifier Node (Stub)

Tags each uploaded document as 'loan' or 'insurance'.
Stub: returns 'loan' for everything. Real logic in Phase 4.
"""

from app.graph.state import GraphState


def classify_documents(state: GraphState) -> GraphState:
    """Classify each document by type. STUB — returns 'loan' for all."""
    doc_paths = state.get("document_paths", [])

    classifications = []
    for i, path in enumerate(doc_paths):
        classifications.append({
            "document_id": f"doc_{i}",
            "file_path": path,
            "doc_type": "loan",
            "confidence": 0.95,
        })

    state["classifications"] = classifications
    return state
