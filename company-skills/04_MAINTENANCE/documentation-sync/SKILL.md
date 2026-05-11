---
name: documentation-sync
description: Detect and report documentation drift — inconsistencies between code and docs, between docs and SRS, between docs and reality. Produces DOC_SYNC_REPORT.md with categorized drift findings, severity, and remediation actions. Run periodically (weekly/monthly) to keep docs trustworthy. Use when docs and code may have diverged after development sprints, before audit prep, when onboarding new team members and want fresh docs, or when generating Phase 4 Maintenance sync output. Triggers include "check docs are up to date", "detect doc drift", "verify documentation matches code", "doc sync audit", or "Phase 4 Maintenance sync".
---

# Documentation Sync

Detect drift across the documentation system: code-vs-docs, docs-vs-SRS, docs-vs-reality. Output is `DOC_SYNC_REPORT.md` listing findings + remediation actions. Run periodically to prevent doc rot.

## When this skill applies

Use when:
- Periodically (weekly / monthly) as a maintenance routine
- Before audit prep (auditors care about doc accuracy)
- After significant development sprints (high drift likely)
- When onboarding new team members (verify docs are trustworthy)
- Generating Phase 4 Maintenance output

Do NOT use for:
- Initial documentation creation (use Phase 0/1/2 skills)
- Fixing docs after drift detected (this skill detects; remediation is per-finding work)
- Code review (different scope)

## Inputs

1. **All docs in `docs/`** — every markdown file
2. **Source code** — to verify references match reality
3. **Git log** — to detect when code changed without doc update
4. `docs/INDEX.md` — master nav, most prone to drift

## Output

`docs/04_MAINTENANCE/DOC_SYNC_REPORT.md` (replace each run; archive prior to `_archive/`).

Filled from [assets/DOC_SYNC_REPORT_template.md](assets/DOC_SYNC_REPORT_template.md).

## Workflow

### Step 1 — Inventory all docs

```bash
find docs/ -name "*.md" -type f | wc -l
find docs/ -name "*.md" -type f
```

Build a list. For each doc, note: last modification date, git log of recent changes.

### Step 2 — Choose sync check mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard sync checks** *(default)* | No company-specific framework | This skill's standard checks |
| **B — Honor company doc-as-code framework** | Company has formal doc-sync standard | Company doc |
| **C — User-defined sync dimensions** | Specific checks needed | User input |

#### Mode A — Standard sync checks

Standard categories of drift:

