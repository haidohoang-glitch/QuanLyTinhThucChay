# Document Index Master — Quality Checklist

Run before publishing INDEX.md.

## Gate 1 — Coverage

- [ ] Every doc in `docs/` (recursive) appears in INDEX (or explicitly excluded with reason)
- [ ] Filesystem scan vs INDEX entries diff = 0 (no missing, no orphan)
- [ ] Each entry has: file link, purpose, status, audience

## Gate 2 — Visual hierarchy

- [ ] Section 1 has bird's-eye visual (ASCII or Mermaid)
- [ ] Section 2 has folder structure tree
- [ ] Section 4 has document relationships diagram
- [ ] Visuals match folder reality (no obsolete diagrams)

## Gate 3 — Per-doc metadata accuracy

- [ ] Status values consistent (Stable / Draft / Deprecated / Archived — pick one set)
- [ ] Status reflects reality (don't mark "Stable" if doc is admittedly draft)
- [ ] Audience non-vague (specific roles, not just "All")
- [ ] Purpose ≤2 lines per doc (concise)

## Gate 4 — Reading orders per role

- [ ] At least 5 roles covered (Tech Lead, Backend, Frontend, QA, DevOps minimum; add Product, Compliance, AI as applicable)
- [ ] Reading orders concrete (numbered list, specific files)
- [ ] AI Agent reading order includes system prompt fragment

## Gate 5 — Glossary

- [ ] Every project-specific term used in INDEX or other docs is defined
- [ ] Standard terms (FR, NFR, ADR, etc.) defined for non-experts
- [ ] Project-specific abbreviations not assumed

## Gate 6 — Audit log

- [ ] Section 7 lists significant cross-doc changes
- [ ] Dates accurate
- [ ] Reasons non-vague

## Gate 7 — Maintenance

- [ ] Section 8 names INDEX maintainer
- [ ] Update cadence defined
- [ ] Issue reporting path explicit

## Gate 8 — Mode discipline

- [ ] Mode A: 8-section standard
- [ ] Mode B: company landing template followed
- [ ] Mode C: user-defined sections; rationale documented

## Gate 9 — Format

- [ ] Output: `docs/INDEX.md`
- [ ] All internal links use relative paths
- [ ] All internal links resolve (verify via link checker)
- [ ] Tables consistent
- [ ] No `{{PLACEHOLDER}}` left except where intentional

## Gate 10 — Recency

- [ ] "Last updated" date is today (or close to)
- [ ] Linked status reports (sync, consistency) point to most recent

## Self-review prompt

Pretend you're a new team member opening INDEX for the first time. Within 30 seconds, can you:
- Find the high-level project overview? (Section 1-2)
- Find the doc for "what does this product do"? (Section 3 → SRS or BUSINESS_CONTEXT)
- Find the operator guide if you're starting AI execution? (Section 3 → AI_OPERATOR_GUIDE)
- Know what reading order to follow as a Backend Dev? (Section 5)

If any takes >30 seconds, the INDEX needs sharper hierarchy.
