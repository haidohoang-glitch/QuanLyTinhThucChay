# Phase 3 Orchestrator — Quality Checklist

## Sub-pipeline A — Setup checklist

### Gate A1 — Pre-flight
- [ ] Phase 2 complete (MASTER_PLAN + WPs verified)
- [ ] AI vendor accounts available
- [ ] Phase 3 cost budget set
- [ ] Operator + tech lead identified

### Gate A2 — ai-operator-protocol output
- [ ] AI_OPERATOR_GUIDE.md generated
- [ ] 7 hard rules present + project-specific
- [ ] 14-step workflow customized for project
- [ ] System prompts for Orchestrator/Executor/Reviewer present
- [ ] Escalation rules clear (when to call human)
- [ ] Tech lead reviewed + approved

### Gate A3 — multi-tier-ai-routing output
- [ ] AI_AGENT_TASK_DISTRIBUTION.md generated
- [ ] 4 tiers defined with examples
- [ ] Tier mapping policy specific to project complexity
- [ ] Cost projection per tier present
- [ ] Vendor outage fallback documented
- [ ] Cost projection within operator budget

## Sub-pipeline B — WP execution checklist (per WP)

### Gate B1 — Per-WP pre-flight
- [ ] WP spec exists in 03_EXECUTION/work-packages/
- [ ] Dependency WPs marked done in PROGRESS.md
- [ ] Estimated cost within remaining budget
- [ ] Operator confirmed dispatch

### Gate B2 — Decomposer output
- [ ] WP-X.Y_tasks.md generated
- [ ] Task count reasonable (typically 10-20)
- [ ] Each task has tier assignment per routing policy
- [ ] Each task has prompt template
- [ ] Each task has verify command
- [ ] Dependency graph between tasks present
- [ ] Total cost estimate present
- [ ] Operator reviewed + approved before dispatch

### Gate B3 — Executor output
- [ ] All tasks dispatched per dependency order
- [ ] Each task: code change + verify pass
- [ ] Failed tasks: retried per AI_OPERATOR_GUIDE rules
- [ ] No task marked done without verify pass

### Gate B4 — Reviewer output
- [ ] Independent reviewer session ran (not same as executor)
- [ ] All verify commands re-run + passed
- [ ] Existing tests still pass (no regression)
- [ ] Anomalies flagged + addressed
- [ ] Reviewer recommendation: APPROVE / FIX / ROLLBACK

### Gate B5 — Operator commit
- [ ] Diff reviewed
- [ ] Commit follows convention (type + scope + body + refs + co-author)
- [ ] PR linked to WP ticket if applicable
- [ ] PROGRESS.md WP row updated

## Per-Phase 3 (across all WPs)

- [ ] All MASTER_PLAN WPs status updated in PROGRESS.md
- [ ] No WP stuck in "in progress" >2 weeks (reflag for re-decompose)
- [ ] Cost actual vs Sub-A projection within ±20%
- [ ] AI tier mix actual vs policy: Tier 1 60-70% / Tier 2 20-30% / Tier 3 5-15% / Human <5% (typical healthy distribution)

## Self-check

After completing 5 WPs, audit:
- Total cost actual vs projection — diff?
- Tier mix actual — matches AI_AGENT_TASK_DISTRIBUTION? if not, re-calibrate
- Reviewer flag rate — should decrease over time as system stabilizes
- Operator override rate — high override = decomposer needs improvement

If any metric off → review + adjust Sub-A docs (they're living, can be updated).