| Category | Description | Detection |
|----------|-------------|-----------|
| **Code reference** | Doc cites file:line; file or line moved | Grep cited paths; verify exist |
| **Function reference** | Doc names function; function renamed/removed | Grep function name in code |
| **Config reference** | Doc cites env var or config; renamed/removed | Grep env names in `.env*` and config files |
| **Schema reference** | Doc describes table/column; schema changed | Compare doc DDL vs current schema |
| **Dependency reference** | Doc names library/version; changed | Compare to `package.json`/`requirements.txt` |
| **Process reference** | Doc describes workflow; reality differs | Verify by interview / observation |
| **Cross-doc reference** | Doc A links to Doc B; Doc B moved | Verify all internal links resolve |
| **Index drift** | Master INDEX missing new docs OR lists removed docs | Compare INDEX.md to filesystem |
| **Stale data** | Doc has stats / counts; outdated | Refresh; compare |
| **Authorial intent** | Doc says "we plan to do X" but X happened (or didn't) | Manual review |

### Step 3 — Run automated drift checks

For each category, automated where possible:

```bash
# Cross-doc reference check (broken internal links)
# Walk docs/, extract markdown links, verify target exists
find docs/ -name "*.md" -type f -exec grep -oE '\[.*?\]\([^)]+\.md[^)]*\)' {} \; | \
  while read line; do
    target=$(echo "$line" | sed -E 's/.*\(([^)]+)\).*/\1/')
    [ -f "$target" ] || echo "BROKEN: $line"
  done

# Code path check — find file:line references in docs that point to non-existent files
grep -rE '`[a-z]+/[a-zA-Z0-9_/.-]+\.(ts|js|py|go|sql)(:[0-9]+)?`' docs/ | \
  while read match; do
    path=$(echo "$match" | grep -oE '`[^`]+`' | tr -d '`' | head -1 | sed 's/:.*//')
    [ -f "$path" ] || echo "MISSING FILE: $match"
  done

# Env var check
grep -rE '(?:env\.|process\.env\.|os\.getenv)([A-Z_]+)' docs/ | \
  awk '{print $NF}' | sort -u > /tmp/docs-env-vars.txt
# Compare to actual env files
```

Some checks need human eyes (process drift, intent drift); flag those for manual review section.

### Step 4 — Categorize findings by severity

| Severity | Criteria |
|----------|----------|
| **Critical** | Doc actively misleads (e.g., wrong command in incident playbook) |
| **High** | Doc broken or significantly out of date (broken link in INDEX, schema doc shows obsolete tables) |
| **Medium** | Doc has stale specifics but core message still correct (LOC count outdated; file path moved by 1 dir) |
| **Low** | Cosmetic (typo, formatting); doc otherwise accurate |

Critical findings warrant immediate fix (within 1 week); Low can batch.

### Step 5 — For each finding, propose remediation

| Finding type | Typical remediation |
|--------------|---------------------|
| Broken file path | Update doc with current path |
| Removed function | Remove reference OR update to replacement |
| Renamed env var | Update doc; verify all callers updated |
| Schema drift | Regenerate schema doc from `pg_dump --schema-only` or equivalent |
| Stale stats | Refresh from current measurement |
| Process drift | Interview to capture current process; update doc |
| Index drift | Update INDEX.md (consider running `document-index-master` skill) |

Each finding gets: description + severity + remediation + owner + target date.

### Step 6 — Identify staleness patterns

Beyond per-finding fixes, look for patterns:

- **Same doc has 5+ findings** — doc may need full rewrite, not patches
- **Multiple docs reference same removed code** — root cause is incomplete deletion (code removed, refs stayed)
- **INDEX has many missing entries** — INDEX update process broken
- **Process docs all stale** — team isn't reviewing/updating; cultural issue

Pattern findings often reveal process gaps; surface in report's "Systemic Findings" section.

### Step 7 — Coverage report

What was checked vs not:

- **Automated checks completed:** {{LIST}}
- **Manual reviews completed:** {{LIST}}
- **Not checked (cite reason):** {{LIST}}

Honest scope statement matters — claiming full sync when you only checked half is misleading.

### Step 8 — Remediation tracking

Each finding goes into a tracking system (Jira / Linear / GitHub Issues / inline checklist). Don't just publish report — assign owners.

Section in report: "Action Items" with finding ID + owner + target date.

### Step 9 — Self-review

Run [references/checklist.md](references/checklist.md). Sync report is most useful when accurate; verify before publishing.

## Quality bar

A good sync report lets:
- A team lead see at a glance how much drift exists
- Each finding be actionable (specific doc + specific fix)
- Patterns surface for process improvement
- Auditors trust docs after the report's findings are fixed

If the report is "looks fine", you didn't look hard enough. Most projects have 5-30 drift findings per quarter on actively developed code.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: small doc set (lighter checks), regulated industries (audit-grade rigor), multi-team (per-team sub-reports), automated CI integration.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: monthly sync report for a project with 27 docs, finding 14 drift items.

## Failure modes to avoid

- **Vague findings.** "Some docs out of date" — useless. Cite specific doc + line + what's wrong.
- **No remediation.** Detection without fix → drift continues.
- **No owner.** Findings without owner = nobody fixes.
- **Skipping manual checks.** Some drift only humans detect (process drift, intent drift).
- **Treating all findings as Critical.** Calibration matters; if all are Critical, none are.
- **One-time run.** Drift compounds; needs periodic re-run (quarterly minimum, monthly typical).
- **No automation.** Manual sync at scale fails; build automated checks for repeatable findings.
