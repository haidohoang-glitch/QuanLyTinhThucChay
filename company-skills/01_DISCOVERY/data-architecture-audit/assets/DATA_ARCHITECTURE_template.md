# {{PROJECT_NAME}} — Data Architecture Audit

> **Purpose:** Document how this system stores, moves, and governs data. Identifies storage layers, data flow, governance gaps, consistency risks.
> **Audience:** Tech leads, architects, compliance reviewers, AI agents planning data migrations.
> **Last updated:** {{YYYY-MM-DD}}
> **Generated using:** `data-architecture-audit` skill v1
> **Reviewer:** {{NAME_OR_TBD}}

---

## 1. Executive Summary

**Overall posture:** {{ONE_PARAGRAPH — current state, primary concerns, urgent gaps}}

**Stores in use:** {{COUNT}} primary stores, {{COUNT}} cache/edge tiers, {{COUNT}} third-party.

**Top 3 risks (preview):**
1. {{RISK_1}} — severity {{P0/P1/P2}}
2. {{RISK_2}} — severity {{P0/P1/P2}}
3. {{RISK_3}} — severity {{P0/P1/P2}}

(Full risk list in Section 7.)

---

## 2. Storage Layer Map

Classification: see Section 9 for mode used (A / B / C).

### Stores by layer

| Layer | Store | Purpose | Tech | Owner |
|-------|-------|---------|------|-------|
| {{LAYER_ID}} | {{STORE_NAME}} | {{ONE_LINE}} | {{TECH}} | {{TEAM_OR_OWNER}} |

### Visualization

```
{{ASCII_OR_MERMAID_DIAGRAM_OF_LAYERS_AND_FLOW}}
```

---

## 3. Schema Inventory (Primary Stores)

For each L4/L5 primary store:

### Store: {{STORE_NAME}}

| Table / Collection | Purpose | Row count | Key columns | Sensitive fields |
|--------------------|---------|-----------|-------------|------------------|
| {{NAME}} | {{ONE_LINE}} | {{NUMBER_OR_~}} | {{PK, FKs, notable indexes}} | {{PII_OR_SECRETS}} |

### Schemas not documented

If any store's schema is dynamic, undocumented, or lives only in code:
- {{STORE}} — {{REASON}} → flagged as Open Question

---

## 4. Data Flow

### Major data types

For each significant entity (user, transaction, product, etc.):

#### {{ENTITY_NAME}}

**Write path:**
```
{{SOURCE}} → {{VALIDATION}} → {{L4_WRITE}} → {{CACHE_INVALIDATE}} → {{L5_SYNC}}
```

**Read path:**
```
{{REQUEST}} → {{L3_CACHE}} → {{L4_FALLBACK}}
```

**Sync mechanisms:** {{ETL/CDC/dual-write/none}}
**Transaction boundary:** {{WHERE}}
**Failure mode if {{STORE}} is down:** {{BEHAVIOR}}

{{REPEAT_FOR_EACH_MAJOR_ENTITY}}

---

## 5. Quotas, Usage, Costs

| Store | Plan | Quota / Limit | Current usage | Projected at 10x | Monthly cost (now → 10x) |
|-------|------|---------------|---------------|------------------|---------------------------|
| {{STORE}} | {{PLAN}} | {{LIMIT}} | {{CURRENT}} | {{PROJECTED}} | {{NOW}} → {{10X}} |

### Bottleneck analysis

Which store hits its limit first as the system grows?

- **First to break:** {{STORE}} at {{SCALE_POINT}} because {{REASON}}
- **Mitigation if not addressed:** {{IMPACT}}

---

## 6. Governance Audit

| Concern | Status | Evidence | Gap |
|---------|--------|----------|-----|
| PII inventory | {{✅ Documented / ⚠️ Partial / ❌ Missing}} | {{WHERE}} | {{WHAT_IS_MISSING}} |
| GDPR right-to-export | {{STATUS}} | {{EVIDENCE}} | {{GAP}} |
| GDPR right-to-delete | {{STATUS}} | {{EVIDENCE}} | {{GAP}} |
| Retention policy | {{STATUS}} | {{EVIDENCE}} | {{GAP}} |
| Audit trail | {{STATUS}} | {{EVIDENCE}} | {{GAP}} |
| Encryption at rest | {{STATUS}} | {{EVIDENCE}} | {{GAP}} |
| Encryption in transit | {{STATUS}} | {{EVIDENCE}} | {{GAP}} |
| Access control / RLS | {{STATUS}} | {{EVIDENCE}} | {{GAP}} |
| Backup & DR | {{STATUS}} | {{EVIDENCE}} | {{GAP}} |

### PII field map

| Field | Stored in | Encrypted at rest? | Encrypted in transit? | In backups? | Tagged for GDPR? |
|-------|-----------|---------------------|------------------------|-------------|-------------------|
| {{FIELD_NAME}} | {{STORE.TABLE}} | {{Y/N}} | {{Y/N}} | {{Y/N}} | {{Y/N}} |

---

## 7. Risk Findings

| ID | Risk | Severity | Layer | Evidence | Recommended next step |
|----|------|----------|-------|----------|----------------------|
| R-01 | {{ONE_LINE_RISK}} | {{P0/P1/P2/P3}} | {{LAYER}} | {{FILE:LINE_OR_QUERY}} | {{NEXT_STEP}} |

### Severity definitions used

- **P0** — Active data loss, security incident, compliance violation. Stop work and fix.
- **P1** — Likely to cause incident in <90 days. Plan immediate remediation.
- **P2** — Latent risk, not currently triggering. Address in next planning cycle.
- **P3** — Notable but acceptable for now.

---

## 8. Open Questions

| ID | Question | Where seen | Suggested next step |
|----|----------|------------|---------------------|
| OQ-1 | {{SPECIFIC_QUESTION}} | {{LOCATION}} | {{NEXT_STEP}} |

If <3 open questions, you stopped too early. Look harder at: undocumented stores, retention behavior, encryption configuration, multi-tenant isolation, backup restore tests.

---

## 9. Notes & Caveats

- **Classification mode:** {{A — Standard layered model / B — Honor codebase declared model / C — User-defined}}
- **Mode rationale:** {{WHY}}
- **If Mode B:** Source = `{{PATH_TO_DATA_DOC}}` (commit `{{HASH}}`)
- **If Mode C:** Categories = {{LIST}}; rationale = {{WHY}}
- **Audit scope:** {{WHAT_WAS_DONE — e.g., read schema definitions, ran sample queries, reviewed env files}}. NOT done: {{WHAT_WAS_SKIPPED — e.g., live performance test, security pen test, restore drill}}.
- **Time spent:** {{HOURS}}
- **Confidence:** {{HIGH/MEDIUM/LOW}}
- **Known gaps:** {{WHAT_THIS_AUDIT_DOES_NOT_COVER}}

---

*Findings here are descriptive — what IS and what's RISKY. Solution proposals belong in Phase 2 Strategic documents (`tech-solution-design`, `implementation-planning`).*
