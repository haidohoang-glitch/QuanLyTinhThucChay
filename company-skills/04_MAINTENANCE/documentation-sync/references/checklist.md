# Documentation Sync — Quality Checklist

Run before publishing the sync report.

## Gate 1 — Coverage discipline

- [ ] All docs in `docs/` accounted for (opened at least once OR explicitly skipped with reason)
- [ ] Section 5 Coverage Statement honest: lists what was checked vs. skipped
- [ ] Confidence rating reflects coverage (don't claim High if half was skipped)

## Gate 2 — Per-finding rigor

- [ ] Every finding has: doc path, specific issue, detection method, remediation, owner, target date
- [ ] Specifics not vague: "command on line 42 references obsolete host" beats "command outdated"
- [ ] Remediation actionable (not "investigate")
- [ ] Owner named (role at minimum; person ideally)

## Gate 3 — Severity calibration

- [ ] Critical: doc actively misleads (would cause incident or harm)
- [ ] High: significantly out of date but not actively dangerous
- [ ] Medium: stale specifics; core message still correct
- [ ] Low: cosmetic
- [ ] No "all Critical" inflation
- [ ] No "everything Low" downplay

## Gate 4 — Pattern recognition

- [ ] Section 4 Systemic Findings has ≥1 pattern (most projects have at least one process gap)
- [ ] Pattern findings link to specific evidence (multiple findings supporting same root cause)
- [ ] Each pattern has process recommendation (not just doc fix)

## Gate 5 — Action items tracking

- [ ] Section 6 has every finding's action item with owner + target
- [ ] Critical actions ≤ 1 week target
- [ ] High actions ≤ 30 days target
- [ ] Medium / Low can be batched but still scheduled

## Gate 6 — Trend tracking

- [ ] Section 7 lists findings resolved since last report (for trend visibility)
- [ ] If first report, note "first run" explicitly

## Gate 7 — Recommendations forward-looking

- [ ] Section 9 has ≥2 systemic recommendations
- [ ] Recommendations target prevention, not just per-finding fixes
- [ ] Recommendations actionable

## Gate 8 — Mode discipline

- [ ] Mode A: standard 10 categories checked
- [ ] Mode B: company framework cited
- [ ] Mode C: user-defined dimensions; rationale documented

## Gate 9 — Format

- [ ] Output: `docs/04_MAINTENANCE/DOC_SYNC_REPORT.md`
- [ ] Prior version archived: `_archive/DOC_SYNC_REPORT_<DATE>.md`
- [ ] Finding IDs follow `DRIFT-<SEVERITY-SHORTHAND><N>` (e.g., DRIFT-C1, DRIFT-H2)
- [ ] Tables consistent

## Gate 10 — Honesty

- [ ] If you skipped some checks (process review, etc.), said so
- [ ] If automation didn't run on some docs, said so
- [ ] No false positives (verify each finding before reporting)
- [ ] No false confidence ("looks fine" when only 30% was checked)

## Self-review prompt

Pick 5 random findings. For each:
- Open the cited doc; verify the issue is real (not auto-detection false positive)
- Verify the remediation makes sense
- Confirm owner is the right person

If 1+ of 5 fails, the report has noise. Trim or sharpen before publishing.

Then ask: "If I'm a new team member reading this report, do I trust the docs more or less after fixes?" Trust gain is the value.
