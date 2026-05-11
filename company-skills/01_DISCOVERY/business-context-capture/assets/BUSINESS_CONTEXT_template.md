# {{PROJECT_NAME}} — Business Context

> **Purpose:** Reverse-engineer the business view of this codebase: who uses it, what they do, what rules govern those actions, what invariants must hold.
> **Audience:** Product managers, new engineers, AI agents needing domain understanding before code change.
> **Last updated:** {{YYYY-MM-DD}}
> **Generated using:** `business-context-capture` skill v1
> **Reviewer:** {{NAME_OR_TBD}}

---

## 1. Product Summary

**One-paragraph product description (in business language):**
{{PARAGRAPH — what the product does, who it's for, the value it delivers}}

**Domain area:** {{e.g., E-commerce, Healthcare, Fintech, EdTech, Logistics}}

**Maturity / scale:** {{e.g., MVP / Growth / Mature; ~user count if known}}

---

## 2. Decomposition Mode

See Section 11 for chosen mode (A / B / C). In summary:
- **Mode A** organizes by Actor → Use Cases → Entities → Rules → Workflows → Invariants
- **Mode B** organizes by the codebase's bounded contexts
- **Mode C** organizes by user-supplied taxonomy

---

## 3. Actors

| Actor | Description | How they enter the system | Tools they use |
|-------|-------------|---------------------------|----------------|
| {{ACTOR_NAME}} | {{ONE_LINE}} | {{LOGIN/SIGNUP/API_KEY/SCHEDULED}} | {{UI/API/CLI}} |

### External actors (non-human)

| Actor | Trigger | Interface |
|-------|---------|-----------|
| {{e.g., Stripe webhook}} | {{e.g., charge.succeeded event}} | {{POST endpoint, signature verified}} |

---

## 4. Use Cases

Format: {Actor} can {verb} {noun} {qualifier?}

### {{ACTOR or DOMAIN GROUP}}

- UC-01: {{ACTOR}} can {{ACTION}}
- UC-02: {{ACTOR}} can {{ACTION}}
- ...

{{REPEAT_FOR_EACH_ACTOR_OR_DOMAIN}}

If you have >50 use cases, group by domain area; if >100, this is too granular — collapse similar cases.

---

## 5. Domain Entities

Nouns the business cares about. Use the product's own terminology.

| Entity | Definition (business terms) | Key attributes the business cares about | Related to |
|--------|------------------------------|------------------------------------------|------------|
| {{ENTITY_NAME}} | {{ONE_LINE_DEFINITION}} | {{ATTRIBUTE_LIST}} | {{OTHER_ENTITIES}} |

### Entity relationship overview

```
{{ASCII_OR_MERMAID_OF_KEY_RELATIONSHIPS}}
```

### Terminology notes

- "{{TERM_A}}" and "{{TERM_B}}" appear interchangeably in code; product treats them as: {{SAME / DIFFERENT — clarification}}
- "{{TERM_C}}" is used in code but the product team calls it "{{ALTERNATE}}"

---

## 6. Business Rules

### 6.1 Validation Rules

| Rule ID | Rule | Where enforced | Where else it matters |
|---------|------|----------------|----------------------|
| BR-V-01 | {{e.g., Email must be unique per tenant}} | `{{FILE:LINE}}` | Signup, profile edit |
| BR-V-02 | ... | ... | ... |

### 6.2 Calculation Rules

| Rule ID | Rule | Where enforced |
|---------|------|----------------|
| BR-C-01 | {{e.g., Tax = subtotal × rate(state)}} | `{{FILE:LINE}}` |

### 6.3 Eligibility / Authorization Rules

| Rule ID | Rule | Where enforced |
|---------|------|----------------|
| BR-A-01 | {{e.g., Only Pro tier can access export}} | `{{FILE:LINE}}` |

---

## 7. Workflows

Multi-step journeys spanning use cases.

### Workflow: {{WORKFLOW_NAME}}

**Trigger:** {{WHAT_STARTS_IT}}

**Happy path:**
```
1. {{STEP}}
2. {{STEP}}
3. {{STEP}}
```

**Failure paths:**
- {{CONDITION}} → {{OUTCOME}}
- {{CONDITION}} → {{OUTCOME}}

**Termination states:** {{LIST}}

**Stuck states (workflows that can sit indefinitely):**
- {{STATE}} — {{WHY_IT_HAPPENS}}

{{REPEAT_FOR_EACH_KEY_WORKFLOW}}

---

## 8. Invariants

Conditions that must ALWAYS hold. If broken, the product is broken.

| Inv ID | Invariant | Why it matters | Where enforced (or NOT enforced) |
|--------|-----------|----------------|-----------------------------------|
| INV-01 | {{e.g., Sum of debits = sum of credits per wallet}} | {{BUSINESS_REASON}} | DB trigger / app layer / not enforced (gap) |
| INV-02 | ... | ... | ... |

If "not enforced" — flag in Section 10 (Tensions & Gaps).

---

## 9. Tensions & Ambiguities

Domain inconsistencies and unclear behavior found while reading.

| ID | Tension | Where seen | Suggested resolution |
|----|---------|------------|----------------------|
| T-01 | {{e.g., UI says "Account suspended" but DB has both `is_suspended` and `status='inactive'` — different code paths use different fields}} | {{FILES}} | Interview product owner; pick one source of truth |
| T-02 | ... | ... | ... |

---

## 10. Open Questions

| ID | Question | Where seen | Next step |
|----|----------|------------|-----------|
| OQ-1 | {{SPECIFIC_QUESTION}} | {{LOCATION}} | Interview {{ROLE}}; or read {{DOC}} |

If <3, look harder. Domain understanding is never complete on first read.

---

## 11. Notes & Caveats

- **Decomposition mode:** {{A — DDD-lite / B — Honor codebase domain model / C — User-defined}}
- **Mode rationale:** {{WHY}}
- **If Mode B:** Source = `{{PATH_TO_DOMAIN_DOC}}` (commit `{{HASH}}`)
- **If Mode C:** Categories = {{LIST}}; rationale = {{WHY}}
- **Capture scope:** {{WHAT_WAS_DONE — e.g., read all schemas, sampled UI flows, traced 3 critical workflows}}. NOT done: {{WHAT_WAS_SKIPPED — e.g., user interviews, log analysis to validate workflows}}.
- **Time spent:** {{HOURS}}
- **Confidence:** {{HIGH/MEDIUM/LOW — calibrate based on how much was inferred vs. confirmed}}
- **Inferred items:** {{HOW_MANY_RULES_OR_INVARIANTS_WERE_INFERRED_VS_DOCUMENTED}}

---

*This is descriptive — what the product DOES. To propose changes, use `tech-solution-design`. To formalize as requirements, see `srs-reverse-engineer`.*
