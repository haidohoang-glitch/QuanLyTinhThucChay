# {{PROJECT_NAME}} — Tech Debt Audit

> **Purpose:** Identify and rank technical debt across categories. Descriptive (what's broken/risky), not prescriptive (fix designs belong elsewhere).
> **Audience:** Tech lead, architect, engineering manager, security reviewer.
> **Last updated:** {{YYYY-MM-DD}}
> **Generated using:** `tech-debt-audit` skill v1
> **Reviewer:** {{NAME_OR_TBD}}

---

## 1. Executive Summary

**Overall debt level:** {{LOW / MEDIUM / HIGH / CRITICAL}}

**Highlights:**
- Total findings: {{NUMBER}} ({{P0_COUNT}} P0, {{P1_COUNT}} P1, {{P2_COUNT}} P2, {{P3_COUNT}} P3)
- Categories with most debt: {{TOP_2_CATEGORIES}}
- Estimated total remediation effort: {{HOURS_OR_DAYS}}

**Top 3 risks:**
1. {{FINDING_ID}} — {{ONE_LINE}} ({{SEVERITY}})
2. {{FINDING_ID}} — {{ONE_LINE}} ({{SEVERITY}})
3. {{FINDING_ID}} — {{ONE_LINE}} ({{SEVERITY}})

---

## 2. Quality Signals (Raw Data)

Cheap automated signals collected before manual review:

| Signal | Value | Notes |
|--------|-------|-------|
| Test coverage | {{PERCENTAGE}} | {{TOOL_USED}}; critical paths: {{LIST_LOW_COVERAGE_AREAS}} |
| Lint errors | {{COUNT}} | Top rule violations: {{LIST}} |
| Type errors (`tsc --noEmit` or equiv) | {{COUNT}} | {{NOTES}} |
| `npm audit` | {{COUNT}} vulns ({{HIGH}} high, {{CRITICAL}} critical) | {{TOP_3_PACKAGES}} |
| `npm outdated` (or equiv) | {{COUNT}} packages outdated | {{COUNT_MAJOR}} major versions behind |
| Bundle size (if applicable) | {{SIZE}} | {{TREND}} |
| Largest files | {{LIST_TOP_5}} | LOC count |

These are inputs, not findings. Findings are in Section 4.

---

## 3. Categorization Mode

See Section 9 for chosen mode (A / B / C).

---

## 4. Findings (by category)

### {{CATEGORY_NAME — e.g., SECURITY}}

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| F-{{NN}} | {{P0/P1/P2/P3}} | {{XS/S/M/L/XL}} | {{ONE_LINE}} | `{{FILE:LINE}}` or query | {{CONTEXT}} |

{{REPEAT_FOR_EACH_FINDING_IN_CATEGORY}}

{{REPEAT_SUBSECTION_FOR_EACH_CATEGORY}}

---

## 5. Clusters (Root-cause groupings)

Findings that share a root cause. Fixing the root cause usually closes multiple findings.

### Cluster: {{CLUSTER_NAME}}

- **Root cause:** {{ONE_PARAGRAPH}}
- **Findings included:** {{F-NN, F-NN, F-NN, ...}}
- **Combined effort to fix root cause:** {{ESTIMATE}}
- **Combined risk reduction:** {{LIST_FINDINGS_RESOLVED}}

{{REPEAT_FOR_EACH_CLUSTER}}

---

## 6. Top 10 Punch List

The recommended order to start fixing, considering severity, effort, and dependencies:

| Order | Finding | Why this priority | Effort |
|-------|---------|-------------------|--------|
| 1 | {{F-ID}} | {{ONE_LINE_REASON}} | {{EFFORT}} |
| 2 | {{F-ID}} | {{REASON}} | {{EFFORT}} |
| 3 | {{F-ID}} | {{REASON}} | {{EFFORT}} |
| 4 | {{F-ID}} | {{REASON}} | {{EFFORT}} |
| 5 | {{F-ID}} | {{REASON}} | {{EFFORT}} |
| 6 | {{F-ID}} | {{REASON}} | {{EFFORT}} |
| 7 | {{F-ID}} | {{REASON}} | {{EFFORT}} |
| 8 | {{F-ID}} | {{REASON}} | {{EFFORT}} |
| 9 | {{F-ID}} | {{REASON}} | {{EFFORT}} |
| 10 | {{F-ID}} | {{REASON}} | {{EFFORT}} |

This is a recommendation, not a plan. Implementation planning belongs to `implementation-planning` skill.

---

## 7. Aggregate by Severity & Effort

| | XS (<2h) | S (2-8h) | M (1-3d) | L (3-10d) | XL (>2w) | Total |
|---|---|---|---|---|---|---|
| **P0** | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| **P1** | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| **P2** | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| **P3** | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| **Total** | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{TOTAL}} |

---

## 8. Open Questions

| ID | Question | Where seen | Suggested next step |
|----|----------|------------|---------------------|
| OQ-1 | {{SPECIFIC_QUESTION}} | {{LOCATION}} | {{NEXT_STEP}} |

If <3 open questions, look harder — every codebase has surprises.

---

## 9. Notes & Caveats

- **Categorization mode:** {{A — Standard 7 categories / B — Honor codebase categories / C — User-defined}}
- **Mode rationale:** {{WHY}}
- **If Mode B:** Source = `{{PATH_TO_PRIOR_AUDIT}}` (commit `{{HASH}}`)
- **If Mode C:** User-provided categories = {{LIST}}; rationale = {{WHY}}
- **Audit scope:** {{WHAT_WAS_DONE — e.g., automated scans, manual review of critical paths, dep audit}}. NOT done: {{WHAT_WAS_SKIPPED — e.g., security pen test, full manual code review, runtime profiling}}.
- **Severity discipline applied:** P0 reserved for active or <7-day-imminent failures. Verify by re-reading findings.
- **Time spent:** {{HOURS}}
- **Confidence:** {{HIGH/MEDIUM/LOW}}

---

*Findings are descriptive. Fix designs belong in `tech-solution-design`. Implementation order belongs in `implementation-planning`.*
