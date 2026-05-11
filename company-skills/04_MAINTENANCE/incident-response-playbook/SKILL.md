---
name: incident-response-playbook
description: Author incident response playbooks (runbooks) — per-incident-type procedures covering detection, triage, containment, eradication, recovery, and post-mortem. Each playbook is a step-by-step guide for on-call engineers to follow during an incident. Use after go-live when establishing on-call processes, when adding new incident classes (DB outage, auth bypass, cost spike), when preparing for compliance audit (SOC2 requires IR plans), or when generating Phase 4 Maintenance runbook output. Triggers include "create incident playbook", "IR runbook", "what to do when X happens", "on-call procedure", "author INCIDENT_RESPONSE", or "Phase 4 Maintenance runbook".
---

# Incident Response Playbook

Author per-incident-type runbooks: structured procedures for on-call engineers responding to specific failure scenarios. Output is one or more files in `docs/04_MAINTENANCE/runbooks/INCIDENT_<TYPE>.md`.

## When this skill applies

Use when:
- Project goes live (or moves to production-like staging); on-call needs procedures
- New incident class identified (e.g., new third-party integration adds new failure mode)
- Compliance audit prep (SOC2, ISO 27001 require IR plans)
- Postmortem reveals a class of incident lacking a playbook → author one
- Generating Phase 4 Maintenance output

Do NOT use for:
- Normal operations runbooks (deployment, scaling — different category)
- Feature extension (use `feature-extension-planning`)
- Code-level documentation (handled by code comments / ADRs)

## Inputs

1. `docs/01_DISCOVERY/CODEBASE_MAP.md` — to understand what's deployed and dependencies
2. `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` — data layer failure modes
3. `docs/00_REQUIREMENTS/SRS_VI/M9` (NFRs) — RTO, RPO, uptime targets
4. **Observability tooling:** Sentry / Datadog / etc. — what alerts exist, what metrics
5. **Team contacts:** on-call rotation, escalation tree
6. **Past incidents:** review postmortems to identify common patterns

## Output

One or more files: `docs/04_MAINTENANCE/runbooks/INCIDENT_<TYPE>.md`. Each playbook covers ONE incident class; create separate playbooks for different incident types.

Filled from [assets/INCIDENT_RUNBOOK_template.md](assets/INCIDENT_RUNBOOK_template.md).

## Workflow

### Step 1 — Identify incident classes

What incidents need playbooks? Common categories:

| Category | Examples |
|----------|----------|
| Availability | Total outage, partial degradation, region failure |
| Performance | Latency spike, throughput collapse, queue backlog |
| Data | Corruption, accidental deletion, replication lag |
| Security | Auth bypass, suspected breach, anomalous access |
| Compliance | PII leak, audit gap, retention violation |
| Operational | Cost spike, vendor outage, certificate expiry |
| Customer | Mass complaints, regression after deploy, lost data report |

For each class your project faces, you need a playbook. Don't try to author all at once; prioritize by likelihood × impact (build for top 5-10 first).

### Step 2 — Choose playbook structure mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — NIST IR phases** *(default)* | No specific framework required | Prepare / Detect / Respond / Recover / Lessons |
| **B — Honor company IR standard** | Company has formal IR framework | Company doc |
| **C — User-defined IR phases** | Specific phasing (e.g., per-vendor SOC) | User input |

Selection logic:
1. User explicit → use it
2. Company has IR framework (ISMS, SOC2-aligned, etc.) → ask user
3. Default → Mode A

#### Mode A — NIST 800-61-style IR phases

| Phase | Purpose | Time horizon |
|-------|---------|---------------|
| **Prepare** | What's set up before incident | Pre-incident (always) |
| **Detect & Analyze** | Recognize incident; classify severity | Minutes |
| **Contain** | Stop the bleeding | Minutes-hours |
| **Eradicate** | Remove root cause | Hours-days |
| **Recover** | Restore service | Hours-days |
| **Post-incident** | Lessons learned, prevent recurrence | Days-weeks |

Each playbook has sections per phase.

### Step 3 — For each playbook, fill the structure

Use [assets/INCIDENT_RUNBOOK_template.md](assets/INCIDENT_RUNBOOK_template.md). Populate:

- **Incident type** (1 specific class — e.g., "Postgres primary unreachable")
- **Severity classification** (P0/P1/P2 with criteria)
- **Detection signals** (alerts, customer reports, monitor patterns)
- **Triage steps** (first 5 minutes — what to verify, what to rule out)
- **Containment steps** (stop further damage)
- **Eradication steps** (root cause fix)
- **Recovery steps** (service restoration; verification)
- **Communication template** (who to notify when; status page wording)
- **Postmortem trigger** (when required)

