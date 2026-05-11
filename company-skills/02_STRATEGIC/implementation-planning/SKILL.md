---
name: implementation-planning
description: Decompose a tech solution into a multi-phase implementation plan with work packages (WPs). Each WP is sized for a single PR and includes scope, files, tests, acceptance criteria, and effort estimate. Produces a MASTER_PLAN.md plus per-phase WP documents that AI agents can execute under human supervision. Use when converting a solution design into actionable engineering work, breaking down a refactor or migration, or generating Phase 2/3 output for the company doc standard. Triggers include "plan the implementation", "break this into work packages", "generate an implementation plan", "create WP documents", "MASTER_PLAN", or "Phase 2/3 planning".
---

# Implementation Planning

Convert a solution design into an executable plan: phases → work packages → tests → acceptance criteria. Output is structured for AI-agent execution under human supervision.

## When this skill applies

Use when:
- A solution design exists (`TECH_SOLUTION_DESIGN.md`) and needs to be turned into actionable work
- A refactor / migration / rewrite needs a multi-week plan
- An existing project plan needs reformatting into the company WP standard
- An AI agent will execute the plan and you need WPs sized appropriately for them

Do NOT use for:
- Solution design itself (use `tech-solution-design` first)
- Quick tactical fixes that don't span phases (just open a single PR)
- Greenfield product roadmap (different scope; this is about engineering execution)

## Inputs (must read first)

Before planning, read in order:

1. `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` (or equivalent solution doc) — what to build
2. `docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md` — scope and budget constraints
3. `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md` — debt that may need bundling into the plan
4. `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` — risks the plan must mitigate
5. `docs/01_DISCOVERY/CODEBASE_MAP.md` — structural reality the plan must respect

If these don't exist, plan creation will be guesswork. Either run prior skills first or document missing inputs as Open Questions.

## Outputs

Multiple files:
- `docs/02_STRATEGIC/MASTER_PLAN.md` — phase overview, timeline, dependencies
- `docs/03_EXECUTION/work-packages/PHASE_<N>_<NAME>.md` — one per phase, containing all WPs

Plus optionally:
- `docs/03_EXECUTION/00_TESTING_INFRASTRUCTURE.md` — if no test framework yet
- `docs/03_EXECUTION/B_QA_CHECKLIST_MASTER.md` — aggregated test cases

Templates: [assets/MASTER_PLAN_template.md](assets/MASTER_PLAN_template.md), [assets/PHASE_template.md](assets/PHASE_template.md), [assets/WP_template.md](assets/WP_template.md).

## Workflow

### Step 1 — Establish scope, constraints, success criteria

From inputs, extract:
- **Goal:** what the plan achieves (1 sentence)
- **Constraints:** budget, deadline, headcount, must-not-break commitments
- **Success criteria:** measurable, time-bound (e.g., "Phase 0 complete with 0 P0 findings remaining")
- **Out of scope:** what this plan does NOT do (often more important than what it does)

Document these in MASTER_PLAN Section 1.

### Step 2 — Choose phase decomposition mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard 5-phase** *(default)* | Mid-size technical migration / refactor | Pre-Flight → Quick Wins → Dual-Write → Switch → Compliance |
| **B — Honor existing phase structure** | Project already has its own SDLC phases (per ADR or company standard) | Project's phases |
| **C — User-defined phases** | User specifies phases (e.g., "by quarter", "by epic", "by release train") | User input |

Selection logic:
1. User explicit → use it.
2. Project has ADR or company standard defining phases → ask user (Mode A or B?).
3. Default → Mode A.

#### Mode A — Standard 5-phase model

Adapted from FinanceOS-style migrations. Phases are about *risk progression*, not feature areas:

| Phase | Purpose | Typical content |
|-------|---------|-----------------|
| **0 — Pre-Flight** | Remove blockers; setup foundation | Critical security/auth fixes, observability, test framework, infra setup |
| **1 — Quick Wins** | Low-risk improvements that buy headroom | Caching, pagination, rate limiting, easy bugs |
| **2 — Dual-Write** | Build new path alongside old; verify equivalence | New service layer, dual-write to old + new, reconciliation |
| **3 — Switch / Cut-over** | Move traffic to new path with rollback | Gradual rollout (5%→25%→50%→100%), monitor, kill switch |
| **4 — Compliance / Cleanup** | Finalize, remove legacy, satisfy regulations | Delete old paths, MFA/GDPR/audit, DR drill |

Not every project needs all 5. Drop phases that don't apply (and document why in Notes).

#### Mode B — Honor existing structure

Common existing structures:
- Inception / Construction / Transition (RUP-style)
- MVP / Iteration 1 / Iteration 2 / GA
- Discovery / Design / Build / Validate / Release
- Per quarter / per release train

Use the project's names. Map standard concepts (risk progression) into their phases where possible.

#### Mode C — User-defined

Common user-supplied:
- "By release: v3.0 / v3.1 / v3.2"
- "By team: Platform team / Product team / Mobile team"
- "By risk: must-have / should-have / could-have"

Confirm phases with user; document rationale in Notes.

### Step 3 — Decompose each phase into Work Packages (WPs)

A Work Package = the unit of execution. Properties:

