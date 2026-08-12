# FinLens — Final Prototype Draft

## 1. The Problem: The "Hidden Debt" Crisis

Millions of people sign complex financial documents — home loans, insurance policies, property agreements — without understanding the jargon, hidden penalties, and ambiguous clauses buried inside them.

**Result:** People overpay in interest, get trapped by foreclosure penalties, or discover too late that their insurance doesn't cover them.

**Gap:** Hiring a lawyer is expensive (₹5,000+), and generic AI chatbots are unreliable black boxes that hallucinate advice. There's no tool offering instant, auditable, personalized risk analysis for retail financial documents.

## 2. The Solution: FinLens

FinLens is a **Comparative Trade-off Engine** — a digital financial auditor that:
- Analyzes multiple documents simultaneously
- Contextualizes risk based on the user's personal profile (age, income, goals)
- Compares terms against live market benchmarks
- Delivers a plain-English verdict on which option fits the user best

## 3. Core Features & User Journey

**Step 1 — Personalized Onboarding**
Four questions build a User Risk Profile:
- Age / career stage (flexibility needs)
- Income & existing EMIs (affordability)
- Risk appetite (safety vs. savings)
- Primary goal (e.g. "lowest EMI" vs. "pay off early")

**Step 2 — Multi-Document Upload**
Users upload 4–5 plans (e.g. HDFC, SBI, ICICI loan offers, or competing mutual fund/investment plans) at once; processed in parallel.

**Step 3 — Agentic Analysis Workflow (LangGraph)**
- **Classifier** — identifies document type (loan / insurance / property / investment plan)
- **Extractor** — pulls critical numbers (interest rates, penalties, fees, expected returns, lock-in periods, exit loads) via structured Pydantic schemas
- **Market Watcher** — runs live web search for current rates, fee benchmarks, and fund/scheme performance data, validated against a curated reference dataset as fallback
- **Trade-off Engine** — compares extracted data against the user's profile and benchmark data

**Step 4 — Verdict Dashboard**
- **Match Scores** — each option scored 0–100 against the user's profile
- **Trade-off Highlights** — e.g. "Bank A has a lower rate, but Bank B allows free prepayment, which suits your goal to pay off early"
- **Final Recommendation** — a clear, conditional verdict, e.g. "Choose SBI if you value flexibility; choose HDFC if you want payment stability" or "Fund A suits your goal if you can hold through the lock-in; Fund B fits if you need earlier liquidity"
- **Sourced numbers** — every fetched figure shows its source, so the verdict is auditable, not a black box

## 4. Technical Architecture

| Component | Technology | Why |
|---|---|---|
| Orchestration | LangGraph | Stateful multi-agent workflow, modular nodes |
| Backend API | FastAPI (Python) | High performance, async, ML-friendly |
| Frontend | React + TypeScript | Interactive comparison tables and sliders |
| LLM Engine | Claude | Reasoning for legal/financial text extraction |
| Live Data | Tavily Search / web search | Current market rates, validated against seed dataset |
| Structure | Pydantic | Enforces valid, hallucination-resistant JSON output |
| Database | SQLite / PostgreSQL | User profiles, document traces, analysis history |

**Market Watcher design:** live search runs first; the returned figure is validated (format/sanity checked) and if it fails or returns nothing, the system falls back to a small curated reference table of known current rates. This keeps the demo reliable while still genuinely using live data, not hardcoded numbers alone.

## 5. Competitive Advantage

- **Context-aware:** a 2% penalty is high-risk for a 25-year-old, low-risk for a 60-year-old — same clause, different verdict
- **Comparative, not single-document:** pits offers against each other rather than summarizing one in isolation
- **Live market intelligence:** benchmarks pulled from current web data, not static/stale tables
- **Auditable:** every number in the verdict is source-linked

## 6. Feasibility & Roadmap

**Current status:** Prototype architecture designed, LangGraph workflow mapped.

**Development strategy — "Product-First":** advanced prompt engineering + live search instead of building a custom labeled dataset upfront. Working MVP achievable in 8 weeks.

**Scalability:** modular LangGraph design — new document types (credit cards, mutual funds) added as new agent nodes without rewriting the core engine.

**Deferred to later phases (not in this prototype):**
- Human-in-the-Loop clarification pauses — real value, but adds significant state-persistence engineering (resuming a graph mid-session) that isn't necessary to prove the core idea
- Banking agreements, credit cards (Phase 2)
- B2B API for fintechs/banks (Phase 3)

## 7. The Vision

FinLens starts with loans, insurance, property agreements, and investment plans. It isn't just reading your contract — it's protecting your financial future.
