# Feasibility Assessment — Quality Checklist

Run before delivering FEASIBILITY_ASSESSMENT.md.

## Gate 1 — Question precision

- [ ] Section 1 states exactly ONE question (go/no-go OR scope OR comparison)
- [ ] Question is in stakeholder language, not technical jargon
- [ ] Stakeholder confirmed the question before analysis began

## Gate 2 — Coverage

- [ ] Section 4 (Cost of Inaction / Do nothing baseline) populated with quantified line items
- [ ] At least 3 scenarios in Section 5 (or per Mode B/C structure)
- [ ] Section 5: each scenario has Scope, Cost, Benefit, Payback, Risks
- [ ] Section 6 side-by-side comparison includes "Do nothing" column
- [ ] Section 7 Assumptions: ≥3 explicit assumptions with confidence + falsification consequence
- [ ] Section 8 Stakeholder Impact covers ≥4 stakeholder types
- [ ] Section 9 Recommendation states scenario + top 3 reasons + change conditions
- [ ] Section 11 Open Questions ≥2

## Gate 3 — Numerical rigor

- [ ] Every cost/benefit number has a basis (calc shown or source cited)
- [ ] Costs use ranges where uncertain ("$80K-$120K") not false precision ("$98,742")
- [ ] Engineering cost calc explicit: hours × $/hr with both shown
- [ ] Infrastructure delta is `new - current`, not just `new total`
- [ ] Year-1 and Year-3 separated (different sums)
- [ ] ROI formula shown: `(Benefit - Cost) / Cost × 100%`
- [ ] Payback period in months, not "soon"

## Gate 4 — Honesty

- [ ] No advocacy language ("we definitely should", "the obvious choice")
- [ ] No inflated benefits (revenue uplift > 2-3x current is suspicious; require strong basis)
- [ ] No hidden assumptions — all in Section 7
- [ ] Confidence levels (H/M/L) match underlying data quality
- [ ] If a number is a guess, says so — does not pretend rigor

## Gate 5 — Stakeholder readability

- [ ] Section 1 Executive Summary readable by non-technical exec in 2 minutes
- [ ] Side-by-side Section 6 understandable without reading other sections
- [ ] No engineering jargon in Sections 1, 6, 9 (the sections leadership reads)
- [ ] Numbers in $ (or local currency) with units
- [ ] Comparisons easy: "Partial saves $X over Full but defers Y compliance"

## Gate 6 — Recommendation defensibility

- [ ] Recommendation logically follows from analysis (no surprises)
- [ ] Top 3 reasons cite specific data (cost difference, ROI, risk closed)
- [ ] "What would change the recommendation" present and specific
- [ ] If recommendation is "do nothing", that's also explicit (rare but valid sometimes)

## Gate 7 — Mode discipline

- [ ] Mode A: 3 scenarios + "Do nothing" baseline
- [ ] Mode B: company template followed; cited at Section 1
- [ ] Mode C: user-confirmed scenarios; rationale documented

## Gate 8 — Format

- [ ] Output: `docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md`
- [ ] Tables consistent and readable
- [ ] Currency notation consistent ($ K vs $)
- [ ] Recommendation in Section 9, not buried elsewhere

## Self-review prompt

Read the document as a skeptical CFO. Where would you push back? Sharpen those points before publishing.

Then read as the engineering lead. Are the costs realistic? Sharpen if optimistic.

Then read as the customer success lead. Are stakeholder impacts captured beyond engineering? Sharpen if narrow.
