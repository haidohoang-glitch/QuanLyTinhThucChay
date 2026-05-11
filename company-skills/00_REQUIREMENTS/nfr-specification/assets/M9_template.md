# M9 — Non-Functional Requirements

> **SRS Module 9 of 10** | Project: {{PROJECT_NAME}} | Version: v0.1 (DRAFT) | Date: {{YYYY-MM-DD}}

---

## 9.0 Overview

This module specifies the **non-functional requirements** for {{PROJECT_NAME}}: how well
the system must perform, not what features it provides. Functional requirements are in
M3-M{{X}}.

**Categorization mode:** {{A — ISO/IEC 25010 / B — Honor company taxonomy / C — User-defined}}
**Mode rationale:** {{WHY}}

**Current state assessment date:** {{YYYY-MM-DD}}
**Sources:**
- M2.5 Constraints (`docs/00_REQUIREMENTS/SRS_VI/M2_*.md`)
- M3-M{{X}} Functional Requirements (for cross-reference)
- `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` Section 6 (governance audit)
- {{REGULATORY_DOC, SLA_CONTRACT, BENCHMARK_DOC, etc.}}

**NFR ID conventions:**
- `NFR-PERF-NN` — Performance Efficiency
- `NFR-SEC-NN` — Security
- `NFR-USE-NN` — Usability
- `NFR-REL-NN` — Reliability
- `NFR-MAINT-NN` — Maintainability
- `NFR-PORT-NN` — Portability
- `NFR-COMPAT-NN` — Compatibility
- `NFR-COMP-NN` — Compliance

---

## 9.1 Performance Efficiency

### NFR-PERF-01 — {{TITLE}}

**Statement:** The system shall {{MEASURABLE_PROPERTY}} under {{CONDITION}}.

**Metric:** {{e.g., Response time p95 (server-side), excluding network)}}
**Target:** {{e.g., ≤ 200ms p95; ≤ 500ms p99}}
**Condition:** {{e.g., 100 req/s nominal load; cache warm; ≤10K rows in user data}}
**Current state:** {{MEASURED_VALUE_OR_"Unknown — not measured"}}
**Source:** {{e.g., Customer SLA Pro tier, Contract §4.2}}
**Verification method:** {{e.g., k6 load test in staging at target load; production APM monitoring}}
**Priority:** {{Must / Should / Could}}
**Functional impact:** {{FR-TRX-04, FR-TRX-07}}
**Notes:** {{ANY_CONTEXT}}

---

### NFR-PERF-02 — {{TITLE}}

(repeat structure)

---

(continue for each Performance NFR — typically 3-10)

---

## 9.2 Security

### NFR-SEC-01 — {{TITLE — e.g., Authentication Method}}

**Statement:** {{The system shall require ... for ...}}

**Metric:** {{e.g., Authentication factor count}}
**Target:** {{e.g., 2FA required for Admin role; 1FA acceptable for End-user with password meeting NIST SP 800-63B Level 1}}
**Condition:** {{e.g., All authenticated requests}}
**Current state:** {{e.g., Currently 1FA only — does not meet target}}
**Source:** {{e.g., SOC2 CC6.6 + customer security questionnaire}}
**Verification method:** {{e.g., Security audit; pen test}}
**Priority:** Must
**Functional impact:** {{FR-AUTH-*}}

---

### NFR-SEC-02 — Encryption at Rest

**Statement:** All data classified as PII shall be encrypted at rest using {{ALGORITHM}}.

**Metric:** Encryption algorithm + key management
**Target:** AES-256-GCM with keys managed by {{KMS_PROVIDER}}, customer-managed keys for {{TIER_OR_DATA_TYPE}}
**Condition:** Every storage system holding PII (per data classification)
**Current state:** {{STATE}}
**Source:** {{REGULATION_OR_CONTRACT}}
**Verification method:** Configuration review + audit; penetration test
**Priority:** Must
**Functional impact:** All FRs that read/write PII

---

(continue for: Encryption in Transit, Audit Trail, Vulnerability Management, Incident Response, Session Management, etc. — typically 8-15 Security NFRs)

