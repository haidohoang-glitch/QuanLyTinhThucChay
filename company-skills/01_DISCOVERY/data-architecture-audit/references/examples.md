# Data Architecture Audit — Worked Example

Anonymized. Fictional project: **"Project Helix"** — a healthcare records aggregator for outpatient clinics. Use to calibrate output style, not to copy.

## Context

**Imagined input:** "Audit Helix's data architecture before we sign the SOC2 engagement."

**Time budget:** 6 hours.

**Mode chosen:** Mode A (codebase has no declared data architecture doc).

---

## Generated output (excerpt)

```markdown
# Project Helix — Data Architecture Audit

> Generated using: data-architecture-audit skill v1
> Last updated: 2026-04-12
> Reviewer: TBD

## 1. Executive Summary

Project Helix aggregates patient records from 200+ outpatient clinics into a central
Postgres store, with daily warehouse sync for analytics. Five storage layers in active
use: 1 primary DB (Postgres on RDS), 1 cache tier (Redis), 1 warehouse (BigQuery via
Fivetran), 1 object store (S3 for documents/scans), 1 third-party (Auth0). Major concerns
are HIPAA-related: Patient name + SSN appears in logs; Auth0 PII export not exercised
in past 12 months; backups exist but restore drill never run.

**Top 3 risks:**
1. **R-01** PHI leaks into application logs (Datadog) — P0
2. **R-02** No tested DR procedure — P1
3. **R-03** Patient deletion does not cascade to BigQuery analytics layer — P1

## 2. Storage Layer Map

| Layer | Store | Purpose | Tech | Owner |
|-------|-------|---------|------|-------|
| L2 | Browser localStorage | UI prefs, draft notes | localStorage | Frontend |
| L3 | Cache (sessions, query results) | Reduce DB load | Redis 7 (ElastiCache) | Backend |
| L4 | Primary records | Source of truth | Postgres 15 (RDS) | Backend |
| L4 | Auth records | Identity, sessions | Auth0 (third-party) | Auth0 |
| L5 | Warehouse | Reporting, analytics | BigQuery (via Fivetran) | Data team |
| L6 | Document store | Lab PDFs, scans | S3 (us-east-1) | Backend |
| L7 | RDS automated backups | DR, PITR window | RDS snapshots | DevOps |

```
                     ┌──────────────────┐
   Browser  ─────►   │  Express API     │
   (localStorage L2) │  (Node 18)       │
                     └────┬─────────────┘
                          │ writes
              ┌───────────┼────────────┐
              ▼           ▼            ▼
          [Auth0 L4]  [Postgres L4] [S3 L6]
                          │  (CDC)
                          ▼
                   [BigQuery L5] (daily Fivetran sync)
                          
              [Redis L3] sits in front of Postgres reads
              [RDS Snapshots L7] = automated backups
```

## 3. Schema Inventory (Primary Stores)

### Store: Postgres `helix_prod`

| Table | Purpose | Row count | Key columns | Sensitive fields |
|-------|---------|-----------|-------------|------------------|
| `patients` | Patient master records | ~2.8M | `id` (PK), `clinic_id` (FK) | `first_name`, `last_name`, `dob`, `ssn_encrypted`, `email` |
| `appointments` | Visit records | ~14M | `id`, `patient_id` (FK), `clinic_id`, `provider_id` | `notes` (free text — may contain PHI) |
| `lab_results` | Lab orders + results | ~9M | `id`, `appointment_id`, `lab_test_code` | `result_value`, `pdf_s3_key` |
| `clinics` | Tenant table | 207 | `id` (PK), `slug` | `address`, `phone` |
| `users` | Clinic staff | ~3.5K | `id`, `clinic_id`, `auth0_sub` | `email`, `phone` |
| `audit_log` | Mutations | ~190M (90 days retention) | `id`, `actor_id`, `action`, `entity` | (depends on entity) |

### Schemas not documented

- Redis: keys named `session:*`, `query:*`, `tenant:*`. No declared schema; inferred from grep. → OQ-1.
- S3: object prefix structure `{clinic_id}/{patient_id}/{document_id}.pdf`. No documentation. → OQ-2.

## 4. Data Flow

### Patient (record creation)

**Write path:**
```
Clinic UI → POST /api/patients → Express validate (Zod)
        → INSERT patients (Postgres, txn)
        → CACHE INVALIDATE redis (key: tenant:{clinic_id}:patients)
        → Fivetran picks up via CDC within 24h → BigQuery
