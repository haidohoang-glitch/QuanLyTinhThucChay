# Project Context Ingestion — Worked Example

Anonymized example: **Project Pegasus**, a logistics SaaS rewrite. Operator received raw materials and used `project-context-ingestion` to produce CONTEXT_PACK.md before any Phase 0 work.

---

## Setup

**Project:** Pegasus — replace a 9-year-old logistics dispatch system used by ~40 mid-size logistics SMBs (50-200 employees each).

**Why context ingestion mattered:** The CTO had been at the company 1 year; founding engineer who built Pegasus left 6 months ago. There was nothing structured to start from. Operator collected raw materials from 4 internal teams + 6 customer interviews.

---

## Sources received (Section 2 of pack)

The operator inventoried 17 sources across all 6 categories:

| Source ID | Title | Format | Date | Origin | Sensitivity |
|-----------|-------|--------|------|--------|-------------|
| SRC-001 | CEO interview — vision + budget | audio + transcript (45 min) | 2026-04-12 | direct interview | PII |
| SRC-002 | CTO interview — technical pain | transcript (60 min) | 2026-04-13 | direct interview | PII |
| SRC-003 | CFO email — budget cap | email thread | 2026-04-14 | internal | PII |
| SRC-004 | "Vision deck v3" pitch | PDF | 2026-Q1 | internal | none |
| SRC-005 | Customer #1 interview (large fleet, 180 trucks) | transcript (40 min) | 2026-04-08 | customer call | PII (anonymized) |
| SRC-006 | Customer #2 interview (small fleet, 25 trucks) | transcript (40 min) | 2026-04-09 | customer call | PII (anonymized) |
| SRC-007 | Customers #3-#6 interviews | transcripts | 2026-04-10..15 | customer calls | PII (anonymized) |
| SRC-008 | Slack #pegasus-eng archive (6 months) | text export | 2025-10-01..2026-04-30 | internal | PII |
| SRC-009 | Competitor "FleetMaster" product tour | screenshots + notes | 2026-04-15 | public | none |
| SRC-010 | Competitor "Routify" pricing page | screenshot | 2026-04-15 | public | none |
| SRC-011 | Industry analyst report excerpt (logistics SaaS Q1 2026) | PDF | 2026-Q1 | analyst firm | confidential (license) |
| SRC-012 | Support tickets, top 50 of 2026 (categorized) | CSV export | 2026-04-30 | internal | PII (anonymized) |
| SRC-013 | Pegasus analytics dashboard snapshot | screenshots | 2026-04-30 | internal | none |
| SRC-014 | Churn report Q1 2026 | PDF | 2026-04-15 | internal | confidential |
| SRC-015 | Cost report (AWS spend) Q1 2026 | spreadsheet | 2026-04-15 | internal | confidential |
| SRC-016 | DOT Hours-of-Service regulation excerpt | PDF | 2024 (current version) | regulatory.gov | none |
| SRC-017 | AWS enterprise agreement (excerpt) | PDF | 2025 | internal/legal | confidential |

**Coverage:** 6/6 categories. Confidence rating: HIGH.

---

## Stakeholder Voice (Section 3 excerpt)

### What stakeholders want (consensus)

| Want | Confidence | Sources |
|------|------------|---------|
| Real-time route optimization (vs current 4 AM batch) | High | [SRC-001], [SRC-002], [SRC-005], [SRC-006], [SRC-007] |
| Mobile UI for drivers (current is desktop-only) | High | [SRC-001], [SRC-005], [SRC-006], [SRC-007] (all customers) |
| Excel export for monthly reporting (NOT to be removed) | High | [SRC-005], [SRC-006], [SRC-007], [SRC-012] |
| Reduce dispatcher manual intervention by ≥50% | Medium | [SRC-001], [SRC-002] only |
| GPS-vehicle integration (telematics) | Medium | [SRC-005], [SRC-007] (large customers); not mentioned by smaller |

### Key verbatim quotes

> "Our drivers literally Bluetooth-tether their phones to a 2018 Android tablet bolted to the cab — anything mobile-first would be a huge unlock." — [SRC-005], Customer #1 (large fleet ops manager), 2026-04-08

> "Excel exports are non-negotiable. My CFO opens Pegasus once a month, and only to download Excel. If you remove Excel, you lose us." — [SRC-006], Customer #2 (logistics SMB owner), 2026-04-09

> "We have $1.4M for 14 months. After that, we're shipping or shutting it down. Don't bring me a 24-month plan." — [SRC-001], CEO, 2026-04-12

---

## Operational Reality (Section 6 excerpt)

| Metric | Value | Source | Implication |
|--------|-------|--------|-------------|
| Active customers | 38 (down from 47 in 2025-Q1) | [SRC-013] | 9-customer churn — material |
| MAU per customer (avg) | 6 dispatchers + 12 drivers (mobile not used) | [SRC-013] | Driver mobile is greenfield, not migration |
| Top 3 support categories | Routing errors (32%); Login/perms (28%); Excel export breaks (19%) | [SRC-012] | Maps to 3 top FRs in future SRS |
| Annual churn | 19% (industry benchmark: 8-12%) | [SRC-014] | High — likely product fit issue |
| AWS spend monthly | $42K (current), forecast $35K post-rewrite | [SRC-015] | Architecture must reduce, not raise spend |

