# SRS Greenfield Author — Worked Example

Anonymized. Fictional project: **"Project Atrium"** — a small-business invoicing SaaS. Mode A.

## Context

**Imagined input:** "Author SRS for Atrium. Founding team has 12 stakeholder interviews, a 1-page product brief, and a $200K seed budget for initial 6-month build."

**Time budget:** 12 hours total (across multiple sessions with stakeholder review).

**Functional domains identified:** 4 (Authentication, Customers, Invoices, Payments).

---

## Output structure

```
docs/00_REQUIREMENTS/SRS_VI/
├── M1_Introduction.md
├── M2_Overall_Description.md
├── M3_Authentication.md
├── M4_Customers.md
├── M5_Invoices.md
├── M6_Payments.md
├── M9_Non_Functional_Requirements.md   (placeholder for nfr-specification)
└── M10_RTM_Issues_Appendix.md          (placeholder for requirements-traceability)
```

---

## M1 excerpt

```markdown
# M1 — Introduction

> SRS Module 1 of 10 | Project: Project Atrium | Version: v0.1 (DRAFT) | Date: 2026-05-08

## 1.1 Purpose

This SRS describes the requirements for **Project Atrium**, a web-based invoicing SaaS
for small businesses (1-20 employees) in the US.

**Audience:**
- Founding team (Product, Engineering)
- External design contractor (UI/UX)
- Investor (Series Seed lead) for technical due diligence

## 1.2 Scope

### Product name
Project Atrium (working title; legal name TBD)

### What it does (3-5 sentences)
Atrium lets small business owners create, send, and track invoices to their customers
via a web app. Invoices can be paid online (Stripe + ACH). Atrium tracks payment status,
sends automatic reminders, and produces basic financial reports (revenue, AR aging).
Self-serve signup; freemium model (5 invoices/month free; $19/mo unlimited).

### What it does NOT do (out of scope for v1)
- Inventory management or product catalog
- Multi-currency invoicing (USD only at v1)
- Time tracking or project management
- Recurring subscription billing (one-off invoices only at v1)
- Mobile native apps (mobile web works; native apps post-v1)
- Multi-user accounts within a business (single-user at v1)
```

## M2 excerpt

```markdown
## 2.5 Design and Implementation Constraints

### Regulatory / Legal

| ID | Constraint | Source |
|----|------------|--------|
| CON-REG-01 | PII (customer email/address) encrypted at rest | Industry standard; CCPA |
| CON-REG-02 | Stripe handles all card data; Atrium is PCI scope-reduced | PCI-DSS SAQ-A |
| CON-REG-03 | Right-to-export user data within 30 days of request | CCPA |

### Technology

| ID | Constraint | Reason |
|----|------------|--------|
| CON-TECH-01 | Backend: Node.js + TypeScript | Founder skill set |
| CON-TECH-02 | Database: Postgres (managed, e.g., RDS or Supabase) | Team familiarity, cost |
| CON-TECH-03 | Stripe is sole payment processor for v1 | Procurement done; alternative would delay launch |
| CON-TECH-04 | Email via SendGrid; alternative providers prohibited at v1 | DPA already executed |

### Operational

| ID | Constraint | Reason |
|----|------------|--------|
| CON-OPS-01 | RTO ≤ 8h, RPO ≤ 1h | Acceptable for SMB; contracts will not promise more |
| CON-OPS-02 | Single region (us-east-1) for v1; multi-region post-launch | Cost; complexity reduction |

### Business

| ID | Constraint | Reason |
|----|------------|--------|
| CON-BIZ-01 | Total monthly cloud cost ≤ $500 at launch | Seed runway |
| CON-BIZ-02 | Launch by 2026-11-30 | YC Demo Day commitment |
```

## M3 excerpt — Authentication domain

