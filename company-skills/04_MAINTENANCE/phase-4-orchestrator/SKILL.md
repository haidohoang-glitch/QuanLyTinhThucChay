---
name: phase-4-maintenance-orchestrator
description: Orchestrate Phase 4 Maintenance skills which run on different cadences (event-driven, monthly, quarterly). Unlike other orchestrators (one-shot pipelines), Phase 4 is ONGOING — orchestrator dispatches the right skill based on trigger event or scheduled time. Component skills: incident-response-playbook, feature-extension-planning, documentation-sync. Use to coordinate ongoing maintenance, not as one-shot pipeline. Triggers include "run phase 4", "maintenance cycle", "monthly maintenance", "feature request handler", or "ongoing operations".
---

# Phase 4 Maintenance Orchestrator

Coordinate ongoing Phase 4 skills triggered by EVENTS or SCHEDULES rather than sequential pipeline. Unlike Phases 0-3, Phase 4 has no "complete" state — it's a continuous loop while project is in production.

## Why this orchestrator differs

Other phase orchestrators run sequentially to a completion state. Phase 4 has 3 different loop types:

| Loop | Trigger | Skill |
|------|---------|-------|
| **Pre-deploy preparation** | Once before go-live + after major changes | `incident-response-playbook` (per failure mode) |
| **Event-driven** | Feature request, sự cố | `feature-extension-planning`, `incident-response-playbook` |
| **Scheduled** | Monthly, quarterly, yearly | `documentation-sync`, `document-consistency-review` |

Orchestrator's job: dispatch correct skill based on trigger, manage scheduling, and ensure cross-skill coordination (e.g., feature-extension may trigger consistency-review).

## When this orchestrator applies

Use when:
- Project has gone live and is in production
- Need to coordinate ongoing maintenance activities
- Setting up Phase 4 maintenance schedule
- Responding to maintenance triggers (incidents, feature requests, scheduled audits)

Do NOT use orchestrator for:
- Pre-production setup (use Phase 0/1/2/3 orchestrators)
- One-time skill invocation (just run the skill directly)
- Cross-project portfolio operations (out of scope)

## Component skills

| Skill | Trigger pattern | Cadence |
|-------|------------------|---------|
| `incident-response-playbook` | Pre-deploy (proactive) + incident response (reactive) + post-incident review | Pre-deploy: per failure mode<br>Reactive: per incident<br>Review: 48 hr post-incident |
| `feature-extension-planning` | Feature request from PM/customer | Per feature request |
| `documentation-sync` | Scheduled monthly + ad-hoc on PR | Monthly + per significant PR |
| `document-consistency-review` | Scheduled quarterly + before audit | Quarterly + audit-prep |

(Cross-cutting skills `document-index-master` and `document-consistency-review` also apply to Phase 4 lifecycle but are managed cross-phase.)

## Modes

| Mode | Description | Use case |
|------|-------------|----------|
| **A — Setup** | Initial Phase 4 setup: build runbook library, schedule recurring tasks | One-time at go-live |
| **B — Triggered** | Dispatch one skill per trigger event (operator-driven) | Day-to-day operations |
| **C — Scheduled** | Run scheduled batch (e.g., monthly cycle) | Cron-like cadence |
| **D — Audit prep** | Run multiple skills together for audit preparation | Quarterly/yearly audit |

## Workflow — Mode A (Setup, one-time)

### Pre-flight
- Phase 3 complete (production deployment imminent or done)
- On-call rotation defined
- Monitoring/alerts configured
- Backup/recovery procedures exist

### Steps

```
Step 1: Inventory failure modes
        → For each component in TECH_SOLUTION_DESIGN, list failure modes
        → Typically 10-30 failure modes for medium project

Step 2: Run incident-response-playbook per failure mode
        → For each: NIST IR 6-phase runbook
        → Output: docs/04_MAINTENANCE/runbooks/INCIDENT_<id>.md
        → Group by severity (P0/P1/P2)

Step 3: Schedule recurring tasks
        → Monthly: documentation-sync (typically 1st of month)
        → Quarterly: document-consistency-review (Q1/Q2/Q3/Q4 start)
        → Yearly: full Phase 4 review + skill suite refresh

Step 4: On-call training
        → Tabletop exercise on top 3 P0 runbooks
        → Operator + on-call team walks through

Step 5: Phase 4 setup report
        → docs/04_MAINTENANCE/_setup_report_<DATE>.md
        → Lists runbooks created, schedules set, training done
```

## Workflow — Mode B (Triggered)

For each trigger:

### Trigger: Feature request
```
Operator: "Feature request: FEAT-042 Bulk Customer Export from sales team"

Orchestrator:
  Step 1: Pre-flight
    - Production stable? (no active P0 incident)
    - Existing scope of feature understood?
    - Capacity available?
  Step 2: Run feature-extension-planning
    - Output: docs/04_MAINTENANCE/feature-extensions/FEAT-042_*.md
  Step 3: Operator decision tree
    - Small (<1 week): direct to work-package-decomposer (skip Phase 2)
    - Medium (1-4 weeks): mini Phase 2 (feasibility + design)
    - Large (>1 month): full Phase 2 orchestrator
  Step 4: Hand-off to Phase 3 (work-package-decomposer)
  Step 5: Update INDEX.md to add new feature
```

