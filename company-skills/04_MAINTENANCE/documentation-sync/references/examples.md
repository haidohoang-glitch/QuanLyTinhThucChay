# Documentation Sync — Worked Example

Anonymized. Fictional project: monthly sync run on a mid-size project with 27 docs.

## Context

**Imagined input:** "Run monthly sync on Project Voyager docs. Last sync 2026-09-20."

**Mode:** A.

**Time budget:** 4 hours (combination of automated + manual).

---

## Output excerpt

```markdown
# Project Voyager — Documentation Sync Report

> Run date: 2026-10-20
> Auditor: Lead Backend Engineer
> Scope: All 27 docs in `docs/` + cross-reference to `src/`
> Generated using: documentation-sync skill v1
> Previous run: 2026-09-20 → archived as `_archive/DOC_SYNC_REPORT_2026-09-20.md`
> Next planned run: 2026-11-20

## 1. Executive Summary

**Overall doc health:** Drift accumulating (manageable, but trending up)

**Numbers:**
- Total docs: 27
- Docs reviewed: 27 (full coverage this run)
- Findings: 14 (1 Critical, 4 High, 7 Medium, 2 Low)
- Trend vs last report: 9 new findings, 6 resolved since last run (last report had 11 open)

**Top concerns:**
1. **Critical:** DB host name in incident runbook is obsolete; on-call would fail to connect during incident
2. **High:** INDEX.md missing 4 of 4 newly-created feature spec docs
3. **High:** Schema doc shows obsolete `legacy_users` table (dropped 60 days ago)

## 2. Mode & Scope

Mode A — Standard 10-category checks.

| Category | Method | Findings |
|----------|--------|----------|
| Code reference (file paths) | Automated grep + existence check | 3 |
| Function reference | Automated grep | 1 |
| Config / env var | Automated grep + .env compare | 0 |
| Schema reference | Manual + diff vs `pg_dump` | 2 |
| Dependency reference | Compare to `package.json` | 1 |
| Process reference | Manual review (3 of 8 runbooks interviewed) | 2 |
| Cross-doc references (links) | Custom link check script | 1 |
| Index drift | INDEX vs filesystem diff | 1 |
| Stale data | Manual sample (5 docs) | 3 |
| Authorial intent | Manual | 1 |

### Categories partially checked

- Process docs: only 3/8 runbooks verified by interview this run; remaining 5 flagged for next run

---

## 3. Findings

### Critical findings

| ID | Doc | Issue | Detection | Remediation | Owner | Target |
|----|-----|-------|-----------|-------------|-------|--------|
| DRIFT-C1 | `docs/04_MAINTENANCE/runbooks/INCIDENT_POSTGRES_PRIMARY.md` | Cited host `primary.db` (line 47) — host renamed to `primary.voyager-db.us-east-1.rds.amazonaws.com` 30 days ago. On-call following runbook would fail to connect during incident. | Manual review during runbook spot-check | Update host name in 3 places in runbook (lines 47, 58, 74); also update related `INCIDENT_POSTGRES_REPLICA.md` (same issue) | DBA on-call | 2026-10-25 (within 1 week) |

### High findings

| ID | Doc | Issue | Detection | Remediation | Owner | Target |
|----|-----|-------|-----------|-------------|-------|--------|
| DRIFT-H1 | `docs/INDEX.md` | Missing entries for 4 newly-created feature specs: FEAT_BULK_EXPORT.md, FEAT_DARK_MODE.md, FEAT_2FA_OPTIONAL.md, FEAT_CSV_IMPORT.md | INDEX vs filesystem diff | Add entries to INDEX OR run `document-index-master` skill to regenerate | Doc maintainer | 2026-10-30 |
| DRIFT-H2 | `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` | Section 3 schema lists `legacy_users` table (dropped 2026-08-22 in WP-3.D) | Compare doc DDL vs `pg_dump --schema-only` | Remove `legacy_users` row; verify other tables still match current schema | Backend lead | 2026-10-30 |
| DRIFT-H3 | `docs/02_STRATEGIC/MASTER_PLAN.md` | Section 3 phase summary shows total effort 530h; current actuals after Phase 0+1 done = 412h remaining; doc never updated | Stat refresh | Update Section 3 with current vs planned remaining effort | Tech lead | 2026-11-01 |
| DRIFT-H4 | `docs/03_EXECUTION/work-packages/PHASE_2_DUAL_WRITE.md` | WP-2.B "Dual-Write Integration" references `OldUserService` class — class was renamed to `LegacyUserAdapter` 14 days ago (search confirms 0 references to old name in src/) | grep verify | Update WP-2.B section | Backend lead | 2026-10-25 |

### Medium findings

| ID | Doc | Issue | Remediation | Owner |
|----|-----|-------|-------------|-------|
| DRIFT-M1 | `docs/01_DISCOVERY/CODEBASE_MAP.md` | LOC count says ~25K; current ~31K (+24% growth in 60 days) | Refresh count via `find ... \| xargs wc -l`; also update file count | Tech lead |
| DRIFT-M2 | `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md` | F-08 (axios CVE) marked OPEN — actually closed in WP-0.B 14 days ago | Mark closed; update aggregate counts | QA lead |
| DRIFT-M3 | `docs/04_MAINTENANCE/runbooks/INCIDENT_PAYMENTS.md` | Cites Stripe SDK v8.x; current `package.json` shows v12.x; API surface different | Verify SDK API still applies; update if changed | Backend lead |
| DRIFT-M4 | `docs/QUICK_START.md` | Cites Node 18; current `.nvmrc` is Node 20 | Update to Node 20 | DevOps |
| DRIFT-M5 | `docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md` | Cost model uses Claude Opus 4 pricing; pricing shifted 2026-10-01; needs refresh | Update pricing in Section 1 + Section 6 cost projections | Operator |
| DRIFT-M6 | `docs/00_REQUIREMENTS/SRS_VI/M2_Mo_ta_tong_quan.md` | M2.4 Operating environment lists single region (us-east-1); architecture moved to multi-region per ADR-001 | Update to current state | Tech lead |
| DRIFT-M7 | `docs/01_DISCOVERY/red_team_audit_report.md` | Test coverage stat (38%) — current is 51% per latest CI | Refresh stat | QA lead |

### Low findings

| ID | Doc | Issue | Remediation | Owner |
|----|-----|-------|-------------|-------|
| DRIFT-L1 | `docs/02_STRATEGIC/MASTER_PLAN.md` | Typo "implementaton" line 47 | Spelling fix | Author |
| DRIFT-L2 | `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md` | Section 11 says "Last reviewed: 2026-08" — no date; should be specific | Refresh date | Operator |

---

## 4. Systemic Findings (Patterns)

| Pattern | Evidence | Recommendation |
|---------|----------|----------------|
| INDEX consistently lags doc creation (3rd report flagging it) | DRIFT-H1; same issue in last 3 reports | Make INDEX update mandatory in PR template for new doc creation; OR run `document-index-master` skill weekly via CI |
| Schema-related docs drift fastest (multiple findings) | DRIFT-H2, DRIFT-M6, multiple over time | Auto-generate schema doc from `pg_dump`; remove manual maintenance |
| Stat-based docs (LOC, coverage, costs) all stale | DRIFT-M1, M5, M7 | Add periodic refresh job; OR mark these as "approximate, updated quarterly" |
| Runbook drift highest where on-call has least DBA knowledge | DRIFT-C1, DRIFT-M3 | Quarterly drill of each runbook; update during drill |

---

## 5. Coverage Statement

What was verified:

- [x] All 27 docs opened (full coverage this run)
- [x] Automated link check (custom shell script): 1 broken internal link found (DRIFT-C1 also has external; resolved as runbook update)
- [x] Automated path-reference check ran: 3 paths verified missing (some quoted in comments only — false positives filtered)
- [x] Schema diff: `pg_dump --schema-only` compared to doc; 1 obsolete table found
- [x] Manual review of 3/8 runbooks (interview + walk-through)
- [ ] Manual review of remaining 5/8 runbooks: deferred to next run
- [ ] OpenAPI / API contract: project has no formal spec → flagged as systemic gap

Confidence in this report: **Medium-High**.

---

## 6. Action Items (Tracked)

| Finding | Owner | Target | Jira ticket | Status |
|---------|-------|--------|--------------|--------|
| DRIFT-C1 | DBA on-call | 2026-10-25 | VOY-1234 | Open |
| DRIFT-H1 | Doc maintainer | 2026-10-30 | VOY-1235 | Open |
| DRIFT-H2 | Backend lead | 2026-10-30 | VOY-1236 | Open |
| DRIFT-H3 | Tech lead | 2026-11-01 | VOY-1237 | Open |
| DRIFT-H4 | Backend lead | 2026-10-25 | VOY-1238 | Open |
| DRIFT-M1..M7 | various | 2026-11-15 (batch) | VOY-1239 (epic) | Open |
| DRIFT-L1, L2 | various | next sprint | (low priority — included in next docs PR) | Open |

---

## 7. Resolved Since Last Report

| Finding ID (Sept) | Resolution date | Notes |
|-------------------|-----------------|-------|
| DRIFT-H4 (Sept) | 2026-09-25 | INDEX update for backlog of 6 docs |
| DRIFT-M1 (Sept) | 2026-09-30 | Schema doc updated for `customers` table changes |
| DRIFT-M3 (Sept) | 2026-10-05 | Sentry DSN env var renamed in docs |
| DRIFT-M4 (Sept) | 2026-10-08 | LOC count refreshed (last refresh) |
| DRIFT-L1 (Sept) | 2026-10-10 | Typos cleaned up across 3 docs |
| DRIFT-L2 (Sept) | 2026-10-10 | Cosmetic header fix |

6 closed, 5 still open from prior report; 9 new this run → trend: backlog growing slightly.

---

## 8. Notes & Caveats

- **Mode:** A — Standard
- **Time spent:** 4 hours (1.5h automated check setup + run; 2.5h manual review + interviews)
- **Tools:**
  - Custom script `scripts/check-doc-paths.sh` for path verification
  - `scripts/check-doc-links.sh` for internal link verification
  - `pg_dump --schema-only` for schema comparison
  - Interview with DBA on-call for runbook accuracy (3 of 8 runbooks)
- **Limitations:**
  - Process docs only sampled (3/8 runbooks); next run cover remaining
  - No formal API spec in project → API drift undetectable

---

## 9. Recommendations

1. **Add INDEX-update gate to PR template:** PR creating new doc must update INDEX (or trigger `document-index-master` skill). Likely closes recurring DRIFT-INDEX issues.
2. **Auto-generate schema docs:** Replace manually maintained schema sections with `pg_dump --schema-only` output piped through a formatter. Fixes recurring schema drift.
3. **Quarterly runbook drills:** Each runbook drilled (tabletop or live) at least quarterly; update during drill. Catches runbook drift before incident.
4. **Stat refresh automation:** LOC, coverage, cost stats — set quarterly cron to refresh; alert if drift >20%.
5. **Track sync run quality:** Monitor closed-vs-new finding ratio; if >1 month >1.0 (more new than closed), team needs intervention.

---

## 10. Next Run

- **Recommended frequency:** Monthly (continue)
- **Next run date:** 2026-11-20
- **Triggered re-run:** Pre-SOC2 audit (target Q1 2027)
```

---

## Calibration notes

- **14 findings is realistic for monthly run on 27-doc project.** Zero findings would indicate inadequate review.
- **1 Critical only.** Don't inflate. Critical = "would cause incident if unfixed".
- **Patterns surface real process gaps.** Recurring INDEX issue → process change (PR template) more valuable than per-finding fix.
- **Coverage statement honest.** Says "5/8 runbooks not interviewed this run" — sets expectation for next run.
- **Resolved-vs-new tracking.** 6 closed, 9 new = backlog growing slightly. Concrete trend data, not just current snapshot.
- **Recommendations forward-looking.** Section 9 recommends process changes, not just per-finding fixes.
- **Time budget realistic.** 4 hours for 27 docs ≈ 9 min/doc average; matches actual sustainable cadence.
