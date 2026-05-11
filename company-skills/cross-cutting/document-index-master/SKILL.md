---
name: document-index-master
description: Author or update the master documentation index (`docs/INDEX.md`) — the navigation hub linking every doc with purpose, audience, status, and reading order per role. Generates from filesystem inventory + doc metadata. Use when creating a new project's docs system, when significant docs added/removed, when INDEX has drifted, when onboarding new team members and want fresh nav, or when generating cross-cutting INDEX output. Triggers include "create master index", "INDEX.md", "documentation navigation hub", "regenerate INDEX", or "cross-cutting index".
---

# Document Index Master

Author or refresh `docs/INDEX.md` — the master navigation hub. Every doc system needs one canonical entry point listing all docs with purpose, audience, status, and reading orders per role.

## When this skill applies

Use when:
- Creating new project's `docs/` structure (Phase 0+ skills haven't run yet, but you want INDEX scaffold)
- After significant doc creation/removal (Phase 0/1 skills produced new docs)
- INDEX has drifted (per `documentation-sync` findings)
- Onboarding new team members; want fresh nav
- Generating cross-cutting INDEX output

Do NOT use for:
- Per-doc authoring (use Phase 0/1/2/3/4 skills)
- Cross-doc consistency check (use `document-consistency-review`)
- Drift detection (use `documentation-sync`)

## Inputs

1. **Filesystem inventory:** all files in `docs/` (find recursively)
2. **Each doc's frontmatter / first section:** for purpose, audience, status
3. **Project context:** company / project name, version
4. **Roles in the project:** who reads docs (Tech Lead, Backend Dev, QA, etc.)

## Output

`docs/INDEX.md`, filled from [assets/INDEX_template.md](assets/INDEX_template.md).

## Workflow

### Step 1 — Inventory all docs

```bash
find docs/ -name "*.md" -type f | sort
```

Group by phase folder:
- `docs/00_REQUIREMENTS/`
- `docs/01_DISCOVERY/`
- `docs/02_STRATEGIC/`
- `docs/03_EXECUTION/`
- `docs/04_MAINTENANCE/`
- Root: `INDEX.md`, `QUICK_START.md`, etc.

### Step 2 — Choose index structure mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard 8-section index** *(default)* | No company-specific format | This skill's standard structure |
| **B — Honor company doc landing template** | Company has fixed INDEX format | Company template |
| **C — User-defined sections** | Specific structure preferred | User input |

#### Mode A — Standard 8 sections

```
1. Bird's-eye map (visual / ASCII)
2. Folder structure
3. Per-phase doc tables (purpose, audience, status)
4. Document relationships diagram
5. Reading orders per role
6. Glossary
7. Cross-document corrections / audit log
8. Maintenance / contact / next review
```

### Step 3 — Extract per-doc metadata

For each doc, extract or infer:

- **Purpose** (1 line) — from doc's title + first paragraph
- **Status** — Stable / Draft / Deprecated / Archived
- **Audience** — read tags in frontmatter or first section
- **Last updated** — `git log -1` for the file
- **Version** (if applicable) — from doc's metadata

If frontmatter exists with these fields, use it. Otherwise, infer from content (mark as "inferred" if uncertain).

### Step 4 — Build folder structure visualization

ASCII tree representing the docs/ hierarchy:

```
docs/
├── 00_REQUIREMENTS/
│   ├── SRS.md
│   └── SRS_VI/M1-M10
├── 01_DISCOVERY/
│   ├── CODEBASE_MAP.md
│   ├── DATA_ARCHITECTURE.md
│   ├── TECH_DEBT_AUDIT.md
│   └── BUSINESS_CONTEXT.md
├── 02_STRATEGIC/
│   ├── FEASIBILITY_ASSESSMENT.md
│   ├── TECH_SOLUTION_DESIGN.md
│   └── MASTER_PLAN.md
├── 03_EXECUTION/
│   ├── AI_OPERATOR_GUIDE.md
│   ├── AI_AGENT_TASK_DISTRIBUTION.md
│   ├── 00_TESTING_INFRASTRUCTURE.md
│   ├── A_CODE_SNIPPETS.md
│   ├── B_QA_CHECKLIST_MASTER.md
│   └── work-packages/
│       ├── PHASE_0_PRE_FLIGHT.md
│       ├── PHASE_1_QUICK_WINS.md
│       ├── PHASE_2_DUAL_WRITE.md
│       ├── PHASE_3_SWITCH_READS.md
│       └── PHASE_4_COMPLIANCE.md
├── 04_MAINTENANCE/
│   ├── runbooks/
│   ├── feature-extensions/
│   └── DOC_SYNC_REPORT.md
├── INDEX.md
└── QUICK_START.md
```

