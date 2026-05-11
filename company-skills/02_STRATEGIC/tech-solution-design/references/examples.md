# Tech Solution Design — Worked Example

Anonymized. Continuing **"Project Helix"** (healthcare records system from `data-architecture-audit`). Mode A.

## Context

**Imagined input:** "Helix needs to migrate from single-region monolith to multi-region active-passive. SRS requires 99.9% uptime, EU data residency for new EU customers, p95 latency <100ms for EU reads. Audit found 5 P1 data risks. Design the solution."

**Time budget:** 16 hours over 1 week.

**Mode chosen:** Mode A (existing system has no formal ADRs; designing fresh).

---

## Output excerpt

```markdown
# Project Helix — Tech Solution Design

## 1. Problem Frame

**What we have:** Single-region monolith (Express + Postgres + Redis + S3 in us-east-1).
Serves 200+ outpatient clinics, mostly US.

**What we need:** Multi-region active-passive (us-east-1 primary, eu-west-1 read replica)
to satisfy SRS NFR-PERF-01 (EU read latency <100ms p95) and NFR-COMP-03 (EU data residency
for new EU customers).

**The gap:** Current arch has no replication primitive; data layer is single-region;
auth tokens in localStorage (TECH_DEBT_AUDIT F-03 P0); audit log retention misaligned
with HIPAA Six Year requirement.

**Constraints:** $480K budget (per Partial scenario in FEASIBILITY); 14-week timeline;
4 senior backend devs; no major UI changes; SOC2 Type I deadline Q4.

---

## 3. Candidate Architectures

| Candidate | Pattern | Why considered | Strengths | Weaknesses | Cost |
|-----------|---------|----------------|-----------|------------|------|
| A | Active-Passive multi-region (Postgres logical replication) | Direct fit for read-only EU; minimal arch change | Mature pattern; team familiar; small migration | EU read-only (no writes from EU); replication lag must be managed | Low |
| B | Active-Active multi-region (custom CRDT layer) | Full EU writes; future-proof | Reads + writes from any region | Major arch change; custom layer; team unfamiliar; 2x complexity | High |
| C | Hybrid (Active-Passive base + write forwarding for EU) | EU writes proxied to us-east-1 | Compromise; user-perceived bidirectional | Latency on EU writes (round-trip to US); cache invalidation issues | Medium |

(Two candidates would be too few; four would be overthinking.)

---

## 4. Comparison Matrix

| Requirement / Criterion | A (Active-Passive) | B (Active-Active) | C (Hybrid) |
|------------------------|--------------------|--------------------|-----------|
| FR-AUTH-01..N | ✅ Native | ✅ Native | ✅ Native |
| FR-{{EU_NEW_CUSTOMER_ONBOARDING}} | ✅ EU users see EU data | ✅ Native | ⚠️ Write latency 100-200ms |
| NFR-PERF-01 (EU read p95 <100ms) | ✅ <60ms typical from EU node | ✅ Native | ✅ Native (reads) |
| NFR-PERF-02 (EU write p95 <500ms) | ⚠️ Writes still go to US (~120ms RT) | ✅ Native | ❌ 200ms+ RT typical |
| NFR-REL-01 (99.9% uptime) | ✅ Region failover possible | ✅ Native | ⚠️ Adds dependency on writeforward |
| NFR-COMP-03 (EU data residency for EU customers) | ✅ Sufficient (read traffic from EU) | ✅ Native | ⚠️ Writes still touch US — may not satisfy EU regulator |
| NFR-COMP-HIPAA | ✅ | ✅ | ✅ |
| Team familiarity | ✅ Postgres replication well-known | ❌ CRDT new to team | ⚠️ Mid |
| Migration cost | ✅ ~14 weeks (matches FEASIBILITY budget) | ❌ ~28 weeks ($1.4M+) | ⚠️ ~18 weeks ($600K+) |
| Time-to-first-value | ✅ EU reads working at week 8 | ❌ Earliest at week 18 | ⚠️ Week 12 |
| Risk profile | Low (mature pattern) | High (custom layer) | Medium |
| **Score (qualitative)** | **9/11 ✅** | 6/11 ✅ | 5/11 ✅ |

---

## 5. Architecture Decision Record (ADR)

### ADR-001: Adopt Active-Passive Multi-Region (Candidate A)

**Status:** Proposed (review by Tech Lead + DBA + Compliance Lead by 2026-06-15)

**Context:** Helix needs to serve EU customers per NFR-PERF-01 (latency) and NFR-COMP-03 (residency)
within Q4 SOC2 deadline. Three architecture candidates were evaluated against requirements
and constraints.

**Decision:** Adopt Active-Passive multi-region using Postgres logical replication.
Primary writer in us-east-1; read replica in eu-west-1; EU customer reads served from
eu-west-1; EU customer writes proxy to us-east-1.

**Rationale:**
1. Best fit for current 14-week budget; team has existing Postgres replication expertise
2. Satisfies critical NFRs (EU read latency, US data residency); compromise on EU write
   latency acceptable per Compliance review (writes are infrequent vs reads in clinical
   workflow)
3. Enables future migration to active-active if EU customer volume grows; pattern is a
   stepping stone, not a dead-end

**Consequences (positive):**
- Mature, well-understood pattern reduces operational risk
- Existing tooling (Datadog, RDS automated PITR) extends naturally
- Failover procedure (us-east-1 outage) becomes feasible (separate WP)

**Consequences (negative — accepted):**
- EU customer writes have ~120ms latency from EU (acceptable per NFR-PERF-02 target ≤500ms)
- Two regions to monitor and operate (slight ops overhead)
- Replication lag must be monitored; reads in EU may serve slightly-stale data (0-30s typical)
- Data residency for EU customers is "EU read replica only" — writes still cross Atlantic;
  Compliance has signed off this is acceptable per current EU customer count <10 and DPA
  language; Active-Active reconsidered in Year 2 if EU customers >50

**Alternatives rejected:**
- **Candidate B (Active-Active CRDT):** Rejected because cost ($1.4M) and timeline (28w)
  exceed Partial budget; complexity adds risk for first-time adoption
- **Candidate C (Hybrid):** Rejected because EU write latency (200ms+) likely exceeds
  NFR-PERF-02 target under load; complexity of write-forward layer adds risk without
  proportionate benefit

**Revisit conditions:**
- If EU customer count exceeds 50 (re-evaluate active-active)
- If EU regulator changes residency interpretation requiring writes in EU
- If replication lag exceeds 60s sustained (re-evaluate replication strategy)

---

## 6. Component Design

### Component diagram

```
                    ┌────────────────────┐
                    │   API Gateway       │
                    │  (CloudFront/Route53)│
                    └────────┬─────────────┘
                             │
              ┌──────────────┴──────────────────┐
              │                                  │
              ▼                                  ▼
    ┌─────────────────┐                ┌─────────────────┐
    │  US Region      │                │  EU Region      │
    │  (us-east-1)    │                │  (eu-west-1)    │
    │                 │                │                 │
    │  ┌───────────┐ │                │  ┌───────────┐ │
    │  │ Express   │ │   reads        │  │ Express   │ │
    │  │ App       │◄├────────────────┤  │ App       │ │
    │  │ (writer)  │ │                │  │ (reader)  │ │
    │  └─────┬─────┘ │                │  └─────┬─────┘ │
    │        │       │                │        │       │
    │  ┌─────▼─────┐ │   logical repl │  ┌─────▼─────┐ │
    │  │ Postgres  │─├────────────────►  │ Postgres  │ │
    │  │ (primary) │ │                │  │ (replica) │ │
    │  └───────────┘ │                │  └───────────┘ │
    │  ┌───────────┐ │                │  ┌───────────┐ │
    │  │ Redis     │ │                │  │ Redis     │ │
    │  │ (sessions)│ │                │  │ (sessions)│ │
    │  └───────────┘ │                │  └───────────┘ │
    └─────────────────┘                └─────────────────┘
              ▲                                  ▲
              └─────── shared S3 (us-east-1) ────┘
              └─────── shared Auth0 (global) ────┘
