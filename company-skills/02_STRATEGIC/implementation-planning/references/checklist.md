# Implementation Planning — Quality Checklist

Run before delivering MASTER_PLAN.md and PHASE_*.md docs.

## Gate 1 — Plan-level coverage

- [ ] MASTER_PLAN.md Section 1: Goal, constraints, success criteria, out-of-scope all populated
- [ ] Section 3: Phase summary table has effort + duration for every phase
- [ ] Section 4: Cross-phase dependency graph or table present
- [ ] Section 5: ≥3 plan-level risks with mitigations
- [ ] Section 6: Verification gate criteria for every phase
- [ ] Section 7: Plan-level rollback strategy table
- [ ] Section 8: Phase decomposition mode documented
- [ ] All chosen-mode requirements (e.g., source doc for Mode B) populated

## Gate 2 — Phase-level coverage

For each PHASE_*.md file:

- [ ] Context section explains WHY this phase exists (not just what)
- [ ] Inputs (preconditions) and Outputs (postconditions) are observable
- [ ] WP sequence with dependency table
- [ ] Every WP has the full structure: goal, effort, owner, deps, files, AC, tests, TCs, risks, rollback, PR title
- [ ] Verification Gate at end with explicit pass criteria
- [ ] WP count is 4-12 per phase (else justify in Notes)

## Gate 3 — WP-level rigor

For every WP:

- [ ] Goal is one sentence; not "improve X" but "do Y so that Z"
- [ ] Effort is XS/S/M/L; if L, justify why not split
- [ ] Files affected lists ≤10 files (else split)
- [ ] Acceptance criteria are observable, not vague
- [ ] At least 1 unit test specified
- [ ] At least 1 manual TC specified
- [ ] Risks section non-empty (every WP has ≥1 risk)
- [ ] Rollback plan specific, not "git revert"
- [ ] AI agent execution notes preserved (do not delete)

## Gate 4 — Sequencing realism

- [ ] No WP depends on a WP in a later phase
- [ ] Within a phase, parallelism explicit
- [ ] Total phase duration accounts for review/QA time (~20%) and buffer (15-25%)
- [ ] Calendar duration expressed as range, not point estimate

## Gate 5 — Scope discipline

- [ ] No WP bundles unrelated changes
- [ ] No WP includes solution design ("decide between approach A vs B" — that's `tech-solution-design`)
- [ ] No WP is a vague "improve area X" research task
- [ ] Verification gates do NOT include subjective tests ("looks good", "feels stable")

## Gate 6 — Inputs honesty

- [ ] MASTER_PLAN Section 8 lists which input docs were available vs missing
- [ ] If inputs missing, the gaps are documented as Open Questions (not invented)
- [ ] Confidence rating reflects how much was inferred vs derived

## Gate 7 — AI-agent executability

A WP must be executable by an AI agent under human supervision. Verify:

- [ ] Files affected explicitly enumerated (not "wherever needed")
- [ ] Acceptance criteria do not require judgment calls beyond the WP scope
- [ ] Rollback plan is mechanical (steps, not heuristics)
- [ ] No WP requires "talk to product to clarify" mid-execution (that should be resolved before WP starts)

## Gate 8 — Format

- [ ] MASTER_PLAN.md at `docs/02_STRATEGIC/MASTER_PLAN.md`
- [ ] PHASE_*.md at `docs/03_EXECUTION/work-packages/PHASE_<N>_<NAME>.md`
- [ ] WP IDs follow `WP-<phase>.<letter>` (e.g., WP-0.A, WP-2.H)
- [ ] TC IDs follow `TC-<phase><letter>-<NN>` (e.g., TC-0A-01)
- [ ] Section headings match templates

## Self-review prompt

Re-read the plan as the engineer who'll execute Day 1. Ask: "If I started Phase 0 WP-0.A right now, would I know exactly what to do?" If not, the plan is too abstract. Sharpen.

Then re-read as the tech lead who'll be paged at 2am if something breaks. Ask: "If WP-2.B breaks production, do I know how to roll back without losing data?" If not, the rollback section is incomplete.
