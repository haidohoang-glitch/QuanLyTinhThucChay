# Tech Debt Audit — Worked Example

Anonymized. Fictional project: **"Project Beacon"** — a B2B analytics dashboard, 3 years old, 2 engineers maintaining. Mode A.

## Context

**Imagined input:** "Audit Beacon. We're considering a v3 rewrite — need data on whether to refactor incrementally or rewrite."

**Time budget:** 4 hours.

---

## Generated output (excerpt)

```markdown
# Project Beacon — Tech Debt Audit

> Generated using: tech-debt-audit skill v1
> Last updated: 2026-04-22
> Reviewer: TBD

## 1. Executive Summary

**Overall debt level:** HIGH (but manageable — incremental refactor is feasible).

**Highlights:**
- Total findings: 38 (2 P0, 11 P1, 19 P2, 6 P3)
- Categories with most debt: SECURITY (9), MAINTAINABILITY (10)
- Estimated total remediation effort: ~280 dev-hours (~7-8 dev-weeks)

**Top 3 risks:**
1. F-03 — Auth tokens stored in localStorage; XSS leads to full account takeover (P0)
2. F-08 — npm audit reports critical vuln in `axios@0.21.1` (P0)
3. F-12 — DB connection pool exhausts under burst load; outages monthly (P1)

---

## 2. Quality Signals (Raw Data)

| Signal | Value | Notes |
|--------|-------|-------|
| Test coverage | 22% | Vitest; critical paths (auth, billing) at 5-12% |
| Lint errors | 147 | Top: `@typescript-eslint/no-explicit-any` (62 occurrences) |
| Type errors (`tsc --noEmit`) | 23 | Mostly in `src/legacy/*` |
| `npm audit` | 14 vulns (2 critical, 5 high) | axios, lodash, marked |
| `npm outdated` | 38 packages outdated, 12 major versions behind | React 17 → 19, Node 16 → 22 |
| Bundle size | 1.4 MB gzipped | Up from 0.8 MB a year ago |
| Largest files | `src/legacy/Dashboard.tsx` (2400 LOC), `src/api/users.ts` (1800 LOC) | |

---

## 3. Categorization Mode

See Section 9 (Mode A — standard 7 categories).

---

## 4. Findings (by category)

### SECURITY

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| F-01 | P1 | M | CORS allows `*`; no origin validation | `src/server/middleware/cors.ts:8` | Set explicit allowlist |
| F-02 | P1 | S | No rate limiting on login endpoint | `src/server/routes/auth.ts:24` (no middleware) | Add `express-rate-limit` |
| F-03 | **P0** | M | Auth tokens in localStorage; vulnerable to XSS | `src/api/client.ts:14` reads `localStorage.token` | XSS surface present (F-22) — chain risk |
| F-04 | P1 | S | Unsanitized HTML rendered with `dangerouslySetInnerHTML` | `src/components/RichText.tsx:42` | Use DOMPurify |
| F-05 | P2 | XS | Helmet middleware not enabled | `src/server/index.ts` | One-line fix |
| F-06 | P1 | M | Password reset token never expires | `src/server/services/auth/reset.ts` | Add 1h expiry + DB index |
| F-07 | P2 | S | Stripe webhook signature not verified | `src/server/webhooks/stripe.ts:12` | Use `stripe.webhooks.constructEvent` |
| F-08 | **P0** | XS | `axios@0.21.1` has CVE-2023-45857 (high) | `package.json` | Upgrade to ^1.6 |
| F-09 | P2 | S | Tenant-scoping relies on app-layer; no RLS at DB | `src/server/services/*` | Defer to data audit; flag here |

### CODE_QUALITY

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| F-10 | P2 | M | `src/legacy/Dashboard.tsx` 2400 LOC, untested | file size + coverage report | Split into 4-5 components, add tests |
| F-11 | P2 | L | 62 `any` type violations | lint report | Migrate top files first |
| F-12 | P1 | S | DB connection pool size hardcoded to 5 | `src/server/db/pool.ts:6` | Outages observed monthly under burst |
| F-13 | P3 | XS | Console.log statements in production paths | grep results, 23 occurrences | Replace with logger |

### PERFORMANCE

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| F-14 | P1 | M | N+1 in `/api/dashboards/:id` (loads each widget separately) | `src/api/dashboards.ts:78-95` | Use single JOIN or batched fetch |
| F-15 | P2 | S | List endpoint has no pagination | `src/server/routes/users.ts:45` | Add limit/offset |
| F-16 | P2 | M | Bundle includes `moment.js` (heavy) + `date-fns` (already used) | bundle analyzer | Remove moment.js — saved ~250KB |
| F-17 | P3 | S | Sync `fs.readFileSync` on cold-start | `src/server/templates.ts:8` | Async load + cache |

### RELIABILITY

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| F-18 | P1 | M | 12 catch blocks swallow errors silently | grep `catch.*\{\s*\}` | Log + Sentry capture |
| F-19 | P1 | S | No timeouts on outbound HTTP calls | `src/server/services/external/*` (axios defaults) | Set 5s timeout |
| F-20 | P2 | M | Background jobs have no retry/dead-letter | `src/jobs/*` | Add BullMQ retry config |
| F-21 | P2 | XS | `process.exit(0)` in test cleanup leaks to dev | `tests/setup.ts:14` | Wrap in NODE_ENV check |

### MAINTAINABILITY

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| F-22 | P1 | XL | React 17 → React 19 upgrade | `package.json` | Major work, blocks several other findings |
| F-23 | P1 | L | Node 16 EOL — unsupported | runtime in CI/Dockerfile | Bump to Node 22 |
| F-24 | P2 | M | Test coverage 22% — too low for refactor confidence | coverage report | Triage critical paths first |
| F-25 | P2 | M | Two state management libraries (Redux + Zustand) | grep imports | Pick one, migrate |
| F-26 | P2 | S | No CI step for `tsc --noEmit` | `.github/workflows/ci.yml` | Add type-check job |
| F-27 | P3 | XS | README missing local-setup instructions | `README.md` | One-page update |

### SCALABILITY

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| F-28 | P2 | M | In-memory rate limiter (won't survive horizontal scale) | `src/server/middleware/rateLimit.ts` | Move to Redis-backed limiter |
| F-29 | P2 | S | File uploads stored on local disk | `src/server/routes/uploads.ts:30` | Move to S3 |
| F-30 | P2 | L | Background jobs hardcoded `if (clinic_id === 'foo')` patterns | `src/jobs/*` | Refactor to data-driven |

### COMPLIANCE

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| F-31 | P1 | M | No GDPR export endpoint | grep | Add `/api/me/export` |
| F-32 | P1 | M | User delete is soft, but doesn't cascade to backup tier | `src/server/services/users/delete.ts` | See data audit R-03 |
| F-33 | P2 | XS | Privacy policy in code repo is 2 years stale | `legal/PRIVACY.md` | Legal review needed |
| F-34 | P2 | S | No audit log for billing events | `src/server/services/billing/*` | Add write to audit_log table |
| F-35 | P3 | S | Cookie banner consent not granular (single accept-all) | `src/components/CookieBanner.tsx` | Per CCPA likely insufficient |

(3 more P3 findings omitted for brevity)

---

## 5. Clusters

### Cluster: "No defensive programming discipline"

- **Root cause:** Codebase grew without consistent error/timeout/retry patterns. Likely stems from solo founder phase.
- **Findings included:** F-18, F-19, F-20
- **Combined effort to fix root cause:** ~M (set up shared utility for outbound calls + error handler middleware)
- **Combined risk reduction:** all 3 findings closed

### Cluster: "Auth/security fundamentals missing"

- **Root cause:** Initial auth implementation copied from a tutorial; never hardened.
- **Findings included:** F-01, F-02, F-03, F-04, F-05, F-06, F-07
- **Combined effort:** L (restructure as 1-week security sprint)
- **Combined risk reduction:** 7 findings closed; 1 P0 + 4 P1 + 2 P2

### Cluster: "Stack age — React 17 + Node 16"

- **Root cause:** No upgrade discipline; major upgrades skipped.
- **Findings included:** F-08, F-22, F-23, F-26
- **Combined effort:** XL (upgrades unblock other work)
- **Combined risk reduction:** unblocks improvements across all categories

---

## 6. Top 10 Punch List

| Order | Finding | Why this priority | Effort |
|-------|---------|-------------------|--------|
| 1 | F-08 | P0 critical CVE; XS effort; no excuse | XS |
| 2 | F-03 | P0 token storage; chained risk with F-22 | M |
| 3 | F-22 | Unblocks 4+ other findings; foundation | XL |
| 4 | F-23 | Node 16 EOL; security + ecosystem | L |
| 5 | F-12 | Active production outages | S |
| 6 | F-18 | Silent failures hide other issues | M |
| 7 | F-19 | Cheap fix, big reliability gain | S |
| 8 | F-31 | GDPR exposure, M effort | M |
| 9 | F-14 | Customer-visible perf complaint | M |
| 10 | F-32 | Compliance + data layer alignment | M |

---

## 7. Aggregate by Severity & Effort

| | XS | S | M | L | XL | Total |
|---|---|---|---|---|---|---|
| **P0** | 1 | 0 | 1 | 0 | 0 | 2 |
| **P1** | 0 | 3 | 6 | 1 | 1 | 11 |
| **P2** | 2 | 5 | 7 | 2 | 3 | 19 |
| **P3** | 2 | 2 | 1 | 0 | 1 | 6 |
| **Total** | 5 | 10 | 15 | 3 | 5 | 38 |

---

## 8. Open Questions

| ID | Question | Where | Next step |
|----|----------|-------|-----------|
| OQ-1 | Are there findings in `src/legacy/*` that are unused dead code vs actively used? | grep imports | Triage; if dead, delete reduces debt by ~30% |
| OQ-2 | Is React 19 upgrade blocked by which 3rd-party deps? | check peer deps of all React-related libs | Inventory before scheduling F-22 |
| OQ-3 | Does customer SLA exist that bounds remediation timelines? | contract review | If yes, P1s with SLA tie-in escalate to P0 |
| OQ-4 | Are there any compliance audits planned in next 90 days? | engineering manager / legal | If yes, COMPLIANCE findings re-rank up |

## 9. Notes & Caveats

- **Categorization mode:** A — Standard 7 categories.
- **Mode rationale:** Codebase has no prior audit using its own categories.
- **Audit scope:** Ran automated scans (lint, type-check, npm audit, coverage). Manually reviewed top 5 largest files, all auth/billing services, all webhooks. NOT done: pen test, DB-level review (separate `data-architecture-audit`), full code review.
- **Severity discipline applied:** P0 limited to 2 (active CVE + token storage chain). Did NOT P0 things like "no MFA" — that's P1 latent risk.
- **Time spent:** 4 hours.
- **Confidence:** Medium-High.
```

---

## Calibration notes

- **2 P0 / 11 P1 / 19 P2 / 6 P3 distribution.** This is healthy. Most projects audit out to ~5-15% P0/P1, ~50-60% P2. If yours is 50% P0, you've inflated.
- **Top 10 sequencing prefers unblockers.** F-22 (React upgrade) is XL but ranked #3 because it gates other work. Pure severity ordering would put it later.
- **Clusters surface root causes.** Three findings about silent errors → one cluster, one fix. Avoids the trap of "37 separate tickets" when really it's 3 themes.
- **Don't move to fix design.** "Combined effort: M" is a sizing estimate, not a plan. The actual fix design happens in `tech-solution-design`.
