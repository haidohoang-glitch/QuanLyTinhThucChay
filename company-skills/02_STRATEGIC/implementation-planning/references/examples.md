# Implementation Planning — Worked Example

Anonymized. Fictional project: **"Project Voyager"** — a logistics tracking platform migrating from a single-region monolith to a multi-region distributed system. Mode A (standard 5-phase migration template).

## Context

**Imagined input:** "Plan the Voyager migration. We have TECH_SOLUTION_DESIGN, FEASIBILITY ($120K budget, 12 weeks), TECH_DEBT_AUDIT (47 findings, 3 P0)."

**Time budget for plan creation:** 6 hours.

**Team:** 3 backend devs + 1 DevOps + 1 QA, full-time.

---

## MASTER_PLAN.md (excerpt)

```markdown
# Project Voyager — Master Implementation Plan

> Generated using: implementation-planning skill v1
> Last updated: 2026-05-08

## 1. Goal & Scope

**Goal:** Migrate Voyager from single-region monolith (us-east-1) to multi-region
distributed architecture (us-east-1 primary, eu-west-1 read replica) without losing
data or impacting active customer SLAs.

**Constraints:**
- Budget: $120K (~960 dev-hours including coordination)
- Deadline: 12 calendar weeks (hard — board commitment to EU customers)
- Headcount: 3 BE + 1 DevOps + 1 QA, full-time
- Must not break: existing API contract, 99.9% uptime SLA, US data residency for US customers

**Success criteria:**
1. EU customers can read order data from EU region with <100ms p95 latency, by Week 12
2. Migration completes with zero data loss (verified via reconciliation report)
3. No more than 1 customer-facing incident with >15min impact during migration
4. All P0 findings from TECH_DEBT_AUDIT closed by Phase 0 end

**Out of scope:**
- Active-active write region (this plan is active-passive)
- Data sovereignty enforcement (separate compliance project)
- Frontend SPA migration (different team, different repo)

## 2. Phase Decomposition Mode

Mode A — Standard 5-phase migration template (see Section 8).

## 3. Phase Summary

| Phase | Name | WP count | Effort (hrs) | Calendar (days) | Gate |
|-------|------|----------|--------------|-----------------|------|
| 0 | Pre-Flight | 7 | 88 | 8-10 | Gate 0 |
| 1 | Quick Wins | 5 | 56 | 6-7 | Gate 1 |
| 2 | Dual-Write | 8 | 188 | 18-22 | Gate 2 |
| 3 | Switch Reads | 5 | 102 | 10-12 | Gate 3 |
| 4 | Compliance + Decommission | 6 | 96 | 9-11 | Gate 4 |
| **Total** | | **31** | **530** | **51-62** | |

With 5-person team, parallelism factor 0.55 → ~10 calendar weeks. Plus 20% review/QA → 12 weeks. ✅ Matches deadline.

## 4. Dependency Graph

### High-level

```
Phase 0 ──────► Phase 1 ──────► Phase 2 ──────► Phase 3 ──────► Phase 4
                  │                │
                  └ may overlap ──┘ (Phase 1 cleanup runs while Phase 2 builds)
