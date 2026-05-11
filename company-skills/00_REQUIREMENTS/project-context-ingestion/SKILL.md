---
name: project-context-ingestion
description: Ingest raw project context — user interview transcripts, stakeholder discussion notes, requirements emails, RFPs, competitor screenshots, regulatory excerpts, ops data, prior tribal-knowledge docs — and produce a structured CONTEXT_PACK.md that downstream skills (srs-greenfield-author, srs-reverse-engineer, business-context-capture, feasibility-assessment) consume. Use BEFORE Phase 0/1 work to ensure requirements derive from real stakeholder voice + constraints, not just code reading. Triggers include "ingest project context", "process user interviews", "consolidate raw inputs", "build context pack", "what do stakeholders want", or "before Phase 0".
---

# Project Context Ingestion

Convert messy real-world inputs (interview recordings, emails, slides, regulatory PDFs, competitor screenshots, ops dashboards) into a single structured `CONTEXT_PACK.md` that captures stakeholder voice, business constraints, and operational reality. This pack feeds Phase 0 Requirements + Phase 1 Discovery + Phase 2 Strategic skills, so they no longer rely on the operator to manually re-extract context every time.

## Why this skill exists

Reading the codebase tells you WHAT the system does, never WHY. Without raw stakeholder voice + business constraints + ops data, downstream skills (especially SRS authoring, business context, feasibility) silently fall back on assumptions or operator memory — which doesn't scale across 60+ projects and rotates with team members.

This skill is the upstream funnel: take everything the project owners hand over, extract the load-bearing facts, cite them, and produce a pack the rest of the suite can trust.

## When this skill applies

Use when:
- Starting a new engagement with raw materials in hand (Slack archives, interview transcripts, RFP docs, competitor analyses, regulatory PDFs)
- Before running `srs-greenfield-author` (so SRS draws from real stakeholder voice, not vibes)
- Before running `srs-reverse-engineer` or `business-context-capture` (to layer business intent onto code findings)
- Before `feasibility-assessment` (to surface stakeholder-imposed constraints early)
- Re-ingesting after a major stakeholder change (new exec, new compliance requirement, pivot)

