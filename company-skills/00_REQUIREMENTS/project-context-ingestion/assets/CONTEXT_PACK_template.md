# {{PROJECT_NAME}} — Context Pack

> **Generated:** {{YYYY-MM-DD}}
> **Author:** {{NAME or AI agent}}
> **Source skill:** `project-context-ingestion` v1
> **Mode:** {{A — Standard 6-category / B — Honor company framework / C — User-defined}}
> **Source count:** {{N}} ({{N_USER}} user research / {{N_COMM}} comms / {{N_DOCS}} informal docs / {{N_EXT}} external / {{N_OPS}} operational / {{N_REG}} regulatory)
> **Coverage confidence:** {{HIGH / MEDIUM / LOW}}

---

## 1. Executive Summary

**What we know:** {{2-3 sentences capturing the strongest signal from the inputs.}}

**What we don't know:** {{2-3 sentences naming the load-bearing gaps.}}

**Top 3 stakeholder priorities (ranked by source weight):**
1. {{ONE_LINE — cite top sources}}
2. {{ONE_LINE — cite top sources}}
3. {{ONE_LINE — cite top sources}}

**Top 3 unresolved contradictions:**
1. {{ONE_LINE — name the conflicting sources}}
2. {{ONE_LINE — name the conflicting sources}}
3. {{ONE_LINE — name the conflicting sources}}

**Decision-readiness:** {{Phase 0 can start / Phase 0 blocked on Q1+Q2 / Re-ingestion needed}}

---

## 2. Source Inventory

| Source ID | Title | Format | Date | Origin | Sensitivity | Anonymized? |
|-----------|-------|--------|------|--------|-------------|-------------|
| SRC-001 | {{...}} | {{audio/transcript/PDF/screenshot/text}} | {{YYYY-MM-DD}} | {{interview/email/web/internal}} | {{none/PII/confidential}} | {{Yes/No}} |
| SRC-002 | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |
| ... | ... | ... | ... | ... | ... | ... |

**Total:** {{N}} sources

**Source files:** see `docs/00_REQUIREMENTS/_sources/`

---

## 3. Stakeholder Voice (User Research + Internal Comms)

Synthesized claims from SRC-* with citations. Each item below is grounded in ≥1 source.

### 3.1 Primary stakeholders

| Stakeholder role | Priorities (per them) | Sources |
|------------------|------------------------|---------|
| {{e.g., CEO}} | {{1-3 bullets}} | [SRC-001], [SRC-007] |
| {{e.g., CFO}} | {{1-3 bullets}} | [SRC-003] |
| {{e.g., Head of Ops}} | {{...}} | {{...}} |
| {{e.g., End user — Customer A}} | {{...}} | {{...}} |

### 3.2 Verbatim quotes (load-bearing)

Quotes that drove a finding. Use sparingly — only when paraphrasing loses force.

> "{{EXACT QUOTE}}" — [SRC-001], CEO interview, 2026-04-12

> "{{EXACT QUOTE}}" — [SRC-012], support ticket #4521

### 3.3 What stakeholders want (consolidated)

Items where ≥2 sources concur:

| Want / Need | Confidence | Sources |
|-------------|------------|---------|
| {{e.g., "Faster monthly close — currently 5 days, target 2"}} | High | [SRC-001], [SRC-003], [SRC-007] |
| {{e.g., "Mobile-first UI for warehouse staff"}} | Medium | [SRC-005] only |
| {{...}} | {{...}} | {{...}} |

### 3.4 Pain points cited

| Pain | Frequency in sources | Sources |
|------|----------------------|---------|
| {{e.g., "Excel exports break for >10K rows"}} | 4 distinct sources | [SRC-001], [SRC-008], [SRC-012], [SRC-014] |
| {{...}} | {{...}} | {{...}} |

---

## 4. Business Context (informal docs, prior reports)

What prior artifacts say about the product, market, and business model.

### 4.1 Product positioning (per inputs)

{{1-2 paragraphs synthesizing pitch decks, RFPs, prior consultant reports. Cite sources.}}

### 4.2 Business model

| Aspect | Per inputs | Sources |
|--------|-------------|---------|
| Revenue model | {{e.g., per-seat SaaS, $X/user/month}} | [SRC-006] |
| Customer segments | {{...}} | {{...}} |
| Pricing | {{...}} | {{...}} |
| Growth thesis | {{...}} | {{...}} |

### 4.3 Strategic goals (cited)

| Goal | Source | Date | Still current? |
|------|--------|------|-----------------|
| {{e.g., "Reach 10K paid seats by Q4 2026"}} | [SRC-002] | 2026-Q1 OKR doc | {{Yes / Likely outdated}} |
| {{...}} | {{...}} | {{...}} | {{...}} |

---

## 5. External Context (competitors, market)

### 5.1 Competitor landscape (per inputs)

| Competitor | What they do | What stakeholders said about them | Sources |
|------------|--------------|------------------------------------|---------|
| {{e.g., Acme Corp}} | {{1 line}} | {{e.g., "they have better mobile UX"}} | [SRC-009], [SRC-011] |
| {{...}} | {{...}} | {{...}} | {{...}} |

### 5.2 Market signals

{{Bullets summarizing analyst writeups, market reports, comparable products. Each with [SRC-NNN].}}

---

## 6. Operational Reality (analytics, support, churn)

What the data says (when ops data was provided).

