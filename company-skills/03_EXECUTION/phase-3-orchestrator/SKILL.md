---
name: phase-3-execution-orchestrator
description: Orchestrate Phase 3 Execution setup pipeline (ai-operator-protocol → multi-tier-ai-routing → work-package-decomposer per WP) and ongoing WP execution loop. Phase 3 is BIMODAL — one-time setup phase + ongoing per-WP loop. Use after Phase 2 approval to set up AI execution infrastructure, then to dispatch each WP through decomposer + executor + reviewer cycle. Triggers include "run phase 3", "set up execution", "execute work package", "phase 3 setup", or "WP loop".
---

# Phase 3 Execution Orchestrator

Coordinate Phase 3 in two distinct sub-pipelines:

- **Sub-pipeline A — Setup (one-time):** `ai-operator-protocol` → `multi-tier-ai-routing`
- **Sub-pipeline B — WP execution loop (per Work Package):** `work-package-decomposer` → AI executor → AI reviewer → operator commit

This orchestrator coordinates BOTH sub-pipelines. Operator chooses which mode to run.

## When this orchestrator applies

Use when:
- Phase 2 complete with approved MASTER_PLAN + Work Packages
- Setting up AI execution infrastructure for the project (Sub-pipeline A)
- Dispatching individual WPs to AI executor (Sub-pipeline B)

Do NOT use orchestrator for:
- Single skill update (run component skill directly)
- Phase 4 maintenance (different orchestrator)
- Cross-project AI policy work (out of scope)

## Sub-pipeline A — Setup (one-time per project)

Run once at the start of Phase 3, before any WPs execute.

### Component skills

| # | Skill | Output |
|---|-------|--------|
| 1 | `ai-operator-protocol` | `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md` |
| 2 | `multi-tier-ai-routing` | `docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md` |

### Pre-flight (Sub-pipeline A)

- Phase 2 complete? Verify MASTER_PLAN + WP files
- AI vendor accounts available? (Anthropic / OpenAI / etc — operator confirms)
- Cost budget set? Operator gives ceiling for Phase 3 AI spend

### Workflow (Sub-pipeline A)

```
Step 0: Pre-flight + plan
Step 1: ai-operator-protocol
        → Produce 7 hard rules + 14-step workflow
        → System prompts for Orchestrator/Executor/Reviewer AIs
        → Escalation rules
Step 2: multi-tier-ai-routing
        → 4-tier policy + cost projections + vendor fallback
Step 3: Phase report + transition to Sub-pipeline B
```

### Checkpoints

After each step, operator reviews + commits. Both outputs are project-stable (rarely changed) — review carefully.

## Sub-pipeline B — WP execution loop (per WP)

Run once per Work Package. This is the actual "doing the work" loop.

### Component skill

`work-package-decomposer` (1 skill, but invoked per WP)

### Pre-flight (Sub-pipeline B, per WP)

- Sub-pipeline A complete? AI_OPERATOR_GUIDE + AI_AGENT_TASK_DISTRIBUTION exist
- WP spec exists in `docs/03_EXECUTION/work-packages/PHASE_*.md`
- Dependencies done? (Other WPs that this WP depends on)
- Operator dispatched, approved, ready to supervise

### Workflow (Sub-pipeline B, per WP)

```
For each WP-X.Y:

Step 1: Pre-flight check
        - Dependencies completed?
        - WP spec well-defined?
        - Estimated cost within budget?

Step 2: Run work-package-decomposer
        - Input: WP spec + AI_OPERATOR_GUIDE + AI_AGENT_TASK_DISTRIBUTION
        - Output: WP-X.Y_tasks.md with N micro-tasks

Step 3: Operator reviews task breakdown
        - Verify tier assignment makes sense
        - Verify verify-commands per task
        - Adjust if needed

Step 4: Dispatch tasks to AI executor(s)
        - Per dependency order
        - Each task: prompt → AI generates change → verify command → diff
        - Log per task in PROGRESS.md

Step 5: AI reviewer (separate session) verifies WP completion
        - Run all verify commands
        - Check task list checklist
        - Flag anomalies

Step 6: Operator final review + commit
        - Review diff
        - Commit per convention (see OPERATIONS_MANUAL Section 6)
        - Update PROGRESS.md WP row

Step 7: WP report
        - Tasks completed: N/N
        - Cost actual vs estimate
        - Time elapsed
        - Issues encountered + resolutions
```