Do NOT use for:
- Pure code reading (use `codebase-discovery`)
- Producing the SRS itself (this is upstream of `srs-greenfield-author`)
- Producing BUSINESS_CONTEXT.md (that's `business-context-capture`; this provides INPUT to that skill)
- Cleaning up already-structured docs (this is for raw → structured)

## Inputs (raw materials)

Anything the project owners hand over. The skill organizes them into 6 categories:

| # | Category | Examples |
|---|----------|----------|
| 1 | **User research** | Interview recordings/transcripts, user surveys, usability test notes, support tickets, NPS comments |
| 2 | **Internal communication** | Stakeholder Slack threads, emails about the project, meeting minutes, decision logs |
| 3 | **Existing informal docs** | Pitch decks, brain-dump Google docs, whiteboard photos, prior consultant reports, RFPs |
| 4 | **External context** | Competitor screenshots, market reports, analyst writeups, comparable products' docs |
| 5 | **Operational data** | Analytics dashboards, error logs, support volume by feature, churn data, cost reports |
| 6 | **Constraints & compliance** | Regulatory excerpts, legal requirements, contract obligations, vendor lock-ins, SLA commitments |

If the operator has only 1-2 categories of input, that is itself a finding — flag it as a gap.

## Output

Primary: `docs/00_REQUIREMENTS/CONTEXT_PACK.md`, filled from [assets/CONTEXT_PACK_template.md](assets/CONTEXT_PACK_template.md).

Optional companion: `docs/00_REQUIREMENTS/_sources/` — anonymized copies of the raw inputs (one file per source) so downstream readers can verify quotes. Each source file gets a stable ID (`SRC-001`, `SRC-002`, …) referenced from the pack.

## Workflow

### Step 1 — Inventory all sources

Before processing anything, list every artifact the operator has provided. Sources may live in:

- A handover folder (Drive, Notion, SharePoint export)
- A chat archive
- The operator's own notes
- Linked external URLs (publish status: stable? could rot?)

Build a flat inventory table:

| Source ID | Title | Format | Date | Origin | Sensitivity |
|-----------|-------|--------|------|--------|-------------|
| SRC-001 | "CEO interview 2026-04-12" | audio + transcript | 2026-04-12 | direct interview | PII (named individual) |
| SRC-002 | "Competitor Acme product tour" | screenshots | 2026-04-15 | public web | none |
| SRC-003 | "GDPR Article 17 excerpt" | PDF page | 2026-04-15 | regulatory.eu | none |
| SRC-004 | "Slack #project-helix archive" | text export | 2026-01-01..2026-04-30 | internal | PII (multiple individuals) |

Stop here and confirm with operator: is anything missing? People often forget the unstructured stuff (Slack, emails) until prompted.

### Step 2 — Choose ingestion mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard 6-category framework** *(default)* | No company-specific research process | The 6 categories above |
| **B — Honor company research framework** | Company uses Jobs-to-be-Done / Design Thinking / specific UX research format | Company framework |
| **C — User-defined categories** | Operator specifies own taxonomy (e.g., by stakeholder type, by decision node) | User input |

Selection logic:
1. User explicit → use it
2. Company has a research playbook (e.g., a UX research wiki) → ask which sections are required
3. Default → Mode A

### Step 3 — Anonymize and handle PII

Default behavior: **anonymize-by-default**. Most projects either (a) don't need real names in the pack or (b) eventually share the pack with parties who shouldn't see them.

For each source containing PII:
- Replace named individuals with role labels: "CEO", "Customer #3", "Support agent A"
- Replace company names (if customer interviews) with "Customer (logistics SMB, ~50 employees)"
- Strip emails, phone numbers, addresses
- Preserve role + context (so quotes are still attributable to a perspective)

Skip anonymization ONLY if operator confirms:
- Pack will stay strictly internal AND
- Real attribution adds decision value (e.g., "the CFO said X" matters for political weight)

Either way, log the choice in Section 11 (Notes & Caveats) of the pack.

### Step 4 — Extract insights per source

For each source, do a focused pass extracting only what's load-bearing for the project. Write to a scratch file per source first, then merge.

For each source, capture:

- **Source one-liner** — what is this artifact?
- **Key claims / facts** — bullets, each with a verbatim quote when meaningful
- **Implied requirements** — what would have to be true for this claim to hold? (e.g., "user said 'I refresh hourly to check status' → implies real-time or near-real-time status surfacing is a Should)
- **Constraints surfaced** — anything that bounds the solution space (regulatory, budget, timeline, vendor)
- **Open questions** — claims that are vague, contradicted, or need follow-up
- **Confidence** — High / Medium / Low (how certain are we this generalizes vs. is one person's opinion?)

Resist over-extracting. If a source has 50 bullets, you've quoted the artifact, not extracted insight. Aim 5-15 load-bearing items per source for medium-density inputs.

### Step 5 — Cross-reference: consensus, contradictions, gaps

Now look ACROSS sources. This is where the value compounds.

Build three lists:

**Consensus** — claims that ≥3 sources agree on. These are high-confidence inputs to SRS / business context.
> Example: "Reporting must export to Excel" — confirmed by SRC-001 (CEO), SRC-007 (CFO email), SRC-012 (support tickets). Treat as a near-certain Must.

**Contradictions** — different stakeholders saying opposite things. These are the most valuable findings — they need stakeholder resolution before SRS, not after.
> Example: SRC-001 (CEO) says "we want a clean rewrite". SRC-003 (CTO email) says "incremental refactor only — rewrite is off the table". Real conflict. Surface in Section 8.

**Gaps** — important questions where NO source speaks.
> Example: 6 categories of input, but no operational data on actual user behavior. Is the team flying on stakeholder opinion alone? Flag.

### Step 6 — Identify open questions for stakeholders

From contradictions + gaps + low-confidence items, build a prioritized question list for the next stakeholder session:

| # | Question | Why it matters | Asked of |
|---|----------|----------------|----------|
| Q1 | Is this a rewrite or incremental refactor? | Determines Phase 2 strategy entirely | CEO + CTO together |
| Q2 | What's the actual budget cap? | Bounds scenario design in feasibility | CFO |
| Q3 | What does "compliance" mean concretely — GDPR? SOC2? Both? | Drives M9 NFRs | Legal |

These are NOT for you to answer. They go to the operator to take to stakeholders. Phase 0 should not start until the highest-priority ones are answered.

### Step 7 — Produce the Context Pack

Open [assets/CONTEXT_PACK_template.md](assets/CONTEXT_PACK_template.md), fill every `{{PLACEHOLDER}}`. Write to `docs/00_REQUIREMENTS/CONTEXT_PACK.md`. Copy anonymized source files to `docs/00_REQUIREMENTS/_sources/SRC-NNN_<slug>.md`.

Cite source IDs everywhere. A claim without a `[SRC-NNN]` citation is your invention, not stakeholder voice. Remove it or move it to Section 10 (Operator Hypotheses, clearly marked).

### Step 8 — Self-review

Run [references/checklist.md](references/checklist.md). Do not deliver until all gates pass.

## Quality bar

A good `CONTEXT_PACK.md` lets a downstream skill operator:

1. Find every important stakeholder claim in one place, with citations
2. See where stakeholders agree vs. disagree (so SRS doesn't paper over real conflicts)
3. See what's MISSING from the inputs (so Phase 0 doesn't fly blind in those areas)
4. Trace any pack claim back to a verifiable source
5. Skip re-reading 200 pages of raw material before drafting SRS

If a downstream operator runs `srs-greenfield-author` and still has to ask "but what does the CEO actually want?", the pack failed.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: low-input-volume projects (just 2-3 sources), enterprise projects (50+ sources), hostile-stakeholder situations (where claims conflict by design), greenfield with no users yet (substitute competitor + market research), regulated industries (compliance-heavy ingestion).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Pegasus", a logistics rewrite, ingesting 17 sources across all 6 categories.

## Failure modes to avoid

- **Quoting everything.** A pack that's 80% verbatim quotes is just a longer transcript. Extract; don't transcribe.
- **Inventing claims.** Every fact in the pack must cite a source. If no source supports it, it goes in Section 10 Operator Hypotheses (clearly marked) or gets cut.
- **Ignoring contradictions.** The instinct is to pick a side and "synthesize" — don't. Surface contradictions; let stakeholders resolve them.
- **Privacy leak.** Personal details, customer names, internal Slack profanity — these survive into shared docs unless you anonymize. Anonymize-by-default.
- **Pretending complete coverage.** If the operator gave you 3 sources, the pack covers what those 3 say — not the project's full reality. State coverage honestly in Section 11.
- **Letting old sources dominate.** A 2024 stakeholder interview may be obsolete by 2026. Date every source; weight recent ones higher.
- **Refusing to flag missing categories.** "No operational data was provided" is itself a finding — it tells the operator to push for analytics access before Phase 0.
