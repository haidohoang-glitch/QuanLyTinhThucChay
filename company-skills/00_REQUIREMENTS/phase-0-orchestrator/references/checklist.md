# Phase 0 Orchestrator — Quality Checklist

Run after orchestrator pipeline completes. This is in addition to component skills' own checklists.

## Gate 1 — Pre-flight integrity

- [ ] Project type (greenfield/legacy) detected and confirmed by operator
- [ ] Mode (A/B/C) selected with rationale
- [ ] Existing files archived to `_archive/<DATE>/` (if applicable)
- [ ] Operator approved plan before Step 1

## Gate 2 — Component skill completion

- [ ] Step 1 — `project-context-ingestion` ran (or explicitly skipped with reason)
- [ ] Step 2 — Correct SRS skill ran (greenfield-author OR reverse-engineer per project type)
- [ ] Step 3 — `nfr-specification` ran
- [ ] Step 4 — `requirements-traceability` ran
- [ ] Each component skill's `references/checklist.md` passed (verify per-skill)

## Gate 3 — Inter-skill consistency

- [ ] FRs in M3-Mx cite [SRC-NNN] from CONTEXT_PACK (if Step 1 ran)
- [ ] NFRs in M9 cite source (regulatory / SLA / baseline)
- [ ] Open Questions in M10 RTM consolidate from: CONTEXT_PACK Section 12 + SRS M10 + NFR gaps
- [ ] Glossary in M1.3 consistent with terminology in M3-Mx

## Gate 4 — Checkpoint discipline

- [ ] Mode A: operator reviewed at every step boundary
- [ ] Mode B: operator at minimum reviewed pre-flight + final
- [ ] Any blocking Open Question NOT silently bypassed
- [ ] Critical contradictions from CONTEXT_PACK either resolved OR documented as deferred

## Gate 5 — Phase report

- [ ] `_phase_report_<DATE>.md` generated OR `PROGRESS.md` updated
- [ ] Run summary lists every skill + duration + status
- [ ] Quality gate results recorded
- [ ] Next-phase recommendation stated

## Gate 6 — Audit-grade output

- [ ] M1-M10 all present (no placeholder)
- [ ] M9 NFRs have target value + measurement method + source
- [ ] RTM has FR-ID + Description + Test refs (or "GAP" marker) + Code refs (legacy) + Owner
- [ ] No fabricated requirements (every FR traceable)

## Gate 7 — Hand-off readiness

- [ ] Phase 0 marked COMPLETE in PROGRESS.md
- [ ] Outputs ready for Phase 2 orchestrator inputs
- [ ] INDEX.md refresh recommended (link to `document-index-master`)

## Self-check

Pick 3 random FRs and 2 random NFRs. For each:
- Verify source citation exists and points to real source
- Verify language is testable (not vague)
- Verify priority is set (not all "Must")

If 1+ fails → orchestrator output has noise. Re-run problematic component skill(s).
