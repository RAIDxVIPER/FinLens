# FinLens — Build Plan & Project Brief

> Read this file completely before writing any code. It is the source of truth for scope,
> architecture, and current status. Update the **Status Log** at the bottom every time you
> finish a milestone — don't let this file drift out of sync with the repo.

## 1. What FinLens Is

A comparative financial-document auditor. A user uploads 2–5 competing financial offers
(loan agreements, insurance policies), answers 4 quick profile questions, and gets a
plain-English, source-cited verdict on which offer fits them best — not a single-document
summarizer, not a generic chatbot.

**One-line pitch:** "The credit score for your financial documents."

**Not this project:** a general AI legal advisor, a robo-advisor that manages money, a
chatbot. Every feature must serve *compare documents → personalize → recommend*.

## 2. MVP Scope (locked for the first 8 weeks)

| In scope (v1) | Deferred |
|---|---|
| Loan agreements (home loans) | Property agreements |
| Insurance policies | Investment plans / mutual funds |
| 2–5 documents per session | Banking / credit card docs (Phase 2) |
| 4-question profile (age, income+EMIs, risk appetite, goal) | Human-in-the-loop clarification pauses |
| — | B2B API (Phase 3) |

Reasoning: the pptx narrows MVP to loans+insurance for a realistic semester timeline; the
draft's broader four-type scope is the Phase 1.5 target once the core pipeline is proven.
**If this assumption is wrong, say so before Phase 0 starts — the Pydantic schemas below are
built around two document types and expanding later is a new-agent-node exercise, not a
rewrite, but it's not free.**

## 3. Architecture

```
Upload (2-5 PDFs) + Profile Form
        │
        ▼
  ┌─────────────┐
  │ Classifier   │  → tags each doc: "loan" | "insurance"
  └─────────────┘
        │
        ▼
  ┌─────────────┐
  │ Extractor    │  → pulls structured fields per Pydantic schema (below)
  └─────────────┘
        │
        ▼
  ┌─────────────┐
  │ Market       │  → live web search (Tavily) for current rates/benchmarks
  │ Watcher      │     validated + falls back to curated reference table on failure
  └─────────────┘
        │
        ▼
  ┌─────────────┐
  │ Trade-off    │  → scores each doc 0-100 against user profile,
  │ Engine       │     produces conditional verdict + trade-off highlights
  └─────────────┘
        │
        ▼
  Dashboard: match scores, highlights, verdict, full source trace
```