---

## 9.3 Usability

### NFR-USE-01 — Task Completion Time (New User Signup)

**Statement:** A new user without prior product knowledge shall complete signup in ≤ {{TIME}} measured from landing on signup form to dashboard load.

**Metric:** Median time from form-load to first dashboard render
**Target:** ≤ 3 minutes median; ≤ 5 minutes p95
**Condition:** Standard onboarding flow; no email verification delays included
**Current state:** {{MEASURED_OR_UNKNOWN}}
**Source:** Product team usability target
**Verification method:** Moderated usability test with 5 users; recorded session analytics
**Priority:** Should
**Functional impact:** FR-AUTH-01, FR-{{ONBOARDING_FRS}}

---

### NFR-USE-02 — Accessibility (WCAG)

**Statement:** All user-facing interfaces shall conform to WCAG 2.1 Level AA.

**Metric:** WCAG 2.1 conformance level
**Target:** Level AA (no Level A failures, no Level AA failures detected by axe-core or similar)
**Condition:** All public web pages and authenticated pages
**Current state:** {{STATE}}
**Source:** Accessibility commitment / regulatory (e.g., ADA, EAA in EU)
**Verification method:** Automated axe-core scan in CI; manual audit by accessibility consultant pre-launch
**Priority:** Must
**Functional impact:** All FRs with UI

---

(continue for: Browser support, Mobile responsiveness, Internationalization, Error message clarity, etc.)

---

## 9.4 Reliability

### NFR-REL-01 — Uptime

**Statement:** The system shall achieve at least {{PERCENT}}% uptime measured monthly, excluding planned maintenance windows.

**Metric:** Successful health check %, measured externally (e.g., Pingdom, StatusCake)
**Target:** ≥ 99.9% (max ~43 min downtime/month)
**Condition:** Production environment; planned maintenance announced ≥48h in advance
**Current state:** {{STATE_OR_UNKNOWN}}
**Source:** Customer SLA / industry standard
**Verification method:** External uptime monitor; monthly SLA report
**Priority:** Must
**Functional impact:** All user-facing FRs

---

### NFR-REL-02 — Recovery Time Objective (RTO)

**Statement:** Recovery from regional infrastructure failure shall complete within {{HOURS}} hours.

**Metric:** Time from detection to service restoration
**Target:** ≤ 4 hours
**Condition:** Loss of primary region; secondary region available
**Current state:** {{TESTED_RTO_OR_"Never tested"}}
**Source:** Customer DR commitment
**Verification method:** Quarterly DR drill (`docs/04_MAINTENANCE/runbooks/`)
**Priority:** Must
**Functional impact:** All FRs

---

### NFR-REL-03 — Recovery Point Objective (RPO)

**Statement:** Maximum acceptable data loss shall be {{TIME}}.

**Metric:** Time gap between last successful backup and incident
**Target:** ≤ 1 hour
**Condition:** Standard DR scenario
**Current state:** {{STATE}}
**Source:** Customer DR commitment + data sensitivity
**Verification method:** DR drill; backup automation verification
**Priority:** Must

---

(continue for: Error rate, Mean Time Between Failures, Data integrity, Backup retention, etc.)

---

## 9.5 Maintainability

### NFR-MAINT-01 — Test Coverage

**Statement:** Critical-path code shall maintain ≥ {{PERCENT}}% statement coverage.

**Metric:** Statement coverage from test runner
**Target:** ≥ 80% for `src/server/services/payments/*` and `src/server/middleware/auth.ts`
**Condition:** Per-file coverage as reported by `nyc` or equivalent
**Current state:** {{COVERAGE_REPORT}}
**Source:** Engineering quality standard
**Verification method:** CI coverage report; PR gate enforces threshold
**Priority:** Must

---

(continue for: Build time, Deployment frequency, MTTR, Documentation coverage, etc.)

---

## 9.6 Portability

### NFR-PORT-01 — Cloud Provider Independence

**Statement:** The system shall {{NOT_REQUIRE_VENDOR_LOCK_INS}} for {{COMPONENTS}}.

