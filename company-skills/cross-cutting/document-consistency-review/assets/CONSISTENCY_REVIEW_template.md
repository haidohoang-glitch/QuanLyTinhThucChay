# {{PROJECT_NAME}} — Cross-Document Consistency Review

> **Run date:** {{YYYY-MM-DD}}
> **Auditor:** {{NAME or AI agent}}
> **Scope:** All docs in `docs/`
> **Generated using:** `document-consistency-review` skill v1
> **Previous run:** {{YYYY-MM-DD}} — see `_archive/CONSISTENCY_REVIEW_<DATE>.md`
> **Next planned run:** {{YYYY-MM-DD}}

---

## 1. Executive Summary

**Overall consistency:** {{Healthy / Minor inconsistencies / Significant conflicts / Critical}}

**Numbers:**
- Total docs reviewed: {{N}}
- Findings: {{N}} ({{N_CRITICAL}} Critical, {{N_HIGH}} High, {{N_MED}} Medium, {{N_LOW}} Low)
- Trend vs last report: {{N_NEW}} new, {{N_RESOLVED}} resolved

**Top concerns:**
1. {{ONE_LINE}}
2. {{ONE_LINE}}
3. {{ONE_LINE}}

---

## 2. Mode & Scope

**Review mode:** {{A — Standard 8-dim / B — Honor company / C — User-defined}}

### Dimensions checked

| # | Dimension | Findings |
|---|-----------|----------|
| 1 | Terminology | {{N}} |
| 2 | Numbers (counts, dates, costs) | {{N}} |
| 3 | References (links, citations) | {{N}} |
| 4 | Versioning (component versions) | {{N}} |
| 5 | Owners / contacts | {{N}} |
| 6 | Decisions (ADRs reflected consistently) | {{N}} |
| 7 | Status (phase, WP, FR statuses) | {{N}} |
| 8 | Glossary (term definitions and usage) | {{N}} |

### Coverage

- Automated: {{LIST_OF_AUTOMATED_CHECKS}}
- Manual: {{LIST_OF_MANUAL_REVIEWS}}
- Skipped: {{LIST_OF_SKIPPED_AND_REASON}}

---

## 3. Findings

### Critical findings

(Conflicts that affect decisions or commitments)

| ID | Conflict | Docs involved | Canonical source | Remediation | Owner | Target |
|----|----------|---------------|------------------|-------------|-------|--------|
| INC-C1 | {{e.g., MASTER_PLAN says timeline 14 weeks; FEASIBILITY says 12 weeks; stakeholder commitment is 14 weeks per board minutes}} | MASTER_PLAN.md (line 27); FEASIBILITY_ASSESSMENT.md (line 14) | MASTER_PLAN.md (board confirmed) | Update FEASIBILITY to 14 weeks; revise scenario calculations | PM | {{YYYY-MM-DD}} |
| INC-C2 | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

### High findings

(Significant inconsistency; broken references)

