# Phase 0 Orchestrator — Runbook (Examples + Troubleshooting)

## Worked example 1 — Greenfield project, Mode A Supervised

**Setup:** Project Atrium, invoicing SaaS, no code yet, 11 raw inputs in `_handover/`.

**Run:**

```
Operator prompt:
"Run phase-0-requirements-orchestrator for Project Atrium.
Mode A. Inputs at _handover/. Output to docs/00_REQUIREMENTS/."
```

**Pipeline progression:**

| Step | Skill | Duration | Operator action |
|------|-------|----------|------------------|
| 0 | Pre-flight | 5 min | Confirmed greenfield, approved plan |
| 1 | project-context-ingestion | 1.5 hr | Reviewed CONTEXT_PACK, scheduled stakeholder meeting for 2 blocking Open Questions |
| — | (Pause 2 days) | — | Stakeholder meeting resolved Open Questions |
| 2 | srs-greenfield-author | 3 hr | Reviewed M1-M8, accepted |
| 3 | nfr-specification | 1 hr | Reviewed M9, requested 1 NFR more strict (security audit cadence) |
| — | (Re-run Step 3 partial) | 15 min | Updated NFR-SEC-04 |
| 4 | requirements-traceability | 30 min | Reviewed M10, accepted |

**Total:** ~6 hr AI work + ~2 hr operator review across 3 days (with 2-day stakeholder pause).

**Outputs:**
- 11 sources processed → CONTEXT_PACK with 4 contradictions, 2 blocking
- M1-M8 with 47 FRs across 4 functional domains
- M9 with 23 NFRs across 7 categories
- M10 with RTM (47 FRs, 0 test refs since no code yet — flagged), 8 Open Questions, glossary

**Hand-off:** Operator initiated Phase 2 orchestrator next day.

## Worked example 2 — Legacy project, Mode B Express

**Setup:** Project Helix (existing dispatch tool), Phase 1 already done, refresh Phase 0 because audit prep.

**Run:**

```
Operator prompt:
"Run phase-0-requirements-orchestrator Mode B Express for Project Helix.
Phase 1 docs in docs/01_DISCOVERY/ are current.
Skip Step 1 (CONTEXT_PACK still valid from 2 weeks ago).
Output: refresh existing M1-M10, archive prior version."
```

**Pipeline:**

| Step | Skill | Duration | Pause? |
|------|-------|----------|---------|
| 0 | Pre-flight | 3 min | Auto (legacy detected, Phase 1 verified) |
| 1 | project-context-ingestion | (skipped) | — |
| 2 | srs-reverse-engineer | 2.5 hr | No (Express mode) |
| 3 | nfr-specification | 45 min | No |
| 4 | requirements-traceability | 25 min | No |
| 5 | Phase report | 5 min | Final review |

**Total:** ~3.5 hr AI work + 30 min operator review at end.

**Caveat from runbook:** Express mode acceptable here because (a) refresh, not initial; (b) audit-prep timeline tight; (c) operator confident outputs only need final review. NOT recommended for first run.

## Worked example 3 — Selective re-run

**Setup:** Stakeholder added 1 new regulation (GDPR Article 17 update). NFRs need refresh.

**Run:**

```
Operator prompt:
"Run phase-0-requirements-orchestrator Mode C Selective.
Skills to run: nfr-specification only.
Reason: GDPR update requires new compliance NFRs; rest of SRS unchanged.
Update CONTEXT_PACK Section 7.1 first with new regulatory citation."
```

**Pipeline:**

| Step | Action | Duration |
|------|--------|----------|
| 0 | Pre-flight + CONTEXT_PACK Section 7.1 patch (manual edit) | 10 min |
| 3 | nfr-specification (re-run, archive prior) | 45 min |
| Post | Update RTM Section if NFRs changed test refs | 10 min |

**Total:** ~1 hr.

This is selective re-run, not full pipeline. Acceptable because change is localized.

---

## Troubleshooting

