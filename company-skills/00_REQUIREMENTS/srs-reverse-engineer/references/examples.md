# SRS Reverse Engineer — Worked Example

Anonymized. Fictional project: **"Project Anchor"** — a 7-year-old internal CRM that the company is formalizing for SOC2 Type II audit. Mode A.

## Context

**Imagined input:** "Reverse-engineer SRS for Anchor. SOC2 audit in 90 days. Founder still works here but original eng team is gone. We have CODEBASE_MAP, BUSINESS_CONTEXT (both fresh), DATA_ARCHITECTURE."

**Time budget:** 24 hours over 2 weeks.

**Functional domains identified:** 5 (Authentication, Customers, Deals, Activity Feed, Admin & Audit).

---

## Output structure

```
docs/00_REQUIREMENTS/SRS_VI/
├── M1_Introduction.md
├── M2_Overall_Description.md
├── M3_Authentication.md
├── M4_Customers.md
├── M5_Deals.md
├── M6_Activity_Feed.md
├── M7_Admin_and_Audit.md
├── M9_Non_Functional_Requirements.md  (placeholder; SOC2 makes this load-bearing)
└── M10_RTM_Issues_Appendix.md
```

---

## M1.1 excerpt — explicit "as-is" framing

```markdown
## 1.1 Purpose

This Software Requirements Specification documents the **current state** of Project Anchor
as of 2026-04-30 (commit `7f3e9a2` on `main` branch). It is a **reverse-engineered
"as-is" SRS** — it captures what the system does today, not what it should do.

**Audience:**
- SOC2 auditor (primary)
- Engineering team (now consisting of 4 engineers; founder + 3 hired post-original team)
- Internal compliance lead

**Purpose of this document:**
- Provide formal requirements artifact for SOC2 Type II audit (Trust Services Criteria CC6, CC7, A1)
- Establish baseline for any future product decisions ("here's what we have today")
- Surface gaps between current behavior and intended behavior (for prioritization, not blame)

**This SRS is not:**
- A specification of intended future behavior (use a separate "to-be" SRS for that)
- A roadmap or product plan
- A bug list (use `tech-debt-audit` output for that)

## 1.4 References

| ID | Reference | Why it matters here |
|----|-----------|---------------------|
| REF-01 | IEEE 830-1998 | Format basis |
| REF-02 | SOC2 Type II Trust Services Criteria (2022) | Drives M9 NFRs and M2.5 constraints |
| REF-03 | docs/01_DISCOVERY/CODEBASE_MAP.md (commit 7f3e9a2) | Source for M2.1, M2.4 |
| REF-04 | docs/01_DISCOVERY/BUSINESS_CONTEXT.md (commit 7f3e9a2) | Source for M3-M7 use cases, entities, rules |
| REF-05 | docs/01_DISCOVERY/DATA_ARCHITECTURE.md (commit 7f3e9a2) | Source for M2.5 constraints, M9 placeholder seeds |
| REF-06 | Founder interview, 2026-04-22 (transcript in M10 Appendix) | Source for intent-questions in M3-M7 |
```

---

## M2.5 excerpt — distinguishing intentional vs accidental constraints

