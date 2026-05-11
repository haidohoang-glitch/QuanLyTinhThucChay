# Codebase Discovery — Quality Checklist

Run this checklist before delivering `CODEBASE_MAP.md`. Do not deliver until ALL gates pass. If a gate cannot be satisfied, document why in Section 9 (Notes & Caveats) of the output.

## Gate 1 — Completeness

- [ ] Every `{{PLACEHOLDER}}` in the template is filled or explicitly marked "Unknown — {{reason}}"
- [ ] Section 1 Executive Summary fits in <150 words
- [ ] Section 2 Tech Stack lists at minimum: language/runtime, framework, primary data store, build tool
- [ ] Section 3 Folder Structure shows top 2 levels (no deeper unless critical)
- [ ] Section 4 Module Boundaries has 5-25 modules (Mode A) OR follows the chosen Mode B/C taxonomy; if outside expected range, justify
- [ ] Section 5 External Dependencies lists every service the app talks to
- [ ] Section 6 Build & Deploy includes commands a new dev can copy-paste
- [ ] Section 7 Entry Points covers every way the codebase starts (server, CLI, workers, build hooks)
- [ ] Section 8 Open Questions has ≥3 items
- [ ] Section 9 Notes documents the **classification mode** (A / B / C) and the rationale

## Gate 2 — Honesty

- [ ] No invented information — every fact is verifiable from the codebase
- [ ] Things I had to guess are marked as "inferred" or moved to Open Questions
- [ ] Confidence rating in Section 9 reflects actual confidence, not desired confidence
- [ ] If I disabled or skipped any normal discovery step (e.g., did not run build), it's documented
- [ ] If classification mode was ambiguous (e.g., codebase had partial architecture docs), I asked the user instead of silently picking Mode A or B

## Gate 3 — Usefulness

A new engineer reading this map should be able to answer in <5 minutes:
- [ ] What does this project do? (Section 1)
- [ ] What stack? (Section 2)
- [ ] Where is feature X? (Section 4 module map)
- [ ] What does it depend on externally? (Section 5)
- [ ] How do I run/build/test it? (Section 6)
- [ ] What's confusing or risky? (Section 8)

If you cannot answer YES to all six, the map is incomplete.

## Gate 4 — Scope discipline

This skill produces *descriptive* technical structure. It must NOT include:

- [ ] No business logic explanation (that belongs in `business-context-capture`)
- [ ] No improvement proposals (that belongs in `tech-debt-audit` and `tech-solution-design`)
- [ ] No implementation plans (that belongs in `implementation-planning`)
- [ ] No security findings (that belongs in `tech-debt-audit`)
- [ ] No opinions about whether the architecture is "good" — only what it IS

If you find yourself writing recommendations, stop and move that content to the appropriate downstream skill output.

## Gate 5 — Format

- [ ] Output filename: `CODEBASE_MAP.md`
- [ ] Output location: `docs/01_DISCOVERY/CODEBASE_MAP.md` (per company doc standard)
- [ ] All section headings match the template (do not rename or reorder)
- [ ] Tables have headers; tables are not converted to bullet lists
- [ ] Code blocks have language hints (` ```bash `, ` ```typescript `)
- [ ] Internal links use relative paths

## Self-review prompt

After filling the template, re-read your output as if you were a new hire who has never seen this codebase. Ask: "What's still confusing?" Add those items to Section 8 Open Questions.