### Per-WP gate (G3-equivalent for individual WP)

Before marking WP complete:
- [ ] All micro-tasks verified
- [ ] WP-level test suite passes
- [ ] No regressions (existing tests still pass)
- [ ] Operator signed-off in commit message

## Modes (for both sub-pipelines)

| Mode | Description | Use case |
|------|-------------|----------|
| **A — Supervised** *(default)* | Operator review at every step | Production runs |
| **B — Express (Sub-A only)** | Chain Setup with minimal pauses | Refresh after Phase 2 update |
| **C — Auto-WP (Sub-B only, with policy)** | Per-WP loop runs autonomously for low-risk WPs (Tier 1 majority) | After 5+ WPs successfully completed, operator gains confidence |
| **D — Selective** | Operator picks specific component to run | Targeted update |

**Note on Mode C:** The orchestrator will not enable Mode C unless `AI_OPERATOR_GUIDE.md` explicitly authorizes per-WP autonomy AND operator confirms per-run.

## Workflow combined view

```
[Phase 2 done]
      ↓
Sub-pipeline A (one-time setup)
      ↓
  Phase 3 infrastructure ready
      ↓
Sub-pipeline B (loop per WP)
      ↓ ↑
      ↓ ↑   loop until all WPs done
      ↓ ↑
  All WPs complete
      ↓
[G3 pre-deploy gate]
      ↓
[Production deploy]
      ↓
[Phase 4 begins]
```

## Error recovery

| Failure | Action |
|---------|--------|
| Sub-A pre-flight: Phase 2 incomplete | Abort, run Phase 2 orchestrator first |
| Sub-A Step 1 produces vague rules | Re-run with explicit project-specific constraints |
| Sub-A Step 2 over-routes to Tier 3 | Re-calibrate tier policy based on actual Phase 1 complexity |
| Sub-B pre-flight: dependency WP not done | Pause, dispatch dependency WP first |
| Sub-B Step 2 decomposer produces too few/many tasks | Re-run with explicit guidance (target 10-20 tasks/WP) |
| Sub-B Step 4 AI executor fails task | Per AI_OPERATOR_GUIDE escalation: retry once, escalate to operator if 2nd fail |
| Sub-B Step 5 reviewer flags critical issue | Block commit, operator decides: rollback, fix, or accept with caveat |
| Mid-WP timeout | Resume from last verified task |

## Quality gate (orchestrator-level)

### Sub-pipeline A
- [ ] Both setup docs generated
- [ ] Tier policy makes sense for project complexity
- [ ] Cost projection within operator's budget
- [ ] Operator + tech lead signed off on AI_OPERATOR_GUIDE

### Sub-pipeline B (per WP)
- [ ] Pre-flight passed (deps + spec + budget)
- [ ] Decomposer output reviewed by operator before dispatch
- [ ] All tasks have verify commands
- [ ] All verify commands ran + passed
- [ ] AI reviewer signed-off
- [ ] Operator committed per convention
- [ ] PROGRESS.md updated

## Hand-off

After Sub-A:
- Sub-pipeline B can begin (loop per WP)

After all WPs in Sub-B:
- Pre-deploy gate (G3 — out of scope of orchestrator, ops responsibility)
- → Phase 4 orchestrator (after deploy)

## Failure modes to avoid

- **Skipping Sub-pipeline A:** Without operator-protocol + tier-routing, Sub-B has no rules. Mandatory.
- **Auto Mode C from Day 1:** Operator must build confidence with 5+ supervised WPs first.
- **Decomposer output dispatched without review:** Tier assignment errors cost real money. Always review.
- **WP marked complete without verify pass:** "Looks good" ≠ verified. Run all verify commands.
- **Skipping reviewer step:** Self-review by executor AI ≠ independent review. Use separate session.
- **Aggregating per-WP commits:** Each WP should have its own commit/PR. Aggregate = lost rollback granularity.

## References

- [references/checklist.md](references/checklist.md)
- [references/runbook.md](references/runbook.md)
