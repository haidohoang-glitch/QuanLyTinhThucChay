# Incident Playbook — {{INCIDENT_TYPE}}

> **Incident class:** {{ONE_LINE — e.g., "Postgres primary unreachable"}}
> **Severity (default):** {{P0 / P1 / P2}}
> **Last updated:** {{YYYY-MM-DD}}
> **Last drilled:** {{YYYY-MM-DD or "Never — first drill before relying on this playbook"}}
> **Owner:** {{NAME — runbook maintainer}}

---

## 1. Incident Signature

### What this incident IS

{{1-paragraph definition of this specific incident class. Distinguish from similar incidents.}}

### What this incident is NOT

- {{Distinguish from related incidents that have separate playbooks}}
- {{Distinguish from non-incident events that might look similar}}

---

## 2. Severity Classification

| Severity | Criteria | Examples |
|----------|----------|----------|
| **P0** | {{Customer-facing total outage; data loss; security breach}} | {{e.g., All API requests returning 5xx; database unrecoverable}} |
| **P1** | {{Significant degradation; partial outage}} | {{e.g., Some endpoints failing; single region down}} |
| **P2** | {{Latent issue; recoverable; low customer impact}} | {{e.g., Monitoring degraded; single user affected}} |

Default classification for THIS incident class: **{{P0 / P1 / P2}}**

(May escalate based on observed impact during triage.)

---

## 3. Detection Signals

If ANY of these signals fire, this playbook applies:

| Signal | Source | Threshold |
|--------|--------|-----------|
| {{e.g., Datadog monitor "DB primary connection failures"}} | Datadog | >50 errors/min for 2 min |
| {{e.g., Sentry alert "DatabaseError"}} | Sentry | >100 events in 5 min |
| {{e.g., Customer report}} | Zendesk / Intercom | "Cannot save", "site is down" pattern |
| {{e.g., Synthetic check failing}} | Pingdom / Datadog Synthetics | 3 consecutive failures |

---

## 4. Phase 1: Triage (first 5 minutes)

Run these steps IN ORDER. Do not skip.

```
1. Acknowledge in PagerDuty (signals "I'm responding")
2. Post to #incidents Slack: "Responding to [alert]. Investigating per
   docs/04_MAINTENANCE/runbooks/INCIDENT_<TYPE>.md"
3. Open monitoring:
   - {{LINK_TO_DATADOG_BOARD}}
   - {{LINK_TO_SENTRY_PROJECT}}
4. Verify it's a real incident (not transient):
   - Wait 60s; does signal persist?
   - Run quick health check: `{{COMMAND}}`
5. If transient (auto-recovered): document; close PagerDuty; STOP
6. If real incident: classify severity (use Section 2 criteria); declare incident
7. If P0 or P1: page incident commander; start incident channel #inc-<date>
```

### Quick triage commands

```bash
# Health check
{{COMMAND_1}}

# Connectivity test
{{COMMAND_2}}

# Last successful operation
{{COMMAND_3}}
```

Expected output for healthy state: {{DESCRIBE}}
Expected output for incident state: {{DESCRIBE}}

---

## 5. Phase 2: Containment

Goal: stop further damage. Does NOT need to fix root cause yet.

### Immediate containment steps (in order)

```
1. {{e.g., Disable feature flag `enable_X`: `gh ./scripts/flag-off.sh X`}}
2. {{e.g., Failover to read replica: `./scripts/failover-to-replica.sh`}}
3. {{e.g., Increase rate limits to absorb spike: edit nginx.conf line 42}}
4. {{e.g., Page secondary engineer if scope expands}}
```

### What NOT to do during containment

- {{e.g., Do NOT restart Postgres primary without DBA approval — risks data loss}}
- {{e.g., Do NOT roll back deploy until you confirm deploy caused incident}}

---

## 6. Phase 3: Eradicate (root cause fix)

### Diagnostic approach

Identify root cause:

```
1. {{Check error logs: command + what to look for}}
2. {{Check resource utilization: command + what's normal}}
3. {{Check recent changes: `git log --since='2 hours ago' --oneline`}}
4. {{Check vendor status pages: AWS, Stripe, etc.}}
```

### Common root causes for this incident class

