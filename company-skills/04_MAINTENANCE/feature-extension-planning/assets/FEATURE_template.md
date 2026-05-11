# FEAT-{{ID}} — {{FEATURE_NAME}}

> **Project:** {{PROJECT_NAME}}
> **Author:** {{NAME}}
> **Date:** {{YYYY-MM-DD}}
> **Status:** {{Draft / Reviewed / Approved / In Implementation / Shipped / Deferred}}
> **Effort estimate:** {{XS/S/M/L}}
> **Target release:** {{VERSION_OR_DATE}}

---

## 1. What & Why

### What
{{1 paragraph — concrete description of what the feature does}}

### Who uses it
{{User class(es) from M2.3 of SRS}}

### Why we're building it
{{Business reason — customer ask, sales gating, competitive parity, regulatory, etc.}}

### Success measure
{{How will we know it worked? Metric + target. E.g., "30% of Pro users use bulk export at least once in first 90 days"}}

---

## 2. Mode & Scope

**Mode:** {{A — Standard / B — Company template / C — User-defined}}

### In scope

- {{INCLUDED}}
- {{INCLUDED}}

### Out of scope (explicit)

- {{NOT_INCLUDED — why}}
- {{NOT_INCLUDED}}

---

## 3. SRS Alignment

### Maps to existing FRs

| Existing FR | Relationship | Change needed |
|-------------|--------------|----------------|
| FR-{{ID}} | {{Extends / Conflicts / Related}} | {{NONE / specific change}} |

### New FRs to add

| New FR | Statement | Domain (Mx) | Priority |
|--------|-----------|-------------|----------|
| FR-{{NEW_ID}} | The system shall... | M{{N}} | Must / Should / Could |

(These FRs will be added to SRS M3-Mx via SRS author skill or manual edit.)

### NFR considerations

- **Performance:** {{Will this feature change response times? Throughput? Cache hit?}}
- **Security:** {{New attack surface? Auth/authz change?}}
- **Compliance:** {{Touch PII? Audit log requirement? GDPR right-to-export?}}
- **Reliability:** {{Failure modes? Graceful degradation?}}

If NFRs change, update M9 of SRS.

---

## 4. Design

### User flow

```
1. {{User opens X}}
2. {{User clicks Y}}
3. {{System does Z}}
4. {{User sees result}}
```

(For UI features, attach mockup OR describe in detail.)

### Data

| Entity | Action | Notes |
|--------|--------|-------|
| {{e.g., Export job}} | NEW table | tracks user export requests |
| {{e.g., User}} | UPDATE | add `last_export_at` column |

### API surface

| Endpoint | Method | Purpose | Auth |
|----------|--------|---------|------|
| {{e.g., POST /api/v1/exports}} | POST | Create export job | User session |
| {{e.g., GET /api/v1/exports/:id}} | GET | Check status | Same user only |

(Reference OpenAPI / contract test file if applicable.)

### UI changes

- {{New page / component / state}}
- {{Modified existing UI}}

### Integration

- **Touched components:** {{LIST}}
- **External services called:** {{LIST}}
- **Background jobs introduced:** {{LIST}}

---

## 5. Schema Changes

### Migrations

| Migration | Type | Description | Reversible? |
|-----------|------|-------------|-------------|
| {{e.g., 20260920_add_exports_table.sql}} | CREATE | New table for export jobs | Yes (DROP TABLE) |
| {{e.g., 20260921_add_user_last_export.sql}} | ALTER ADD COLUMN | New column on users | Yes (DROP COLUMN) |

### Migration risks

- {{e.g., New table — additive, low risk}}
- {{e.g., Online migration; no downtime}}

If breaking migration: escalate to `tech-solution-design`-quality review.

---

## 6. Rollout Plan

### Feature flag

- **Name:** `{{enable_feature_x}}`
- **Default state:** `false` (off)
- **Audience targeting:** {{e.g., enabled for internal users → 5% Pro tier → 25% → 100%}}
- **Kill switch:** flag → false; verify with synthetic check

### Gradual rollout

