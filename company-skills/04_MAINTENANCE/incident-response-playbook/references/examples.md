# Incident Response Playbook — Worked Example

Anonymized. Fictional incident playbook: **"Postgres primary unreachable"** for a typical SaaS project.

## Context

**Imagined input:** "Author the playbook for the most common P0 we face: Postgres primary unreachable. We use AWS RDS with Multi-AZ failover. On-call is mid-level engineer."

**Mode:** A (NIST IR phases).

---

## Output excerpt

```markdown
# Incident Playbook — Postgres Primary Unreachable

> Incident class: Postgres primary unreachable from application servers
> Severity (default): P0
> Last updated: 2026-09-20
> Last drilled: 2026-09-15 (Pass with minor friction — see Section 12)
> Owner: Platform team lead

## 1. Incident Signature

### What this incident IS

Application instances cannot connect to the primary Postgres database. Symptoms:
- Connection errors in application logs (`ECONNREFUSED`, `connection timeout`, `terminating connection due to administrator command`)
- API endpoints returning 5xx
- Background jobs failing
- Multi-AZ failover may or may not be in progress

### What this incident is NOT

- **Replica unreachable** (different playbook: `INCIDENT_POSTGRES_REPLICA.md`) — primary still works, only replicas affected
- **Slow queries / latency spike** (use `INCIDENT_DB_PERFORMANCE.md`) — connections succeed but queries slow
- **Application bug causing connection exhaustion** (use `INCIDENT_CONNECTION_POOL.md`) — DB itself healthy, app pool exhausted

## 2. Severity Classification

| Severity | Criteria | Examples |
|----------|----------|----------|
| **P0** | Primary writes failing system-wide; no functional fallback | Total API failure; cannot record orders |
| **P1** | Primary failing, replica serving cached/read traffic in degraded mode | Reads work; writes fail |
| **P2** | Brief disconnection (<30s); auto-recovered | Transient blip during failover |

Default for THIS playbook: **P0** (assume worst case until triage proves otherwise)

## 3. Detection Signals

| Signal | Source | Threshold |
|--------|--------|-----------|
| Datadog "DB Connection Failures" | Datadog APM | >50 errors/min for 2 min |
| Sentry "DatabaseError" | Sentry | >100 events in 5 min |
| RDS Event Notifications | AWS SNS → Slack #db-alerts | Failover events; instance state changes |
| Customer reports | Zendesk | "site down", "cannot save" |
| Synthetic check failure | Datadog Synthetics "API health" | 3 consecutive failures |

## 4. Phase 1: Triage (first 5 minutes)

```
1. Acknowledge in PagerDuty (signals "I'm responding")
2. Slack #incidents: "Responding to DB primary unreachable. Investigating per
   docs/04_MAINTENANCE/runbooks/INCIDENT_POSTGRES_PRIMARY.md"
3. Open monitoring:
   - Datadog: https://app.datadoghq.com/dashboard/abc-123/db-overview
   - AWS Console RDS: https://console.aws.amazon.com/rds/home?region=us-east-1
   - Sentry: https://sentry.io/organizations/voyager/projects/api/
4. Verify it's real (not transient):
   - Wait 60s; does signal persist?
   - Quick health check: `psql -h primary.voyager-db.us-east-1.rds.amazonaws.com -U health -c 'SELECT 1' -t 5`
5. If transient (auto-recovered): document; close PagerDuty; STOP
6. If real: classify severity (per Section 2); declare incident
7. P0: page DBA on-call (PagerDuty service "DBA-OnCall"); start #inc-YYYY-MM-DD-db-primary
```

### Quick triage commands

```bash
# DB connectivity test (from any app server)
psql -h primary.voyager-db.us-east-1.rds.amazonaws.com -U health -c 'SELECT 1' -t 5

# RDS instance status
aws rds describe-db-instances --db-instance-identifier voyager-db-primary --query 'DBInstances[0].DBInstanceStatus'

