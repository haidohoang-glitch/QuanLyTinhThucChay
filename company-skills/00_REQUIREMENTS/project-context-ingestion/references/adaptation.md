# Project Context Ingestion — Adaptation

Variations by project context and input shape.

> **Applies to Mode A only.** Mode B/C follow their own framework conventions.

---

## Low-input-volume projects (1-3 sources)

When operator hands over almost nothing:

**Adjust:**
- Don't pad. A 3-source pack is short — that's honest.
- Section 9 (Gaps) becomes the dominant section
- Section 12 (Open Questions) is the load-bearing output

**Add:**
- Explicit recommendation: "Pack confidence LOW. Recommend pausing Phase 0 until ≥5 more sources gathered."
- Suggest minimum sources: 1 stakeholder interview per role + 1 ops-data export + 1 constraint doc

**Don't:**
- Invent additional sources from external research and pretend they're project context
- Synthesize "consensus" from a single source

---

## Enterprise / high-input-volume (50+ sources)

When the operator dumps a year of Slack + a dozen consultant reports:

**Adjust:**
- Sample-based extraction: read ALL high-priority sources (interviews, exec emails); sample 20% of low-priority (Slack archives, support tickets)
- Tag sources by tier: Tier 1 (read fully) / Tier 2 (skim) / Tier 3 (search-only)
- Section 2 inventory grows large — split into sub-tables by category if >40 rows

**Add:**
- Per-source confidence weighting: a CEO interview outweighs 50 random Slack messages
- Frequency analysis: "X mentioned in 23 of 50 sources" is itself a signal
- Tooling: scripts to extract dates, names, key terms from text dumps

**Don't:**
- Try to read everything verbatim — you'll burn time, miss patterns
- Treat all sources as equal-weight

---

## Hostile-stakeholder situations

When stakeholders disagree by design (M&A integration, post-incident, internal politics):

**Adjust:**
- Section 8 (Contradictions) is the most important section, not an afterthought
- Capture not just WHAT each side says, but WHY (their incentives, their context)
- Don't pick a side. The pack's job is fidelity, not synthesis.

**Add:**
- A "stakeholder map" showing reporting lines + who has decision authority over what
- Mark which contradictions are factual (testable) vs preferential (political)
- Recommend mediation in Section 12 — name a senior decider who must rule

**Don't:**
- Try to find "the truth" by averaging stakeholders
- Hide contradictions to make the pack look cleaner

---

## Greenfield with no users yet

When the product doesn't exist, so there's no user research data:

**Adjust:**
- Substitute: comparable products' user research (analyst reports, App Store reviews of competitors)
- Substitute: interview with target users of competing products, not yours
- Section 3 (Stakeholder Voice) leans heavily on internal stakeholders + market proxies

**Add:**
- Explicit caveat: "User voice is inferred from comparable products; risk of mismatch with our actual future users"
- Recommend in Section 12: "Run 5-10 user interviews with target persona before SRS finalization"

**Don't:**
- Pretend "what users want" is known when no users have been interviewed
- Skip user research entirely — substitute is fine; absence is not

---

## Regulated industries (FDA, financial, healthcare)

When compliance dominates:

**Adjust:**
- Section 7.1 Regulatory becomes the heaviest section
- Each regulatory citation needs full reference (regulation name, section, version, jurisdiction)
- Auditor will read this pack — write to that audience

**Add:**
- Regulatory-to-requirement mapping table: "GDPR Art. 17 → must have FR for user-data deletion → goes to M3 user-management"
- Compliance changes log: regulations evolve; date-stamp every regulatory citation
- Cite official sources only (not blog summaries of regulations)

**Don't:**
- Paraphrase regulatory language — quote it verbatim with citation
- Mix legal counsel input with stakeholder opinion (separate sections)

---

## Multilingual projects

When sources are in multiple languages:

**Adjust:**
- Quote in original language; provide translation in pack
- Format: `> "Original quote" (translation: "...") — [SRC-NNN]`
- Anonymization needs to handle name conventions per language/culture

**Add:**
- Per-source language tag in inventory
- Translation quality note: "Auto-translated" vs "Bilingual operator translated"

**Don't:**
- Translate then discard original — original language matters for nuance

---

## Internal-tool projects (small user base, well-known users)

When users = 10 people in finance department, all known:

**Adjust:**
- Skip anonymization (operator confirms — small known group, internal-only pack)
- Use real names + roles (more useful than abstractions for a 10-person system)
- User research may be 1-on-1s, not surveys

**Add:**
- Per-user note section (each named user's specific workflow)

**Don't:**
- Anonymize blindly when it removes load-bearing information

---

## Re-ingestion (refresh after time)

When pack already exists from a prior run, and time has passed:

**Adjust:**
- Don't rebuild from scratch — diff the new sources against prior pack
- Mark each prior claim: still valid? superseded? stale?
- Section 14 lists what changed since last run

**Add:**
- "Stale claims" subsection — what was true 6 months ago but is no longer
- Date-stamp every refreshed claim

**Don't:**
- Discard prior open questions silently — close them with the answers found

---

## When ingestion is overkill

If the project is:
- 1-page brief from a single decider
- Already-documented in another structured doc the operator can read directly
- A trivial 1-week feature add (no SRS/feasibility needed)

→ Skip this skill. Read the brief directly. Apply judgment, not process.

This skill earns its weight when raw inputs are messy, multi-sourced, contradiction-prone, or compliance-relevant. Don't apply it ceremonially.

---

## Differences from `business-context-capture`

| | `project-context-ingestion` | `business-context-capture` |
|---|------------------------------|------------------------------|
| Inputs | Raw materials (interviews, emails, PDFs, Slack) | Codebase + already-structured pre-work |
| Source of truth | What stakeholders SAY | What the code DOES |
| Output | CONTEXT_PACK.md (raw → structured) | BUSINESS_CONTEXT.md (code → business view) |
| Phase | Pre-Phase 0 / Phase 0 prep | Phase 1 Discovery |
| Question answered | "What do stakeholders want? What constraints exist?" | "What does this product actually do (in business terms)?" |

Both feed into SRS skills. They are complementary; neither replaces the other.

For a NEW project (no code yet): only `project-context-ingestion` applies; there's no code for `business-context-capture` to read.

For a LEGACY project (code exists, no docs): both apply. Run `project-context-ingestion` first to capture stakeholder voice + constraints; then `business-context-capture` to map the code; SRS skill reconciles them.

---

## Differences from `documentation-sync`

| | `project-context-ingestion` | `documentation-sync` |
|---|------------------------------|------------------------|
| Direction | Outside-in (raw → docs) | Doc-vs-reality (existing docs → audit) |
| Frequency | Once at project start; on stakeholder change | Monthly |
| Output | CONTEXT_PACK.md | DOC_SYNC_REPORT.md |

These don't compete; they run at different points in the project lifecycle.
