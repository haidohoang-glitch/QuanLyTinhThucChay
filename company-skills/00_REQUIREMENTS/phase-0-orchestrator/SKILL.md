---
name: phase-0-requirements-orchestrator
description: Orchestrate the full Phase 0 Requirements pipeline by running component skills sequentially with operator checkpoints. Handles greenfield-vs-legacy branching automatically. Component skills: project-context-ingestion → srs-greenfield-author OR srs-reverse-engineer → nfr-specification → requirements-traceability. Use when starting a new project, refreshing all requirements docs after major change, or auditing Phase 0 completeness in one orchestrated run. Triggers include "run phase 0", "execute requirements pipeline", "do all phase 0 skills", "orchestrate requirements", or "phase 0 full run".
---

# Phase 0 Requirements Orchestrator

Coordinate end-to-end execution of Phase 0 Requirements skills. Replaces 4-5 manual skill invocations with one orchestrated run, while preserving operator checkpoints between steps.

## When this orchestrator applies

Use when:
- Starting a new project — run full pipeline to produce CONTEXT_PACK + SRS + NFR + RTM
- Refreshing Phase 0 after major stakeholder/scope change — re-run with cascade
- Audit prep — verify Phase 0 completeness (all 4 outputs current)
- Onboarding to legacy project — full pipeline produces audit-grade docs in one shot

Do NOT use orchestrator for:
- Single-skill update (e.g., add 1 FR) → invoke component skill directly
- Phase 0 partially done already → invoke remaining skills individually (orchestrator assumes fresh start)
- Pure NFR work without SRS context → use `nfr-specification` standalone

## Component skills (in execution order)

| # | Skill | Required? | Skip condition |
|---|-------|-----------|----------------|
| 1 | `project-context-ingestion` | Strongly recommended | Operator confirms no raw inputs available |
| 2A | `srs-greenfield-author` | Required IF greenfield | Skip if legacy |
| 2B | `srs-reverse-engineer` | Required IF legacy | Skip if greenfield |
| 3 | `nfr-specification` | Required | (none — always run) |
| 4 | `requirements-traceability` | Required | (none — always run) |

## Modes

| Mode | Description | When |
|------|-------------|------|
| **A — Supervised** *(default)* | Pause for operator review after each skill | Production runs, audit-grade output |
| **B — Express** | Chain through, stop only at hard checkpoints (project type detection, contradiction surface) | Internal drafts, exploratory runs |
| **C — Selective** | Operator pre-specifies skill subset to run | Partial refresh after change |

## Pre-flight check (before Step 1)

The orchestrator MUST verify before starting:

1. **Project type detected:** greenfield (no code) or legacy (code exists)?
   - Auto-detect: if `src/` exists with non-trivial code → legacy; else greenfield
   - Confirm with operator before proceeding
2. **Raw inputs available?** Check for:
   - `_handover/`, `_inputs/`, or operator-specified folder
   - At least 1 stakeholder interview / RFP / brief
3. **Output destination clean?** Check `docs/00_REQUIREMENTS/`:
   - If files exist → ask operator: archive or overwrite?
   - Default: move existing to `_archive/<DATE>/` before proceeding

If pre-flight fails → ABORT, report to operator with what's missing.

## Workflow

### Step 0 — Pre-flight + plan announcement

```
Orchestrator output to operator:
"Phase 0 Requirements pipeline starting.

Detected project type: [GREENFIELD | LEGACY]
Mode: [A Supervised | B Express | C Selective]
Skills to run (in order):
  1. project-context-ingestion
  2. srs-[greenfield-author | reverse-engineer]
  3. nfr-specification
  4. requirements-traceability

Estimated runtime: 4-8 hours AI work + 2-4 hours operator review.
Estimated cost: ~$X (per multi-tier-ai-routing policy if Phase 3 set up).

Pre-flight checks:
✅ Project type confirmed
✅ Raw inputs found (N sources in _handover/)
✅ Output destination clean (or archived)

Proceed? [yes/no]"
```

If operator says no → exit with no changes.

### Step 1 — Run `project-context-ingestion`

**Inputs check:** raw materials folder.

**Run:**
- Mode A (6-category default) unless operator overrides
- Anonymize-by-default
- Output: `docs/00_REQUIREMENTS/CONTEXT_PACK.md` + `_sources/`

**Checkpoint after:**

```
Step 1 complete. CONTEXT_PACK.md generated.

Summary:
- N sources processed (X in user-research, Y in comms, Z in regulatory, ...)
- Top 3 contradictions surfaced: [list]
- Open Questions for stakeholder: N items, M blocking

⚠️ Blocking Open Questions:
[list]

Recommendation: Resolve blocking Open Questions with stakeholder before
proceeding to Step 2 (SRS authoring will be unsupported otherwise).

Mode A — pause for operator decision:
  [A1] Continue to Step 2 (accept Open Questions as-is)
  [A2] Pause pipeline, schedule stakeholder meeting first
  [A3] Re-run Step 1 with additional sources
```

In Mode B Express, skip pause unless ≥3 blocking Open Questions.

### Step 2 — Run SRS skill (greenfield OR legacy)

**Branching logic:**

```
IF project_type == greenfield:
    skill = srs-greenfield-author
ELSE IF project_type == legacy:
    # Pre-requisite check: Phase 1 docs exist?
    IF NOT exists(docs/01_DISCOVERY/BUSINESS_CONTEXT.md):
        ABORT: "Legacy project requires Phase 1 Discovery before Phase 0 SRS.
                Run phase-1-discovery-orchestrator first, then resume."
    skill = srs-reverse-engineer
```