**Metric:** Vendor-locked dependencies count
**Target:** {{e.g., 0 AWS-specific services for core compute path; managed Postgres acceptable but with documented migration path}}
**Source:** Operational risk policy
**Verification method:** Architecture review; dependency audit
**Priority:** Should

---

(continue for: OS support, Browser compatibility, Database engine flexibility, etc.)

---

## 9.7 Compatibility

### NFR-COMPAT-01 — API Backward Compatibility

**Statement:** Public API shall maintain backward compatibility for {{DURATION}} after a major version release.

**Target:** v3 supports v2 contracts for 12 months post-v3 release; deprecation warnings begin month 6
**Source:** Customer integration commitment
**Verification method:** Contract test against v2 schema in CI; customer notification audit trail
**Priority:** Must

---

## 9.8 Compliance

### NFR-COMP-01 — {{REGULATION_NAME}} (e.g., GDPR Right-to-Export)

**Statement:** Upon request, the system shall provide a data subject's complete personal data within {{DAYS}} days.

**Metric:** Days from request to data delivery
**Target:** ≤ 30 days (per GDPR Art. 12(3))
**Source:** GDPR Article 15 (Right of access) + Article 12 (timeframe)
**Verification method:** End-to-end test of export flow; audit log of requests fulfilled within timeframe
**Priority:** Must
**Functional impact:** FR-{{EXPORT_FR_ID}}

---

### NFR-COMP-02 — {{NEXT_REGULATION_OR_STANDARD}}

(repeat for each compliance obligation)

---

## 9.9 NFR-to-FR Cross-Reference

For traceability, this table maps each NFR to the FRs it constrains.

| NFR ID | Constrains FR(s) |
|--------|------------------|
| NFR-PERF-01 | FR-AUTH-01, FR-AUTH-02 |
| NFR-PERF-03 | FR-TRX-04, FR-TRX-07 |
| NFR-SEC-02 | All FRs reading/writing PII (~30 FRs) |
| NFR-COMP-01 | FR-{{EXPORT_FR_ID}} |
| ... | ... |

---

## 9.10 Constraint-to-NFR Cross-Reference

For traceability, this table shows how M2.5 constraints became NFRs.

| Constraint (M2.5) | Became NFR |
|-------------------|------------|
| CON-REG-01 (PII encrypted) | NFR-SEC-02 |
| CON-OPS-01 (RTO ≤ 4h) | NFR-REL-02 |
| CON-OPS-02 (RPO ≤ 1h) | NFR-REL-03 |
| ... | ... |

---

## 9.11 Open NFR Issues

| ID | Issue | Status | Owner |
|----|-------|--------|-------|
| OQ-NFR-01 | Current performance not measured for NFR-PERF-* — need baseline | OPEN | DevOps |
| OQ-NFR-02 | RTO/RPO never tested via DR drill — gap NFR-REL-02, REL-03 | OPEN | DevOps + Compliance |
| OQ-NFR-03 | WCAG audit pending — gap NFR-USE-02 | OPEN | Frontend lead |

---

## 9.12 Summary

| Category | NFR count | Must | Should | Could |
|----------|-----------|------|--------|-------|
| Performance Efficiency | {{N}} | {{N}} | {{N}} | {{N}} |
| Security | {{N}} | {{N}} | {{N}} | {{N}} |
| Usability | {{N}} | {{N}} | {{N}} | {{N}} |
| Reliability | {{N}} | {{N}} | {{N}} | {{N}} |
| Maintainability | {{N}} | {{N}} | {{N}} | {{N}} |
| Portability | {{N}} | {{N}} | {{N}} | {{N}} |
| Compatibility | {{N}} | {{N}} | {{N}} | {{N}} |
| Compliance | {{N}} | {{N}} | {{N}} | {{N}} |
| **Total** | **{{N}}** | **{{N}}** | **{{N}}** | **{{N}}** |

---

*Verification methods feed into RTM (M10) where each NFR's tests/audits/drills are tracked alongside FR tests.*