```

### Cross-phase WP dependencies

| WP | Depends on | Type |
|----|------------|------|
| WP-2.A (Multi-region DB cluster) | WP-0.D (Terraform module skeleton) | Hard |
| WP-2.D (CDC pipeline) | WP-2.A, WP-0.F (Observability) | Hard |
| WP-3.A (Read flip in eu-west-1) | All Phase 2 WPs | Hard |
| WP-3.B (Gradual rollout config) | WP-2.H (Feature flag system) | Hard |
| WP-4.A (Decommission old replica) | WP-3.A complete + 7 days clean | Hard (time gate) |

## 5. Risks & Mitigations

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| RP-01 | EU region capacity unavailable from cloud provider during plan | L | H | Reserve capacity Week 0; fallback region eu-central-1 identified |
| RP-02 | CDC stream lag exceeds RPO during high-traffic event | M | H | Plan Phase 2 outside Black Friday/Q4; load-test CDC at 5x traffic |
| RP-03 | Reconciliation reveals data divergence > 0.1% | M | M | Pause Phase 3; root-cause within 5 days; extend timeline if needed |
| RP-04 | Key engineer (only Postgres replication expert) leaves | L | H | Pair-program WP-2.A and WP-2.D; document decisions thoroughly |
| RP-05 | Phase 2 budget overrun (most expensive phase) | M | M | Phase 2 has explicit checkpoint at 50% effort; abort to dual-write paused state |

## 6. Verification Gates

### Gate 0 — End of Pre-Flight
- [ ] All 3 P0 findings from TECH_DEBT_AUDIT closed
- [ ] CI green for 5 consecutive runs across BE + DevOps repos
- [ ] Sentry capturing errors in production with <1% sampling drop
- [ ] EU region Terraform module deployed (skeleton only, no traffic)
- [ ] Test framework supports multi-region scenarios (`npm run test:multi-region` works)

### Gate 1 — End of Quick Wins
- [ ] DB connection pool tunable via env var (no hardcoded `5`)
- [ ] All `/api/orders/*` endpoints have pagination (limit ≤ 100)
- [ ] Sentry alerts wired to PagerDuty for P1+ severities
- [ ] Phase 1 PRs merged with no production rollback needed

### Gate 2 — End of Dual-Write
- [ ] CDC pipeline replicating us-east-1 → eu-west-1 with <30s lag p95 for 7 consecutive days
- [ ] Reconciliation cron runs hourly with <0.01% drift across critical tables (orders, shipments, customers)
- [ ] Feature flag system in place (WP-2.H) with documented kill switches
- [ ] Manual chaos test: simulate eu-west-1 outage; us-east-1 keeps serving normally

### Gate 3 — End of Switch Reads
- [ ] EU customers' read traffic served from eu-west-1 (verified via X-Region header logs)
- [ ] p95 read latency for EU customers < 100ms (Week 1 average)
- [ ] No data divergence detected in 7 days post-cutover
- [ ] Rollback feature flag tested in staging within 7 days of cutover

### Gate 4 — End (Final)
- [ ] Old replica decommissioned (us-west-2 — not used in new architecture)
- [ ] GDPR right-to-export endpoint covers both regions
- [ ] DR drill executed: simulate us-east-1 loss; eu-west-1 promoted; documented RTO/RPO
- [ ] Postmortem documents written for any incidents during migration

## 7. Rollback Strategy (Plan-level)

| Phase reached | Rollback approach |
|---------------|-------------------|
| Phase 0 only | Revert PRs in reverse order; safe |
| Phase 1 done | Revert Phase 1; safe |
| Phase 2 in progress | Disable dual-write feature flag; CDC pipeline stops; new region has stale data (acceptable) |
| Phase 3 mid-cutover | Flip rollout % back to 0 (US-only reads); verify in eu-west-1 logs |
| Phase 3 fully cut over | Re-flip flag to 0; eu-west-1 falls back to read-only orphan; investigate before retry |
| Phase 4 mid-decommission | DO NOT decommission until Phase 3 stable for 30 days; if abort needed before then, halt decommission scripts |

## 8. Notes & Caveats

- **Phase decomposition mode:** A — Standard 5-phase migration.
- **Mode rationale:** Migration of state-bearing system → standard template fits exactly.
- **Inputs read:** TECH_SOLUTION_DESIGN ✅, FEASIBILITY ✅, TECH_DEBT_AUDIT ✅, DATA_ARCHITECTURE ✅, CODEBASE_MAP ⚠️ (out of date — refreshed during planning)
- **Time spent on plan:** 6 hours (3h reading inputs + 3h writing).
- **Confidence:** Medium-High. Phase 2 (most complex) has 4 high-effort WPs; if any blow up, plan slips by 1-2 weeks.

## 9. Open Questions

| ID | Question | Next step |
|----|----------|-----------|
| OQ-1 | Does Postgres logical replication support our schema (LARGE OBJECT in `documents` table)? | Spike in Phase 0 (WP-0.G) |
| OQ-2 | Will EU customer % grow during plan? Baseline assumes static | Confirm with sales forecast |
| OQ-3 | Are there contractual penalties for incidents > 15min during plan? | Legal review |

## 10. Quick Reference

- Per-phase WPs: `docs/03_EXECUTION/work-packages/PHASE_<N>_<NAME>.md`
- Test infrastructure: `docs/03_EXECUTION/00_TESTING_INFRASTRUCTURE.md`
- AI operator guide: `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md`
- Rollback runbook: `docs/04_MAINTENANCE/runbooks/C_ROLLBACK_RUNBOOK.md`
```

---

## PHASE_0_PRE_FLIGHT.md (excerpt)

```markdown
# Phase 0 — Pre-Flight

> Purpose: Remove blockers; build foundation for multi-region migration.
> WPs: 7 | Total effort: 88 hrs | Calendar: 8-10 days | Gate 0

## Context

Phase 0 exists because the multi-region migration cannot begin while:
1. Three P0 security findings exist (token storage, CVE, missing rate limit)
2. CI has flaky tests masking real failures
3. EU region infrastructure has not been provisioned at all
4. Test framework cannot exercise multi-region scenarios

Without Phase 0, every subsequent phase has hidden risk.

## WP Sequence

```
Day 1-2: WP-0.A, WP-0.B, WP-0.D (parallel)
Day 3:   WP-0.C (depends on A)
Day 4-5: WP-0.E (depends on B), WP-0.F (parallel)
Day 6-8: WP-0.G (spike), WP-0.0 (server restructure)
```

| WP | Depends on | Parallelizable | Effort |
|----|------------|----------------|--------|
| WP-0.A | (none) | B, D | M (2 days) |
| WP-0.B | (none) | A, D | S (1 day) |
| WP-0.C | WP-0.A | — | S |
| WP-0.D | (none) | A, B | M (2 days) |
| WP-0.E | WP-0.B | F | S |
| WP-0.F | (none) | E | M (2 days) |
| WP-0.G | (none, spike) | — | S (time-boxed 1 day) |

---

### WP-0.A — Replace localStorage token storage with httpOnly cookies

**Goal:** Remove XSS-vulnerable token storage; switch to httpOnly secure cookies for auth.
**Effort:** M (2 days)
**Owner:** Backend dev (lead) + Frontend dev (consume)
**Dependencies:** (none)

**Background:** TECH_DEBT_AUDIT F-03 (P0). XSS surface present in F-22 makes this chained risk active.

**Files affected:**
- `src/server/middleware/auth.ts` — change cookie setting (Modify)
- `src/server/routes/auth.ts` — login response stops returning token in body (Modify)
- `src/api/client.ts` — frontend stops reading localStorage; relies on cookie auto-attach (Modify)
- `src/components/AuthGuard.tsx` — adjust loading state (Modify)
- `tests/integration/auth.spec.ts` — new test cases (Modify)
- `migrations/20260508_session_table.sql` — server-side session storage (Create)

**Acceptance criteria:**
- [ ] localStorage no longer contains any auth-related keys after login (verified by browser inspector)
- [ ] Cookie set with `HttpOnly`, `Secure`, `SameSite=Lax`, `Path=/api`
- [ ] Existing logged-in users are migrated (server accepts old token-in-header for 30 days, then rejects)
- [ ] CSRF protection added (`X-CSRF-Token` header validated on state-changing endpoints)
- [ ] Test `auth.spec.ts → 'rejects request without CSRF token'` passes
- [ ] Test `auth.spec.ts → 'old localStorage token rejected after migration window'` passes

**Unit tests:**
- `should set httpOnly cookie on successful login` — `tests/unit/auth.test.ts`
- `should reject token in Authorization header after grace period` — `tests/unit/auth.test.ts`
- `should require X-CSRF-Token on POST/PUT/DELETE` — `tests/unit/csrf.test.ts`

**Manual test cases:**
- TC-0A-01: Log in via UI → check Application tab → no `token` in localStorage; cookie set with HttpOnly flag.
- TC-0A-02: Try to read `document.cookie` from DevTools console → cookie not visible (HttpOnly works).
- TC-0A-03: Capture login request via Burp → tamper response to remove cookie → frontend rejects subsequent requests.
- TC-0A-04: Use stale token from before deploy → first 30 days: accepted with deprecation warning; after: rejected with 401.

**Risks:**
- Cookie domain misconfig in multi-region setup → users logged out after region failover. Mitigation: set Domain=`.voyager.com`; verify in staging multi-region test.
- CSRF implementation breaks legacy mobile app (uses old auth). Mitigation: API version flag; mobile app upgrade scheduled separately.

**Rollback plan:**
1. Revert frontend deploy first (frontend can read both cookie and localStorage during transition)
2. Revert backend deploy (token-in-header path still works for 30 days)
3. If session table caused issue: `DROP TABLE sessions;` + restart server (sessions invalid → users re-login)

**PR title format:**
`[Phase 0][WP-0.A] Migrate auth to httpOnly cookies + CSRF`

---

### WP-0.B — Upgrade axios to ^1.6 (CVE-2023-45857)

**Goal:** Close the high-severity CVE in `axios@0.21.1`.
**Effort:** S (4 hrs)
**Owner:** Backend dev
**Dependencies:** (none)

**Files affected:**
- `package.json` — bump axios version (Modify)
- `package-lock.json` — regenerated (Modify)
- 14 source files using axios — verify API compatibility (Modify if needed)
- `tests/integration/external-calls.spec.ts` — extend to verify timeout behavior (Modify)

**Acceptance criteria:**
- [ ] `npm audit` shows 0 high-severity findings related to axios
- [ ] All existing tests pass after upgrade (no API break)
- [ ] New axios timeout default (10s) tested explicitly

**Unit tests:**
- `axios calls have explicit timeout < 10s` — `tests/unit/api-client.test.ts`

**Manual test cases:**
- TC-0B-01: Hit `/api/orders/sync-from-vendor` with vendor mocked to delay 30s → request fails after 10s with timeout error.

**Risks:** Low — axios v1 is mostly backwards compatible; verify any `axios.create(config)` usages.

**Rollback plan:** `git revert <commit>`; redeploy.

**PR title:** `[Phase 0][WP-0.B] Upgrade axios to v1.6 (close CVE)`

---

(WPs 0.C through 0.G + 0.0 omitted for brevity)

---

## Phase Verification Gate

Cannot proceed to Phase 1 until ALL of:
- [ ] WP-0.A through WP-0.G + WP-0.0 all merged
- [ ] All 3 P0 findings (F-03, F-08, F-XX) closed
- [ ] CI green for 5 consecutive runs
- [ ] Sentry receiving events from production with <1% drop
- [ ] EU region Terraform skeleton deployed; `terraform plan` is clean
- [ ] `npm run test:multi-region` runs green (even if no real multi-region traffic yet)
```

---

## Calibration notes

- **WP sizing.** WP-0.A is M (2 days) because it touches multiple layers (server, client, DB) AND requires migration logic for existing users. If it were just "set HttpOnly flag", it'd be S.
- **Acceptance criteria are observable.** Every checkbox is something you can verify by reading code, browser inspector, or test output. No "improves security posture".
- **Risks are specific.** Not "may break things" — specific scenarios with mitigations.
- **Rollback is mechanical.** Steps a non-author engineer could execute at 2am.
- **Phase 0 includes a spike.** WP-0.G (logical replication compatibility check) is a time-boxed investigation. Not all WPs deliver code; some deliver knowledge that unblocks later WPs.
- **Verification gate is non-negotiable.** "Phase 1 starts at Day 11 if Gate 0 passes; otherwise we slip and document why."
- **Calendar honest.** 88 hours of effort with 5 people is not 88/5 = 18 hours of calendar; it's 8-10 days because of coordination, review, parallel-blockers. Don't pretend perfect parallelism.
