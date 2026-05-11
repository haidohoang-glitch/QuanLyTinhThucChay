---
name: phase-2-strategic-orchestrator
description: Orchestrate Phase 2 Strategic pipeline (feasibility-assessment → STAKEHOLDER GATE → tech-solution-design → ARCHITECTURE GATE → implementation-planning) with MANDATORY hard pauses for human decisions. Unlike other orchestrators, this one CANNOT run autonomously past gates — stakeholder + tech lead must explicitly approve. Use after Phase 0/1 complete to convert requirements into approved, planned implementation. Triggers include "run phase 2", "strategic pipeline", "feasibility through planning", "convert SRS to plan", or "phase 2 full run".
---

# Phase 2 Strategic Orchestrator

Coordinate Phase 2 Strategic skills with **mandatory hard gates** — feasibility approval (stakeholder) and architecture approval (tech lead). This orchestrator does NOT support fully autonomous mode.

## Why this orchestrator differs from others

Phase 2 includes 2 cardinal decision points:
- **G1 — Feasibility approval** (after `feasibility-assessment`): stakeholder picks scenario
- **G2 — Architecture approval** (after `tech-solution-design`): tech lead approves ADR

Skipping these gates = decision without ownership. AI cannot make these decisions.

This orchestrator therefore:
- Has only Mode A (Supervised) — no Express mode
- Forces explicit human approval recorded in writing before each post-gate step
- Will REFUSE to continue if approval not documented

## When this orchestrator applies

Use when:
- Phase 0 + Phase 1 (if legacy) complete with audit-grade output
- Stakeholder + tech lead available for approval gates
- Project ready to commit budget/timeline (not pure exploration)

Do NOT use orchestrator for:
- Exploratory feasibility (run `feasibility-assessment` alone)
- Re-design without scope change (run `tech-solution-design` alone)
- Planning refresh without strategy change (run `implementation-planning` alone)
- Pre-Phase 0 (orchestrator will refuse — Phase 0 must be done first)

## Component skills (in mandatory order)

| # | Skill | Hard gate after? |
|---|-------|--------------------|
| 1 | `feasibility-assessment` | ✋ G1 — Stakeholder approval |
| 2 | `tech-solution-design` | ✋ G2 — Architecture approval |
| 3 | `implementation-planning` | (no gate — Phase 3 setup begins next) |

## Pre-flight check

Before Step 1:

1. **Phase 0 complete?** Verify M1-M10 exist in `docs/00_REQUIREMENTS/SRS_VI/`
2. **Phase 1 complete?** (if legacy) Verify 4 docs in `docs/01_DISCOVERY/`
3. **Stakeholder identified?** Operator confirms WHO will approve at G1 (name + role)
4. **Tech lead identified?** Operator confirms WHO will approve at G2
5. **Schedule reality check:** stakeholder + tech lead available for next 1-2 weeks (gates take time)

If any fail → ABORT with specific remediation instruction.

## Workflow

### Step 0 — Pre-flight + plan

```
"Phase 2 Strategic pipeline starting.

Pre-flight:
✅ Phase 0 complete (M1-M10 found)
✅ Phase 1 complete (4 Discovery docs found)
✅ Stakeholder approver: [NAME, ROLE]
✅ Tech lead approver: [NAME, ROLE]

Pipeline:
  1. feasibility-assessment (~3-5 hr)
  ✋ G1 — Stakeholder approval (1-7 days wait expected)
  2. tech-solution-design (~3-5 hr)
  ✋ G2 — Architecture approval (1-3 days wait expected)
  3. implementation-planning (~2-4 hr)

Estimated total: 10-15 hr AI + 2-4 hr operator + 1-2 weeks elapsed
(due to stakeholder gate timing).

Proceed? [yes/no]"
```

### Step 1 — `feasibility-assessment`

**Inputs:**
- Phase 0 SRS (FR list = scope baseline)
- Phase 1 outputs (cost-of-inaction baseline) if legacy
- CONTEXT_PACK Section 7.3 (budget cap + deadline)
- External: stakeholder constraints

**Run:**
- Mode A (3-scenario default: Full / Partial / Minimum + Do nothing baseline)
- Each scenario: cost, benefit, risk, timeline, ROI
- Operator's recommendation (NOT decision)

**Output:** `docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md`

**Checkpoint after:**
```
Step 1 complete. FEASIBILITY_ASSESSMENT.md generated.

Scenarios summary:
- Full: $X over T months, ROI Y%, risk Z
- Partial: $X over T months, ROI Y%, risk Z
- Minimum: $X over T months, ROI Y%, risk Z
- Do nothing baseline: cost-of-inaction = $W over 12 months

Operator recommendation: [scenario] because [reasoning].

✋ HARD GATE G1 — Stakeholder approval required.

Orchestrator PAUSED. Cannot proceed until stakeholder approval is
documented in either:
  (a) Email/Slack with explicit "Approve scenario [X]" from stakeholder
  (b) Meeting minutes with approval recorded
  (c) ADR or decision-note signed by stakeholder

Save approval artifact to: docs/02_STRATEGIC/_decisions/G1_approval_<DATE>.md
or _sources/SRC-NNN_<slug>.md (if part of CONTEXT_PACK refresh).

Resume orchestrator with: "Continue phase-2 from Step 2, approved scenario: [X]"

If stakeholder rejects all scenarios → re-run Step 1 with new constraints
(loop, not skip).
```

### G1 — Stakeholder approval gate (MANDATORY PAUSE)

**Orchestrator does NOT continue automatically. Operator must:**