```markdown
# M3 — Authentication

## 3.1 Domain Overview

This module covers user account creation, login, password management, and session
handling. Atrium uses email + password authentication only at v1; OAuth/social
sign-in deferred to post-v1.

### User classes involved
- Business Owner (primary; only user class at v1; multi-user accounts deferred)

### External systems involved
- SendGrid (transactional email for verification, password reset)

## 3.2 Functional Requirements

### FR-AUTH-01 — User Registration

**Statement:** The system shall allow a new user to register with email and password.

**Details:**
- Email format validated per RFC 5322
- Password ≥ 12 chars; must include 1 number and 1 special char
- Email uniqueness enforced — duplicate signup attempt returns explicit error
- Confirmation email sent with verification link (24-hour expiry)
- Account is "unverified" until email verified; can log in but cannot send invoices

**Acceptance criteria:**
- [ ] Signup form accepts valid email + strong password; creates account
- [ ] Signup form rejects invalid email format with specific error message
- [ ] Signup form rejects weak password with explanation
- [ ] Duplicate email signup attempts get clear error (not generic "failed")
- [ ] Verification email arrives within 60 seconds (SendGrid SLA-bound)
- [ ] Verification link expires after 24 hours
- [ ] Unverified users see explicit banner: "Verify email to send invoices"

**Priority:** Must

**Source:** Stakeholder interview (Founder, 2026-04-12); regulatory NIST SP 800-63B

**Verification method:** Acceptance tests + manual smoke test on real email delivery

**Test cases (anticipated):** TC-AUTH-01..06

**Notes / Open questions:**
- OQ-AUTH-01: Should "remember me" be available at signup form? (Pending UX review)

---

### FR-AUTH-02 — Login

**Statement:** The system shall authenticate users via email + password.

**Details:**
- 5 consecutive failed attempts lock account for 15 minutes
- Successful login creates session via httpOnly + Secure cookie
- Session timeout: 7 days idle, 30 days max
- Optional "Remember me" checkbox extends max session to 90 days

**Acceptance criteria:**
- [ ] Valid credentials → user logged in, session cookie set
- [ ] Invalid credentials → generic "Invalid email or password" (no info leak)
- [ ] After 5 failures, account locked for 15min with explicit message
- [ ] Session persists across browser restarts (cookie not session-only)
- [ ] "Remember me" extends session per requirements

**Priority:** Must

**Source:** Stakeholder interview (Founder, 2026-04-12); CON-REG-01

**Verification method:** Acceptance tests; security review for lockout policy

**Test cases:** TC-AUTH-07..14

---

### FR-AUTH-03 — Password Reset

**Statement:** The system shall allow users to reset forgotten passwords via email.

**Details:**
- "Forgot password" link on login page
- User enters email; if email exists, reset email sent (no leak if email doesn't exist)
- Reset link valid for 1 hour
- Reset email rate-limited: 1 per email per 5 minutes
- New password must meet same complexity as registration
- Active sessions invalidated upon password change

**Acceptance criteria:**
- [ ] Reset request sends email if account exists
- [ ] Reset request returns same response whether or not account exists (no enumeration)
- [ ] Reset link works exactly once
- [ ] Reset link expires after 1 hour
- [ ] Rate limit enforced (test: 2 requests within 5min → second gets generic message)
- [ ] After password change, all other sessions logged out

**Priority:** Must

**Source:** Stakeholder interview (Founder); standard practice; NIST SP 800-63B

---

### FR-AUTH-04 — Logout

**Statement:** The system shall allow users to log out, invalidating their session.

**Details:**
- "Log out" link in user menu
- Session cookie cleared on client and revoked on server
- After logout, navigation to authenticated pages redirects to login

**Acceptance criteria:**
- [ ] Click "Log out" → session ended; redirect to login page
- [ ] Browser back-button navigation does not show authenticated content (no caching)

**Priority:** Must

---

### FR-AUTH-05 — Email Verification

**Statement:** The system shall verify user email addresses before allowing invoice send.

**Details:**
- Verification link in welcome email (FR-AUTH-01)
- Click link → account marked verified
- Unverified accounts cannot use FR-INV-04 (Send Invoice)
- "Resend verification" available in user settings

**Acceptance criteria:**
- [ ] Link click marks account verified; user redirected to dashboard
- [ ] Expired link shows "Resend" CTA
- [ ] Resend rate-limited (1 per 5 min)

**Priority:** Must

---

(FR-AUTH-06: Account deletion — Should priority, omitted for brevity)

---

## 3.3 Workflows

### Workflow: First-time user registration

**Trigger:** User clicks "Sign up" on landing page

**Actors:** Business Owner

**FRs involved:** FR-AUTH-01, FR-AUTH-05

**Happy path:**
```
1. User submits signup form (FR-AUTH-01) → account created (unverified)
2. User auto-logged in; sees dashboard with "Verify email" banner
3. User clicks verification link in email (FR-AUTH-05) → marked verified
4. Banner disappears; user can now send invoices
```

**Alternative paths:**
- User doesn't verify within 24h → link expires; "Resend" prompt visible
- User wants to send invoice before verifying → blocked with explicit "Verify first" message

---

## 3.4 Out of Scope

- OAuth / social sign-in (Google, Apple) — deferred post-v1
- Multi-factor authentication — deferred post-v1
- Multi-user accounts within one business — deferred post-v1
- SSO for enterprise customers — not applicable at v1 (target market is SMB)

## 3.5 Open Questions

| ID | Question | Action |
|----|----------|--------|
| OQ-AUTH-01 | "Remember me" checkbox at signup or only at login? | Pending UX review (target: 2026-05-15) |
| OQ-AUTH-02 | Account deletion — soft (recoverable for 30d) or hard? | Pending legal review (CCPA implications) |

## 3.6 Priority Summary

| Priority | Count |
|----------|-------|
| Must | 5 |
| Should | 1 |
| Could | 0 |
| Won't (this release) | 0 |

(Within bounds; mostly Must which is normal for foundational auth domain.)
```

