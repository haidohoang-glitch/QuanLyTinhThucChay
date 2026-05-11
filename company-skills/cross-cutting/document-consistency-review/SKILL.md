---
name: document-consistency-review
description: Audit cross-document consistency — find conflicts, contradictions, divergent naming, mismatched versions, and orphan references across all docs. Distinct from `documentation-sync` (which detects code-vs-doc drift); this skill detects doc-vs-doc inconsistency. Produces CONSISTENCY_REVIEW_REPORT.md with findings + remediation. Run quarterly or before audit prep. Use when docs may have diverged after multiple authors, before stakeholder review, when doc-set has grown organically, or when generating cross-cutting consistency output. Triggers include "check doc consistency", "cross-document review", "find conflicts in docs", "consistency audit", or "cross-cutting review".
---

# Document Consistency Review

Audit consistency ACROSS docs: do all docs agree about the same thing? Same term used same way everywhere? Same numbers (counts, dates, costs) consistent? Same references valid? This is doc-vs-doc; `documentation-sync` is doc-vs-code.

## When this skill applies

Use when:
- Quarterly cross-doc audit
- Before stakeholder / executive review
- Before audit prep (auditors notice contradictions fast)
- Doc set has grown organically (multiple authors → likely contradictions)
- Generating cross-cutting consistency output

Do NOT use for:
- Per-doc rigor (each doc's own checklist handles)
- Code-vs-doc drift (use `documentation-sync`)
- Doc creation (Phase 0/1/2/3/4 skills)

## Inputs

1. **All docs in `docs/`** — every markdown file, all phase folders + cross-cutting
2. `docs/INDEX.md` — to know what should exist
3. **Master glossary** (in INDEX.md Section 6 typically)

## Output

`docs/04_MAINTENANCE/CONSISTENCY_REVIEW_REPORT.md` (replace each run; archive prior).

Filled from [assets/CONSISTENCY_REVIEW_template.md](assets/CONSISTENCY_REVIEW_template.md).

## Workflow

### Step 1 — Choose review dimensions mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard 8-dimension review** *(default)* | No company-specific framework | This skill's standard |
| **B — Honor company review checklist** | Company has formal cross-doc review standard | Company doc |
| **C — User-defined dimensions** | Specific concerns | User input |

#### Mode A — Standard 8 dimensions

| # | Dimension | What to check |
|---|-----------|---------------|
| 1 | Terminology | Same concept named consistently across docs |
| 2 | Numbers | Counts, dates, costs, durations consistent |
| 3 | References | Doc A's reference to Doc B is valid (link works, content matches claim) |
| 4 | Versioning | Same component's version consistent across docs |
| 5 | Owner / contact | Same role / person referenced consistently |
| 6 | Decisions | ADRs / decisions reflected consistently in docs that depend on them |
| 7 | Status | Project / WP / FR status consistent (if WP "Done" in MASTER_PLAN, also "Done" in PHASE doc) |
| 8 | Glossary | Terms in glossary used per definition; new terms added to glossary |

### Step 2 — Build a fact extraction

For each doc, extract key facts:

| Fact category | What to extract |
|---------------|-----------------|
| Names | Project name; product name; team names; person names |
| Numbers | Dates (deadlines, milestones); counts (FRs, NFRs, WPs, costs); durations |
| Statuses | Phase status, WP status, ADR status |
| Tech stack | Versions of major components (Postgres, Node, etc.) |
| Decisions | Cited ADRs; cited choices |
| Costs | Budget, projections, actuals |
| Performance targets | NFR values |

Build a table or spreadsheet.

### Step 3 — Compare facts across docs

For each fact, list the docs that mention it. If multiple docs disagree → finding.

Examples:
- MASTER_PLAN says "14 weeks"; FEASIBILITY says "12 weeks" → conflict (T-N-01)
- TECH_DEBT_AUDIT says "47 findings"; MASTER_PLAN says "All P0/P1 findings" but counts mismatch → conflict
- ADR-001 says "Postgres logical replication"; MASTER_PLAN says "Postgres physical replication" → conflict

### Step 4 — Run terminology check

For each domain term, find all uses across docs. Inconsistencies:
- "User" in M3 SRS vs "Customer" in M4 SRS — same entity?
- "Customer" in BUSINESS_CONTEXT vs "Account" in CODEBASE_MAP — same entity?
- "Wallet" in M5 vs "Account" in DATA_ARCHITECTURE — same entity?

Each inconsistency is a finding.

### Step 5 — Run reference validity check

Each cross-doc reference (link or quoted claim) verified:

```bash
# Find all references to other docs
grep -rE '\[.*?\]\([^)]+\.md[^)]*\)' docs/ | sort -u
```

For each reference:
- Target file exists?
- Target section/anchor exists?
- Quoted content matches actual target?

### Step 6 — Run version + status consistency check

Major components / decisions:
- Postgres version in DATA_ARCH vs CODEBASE_MAP vs PHASE_*.md
- WP status in MASTER_PLAN vs PHASE_*.md
- ADR status in TECH_SOLUTION_DESIGN vs MASTER_PLAN

Each disagreement is a finding.

### Step 7 — Categorize findings by severity

| Severity | Criteria |
|----------|----------|
| **Critical** | Conflicting facts that affect decisions (timeline mismatch leading to wrong commitments; conflicting requirements) |
| **High** | Same concept named 2+ different ways system-wide; broken cross-references |
| **Medium** | Localized inconsistency (one doc has wrong number; rest correct) |
| **Low** | Cosmetic (capitalization variance, minor naming) |

### Step 8 — Propose remediation

For each inconsistency, decide which doc is "source of truth" and which needs updating:

- Numbers / dates: typically the most-recent doc is correct
- Terminology: pick canonical name; update others
- References: update broken; verify content matches

Each finding has: description + canonical source + remediation owner + target.

### Step 9 — Self-review

Run [references/checklist.md](references/checklist.md). Consistency review is most useful when accurate; verify before publishing.

## Quality bar

A good consistency review lets:
- Stakeholders trust the doc set (no contradictions)
- New readers not get confused by terminology variations
- Auditors find no obvious contradictions
- Future doc authors know which fact is canonical

If the report is "looks consistent", you didn't look hard enough. Active doc systems accumulate ~10-30 inconsistencies per quarter.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: small doc sets, large doc sets, multi-team projects, regulated industries.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: quarterly review on a 31-doc project finding 18 inconsistencies.

## Failure modes to avoid

- **Vague findings.** "Some terms inconsistent" — useless. "MASTER_PLAN.md uses 'User' (line 47); BUSINESS_CONTEXT.md uses 'Customer' (line 12); SRS M3 uses 'Account holder'" — actionable.
- **No canonical source.** Without picking one as truth, remediation drifts.
- **Skipping terminology check.** Most subtle inconsistencies are word-level; easy to miss without explicit pass.
- **Treating every minor variant as Critical.** Calibrate severity.
- **One-time run.** Doc systems drift; needs quarterly cadence minimum.
- **Confusing with `documentation-sync`.** Sync = doc vs reality. Consistency = doc vs doc. Run both periodically.