| Stage | % audience | Duration | Cutover criterion |
|-------|------------|----------|--------------------|
| Internal beta | 0% public; staff only | 1 week | No P1+ issues; staff feedback positive |
| 5% | 5% Pro tier | 1 week | Error rate < 0.5%; no support escalations |
| 25% | 25% Pro tier | 1 week | Same |
| 100% | All Pro tier | (full release) | Success metric trending up |

### Backward compatibility

- {{Does this break existing API? UI? Data assumptions?}}
- {{If yes: how is migration handled?}}

### Customer communication

- **Changelog entry:** {{TEXT}}
- **Help docs:** {{LINK}}
- **Email / in-product announcement:** {{If yes, when + audience}}

---

## 7. Test Plan

### Unit tests

- {{TEST}} — `{{file:test_name}}`
- {{TEST}} — `{{file:test_name}}`

### Integration tests

- {{TEST}} — covers {{flow}}

### Manual test cases (TC IDs to add to RTM)

- TC-FEAT-{{ID}}-01: {{Scenario}} → {{Expected}}
- TC-FEAT-{{ID}}-02: {{Scenario}} → {{Expected}}

### Performance test

- {{If this feature changes load profile, specify test}}
- {{Baseline metric + target}}

### Security test

- {{If feature changes auth surface, specify test}}
- {{e.g., AuthZ check: user A cannot access user B's exports}}

---

## 8. Risks & Mitigations

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| FR-01 | {{e.g., Export job creates large memory load}} | M | M | {{e.g., Use streaming; cap export size at 10K rows}} |
| FR-02 | {{e.g., User exports PII; GDPR concern}} | L | H | {{e.g., Consent check before export; audit log of every export}} |
| FR-03 | {{...}} | {{...}} | {{...}} | {{...}} |

---

## 9. Rollback Plan

If feature breaks production:

```
1. Disable flag: {{COMMAND}}
2. Verify flag off via synthetic check
3. If schema issue: run reverse migration {{NAME}}
4. If data issue: investigate before any cleanup; coordinate with DBA
5. Customer comm: changelog updated; status page if needed
```

---

## 10. Implementation Plan

### Approach

- **Single WP** (small feature): can implement as one PR
- **Multiple WPs** (medium-large feature): use `implementation-planning` skill to decompose

### WP outline (if multi-WP)

| WP | Description | Effort |
|----|-------------|--------|
| WP-FEAT-{{ID}}-A | {{Migration + schema}} | S |
| WP-FEAT-{{ID}}-B | {{Backend implementation}} | M |
| WP-FEAT-{{ID}}-C | {{Frontend implementation}} | M |
| WP-FEAT-{{ID}}-D | {{Tests + flag wiring}} | S |

### Dependencies

- {{Other features / refactors needed first}}
- {{External: vendor SDK update, infra capacity}}

---

## 11. Compliance / Privacy Review

(Only required for features touching PII, PHI, financial data, or regulated areas)

- **Data classification:** {{What data does feature touch?}}
- **Lawful basis (GDPR):** {{Consent / Contract / Legitimate interest}}
- **Audit log entries:** {{What's logged about feature usage}}
- **Data retention:** {{How long is feature data kept}}
- **Reviewer sign-off required:** {{e.g., Compliance Lead, Security Lead, Legal}}

(Skip section if feature has no compliance implications.)

---

## 12. Open Questions

| ID | Question | Owner | Target |
|----|----------|-------|--------|
| OQ-1 | {{Specific question}} | {{NAME}} | {{DATE}} |

---

## 13. Decision Log

| Date | Decision | Rationale | Owner |
|------|----------|-----------|-------|
| {{DATE}} | {{e.g., Use signed URL for export download vs. direct stream}} | {{Why}} | {{NAME}} |

(Capture decisions made during spec review for future reference.)

---

## 14. Sign-off

(Required to move from Draft → Approved.)

| Role | Name | Status | Date |
|------|------|--------|------|
| Product | | | |
| Engineering Lead | | | |
| QA Lead | | | |
| Compliance (if applicable) | | | |
| Security (if applicable) | | | |

---

*This spec is the contract for implementation. Changes after Approved status require re-review.*
