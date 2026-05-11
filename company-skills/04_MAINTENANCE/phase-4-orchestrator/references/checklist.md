# Phase 4 Orchestrator — Quality Checklist

Phase 4 has 4 modes; checklist organized per mode.

## Mode A — Setup checklist

### Pre-flight
- [ ] Phase 3 deployed to production OR imminent
- [ ] Monitoring + alerting configured
- [ ] On-call rotation defined with names
- [ ] Backup/recovery procedures documented elsewhere

### Failure mode coverage
- [ ] Failure modes inventoried per TECH_SOLUTION_DESIGN component
- [ ] At least 1 runbook per P0 component (DB, auth, payment, ...)
- [ ] Each runbook has all 6 NIST IR phases
- [ ] Step-by-step commands (not "failover the database")
- [ ] On-call rotation can read + execute without consultation

### Schedule
- [ ] Monthly documentation-sync scheduled (calendar/cron)
- [ ] Quarterly document-consistency-review scheduled
- [ ] Yearly full Phase 4 review scheduled
- [ ] Notifications configured (Slack/email)

### Training
- [ ] Tabletop exercise on top 3 P0 runbooks completed
- [ ] On-call team comfortable with playbook navigation
- [ ] Escalation paths confirmed (when to call who)

### Setup report
- [ ] _setup_report_<DATE>.md generated
- [ ] Lists all runbooks created
- [ ] Lists all schedules set up
- [ ] Operator + tech lead signed-off

## Mode B — Triggered (per event)

### Per feature request
- [ ] Trigger logged in tracker
- [ ] feature-extension-planning ran
- [ ] FEAT_*.md generated with scope/effort/dependencies
- [ ] Operator decided routing (small / medium / large)
- [ ] Hand-off to Phase 3 or mini-Phase 2 happened
- [ ] PROGRESS.md updated

### Per incident
- [ ] Runbook found (or improvised + new runbook created)
- [ ] Timeline logged during incident
- [ ] Recovery confirmed
- [ ] Post-incident review within 48 hr
- [ ] Lessons applied to runbook update
- [ ] If new failure mode: new runbook added to library

### Per code merge (light check)
- [ ] documentation-sync --scope=changed-files-only ran
- [ ] If drift: comment/issue/follow-up created
- [ ] If material change: triggered feature-extension or doc refresh

## Mode C — Scheduled (per cycle)

### Monthly
- [ ] Ran on schedule (1st of month or close)
- [ ] documentation-sync completed
- [ ] DOC_SYNC_REPORT generated + reviewed
- [ ] Critical/High findings ticketed
- [ ] INDEX.md refreshed
- [ ] Prior month's tickets reviewed (closed or rolled)

### Quarterly
- [ ] Ran on schedule
- [ ] document-consistency-review completed
- [ ] CONSISTENCY_REVIEW_REPORT generated
- [ ] Patterns analyzed (systemic issues)
- [ ] Action items assigned + targeted
- [ ] Skill suite version checked

### Yearly
- [ ] Full re-audit ran
- [ ] CONTEXT_PACK refreshed (year of stakeholder change captured)
- [ ] Phase 0 freshness verified (regulations + NFRs)
- [ ] Phase 2 strategy review
- [ ] Skill suite upgrade considered
- [ ] Major report to CEO/CTO

## Mode D — Audit prep

### Pre-flight
- [ ] Auditor + scope + deadline confirmed
- [ ] Audit framework requirements understood (SOC2 / ISO / FDA / etc)

### Evidence gathering
- [ ] Latest documentation-sync run (full scope)
- [ ] Latest document-consistency-review (full scope)
- [ ] All Phase 0-4 docs current (no placeholders)
- [ ] Runbooks spot-checked (random 3)
- [ ] CONTEXT_PACK Section 7.1 regulatory citations verified current

### Critical/High findings
- [ ] All Critical addressed before audit
- [ ] All High triaged (resolved OR explicitly accepted with rationale)
- [ ] Documentation gaps explicitly stated

### Delivery
- [ ] Audit binder organized per framework requirements
- [ ] Git tag created for snapshot
- [ ] Auditor received binder before deadline

## Per-Phase 4 ongoing health

### Quarterly self-check

- [ ] Monthly cycles ran (≥10 of 12 months in past year)
- [ ] Quarterly cycles ran (≥3 of 4 quarters in past year)
- [ ] Incidents had post-incident reviews (≥80% within 48 hr)
- [ ] Feature extensions documented before code (not after)
- [ ] Runbook count growing or stable (not decreasing — that means failure modes dropped from coverage)
- [ ] Drift findings trending down quarter-over-quarter

If multiple ❌ → Phase 4 discipline broken. Re-engage.

## Self-check

Pick 3 random runbooks. For each:
- Open + verify steps still applicable to current production
- Verify monitoring alert actually fires for this failure mode
- Verify on-call can find runbook in <2 minutes (not buried)

If 1+ fails → runbook library outdated; refresh.

Pick latest DOC_SYNC_REPORT. Verify:
- Findings actually triaged (not just listed)
- Critical findings addressed within sprint
- Trend vs prior month present

If trend missing → Mode C discipline weak.