```markdown
## 2.5 Design and Implementation Constraints

These constraints describe the design space within which Project Anchor currently operates.
**Intentional** constraints were deliberate decisions; **accidental** constraints are
current limitations from legacy decisions that should be reviewed for relaxation.

### Regulatory / Legal

| ID | Constraint | Type | Source |
|----|------------|------|--------|
| CON-REG-01 | PII (customer email/name/phone) encrypted at rest | Intentional | SOC2 CC6.7 |
| CON-REG-02 | Audit log of mutations on Customer and Deal entities | Intentional | SOC2 CC7.2 |
| CON-REG-03 | Data residency: US-only (us-east-1) | Intentional | Customer commitment (US-only product) |
| CON-REG-04 | No GDPR right-to-export endpoint exists | **Gap (accidental)** | Should exist if EU customers added; current product is US-only |

### Technology

| ID | Constraint | Type | Source |
|----|------------|------|--------|
| CON-TECH-01 | Backend in Ruby on Rails 6.x | Accidental (legacy) | Original team's choice; team prefers Node now |
| CON-TECH-02 | Postgres 12 (not upgraded since 2021) | Accidental | Major upgrade postponed; should plan |
| CON-TECH-03 | No caching layer — direct Postgres reads | Accidental | Sufficient at current scale; would constrain growth |
| CON-TECH-04 | Email via SendGrid (DPA in place) | Intentional | Standard vendor |

### Operational

| ID | Constraint | Type | Source |
|----|------------|------|--------|
| CON-OPS-01 | Single AZ deployment (no HA) | Accidental | Cost; acceptable for internal tool |
| CON-OPS-02 | RTO not formally defined; observed restore: ~2h from snapshot | Accidental | Should formalize for SOC2 |
| CON-OPS-03 | Backups daily; 30-day retention | Intentional (per founder interview) | Confirmed in REF-06 |

### Why distinguish?
- **Intentional** constraints: keep, document why
- **Accidental** constraints: candidates for relaxation; flag in M10 Open Issues for prioritization

(Founder interview REF-06 confirmed the Type column for entries marked "per founder interview". Other Type assignments are inferred and should be reviewed.)
```

---

## M3 excerpt — FR with reverse-engineered source

```markdown
### FR-AUTH-01 — User Login with Username + Password

**Statement:** The system shall authenticate users via username + password.

**Details:**
- Username = email; format validated per RFC 5322
- Password ≥ 8 characters (no other complexity rules currently enforced)
- Successful login creates server-side session; session ID stored in httpOnly cookie
- Session timeout: 24 hours (no "remember me" feature)
- Failed login attempts logged but no lockout policy enforced

**Acceptance criteria** (verifies current behavior):
- [x] Verified live: valid credentials log user in
- [x] Verified live: invalid credentials show generic error message
- [x] Verified live: cookie has HttpOnly flag (browser DevTools)
- [x] Verified live: 24h timeout (left logged in overnight; verified expired next morning)
- [ ] **Gap:** No verification of failed login lockout — code shows logging but not enforcement

**Priority:** Currently Implemented (default)

**Source:** Reverse-engineered from `app/controllers/sessions_controller.rb:14-58` and `app/models/user.rb:78`.

**Verification method:** Live UI test on staging clone; code inspection.

**Notes / Open Issues:**
- OQ-AUTH-01: Was 8-character minimum chosen intentionally? SOC2 likely requires stronger. (Pending founder confirmation; may need change)
- OQ-AUTH-02: No account lockout despite logging — was this intentional or oversight? Code suggests lockout was started but not finished (commented-out lines at sessions_controller.rb:42).
- OQ-AUTH-03: Password storage uses bcrypt (verified `User#authenticate` method); confirmed adequate.

---

### FR-AUTH-02 — Logout

**Statement:** The system shall allow users to log out, ending their session.

**Details:**
- "Sign Out" link in user dropdown menu
- Server-side session destroyed; cookie cleared

**Acceptance criteria:**
- [x] Verified live: clicking Sign Out ends session and redirects to login

**Priority:** Currently Implemented

**Source:** Reverse-engineered from `app/controllers/sessions_controller.rb:65-71`.

---

(FR-AUTH-03 through 07 omitted for brevity)

## 3.6 Open Questions (for stakeholder review)

| ID | Question | Category | Action |
|----|----------|----------|--------|
| OQ-AUTH-01 | Is 8-char password minimum intentional or oversight? | Intent unclear | Founder review; SOC2 may force change |
| OQ-AUTH-02 | Is missing lockout intentional or unfinished? | Intent unclear | Code archeology + founder interview |
| OQ-AUTH-04 | "Remember me" not present — was it removed? Or never built? | Intent unclear | Git log archaeology |
| OQ-AUTH-05 | MFA not present — required for SOC2 admin accounts? | Compliance gap | Required for SOC2 CC6.6; MUST be added before audit |

(5 OQs in this domain; expected for reverse-engineered SRS.)