### T1 — Pre-flight fails: "Cannot detect project type"

**Cause:** `src/` exists but is empty or contains only config files.

**Resolution:**
```
Operator: "Project Foo has scaffolding but no real code yet. Treat as greenfield."
```
Force greenfield mode via prompt.

### T2 — Step 1 produces zero contradictions

**Cause:** Either (a) too few sources to find conflict, or (b) AI synthesizing.

**Resolution:**
1. Check source count — if <5 sources, expected (and pack confidence should be MEDIUM)
2. If ≥10 sources and 0 contradictions, AI is synthesizing. Re-run with explicit prompt: "Force-find at least 2 contradictions; if none exist after honest analysis, document why."

### T3 — Step 2 fails: "Legacy SRS needs BUSINESS_CONTEXT.md but file missing"

**Cause:** Pipeline ordering — Phase 1 not run for legacy project.

**Resolution:**
```
Abort Phase 0 orchestrator.
Run phase-1-discovery-orchestrator first.
Then resume Phase 0 from Step 2.
```

Don't try to fudge — SRS without business context will be guessing.

### T4 — Step 3 produces NFRs without source citations

**Cause:** CONTEXT_PACK Section 7 (regulatory + SLA) is thin or missing.

**Resolution:**
1. If thin: re-ingest with operator emphasis on regulatory + SLA inputs
2. If unfixable: mark NFRs as "operator hypothesis" in M9 and flag for stakeholder confirmation; don't ship as audit-grade

### T5 — Step 4 RTM has 0 test references

**Cause for greenfield:** expected — no code yet.
**Cause for legacy:** test discovery didn't run, OR no tests exist.

**Resolution:**
- Greenfield: accept 0 refs, mark "GAP — populated in Phase 3"
- Legacy: re-run with explicit test path scan; if still 0, flag as critical Phase 4 finding

### T6 — Operator interrupted mid-pipeline

**Cause:** Long-running Step 2 or 3, operator killed AI session.

**Resolution:**
1. Check `_phase_report_<DATE>.md` partial state if exists
2. List completed steps from file timestamps in `docs/00_REQUIREMENTS/`
3. Resume with: "Resume phase-0-requirements-orchestrator from Step N"
4. AI re-validates pre-conditions for Step N before continuing

### T7 — Two simultaneous Phase 0 runs (e.g., two operators)

**Cause:** No locking mechanism (skills are stateless).

**Resolution:**
- Convention: one operator at a time per project
- Detect: check git working tree dirty before starting
- Recover: take latest run as authoritative; re-run if truly diverged

### T8 — Express mode results disagreed with Supervised

**Symptom:** Operator runs Mode B, then re-runs Mode A on same inputs, gets different outputs.

**Cause:** AI non-determinism + lack of operator nudges in Express.

**Resolution:**
- Diff outputs side-by-side
- Where they differ: Supervised wins by default (more careful)
- Update Express mode prompts to include operator nudges from Supervised feedback

---

## Cost projections

For a medium-sized project (~50 FRs, 4 functional domains):

| Mode | AI work | Operator time | Total | Cost (per multi-tier-routing) |
|------|---------|---------------|-------|-------------------------------|
| A Supervised | 6-8 hr | 2-4 hr | 1-3 days elapsed | ~$15-25 (mostly Tier 2) |
| B Express | 3-5 hr | 0.5-1 hr | <1 day | ~$10-18 |
| C Selective (single skill) | 0.5-2 hr | 15-30 min | <2 hr | ~$2-5 |

Plus stakeholder time for resolving Open Questions (variable).

---

## When orchestrator is NOT the right tool

- **Single-doc updates** (typo, FR add) → invoke component skill directly (or edit doc inline)
- **Cross-phase work** (touching Phase 0 + Phase 1 simultaneously) → run each phase orchestrator separately, with operator coordinating
- **Discovery/exploration before formal work** → run skills individually for flexibility

Orchestrator's value is in routine pipelines, not in unusual situations.
