# Document Consistency Review — Worked Example

Anonymized. Quarterly review on a 31-doc project (Project Voyager).

## Context

**Imagined input:** "Run quarterly consistency review on Voyager docs. Last review 2026-07-15."

**Mode:** A.

**Time budget:** 6 hours.

---

## Output excerpt

```markdown
# Project Voyager — Cross-Document Consistency Review

> Run date: 2026-10-22
> Auditor: Tech Lead
> Scope: All 31 docs in `docs/`
> Generated using: document-consistency-review skill v1
> Previous run: 2026-07-15
> Next planned run: 2027-01-22

## 1. Executive Summary

**Overall consistency:** Minor inconsistencies (manageable; trending neutral)

**Numbers:**
- Total docs reviewed: 31 (full coverage)
- Findings: 18 (1 Critical, 5 High, 9 Medium, 3 Low)
- Trend vs last report: 11 new, 8 resolved (last had 15)

**Top concerns:**
1. **Critical:** WP-2.B status conflict (Done in PHASE doc, In progress in MASTER_PLAN) → may have stakeholders confused about phase progress
2. **High:** "Customer" vs "User" vs "Account" terminology inconsistency across SRS modules
3. **High:** Broken cross-references: 3 docs link to `PROGRESS_TRACKER.md` which doesn't exist

## 2. Mode & Scope

Mode A — 8 dimensions.

| # | Dimension | Findings |
|---|-----------|----------|
| 1 | Terminology | 6 |
| 2 | Numbers | 4 |
| 3 | References | 3 |
| 4 | Versioning | 2 |
| 5 | Owners | 0 |
| 6 | Decisions (ADRs) | 1 |
| 7 | Status | 1 (the Critical) |
| 8 | Glossary | 1 |

### Coverage
- Automated: link checker, terminology extraction
- Manual: ADR consistency, status spot-check
- Skipped: per-WP test count (relegated to RTM skill)

## 3. Findings

### Critical findings

| ID | Conflict | Docs involved | Canonical | Remediation | Owner | Target |
|----|----------|---------------|-----------|-------------|-------|--------|
| INC-C1 | WP-2.B "Dual-Write Integration" status: MASTER_PLAN says "In progress" (Section 3 row); PHASE_2_DUAL_WRITE.md WP-2.B section says "Done" (operator updated PHASE doc but not MASTER) | MASTER_PLAN.md (Section 3, row WP-2.B); PHASE_2_DUAL_WRITE.md (WP-2.B header) | PHASE doc (operator's authoritative status update) | Update MASTER_PLAN row to "Done" + adjust phase progress percentage | PM | 2026-10-25 |

### High findings

| ID | Conflict | Docs involved | Remediation | Owner | Target |
|----|----------|---------------|-------------|-------|--------|
| INC-H1 | "Customer" (BUSINESS_CONTEXT, M4 SRS) vs "User" (M3 SRS) vs "Account" (CODEBASE_MAP) — same entity referenced differently | M3 SRS (lines 24, 47, 89); M4 SRS (lines 12, 33); BUSINESS_CONTEXT.md Section 5; CODEBASE_MAP.md Section 4 | Adopt "Customer" (per BUSINESS_CONTEXT primary); update M3 SRS + CODEBASE_MAP; add to glossary | Tech Lead | 2026-11-05 |
| INC-H2 | "Tenant" (M2.3) vs "Workspace" (M8.1) vs "Organization" (CODEBASE_MAP) — same entity | M2 SRS (line 88); M8 SRS (line 14); CODEBASE_MAP.md (Section 4 row) | Adopt "Tenant" (per industry standard); update M8 SRS + CODEBASE_MAP | Tech Lead | 2026-11-05 |
| INC-H3 | Cross-reference broken: 3 docs link to `docs/03_EXECUTION/PROGRESS_TRACKER.md` which doesn't exist | AI_OPERATOR_GUIDE.md (line 47); QUICK_START.md (line 65); MASTER_PLAN.md (Section 8) | Either create PROGRESS_TRACKER.md (template available in operator guide) OR remove references | Operator | 2026-10-30 |
| INC-H4 | ADR-001 status: TECH_SOLUTION_DESIGN says "Approved 2026-09-05"; MASTER_PLAN preface says "Proposed" | TECH_SOLUTION_DESIGN.md (Section 5); MASTER_PLAN.md (preface) | TECH_SOLUTION_DESIGN authoritative (per ADR convention); update MASTER_PLAN | Tech Lead | 2026-10-30 |
| INC-H5 | Effort estimate for Phase 2: MASTER_PLAN says "~150 hours"; FEASIBILITY_ASSESSMENT scenario PARTIAL says "~120 hours"; PHASE_2 doc effort sum is "~140 hours" | MASTER_PLAN.md (Section 3); FEASIBILITY_ASSESSMENT.md (Scenario PARTIAL); PHASE_2_DUAL_WRITE.md (effort table) | Recompute from PHASE_2 actual WP estimates; align other docs | PM | 2026-11-01 |

### Medium findings

| ID | Conflict | Docs | Remediation | Owner |
|----|----------|------|-------------|-------|
| INC-M1 | Postgres version: DATA_ARCH says v15; CODEBASE_MAP says v15.4; PHASE_0 says v15 | DATA_ARCH, CODEBASE_MAP, PHASE_0 | Use major.minor format consistently (v15.4 fully precise); update DATA_ARCH and PHASE_0 | Tech Lead |
| INC-M2 | Sentry plan tier: PHASE_0 says "Team plan"; AI_OPERATOR_GUIDE says "Pro plan" | PHASE_0_*.md, AI_OPERATOR_GUIDE.md | Verify current; update incorrect doc | DevOps |
| INC-M3 | Number of WPs total: MASTER_PLAN says 31; FEASIBILITY says 30; INDEX says 31 | MASTER_PLAN, FEASIBILITY, INDEX | 31 is correct (after WP-3.B added in Phase 2); update FEASIBILITY | PM |
| INC-M4 | Compliance reviewer name: SRS M2.5 says "Diana L."; FEAT_BULK_EXPORT says "Diana L."; FEAT_2FA_OPTIONAL says "Diane L." | FEAT_2FA_OPTIONAL.md | Spelling fix in FEAT_2FA | Author |
| INC-M5 | "BullMQ" capitalized differently across docs ("Bull MQ", "BullMQ", "bull-mq") | various | Standardize on "BullMQ" (vendor's official) | Doc maintainer |
| INC-M6 | NFR-PERF-01 target: M9 says "p95 ≤ 500ms"; PHASE_3 perf test target says "p95 ≤ 600ms" | M9, PHASE_3 | M9 authoritative; update PHASE_3 | Tech Lead |
| INC-M7 | Budget figure: FEASIBILITY says "$480K"; MASTER_PLAN preface says "~$500K" | FEASIBILITY, MASTER_PLAN | Use $480K consistently (per board commitment) | PM |
| INC-M8 | "Stripe" vs "stripe" usage inconsistency | various | Capitalize when referring to company/product | Doc maintainer |
| INC-M9 | New term "saga pattern" introduced in TECH_SOLUTION_DESIGN; not in glossary | TECH_SOLUTION_DESIGN.md, INDEX.md (Section 6) | Add to glossary | Doc maintainer |

### Low findings

| ID | Conflict | Docs | Remediation | Owner |
|----|----------|------|-------------|-------|
| INC-L1 | "Sign in" vs "Login" vs "Log in" inconsistency in UI strings docs | various | Standardize on "Sign in" | UX |
| INC-L2 | Date format: "2026-09-15" vs "Sept 15, 2026" vs "15/09/2026" | various | ISO format (YYYY-MM-DD) per company style | Doc maintainer |
| INC-L3 | Trailing whitespace and inconsistent heading levels in 4 docs | various | Auto-fix via prettier | Doc maintainer |

---

## 4. Terminology Audit

| Variants found | Locations | Recommended canonical |
|----------------|-----------|------------------------|
| "User" / "Customer" / "Account" / "Account holder" | M3, M4, M5, M6 SRS; CODEBASE_MAP; BUSINESS_CONTEXT | **"Customer"** (BUSINESS_CONTEXT) |
| "Tenant" / "Workspace" / "Organization" | M2, M8 SRS; CODEBASE_MAP | **"Tenant"** |
| "Sign in" / "Login" / "Log in" / "Authenticate" | UI strings (various); API docs | UI: **"Sign in"**; API docs: **"authenticate"** |
| "BullMQ" / "Bull MQ" / "bull-mq" | various | **"BullMQ"** |
| "saga pattern" — new term not in glossary | TECH_SOLUTION_DESIGN.md | Add to glossary |

---

## 5. Reference Validity

| Reference type | Total | Valid | Broken |
|----------------|-------|-------|--------|
| Internal markdown links | 47 | 44 | 3 (INC-H3) |
| File path citations | 89 | 85 | 4 (mostly path drift; covered in DOC_SYNC report) |
| FR/NFR ID citations | 156 | 156 | 0 |
| ADR citations | 12 | 12 | 0 |
| External URL links | 23 | 21 | 2 (vendor doc URL changed; non-blocking) |

---

## 6. Version & Status Consistency

### Component versions

| Component | Documented | Discrepancy |
|-----------|------------|-------------|
| Postgres | v15 (some), v15.4 (some) | INC-M1 |
| Node.js | v20 | None |
| React | v19 | None |
| BullMQ | v5.x | None |
| Stripe SDK | v12.x | None |

### Status consistency

| Item | Doc A status | Doc B status | Action |
|------|--------------|--------------|--------|
| WP-2.B | "In progress" (MASTER_PLAN) | "Done" (PHASE_2 doc) | INC-C1 |
| ADR-001 | "Approved" (TSD) | "Proposed" (MASTER preface) | INC-H4 |
| WP-1.E | "Done" (both) | — | OK |

---

## 7. Decisions Reflected

| Decision (ADR) | Should appear in | Actually appears in | Gap |
|-----------------|-------------------|----------------------|-----|
| ADR-001 (Multi-region active-passive) | TECH_SOLUTION_DESIGN, MASTER_PLAN, PHASE_2/3, DATA_ARCHITECTURE | TSD ✅, MASTER_PLAN ⚠️ (status mismatch INC-H4), PHASE_2/3 ✅, DATA_ARCHITECTURE ❌ (no mention) | Update DATA_ARCHITECTURE per ADR-001 |
| ADR-002 (Stripe-only payments) | TSD, M6 SRS, PHASE_0 | All ✅ | None |

---

## 8. Action Items

| Finding | Owner | Target | Jira |
|---------|-------|--------|------|
| INC-C1 | PM | 2026-10-25 | VOY-1240 |
| INC-H1 | Tech Lead | 2026-11-05 | VOY-1241 |
| INC-H2 | Tech Lead | 2026-11-05 | VOY-1242 |
| INC-H3 | Operator | 2026-10-30 | VOY-1243 |
| INC-H4 | Tech Lead | 2026-10-30 | VOY-1244 |
| INC-H5 | PM | 2026-11-01 | VOY-1245 |
| INC-M1..M9 | various | 2026-11-15 batch | VOY-1246 (epic) |
| INC-L1..L3 | various | next sprint | (low priority) |

---

## 9. Resolved Since Last Report

| Prior finding | Resolved | Notes |
|---------------|----------|-------|
| INC-H3 (Jul) | 2026-08-10 | Cleaned up "FR" ID inconsistency in M4 SRS |
| INC-M1 (Jul) | 2026-09-01 | Sentry version updated in 3 docs |
| INC-M2 (Jul) | 2026-09-15 | Postgres SDK references aligned |
| (5 more) | | |

---

## 10. Patterns / Systemic Findings

| Pattern | Evidence | Recommendation |
|---------|----------|----------------|
| WP status drifts between MASTER_PLAN and PHASE docs (recurring 2 of 3 reports) | INC-C1 + history | **Single source of truth**: PHASE doc owns WP status; MASTER_PLAN auto-aggregates (script). Manual MASTER_PLAN update no longer required |
| New terminology introduced without glossary update (recurring) | INC-M9 + others | **PR template question**: "New terminology? Add to glossary?" |
| Stat / number discrepancies (effort estimates, costs, counts) | INC-H5, INC-M3, INC-M7 | **Single source of truth**: numbers reside in MASTER_PLAN; FEASIBILITY references it. Don't duplicate |

---

## 11. Notes

- **Mode:** A — Standard 8-dimension
- **Time spent:** 6 hours
- **Tools:** Custom script `scripts/check-doc-links.sh`; manual terminology extraction
- **Limitations:** Did not audit FEAT_*.md docs in 04_MAINTENANCE deeply (sample only)
- **Confidence:** Medium-High

---

## 12. Recommendations

1. **WP status: PHASE doc is source of truth.** MASTER_PLAN auto-aggregates via script. Removes ongoing INC-C1 drift.
2. **Terminology PR gate.** When PR introduces new terminology, must add to glossary AND verify no synonym already exists. Catches INC-H1, H2, M9 patterns.
3. **Numbers single source of truth.** Effort, cost, count numbers in MASTER_PLAN; other docs reference (don't duplicate). Reduces INC-H5, M3, M7 patterns.
4. **Quarterly cadence works.** 18 findings is normal range; running monthly would over-spend time.
5. **Combine with sync skill once?** Discuss whether single quarterly "Doc Health" report combining sync + consistency is more efficient.

---

## 13. Next Run

- **Next:** 2027-01-22
- **Triggered re-run:** before SOC2 audit prep (target Q1 2027)
```

---

## Calibration notes

- **18 findings is normal.** Zero findings would suggest under-thoroughness; 50+ would suggest cultural process issue.
- **1 Critical only.** Status conflict in WP-2.B is real (stakeholders may misread progress); not "feels critical".
- **Terminology section gold.** Section 4 surfaces the most subtle drift; auditors notice these immediately.
- **Patterns drive recommendations.** Recurring "WP status drift" → recommend single-source-of-truth solution, not just per-finding fix.
- **Resolved findings show progress.** 8 resolved since July → trend is healthy (closing > new × buffer).
- **References to other reports.** "Combine with sync skill" → recognizes overlap; offers efficiency gain.
- **Coverage statement honest.** Notes FEAT docs only sampled — sets expectation.