1. Schedule stakeholder review (typically 30-60 min meeting)
2. Present FEASIBILITY_ASSESSMENT.md
3. Document approval (email, minutes, signed decision)
4. Save artifact to `docs/02_STRATEGIC/_decisions/G1_approval_<DATE>.md`
5. Update CONTEXT_PACK if business model assumptions changed
6. Re-invoke orchestrator with explicit approved-scenario parameter

**Verification before Step 2:**
Orchestrator MUST check that approval artifact exists. If not:
```
"G1 approval artifact not found at expected location.
Cannot proceed to Step 2.

Required: docs/02_STRATEGIC/_decisions/G1_approval_*.md
or operator confirmation pointing to alternate artifact path.

Provide approval artifact path:"
```

### Step 2 — `tech-solution-design`

**Inputs:**
- FEASIBILITY_ASSESSMENT + approved scenario (from G1 artifact)
- M9 NFRs (constraints)
- CONTEXT_PACK Section 7.2 (vendor lock-ins)
- Phase 1 outputs (legacy constraints)

**Run:**
- Identify major architectural decisions
- ≥3 candidate architectures per major decision
- Decision matrix per candidate
- ADR per major decision (Context / Decision / Alternatives / Consequences)
- System diagram (component-level)

**Output:** `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` (with embedded or linked ADRs)

**Checkpoint:**
```
Step 2 complete. TECH_SOLUTION_DESIGN.md generated.

Summary:
- N major decisions documented as ADRs
- M architectural components designed
- Constraints honored: [list from CONTEXT_PACK 7.2 + M9 NFRs]
- Estimated implementation effort: K WPs (refined in Step 3)

✋ HARD GATE G2 — Architecture approval required.

Orchestrator PAUSED. Tech lead must explicitly approve ADRs.

Save approval to: docs/02_STRATEGIC/_decisions/G2_approval_<DATE>.md

Resume with: "Continue phase-2 from Step 3, ADRs approved by [NAME]"
```

### G2 — Architecture approval gate (MANDATORY PAUSE)

Tech lead reviews ADRs, can:
- Approve all → proceed to Step 3
- Approve with modifications → operator updates ADRs, re-presents (no full Step 2 re-run unless major)
- Reject → re-run Step 2 with new constraints

Approval artifact required before Step 3 (same as G1).

### Step 3 — `implementation-planning`

**Inputs:**
- TECH_SOLUTION_DESIGN with approved ADRs
- FEASIBILITY (timeline + budget)
- M1-M10 SRS (FR scope)

**Run:**
- Decompose architecture into implementation phases (typically 0: bootstrap, 1: foundation, 2-N: features, +1: hardening)
- Per phase: enumerate Work Packages
- Per WP: scope, FR coverage, dependencies, effort, owner role
- Critical path identification

**Output:**
- `docs/02_STRATEGIC/MASTER_PLAN.md`
- `docs/03_EXECUTION/work-packages/PHASE_0_*.md` ... `PHASE_N_*.md`

**Final checkpoint:**
```
Step 3 complete. Phase 2 pipeline finished.

Outputs:
- MASTER_PLAN.md
- N Phase docs in 03_EXECUTION/work-packages/
- Total WPs: M
- Critical path: WP-X.Y → WP-X.Z (timeline blockers)

Hand-off to Phase 3 orchestrator (set up AI execution infrastructure).
```

### Step 4 — Phase report

`docs/02_STRATEGIC/_phase_report_<DATE>.md`:
- Skills run + durations
- G1/G2 approval artifacts referenced
- Approved scenario + key ADRs
- Hand-off recommendations

## Error recovery

| Failure | Action |
|---------|--------|
| Pre-flight: Phase 0 incomplete | Abort, run `phase-0-requirements-orchestrator` first |
| Step 1 stakeholder rejects all scenarios | Loop: gather new constraints, re-run Step 1 |
| G1 approval artifact missing | Refuse to start Step 2 — operator must provide |
| Step 2 ADR rejected at G2 | Operator updates per feedback; if major rework needed, re-run Step 2 |
| Step 3 timeline doesn't fit approved budget | Re-loop: either re-run Step 1 (new constraints) or descope WPs |
| Stakeholder unavailable >2 weeks | Pause orchestrator; do NOT auto-proceed; consider alternative approver |

## Quality gate (orchestrator-level)

- [ ] Both G1 and G2 approval artifacts exist
- [ ] Approved scenario referenced in TECH_SOLUTION_DESIGN
- [ ] All ADRs have 4 sections (Context/Decision/Alternatives/Consequences)
- [ ] MASTER_PLAN timeline fits approved scenario budget+timeline
- [ ] WP count is reasonable (10-30 typical; <5 = under-decomposed; >50 = over-decomposed)
- [ ] Phase report generated with approval references

## Hand-off

After successful run:
- → Phase 3 orchestrator (set up AI execution)
- → Update INDEX.md (link to MASTER_PLAN)

## Failure modes to avoid

- **Auto-resuming without approval artifact:** Orchestrator MUST refuse. Operator cannot bypass.
- **Treating G1 as formality:** Stakeholder must understand 3 scenarios before picking. Don't rush.
- **Skipping ADR alternatives:** Decision without alternatives = mệnh lệnh, not design.
- **Loose timeline check Step 3:** If MASTER_PLAN says 18 months but approved scenario is 14 months, re-loop, don't ship.
- **Operator approving as proxy:** Operator ≠ stakeholder ≠ tech lead. Approval rights must be respected.

## References

- [references/checklist.md](references/checklist.md)
- [references/runbook.md](references/runbook.md)