### Trigger: Incident detected
```
On-call alert: "Postgres primary unreachable, P0"

Orchestrator (or on-call directly):
  Step 1: Open relevant runbook
    - Locate docs/04_MAINTENANCE/runbooks/INCIDENT_postgres_primary_down.md
    - Follow NIST IR phases
  Step 2: During incident: log timeline + actions in incident channel
  Step 3: Recovery confirmed: incident closed
  Step 4: Within 48 hr — post-incident review
    - Run incident-response-playbook in "post-incident" mode
    - Output: timeline + lessons + action items
    - Update existing runbook with lessons
  Step 5: If new failure mode discovered (not in existing runbooks)
    - Run incident-response-playbook to create new runbook
```

### Trigger: Code change merged
```
PR merged to main

Orchestrator:
  Step 1: Quick doc-sync check (changed files only)
    - Run documentation-sync --scope=changed-files-only
  Step 2: If drift detected: comment on PR or open follow-up issue
  Step 3: If material API/schema change: trigger feature-extension-planning
          to update relevant SRS/ADR
```

## Workflow — Mode C (Scheduled)

### Monthly cycle (1st of month)
```
Step 1: Run documentation-sync (full scope)
Step 2: Operator reviews DOC_SYNC_REPORT.md
Step 3: For each High/Critical drift finding:
          - Create remediation ticket
          - Assign owner + target
Step 4: Run document-index-master to refresh INDEX.md
Step 5: Update PROGRESS.md with monthly cycle done
```

### Quarterly cycle
```
Step 1: Run document-consistency-review
Step 2: Operator + tech lead review CONSISTENCY_REVIEW_REPORT.md
Step 3: Address Critical/High findings within 1 sprint
Step 4: Skill suite review (any company-skills updates available?)
Step 5: Phase 4 health report
```

### Yearly cycle
```
Step 1: Full re-audit:
        - documentation-sync full
        - document-consistency-review full
Step 2: Re-run project-context-ingestion (capture year of stakeholder change)
Step 3: Phase 0 freshness check (M9 NFRs still valid? regulations changed?)
Step 4: Phase 2 strategy review (is approved scenario still right?)
Step 5: Skill version upgrade if available
Step 6: Major Phase 4 health report → CEO/CTO review
```

## Workflow — Mode D (Audit prep)

```
Pre-flight: Audit timeline + scope confirmed

Step 1: Run documentation-sync (latest, full)
Step 2: Run document-consistency-review (latest, full)
Step 3: Address any Critical drift/inconsistency
Step 4: Spot-check runbooks (random 3) — still accurate?
Step 5: Generate audit binder:
        - All Phase 0-4 docs current
        - DOC_SYNC + CONSISTENCY reports as evidence
        - Runbook samples
        - Phase 4 setup report
Step 6: Auditor receives binder + git tag for snapshot
```

## Pre-flight check (per mode)

- **Mode A:** Phase 3 deployed; on-call defined
- **Mode B:** Production stable; trigger event clearly identified
- **Mode C:** Schedule reached; previous cycle archived
- **Mode D:** Audit details confirmed (auditor, scope, deadline)

## Error recovery

| Failure | Action |
|---------|--------|
| Mode A: Phase 3 not yet deployed | Defer Phase 4 setup until production live |
| Mode B feature: capacity unavailable | Park feature, schedule for next sprint |
| Mode B incident: runbook missing | Improvise based on similar runbook + create new runbook in post-incident |
| Mode C monthly cycle missed | Catch up next cycle; skip 1 cycle is OK; skip 2+ = review process |
| Mode D audit deadline tight | Prioritize by audit framework requirements; document gaps explicitly |

## Quality gate (orchestrator-level)

### Mode A Setup
- [ ] Runbook count matches identified failure modes (≥80% coverage)
- [ ] Schedules created in operational calendar
- [ ] On-call team trained on top 3 P0 runbooks
- [ ] Setup report generated

### Mode B Triggered (per trigger)
- [ ] Trigger logged with timestamp
- [ ] Correct skill dispatched
- [ ] Output committed
- [ ] PROGRESS.md updated with event

### Mode C Scheduled (per cycle)
- [ ] Cycle ran on schedule (or rationale if delayed)
- [ ] Reports generated
- [ ] Action items assigned to owners
- [ ] Prior cycle's action items closed or rolled forward

### Mode D Audit prep
- [ ] All evidence gathered
- [ ] Snapshot tag created in git
- [ ] Binder delivered before audit deadline

## Hand-off

Phase 4 has no terminal hand-off (continuous loop). But specific events hand off:

- **Feature request → Phase 3** (work-package-decomposer)
- **Major scope change → Phase 2** (feasibility-assessment)
- **Major refactor → Phase 1** (re-discovery)
- **Pivot → Pre-Phase 0** (re-ingest CONTEXT_PACK)

## Failure modes to avoid

- **Skipping Mode A setup:** Production without runbooks = MTTR disaster. Mandatory before go-live.
- **Skipping monthly documentation-sync:** Drift compounds invisibly. Discipline > urgency.
- **Treating incidents as "fix and forget":** Without post-incident review, runbooks don't improve.
- **Letting feature-extension bypass scope check:** Features = scope creep. Mini-Phase 2 prevents this.
- **Audit prep cramming:** Mode D should run quarterly anyway, not just before audits. If you're cramming, your maintenance discipline is broken.

## References

- [references/checklist.md](references/checklist.md)
- [references/runbook.md](references/runbook.md)
