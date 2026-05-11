---
name: feasibility-assessment
description: Produce a business-case feasibility assessment for a proposed technical solution, evaluating ROI, cost, risk, and benefit across multiple scenarios (full / partial / minimum scope). Translates technical findings into stakeholder-readable business decisions. Use when a Phase 1 audit identified problems and the team must justify investment to leadership/investors, when comparing build-vs-buy or rewrite-vs-refactor decisions, when budgeting an engineering initiative, or when generating Phase 2 Strategic feasibility output. Triggers include "is this worth doing", "ROI assessment", "business case", "feasibility study", "should we do this", "generate FEASIBILITY", or "Phase 2 Strategic feasibility".
---

# Feasibility Assessment

Convert technical findings (debt, risk, opportunity) into a business case that non-technical stakeholders can decide on. Output is `FEASIBILITY_ASSESSMENT.md` evaluating multiple scenarios with cost, ROI, risk, and benefit per scenario.

## When this skill applies

Use when:
- Phase 1 audits identified significant work; leadership must approve before engineering invests
- Build vs buy / rewrite vs refactor decision needs a structured comparison
- Budget request needs business-case backing
- Investor / board / customer needs technical justification in business language
- Producing Phase 2 Strategic feasibility output for company doc standard

Do NOT use for:
- Pure technical solution design (use `tech-solution-design`)
- Feature-level prioritization (too small; use product roadmap process)
- Operational expense planning (use FinOps/finance team)

## Inputs (must read first)

1. **`docs/00_REQUIREMENTS/CONTEXT_PACK.md`** *(strongly recommended, from `project-context-ingestion`)* — supplies stakeholder-stated budget cap (Section 7.3), regulatory deadlines (Section 7.1), competitor signals (Section 5), churn / cost / ops baselines (Section 6), and unresolved contradictions (Section 8 — these often determine which scenario is even viable). Without CONTEXT_PACK, items 5-6 below come from operator memory, which is unreliable across 60+ projects.
2. `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md` — what's broken / risky (cost of inaction)
3. `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` — data risks + cost projections
4. `docs/01_DISCOVERY/CODEBASE_MAP.md` — system shape (effort estimation context)
5. `docs/01_DISCOVERY/BUSINESS_CONTEXT.md` — value at risk if system fails
6. **External (or from CONTEXT_PACK):** known business goals, deadlines, competitor pressure, regulatory deadlines, current revenue, cost structure
7. **External (or from CONTEXT_PACK):** stakeholder constraints (budget cap, timeline, team capacity)

If Phase 1 outputs missing, the feasibility is guesswork. Don't write a feasibility from vibes. If CONTEXT_PACK is missing AND items 6-7 are gathered ad-hoc, mark confidence as MEDIUM at best in the report.

## Output

`docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md`, filled from [assets/FEASIBILITY_template.md](assets/FEASIBILITY_template.md).

## Workflow

### Step 1 — Define the question precisely

A feasibility assessment answers exactly one of:

- **"Should we do X?"** — go / no-go decision
- **"How much of X should we do?"** — scope decision (full / partial / minimum)
- **"X vs Y — which?"** — comparison decision (rewrite vs refactor; vendor A vs B)

Write the question in 1 sentence; verify with stakeholders before continuing. Each question type uses different scenarios in Step 4.

### Step 2 — Choose scenario mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard 3-scenario** *(default)* | "How much should we do?" question | Full / Partial / Minimum scope variants |
| **B — Honor company financial planning template** | Company has fixed feasibility format (e.g., per-quarter funding cycle) | Company template |
| **C — User-defined scenarios** | Specific comparison ("AWS vs GCP", "rewrite vs refactor", custom budget tiers) | User input |

Selection logic:
1. User explicit → use it
2. Company has budget-request template → ask user
3. Default → Mode A

#### Mode A — 3-scenario standard

| Scenario | Scope | Approx cost | Approx duration |
|----------|-------|-------------|-----------------|
| **Full** | All Phase 0-4 work | Highest | Longest |
| **Partial** | Phase 0 + 1 (urgent fixes + quick wins) | Medium | Medium |
| **Minimum** | Phase 0 only (critical security/blockers) | Lowest | Shortest |

Allows leadership to choose ambition level vs. budget.

#### Mode B — Company template

Common templates:
- "Quarterly investment proposal" (1 page exec summary + 3 page detail)
- "Capex justification" (long-form with depreciation schedule)
- "OKR-aligned proposal" (each scenario maps to OKR keyresults)

#### Mode C — User-defined

Examples:
- "Compare 3 vendors" (each vendor = scenario)
- "Compare 2 architectures" (rewrite vs migration)
- "Compare 4 budget tiers" (test elasticity of scope)

### Step 3 — Quantify cost of inaction