```

**Read path:**
```
GET /api/patients/:id → Redis lookup (TTL 300s)
                     → cache miss → SELECT from Postgres → cache populate
```

**Sync mechanism:** Postgres → BigQuery via Fivetran (logical replication, daily).
**Transaction boundary:** patients + initial appointment INSERT in same txn.
**Failure mode if Postgres down:** API returns 503; UI shows "system maintenance"; no fallback to Redis (Redis only holds reads).

### Lab result (with PDF)

**Write path:**
```
Lab webhook → POST /webhooks/lab-vendor → S3 PUT (PDF)
           → INSERT lab_results (PDF S3 key, NOT content)
           → notify patient via SendGrid
```

**Failure mode if S3 down:** webhook retries 3x; if still failing, marked `pending_upload=true`, polled by cron.

[... more entities omitted for brevity ...]

## 5. Quotas, Usage, Costs

| Store | Plan | Limit | Current | At 10x | Cost (now → 10x) |
|-------|------|-------|---------|--------|-------------------|
| Postgres (RDS db.r6g.xlarge) | Provisioned | 50K IOPS | ~6K avg | ~60K (at limit) | $850/mo → $4500/mo |
| Redis (ElastiCache cache.r6g.large) | Provisioned | 13 GB | 4 GB | 40 GB → upsize | $230/mo → $900/mo |
| BigQuery | On-demand | 1 PB/mo scan | ~3 TB/mo | 30 TB/mo | $15/mo → $150/mo |
| S3 | Pay-as-you-go | unlimited | 1.4 TB | 14 TB | $32/mo → $322/mo |
| Auth0 | B2B Essentials | 10K MAU | ~3.5K (staff only) | ~35K (NEED ENT TIER) | $240/mo → $1200+/mo |
| Total | | | | | $1367/mo → $7000+/mo |

### Bottleneck analysis

**First to break:** Postgres IOPS at 10x scale. Recommend partitioning + read replicas.
**Auth0 plan tier flip:** at 10K MAU, must move to Enterprise (~5x cost).

## 6. Governance Audit

| Concern | Status | Evidence | Gap |
|---------|--------|----------|-----|
| PII inventory | ⚠️ Partial | `audit/pii-fields.md` exists but last updated 2024 | New fields added since (e.g., `phone_secondary`) not tagged |
| GDPR right-to-export | ❌ Missing | No code path found | No `/api/users/me/export` endpoint |
| GDPR right-to-delete | ⚠️ Partial | `users.deleted_at` works in Postgres | Does not cascade to BigQuery (R-03) or S3 documents |
| Retention policy | ⚠️ Partial | `audit_log` has 90d retention via cron | `appointments.notes` retained forever; no policy for S3 |
| Audit trail | ✅ Documented | `audit_log` table with triggers on critical tables | Triggers missing from `lab_results` |
| Encryption at rest | ✅ All stores | RDS+ElastiCache+S3 all KMS-encrypted | Auth0 — managed by vendor (BAA in place) |
| Encryption in transit | ✅ All stores | TLS enforced; verified via security group rules | None |
| Access control / RLS | ⚠️ Partial | App-layer tenant filtering | Postgres RLS not enabled; raw DB access bypasses tenant isolation |
| Backup & DR | ⚠️ Partial | RDS automated PITR (7 day window) | Restore never tested; no RTO/RPO documented |

### PII / PHI field map

| Field | Stored in | At rest? | In transit? | In backups? | Tagged? |
|-------|-----------|----------|-------------|-------------|---------|
| `patients.first_name` | Postgres | Y (KMS) | Y (TLS) | Y | ✅ |
| `patients.ssn_encrypted` | Postgres | Y (app-layer + KMS) | Y | Y | ✅ |
| `patients.email` | Postgres | Y | Y | Y | ✅ |
| `appointments.notes` | Postgres | Y | Y | Y | ⚠️ Not tagged but contains PHI |
| `lab_results.pdf_s3_key` | Postgres + S3 | Y | Y | Y (S3 versioning ON) | ⚠️ S3 versioning = old PHI never deleted |
| Application logs (Datadog) | Datadog | Y | Y | Y (90 days) | ❌ Patient names in error stack traces (R-01) |

## 7. Risk Findings

| ID | Risk | Severity | Layer | Evidence | Next step |
|----|------|----------|-------|----------|-----------|
| R-01 | PHI in application logs (Datadog) — patient names appear in error stack traces from `appointments` controller | **P0** | Cross-cutting | `grep "patient_name" datadog/last_24h` returns 1200+ events | Implement log sanitizer middleware; rotate any exported logs |
| R-02 | DR restore never tested; no RTO/RPO defined | **P1** | L7 | `runbooks/dr.md` is a stub | Schedule restore drill; document RTO/RPO in DPA |
| R-03 | Patient delete does not cascade to BigQuery; old PHI persists in analytics | **P1** | L5 | Tested manually: deleted patient, BigQuery row remains | Add Fivetran custom transform to delete; or schedule purge cron |
| R-04 | Postgres RLS not enabled; SQL Console users see all tenants | **P1** | L4 | `pg_policies` query returns empty | Enable RLS, define per-tenant policies, audit Console access |
| R-05 | S3 versioning ON without lifecycle = old PHI undeletable | **P1** | L6 | S3 console shows 1.8x storage cost from prior versions | Define lifecycle to expire prior versions after retention period |
| R-06 | `appointments.notes` retained indefinitely | **P2** | L4 | No retention job for this column | Define clinical record retention per state law (varies) |
| R-07 | `audit_log` triggers missing from `lab_results` | **P2** | L4 | DDL inspection | Add triggers; backfill is unnecessary (forward only) |
| R-08 | Auth0 right-to-export workflow not documented or exercised | **P2** | L4 (third-party) | No runbook found | Document; exercise quarterly |

## 8. Open Questions

| ID | Question | Where | Next step |
|----|----------|-------|-----------|
| OQ-1 | Redis key conventions undocumented (sessions, queries, tenants) | grep across `cache.ts` | Interview backend lead |
| OQ-2 | S3 prefix structure undocumented | bucket inspection | Document in `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` after audit |
| OQ-3 | BigQuery dataset access — who has BQ console access? | needs IAM review | Run `gcloud projects get-iam-policy` |
| OQ-4 | Fivetran tenant isolation — does the Fivetran connector replicate ALL tenants together? | Fivetran config | Review connector schema mapping |

## 9. Notes & Caveats

- **Classification mode:** A — Standard layered model.
- **Mode rationale:** Codebase has no declared data architecture doc. Standard 8-layer model fits.
- **Audit scope:** Read schema definitions, verified env files, sampled queries against staging clone. NOT done: live performance test, security pen test, restore drill.
- **Time spent:** 6 hours.
- **Confidence:** Medium-High. Open Questions are genuine unknowns.
- **Known gaps:** Did not audit Auth0 internals (vendor scope). Did not measure exact cost at 10x — projection extrapolated from current.
```

---

## Calibration notes

- **Severity discipline.** R-01 is P0 because PHI in logs is an active HIPAA violation. R-02 is P1 (latent risk, will become P0 during an incident). Don't inflate to P0 to drive urgency.
- **Evidence is mandatory.** Every R-XX has a file/query/runbook reference. "Best practice" is not evidence.
- **Mode A fits even regulated industries.** HIPAA-specific checks layer on top of whichever mode — they're cross-cutting, not a separate Mode D.
- **Cost projection is approximate.** Use current real cost × scaling factor; do not invent precise numbers. If unknown, write "Unknown — needs measurement".