```

### Component inventory

| Component | Purpose | Public interface | Depends on | Anti-scope |
|-----------|---------|------------------|------------|------------|
| API Gateway (CF + R53) | Geo-route requests to nearest region | DNS resolution + HTTPS proxy | Health checks of regional apps | Does NOT do auth, business logic |
| Regional App (US writer) | Handles all writes; reads in US | HTTPS REST API | Postgres-US, Redis-US, S3, Auth0 | Does NOT cross-region read |
| Regional App (EU reader) | Handles EU reads; proxies EU writes to US | HTTPS REST API | Postgres-EU (read), Redis-EU, US writer (for write proxy) | Does NOT write to Postgres-EU |
| Postgres Primary (US) | Source of truth | SQL | Internal | Does NOT serve EU read traffic directly |
| Postgres Replica (EU) | Read-only replica | SQL (read-only) | Postgres-US logical replication | Does NOT accept writes |
| Redis (US, EU) | Sessions + per-region cache | Redis protocol | Per-region Postgres for cache miss | Does NOT replicate cross-region |
| S3 | Document storage | S3 API | KMS for encryption | Does NOT replicate to EU at v1 (Year 2 plan) |
| Replication Monitor | Track replication lag | Metrics | Postgres replication slots | Does NOT auto-promote |

---

## 7. Data Evolution

### Current state
Single Postgres in us-east-1; no replication; manual backups via RDS PITR.

### Target state
Postgres primary us-east-1; logical replication to eu-west-1 replica; replication slot
monitored; failover playbook documented.

### Schema changes

| Change | Type | Migration approach | Rollback |
|--------|------|---------------------|----------|
| Enable logical replication on primary | Config (no schema) | Pre-migration: ALTER SYSTEM SET wal_level=logical; restart | Revert wal_level |
| Add replication slots for EU replica | Config | CREATE PUBLICATION; CREATE SUBSCRIPTION | Drop subscription |
| Add `region_origin` column to audit_log | Additive | Online (with default 'us-east-1') | Drop column |
| Add per-tenant `data_region` column | Additive | Online (default 'US') | Drop column |

### Data migration plan

- **Strategy:** Set up replication; let initial sync complete; switch EU reads gradually
- **Initial sync:** ~2-4 hours expected (database ~80GB at current size); plan during low-traffic window
- **Reconciliation:** Replication monitor alerts if lag >30s; weekly automated row count comparison between primary and replica
- **Compatibility window:** App code reads from "regional store" abstraction; before cutover, all regions read from US; after cutover, EU reads from EU. No code change for compatibility — done via routing.

### Rollback for replication
- Drop EU subscription
- EU app continues serving stale cache during incident
- Resume EU reads from US (cross-Atlantic latency, but available)

---

## 9. Rollout Strategy

### Phasing

| Phase | What ships | Behind feature flag? | Rollout % | Cutover criterion |
|-------|------------|----------------------|-----------|--------------------|
| 1 | EU infra deployed (VPC, RDS replica, ECS cluster) | n/a | 0% traffic | Healthchecks pass; replication lag <30s for 7 days |
| 2 | EU app receives no live traffic; smoke tests | n/a | 0% | Smoke tests pass; replication validated |
| 3 | EU read traffic gradually shifted | Yes (`eu_read_pct`) | 5% → 25% → 50% → 100% | Latency, error rate stable per stage; full week between stages |
| 4 | EU write proxy enabled | Yes (`eu_write_proxy`) | 100% (binary flip) | Phase 3 stable for 30 days |
| 5 | Old single-region path code paths cleaned | n/a | n/a | Phase 4 stable for 30 days |

### Cutover gates

- **Phase 1 → 2:** RDS healthchecks green; replication lag <30s for 7 days; `pg_stat_replication` clean
- **Phase 2 → 3:** Smoke test suite passes; manual queries validated; rollback procedure tested in staging
- **Phase 3 stages:** No P1+ incident attributable to multi-region for 7 days; latency targets met at p95
- **Phase 4:** All Phase 3 metrics stable for 30 days; incident-free
- **Phase 5:** Phase 4 stable for 30 days

### Rollback strategy (per phase)

| Phase | Rollback approach |
|-------|-------------------|
| 1 | Tear down EU infra; no impact |
| 2 | Same |
| 3 | Flip `eu_read_pct` flag back; EU traffic returns to US (latency degradation but available) |
| 4 | Flip `eu_write_proxy` flag back; EU writes go through US directly (current behavior) |
| 5 | Code cleanup; difficult to roll back; forward-fix preferred |

---

## 11. Risks & Mitigations

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| RP-01 | Logical replication doesn't support our LARGE OBJECTS in `documents` table | M | H | Spike WP-0.G in Phase 0 to verify; fallback: dump/restore for `documents` separately |
| RP-02 | Replication lag spikes during high-traffic events | M | M | Monitoring + alert; if sustained >2 min, auto-flip EU reads back to US |
| RP-03 | EU write proxy adds latency unacceptable to users | L | M | Measure during Phase 4 ramp; if user feedback negative, tune or escalate to Active-Active reconsideration |
| RP-04 | Compliance disputes "EU residency" claim | L | H | Pre-engagement with Compliance + DPA review BEFORE Phase 1 |
| RP-05 | Postgres EOL on current version forces upgrade mid-project | M | M | Upgrade to Postgres 16 in Phase 0 BEFORE replication setup |

## 12. Notes

- **Architecture mode:** A — Standard pattern (Active-Passive multi-region; chosen from 3 candidates)
- **Inputs read:** SRS ✅, CODEBASE_MAP ✅, DATA_ARCHITECTURE ✅ (R-04 risk acknowledged), TECH_DEBT_AUDIT ✅, BUSINESS_CONTEXT ✅, FEASIBILITY ✅ (Partial scenario)
- **Time spent:** 16 hours over 1 week
- **Confidence:** Medium-High (proven pattern; team familiar; OQs are spike-able)

## 13. Open Questions

| ID | Question | Next step |
|----|----------|-----------|
| OQ-1 | Logical replication compatible with `documents.large_object` columns? | Spike WP-0.G |
| OQ-2 | Compliance signs off on "EU residency = read replica" interpretation? | Pre-Phase-1 review |
| OQ-3 | Cost projection for cross-region S3 transfer (documents) — Year 1 vs Year 2? | DevOps spike |
| OQ-4 | RDS instance size for EU replica — same as US or smaller? | Capacity planning |

## 14. Next Steps

1. ADR review with Tech Lead, DBA, Compliance Lead by 2026-06-15
2. Spike OQ-1 (RP-01 mitigation) before approving for implementation
3. Pre-Phase-1 Compliance review (OQ-2)
4. Pass approved design to `implementation-planning` skill → produces 14-week WP plan
```

---

## Calibration notes

- **3 candidates, not 1.** Even though Active-Passive was the obvious fit, exploring Active-Active and Hybrid forces explicit reasoning. ADR cites why each was rejected.
- **Comparison matrix uses real requirements.** "Score: 9/11 ✅" not "feels right". Each cell traces to a specific FR/NFR.
- **ADR Consequences (negative — accepted) is critical.** Lists the costs honestly (EU writes 120ms; data residency interpretation; Year 2 reconsideration). No surprises later.
- **Component anti-scope explicit.** "API Gateway does NOT do auth or business logic" — stops scope creep into wrong layer.
- **Phasing has cutover criteria, not just dates.** "Cutover when replication lag <30s for 7 days" — measurable, not opinion.
- **Open Questions feed into Phase 0 spikes.** OQ-1 became WP-0.G (logical replication compatibility spike). Plan can absorb 1-2 spike WPs without wholesale change.
- **Revisit conditions in ADR.** Architecture decisions aren't permanent; ADR specifies when to re-evaluate.
