# Tech Debt Audit — Quality Checklist

Run before delivering `TECH_DEBT_AUDIT.md`.

## Gate 1 — Coverage

- [ ] Every category in the chosen mode has been explicitly hunted for findings (or "no findings" recorded with what was checked)
- [ ] Section 2 includes at minimum: test coverage, lint, type errors, dep audit, outdated deps
- [ ] Each finding has: severity, effort, evidence pointer, one-line title
- [ ] Section 5 has ≥1 cluster (most projects have repeated root causes; if you found zero, you may have under-clustered)
- [ ] Section 6 Top 10 list has 10 items, ordered by priority
- [ ] Section 7 aggregate matrix has counts for every cell
- [ ] Section 8 Open Questions has ≥3 items
- [ ] Section 9 documents categorization mode and rationale

## Gate 2 — Severity discipline

- [ ] P0 count is ≤ 5 (more than 5 P0 = inflation, recalibrate)
- [ ] Every P0 has an explicit failure mode with timeline (<7 days)
- [ ] Every P1 has an explicit 90-day risk articulated
- [ ] No "P0 because it offends my taste" — must be observable risk

## Gate 3 — Evidence quality

- [ ] Every finding cites a file path (and line where possible) OR a query/command result
- [ ] No findings of the form "consider improving X" — must be specific
- [ ] If a finding required interpretation (not direct evidence), it's labeled "Inferred"
- [ ] No findings copy-pasted from generic best-practice guides without verifying they apply

## Gate 4 — Effort calibration

- [ ] Effort estimates respect the rubric (XS <2h, S 2-8h, M 1-3d, L 3-10d, XL >2w)
- [ ] Effort doesn't pretend false precision (no "4.7 hours")
- [ ] Aggregate effort total is sanity-checked: does the sum match the size of debt the project actually has?

## Gate 5 — Scope discipline

This skill produces a *findings list*. It must NOT include:

- [ ] No fix designs (those go to `tech-solution-design`)
- [ ] No implementation plans (those go to `implementation-planning`)
- [ ] No business priority decisions (severity is technical, not business — let stakeholders weigh business factors)
- [ ] No data-layer findings unrelated to code (those may go to `data-architecture-audit`)

## Gate 6 — Format

- [ ] Output filename: `TECH_DEBT_AUDIT.md`
- [ ] Output location: `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md`
- [ ] Finding IDs are sequential `F-01`, `F-02`, ...
- [ ] Open Question IDs `OQ-1`, `OQ-2`, ...
- [ ] Section headings match template

## Self-review prompt

Re-read the Top 10 Punch List as the engineer who'll start fixing tomorrow. For each item, ask: "Is the description specific enough that I can start without asking 'where do I begin'?" If not, sharpen the evidence.