**Run** chosen skill with inputs:
- `docs/00_REQUIREMENTS/CONTEXT_PACK.md`
- (legacy) Phase 1 outputs in `docs/01_DISCOVERY/`
- Mode A (IEEE 830 standard) unless overridden

**Output:** `docs/00_REQUIREMENTS/SRS_VI/M1-Mx_*.md` + M9/M10 placeholders

**Checkpoint after:**
```
Step 2 complete. SRS M1-M8 generated.

Summary:
- M1 Introduction: scope confirmed
- M2 Overall Description: N user classes, M constraints
- M3-Mx Functional modules: N domains, M FRs total
  - Must: X | Should: Y | Could: Z | Won't: W
- M9, M10: placeholders (will populate next steps)
- Open Issues identified: N items (sourced from CONTEXT_PACK + code mismatches)

Mode A — pause:
  [A1] Continue to Step 3 (NFR)
  [A2] Operator review M1-M8 first
  [A3] Re-run with adjustments
```

### Step 3 — Run `nfr-specification`

**Inputs:**
- `docs/00_REQUIREMENTS/SRS_VI/M1-M8` (generated in Step 2)
- `docs/00_REQUIREMENTS/CONTEXT_PACK.md` (regulatory constraints from Section 7.1)
- (legacy) `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`

**Run:**
- Default 7 NFR categories (Performance / Security / Availability / Scalability / Usability / Maintainability / Compliance)
- Each NFR: target value + measurement method + source

**Output:** `docs/00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md` (overwrite placeholder)

**Checkpoint after:**
```
Step 3 complete. M9 NFR generated.

Summary:
- N NFRs across 7 categories
- M sourced from regulatory (cited)
- K sourced from SLA commitments (cited)
- L from operational baselines (cited from CONTEXT_PACK Section 6)

⚠️ NFRs without source citation: N items (must fix before audit-grade)

Mode A — pause:
  [A1] Continue to Step 4 (RTM)
  [A2] Operator review NFRs
```

### Step 4 — Run `requirements-traceability`

**Inputs:**
- All M1-M9 generated previously
- (Optional) test files, code paths if legacy

**Run:**
- 3 parts: RTM matrix + Open Issues + Appendix
- Open Issues consolidate from CONTEXT_PACK Section 12 + SRS M10 + NFR gaps

**Output:** `docs/00_REQUIREMENTS/SRS_VI/M10_RTM_Issues_Appendix.md` (overwrite placeholder)

**Checkpoint after:**
```
Step 4 complete. M10 RTM generated.

Summary:
- N FRs traced
- M FRs with test coverage gap (flagged "GAP — needs test plan")
- K Open Issues consolidated
- Glossary: N terms

Pipeline complete.
```

### Step 5 — Final phase report

Generate summary at `PROGRESS.md` (append) or `docs/00_REQUIREMENTS/_phase_report_<DATE>.md`:

```markdown
# Phase 0 Run Report — <DATE>

## Skills run
- ✅ project-context-ingestion (N sources, M contradictions)
- ✅ srs-<greenfield|reverse> (Mode A, N FRs)
- ✅ nfr-specification (N NFRs, 7 categories)
- ✅ requirements-traceability (N FRs traced, M test gaps)

## Outputs
- docs/00_REQUIREMENTS/CONTEXT_PACK.md
- docs/00_REQUIREMENTS/_sources/SRC-001..N
- docs/00_REQUIREMENTS/SRS_VI/M1-M10

## Quality gates
- [ ] Each component skill checklist passed
- [ ] Open Questions reviewed by stakeholder
- [ ] Blocking issues escalated

## Next: Phase 1 (legacy) or Phase 2 (greenfield)
```

## Error recovery

Per-step failure handling:

| Failure | Action |
|---------|--------|
| Pre-flight fails | Abort, log, return to operator |
| Step 1 fails (no inputs) | Operator manually provides inputs OR mark Step 1 skipped + note in CONTEXT_PACK |
| Step 2 legacy + no Phase 1 docs | Abort, instruct: "Run Phase 1 orchestrator first" |
| Step 3 fails (no SRS) | Abort, Step 2 must complete |
| Step 4 fails | Continue (RTM gracefully degrades — partial RTM still useful) |
| AI session timeout | Resume from last completed checkpoint |
| Operator interrupts | Save state, allow resume with `--resume` flag (operator concept) |

## Quality gate (orchestrator-level)

After Step 4, verify:

- [ ] All 4 (or 3 if Step 1 skipped) component skills' checklists passed
- [ ] M9 NFRs each have source citation
- [ ] RTM coverage statement is honest about test gaps
- [ ] Open Questions list is non-empty (suspicious if empty)
- [ ] Phase report generated

If any fails → mark Phase 0 INCOMPLETE in PROGRESS.md.

## Hand-off

After successful run:
- → Phase 1 orchestrator (if legacy + Phase 1 not done yet) — but typically Phase 1 runs BEFORE Phase 0 SRS for legacy
- → Phase 2 orchestrator (`feasibility-assessment` next)
- → `document-index-master` (refresh INDEX.md)

## Failure modes to avoid

- **Auto-running for legacy without Phase 1:** Pre-flight detects this. Don't override.
- **Skipping CONTEXT_PACK:** SRS without it = SRS sai chiều. Default to running it; operator must explicitly skip with reason logged.
- **Pipeline through Open Questions:** Mode A pauses on blocking. Don't change Mode A default to autonomous.
- **Overwriting without archive:** Pre-flight handles this. Verify archive happened before Step 1 writes.
- **Treating express mode as "faster + safer":** It's NOT safer. It skips review. Use for drafts only.

## Reference

- See [references/runbook.md](references/runbook.md) for worked examples + troubleshooting
- See [references/checklist.md](references/checklist.md) for orchestrator-level quality gates
- Component skill docs in same parent folder
