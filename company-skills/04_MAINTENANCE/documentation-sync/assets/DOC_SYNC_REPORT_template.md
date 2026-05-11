# {{PROJECT_NAME}} — Documentation Sync Report

> **Run date:** {{YYYY-MM-DD}}
> **Auditor:** {{NAME or AI agent run}}
> **Scope:** All docs in `docs/` + cross-reference to `src/`
> **Generated using:** `documentation-sync` skill v1
> **Previous run:** {{YYYY-MM-DD}} — see `_archive/DOC_SYNC_REPORT_<DATE>.md`
> **Next planned run:** {{YYYY-MM-DD}}

---

## 1. Executive Summary

**Overall doc health:** {{Healthy / Drift accumulating / Significant drift / Critical}}

**Numbers:**
- Total docs in `docs/`: {{N}}
- Docs reviewed in this run: {{N}}
- Findings: {{N}} ({{N_CRITICAL}} Critical, {{N_HIGH}} High, {{N_MED}} Medium, {{N_LOW}} Low)
- Trend vs last report: {{N_NEW}} new findings, {{N_RESOLVED}} resolved since last run

**Top concerns:**
1. {{ONE_LINE}}
2. {{ONE_LINE}}
3. {{ONE_LINE}}

---

## 2. Mode & Scope

**Sync check mode:** {{A — Standard / B — Honor company / C — User-defined}}

### Categories checked

| Category | Method | Findings |
|----------|--------|----------|
| Code reference (file paths) | Automated grep | {{N}} |
| Function reference | Automated grep | {{N}} |
| Config / env var reference | Automated grep | {{N}} |
| Schema reference | Manual + diff against current schema | {{N}} |
| Dependency reference | Compare to package.json | {{N}} |
| Process reference | Manual review / interview | {{N}} |
| Cross-doc reference (links) | Automated link check | {{N}} |
| Index drift | Diff INDEX.md vs filesystem | {{N}} |
| Stale data (stats, counts) | Manual sample + refresh | {{N}} |
| Authorial intent | Manual review | {{N}} |

### Categories NOT checked (and why)

- {{e.g., "API contract drift — no OpenAPI spec to validate against; flagged as systemic gap"}}

---

## 3. Findings

### Critical findings (immediate fix required)

| ID | Doc | Issue | Detection | Remediation | Owner | Target |
|----|-----|-------|-----------|-------------|-------|--------|
| DRIFT-C1 | {{e.g., docs/04_MAINTENANCE/runbooks/INCIDENT_DB.md}} | Cited command `psql -h primary.db` — host renamed to `primary.voyager-db.us-east-1.rds.amazonaws.com` 30 days ago; on-call would fail to connect during incident | Manual review | Update host name in 3 places in runbook | DBA on-call | {{YYYY-MM-DD (within 1 week)}} |
| DRIFT-C2 | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

### High findings (significantly out of date)

| ID | Doc | Issue | Detection | Remediation | Owner | Target |
|----|-----|-------|-----------|-------------|-------|--------|
| DRIFT-H1 | {{e.g., docs/INDEX.md}} | Missing 4 newly-created docs (FEAT_*.md from feature-extension work) | INDEX vs filesystem diff | Add entries to INDEX or run `document-index-master` skill | Doc maintainer | {{YYYY-MM-DD}} |
| DRIFT-H2 | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

### Medium findings (stale specifics)

| ID | Doc | Issue | Remediation | Owner |
|----|-----|-------|-------------|-------|
| DRIFT-M1 | {{e.g., docs/01_DISCOVERY/CODEBASE_MAP.md}} | LOC count says ~25K; current ~31K (+24% growth) | Refresh count; possibly run `codebase-discovery` to regenerate | Tech lead |
| DRIFT-M2 | {{...}} | {{...}} | {{...}} | {{...}} |

### Low findings (cosmetic)

| ID | Doc | Issue | Remediation | Owner |
|----|-----|-------|-------------|-------|
| DRIFT-L1 | {{e.g., docs/02_STRATEGIC/MASTER_PLAN.md}} | Typo "implementaton" line 47 | Spelling fix | Author |
| DRIFT-L2 | {{...}} | {{...}} | {{...}} | {{...}} |

---

## 4. Systemic Findings (Patterns)

Beyond per-doc findings, these reveal process gaps:

| Pattern | Evidence | Recommendation |
|---------|----------|----------------|
| {{e.g., "Index missing 4 of last 5 doc additions"}} | DRIFT-H1 + history | Make INDEX update part of doc-creation PR template |
| {{e.g., "Schema drift recurring; 3 of last 4 reports flagged it"}} | Cross-report comparison | Auto-generate schema doc from `pg_dump`; remove manual maintenance |
| {{e.g., "Process docs (runbooks) consistently stalest"}} | 6 of 14 findings in runbooks | Quarterly drill+update cycle for each runbook |

---

## 5. Coverage Statement

What was actually verified in this run:

- [x] All 27 docs in `docs/` opened (read at minimum once)
- [x] Automated link check ran (broken-links.txt produced)
- [x] Automated path-reference check ran (33 paths verified, 4 broken)
- [x] Automated env-var check ran
- [x] Schema docs spot-checked (5/8 sampled)
- [ ] Process runbooks: only 3/8 verified by current state interview (others flagged for next run)
- [ ] OpenAPI / contract docs: not checked (project has no formal API spec)

Confidence in this report: {{HIGH/MEDIUM/LOW}} based on coverage above.

---

## 6. Action Items (Tracked)

| Finding | Owner | Target | Status |
|---------|-------|--------|--------|
| DRIFT-C1 | DBA on-call | 2026-10-25 | Open |
| DRIFT-C2 | {{...}} | {{...}} | Open |
| DRIFT-H1 | Doc maintainer | 2026-10-30 | Open |
| ... | | | |

(Tracked in Jira / Linear: ticket numbers added once created.)

---

## 7. Resolved Since Last Report

(For trend tracking.)

| Finding ID (from prior report) | Resolution date | Notes |
|---------------------------------|-----------------|-------|
| DRIFT-H4 (prior) | 2026-09-15 | Index updated; no longer relevant |
| ... | | |

---

## 8. Notes & Caveats

- **Mode:** {{A / B / C}}
- **Time spent:** {{HOURS}}
- **Tools used:** {{e.g., grep, find, custom script `scripts/check-doc-links.sh`}}
- **Limitations:** {{What was out of scope; budget constraints}}

---

## 9. Recommendations

For sustained doc health:

1. {{e.g., "Make INDEX update mandatory in doc-creation PR template"}}
2. {{e.g., "Auto-generate schema doc; remove manual maintenance"}}
3. {{e.g., "Quarterly runbook drills with explicit doc-update step"}}

---

## 10. Next Run

- **Recommended frequency:** {{Monthly / Quarterly}}
- **Next run date:** {{YYYY-MM-DD}}
- **Triggered re-run:** if {{e.g., major release, audit prep}}

---

*Drift is normal. The goal is not zero drift; the goal is bounded drift with timely remediation.*