---

## Constraints (Section 7 excerpt)

### Regulatory

| Requirement | Source | Affects |
|-------------|--------|---------|
| DOT Hours-of-Service: drivers cannot exceed 11 hrs driving / 14 hrs on-duty | [SRC-016] | Routing engine MUST enforce; M3 routing FR; M9 NFR for accuracy |

### Contractual

| Constraint | Source | Affects |
|------------|--------|---------|
| AWS commit through 2028 (~$1.8M remaining commitment) | [SRC-017] | tech-solution-design must use AWS-native; GCP/Azure off the table |

### Budget / timeline

| Constraint | Stated by | Source |
|------------|-----------|--------|
| Budget cap | $1.4M total | [SRC-001], CEO |
| Hard deadline | 14 months from approval | [SRC-001], CEO |

---

## Contradictions (Section 8)

| ID | Topic | Position A | Position B | Sources A | Sources B | Resolution |
|----|-------|-----------|-----------|-----------|-----------|------------|
| CON-1 | Approach | "Clean rewrite" | "Incremental refactor only" | [SRC-001] CEO | [SRC-002] CTO | Joint CEO+CTO call before Phase 2 starts |
| CON-2 | Driver mobile priority | "Must-have, day-1" | "Phase 2, after dispatcher MVP" | [SRC-005], [SRC-007] (customers) | [SRC-002] (CTO — capacity concern) | Resolve in feasibility scenarios — show cost diff |
| CON-3 | Pricing tiers | "Keep 3 tiers" | "Simplify to 2" | [SRC-001] CEO | [SRC-006] (small customer wants single price) | Defer; pricing is post-launch decision |

---

## Gaps (Section 9)

| Gap | Why it matters | How to close |
|-----|----------------|--------------|
| No interviews with dispatchers (the daily users) | All customer interviews were with owners/ops managers, not the people using Pegasus 8 hrs/day | Run 5 dispatcher interviews before SRS — biggest UX risk if skipped |
| No data on competitor pricing models beyond public list price | Feasibility ROI scenarios will be hand-wavy | Sales team has done win/loss analyses — pull internal data |
| No security audit of legacy Pegasus | Migration risk unknown | Internal sec review needed; not yet scheduled |

---

## Open Questions (Section 12)

| # | Question | Why | Ask of | Blocking? |
|---|----------|-----|--------|-----------|
| Q1 | Rewrite or incremental refactor? | Determines Phase 2 entirely | CEO + CTO together | **Yes** |
| Q2 | Driver mobile day-1 or Phase 2? | Drives 14-month vs 18-month timeline | CEO (with cost data from feasibility) | **Yes** |
| Q3 | Telematics integration in-scope or out? | Affects 3 customer renewals (per [SRC-005], [SRC-007]) | Head of Customer Success | **Yes** |
| Q4 | Will dispatchers be interviewed? | Closes biggest UX gap | Operator + Head of CS | No (but recommended) |
| Q5 | What does "mobile-first" mean — PWA, native iOS, Android? | Tech stack decision | CTO | No (Phase 2) |

---

## Hand-off (Section 13 in pack)

After publishing CONTEXT_PACK.md, downstream skills consumed it as follows:

- **`srs-greenfield-author`** — drew M3 (routing) FRs from [SRC-016] DOT regulations + customer routing pain ([SRC-005], [SRC-007]); M4 (mobile driver app) from customer voice; M9 NFRs from [SRC-016] safety + [SRC-014] performance benchmarks. M10 Open Issues populated directly from Section 12 of pack.
- **`feasibility-assessment`** — used [SRC-001] $1.4M / 14-month constraint to bound scenarios (Full $1.4M / Partial $900K / Minimum $400K); [SRC-014] churn data to estimate revenue at risk if scope cut.
- **`tech-solution-design`** — used [SRC-017] AWS commit to scope candidate stack; [SRC-015] cost forecast to set NFR budget for solution architecture.
- **`nfr-specification`** — used [SRC-016] regulatory constraints + [SRC-013] performance baseline to set quantitative NFRs.

Without this pack, each downstream skill would have re-extracted these facts independently — and likely missed CON-1 (the rewrite-vs-refactor disagreement), which then blew up in Phase 2 feasibility review when the CTO rejected the strategy chosen by the CEO. The pack surfaced the conflict before either side committed.

---

## What this example illustrates

1. **Coverage matters.** 6/6 categories meant high confidence. With only 2-3 categories the pack would have flagged itself as LOW confidence.
2. **Contradictions surface early.** CON-1 (rewrite vs refactor) was not an SRS or feasibility problem — it was a stakeholder-alignment problem. Catching it in ingestion saved weeks of rework.
3. **Quotes drive priority.** "Excel exports are non-negotiable" became a Must-have FR, not a nice-to-have, because it was a customer's gating purchase criterion.
4. **Gaps are findings.** "No dispatcher interviews" got documented; the operator scheduled them before SRS finalization.
5. **Operational data anchors stakeholder claims.** CEO said "drivers love the system" — but [SRC-013] showed 0 driver MAU because no driver UI existed. The data won.

---

*This example is anonymized. Real Pegasus is fictional. Numbers and quotes illustrate skill output shape, not real contracts.*