| ID | Conflict | Docs involved | Remediation | Owner | Target |
|----|----------|---------------|-------------|-------|--------|
| INC-H1 | {{e.g., "User" used in M3 SRS; "Customer" in M4-M6 SRS; "Account" in CODEBASE_MAP — same entity}} | M3, M4, M5, M6 SRS; CODEBASE_MAP.md | Adopt "Customer" (per BUSINESS_CONTEXT); update M3 SRS + CODEBASE_MAP | Tech Lead | {{YYYY-MM-DD}} |
| INC-H2 | {{e.g., Broken cross-reference: AI_OPERATOR_GUIDE links to docs/03/PROGRESS_TRACKER.md which doesn't exist}} | AI_OPERATOR_GUIDE.md (line 47) | Either create PROGRESS_TRACKER.md OR update reference | Operator | {{YYYY-MM-DD}} |
| INC-H3 | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

### Medium findings

(Localized; doesn't affect overall message)

| ID | Conflict | Docs involved | Remediation | Owner |
|----|----------|---------------|-------------|-------|
| INC-M1 | {{e.g., MASTER_PLAN cost estimate $480K; PHASE 0 doc cost $475K; rounding mismatch}} | MASTER_PLAN.md, PHASE_0_*.md | Round consistently (to $5K); update one | PM |
| INC-M2 | {{e.g., Postgres v15 in DATA_ARCH; v15.4 in CODEBASE_MAP — same major version, different patch}} | DATA_ARCHITECTURE.md, CODEBASE_MAP.md | Use major version only (v15) consistently | Tech Lead |
| INC-M3 | {{...}} | {{...}} | {{...}} | {{...}} |

### Low findings

| ID | Conflict | Docs | Remediation | Owner |
|----|----------|------|-------------|-------|
| INC-L1 | {{e.g., "git mv" capitalized differently across docs}} | various | Standardize on lowercase | Doc maintainer |
| INC-L2 | {{...}} | {{...}} | {{...}} | {{...}} |

---

## 4. Terminology Audit (special section)

When the same concept has multiple names, that's the most common inconsistency type. List all terms with multiple variants:

| Variants found | Locations | Recommended canonical |
|----------------|-----------|------------------------|
| "User" / "Customer" / "Account" / "Account holder" | M3, M4, M5, M6, M7 SRS; CODEBASE_MAP; BUSINESS_CONTEXT | "Customer" (per BUSINESS_CONTEXT primary terminology) |
| "Tenant" / "Workspace" / "Organization" | M2, M8 SRS; CODEBASE_MAP | "Tenant" (per industry standard) |
| "Login" / "Sign in" / "Authenticate" | UI strings, API docs | UI: "Sign in"; API: "authenticate" |
| {{...}} | {{...}} | {{...}} |

Once canonical chosen, update non-canonical instances per Section 3 findings.

---

## 5. Reference Validity Check

| Reference type | Total | Valid | Broken | Notes |
|----------------|-------|-------|--------|-------|
| Internal markdown links | {{N}} | {{N}} | {{N}} | {{Listed in INC-H findings}} |
| File path citations | {{N}} | {{N}} | {{N}} | {{...}} |
| FR/NFR ID citations | {{N}} | {{N}} | {{N}} | {{...}} |
| ADR citations | {{N}} | {{N}} | {{N}} | {{...}} |
| External URL links | {{N}} | {{N}} | {{N}} | {{...}} |

Broken references go to Section 3 with severity.

---

## 6. Version & Status Consistency

### Component versions

| Component | Documented as | Discrepancies |
|-----------|---------------|---------------|
| Postgres | v15 in {{N docs}} | M-2 above |
| Node.js | v20 in all | None |
| React | v19 in {{N}} docs; v18 in 1 doc (legacy reference) | 1 minor finding |
| {{...}} | {{...}} | {{...}} |

### Status (Phase / WP / FR / ADR)

| Item | Status per Doc A | Status per Doc B | Status per Doc C | Resolution |
|------|------------------|------------------|------------------|------------|
| WP-2.B | "In progress" (MASTER_PLAN) | "Done" (PHASE_2 doc) | n/a | Doc B authoritative; update MASTER_PLAN |
| ADR-001 | "Approved" (TECH_SOLUTION_DESIGN) | "Proposed" (MASTER_PLAN preface) | n/a | A authoritative; update B |
| {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

---

## 7. Decisions Reflected Consistently

For each significant decision (ADR), verify ALL dependent docs reflect it:

| Decision (ADR) | Should appear in | Actually appears in | Gap |
|-----------------|-------------------|----------------------|-----|
| ADR-001 (Multi-region active-passive) | TECH_SOLUTION_DESIGN, MASTER_PLAN, PHASE_2_*, PHASE_3_*, DATA_ARCHITECTURE | All except DATA_ARCHITECTURE | Update DATA_ARCHITECTURE |
| {{...}} | {{...}} | {{...}} | {{...}} |

Gaps go to Section 3 findings.

---

## 8. Action Items (Tracked)

| Finding | Owner | Target | Jira ticket | Status |
|---------|-------|--------|--------------|--------|
| INC-C1 | PM | 2026-10-25 | {{ID}} | Open |
| INC-H1 | Tech Lead | 2026-10-30 | {{ID}} | Open |
| INC-H2 | Operator | 2026-10-25 | {{ID}} | Open |
| INC-M1..M3 | various | 2026-11-15 (batch) | {{ID}} | Open |
| INC-L1, L2 | Doc maintainer | next sprint | (low priority) | Open |

---

## 9. Resolved Since Last Report

| Finding ID (prior) | Resolution date | Notes |
|---------------------|-----------------|-------|
| {{ID}} | {{DATE}} | {{...}} |

---

## 10. Patterns / Systemic Findings

| Pattern | Evidence | Recommendation |
|---------|----------|----------------|
| {{e.g., Status drifts between MASTER_PLAN and PHASE docs}} | Multiple INC-* findings | Single source of truth: pick MASTER_PLAN OR PHASE; update via auto-script |
| {{e.g., New terms introduced without glossary update}} | Glossary missing 5 new terms | Add glossary check to PR template |

---

## 11. Notes & Caveats

- **Mode:** {{A / B / C}}
- **Time spent:** {{HOURS}}
- **Tools used:** {{e.g., grep, custom scripts}}
- **Limitations:** {{What was scope-cut}}
- **Confidence:** {{HIGH/MEDIUM/LOW}}

---

## 12. Recommendations

1. {{e.g., "Adopt single canonical entity name 'Customer' system-wide; update non-canonical refs in 1 sprint"}}
2. {{e.g., "Add cross-doc consistency check to PR template (require author confirms no conflicts introduced)"}}
3. {{e.g., "Consolidate WP status updates to MASTER_PLAN only; PHASE docs reference MASTER_PLAN"}}

---

## 13. Next Run

- **Recommended frequency:** Quarterly
- **Next run date:** {{YYYY-MM-DD}}
- **Triggered re-run:** before audit prep; after major doc additions

---

*Cross-doc consistency is invisible when good and obvious when bad. Auditors and new team members notice contradictions instantly.*
