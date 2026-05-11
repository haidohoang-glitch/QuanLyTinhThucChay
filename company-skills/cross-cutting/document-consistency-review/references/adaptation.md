# Document Consistency Review — Adaptation

Variations by project context.

> **Applies to Mode A only.** Mode B/C follow conventions.

## Small doc sets (<10 docs)

When set is small:

**Adjust:**
- Manual review fastest
- Section 4 Terminology + Section 5 Reference may be quick
- Run quarterly is overkill; semi-annually OK

## Large doc sets (50+ docs)

When set is extensive:

**Adjust:**
- Heavy automation needed
- Sample-based manual review (10-20% of docs deeply)
- Per-domain sub-reviews (each domain area reviewed independently)

**Add:**
- Tooling investment: scripts for terminology extraction
- CI integration: auto-detect new terminology variants

## Multi-team projects

When ownership distributed:

**Adjust:**
- Per-team sections (each team's docs sub-audited)
- Cross-team findings need negotiation (which team's terminology wins?)

**Add:**
- Cross-team review meeting after audit
- Glossary with team-attribution (if multiple definitions, why)

## Doc-as-code projects

When docs auto-generated from code:

**Adjust:**
- Auto-gen docs less subject to terminology drift (code provides one truth)
- Hand-written docs need more attention
- Drift between auto-gen and hand-written common

**Add:**
- Verify auto-gen pipeline produces consistent terminology
- Hand-written summaries match auto-gen detail

## Regulated industries

When auditors look at consistency:

**Adjust:**
- Audit-grade rigor
- Sign-off required on report
- Inconsistencies in compliance-sensitive docs escalate to Critical

**Add:**
- External review of consistency report annually
- Doc change log per terminology change (auditable trail)

## Multilingual projects

When docs in multiple languages:

**Adjust:**
- Per-language consistency separately
- Cross-language terminology mapping (glossary entries pair EN/VI/etc.)

**Add:**
- Translation-induced drift watch (new EN term added; VI doc not updated)

## Versioned docs

When docs versioned per release:

**Adjust:**
- Per-version consistency only (cross-version drift is expected)
- Audit only the active versions
- Latest version is source of truth for new authoring

## Living-doc projects

When docs change with every code change:

**Adjust:**
- High change rate → high inconsistency risk
- Run more frequently (monthly vs quarterly)
- Automate terminology check on every PR

**Add:**
- PR template question: "Did you introduce new terminology?"
- Glossary as a code-style file checked into repo

---

## When consistency review becomes overhead

If reviews consistently find 0-2 findings, the project's consistency culture is healthy:
- Run annually or on-demand
- Focus reviews on stakeholder-facing milestones (audit prep)
- Trust auto-detection for routine

Conversely, if reviews find 50+ each quarter:
- Cultural / process issue (multiple authors not coordinating)
- Investment needed: terminology decisions made centrally; PR review for terminology

---

## Differences from `documentation-sync`

Both detect drift but DIFFERENT axes:

| | `documentation-sync` | `document-consistency-review` |
|---|----------------------|--------------------------------|
| Detects | Doc vs reality (code, schema, env) | Doc vs doc (cross-document conflicts) |
| Example finding | "Doc cites old function name; code renamed" | "Doc A says 14 weeks, Doc B says 12 weeks" |
| Frequency | Monthly | Quarterly |
| Tools | Code parsers, schema diffs | Text comparison, terminology extraction |
| Output report | DOC_SYNC_REPORT.md | CONSISTENCY_REVIEW_REPORT.md |

Both should run; they catch different problems. Run sync more frequently (monthly); consistency less frequently (quarterly).

## Combined report option

For lean teams, a single quarterly report can combine both:

```
# Quarterly Doc Health Report

## Part 1: Sync (doc vs reality) — from documentation-sync
## Part 2: Consistency (doc vs doc) — from this skill
```

Adjust skill outputs to feed combined report.
