# Requirements Traceability — Worked Example

Anonymized. Continuing **"Project Atrium"** from `srs-greenfield-author` and `nfr-specification` examples. Mode A.

## Context

**Imagined input:** "Build initial RTM for Atrium. SRS exists (47 FRs, 31 NFRs). Implementation has begun (Phase 0 + 1 of plan complete; ~30 of 47 FRs implemented). Pre-launch — preparing for SOC2 Type I audit."

**Time budget:** 6 hours.

**RTM scope:** All 47 FRs + 31 NFRs = 78 RTM rows.

---

## M10 RTM excerpt

```markdown
## 10.1 Requirements Traceability Matrix (RTM)

**Mode used:** A — Standard 4-tier (Req → Design → Code → Test)
**Mode rationale:** Default; no SOC2-specific RTM template required at Type I (Type II audit may add columns later).

**RTM scope:** All 47 FRs + 31 NFRs = 78 rows.
**Source SRS commit:** `9b2a1f4` (date: 2026-08-15)
**Source codebase commit:** `7c3d2e9` (date: 2026-08-22)
**Last test run:** 2026-08-22 (CI run #2847, branch `main`)

### 10.1.0 Functional Requirements (excerpt — first 8 of 47 rows)

| Req ID | Title | Design | Code | Test | Status | Last verified | Notes |
|--------|-------|--------|------|------|--------|---------------|-------|
| FR-AUTH-01 | User Registration | M2.1; ADR-001 (auth approach) | `src/server/services/auth/signup.ts:1-67`; `src/server/routes/auth.ts:14-32` | TC-AUTH-01..05; `auth.spec.ts → 'signup with valid credentials'`, 4 more | PASS | 2026-08-22 | |
| FR-AUTH-02 | Login | ADR-001 | `src/server/services/auth/login.ts:1-58`; `src/server/middleware/session.ts` | TC-AUTH-07..14; `auth.spec.ts → 'login'` (8 cases) | PASS | 2026-08-22 | All TCs pass; lockout test added 2026-08-15 |
| FR-AUTH-03 | Password Reset | ADR-001 | `src/server/services/auth/reset.ts:1-89`; `src/server/services/email/templates/reset.ts` | TC-AUTH-15..19; `auth.spec.ts → 'reset'` | **FAIL** | 2026-08-22 | TC-AUTH-17 fails: rate limit not enforced — see ISS-21 |
| FR-AUTH-04 | Logout | ADR-001 | `src/server/services/auth/logout.ts:1-22` | TC-AUTH-20; `auth.spec.ts → 'logout'` | PASS | 2026-08-22 | |
| FR-AUTH-05 | Email Verification | ADR-001 | `src/server/services/auth/verify.ts:1-51` | TC-AUTH-21..23 | PASS | 2026-08-22 | |
| FR-CUST-01 | Create Customer | M2.1 | `src/server/services/customers/create.ts:1-43`; `src/server/routes/customers.ts:8-22` | TC-CUST-01..03; `customers.spec.ts → 'create'` | PASS | 2026-08-22 | |
| FR-CUST-02 | List Customers | M2.1 | `src/server/services/customers/list.ts:1-38`; `src/server/routes/customers.ts:24-32` | TC-CUST-04; `customers.spec.ts → 'list with pagination'` | PASS | 2026-08-22 | |
| FR-CUST-03 | Update Customer | M2.1 | `src/server/services/customers/update.ts:1-55` | TC-CUST-05..07; `customers.spec.ts → 'update'` (3 cases) | PASS | 2026-08-22 | |
| FR-CUST-04 | Delete Customer | M2.1 | `src/server/services/customers/delete.ts:1-34` | TC-CUST-08 | **NOT RUN** | 2026-08-15 | Test exists but skipped due to fixture issue — see ISS-22 |
| ... (38 more FR rows) | | | | | | | |
| FR-INV-04 | Send Invoice via Email | ADR-003 (email infra) | `src/server/services/invoices/send.ts:1-92`; `src/server/services/email/send.ts` | TC-INV-04..06; `invoices.spec.ts → 'send'` | PASS | 2026-08-22 | |
| FR-PAY-01 | Stripe Checkout Link | ADR-002 (Stripe integration) | `src/server/services/payments/createCheckout.ts` | TC-PAY-01..03; `payments.spec.ts → 'checkout link'` | PASS | 2026-08-22 | |
| FR-PAY-02 | Webhook (payment_intent.succeeded) | ADR-002 | `src/server/webhooks/stripe.ts:1-67` | TC-PAY-04..06; `payments.spec.ts → 'webhook'`; smoke test against Stripe sandbox | PASS | 2026-08-22 | Manual sandbox test critical; webhook signature verified |
| FR-PAY-03 | Refund | ADR-002 | **NOT IMPLEMENTED** (Phase 2 target) | TC-PAY-07..08 (drafted) | NOT IMPLEMENTED | n/a | Planned: Phase 2 WP-2.D |
| FR-PAY-04 | Manual Payment Recording | M2.1 | **NOT IMPLEMENTED** (Phase 2 target) | TC-PAY-09 (drafted) | NOT IMPLEMENTED | n/a | Planned: Phase 2 WP-2.E |
| ... | | | | | | | |

### 10.1.1 Non-Functional Requirements (excerpt — 6 of 31 rows)

| NFR ID | Title | Verification method | Verification artifact | Status (target met?) | Last verified |
|--------|-------|----------------------|------------------------|----------------------|---------------|
| NFR-PERF-01 | API GET p95 ≤ 500ms | k6 load test at 50 req/s | `tests/perf/api_get.js` (run 2026-08-20) | PASS (p95 = 320ms; target ≤ 500ms) | 2026-08-20 |
| NFR-PERF-02 | API write p95 ≤ 1000ms | k6 load test at 20 req/s | `tests/perf/api_write.js` | PASS (p95 = 740ms) | 2026-08-20 |
| NFR-PERF-03 | Email delivery p95 ≤ 60s | Synthetic monitor | Datadog synthetic test "email-delivery-check" | PASS (p95 = 28s over 7 days) | 2026-08-22 |
| NFR-SEC-01 | Auth method (NIST 800-63B Level 1) | Code review + pen test | `audit/2026-Q3-pen-test-report.pdf` (page 12) | PASS | 2026-08-15 |
| NFR-SEC-02 | Encryption at rest (AES-256-GCM) | Configuration audit | RDS console screenshot + KMS audit log | PASS | 2026-08-10 |
| NFR-SEC-03 | TLS 1.3 in transit | SSL Labs scan | Scan result A+ on https://atrium.app, dated 2026-08-12 | PASS | 2026-08-12 |
| NFR-SEC-08 | Incident response detection ≤ 30 min | Tabletop exercise | (pending — drill scheduled 2026-09-15) | **NOT VERIFIED** | n/a |
| NFR-REL-01 | Uptime ≥ 99.9% | External monitor | Pingdom report Aug 2026 | NOT VERIFIED (insufficient history; 22 days uptime data) | 2026-08-22 |
| NFR-REL-02 | RTO ≤ 8 hours | DR drill | (pending — pre-launch drill scheduled 2026-09-30) | **NOT VERIFIED** | n/a |
| NFR-COMP-01 | SOC2 Type I (Year 1) | External audit | (audit scheduled 2027-Q1) | **NOT VERIFIED** (target Year 1) | n/a |
| NFR-COMP-04 | PCI-DSS SAQ-A scope | Self-assessment + code review | `audit/2026-saq-a-self-assessment.pdf`; code review confirmed no card data on Atrium servers | PASS | 2026-08-18 |
| ... | | | | | | |

### 10.1.2 Coverage Statistics

| Metric | Count | % of total |
|--------|-------|------------|
| **Functional Requirements (47 total)** | | |
| FRs with design linked | 47 | 100% |
| FRs with code linked | 31 | 66% |
| FRs with test linked (manual or automated) | 47 | 100% (TCs drafted for all) |
| FRs with passing automated test | 28 | 60% |
| FRs with failing test | 1 | 2% (FR-AUTH-03) |
| FRs not yet implemented (planned) | 16 | 34% |
| **Non-Functional Requirements (31 total)** | | |
| NFRs with verification method documented | 31 | 100% |
| NFRs with verification artifact present | 18 | 58% |
| NFRs currently meeting target | 16 | 52% |
| NFRs not yet verified (pending audit/drill/launch) | 13 | 42% |
| **Orphans** | | |
| Orphan code paths (no Req linked) | 12 | (info only) |
| Orphan tests (no Req linked) | 5 | (info only) |

### 10.1.3 Findings

#### Orphan requirements (no test or no code)

| Req ID | Issue | Severity | Recommended action |
|--------|-------|----------|---------------------|
| FR-AUTH-03 | TC-AUTH-17 (rate limit) fails | High (security-relevant) | Backend lead: implement rate limit in reset.ts; ETA 2026-09-05 |
| FR-CUST-04 | TC-CUST-08 not running (skipped due to fixture issue) | High | QA lead: fix fixture; re-run; ETA 2026-08-30 |
| FR-PAY-03 | Not implemented | Expected (Phase 2 target) | Per plan; no action |
| FR-PAY-04 | Not implemented | Expected (Phase 2 target) | Per plan; no action |
| ... (12 more "not implemented yet" entries — all expected per implementation plan) |
| NFR-SEC-08 | IR plan does not exist | Medium | Eng lead: draft IR plan + tabletop drill; ETA 2026-09-15 |
| NFR-REL-02 | DR drill not yet executed | Medium | DevOps: pre-launch drill; ETA 2026-09-30 |
| NFR-COMP-01 | SOC2 audit Year 1 target | Expected | Per plan; engagement starts 2027-Q1 |

#### Orphan code (12 paths)

| Code path | Likely category | Action |
|-----------|-----------------|--------|
| `src/utils/dateFormat.ts` | Utility | Acceptable — no Req expected |
| `src/utils/currency.ts` | Utility | Acceptable |
| `src/server/middleware/correlationId.ts` | Infrastructure | Acceptable — internal observability |
| `src/server/middleware/logging.ts` | Infrastructure | Acceptable |
| `src/server/migrations/*.ts` (5 files) | Infrastructure | Acceptable — schema migrations |
| `src/server/scripts/seed.ts` | Operations script | Acceptable |
| `src/server/legacy/oldEmailFormat.ts` | **Stale code?** | Investigate: not in any Req trace; may be dead. Action: confirm with code owner; remove if unused. |
| `src/api/clientLegacy.ts` | **Stale code?** | Investigate: pre-refactor variant; if unused, remove. |

#### Orphan tests (5 tests)

| Test path | Description | Action |
|-----------|-------------|--------|
| `tests/integration/db.fixture.test.ts` | DB fixture validation | Acceptable — infrastructure test |
| `tests/integration/healthcheck.spec.ts` | Health endpoint | Should map to NFR-REL-01; **add Req link** |
| `tests/unit/utils/dateFormat.test.ts` | Utility unit tests | Acceptable |
| `tests/unit/utils/currency.test.ts` | Utility unit tests | Acceptable |
| `tests/unit/legacy/oldEmailFormat.test.ts` | Tests stale code | Remove with stale code (see orphan code action) |

#### Failing tests (current state)

| Req ID | Test | Failure | Owner | Target fix |
|--------|------|---------|-------|------------|
| FR-AUTH-03 | TC-AUTH-17 | Rate limit not enforced | Backend lead | 2026-09-05 |

#### Not-run tests (skipped or stale)

| Req ID | Test | Reason | Action |
|--------|------|--------|--------|
| FR-CUST-04 | TC-CUST-08 | Fixture issue | Fix and re-run |

### 10.1.4 Verification log

This RTM was last validated on 2026-08-22 by QA Lead.

Validation method:
- [x] Random sample of 10 FRs verified — Code links open to correct files; tests exist
- [x] Random sample of 10 NFRs verified — Verification artifacts exist
- [x] Test status verified by re-running CI (run #2847)
- [x] Coverage statistics computed from CI run #2847 data
- [x] 1 stale entry corrected (NFR-PERF-03 last verified date refreshed from synthetic monitor)

### 10.1.5 Maintenance approach

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Update RTM row when PR merges | Per PR | PR author (gated by PR template asking "RTM row updated?") |
| Quarterly accuracy audit (10% sample) | Quarterly | QA Lead |
| Coverage statistics refresh | Weekly via CI | CI (auto-generated to `coverage_stats.json` then merged into RTM) |
| External RTM audit (SOC2-aligned) | Annually | External SOC2 auditor |
| Refresh "Last verified" dates | Monthly (10 random rows) | QA Lead |

---

## 10.2 Open Issues

(Including issues from earlier SRS authoring + new from RTM analysis)

| ID | Issue | Originated | Status | Owner | Target |
|----|-------|------------|--------|-------|--------|
| ISS-01..05 | (preserved from M3-M6 author work) | M3-M6 | (various) | (various) | (various) |
| ISS-21 | TC-AUTH-17 fails: password reset rate limit not enforced (FR-AUTH-03) | M10 RTM | OPEN | Backend lead | 2026-09-05 |
| ISS-22 | TC-CUST-08 fixture issue blocking test run (FR-CUST-04) | M10 RTM | OPEN | QA lead | 2026-08-30 |
| ISS-23 | NFR-SEC-08 IR plan absent | M10 RTM + M9 | OPEN | Engineering lead | 2026-09-15 |
| ISS-24 | NFR-REL-02 DR drill not yet executed | M10 RTM + M9 | OPEN | DevOps | 2026-09-30 |
| ISS-25 | NFR-REL-01 insufficient uptime history for verification | M10 RTM + M9 | OPEN | DevOps | (resolves naturally with time) |
| ISS-26 | Orphan code: `src/server/legacy/oldEmailFormat.ts` likely stale | M10 RTM | OPEN | Backend lead | Investigate by 2026-09-01 |
| ISS-27 | Orphan code: `src/api/clientLegacy.ts` likely stale | M10 RTM | OPEN | Frontend lead | Investigate by 2026-09-01 |
| ISS-28 | Health endpoint test (`tests/integration/healthcheck.spec.ts`) not linked to NFR-REL-01 | M10 RTM | OPEN | QA lead | Update RTM by 2026-08-30 |

---

## 10.3 Appendix

### A. Data Dictionary
(Preserved from SRS author skill — 12 entities)

### B. User Class Privilege Matrix
(Preserved)

### C. State Diagrams
(Preserved)

### D. Glossary (extended)
(Preserved)

### E. RTM Generation Tools

This RTM was authored manually by QA Lead with input from:
- `coverage_stats.json` generated by Vitest with `--coverage` (CI run #2847)
- Code link verification via shell `find` and `grep` commands (no auto-generation tool yet)
- Test status from CI workflow logs

**Future improvement:** automate RTM update via CI script extracting `// @implements FR-XXX-NN` annotations. Drafted as ISS-29 (deferred to post-launch).

### F. RTM Export Formats

For SOC2 audit Year 1:
- PDF export of M10.1.0 + M10.1.1 (RTM tables) saved quarterly to `audit/rtm_YYYY-QQ.pdf`

### G. Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2026-08-22 | QA Lead | Initial RTM populated from SRS v0.4 + codebase commit `7c3d2e9` |

---

## 10.4 Sign-off

(To be completed before SRS v1.0 promotion)

| Role | Name | Approval | Date |
|------|------|----------|------|
| Engineering Lead | | | |
| QA Lead | | | |
| Compliance / Audit | | | |
```

---

## Calibration notes

- **Coverage at 60% passing tests is normal pre-launch.** Atrium has 16 FRs not yet implemented (deliberate — Phase 2 work). The 1 FAIL (FR-AUTH-03) is a real finding, properly tracked as ISS-21.
- **NFR coverage at 58% is honest.** 13 NFRs are pending audit/drill/launch — these resolve naturally with time, not from skill avoidance.
- **Orphan code investigation matters.** 12 orphan code paths surfaced; 10 are acceptable (utility/infra), 2 are likely stale (ISS-26, ISS-27). The skill earned its keep here — these would have been technical debt.
- **Last verified dates honest.** Each row says when trace was last confirmed accurate. Stale dates trigger maintenance. Some NFRs have very recent dates (just verified); others are "n/a" (not yet verifiable).
- **Open Issues consolidated.** RTM authoring added 8 new ISS entries (ISS-21 through 28). Pre-existing ISS-01..05 from SRS author work preserved.
- **Maintenance approach explicit.** 10.1.5 documents who keeps it updated and how. Without this, the RTM rots within 3 months.
- **Coverage stats sanity-check.** 100% of FRs have manual TCs drafted, but only 60% have passing automated tests — the gap is healthy progress through implementation, not a quality issue.
- **Audit-grade evidence.** NFR-PERF-03 cites Datadog synthetic test name + 7-day window. NFR-SEC-02 cites RDS console + KMS audit log. NFR-COMP-04 cites SAQ-A self-assessment PDF. Auditors can verify each claim.
