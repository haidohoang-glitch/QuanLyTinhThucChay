# SRS Reverse Engineer — Quality Checklist

Run before delivering the reverse-engineered SRS module set.

## Gate 1 — Inputs verified

- [ ] `BUSINESS_CONTEXT.md` exists and was generated/refreshed within last 60 days
- [ ] `CODEBASE_MAP.md` exists and matches current code (sample 3-5 files to confirm)
- [ ] `DATA_ARCHITECTURE.md` exists; if not, document M2.5 constraint section as "lower confidence"
- [ ] Live UI verified (where possible) — at least 3 use cases observed end-to-end
- [ ] If any input is stale, the affected sections are marked "lower confidence" in M10

## Gate 2 — Coverage

Same as `srs-greenfield-author` Gate 1, plus:

- [ ] M1.1 explicitly states "This is a reverse-engineered as-is SRS"
- [ ] M1.4 references include the git commit hash (or branch + date) of the code state captured
- [ ] M2.5 distinguishes intentional constraints from accidental constraints (legacy lock-in)
- [ ] M3-Mx: every FR has source citation pointing to code (file:line) or doc, NOT to invented stakeholders
- [ ] M9 placeholder notes that `DATA_ARCHITECTURE.md` Section 6 + `TECH_DEBT_AUDIT.md` (if exists) provide head start
- [ ] M10 Open Issues has ≥10 items (reverse-engineering always has gaps; small list = under-thoroughness)

## Gate 3 — Source rigor (CRITICAL for reverse-engineering)

- [ ] No FR sources stakeholders who didn't actually confirm — every FR is sourced from observable code/UI
- [ ] Source format: "Reverse-engineered from `<path:line>`" or "Observed in UI at <screen>"
- [ ] FRs marked "Inferred — not verified live" if behavior derived from code but not observed running
- [ ] Where intent is unclear, FR description sticks to what code does; "Why?" goes to Open Issues

## Gate 4 — Honesty (specific to reverse-engineering)

- [ ] Did not invent priority — defaulted all to Must with caveat, OR added a "Was this intentional?" sub-field
- [ ] Did not pretend to know intent ("FR shall validate X *to ensure Y*" — drop the *to ensure* unless you know)
- [ ] Documented behaviors that look buggy as Open Issues, NOT as requirements
- [ ] If a behavior is gated by feature flag and you only saw one path, that's noted
- [ ] Confidence ratings calibrated honestly per module (most reverse-engineered SRSs have Medium confidence at best)

## Gate 5 — Per-FR rigor

(Same as greenfield, plus:)

- [ ] Each FR's acceptance criteria match what the system *currently* does, not what it *should* do
- [ ] Where the system currently does the wrong thing (per `BUSINESS_CONTEXT.md` invariant violations), this is captured as Open Issue, not as accepted FR
- [ ] FRs that depend on undocumented external system behavior (third-party API, vendor SDK) note this dependency

## Gate 6 — Constraint capture

- [ ] M2.5 includes implicit constraints from being locked into current tech stack (database choice, language, deployment)
- [ ] Regulatory constraints from `DATA_ARCHITECTURE.md` Section 6 fully transferred to M2.5
- [ ] "Accidental constraints" (legacy decisions) flagged for review — these are candidates for relaxation in a rewrite
- [ ] Performance/scaling constraints from current production observed (e.g., "currently handles 1K req/s; not tested above")

## Gate 7 — Scope discipline

- [ ] No solution proposals (e.g., "system *should* be migrated to X" → that's `tech-solution-design`)
- [ ] No improvement recommendations (those go to `tech-debt-audit` if not already there)
- [ ] No future-state speculation in M3-Mx — if it's not in code, it's not in M3-Mx (move to M10 Open Issues if it's a known gap)

## Gate 8 — Format

(Same as greenfield, plus:)

- [ ] Output files at `docs/00_REQUIREMENTS/SRS_VI/`
- [ ] M1.4 references explicitly cite Discovery outputs (`BUSINESS_CONTEXT.md` v?, `CODEBASE_MAP.md` v?)
- [ ] M10.3 Appendix includes a "Source-to-FR map" table summarizing where each FR was extracted from

## Self-review prompt

For each module, ask:

> "If an auditor opens the codebase and tries to verify FR-XXX-NN, can they find the corresponding code in <5 minutes using the cited source?"

If not, the source is too vague. Sharpen.

Then, for the SRS as a whole:

> "Does this SRS describe what the system DOES (verifiable today), or what we wish it did (aspirational)?"

The answer must be the former. Otherwise this SRS misleads auditors and rewrites alike.
