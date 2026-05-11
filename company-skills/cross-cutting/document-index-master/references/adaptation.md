# Document Index Master — Adaptation

Variations by project size and structure.

> **Applies to Mode A only.** Mode B/C follow conventions.

## Small projects (<10 docs)

When doc set is small:

**Adjust:**
- Single-page index suffices; collapse sections
- Skip Section 4 relationships diagram (overhead)
- Reading orders can be 1 or 2 (e.g., "Everyone" + "AI Agent")

**Don't:**
- Skip glossary (even small projects benefit)
- Skip maintenance section (tells future maintainer where to start)

## Large projects (50+ docs)

When doc set is extensive:

**Adjust:**
- Per-phase sub-INDEXes (each phase folder has its own `_INDEX.md`)
- Master INDEX summarizes; sub-INDEXes detail
- Section 3 may reference sub-INDEX rather than listing all docs

**Add:**
- Search-friendly metadata in frontmatter (tags, keywords)
- Auto-generation tooling (scripts that build INDEX from filesystem)

## Multi-team projects

When ownership distributed:

**Adjust:**
- Per-team sections in Section 3 (group by team ownership)
- Owner column in tables (which team maintains)
- Cross-team reading orders may be needed

**Add:**
- Team boundaries explicit (which docs are team-internal vs. shared)

## Doc-as-code projects

When INDEX auto-generates from code/filesystem:

**Adjust:**
- INDEX is mostly auto-generated; manual content limited
- Headers and intro paragraphs stay manual
- Per-doc metadata extracted from frontmatter

**Add:**
- Generation script committed (`scripts/build-index.sh`)
- CI runs script on doc changes; commits if drift
- "Last generated" timestamp in INDEX

## API-only projects

When primary "doc" is API spec:

**Adjust:**
- Section 1 visual emphasizes API resources, not phases
- Reading orders favor API consumers (developer integrators)
- OpenAPI / AsyncAPI spec linked as primary entry point

## Open-source projects

When INDEX is public:

**Adjust:**
- Audience expanded: includes external users, contributors
- Reading orders include "First-time user", "Contributor"
- Link to CONTRIBUTING.md, CODE_OF_CONDUCT.md etc.

**Add:**
- License section
- "Status" badges (build, test coverage, etc.)

## Internal tools / non-product docs

When project is internal-only:

**Adjust:**
- Lighter formal weight
- Audience focused on internal roles
- Compliance section may be minimal (depending on data sensitivity)

## Multilingual projects

When docs in multiple languages:

**Adjust:**
- Per-language INDEX (e.g., `INDEX_VI.md`, `INDEX_EN.md`)
- Master INDEX links to language-specific versions
- Translation status per doc

## Versioned docs

When docs are versioned (e.g., per product release):

**Adjust:**
- Per-version INDEX (e.g., `INDEX-v3.md`, `INDEX-v4.md`)
- Latest INDEX symlinked or aliased to current version
- Diff section: "Changes from prior version"

---

## Index regeneration triggers

When to re-run this skill:

| Trigger | Frequency |
|---------|-----------|
| New doc added | Per-doc PR (small INDEX update) |
| Doc removed | Per-removal PR |
| Phase folder restructure | Per-restructure |
| Significant doc renaming | Per-event |
| Quarterly review | Quarterly (full re-validation) |
| `documentation-sync` flagged INDEX issues | Per-issue |

For active projects, INDEX touches every 1-2 weeks. For mature projects, monthly-quarterly.

## When INDEX becomes obsolete

Signs the INDEX should be regenerated wholesale:

- Filesystem and INDEX disagree on >20% of docs
- Section 7 audit log untouched in 6+ months (no maintenance)
- Multiple new sub-folders not represented
- Reading orders cite docs that no longer exist

Run this skill from scratch (don't patch incrementally) when these signs accumulate.

---

## Sub-INDEX pattern (for large projects)

For projects with 50+ docs:

```
docs/INDEX.md                        ← master, summary level
docs/00_REQUIREMENTS/_INDEX.md       ← phase 0 detailed
docs/01_DISCOVERY/_INDEX.md          ← phase 1 detailed
... etc.
```

Master INDEX links to phase INDEXes; phase INDEXes list per-doc. Avoids master INDEX growing unwieldy while preserving discoverability.

When using sub-INDEX pattern, this skill produces both master AND phase sub-INDEXes (or master only, with phase sub-INDEXes manual).
