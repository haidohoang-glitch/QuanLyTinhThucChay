# Requirements Traceability — Quality Checklist

Run before delivering M10 RTM.

## Gate 1 — Coverage of Reqs

- [ ] Every FR-XXX-NN from M3-Mx has a row in 10.1.0
- [ ] Every NFR-XXX-NN from M9 has a row in 10.1.1
- [ ] No requirement is silently skipped — if an FR is intentionally excluded, document why in 10.1.3 Findings
- [ ] Total Reqs in 10.1.2 statistics matches sum of M3-Mx + M9

## Gate 2 — Per-row rigor (CRITICAL)

For each row, verify:

- [ ] Design column is non-empty: ADR ID, doc section, OR explicit "Implicit (not formally designed)" + flagged in Findings
- [ ] Code column references actual file path(s); paths exist in current commit
- [ ] Test column references actual test names/IDs that exist
- [ ] Status reflects most recent test run (not stale by >30 days)
- [ ] Last verified date is honest: matches last actual review, not just "today"

## Gate 3 — Honesty (audit-grade)

This is the gate auditors care about most:

- [ ] No "PASS" status without verifiable evidence (CI run ID, test report, audit doc)
- [ ] No invented test names — if a test doesn't exist, status is "NOT IMPLEMENTED" not "PASS"
- [ ] No stale data — if test hasn't run in >30 days, re-run before publishing OR status is "NOT RUN" with date
- [ ] Coverage statistics computed from actual data; round to nearest %, no false precision
- [ ] If sampled-verification done (e.g., 10% spot-check), document method and date

## Gate 4 — Orphan analysis

- [ ] Every orphan requirement (no code OR no test) listed in 10.1.3 Findings with severity + recommended action
- [ ] Orphan code paths investigated — at minimum, documented with "likely category" (utility, dead code, missing Req, etc.)
- [ ] Orphan tests investigated — categorize as acceptable (fixture/infra) or flag for missing Req
- [ ] Failing tests listed in 10.1.3 Findings table with owner + target fix date

## Gate 5 — Trace bidirectionality

- [ ] For each test in the test suite, can you trace it back to a Req? (Spot-check: 10 random tests)
- [ ] For each Req, can you trace forward to test? (Already covered by row population)
- [ ] Bidirectional gaps documented as orphans

## Gate 6 — Mode discipline

- [ ] If Mode A: all 4 standard columns present (Design, Code, Test, Status)
- [ ] If Mode B: company template followed faithfully; cited at 10.1
- [ ] If Mode C: user-confirmed columns present; rationale documented at 10.1

## Gate 7 — NFR verification rigor

NFRs have non-test verification methods. Verify:

- [ ] Performance NFRs: reference load test artifact (file path + last-run date) OR production monitoring screenshot/dashboard URL
- [ ] Security NFRs: reference audit report, pen test result, or configuration review
- [ ] Compliance NFRs: reference external audit (with auditor name + date) for fully verified; OR "not yet audited" with target date
- [ ] Reliability NFRs: reference incident log, uptime report, or DR drill record

Avoid: NFR "PASS" with no artifact link. Auditors reject this.

## Gate 8 — Findings actionable

In 10.1.3, every finding has:
- [ ] Severity (High / Medium / Low)
- [ ] Recommended action (specific, not "investigate")
- [ ] Owner (named role or person)
- [ ] Target date (or explicit "TBD pending {{}}")

## Gate 9 — Open Issues preserved + extended

- [ ] All Open Issues from prior SRS author skills preserved in 10.2
- [ ] New Open Issues from RTM findings added with proper IDs (ISS-NN)
- [ ] No issues silently closed or removed without resolution doc

## Gate 10 — Maintenance approach documented

- [ ] 10.1.5 explains how RTM stays current (per-PR? quarterly? auto-gen?)
- [ ] Maintenance owner named per activity
- [ ] If RTM is partly auto-generated, tools and scope cited in 10.3.E

## Gate 11 — Format

- [ ] Output filename: `M10_RTM_Issues_Appendix.md`
- [ ] Output location: `docs/00_REQUIREMENTS/SRS_VI/`
- [ ] Section numbering matches template (10.1 RTM, 10.2 Open Issues, 10.3 Appendix, 10.4 Sign-off)
- [ ] Tables use consistent column layout
- [ ] Code paths use `path/to/file.ts` format consistently

## Self-review prompt

Pick **5 random rows** from your RTM. For each:

1. Open the SRS — does the Req still match? (Sometimes Reqs are renamed in SRS; RTM goes stale.)
2. Open the cited code path — does the code still implement what the Req describes?
3. Open the test file — does the test still exist with that name?
4. Check last test run — was it actually recent?

If any of the 5 fails any check, the RTM as a whole has accuracy issues. Don't claim higher accuracy than your sample suggests.

Then ask:

> "If an auditor opened this RTM tomorrow and demanded evidence for FR-XXX-NN, could I produce it within 10 minutes?"

If not for all rows, the RTM doesn't yet earn audit-grade trust. Sharpen evidence pointers.
