---
name: phase-1-discovery-orchestrator
description: Orchestrate the full Phase 1 Discovery pipeline by running 4 component skills sequentially with operator checkpoints. ONLY for legacy projects (codebase exists). Component skills: codebase-discovery → data-architecture-audit → business-context-capture → tech-debt-audit. Some steps can run in parallel. Use when onboarding to existing codebase, before reverse-engineering SRS, or when refreshing all Discovery docs after major refactor. Triggers include "run phase 1", "discovery pipeline", "explore legacy codebase", "all phase 1 skills", or "phase 1 full run".
---

# Phase 1 Discovery Orchestrator

Coordinate end-to-end execution of Phase 1 Discovery skills for a legacy project. Replaces 4 manual skill invocations with one orchestrated run.

## When this orchestrator applies

Use when:
- Onboarding to legacy codebase that has no Discovery docs
- Refreshing Phase 1 after major refactor (rewrite, dependency upgrade, architecture change)
- Pre-rewrite work — capture as-is state before designing to-be
- Pre-Phase 0 SRS for legacy — Phase 1 is mandatory input

Do NOT use orchestrator for:
- Greenfield projects (no code → Phase 1 doesn't apply)
- Single-skill update (e.g., refresh CODEBASE_MAP only)
- Cross-cutting investigation that doesn't fit 4 skills

## Component skills

| # | Skill | Output | Parallelizable? |
|---|-------|--------|-----------------|
| 1 | `codebase-discovery` | `01_DISCOVERY/CODEBASE_MAP.md` | Step 1 first |
| 2 | `data-architecture-audit` | `01_DISCOVERY/DATA_ARCHITECTURE.md` | Can parallel with Step 3 after Step 1 |
| 3 | `business-context-capture` | `01_DISCOVERY/BUSINESS_CONTEXT.md` | Can parallel with Step 2 after Step 1 |
| 4 | `tech-debt-audit` | `01_DISCOVERY/TECH_DEBT_AUDIT.md` | Step 4 last (depends on 1-3) |

**Dependency graph:**
```
Step 1 (codebase-discovery)
    ↓
    ├─→ Step 2 (data-architecture-audit) ─┐
    └─→ Step 3 (business-context-capture)─┤
                                          ↓
                                       Step 4 (tech-debt-audit)
```

## Modes

| Mode | Description | When |
|------|-------------|------|
| **A — Supervised sequential** *(default)* | Run Step 1 → 2 → 3 → 4 with operator review between | First run, audit-grade |
| **B — Supervised parallel** | Run Step 1, then Step 2+3 parallel, then Step 4 | Time-pressured runs |
| **C — Express** | Chain through with minimal pauses | Refresh runs |
| **D — Selective** | Operator pre-specifies skill subset | Targeted refresh |

## Pre-flight check

Before Step 1:

1. **Project is legacy?** Verify `src/` (or equivalent) has non-trivial code.
   - If empty → ABORT: "Phase 1 only for legacy. Skip to Phase 0 greenfield."
2. **Codebase access:** Read access to repo confirmed.
3. **CONTEXT_PACK exists?** Recommended but not required.
   - If exists → cross-reference will be richer in business-context-capture
   - If missing → operator confirms proceeding without

## Workflow

### Step 0 — Pre-flight + plan

```
Orchestrator output:
"Phase 1 Discovery pipeline starting.

Detected: legacy project (X files in src/, Y in lib/).
CONTEXT_PACK: [present | missing]
Mode: [A | B | C | D]
Skills:
  1. codebase-discovery (~2 hr)
  2. data-architecture-audit (~1.5 hr)
  3. business-context-capture (~2.5 hr)
  4. tech-debt-audit (~3 hr)

Estimated total: 9-10 hr AI + 2-3 hr operator review.

Proceed? [yes/no]"
```

### Step 1 — `codebase-discovery`

**Why first:** All other Phase 1 skills need a structural map of the code.

**Run:**
- Sample-based deep dive on src/, scan tests/, ghi chú config/
- Output: `docs/01_DISCOVERY/CODEBASE_MAP.md`

**Checkpoint:**
```
Step 1 complete.

Summary:
- N entry points identified
- M top-level modules mapped
- K external dependencies catalogued
- Build/run/test commands documented
- Coverage: X% files read directly, Y% sampled

Mode A — pause for operator review.
Mode B/C — auto-continue if Coverage ≥70%.
```

### Steps 2 + 3 — Parallel branch (data + business)

In Mode B (parallel), dispatch both:

**Step 2 — `data-architecture-audit`**
- Inputs: codebase + DB schemas + cloud config + CODEBASE_MAP
- Output: `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`
- Focus: PII, retention, encryption, governance

**Step 3 — `business-context-capture`**
- Inputs: codebase + CODEBASE_MAP + (optional) CONTEXT_PACK
- Output: `docs/01_DISCOVERY/BUSINESS_CONTEXT.md`
- Focus: actors, use cases, business rules, workflows, invariants

**Synchronization:** Both must complete before Step 4. If one is faster, operator can review while waiting.

**Checkpoint after both:**
```
Steps 2 + 3 complete.

DATA_ARCHITECTURE summary:
- N storage layers (DB, cache, blob, queue)
- M PII fields identified (cross-ref CONTEXT_PACK Section 7.1 if exists)
- K data flows mapped
- L governance findings

BUSINESS_CONTEXT summary:
- N actors
- M use cases
- K business rules (validation/calculation/eligibility)
- L workflows
- P invariants

⚠️ Code-vs-stakeholder mismatches: N items
(BUSINESS_CONTEXT cross-referenced with CONTEXT_PACK Section 3 if available)

Mode A — pause for operator review.
```

### Step 4 — `tech-debt-audit`

**Inputs:** All 3 prior Phase 1 outputs.

**Run:**
- Sample-based deep dive (30% of important files)
- Severity calibration: Critical / High / Medium / Low
- Cost-of-inaction + cost-to-fix per finding

**Output:** `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md`

**Checkpoint:**
```
Step 4 complete.

Summary:
- N findings: X Critical, Y High, Z Medium, W Low
- M systemic patterns identified
- Total cost-to-fix estimate: $K (rough)
- Total cost-of-inaction baseline: $L (rough)

Top 3 Critical:
[list]
```

### Step 5 — Phase report

Generate `docs/01_DISCOVERY/_phase_report_<DATE>.md`:

```markdown
# Phase 1 Run Report — <DATE>

## Skills run
- ✅ codebase-discovery
- ✅ data-architecture-audit
- ✅ business-context-capture
- ✅ tech-debt-audit

## Outputs (4 files in 01_DISCOVERY/)

## Quality gates
- [ ] Each component skill checklist passed
- [ ] Code-vs-stakeholder mismatches surfaced (not papered over)
- [ ] Tech debt severity calibrated honestly

## Next: Phase 0 (srs-reverse-engineer)
```

## Error recovery

| Failure | Action |
|---------|--------|
| Pre-flight: not legacy | Abort, recommend Phase 0 greenfield |
| Step 1 read errors | Retry with restricted scope; partial CODEBASE_MAP acceptable |
| Step 2 DB access denied | Skip data audit, mark as gap, proceed to Step 3 |
| Step 3 ambiguous business logic | Capture ambiguities as Open Questions; don't invent |
| Step 4 too many "Critical" | Force re-calibration: max 10 Critical for typical project |
| Mid-pipeline timeout | Resume from last completed step |

## Quality gate (orchestrator-level)

- [ ] All 4 component skills' checklists passed
- [ ] CODEBASE_MAP coverage statement honest (% read vs sample)
- [ ] DATA_ARCHITECTURE PII section explicit (no implicit "we have PII somewhere")
- [ ] BUSINESS_CONTEXT invariants section non-empty
- [ ] TECH_DEBT severity not inflated (Critical ≤ 10)
- [ ] Phase report generated

## Hand-off

After successful run:
- → Phase 0 orchestrator (legacy SRS reverse-engineer)
- → Phase 2 orchestrator (feasibility-assessment uses tech-debt-audit findings)
- → INDEX.md refresh

## Failure modes

- **Running for greenfield:** pre-flight catches; if forced, output is meaningless
- **Step 1 sampled too lightly:** downstream skills inherit blind spots; ≥70% coverage target
- **Skipping Step 4 because "we know the debt":** operator perception ≠ documented debt; always run
- **Treating parallel mode as default:** Operator review of Step 2+3 outputs together is harder than separately; default Sequential

## References

- [references/runbook.md](references/runbook.md)
- [references/checklist.md](references/checklist.md)