---

## M10 Open Issues excerpt

```markdown
## 10.2 Open Issues

| ID | Issue | Originated | Status | Owner | Target |
|----|-------|------------|--------|-------|--------|
| ISS-01 | "Remember me" checkbox UX (FR-AUTH-01, FR-AUTH-02) | M3 | OPEN | Founder + UX contractor | 2026-05-15 |
| ISS-02 | Account deletion soft vs hard (FR-AUTH-06, CON-REG-03) | M3 + M2.5 | BLOCKED on legal | External legal counsel | 2026-05-30 |
| ISS-03 | Invoice numbering scheme (sequential per user vs global UUID) | M5 | OPEN | Founder | 2026-05-12 |
| ISS-04 | Stripe payout delay (T+2) — should we display "expected on" date to user? | M6 | OPEN | Founder + design | 2026-05-15 |
| ISS-05 | Tax line items — should v1 support multiple tax rates per invoice or single rate? | M5 | OPEN | Stakeholder interview | 2026-05-20 |

(5 open issues at draft; expected to resolve before v1.0 sign-off.)
```

---

## Calibration notes

- **DRAFT until reviewed.** Marked v0.1 because not all stakeholders have reviewed. Keep it DRAFT honest — promote to v1.0 only after sign-off.
- **OQ propagation.** Questions in functional modules (M3.5, M4.5, etc.) propagate to consolidated M10.2. Don't lose them.
- **Out-of-scope items are gold.** v1 has 6 explicit out-of-scope items; this prevents stakeholder "could you also..." after launch.
- **Priority distribution.** Auth domain skewing Must is fine (it's foundational). Other domains should have more Should / Could spread.
- **Constraints flow.** CON-REG-01 (PII encrypted) cited in FR-AUTH-02 source field. The traceability between constraints and FRs is what makes the SRS auditable.
- **No NFRs in M3-Mx.** "Verification email arrives within 60 seconds" looks NFR-ish but is a *functional* acceptance criterion (the FR is "send email"; the 60s is part of the FR's success). The general "system shall be fast" goes to M9.
- **"Inferred" honesty.** If a stakeholder didn't explicitly say something, mark it Inferred so it can be confirmed.