### Step 5 — Build per-phase doc tables

Each phase gets a table:

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| `00_REQUIREMENTS/SRS_VI/M1.md` | Introduction | Stable | All |
| `00_REQUIREMENTS/SRS_VI/M2.md` | Overall Description | Stable | Tech Lead |

### Step 6 — Build document relationships diagram

Show how docs feed into each other:

```
Phase 0 Requirements ──┐
                       ├──> Phase 2 Strategic ──> Phase 3 Execution ──> Phase 4 Maintenance
Phase 1 Discovery ─────┘
```

This visualizes the doc lifecycle.

### Step 7 — Reading orders per role

For each role in the project, recommend reading order:

```
Tech Lead / Architect:
1. INDEX.md (this file)
2. 02_STRATEGIC/TECH_SOLUTION_DESIGN.md (Section 1-3)
3. 01_DISCOVERY/DATA_ARCHITECTURE.md (Section 10 corrections)
4. 02_STRATEGIC/MASTER_PLAN.md
5. 03_EXECUTION/work-packages/PHASE_*.md (lookup as needed)

Backend Developer:
1. INDEX.md
2. 02_STRATEGIC/MASTER_PLAN.md
3. 02_STRATEGIC/SERVER_ARCHITECTURE.md (if exists)
4. 03_EXECUTION/00_TESTING_INFRASTRUCTURE.md
5. PHASE_0 ... etc.
```

Cover: Tech Lead, Backend Dev, Frontend Dev, QA, DevOps, Product, Compliance, AI Agent.

### Step 8 — Glossary

Project-specific terminology used across docs:

```
WP = Work Package — smallest unit of execution
RTM = Requirements Traceability Matrix
NFR = Non-Functional Requirement
DG = DATA_GOVERNANCE.md (legacy alias)
{{...}}
```

Helps readers across roles avoid ambiguity.

### Step 9 — Cross-document corrections / audit log

Track significant cross-doc changes:

| Date | Change | Files affected |
|------|--------|----------------|
| 2026-05-04 | Timeline corrected from 6-8 to 7-9 weeks | NEW_TECH_SOLUTION.md, MASTER_PLAN.md |
| 2026-05-05 | Reorganized to phase-based structure | (all docs) |

This is for posterity; future readers can understand the doc system's evolution.

### Step 10 — Self-review

Run [references/checklist.md](references/checklist.md). Index quality directly affects every reader; rigor matters.

## Quality bar

A good INDEX lets:
- Anyone find any doc within 30 seconds
- A new team member start reading from the right entry per role
- A reviewer audit doc completeness (what exists, what's missing)
- An AI agent navigate the doc system without crawling

If readers ask "where is the doc for X?", the INDEX failed — fix it.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: small projects (single-page index), large projects (per-phase sub-indexes), multi-team projects, doc-as-code projects.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: INDEX for a fully-stocked project (Phase 0-4 docs all present).

## Failure modes to avoid

- **Stale entries.** INDEX lists docs that no longer exist; readers click broken links.
- **Missing entries.** New docs created without INDEX update; readers don't find them.
- **Vague purposes.** "Documentation about the system" — useless. "Audit of data layer with PII map and governance gaps" — specific.
- **No reading orders.** Without role-based reading guidance, readers crawl randomly.
- **Inflated structure.** 8 sections when 4 suffice — wastes attention.
- **Frozen forever.** Index is a living doc; needs updating per `documentation-sync` cadence.