For each P0/P1 finding from `TECH_DEBT_AUDIT.md`, estimate the cost of NOT acting:

- **Direct cost:** customer churn, refund liability, incident response time
- **Opportunity cost:** features delayed because of debt friction
- **Risk cost:** probability × impact of incidents (data breach, outage, compliance fine)
- **Cost growth:** does this cost grow with scale? (often yes — accelerating)

Express in dollars/month or dollars/year where possible. If unmeasurable, use ranges or "Critical/High/Med/Low" with rationale.

This is the "do nothing" baseline. Without it, scenarios have nothing to be compared against.

### Step 4 — For each scenario: scope, cost, benefit

Use [assets/FEASIBILITY_template.md](assets/FEASIBILITY_template.md). For each scenario:

**Scope:**
- Specific WPs from implementation plan (or Phase 1 findings) included
- Explicit out-of-scope items

**Cost:**
- Engineering effort (hours × $/hr) — use loaded cost (~$150-250/hr for senior dev)
- Infrastructure cost delta (new tools, services)
- External cost (consultants, audits, vendors)
- Opportunity cost (what else won't happen during these N weeks)

**Benefit:**
- Direct savings (reduced infra cost, reduced support time)
- Risk reduction (fewer incidents × cost per incident)
- New capability (revenue from features unblocked)
- Compliance achievement (sales unblocked; regulatory fine avoided)

**Time-to-value:**
- When do benefits start materializing? (sometimes Phase 0 alone unlocks sales)
- Payback period

### Step 5 — Compare scenarios

Build a side-by-side comparison table:

| Dimension | Full | Partial | Minimum |
|-----------|------|---------|---------|
| Cost (one-time) | $X | $Y | $Z |
| Cost (annual ongoing) | $X | $Y | $Z |
| Annual benefit (Year 1) | $X | $Y | $Z |
| Annual benefit (Year 3) | $X | $Y | $Z |
| Payback period | months | months | months |
| Risk closed (#findings) | most | medium | minimal |
| Time-to-completion | weeks | weeks | weeks |

Add ROI calculation: `(Benefit - Cost) / Cost × 100%` for Year 1 and Year 3.

### Step 6 — Articulate assumptions

Every projection has assumptions. List them:

- "Assume 10x user growth in Year 2" (if false → benefit projections wrong)
- "Assume current vendor pricing stable" (if false → cost projections wrong)
- "Assume team size N" (if changes → timeline wrong)
- "Assume no major regulatory shift" (if false → scenarios may shift entirely)

Mark each assumption: confidence (High/Medium/Low), and what changes if violated.

### Step 7 — Risks of each scenario

Each scenario has unique risks (separate from cost-of-inaction):

| Scenario | Top risks |
|----------|-----------|
| Full | Resource depletion; team burnout; longer time before any benefit lands |
| Partial | Doesn't fully close compliance gap; compounding debt resumes |
| Minimum | Defers risk rather than resolves; audit/incident may force redo at higher cost |

Quantify risks where possible.

### Step 8 — Recommendation

Most stakeholders prefer a clear recommendation, even if they choose otherwise.

State:
- Which scenario the analysis supports
- Why (top 2-3 reasons)
- What conditions would change the recommendation
- What stakeholder must decide

Recommendation must be defensible from the analysis — do not surprise the reader.

### Step 9 — Self-review

Run [references/checklist.md](references/checklist.md). Feasibility assessments are read by skeptical audiences — verify rigor.

## Quality bar

A good feasibility assessment lets:
- A non-technical exec understand the trade-offs in 5-10 minutes
- A finance/budget owner see the numbers (cost, benefit, payback)
- A board member trust the analysis (assumptions explicit, not hidden)
- A skeptic challenge specific lines without invalidating the whole thing

If the document is "we should definitely do this because we should", it's not a feasibility — it's marketing. Strip and rebuild.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: regulated industries (compliance NPV), early-stage startups (lean cost models), enterprise procurement (NPV/IRR rigor), nonprofits (mission impact framing).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Pegasus" — logistics platform deciding between full rewrite, partial refactor, and minimum stabilization.

## Failure modes to avoid

- **Cost-only analysis.** Without benefit and risk quantification, "$X to do this" is unanswerable.
- **Inflated benefit claims.** Don't promise 10x revenue. Use conservative estimates with confidence bands.
- **Vague costs.** "About $200K" — based on what? Show the breakdown.
- **Single-scenario "yes" papers.** A feasibility with 1 option is advocacy, not analysis. Always include "do nothing" + alternatives.
- **Hiding assumptions.** Stakeholder will find them anyway; better to surface and own them.
- **Engineering-only ROI.** Include impact on sales, support, customer success, finance, legal — these are downstream effects of technical debt.
- **Pretending precision.** "$487,234 cost" implies a precision feasibility doesn't have. Use ranges.