| Metric | Value (as of date) | Source | Implication |
|--------|---------------------|--------|-------------|
| Monthly active users | {{X}} | [SRC-013], analytics | {{...}} |
| Top 3 support categories | {{...}} | [SRC-014], support log | {{Maps to FRs in M3-M5 of future SRS}} |
| Annual churn | {{X%}} | [SRC-015] | {{...}} |
| {{...}} | {{...}} | {{...}} | {{...}} |

If operational data was NOT provided, say so here:

> ⚠️ No operational data provided. Stakeholder claims are unverified by usage signal. Recommend obtaining analytics + support volume + churn data before SRS finalization.

---

## 7. Constraints & Compliance

Hard boundaries identified from regulatory excerpts, contracts, vendor agreements.

### 7.1 Regulatory

| Requirement | Source | Affects |
|-------------|--------|---------|
| {{e.g., GDPR Art. 17 — right to erasure}} | [SRC-016], regulatory PDF | M9 NFRs (privacy); M3 user-management FRs |
| {{e.g., SOC2 audit annually}} | [SRC-007], legal email | M9 NFRs (auditability); M10 process docs |
| {{...}} | {{...}} | {{...}} |

### 7.2 Contractual / vendor

| Constraint | Source | Affects |
|------------|--------|---------|
| {{e.g., Locked into AWS for 3 more years (committed spend)}} | [SRC-007] | Tech-solution-design must use AWS-native; can't migrate to GCP |
| {{...}} | {{...}} | {{...}} |

### 7.3 Budget / timeline

| Constraint | Stated by | Source |
|------------|-----------|--------|
| Budget cap | {{e.g., $500K Q3 2026}} | [SRC-003], CFO email |
| Hard deadline | {{e.g., audit prep — 2026-12-01}} | [SRC-003] |

---

## 8. Contradictions & Conflicts

Sources disagree. **These need stakeholder resolution before Phase 0.**

| ID | Topic | Position A | Position B | Sources A | Sources B | Resolution needed by |
|----|-------|-----------|-----------|-----------|-----------|----------------------|
| CON-1 | {{e.g., Rewrite vs refactor}} | {{Clean rewrite}} | {{Incremental refactor only}} | [SRC-001] CEO | [SRC-003] CTO | Joint CEO+CTO call |
| CON-2 | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

---

## 9. Gaps (what's NOT in the inputs)

Important questions where no source speaks:

| Gap | Why it matters | How to close |
|-----|----------------|--------------|
| {{e.g., "No actual user data — stakeholder voice only"}} | SRS may over-fit to exec opinion | Get analytics access; run 5 user interviews |
| {{e.g., "No competitor pricing data"}} | Feasibility ROI scenarios will be hand-wavy on pricing | Public web search + 1 internal estimate session |
| {{...}} | {{...}} | {{...}} |

---

## 10. Operator Hypotheses (NOT from sources)

Inferences the operator made that go BEYOND what sources state. Clearly separated so downstream readers don't mistake them for stakeholder voice.

| # | Hypothesis | Reasoning | Confidence | Should be confirmed by |
|---|------------|-----------|------------|------------------------|
| H1 | {{e.g., "Stakeholders likely care about mobile UX even though only 1 source mentioned it"}} | Mobile is industry-default 2026 | Medium | Direct stakeholder Q |
| H2 | {{...}} | {{...}} | {{...}} | {{...}} |

---

## 11. Notes & Caveats

- **Mode used:** {{A / B / C}}
- **Anonymization:** {{Applied to all sources / Skipped per operator / Mixed}}
- **Sources excluded:** {{LIST_AND_REASON — e.g., "audio without transcript: not processed"}}
- **Date range of sources:** {{earliest YYYY-MM-DD to latest YYYY-MM-DD}}
- **Time spent on ingestion:** {{HOURS}}
- **Confidence overall:** {{HIGH / MEDIUM / LOW with one-line reason}}

### Sources NOT consulted (and why)

| Source | Why not consulted |
|--------|--------------------|
| {{e.g., 2-hour audio recording, no transcript}} | Out of scope for v1 ingestion; transcribe + re-ingest |
| {{...}} | {{...}} |

---

## 12. Recommended Open Questions for Stakeholder Session

Prioritized for next stakeholder meeting. Phase 0 should not begin without answers to Q1-Q3.

| # | Question | Why it matters | Ask of | Blocking? |
|---|----------|----------------|--------|-----------|
| Q1 | {{...}} | {{...}} | {{role}} | Yes |
| Q2 | {{...}} | {{...}} | {{role}} | Yes |
| Q3 | {{...}} | {{...}} | {{role}} | Yes |
| Q4 | {{...}} | {{...}} | {{role}} | No |

---

## 13. Hand-off to Downstream Skills

This pack is consumed by:

| Skill | Uses sections |
|-------|----------------|
| `srs-greenfield-author` | 3 (stakeholder voice), 4 (business context), 7 (constraints), 8 (contradictions), 12 (open Qs → M10 issues) |
| `srs-reverse-engineer` | 3, 4, 7 (overlay business intent on code findings) |
| `business-context-capture` | 3, 4, 6 (validates code-derived business model against stakeholder voice) |
| `feasibility-assessment` | 4 (business model), 6 (operational reality), 7 (constraints — bounds scenarios), 12 (open Qs) |
| `nfr-specification` | 7 (regulatory + SLA constraints become NFR sources) |

---

## 14. Next Run

- **Re-ingest when:** Major stakeholder change / new compliance requirement / pivot / new round of user research
- **Recommended cadence:** Once at project start; refresh annually OR on trigger
- **Last updated:** {{YYYY-MM-DD}}

---

*A context pack is a faithful summary, not a complete account. If sources are thin, the pack is thin — and that's a finding, not a failure.*