| Symptom | Likely cause | Verify by | Fix |
|---------|--------------|-----------|-----|
| {{e.g., Connection refused}} | {{Network ACL change}} | {{Compare with yesterday's ACL}} | {{Restore previous ACL}} |
| {{e.g., Slow queries}} | {{Missing index}} | {{`EXPLAIN ANALYZE` slow query}} | {{Add index in migration}} |
| {{e.g., Disk full}} | {{WAL accumulation due to slow replica}} | {{`df -h` + replication lag check}} | {{Free WAL space; investigate replica}} |

### Apply fix

```
1. Document hypothesis in incident channel
2. Get peer review on proposed fix (even if 30 seconds)
3. Apply fix: {{HOW}}
4. Verify fix: {{HOW}}
```

---

## 7. Phase 4: Recover

Goal: restore service to normal.

```
1. {{e.g., Re-enable feature flag `enable_X`}}
2. {{e.g., Failback to primary: `./scripts/failback.sh`}}
3. Verify with smoke test: `{{COMMAND}}`
4. Monitor for 30 minutes
5. If stable, declare resolved in #incidents
```

### Verification checklist

- [ ] Detection signals returned to normal (alerts resolved)
- [ ] Synthetic checks passing
- [ ] No spike in error rate
- [ ] Customer-facing functionality verified manually (key flow)
- [ ] No replication lag, no queue backlog
- [ ] No new incidents triggered by recovery actions

---

## 8. Communication

### Internal — Slack #incidents

Initial:
```
[INCIDENT P{{N}}] {{Brief description}}
- Detected: {{TIME}}
- Currently investigating
- IC: {{NAME}}
- Will update every 15 min
```

Update (every 15 min):
```
[UPDATE] {{TIME}}
- Status: {{Investigating / Mitigating / Recovering / Resolved}}
- Action: {{Latest action}}
- Customer impact: {{description}}
- ETA to resolution: {{EST OR Unknown}}
```

Resolution:
```
[RESOLVED] {{TIME}}
- Duration: {{N minutes}}
- Root cause: {{One line}}
- Postmortem due by: {{DATE — typically 48 hours}}
```

### External — Status page (customer-facing)

Initial (within 5 min if customer-affecting):
```
{{Investigating | Identified | Monitoring | Resolved}}: {{Brief, jargon-free description}}.
We are actively working on this. {{Optional: workaround if any}}.
Updates every 15 min until resolution.
```

Resolution:
```
The issue affecting {{description}} has been resolved as of {{TIME UTC}}.
{{Brief root cause if customer-facing}}. We apologize for the disruption.
A detailed postmortem will be published within 5 business days.
```

### Stakeholder update (P0 only)

Email/Slack DM to: CEO, CTO, VP Customer Success, key customer contacts (if affected).

```
Subject: [P0 Incident] {{Type}} — {{Status}}

What happened: {{2 sentences}}
Customer impact: {{Specific}}
Current status: {{Investigating / Mitigating / Resolved}}
ETA: {{If known}}
Customer contacts in progress: {{Yes/No}}

Will provide update at {{TIME}}.

— {{IC NAME}}, Incident Commander
```

---

## 9. Escalation Tree

| Severity | Initial responder | If not acked in 5 min | If still unresolved at 30 min |
|----------|--------------------|------------------------|-------------------------------|
| P0 | Primary on-call + Eng Manager | Page secondary + VP Eng | Page CTO; consider customer outreach |
| P1 | Primary on-call | Page secondary | Page Eng Manager |
| P2 | Primary on-call (NBD OK) | Auto-close after 24h | n/a |

### Contacts

| Role | Name | Slack | Phone (P0 only) |
|------|------|-------|------------------|
| Primary on-call | (rotation) | #oncall-rotation | PagerDuty |
| Secondary on-call | (rotation) | #oncall-rotation | PagerDuty |
| Eng Manager | {{NAME}} | @{{handle}} | (PagerDuty) |
| VP Eng | {{NAME}} | @{{handle}} | (PagerDuty P0 only) |
| DBA on-call | (rotation) | #db-oncall | PagerDuty |

---

## 10. Postmortem Trigger

Postmortem REQUIRED for:
- All P0 incidents (within 48 hours)
- P1 incidents with customer impact >15 minutes
- Any incident triggering second-line escalation
- Incidents revealing systemic gap (root cause spans multiple components)

Postmortem template: `docs/04_MAINTENANCE/postmortems/templates/POSTMORTEM_template.md`

Postmortem doc due in: `docs/04_MAINTENANCE/postmortems/{{YYYY-MM-DD}}_{{INCIDENT_TYPE}}.md`

---

## 11. Recovery Verification (final state)

After incident closed, ensure:

- [ ] Action items from postmortem captured (in roadmap or backlog)
- [ ] Playbook updated with lessons learned (specific changes)
- [ ] Detection signals refined if false-positive or false-negative
- [ ] Customer communication completed (status page, support ticket follow-ups)
- [ ] Documentation drift addressed (any docs out of sync with reality?)

---

## 12. Last Drill Date / Quality

| Drill date | Drill type | Outcome | Action items closed |
|------------|------------|---------|---------------------|
| {{YYYY-MM-DD}} | Tabletop / Live | {{Pass/Partial/Fail}} | {{Y/N}} |

If "Last drilled" >6 months ago, schedule new drill before relying on this playbook.

---

## 13. References

- Related playbook: {{LIST}}
- Architecture context: `docs/01_DISCOVERY/CODEBASE_MAP.md`
- Data context: `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`
- Runbook for normal operations (not incident): `docs/04_MAINTENANCE/runbooks/{{NORMAL_OP}}.md`

---

*This playbook is for reading during incidents. Optimize for skim-readability, not narrative flow.*