Orchestrated as a **LangGraph** stateful graph — each box above is one node. This is the
project's core technical bet: modularity (new doc type = new node), accuracy (narrow
prompts + Pydantic-enforced JSON), and auditability (every node's output is logged).

### Tech stack (confirmed, don't relitigate without a reason)

| Layer | Choice | Notes |
|---|---|---|
| Orchestration | LangGraph | one graph, four nodes, see above |
| Backend | FastAPI (Python, async) | |
| Frontend | React + TypeScript | comparison tables, sliders for What-If simulator |
| LLM | Claude (via Anthropic API) | extraction + trade-off reasoning |
| Live data | Tavily search, validated → curated fallback table | Market Watcher only |
| Schema enforcement | Pydantic | every agent output is a typed model, not free text |
| DB | SQLite (dev) → Postgres (later) | user profiles, doc traces, analysis history |

## 4. Data Contracts (write these first — everything else depends on them)

Define these as Pydantic models before any agent logic. Extraction quality lives or dies
on getting these fields right.

```python
class DocumentType(str, Enum):
    LOAN = "loan"
    INSURANCE = "insurance"

class UserProfile(BaseModel):
    age: int
    monthly_income: float
    existing_emis: float
    risk_appetite: Literal["low", "medium", "high"]
    primary_goal: str  # e.g. "lowest_emi", "pay_off_early", "max_coverage"

class LoanExtraction(BaseModel):
    lender_name: str
    interest_rate: float          # annual %, floating or fixed noted separately
    rate_type: Literal["fixed", "floating"]
    processing_fee: float
    prepayment_penalty_pct: float | None
    foreclosure_charges: float | None
    loan_tenure_years: float
    source_snippet: str           # exact text the field was extracted from — for audit trail

class InsuranceExtraction(BaseModel):
    insurer_name: str
    premium_annual: float
    coverage_amount: float
    exclusions: list[str]
    claim_settlement_ratio: float | None
    lock_in_years: float | None
    source_snippet: str

class MarketBenchmark(BaseModel):
    metric_name: str
    current_value: float
    source_url: str | None
    fetched_via: Literal["live_search", "fallback_table"]

class MatchResult(BaseModel):
    document_id: str
    score: int                    # 0-100
    score_breakdown: dict[str, int]   # e.g. {"interest_rate": 30, "flexibility": 25, ...}
    highlights: list[str]
    verdict: str                  # plain-English conditional recommendation
```

## 5. Repo Structure (create this on day 1)

```
finlens/
├── CLAUDE.md                 ← this file
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI entrypoint
│   │   ├── graph/             # LangGraph definition
│   │   │   ├── state.py       # shared graph state model
│   │   │   ├── classifier.py
│   │   │   ├── extractor.py
│   │   │   ├── market_watcher.py
│   │   │   └── tradeoff_engine.py
│   │   ├── schemas/           # Pydantic models from section 4
│   │   ├── db/                # SQLite models + session handling
│   │   └── api/               # routes: upload, profile, analyze, results
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/        # UploadZone, ProfileForm, MatchScoreCard, TradeoffTable
│   │   ├── pages/
│   │   └── api/                # client for backend routes
│   └── package.json
├── data/
│   └── market_reference.json   # curated fallback benchmarks
└── docs/
    └── agent_prompts/          # versioned prompts per node, reviewed like code
```

## 6. Milestones (8-week product-first MVP)

Team of 5: one strong UI/UX, one solid ML background, one Python-only, two ML/DS
beginners. Assign so beginners pair with the ML-strong member on agent logic, and the
Python-only member owns backend plumbing (DB, API routes, auth) rather than prompt work.

| Week | Milestone | Owner-shape |
|---|---|---|
| 1 | Repo scaffolded, Pydantic schemas finalized, FastAPI skeleton + SQLite models, React shell with upload UI | Python-only + UI/UX |
| 2 | Classifier node working on 10+ sample docs (loan vs insurance) | ML-strong + 1 beginner |
| 3–4 | Extractor node: structured extraction per schema, tested against messy real-world PDFs (scanned, multi-column) | ML-strong + both beginners |
| 5 | Market Watcher: Tavily integration + fallback table + validation logic | Python-only + 1 beginner |
| 6 | Trade-off Engine: scoring rubric, verdict generation, source-trace logging | ML-strong |
| 7 | Dashboard frontend: match score cards, trade-off table, audit trail view | UI/UX |
| 8 | End-to-end integration, QA on the full pipeline with real sample docs, demo script (3 loans + 1 insurance, per pptx demo flow) | whole team |

Each milestone should be independently demoable — don't let extraction and trade-off
scoring get built in parallel without a working classifier to feed them real data.

## 7. Immediate Next Steps (start here)

1. Confirm the MVP-scope assumption in section 2 (loans+insurance only) with the team.
2. Scaffold the repo structure in section 5.
3. Write and lock the Pydantic schemas in section 4 — get team sign-off before building
   any agent against them, since every downstream node depends on these shapes.
4. Collect 8–10 real (or realistic sample) loan and insurance documents now — extraction
   quality work in weeks 3–4 is blocked without a test corpus.
5. Set up Claude API access and Tavily API key; confirm rate limits won't block the
   Market Watcher's live-search calls during demo.
6. Build the LangGraph skeleton with four stub nodes that pass data through unchanged —
   get the plumbing working end-to-end before any node does real work.

## 8. Design Principles (don't drift from these)

- Every number the system shows must be source-linked — no unattributed figures in the verdict.
- Prefer one working feature over three half-built ones. Quality over feature count.
- The system assists a decision; it never issues unconditional advice ("Choose Loan B" is
  wrong — "Choose Loan B if you plan to repay early" is right).
- New document types come in as new graph nodes, not by rewriting the core engine.

## Status Log

- 2026-08-12 — Build plan drafted from pptx + final prototype draft. Nothing built yet.
