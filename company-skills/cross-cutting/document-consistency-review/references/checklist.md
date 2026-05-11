# Document Consistency Review — Quality Checklist

Run before publishing the consistency report.

## Gate 1 — Coverage

- [ ] All 8 dimensions checked (Mode A) OR per chosen mode
- [ ] Section 4 Terminology audit completed
- [ ] Section 5 Reference validity check completed
- [ ] Section 6 Version + status consistency checked
- [ ] Section 7 Decisions consistency checked
- [ ] Coverage statement honest about what was sampled vs full

## Gate 2 — Per-finding rigor

- [ ] Each finding has: conflict description, docs involved (with line numbers), canonical source, remediation, owner, target
- [ ] Specifics not vague (line numbers, exact text quoted)
- [ ] Canonical source justified (why this doc wins?)

## Gate 3 — Severity calibration

- [ ] Critical: affects decisions / commitments
- [ ] High: system-wide naming OR broken cross-references
- [ ] Medium: localized
- [ ] Low: cosmetic
- [ ] No "all Critical" inflation

## Gate 4 — Terminology audit rigor

- [ ] Section 4 lists terms with multiple variants
- [ ] All locations of each variant cited
- [ ] Canonical recommendation for each (not "fix later")

## Gate 5 — Pattern recognition

- [ ] Section 10 has ≥1 systemic pattern
- [ ] Pattern findings link to specific evidence (multiple findings)
- [ ] Recommendations target prevention

## Gate 6 — Action items

- [ ] Section 8 has every finding's action item
- [ ] Critical actions ≤ 1 week
- [ ] High actions ≤ 30 days
- [ ] Owner specific (named role or person)

## Gate 7 — Trend tracking

- [ ] Section 9 lists resolved findings since last run
- [ ] If first run, note "first run" explicitly

## Gate 8 — Mode discipline

- [ ] Mode A: 8 dimensions
- [ ] Mode B: company checklist cited
- [ ] Mode C: user-defined dimensions; rationale documented

## Gate 9 — Format

- [ ] Output: `docs/04_MAINTENANCE/CONSISTENCY_REVIEW_REPORT.md`
- [ ] Prior version archived
- [ ] Finding IDs follow `INC-<SEVERITY-SHORTHAND><N>` (INC-C1, INC-H2, INC-M3, INC-L4)

## Gate 10 — Honesty

- [ ] If auto-detection used, note false-positive rate
- [ ] If manual review sampled, sample size noted
- [ ] No false confidence ("looks consistent" without evidence)
- [ ] Self-doubt encouraged: most projects have inconsistencies; finding 0 is suspicious

## Self-review prompt

Pick 5 random findings. For each:
- Open both cited docs; verify the conflict is real (not auto-detect false positive)
- Verify canonical source recommendation makes sense

If 1+ of 5 fails, report has noise. Trim or sharpen.

Then ask: "Could a stakeholder reading both docs be confused or make wrong decision?" If yes → severity is right. If "minor", consider Low.
