# Project Context Ingestion — Quality Checklist

Run before publishing the Context Pack.

## Gate 1 — Source inventory completeness

- [ ] All sources enumerated in Section 2 with stable IDs (SRC-001…)
- [ ] Date, format, origin, sensitivity captured per source
- [ ] Anonymization status logged per source
- [ ] Operator confirmed nothing was forgotten (Slack, emails, prior consultant reports)
- [ ] Sources span ≥3 of 6 categories OR Section 9 names the missing categories as gaps

## Gate 2 — Per-claim citation

- [ ] Every claim in Sections 3-7 has at least one `[SRC-NNN]` citation
- [ ] No claim is sourced solely from "operator memory" — those go to Section 10
- [ ] Verbatim quotes (Section 3.2) cite source + speaker + date

## Gate 3 — Anonymization integrity

- [ ] No real personal names in pack (unless operator approved exception)
- [ ] No emails, phone numbers, addresses
- [ ] Customer names replaced with role + segment label
- [ ] Profanity / off-record commentary scrubbed
- [ ] If skipped, Section 11 explains why

## Gate 4 — Consensus / contradiction discipline

- [ ] Section 3.3 distinguishes high-confidence (≥2-3 sources) from single-source claims
- [ ] Section 8 surfaces real contradictions (not papered over)
- [ ] Each contradiction names the conflicting sources AND who must resolve it
- [ ] Section 9 names gaps explicitly (not silently omitted)

## Gate 5 — Open question quality

- [ ] Section 12 has ≥3 prioritized questions
- [ ] Each question has a "Why it matters" line tied to downstream impact
- [ ] Questions are blocking-or-not flagged
- [ ] Questions go to NAMED roles, not "stakeholders" generically

## Gate 6 — Operator hypothesis hygiene

- [ ] Operator inferences live in Section 10 only
- [ ] Each hypothesis labeled with confidence + how to confirm
- [ ] No hypothesis disguised as stakeholder voice in Sections 3-7

## Gate 7 — Coverage honesty

- [ ] Section 1 declares decision-readiness honestly
- [ ] Section 6 flags missing operational data if applicable
- [ ] Section 11 lists sources NOT consulted with reason
- [ ] Confidence rating in Section 11 matches reality (don't inflate)

## Gate 8 — Cross-skill hand-off

- [ ] Section 13 lists which downstream skills consume which sections
- [ ] CONTEXT_PACK.md saved to `docs/00_REQUIREMENTS/CONTEXT_PACK.md`
- [ ] Anonymized source files saved to `docs/00_REQUIREMENTS/_sources/SRC-NNN_*.md`

## Gate 9 — Mode discipline

- [ ] Mode A: 6 categories used
- [ ] Mode B: company framework cited; sections mapped
- [ ] Mode C: user-defined categories documented + rationale

## Gate 10 — No invention

- [ ] Pack contains nothing the sources don't support (except clearly-marked Section 10)
- [ ] No stakeholder paraphrased into views they didn't express
- [ ] Quotes verified verbatim against source files

## Self-review prompt

Pick 5 random claims in Sections 3-7. For each:
- Open the cited source file
- Verify the source actually says this
- Verify the citation isn't stretched (one offhand mention ≠ "stakeholders want X")

If 1+ of 5 fails verification, the pack is over-claiming. Tighten.

Then ask: "If a downstream operator runs `srs-greenfield-author` with ONLY this pack + the codebase, will they have to call stakeholders to fill gaps?" If yes — that's fine, but Section 12 must list those gaps as Open Questions. If no gaps are listed, you're hiding incompleteness.

## Final sanity check

Re-read Section 1 (Executive Summary). Is the "What we don't know" honest? Most projects DON'T know more than they know — if the section is short or empty, you're inflating confidence.
