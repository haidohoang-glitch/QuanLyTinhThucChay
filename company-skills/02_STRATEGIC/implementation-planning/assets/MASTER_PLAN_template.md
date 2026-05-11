# {{PROJECT_NAME}} — Master Implementation Plan

> **Purpose:** Phase overview, timeline, dependencies, risks. Single source of truth for plan execution.
> **Audience:** Tech lead, engineering manager, AI agents executing WPs, stakeholders tracking progress.
> **Last updated:** {{YYYY-MM-DD}}
> **Generated using:** `implementation-planning` skill v1
> **Reviewer:** {{NAME_OR_TBD}}

---

## 1. Goal & Scope

**Goal (1 sentence):** {{GOAL}}

**Constraints:**
- Budget: {{HOURS_OR_$}}
- Deadline: {{DATE_OR_NONE}}
- Headcount: {{TEAM_COMPOSITION}}
- Must not break: {{e.g., live customers, compliance posture, public API contract}}

**Success criteria:**
1. {{MEASURABLE_TIME_BOUND_CRITERION}}
2. {{...}}
3. {{...}}

**Explicitly out of scope:**
- {{NOT_INCLUDED_1}}
- {{NOT_INCLUDED_2}}

---

## 2. Phase Decomposition Mode

See Section 8 for chosen mode (A / B / C). Mode A summary:

| # | Phase | Purpose |
|---|-------|---------|
| 0 | Pre-Flight | Remove blockers, set up foundation |
| 1 | Quick Wins | Low-risk improvements |
| 2 | Dual-Write | Build new path alongside old |
| 3 | Switch / Cut-over | Move traffic with rollback |
| 4 | Compliance / Cleanup | Finalize + remove legacy |

(Mode B / C: customize this table to match chosen taxonomy.)

---

## 3. Phase Summary

| Phase | Name | WP count | Effort (devhrs) | Calendar (days) | Gate |
|-------|------|----------|-----------------|-----------------|------|
| 0 | {{NAME}} | {{N}} | {{HOURS}} | {{DAYS_RANGE}} | Gate 0 |
| 1 | {{NAME}} | {{N}} | {{HOURS}} | {{DAYS_RANGE}} | Gate 1 |
| 2 | {{NAME}} | {{N}} | {{HOURS}} | {{DAYS_RANGE}} | Gate 2 |
| 3 | {{NAME}} | {{N}} | {{HOURS}} | {{DAYS_RANGE}} | Gate 3 |
| 4 | {{NAME}} | {{N}} | {{HOURS}} | {{DAYS_RANGE}} | Gate 4 (final) |
| **Total** | | {{TOTAL_WP}} | {{TOTAL_HOURS}} | {{TOTAL_RANGE}} | |

Detailed WPs per phase: see `docs/03_EXECUTION/work-packages/PHASE_<N>_<NAME>.md`.

---

## 4. Dependency Graph

### High-level

```
Phase 0 ──> Phase 1 ──> Phase 2 ──> Phase 3 ──> Phase 4
            │           │
            └─ may run in parallel (only if doc allows)
```

(Adapt graph to project; not all migrations are strictly linear.)

### Cross-phase WP dependencies

| WP | Depends on | Type |
|----|------------|------|
| WP-2.A | WP-0.0, WP-0.H | Hard (cannot start before merge) |
| WP-3.A | WP-2.B, WP-2.D | Hard |
| WP-4.B | All Phase 3 | Hard |
| {{...}} | {{...}} | {{Hard/Soft}} |

---

## 5. Risks & Mitigations

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| RP-01 | {{e.g., External vendor changes pricing mid-plan}} | {{L/M/H}} | {{L/M/H}} | {{e.g., Lock pricing tier early; identify alternative vendor}} |
| RP-02 | {{e.g., Key dev leaves; bus factor}} | {{...}} | {{...}} | {{e.g., Pair on critical WPs; document decisions}} |
| RP-03 | {{...}} | {{...}} | {{...}} | {{...}} |

---

## 6. Verification Gates

Each gate must pass before the next phase starts.

### Gate 0 — End of Pre-Flight

Pass criteria:
- [ ] All Phase 0 WPs merged
- [ ] No P0 findings remaining (per `TECH_DEBT_AUDIT.md`)
- [ ] CI green for {{N}} consecutive runs
- [ ] {{PROJECT_SPECIFIC_CRITERION}}

### Gate 1 — End of Quick Wins

Pass criteria:
- [ ] {{METRIC_TARGET}} reduced by {{%}} in production
- [ ] No production incidents introduced
- [ ] {{...}}

(repeat for each gate)

---

## 7. Rollback Strategy (Plan-level)

If the plan needs to abort mid-execution:

| Phase reached | Rollback approach | Data state |
|---------------|-------------------|------------|
| Phase 0 only | Revert PRs in reverse order; deploy each | Trivial (no data migration yet) |
| Phase 1 done | Revert Phase 1 PRs; Phase 0 changes are usually keepable | Trivial |
| Phase 2 in progress | Disable feature flag; dual-write halts; new path data is orphaned | Reconcile if old path still primary |
| Phase 3 mid-cutover | Flip rollout % back to 0; new path absorbs no traffic | Investigate before continuing |
| Phase 3 fully cut over | Difficult to go back; new path is now primary | Forward-fix preferred |

Per-WP rollback is in each WP's "Rollback plan" section.

---

## 8. Notes & Caveats

- **Phase decomposition mode:** {{A — Standard 5-phase / B — Honor existing structure / C — User-defined}}
- **Mode rationale:** {{WHY}}
- **If Mode B:** Source = `{{PATH_TO_PHASE_DOC}}` (commit `{{HASH}}`)
- **If Mode C:** User-provided phases = {{LIST}}; rationale = {{WHY}}
- **Inputs read:** TECH_SOLUTION_DESIGN ({{✅/❌}}), FEASIBILITY ({{✅/❌}}), TECH_DEBT_AUDIT ({{✅/❌}}), DATA_ARCHITECTURE ({{✅/❌}}), CODEBASE_MAP ({{✅/❌}})
- **Missing inputs:** {{LIST_AND_HOW_PLAN_COPED}}
- **Time spent on plan creation:** {{HOURS}}
- **Confidence:** {{HIGH/MEDIUM/LOW}}

---

## 9. Open Questions

| ID | Question | Suggested next step |
|----|----------|---------------------|
| OQ-1 | {{QUESTION}} | {{NEXT_STEP}} |

---

## 10. Quick Reference

- Per-phase WPs: `docs/03_EXECUTION/work-packages/PHASE_<N>_<NAME>.md`
- Test infrastructure: `docs/03_EXECUTION/00_TESTING_INFRASTRUCTURE.md`
- QA checklist (aggregated): `docs/03_EXECUTION/B_QA_CHECKLIST_MASTER.md`
- Rollback runbook: `docs/04_MAINTENANCE/runbooks/C_ROLLBACK_RUNBOOK.md`

*This plan is the contract between leadership (who approve), engineering (who execute), and AI agents (who can be supervised against it). Changes to the plan require updating this doc, not silent drift.*