- **Single PR scope:** one WP = one PR. If it can't be reviewed in one sitting, it's too big.
- **Single concern:** WP fixes/builds one thing; do not bundle unrelated changes.
- **Fully testable:** acceptance criteria must be observable by tests OR by a manual smoke test.
- **Effort sized:** XS (<2h), S (2-8h), M (1-3 days), L (>3 days — split if possible).
- **ID format:** `WP-<phase>.<letter>` (e.g., WP-0.A, WP-2.H).

Decomposition heuristics:
- One WP per `tech-debt-audit` finding being addressed (or per cluster if related)
- One WP per architectural unit being introduced (e.g., new service, new middleware)
- One WP per migration step (schema, dual-write, switch read, cleanup)
- WPs that are "set up the framework for X" deserve their own WP (`00_TESTING_INFRASTRUCTURE` style)

Aim for: 4-12 WPs per phase. Fewer means under-decomposed; more means phase should split.

### Step 4 — For each WP, define structure

Use the [assets/WP_template.md](assets/WP_template.md) format:

```
WP-X.Y: <Title>

Goal: <one sentence>
Effort: <XS/S/M/L>
Owner: <role or person, defaults to "Backend dev" / "Frontend dev" / etc.>
Dependencies: <other WPs that must complete first>
Files affected: <list>
Acceptance criteria: <bullet list, each verifiable>
Unit tests: <list of test cases — "Test that X does Y when Z">
Manual test cases: <list of TC IDs and scenarios>
Risks: <what could go wrong>
Rollback plan: <how to revert if WP breaks something>
```

Every WP must have testable acceptance criteria. "Improves error handling" is NOT acceptance criteria — "All `catch` blocks in `src/api/` log errors via `logger.error` and re-throw if non-recoverable" is.

### Step 5 — Define Verification Gates between phases

Between each phase, a Verification Gate: a checklist that MUST PASS before the next phase starts. Examples:

- Gate 0 (after Phase 0): "All P0 findings closed; CI green; Sentry capturing errors; deploy reversible"
- Gate 1: "Phase 1 reduced [metric] by [%]; no production incidents introduced"
- Gate 2: "Dual-write parity verified for 7 consecutive days; reconciliation cron clean"

Gates prevent moving forward when ground truth says you shouldn't.

### Step 6 — Sequence WPs (dependency graph)

Within and across phases, identify dependencies:

- **Hard dependencies:** WP-B cannot start until WP-A merges
- **Soft dependencies:** WP-B is easier after WP-A but not blocking
- **Parallelizable:** WPs that can run in parallel (often most of them)

Build a Mermaid graph or simple dependency table in MASTER_PLAN Section 4.

### Step 7 — Estimate timeline

For each phase:
- Sum WP efforts (in days)
- Apply parallelism factor (1.0 = solo dev; 0.6 = 2-dev parallelism, accounting for coordination)
- Add buffer (15-25% for unknowns)
- Add review/QA time (~20% of dev time)

Result: phase duration in calendar days. Sum to get plan duration.

DO NOT pretend precision. Express as ranges: "5-7 working days for Phase 0".

### Step 8 — Identify risks and unknowns

Plan-level risks (different from per-WP risks):
- "If Supabase free tier limits change, Phase 2 budget assumption breaks"
- "If team loses developer X, Phase 3 timeline doubles"
- "If user count grows >2x during plan, we need to start Phase 4 earlier"

Document in MASTER_PLAN Section 5.

### Step 9 — Generate output documents

For each phase, generate `PHASE_<N>_<NAME>.md` from [assets/PHASE_template.md](assets/PHASE_template.md), containing:
- Phase overview
- Phase-level acceptance (Verification Gate)
- All WPs in the phase (using WP template structure)

Plus generate `MASTER_PLAN.md` from [assets/MASTER_PLAN_template.md](assets/MASTER_PLAN_template.md).

### Step 10 — Self-review

Run [references/checklist.md](references/checklist.md). Do not deliver until all gates pass.

## Quality bar

A good implementation plan lets:
- A new developer pick up any WP and start coding within 30 minutes
- An AI agent execute a WP under human supervision with no architectural surprises
- A project manager track progress (X of Y WPs done) and forecast finish
- A tech lead refuse to ship Phase N+1 if Verification Gate N didn't pass

If the plan can't pass these tests, it's not ready.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: solo-dev plans, AI-agent-executed plans, regulated-industry plans, accelerated/MVP plans.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Voyager", a logistics tracking platform migration, broken into 5 phases / 28 WPs.

## Failure modes to avoid

- **WPs too big.** If a WP requires touching 20 files across 3 services, it's not one PR. Split.
- **Acceptance criteria fluffy.** "Improves performance" — not testable. "P95 latency on /api/orders < 200ms in load test" — testable.
- **Skipping gates.** "We'll just push through" — every project that says this regrets it. Gates exist because the next phase has hidden dependencies on the previous one being actually done.
- **Optimistic timelines.** A "1-day WP" is rarely 1 day with review, deploy, smoke test. Use the formula in Step 7 honestly.
- **No rollback plan per WP.** If something breaks in production after merge, knowing how to revert SAFELY is the difference between minor incident and major outage.
- **Bundling unrelated changes.** "While I'm in there, I'll also fix Y" — no. Y becomes its own WP.
- **Ignoring `tech-debt-audit` findings.** If the audit said something is P0 and the plan doesn't address it, document why or include it.
