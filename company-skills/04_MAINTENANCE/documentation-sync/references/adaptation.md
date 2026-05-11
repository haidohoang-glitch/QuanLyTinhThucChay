# Documentation Sync — Adaptation

Variations by doc set size and project context.

> **Applies to Mode A only.** Mode B/C follow conventions.

## Small doc sets (<10 docs)

Simpler approach:

**Adjust:**
- Likely don't need automated checks; manual is faster
- Section 4 Patterns may have 0 (small set, less drift accumulation)
- Run quarterly instead of monthly

## Large doc sets (50+ docs)

When project has extensive docs:

**Adjust:**
- Heavy reliance on automation (manual review of all is impractical)
- Per-domain reports (sub-reports per area: API docs, runbooks, etc.)
- Sample-based manual review (10% of docs reviewed manually each run)

**Add:**
- CI integration: run automated checks on every PR; fail if introduces drift
- Tooling investment: scripts for repeatable checks worth maintaining

## Code-heavy projects

When most drift is code-vs-doc:

**Emphasize:**
- File path / function reference checks
- Schema doc auto-generation
- Test that code examples in docs actually run (literate testing)

**Add:**
- Doc tests: code blocks in docs executed in CI
- Annotated source: `// @doc-ref docs/X.md:Y` comments to enforce co-update

## Process-heavy projects

When most drift is process-vs-reality:

**Emphasize:**
- Manual interview-based checks
- Tabletop exercises for runbooks
- Onboarding feedback (new joiners are best drift detectors)

**Add:**
- Quarterly process review meeting
- Drift findings from postmortems folded into sync report

## Regulated industries

When auditors review docs:

**Adjust:**
- Audit-grade rigor required (every finding verifiable by external auditor)
- Sign-offs on report (Quality Lead, Compliance)
- Drift in compliance-sensitive docs (e.g., audit log retention) escalates to Critical automatically

**Add:**
- Annual external review of doc quality
- Doc changes tracked with git audit (who changed what, when)

## Multi-team projects

When ownership is distributed:

**Adjust:**
- Per-team sub-reports (each team owns their docs' drift)
- Cross-team findings (e.g., contract docs) need negotiated ownership

**Add:**
- Doc ownership matrix (which team owns which doc folder)
- SLA per team (how fast each team fixes drift)

## Auto-generated docs

When some docs are auto-generated (OpenAPI, schema docs, JSDoc):

**Distinguish:**
- Auto-gen docs: drift means generation broken (or stopped); fix the pipeline
- Hand-written docs: drift is normal; needs updating

**Add:**
- Pipeline health check (generation runs successfully; output deployed)
- Manual content separated from auto-generated content (clear in doc structure)

## Living-doc projects (continuous deployment)

When docs are part of the deployment pipeline:

**Adjust:**
- Sync runs in CI on every doc change
- Drift detected = PR blocked
- Less periodic review needed; continuous validation

**Add:**
- Doc preview environment (deploys a draft of docs site for review)
- Doc rollback parity with code rollback

## CI integration patterns

For automated drift detection:

```yaml
# Example GitHub Actions workflow
name: doc-sync-check
on: [pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check doc internal links
        run: scripts/check-doc-links.sh
      - name: Check code path references
        run: scripts/check-doc-paths.sh
      - name: Check INDEX completeness
        run: scripts/check-index.sh
```

Failures block merge; teams fix drift inline with code change.

## When sync skill becomes overhead

If sync findings are consistently 0-2 per quarter on a small project, the skill may be heavier than warranted. Adjust:

- Run annually, not quarterly
- Skip automation; manual scan suffices
- Combine with consistency-review (related skill)

Conversely, if findings are 30+ per quarter, the project's doc culture has deeper issues — sync skill is detection; remediation is cultural (PR templates, owner assignment, automation investment).

---

## Tools mentioned in standard checks

Useful for automation:

| Check | Tool / approach |
|-------|----------------|
| Internal markdown links | `markdown-link-check` (npm), or custom shell |
| Path / file references | `grep -E` with file existence test |
| Code symbol references | `tree-sitter` or language-specific parsers |
| Schema docs | `pg_dump --schema-only` diff against doc |
| API docs | OpenAPI spec validator + drift detector |
| INDEX completeness | `find docs/ -name '*.md'` diff against INDEX entries |

Document which tools you use in Section 8 of the sync report.