### Step 4 — Define detection signals concretely

Vague detection: "API is slow"
Concrete detection:
- Datadog monitor: `api.response_time.p95 > 1000ms for 5min`
- Customer report via Zendesk
- Synthetic check failing in `synthetics-prod` workspace
- Sentry error rate >5x baseline

For each signal, specify the response: "If this signal fires, this playbook applies."

### Step 5 — Write triage runbook (first 5 minutes)

What does the on-call do in the first 5 minutes? This is the most important section — clear thinking under pressure requires pre-written steps.

Example:
```
1. Acknowledge alert in PagerDuty (signals you're aware)
2. Open #incidents Slack channel; type "responding to [alert name]"
3. Open dashboards: [link to relevant Datadog board]
4. Check: is this an active incident or transient? Wait 60s for second signal.
5. If still firing: declare incident; classify severity (P0/P1/P2)
6. If P0 or P1: page incident commander
```

Steps must be runnable by someone who has not memorized the system.

### Step 6 — Write containment steps

How to stop further damage WITHOUT necessarily fixing root cause:

- Feature flag off (specify which flag)
- Disable webhook endpoint (specify route)
- Failover to secondary (specify command)
- Enable degraded mode (specify config flag)

Containment buys time. Eradication can be slower.

### Step 7 — Write eradication steps

Root-cause fix:
- Identify root cause via diagnostics (specify queries / logs)
- Apply fix (deploy, config change, data correction)
- Verify root cause addressed

This section may be open-ended for unfamiliar incidents; document the diagnostic approach.

### Step 8 — Write recovery + verification

How to confirm service is fully restored:

- Re-enable feature flag
- Failback from secondary
- Run synthetic checks
- Customer-facing health check
- Monitor for 30 minutes for recurrence

### Step 9 — Communication templates

Pre-written templates for:
- Initial alert to engineering team (Slack)
- Status page update (customer-facing)
- Internal stakeholder update (executives, customer success)
- All-clear communication
- Post-incident report (24-48 hours later)

Pre-writing avoids panic typos under pressure.

### Step 10 — Define escalation tree

Who gets paged when:

| Severity | Initial response | If not acknowledged in N min |
|----------|------------------|-------------------------------|
| P0 | Primary on-call + Eng manager | Page secondary on-call + VP Eng |
| P1 | Primary on-call | Page secondary on-call |
| P2 | Primary on-call (next business day OK) | Auto-close after 24h if no response |

### Step 11 — Postmortem template

For P0/P1 incidents, postmortem required within 48 hours. Include:
- Timeline (event-by-event)
- Impact (customers affected, duration, revenue impact)
- Root cause (5-Whys analysis)
- Action items (preventive)
- Lessons learned (what to add to playbook)

Reference template; don't author full PM here.

### Step 12 — Self-review

Run [references/checklist.md](references/checklist.md). Playbook tested in tabletop exercise before relying on it.

## Quality bar

A good playbook lets:
- A new on-call engineer respond confidently to an incident type they've never seen
- The first 5 minutes happen without needing to "figure out what to do"
- Communication go out promptly (templates ready)
- Postmortem produce action items (not just "be more careful")

If the playbook says "investigate and decide", it's not a playbook. It's an aspiration.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations by incident type (data corruption — different from cost spike — different from auth bypass) and by on-call team setup (solo vs. follow-the-sun, junior vs. senior).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: incident playbook for "Postgres primary unreachable" — a common P0 incident class.

## Failure modes to avoid

- **Vague steps.** "Check the database" — by what command? "Run `psql -h primary.db -U readonly -c 'SELECT 1;'`" — actionable.
- **No detection signal.** If you don't know how the incident is detected, you can't trigger the playbook.
- **No containment vs eradication separation.** Stop bleeding fast; fix root cause carefully — these are separate steps.
- **No communication templates.** On-call writing prose under pressure makes worse messages.
- **No postmortem trigger.** Without explicit trigger, postmortems get skipped — same incident recurs.
- **Single playbook for all incidents.** One playbook per incident class; resist over-generalizing.
- **No tabletop exercise.** Playbook untested = playbook unproven. Drill before need.
- **Stale contact info.** Names / Slack channels / phone numbers change; review quarterly.
