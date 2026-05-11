# Feature Extension Planning — Worked Example

Anonymized. Fictional feature: **"Bulk export"** added to an existing CRM product.

## Context

**Imagined input:** "Add bulk export to our Customers feature. Pro tier only. Top customer requested. SOC2 compliance — audit log every export."

**Mode:** A.

---

## Output excerpt

```markdown
# FEAT-042 — Bulk Customer Export

> Project: Atrium CRM
> Author: Backend Lead
> Date: 2026-10-15
> Status: Approved
> Effort estimate: M (~2 days)
> Target release: v3.4 (2026-11-01)

## 1. What & Why

### What
Pro-tier users can export their entire Customer list as CSV or JSON. Export runs as
a background job; user gets email when ready (signed S3 URL, 24h expiry).

### Who uses it
- Pro tier users (per FR-AUTH tier check)
- Admin users (audit log access)

### Why
- Top customer (CompanyX) requested this for their analytics workflow ($240K ARR — sales gating)
- Competitive parity: Competitor Y has had this for 6 months
- SOC2 audit will look at "data portability" controls

### Success measure
30%+ of Pro users use bulk export at least once in first 90 days.

## 2. Mode & Scope

**Mode:** A — Standard

### In scope
- Customers entity export only (this v1)
- CSV + JSON formats
- Email notification on completion
- Audit log of every export

### Out of scope (explicit)
- Other entities (Deals, Activity Feed) — future feature
- Excel format (CSV opens in Excel; native xlsx deferred)
- Recurring scheduled exports — future
- Export to Google Drive / Dropbox — future
- Imports — separate feature

## 3. SRS Alignment

### Maps to existing FRs

| Existing FR | Relationship | Change |
|-------------|--------------|--------|
| FR-CUST-02 (List Customers) | Related — uses same query basis | None |
| FR-AUTH-04 (Pro tier check) | Required — gates this feature | None |

### New FRs to add

| New FR | Statement | Domain | Priority |
|--------|-----------|--------|----------|
| FR-EXP-01 | Pro tier user shall request a Customer export via UI button | M5 (new submodule) | Must |
| FR-EXP-02 | System shall enqueue export job; user receives email with download link when ready | M5 | Must |
| FR-EXP-03 | Download link is signed S3 URL; expires in 24 hours; one-time use | M5 | Must |
| FR-EXP-04 | Every export logged in audit_log table (actor, count, format, timestamp) | M7 (Audit module) | Must |

(FRs to be added to SRS via `srs-greenfield-author` skill or manual edit; cross-link RTM.)

### NFR considerations

- **Performance:** Export job up to ~10K customers should complete in <5 min p95. Don't block API thread.
- **Security:** Signed URL prevents unauthorized download; one-time use prevents replay.
- **Compliance:** SOC2 CC7.2 — audit log of mutations + privileged ops. Export = privileged op (data egress).
- **Reliability:** Background job retry on failure; max 3 retries.

## 4. Design

### User flow

```
1. Pro user navigates to Customers list
2. Clicks "Export" button (visible only for Pro tier)
3. Selects format (CSV or JSON)
4. Confirms; job enqueued; UI shows "Export in progress; we'll email you"
5. (5-300 seconds later) Email arrives with download link
6. User clicks link → downloads file
7. Link expires after 24h or first download
```

### Data

| Entity | Action | Notes |
|--------|--------|-------|
| `customer_exports` | NEW table | tracks export jobs (id, user_id, status, format, count, s3_key, created_at, downloaded_at, expires_at) |
| `audit_log` | INSERT | one row per export request |

### API surface

| Endpoint | Method | Purpose | Auth |
|----------|--------|---------|------|
| POST /api/v1/exports/customers | POST | Create export job | Pro tier session |
| GET /api/v1/exports/:id | GET | Check status | Owner only |
| GET /api/v1/exports/:id/download | GET | Redirect to signed S3 URL | Owner only; one-time |

### UI changes

- New "Export" button on Customers page (Pro tier only)
- Modal for format selection (CSV / JSON)
- "Exports in Progress" notification badge (count of active jobs)
- Email template for completion

### Integration

- **Touched components:** Customers service (read), Email service (send), S3 (write), Audit log (write)
- **Background job:** new BullMQ queue `customer-export`
- **External services:** SendGrid (email), S3 (storage)

## 5. Schema Changes

### Migrations

| Migration | Type | Description | Reversible |
|-----------|------|-------------|------------|
| 20261015_create_customer_exports_table.sql | CREATE | New table for export jobs | Yes (DROP TABLE; OK because table is new) |

### Migration risks

- Additive migration; low risk
- Online (no downtime)

## 6. Rollout Plan

### Feature flag

- **Name:** `enable_customer_export`
- **Default state:** false
- **Audience targeting:** internal users → 5% Pro → 25% → 100%
- **Kill switch:** flag → false; existing in-progress jobs complete; UI hides export button

### Gradual rollout

| Stage | % | Duration | Cutover criterion |
|-------|---|----------|--------------------|
| Internal beta | 0% public; all staff | 1 week | No P1+ issues; staff feedback positive |
| 5% Pro | 5% Pro tier (random) | 1 week | Error rate < 0.5% on export endpoints |
| 25% Pro | 25% Pro tier | 1 week | Same; no support escalations |
| 100% Pro | All Pro tier | (release) | Success metric trending; CompanyX confirms working |

### Backward compatibility

- No breaking changes; new endpoint, new UI element
- Existing API consumers unaffected

### Customer communication

- **Changelog entry:** "New: Pro users can now export their Customer list as CSV or JSON"
- **Help docs:** New article "How to export your customers"
- **In-product announcement:** Banner shown to Pro users (dismissible)
- **CompanyX direct outreach:** Account manager confirms feature meets their need

## 7. Test Plan

### Unit tests

- `CustomerExportService.create` validates Pro tier — `tests/unit/services/exports.test.ts`
- `CustomerExportService.list` filters by user — `tests/unit/services/exports.test.ts`
- Audit log written on export — `tests/unit/services/exports.test.ts`
- Signed URL expiry logic — `tests/unit/services/s3.test.ts`

### Integration tests

- End-to-end: POST /exports → poll status → download — `tests/integration/exports.spec.ts`
- Auth: free tier user gets 403 — `tests/integration/exports-auth.spec.ts`
- Cross-user: user A cannot access user B's export — `tests/integration/exports-auth.spec.ts`

### Manual TCs

- TC-FEAT-042-01: Pro user creates export with 50 customers; receives email within 60s; downloads CSV; opens in Excel
- TC-FEAT-042-02: Pro user creates export with 5K customers; receives email within 5min; downloads JSON; valid JSON
- TC-FEAT-042-03: Free tier user attempts export → button not visible
- TC-FEAT-042-04: Pro user A creates export; user B logs in and tries to access A's export ID → 403
- TC-FEAT-042-05: Download link clicked twice → second click 410 Gone
- TC-FEAT-042-06: Export expires; user attempts download after 24h → 410 Gone
- TC-FEAT-042-07: Audit log shows entry per export with actor + count + format

### Performance test

- Run `tests/perf/export-load.js` simulating 10 concurrent exports of 5K customers
- Target: p95 export job completion < 5 min
- Target: API thread not blocked (POST /exports returns < 200ms)

### Security test

- Cross-user authz test (in integration tests)
- Signed URL signature validation (cannot tamper)

## 8. Risks & Mitigations

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| FR-01 | Export job uses too much memory for large customer lists | M | M | Stream CSV/JSON; cap export size at 100K rows; reject larger with error |
| FR-02 | User exports PII; GDPR concern | L | H | Audit log every export; consent already established (TOS); Pro tier limited |
| FR-03 | Signed URL leaks; data accessible | L | M | One-time use; 24h expiry; URL not indexable; HTTPS-only |
| FR-04 | Background queue backlog under load | M | L | Per-tenant rate limit (max 5 exports per hour) |

## 9. Rollback Plan

If feature breaks production:

```
1. Disable flag: `./scripts/flag-set.sh enable_customer_export false`
2. Verify flag off via synthetic check (button hidden)
3. In-progress jobs: complete or fail naturally (no harm)
4. Customer comm: changelog entry adjusted; no need for incident comms (feature off → invisible)
5. If schema issue: reverse migration (DROP TABLE customer_exports)
6. Address root cause; re-flag and gradual re-rollout
```

## 10. Implementation Plan

### Approach
Multi-WP (medium feature, ~2 days work).

### WP outline

| WP | Description | Effort |
|----|-------------|--------|
| WP-FEAT-042-A | Schema migration + base CustomerExport service | S (4h) |
| WP-FEAT-042-B | API endpoints + auth checks + audit log | M (1d) |
| WP-FEAT-042-C | BullMQ background job + S3 upload + signed URL | S (4h) |
| WP-FEAT-042-D | Email template + SendGrid integration | XS (2h) |
| WP-FEAT-042-E | UI: button, modal, status indicator | S (4h) |
| WP-FEAT-042-F | Tests + flag wiring + manual TC documentation | S (4h) |

### Dependencies
- BullMQ already in use for other jobs (no new infra needed)
- SendGrid template system already in use
- S3 bucket exists (will create new prefix `exports/{user_id}/`)

## 11. Compliance / Privacy Review

- **Data classification:** Customer records contain PII (name, email, possibly phone, address)
- **Lawful basis (GDPR):** Contract performance (export of customer's own data they manage)
- **Audit log entries:** YES — every export creates audit_log row (actor, action, target, count, timestamp)
- **Data retention:** Export files in S3 expire after 24 hours; audit_log retained per CON-REG-04 (90 days)
- **Reviewer sign-off:** Compliance Lead (signed 2026-10-18); Security Lead (signed 2026-10-18)

## 12. Open Questions

| ID | Question | Owner | Target |
|----|----------|-------|--------|
| OQ-1 | Should free tier users see "Export — Upgrade to Pro" CTA? | Product | 2026-10-20 |
| OQ-2 | Email subject line "Your Customer export is ready" — A/B test? | Marketing | 2026-10-22 |

## 13. Decision Log

| Date | Decision | Rationale | Owner |
|------|----------|-----------|-------|
| 2026-10-15 | Use signed S3 URL vs. proxy download | Reduces server load; standard pattern | Backend Lead |
| 2026-10-15 | Single format choice per export (not "all formats") | Simpler v1; multi-format can come later | Product |
| 2026-10-16 | Cap at 100K customers per export | Performance; >100K customers is rare; segment-and-export pattern OK for power users | Backend Lead |
| 2026-10-17 | 24-hour expiry on download URL | Long enough for users; short enough for security | Security Lead |

## 14. Sign-off

| Role | Name | Status | Date |
|------|------|--------|------|
| Product | Sarah K. | Approved | 2026-10-17 |
| Engineering Lead | Mike J. | Approved | 2026-10-17 |
| QA Lead | Tina P. | Approved | 2026-10-18 |
| Compliance | Diana L. | Approved | 2026-10-18 |
| Security | Ravi S. | Approved | 2026-10-18 |
```

---

## Calibration notes

- **Status was Draft → Reviewed → Approved over 3 days.** Realistic timeline; not "approved instantly".
- **Out-of-scope explicit.** Lists 5 things this v1 does NOT do — prevents scope creep mid-implementation.
- **New FRs proposed with IDs.** SRS gets updated as part of this feature; traceability maintained.
- **NFR considerations specific.** "Export job <5 min p95"; "Don't block API thread" — testable.
- **Flag with kill switch.** No deploy without rollback path.
- **Compliance review thorough.** Section 11 cites lawful basis (GDPR Article 6(1)(b)), audit log, retention. Two reviewers signed.
- **Decision log preserves "why".** Signed URL vs proxy: future engineer asking "why this way?" can find answer.
- **Effort decomposed into 6 WPs.** Each is single-PR scope (matches `implementation-planning` standard).