# Recent RDS events
aws rds describe-events --source-identifier voyager-db-primary --duration 30
```

Healthy state output:
- `psql`: `1`
- RDS status: `available`
- Recent events: routine maintenance only

Incident state output:
- `psql`: timeout or "could not translate host name"
- RDS status: `failover-in-progress` / `rebooting` / `incompatible-network`
- Recent events: include "DB instance restarted" / "Multi-AZ failover" / "Storage exhausted"

## 5. Phase 2: Containment

Goal: prevent customer-facing errors during DB unreachability.

### Immediate containment (in order)

```
1. Enable maintenance mode (returns 503 with retry-after header):
   ./scripts/maintenance-mode.sh on

2. Verify maintenance mode active:
   curl -i https://api.voyager.app/health
   (expect: 503 with body "maintenance")

3. Notify on Slack #incidents: maintenance mode active; users see graceful error

4. If failover in progress (RDS status = failover-in-progress):
   - Wait 60-90s (failover typical duration)
   - Watch RDS event stream
   - Do NOT manually restart instance — let RDS finish

5. If failover NOT in progress (status looks abnormal):
   - DO NOT restart manually
   - Page DBA on-call if not yet (see Section 9)
   - Continue to Eradicate phase
```

### What NOT to do during containment

- DO NOT manually trigger failover — RDS handles this; manual triggering can cause split-brain
- DO NOT restart RDS instance without DBA approval
- DO NOT modify security groups during incident (defer to post-incident root cause)

## 6. Phase 3: Eradicate

### Diagnostic approach

```
1. Check RDS Events for last 1 hour:
   aws rds describe-events --source-identifier voyager-db-primary --duration 60

2. Check CloudWatch metrics:
   - CPUUtilization
   - DatabaseConnections
   - FreeStorageSpace
   - ReadIOPS / WriteIOPS

3. Check VPC / Security Group changes (most common false positive):
   aws ec2 describe-security-groups --group-ids sg-XXXX
   git log --oneline tf/infrastructure/security-groups.tf | head -10

4. Check Postgres logs (if accessible):
   aws rds download-db-log-file-portion --db-instance-identifier voyager-db-primary --log-file-name error/postgresql.log
```

### Common root causes

| Symptom | Likely cause | Verify by | Fix |
|---------|--------------|-----------|-----|
| `connection refused` | Security group ACL changed | Compare current SG to yesterday's | Restore ACL via Terraform; `terraform apply` |
| `incompatible-network` status | RDS subnet group misconfig | Check VPC routing | DBA action: rebuild subnet group |
| `storage-full` | WAL accumulation due to slow replica | `df -h` on primary; replication lag check | Free WAL; investigate replica health |
| `failover-in-progress` for >5 min | Stuck failover | RDS event stream | Open AWS support case (P0) |
| Connection timeout but RDS healthy | Network ACL blocking new connections | Cross-AZ routing test | Investigate VPC config |

### Apply fix (after root cause identified)

```
1. Document hypothesis in #incidents channel
2. Get peer review (DBA or senior eng) — even 30 sec
3. Apply fix: <specific command>
4. Verify: rerun triage commands; expect healthy state
```

## 7. Phase 4: Recover

```
1. Once DB healthy, disable maintenance mode:
   ./scripts/maintenance-mode.sh off

2. Run smoke tests:
   ./scripts/smoke-test.sh staging  # quick first
   ./scripts/smoke-test.sh production --read-only

3. Verify customer-facing functionality:
   - Open https://app.voyager.app
   - Sign in (production smoke account)
   - Create test record (will be deleted after)
   - Verify it persists

4. Monitor 30 minutes:
   - Datadog dashboard: error rate normal
   - Synthetic checks passing
   - No replication lag

