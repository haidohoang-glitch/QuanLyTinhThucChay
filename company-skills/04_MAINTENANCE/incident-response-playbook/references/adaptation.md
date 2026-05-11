# Incident Response Playbook — Adaptation

Variations by incident type and team setup.

> **Applies to Mode A (NIST IR phases) only.** Mode B/C follow conventions.

## Data corruption / loss incidents

**Critical adjustments:**
- Containment FIRST: stop further writes (read-only mode, queue ingest, etc.)
- Triage MUST verify scope: how many records affected? When did corruption start?
- Eradication usually involves: identify last good backup; choose between point-in-time recovery (PITR) vs forward-fix vs accepting some data loss
- Recovery is high-stakes: do NOT rush; consult DBA + tech lead

**Add:**
- Explicit "data loss tolerance" question (which records can be reconstructed from logs?)
- Customer communication template specifically for data loss (legal review may be required)
- Backup verification commands (verify backup CAN be restored; don't trust untested backups)

## Auth bypass / suspected breach

**Critical adjustments:**
- Containment IS the priority: revoke sessions, rotate keys, disable affected accounts
- Eradication may involve security team partnership
- Communication: legal must be looped in BEFORE customer comms (potential disclosure obligations)

**Add:**
- Forensic preservation: save logs / states before changing things (for investigation)
- Coordinate with: Security Lead + Legal + CEO from minute 1
- Status page may be DELAYED until legal review (vs. typical immediate update)

## Performance / latency spikes

**Adjust:**
- Detection often gradual; thresholds matter (don't trigger on every blip)
- Triage: distinguish capacity issue (scale up) from regression (rollback)
- Containment: scale up resources, enable caching, reduce traffic gracefully

**Common root causes for this incident type:**
- Recent deploy (regression)
- Cache cold (after invalidation event)
- Hot key in cache / DB
- Vendor latency (downstream service slow)
- Capacity exceeded (real growth or DoS)

## Cost spike

**Adjust:**
- Often non-customer-facing initially (P2 or P3)
- Detection: budget alerts, vendor invoice anomaly
- Containment: identify and stop runaway resource (loop, infinite retry, leak)
- Communication: internal only usually

**Watch for:**
- AI cost spikes (someone spawned 10K agent calls)
- DB query cost (full-scan introduced)
- Egress cost (data moving cross-region unexpectedly)

## Vendor outage cascade

**Adjust:**
- Triage: distinguish your incident from vendor incident
- If vendor down: limited eradication options; focus on graceful degradation
- Communication: customer status pages should reference vendor's status page if relevant

**Add:**
- Vendor status page links: AWS, Stripe, GitHub, etc.
- Pre-defined "graceful degradation" modes per service
- SLA tracking: did vendor meet their SLA? Credit due?

## Certificate expiry

Specific incident type — preventable but happens:

**Detection:**
- Alert N days before expiry (ideally 30 days)
- Acute alert at expiry (TLS handshake failures)

**Eradicate:**
- Rotate certificate (specific commands)
- Verify new cert deployed across all relevant services
- Update monitoring with new expiry date

**Postmortem:** WHY did proactive monitoring fail to alert in time?

## Compliance violation discovered

**Critical adjustments:**
- May trigger regulatory disclosure obligations (timing varies: 72h GDPR, 60d HIPAA, etc.)
- Legal involvement from minute 1
- Communication may be delayed by legal review

**Add:**
- Disclosure timeline by regulation
- Internal counsel contact info
- "Should this be a public disclosure?" decision tree

## Customer complaint cascade

When mass customer complaints appear (regression or visible bug):

**Detection:**
- Support ticket volume spike
- Social media spike
- Sentry error rate

**Triage:**
- Confirm: is this a real issue or a misunderstanding?
- If real: identify which user segments affected
- Communication BEFORE eradication: customers want acknowledgment first

## On-call team variations

### Solo on-call (no rotation)

- Page goes to one person; high cognitive load
- Playbooks must be very detailed (no peer to ask)
- Escalation tree may be: solo → manager → external consultant

### Follow-the-sun on-call

- Multiple regions cover 24/7
- Handoffs explicit (incident state communicated across timezones)
- Playbook language must work for non-native speakers

### Junior on-call (newer engineers)

- Playbooks more prescriptive (less "use judgment")
- Escalation more aggressive (escalate sooner)
- Pair-on-call for first incidents

### Senior-only on-call

- Less rigid playbooks (judgment calls expected)
- But: still have playbooks for skim-readability under pressure
- Postmortem rigor enforced (seniors most likely to skip "obvious" ones)

---

## Severity calibration

Don't inflate severity. P0 reserved for:

- Customer-facing total outage (>50% requests failing)
- Security breach with data exposure
- Compliance violation (with disclosure obligation)
- Imminent (< 1 hour) risk of any of the above

Common P0 inflation traps:
- "It feels critical" → no, P0 is observable
- "Customer is angry" → P1 perhaps; P0 only with broader impact
- "Could become worse" → P1 with escalation criteria

Rigid calibration prevents alert fatigue.

---

## Playbook lifecycle

| Stage | Trigger | Action |
|-------|---------|--------|
| Draft | Need identified | Author per this skill |
| Reviewed | Tabletop drilled | Update for friction points |
| Approved | Tech lead + ops sign-off | Mark v1; place in `docs/04_MAINTENANCE/runbooks/` |
| Maintained | Quarterly + post-incident | Update contact info; refine commands |
| Retired | Incident class no longer applies | Mark archived; move to `_archive/` |

Don't keep playbooks in eternal "draft" — they need to be live to be useful.