## 3.7 Confidence

**Confidence for this module:** Medium-High.

Reasoning: Auth code is small (~200 LOC across sessions_controller and user model), flow is well-understood, live verification possible. OQ items are about *intent* (not behavior) — behavior itself is well-documented.
```

---

## M10 excerpt — Open Issues consolidated

```markdown
## 10.2 Open Issues

| ID | Issue | Originated | Type | Status | Owner |
|----|-------|------------|------|--------|-------|
| ISS-01 | 8-char password minimum may not meet SOC2 requirements | M3 (FR-AUTH-01) | Compliance gap | OPEN | Founder + Compliance |
| ISS-02 | Account lockout not enforced (code partial) | M3 (FR-AUTH-01) | Bug or intentional? | OPEN | Engineering |
| ISS-03 | No MFA available; SOC2 admin role likely requires it | M3 (FR-AUTH-04) | Compliance gap | BLOCKED on roadmap decision | Founder |
| ISS-04 | RTO not formally defined (currently ~2h observed) | M2.5 (CON-OPS-02) | Documentation gap | OPEN | DevOps + Compliance |
| ISS-05 | No GDPR right-to-export endpoint | M2.5 (CON-REG-04) | Latent compliance gap | DEFERRED | (Not US-only product, but flag for future) |
| ISS-06 | Audit log captures mutations but does not include "who" beyond user_id (no IP, user-agent) | M7 (FR-ADM-04) | SOC2 CC7.2 partial | OPEN | Engineering |
| ISS-07 | Customer entity has 3 fields (`stage`, `lifecycle_stage`, `phase`) — unclear which is canonical | M4 (data dictionary) | Tribal knowledge | OPEN | Founder interview |
| ISS-08 | Activity Feed retention: 90 days vs unlimited — code inconsistent | M6 (FR-FEED-02) | Bug or intent? | OPEN | Engineering |
| ISS-09 | Internal admin UI (Rails console exposed) bypasses all auth | M7 (out of FR scope) | Security gap | OPEN | DevOps + Security |
| ISS-10 | Two database connection methods (legacy + new) coexist; both used | M2.4 (operating env) | Tech debt | OPEN | Engineering |
| ISS-11 | No formal data classification (PII vs internal vs public) | M2.5 + M9 | Compliance gap | OPEN | Compliance |
| ISS-12 | Backup restoration never tested | M2.5 (CON-OPS-02) | DR gap | OPEN | DevOps |
| ISS-13 | Some FRs derived from staging-only behavior; production may differ | M3-M7 | Verification gap | OPEN | DevOps |
| ISS-14 | Founder unavailable from 2026-05-15 to 2026-05-30 | All modules | Schedule risk | NOTED | Compliance lead |

(14 issues — substantive list reflecting genuine reverse-engineering gaps. Compare to greenfield SRS which usually has 3-7.)
```

---

## Calibration notes

- **"As-is" framing in M1.1.** Explicitly states this SRS describes current state, not intended state. Auditors specifically ask "is this what the system does or what we plan?"
- **Source = code path.** Every FR cites a file path and line numbers, not a stakeholder name. This is the audit-trail-friendly format.
- **Intent vs behavior distinction.** "Currently Implemented" replaces MoSCoW priority — reverse-engineering doesn't choose priority; it documents reality.
- **Open Issues are big.** 14 ISS items at draft. This is correct — reverse-engineering surfaces issues. A small list would suggest under-thoroughness.
- **Confidence per module.** M3 Authentication confidence Medium-High because small/clear; other modules might be Lower if data model is complex or live verification was limited.
- **Constraint Type column.** Distinguishing Intentional vs Accidental is gold for downstream rewrite planning. Don't skip this even though it requires founder interview to determine accurately.
- **Compliance gaps surfaced.** ISS-01 (weak password), ISS-03 (no MFA), ISS-05 (no GDPR export), ISS-06 (audit log thin), ISS-09 (Rails console), ISS-11 (no data classification), ISS-12 (no DR test) — these become input to remediation planning.