5. Declare resolved in #incidents
```

### Verification checklist

- [ ] Triage signal cleared (Datadog monitor green)
- [ ] Sentry error rate returned to baseline
- [ ] Synthetic API check passing
- [ ] Manual smoke test complete
- [ ] No replication lag >30s
- [ ] No queue backlog (BullMQ)
- [ ] No customer reports of issues in last 15 min

## 8. Communication

### Initial Slack #incidents (within 5 min)

```
[INCIDENT P0] DB primary unreachable
- Detected: 14:23 UTC
- Maintenance mode active; users see graceful 503
- Investigating per playbook
- IC: @engineer1
- Will update every 15 min
```

### Status page (within 5 min if customer-affecting)

```
Investigating: We're investigating an issue affecting our application.
Some users may see error messages or be unable to access their accounts.
Updates every 15 minutes until resolution.
```

### Resolution Slack

```
[RESOLVED] DB primary back online at 14:42 UTC. Duration: 19 min.
Root cause: Security group ACL change at 14:20 (preview deploy of WP-3.D).
Maintenance mode disabled; service restored.
Postmortem due 2026-09-22 by @dba.
```

### Resolution status page

```
Resolved: The issue affecting our application was resolved at 14:42 UTC.
Caused by an erroneous configuration change. Service is fully restored.
Postmortem will be published within 5 business days.
We apologize for the disruption.
```

## 9. Escalation Tree

| Severity | Initial responder | If not acked in 5 min | If unresolved at 30 min |
|----------|--------------------|------------------------|-------------------------|
| P0 | Primary on-call + DBA on-call | Page Eng Manager + secondary DBA | Page CTO; consider customer outreach |
| P1 | Primary on-call (DBA optional) | Page DBA on-call | Page Eng Manager |
| P2 | Primary on-call (NBD OK) | n/a | n/a |

### Contacts

| Role | Name | Slack | PagerDuty |
|------|------|-------|-----------|
| Primary on-call (rotation) | (rotation) | #oncall-rotation | "Voyager-OnCall" service |
| DBA on-call (rotation) | (rotation) | #db-oncall | "DBA-OnCall" service |
| Eng Manager | Sarah K. | @sarah | (PagerDuty) |
| CTO | Mike J. | @mike | (P0 only via PagerDuty) |
| AWS TAM (P0) | Account team | (escalate via Eng Manager) | n/a |

## 10. Postmortem Trigger

Postmortem REQUIRED for this incident class always (P0 default).

Doc due in 48h: `docs/04_MAINTENANCE/postmortems/2026-09-20_db-primary-unreachable.md`

Include in PM:
- Timeline (every event with timestamp)
- Why detection took N minutes (signal lag analysis)
- Why fix took N minutes (could it be faster?)
- Why root cause occurred (5-Whys)
- Action items: monitoring improvements, alert refinement, runbook updates

## 11. Recovery Verification (after closure)

- [ ] Postmortem published
- [ ] Action items in roadmap (specific WPs)
- [ ] Playbook updated if drill revealed friction
- [ ] Detection signals refined if false-positive / false-negative
- [ ] Customer comms completed (status page, support tickets)

## 12. Drill History

| Date | Type | Outcome | Action items |
|------|------|---------|--------------|
| 2026-09-15 | Tabletop | Pass with friction | (1) Slack channel name lookup added; (2) DBA on-call PagerDuty service name clarified; both incorporated above |
| 2026-06-10 | Live drill (controlled) | Pass | RDS failover took 87s; no customer impact (maintenance mode caught) |

Next drill: 2027-01-15 (quarterly).

## 13. References

- Related: `INCIDENT_POSTGRES_REPLICA.md`, `INCIDENT_CONNECTION_POOL.md`, `INCIDENT_DB_PERFORMANCE.md`
- Architecture: `docs/01_DISCOVERY/CODEBASE_MAP.md`
- Data: `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`
- Operational runbooks (non-incident): `docs/04_MAINTENANCE/runbooks/DB_BACKUP.md`, `DB_FAILOVER_DRILL.md`
```

---

## Calibration notes

- **"What this incident is NOT" eliminates ambiguity.** Three distinct DB-related incidents have separate playbooks; this section helps on-call route correctly.
- **Triage commands include expected output.** "If `psql` returns `1`, healthy" — saves on-call from googling at 2am.
- **Containment uses maintenance mode.** Stops customer-facing errors fast; gives time for proper diagnosis.
- **"Do NOT" warnings prevent worse situations.** Manual restart can cause split-brain; explicit prohibition.
- **Common root causes table is project-specific.** Built from real incident history.
- **Communication templates pre-written.** No on-call author writing prose under pressure.
- **Drill history shows friction-driven improvements.** Tabletop revealed Slack channel ambiguity; playbook updated.
- **PM trigger is automatic for P0.** No "do we need a PM?" debate.
