# NFR Specification — Worked Example

Anonymized. Continuing **"Project Atrium"** from `srs-greenfield-author` example. Mode A.

## Context

**Imagined input:** "Populate M9 for Atrium. We have draft M1, M2, M3-M6 (FRs). Stakeholders agreed to SOC2 Type I within Year 1, basic SLA of 99.9% uptime, p95 ≤ 500ms for API."

**Time budget:** 5 hours.

**Categories used:** All 8 ISO 25010 + Compliance.

---

## Output excerpt

```markdown
# M9 — Non-Functional Requirements (Project Atrium)

## 9.0 Overview

This module specifies the non-functional requirements for **Project Atrium**, an
invoicing SaaS for small businesses. NFRs cover performance, security, usability,
reliability, maintainability, portability, compatibility, and compliance.

**Categorization mode:** A — ISO/IEC 25010
**Mode rationale:** Default; no company-specific NFR taxonomy exists.

**Current state assessment date:** 2026-05-15 (pre-launch; targets are aspirational).
**Sources:**
- M2.5 Constraints (especially CON-OPS-01 RTO ≤ 8h, CON-OPS-02 single AZ at v1)
- All M3-M6 FRs (cross-referenced to NFRs in 9.9)
- Customer commitment: 99.9% uptime; p95 latency ≤ 500ms
- SOC2 Type I commitment (Year 1)
- WCAG 2.1 Level AA commitment (accessibility policy)

**Total NFRs:** 31 across 8 categories.

---

## 9.1 Performance Efficiency (5 NFRs)

### NFR-PERF-01 — API Response Time (Read endpoints)

**Statement:** The system shall respond to authenticated GET endpoints within 500ms p95.
**Metric:** Server-side response time (excludes client network latency)
**Target:** p95 ≤ 500ms; p99 ≤ 1000ms
**Condition:** Up to 50 req/s sustained; database reachable; cold cache acceptable for first 100 req/s on any new endpoint
**Current state:** Not yet built (greenfield)
**Source:** Customer commitment (FAQ on landing page) + reasonable competitor benchmark
**Verification method:** k6 load test against staging at 50 req/s for 5 minutes; production APM alert at p95 > 600ms sustained 5 min
**Priority:** Must
**Functional impact:** All `GET /api/*` endpoints (all read FRs across M3-M6)

### NFR-PERF-02 — API Response Time (Write endpoints)

**Statement:** The system shall complete authenticated POST/PUT/DELETE endpoints within 1000ms p95.
**Metric:** Server-side response time including DB write commit
**Target:** p95 ≤ 1000ms; p99 ≤ 2000ms
**Condition:** Up to 20 req/s sustained; standard payload size <50KB
**Current state:** Not yet built
**Source:** UX commitment (no spinners > 1s on common actions)
**Verification method:** k6 load test; production monitoring
**Priority:** Must
**Functional impact:** All write FRs

### NFR-PERF-03 — Email Delivery (Transactional)

**Statement:** Transactional emails (signup verification, password reset, invoice send) shall arrive within 60 seconds p95.
**Metric:** Time from system trigger to email "delivered" event from SendGrid webhook
**Target:** p95 ≤ 60s; p99 ≤ 5min
**Condition:** SendGrid SLA-bound; recipient mail server functional
**Current state:** Will be ~30s based on SendGrid baseline
**Source:** Implicit user expectation; SendGrid baseline
**Verification method:** Synthetic test sending email to internal Gmail address every 15 min
**Priority:** Should (FR-AUTH-05 verification flow), Must (FR-INV-04 invoice send)
**Functional impact:** FR-AUTH-01, FR-AUTH-03, FR-AUTH-05, FR-INV-04, FR-PAY-02

### NFR-PERF-04 — Page Load Time (initial)

**Statement:** Authenticated dashboard initial load shall complete in ≤ 2.5s p95 on standard broadband (10 Mbps).
**Metric:** Largest Contentful Paint (LCP) per Core Web Vitals
**Target:** ≤ 2.5s p95 (rated "Good" per Web Vitals)
**Condition:** 10 Mbps connection; mid-range device (e.g., MacBook Air 2020 / iPhone 12)
**Current state:** Not yet built
**Source:** Web Vitals "Good" threshold
**Verification method:** Lighthouse in CI; PSI (PageSpeed Insights) on production weekly
**Priority:** Should
**Functional impact:** Dashboard FRs

### NFR-PERF-05 — Concurrent User Load

**Statement:** The system shall support up to 500 concurrent active users without degradation.
**Metric:** Concurrent sessions per minute
**Target:** ≥ 500 concurrent users while NFR-PERF-01 still holds
**Condition:** "Active" = made an authenticated request in last 60s
**Current state:** Not yet built
**Source:** Year 1 traffic projection (1K paying customers × 50% concurrency at peak)
**Verification method:** k6 load test simulating 500 virtual users; pre-launch readiness gate
**Priority:** Should (Year 1 target)
**Functional impact:** All authenticated FRs

---

## 9.2 Security (8 NFRs)

### NFR-SEC-01 — Authentication Method

**Statement:** Users shall authenticate via email + password meeting NIST SP 800-63B Level 1.
**Metric:** Password complexity rules + storage method
**Target:** Min 12 chars, 1 number, 1 special char; bcrypt cost factor ≥ 12; no password expiration enforced
**Condition:** All authenticated requests
**Current state:** Will be designed per FR-AUTH-01
**Source:** NIST SP 800-63B; FR-AUTH-01 acceptance criteria
**Verification method:** Code review; pen test simulated brute force
**Priority:** Must
**Functional impact:** FR-AUTH-01, FR-AUTH-02, FR-AUTH-03

### NFR-SEC-02 — Encryption at Rest

**Statement:** All PII (customer email, name, address, phone, payment metadata) shall be encrypted at rest using AES-256-GCM.
**Metric:** Encryption algorithm + key management
**Target:** AES-256-GCM; keys managed by AWS KMS; default key rotation annual
**Condition:** Postgres database, Postgres backups, S3 buckets storing customer data
**Current state:** Will be configured during deployment (CON-REG-01)
**Source:** CON-REG-01; CCPA; SOC2 CC6.7
**Verification method:** Configuration review; KMS audit logs
**Priority:** Must
**Functional impact:** All FRs handling customer data

### NFR-SEC-03 — Encryption in Transit

**Statement:** All client-server communication shall use TLS 1.3.
**Metric:** TLS version + cipher suite
**Target:** TLS 1.3 minimum; HSTS header with max-age ≥ 31536000; HSTS preload
**Condition:** All endpoints (web app, API)
**Current state:** Will be CloudFront default
**Source:** Industry standard; SOC2 CC6.7
**Verification method:** SSL Labs scan; automated CI test for HSTS header
**Priority:** Must
**Functional impact:** All FRs

### NFR-SEC-04 — Audit Trail

**Statement:** Mutations on Customer, Invoice, and Payment entities shall be logged with actor, timestamp, before/after state.
**Metric:** Audit event capture per critical entity
**Target:** 100% capture; logs stored separately from transactional DB; tamper-resistant (append-only)
**Condition:** Every mutation; both successful and failed authorization attempts
**Current state:** Will be designed per FR-ADM-04 (admin & audit module — but baseline applies to all mutations)
**Source:** SOC2 CC7.2; CCPA breach investigation requirements
**Verification method:** Code review; query audit table after sample mutations; periodic random audit
**Priority:** Must
**Functional impact:** FR-CUST-*, FR-INV-*, FR-PAY-*

### NFR-SEC-05 — Vulnerability Management

**Statement:** Critical CVEs in dependencies shall be patched within 7 days; high within 30 days.
**Metric:** Time from CVE publication to deploy of patched version
**Target:** Critical ≤ 7 days; High ≤ 30 days; Medium ≤ 90 days
**Condition:** Per `npm audit` severity classification
**Current state:** Will be operational from Day 1
**Source:** Industry standard; SOC2 CC7.5
**Verification method:** Automated `npm audit` in CI; alerts to engineering Slack on new findings
**Priority:** Must
**Functional impact:** All

### NFR-SEC-06 — Session Management

**Statement:** Session cookies shall be httpOnly, Secure, SameSite=Lax; sessions invalidate on password change or 30 days max.
**Metric:** Cookie attributes + session lifecycle
**Target:** All session cookies have httpOnly+Secure+SameSite=Lax; max session 30 days; idle timeout 7 days; password change invalidates ALL sessions for that user
**Condition:** All authenticated sessions
**Current state:** Will be designed per FR-AUTH-02
**Source:** OWASP Session Management Cheat Sheet
**Verification method:** Browser DevTools test; integration test
**Priority:** Must
**Functional impact:** FR-AUTH-02, FR-AUTH-03, FR-AUTH-04

### NFR-SEC-07 — Rate Limiting

**Statement:** Login endpoint shall enforce rate limit of 5 attempts per email per 15 minutes; password reset endpoint 1 per email per 5 minutes.
**Metric:** Rate limit enforcement
**Target:** Limits as stated; lockout after threshold
**Condition:** All login and reset attempts
**Current state:** Will be implemented per FR-AUTH-02 acceptance criteria
**Source:** Brute force protection; OWASP Authentication Cheat Sheet
**Verification method:** Integration test attempting >5 logins; verify lockout
**Priority:** Must
**Functional impact:** FR-AUTH-02, FR-AUTH-03

### NFR-SEC-08 — Incident Response Time

**Statement:** Security incidents (P0) shall be detected within 30 minutes and responded to within 4 hours.
**Metric:** Time from event to detection; time from detection to first response
**Target:** Detection p95 ≤ 30 min; response p95 ≤ 4 hours
**Condition:** Production incidents classified P0 (data breach, auth bypass, sustained outage)
**Current state:** No formal IR plan yet (gap)
**Source:** SOC2 CC7.4; customer expectation
**Verification method:** Quarterly tabletop exercise; on-call drill
**Priority:** Should (Year 1); Must (Year 2 for SOC2 audit)
**Functional impact:** All

---

## 9.3 Usability (3 NFRs)

### NFR-USE-01 — Signup Completion Time

**Statement:** A new user shall complete signup (form → verified email → first invoice draft started) in ≤ 5 minutes median.
**Metric:** Median time from `/signup` page load to first `POST /invoices` API call
**Target:** Median ≤ 5 min; p95 ≤ 10 min (excluding email check delays)
**Condition:** Standard signup flow; user has email access
**Current state:** Not yet built
**Source:** Product team UX target
**Verification method:** Moderated usability test (5 users); production funnel metrics
**Priority:** Should
**Functional impact:** FR-AUTH-01, FR-AUTH-05, FR-INV-01

### NFR-USE-02 — Accessibility

**Statement:** All user-facing interfaces shall conform to WCAG 2.1 Level AA.
**Metric:** WCAG conformance level (axe-core scan + manual audit)
**Target:** 0 Level A or AA failures from axe-core scan; manual audit by accessibility consultant pre-launch passes
**Condition:** All public pages, all authenticated pages
**Current state:** Not yet built (will be pre-launch verified)
**Source:** Accessibility commitment; ADA risk
**Verification method:** axe-core in CI; pre-launch manual audit
**Priority:** Must
**Functional impact:** All UI FRs

### NFR-USE-03 — Browser Support

**Statement:** Web app shall function on Chrome 110+, Firefox 110+, Safari 16+, Edge 110+ on desktop and Chrome Android 100+, Safari iOS 15+ on mobile.
**Metric:** Support matrix verification
**Target:** No browser blocking errors; UI usable (read M5 Invoices, send invoice, receive payment confirmation) on all listed browsers
**Condition:** Standard signup, invoice creation, payment receipt flows
**Source:** Market share analysis (covers 95%+ of target users)
**Verification method:** BrowserStack matrix test pre-launch; periodic re-test
**Priority:** Must
**Functional impact:** All UI FRs

---

## 9.4 Reliability (3 NFRs)

### NFR-REL-01 — Uptime

**Statement:** Production system shall achieve ≥ 99.9% uptime measured monthly.
**Metric:** External uptime monitor (Pingdom)
**Target:** ≥ 99.9% (max ~43 min downtime/month); error budget tracked weekly
**Condition:** Excludes planned maintenance announced ≥48h in advance
**Current state:** Not yet built; AWS RDS + ECS combined SLA ≥ 99.95% on paper
**Source:** Customer commitment (Status page)
**Verification method:** Pingdom external check; monthly status report
**Priority:** Must
**Functional impact:** All

### NFR-REL-02 — Recovery Time Objective (RTO)

**Statement:** Recovery from primary AZ failure shall complete within 8 hours.
**Metric:** Time from detection to service restoration
**Target:** ≤ 8 hours (single-AZ at v1; CON-OPS-01)
**Condition:** AZ outage in us-east-1; failover to redeployed infrastructure
**Current state:** Will be tested pre-launch via simulated AZ outage
**Source:** CON-OPS-01; customer DR commitment
**Verification method:** Pre-launch DR drill; quarterly drill post-launch
**Priority:** Must
**Functional impact:** All

### NFR-REL-03 — Recovery Point Objective (RPO)

**Statement:** Maximum acceptable data loss shall be ≤ 1 hour.
**Metric:** Time gap between last successful backup and incident
**Target:** ≤ 1 hour (RDS automated backups every 5 min via WAL)
**Condition:** Standard DR scenario
**Current state:** Will be configured via RDS automated backups (5-min WAL window)
**Source:** Customer DR commitment
**Verification method:** Backup automation verification + restore test
**Priority:** Must
**Functional impact:** All write FRs

---

## 9.5 Maintainability (2 NFRs)

### NFR-MAINT-01 — Test Coverage

**Statement:** Critical paths (auth, payment, invoice send) shall have ≥ 80% statement coverage.
**Metric:** Statement coverage from Vitest
**Target:** ≥ 80% in `src/server/services/auth/*`, `src/server/services/payments/*`, `src/server/services/invoices/send.ts`
**Condition:** Per-file coverage as reported by Vitest
**Current state:** Not yet built
**Source:** Engineering quality bar
**Verification method:** Vitest coverage; PR gate at 80% for these paths
**Priority:** Must
**Functional impact:** All

### NFR-MAINT-02 — Build Time

**Statement:** CI build (lint + type-check + test + build) shall complete in ≤ 10 minutes p95.
**Metric:** GitHub Actions workflow duration
**Target:** p95 ≤ 10 min (cold), ≤ 5 min (cache warm)
**Condition:** Standard PR
**Current state:** Not yet built
**Source:** Developer productivity
**Verification method:** GitHub Actions timing reports
**Priority:** Should
**Functional impact:** All

---

## 9.6 Portability (1 NFR)

### NFR-PORT-01 — Database Portability

**Statement:** Schema and queries shall avoid Postgres-specific features without abstraction.
**Metric:** Postgres-specific feature usage in critical query paths
**Target:** ≤ 5 Postgres-specific patterns in critical query paths; each documented with rationale
**Condition:** v1 stays on Postgres; portability is for "could migrate if needed"
**Source:** Operational risk hedge
**Verification method:** Code review checklist
**Priority:** Could
**Functional impact:** Data-layer FRs

---

## 9.7 Compatibility (1 NFR)

### NFR-COMPAT-01 — API Versioning

**Statement:** Public API endpoints shall support v1 contracts indefinitely once released; breaking changes require v2 path.
**Metric:** Backward compatibility maintenance
**Target:** v1 contracts maintained; deprecation requires 12-month notice + v2 alternative
**Condition:** All `/api/v1/*` endpoints
**Source:** Customer integration commitment
**Verification method:** Contract test in CI; API changelog audit
**Priority:** Must (contractual)
**Functional impact:** All API FRs (M3-M6)

---

## 9.8 Compliance (8 NFRs)

### NFR-COMP-01 — SOC2 Type I (Year 1)

**Statement:** System shall pass SOC2 Type I audit within 12 months of launch.
**Target:** Successful Type I audit covering Security, Availability, Confidentiality
**Source:** Customer commitment; B2B sales gating
**Verification method:** External SOC2 audit
**Priority:** Must
**Functional impact:** All

### NFR-COMP-02 — SOC2 Type II (Year 2)

**Statement:** Within 24 months of launch, achieve SOC2 Type II audit.
**Target:** Successful Type II audit (12-month observation window)
**Source:** Customer commitment
**Verification method:** External SOC2 audit
**Priority:** Should
**Functional impact:** All

### NFR-COMP-03 — CCPA Compliance

**Statement:** California users shall have right-to-export within 45 days, right-to-delete within 45 days.
**Target:** Both rights honored within 45 days per CCPA §1798.130
**Source:** California Consumer Privacy Act
**Verification method:** End-to-end test of export/delete; audit log of fulfillment timestamps
**Priority:** Must
**Functional impact:** Future FR-AUTH-06 (Account Deletion); future FR-EXPORT-01

### NFR-COMP-04 — PCI-DSS Scope Reduction

**Statement:** Atrium shall remain out of full PCI-DSS scope (SAQ-A) by relying on Stripe for all card data handling.
**Target:** No card numbers, CVVs, or full PANs ever stored or transmitted by Atrium servers
**Source:** PCI-DSS SAQ-A; CON-REG-02
**Verification method:** Code review (no Stripe API calls receive raw card data); annual SAQ-A self-assessment
**Priority:** Must
**Functional impact:** FR-PAY-*

### NFR-COMP-05 — Email Sender Authentication

**Statement:** All system emails shall be sent with SPF, DKIM, DMARC properly configured.
**Target:** SPF, DKIM, DMARC PASS for all sent emails (verified via mail-tester.com); DMARC policy = quarantine min
**Source:** Email deliverability + brand spoofing protection
**Verification method:** mail-tester.com pre-launch; ongoing weekly check
**Priority:** Must
**Functional impact:** FR-AUTH-05, FR-INV-04, etc.

(NFR-COMP-06 through 08 omitted for brevity: cookie consent, terms of service display, privacy policy display)

---

## 9.9 NFR-to-FR Cross-Reference

(Table mapping each NFR to FRs it constrains — too long to include here; auto-generated from "Functional impact" fields above)

## 9.10 Constraint-to-NFR Cross-Reference

| Constraint (M2.5) | Became NFR |
|-------------------|------------|
| CON-REG-01 (PII encrypted) | NFR-SEC-02 |
| CON-REG-02 (PCI scope reduction via Stripe) | NFR-COMP-04 |
| CON-REG-03 (Right-to-export ≤ 30d, but CCPA = 45d) | NFR-COMP-03 (relaxed to 45d per CCPA) |
| CON-OPS-01 (RTO ≤ 8h) | NFR-REL-02 |
| CON-OPS-02 (RPO ≤ 1h) | NFR-REL-03 |

## 9.11 Open NFR Issues

| ID | Issue | Status | Owner |
|----|-------|--------|-------|
| OQ-NFR-01 | Specific p95 latency targets — should differ by endpoint? | OPEN | Engineering |
| OQ-NFR-02 | NFR-SEC-08 IR plan does not exist yet — gap for SOC2 | OPEN | Engineering + founder |
| OQ-NFR-03 | NFR-COMP-03 CCPA right-to-export — implementation FR not yet drafted in M3-M6 | OPEN | Product |

## 9.12 Summary

| Category | NFR count | Must | Should | Could |
|----------|-----------|------|--------|-------|
| Performance Efficiency | 5 | 2 | 3 | 0 |
| Security | 8 | 7 | 1 | 0 |
| Usability | 3 | 2 | 1 | 0 |
| Reliability | 3 | 3 | 0 | 0 |
| Maintainability | 2 | 1 | 1 | 0 |
| Portability | 1 | 0 | 0 | 1 |
| Compatibility | 1 | 1 | 0 | 0 |
| Compliance | 8 | 6 | 2 | 0 |
| **Total** | **31** | **22** | **8** | **1** |
```

---

## Calibration notes

- **Targets are aspirational at greenfield.** Current state = "Not yet built" is honest. Reverse-engineered SRSs would have measured values here, often missing target.
- **Sources cite real things.** "Customer commitment", "OWASP Cheat Sheet", "NIST SP 800-63B", "PCI-DSS SAQ-A". No "best practice" without specifying which one.
- **Verification methods are concrete.** "k6 load test in staging at 50 req/s for 5 minutes" — actionable. "Test it" — not actionable.
- **Priority distribution.** 70% Must, 26% Should, 3% Could. For early-stage product, this is reasonable. Mature products tend to push more to Should/Could after stabilization.
- **Compliance NFRs reference clauses.** "CCPA §1798.130" — auditor can verify. "Comply with CCPA" — too vague.
- **8 Security NFRs is rich for a small SaaS.** This is appropriate — Security is where most NFR gaps cause real harm.
- **Open Issues track gaps.** Even at greenfield, OQ-NFR-02 (no IR plan) is honest acknowledgment that some NFRs need follow-up work to support.
