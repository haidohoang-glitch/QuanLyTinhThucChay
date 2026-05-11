# {{PROJECT_NAME}} — Tech Solution Design

> **Purpose:** Convert Phase 1 findings + SRS into a chosen technical solution. Architecture decisions, key components, data evolution, integration plan, rollout strategy.
> **Audience:** Tech lead, architects, senior engineers, AI agents (executing per design).
> **Last updated:** {{YYYY-MM-DD}}
> **Generated using:** `tech-solution-design` skill v1
> **Reviewer:** {{NAME_OR_TBD}}

---

## 1. Problem Frame

**What we have:** {{1-2 SENTENCES — current state per `CODEBASE_MAP.md` + `DATA_ARCHITECTURE.md`}}

**What we need:** {{1-2 SENTENCES — key requirements per SRS M3-M9}}

**The gap:** {{1-2 SENTENCES — what's missing/wrong; references TECH_DEBT_AUDIT findings}}

**Constraints:** {{1 SENTENCE — budget, timeline, team, technology lock-ins from M2.5 and FEASIBILITY_ASSESSMENT}}

---

## 2. Solution Mode

See Section 12 for chosen mode (A / B / C). Default Mode A: pick architecture pattern based on context; document alternatives.

---

## 3. Candidate Architectures

| Candidate | Pattern | Why considered | Strengths | Weaknesses | Cost (relative) |
|-----------|---------|----------------|-----------|------------|-----------------|
| A | {{e.g., Layered + Strategy}} | {{REASON}} | {{LIST}} | {{LIST}} | Low |
| B | {{e.g., Hexagonal / Ports-and-Adapters}} | {{REASON}} | {{LIST}} | {{LIST}} | Medium |
| C | {{e.g., Event-Sourced + CQRS}} | {{REASON}} | {{LIST}} | {{LIST}} | High |

(2-3 candidates; more is over-thinking.)

---

## 4. Comparison Matrix

| Requirement / Criterion | A | B | C |
|------------------------|---|---|---|
| Functional fit (M3-Mx FRs) | {{✅/⚠️/❌}} | {{...}} | {{...}} |
| Performance (NFR-PERF-*) | {{...}} | {{...}} | {{...}} |
| Security (NFR-SEC-*) | {{...}} | {{...}} | {{...}} |
| Reliability (NFR-REL-*) | {{...}} | {{...}} | {{...}} |
| Compliance (NFR-COMP-*) | {{...}} | {{...}} | {{...}} |
| Maintainability (NFR-MAINT-*) | {{...}} | {{...}} | {{...}} |
| Team familiarity | {{...}} | {{...}} | {{...}} |
| Migration cost from current | {{...}} | {{...}} | {{...}} |
| Time-to-first-value | {{...}} | {{...}} | {{...}} |
| Risk profile | {{...}} | {{...}} | {{...}} |
| **Total (subjective)** | {{score}} | {{score}} | {{score}} |

---

## 5. Architecture Decision Record (ADR)

### ADR-{{NN}}: Adopt {{CHOSEN_PATTERN}}

**Status:** Proposed (pending review by {{REVIEWER}})

**Context:** {{Problem summary from Section 1; why a decision is needed now}}

**Decision:** Adopt {{PATTERN}} for {{SCOPE — e.g., the server-side architecture}}.

**Rationale:** {{TOP_3_REASONS, citing comparison matrix}}

**Consequences (positive):**
- {{TRADE_OFF_GAINED}}
- {{TRADE_OFF_GAINED}}

**Consequences (negative — accepted):**
- {{TRADE_OFF_ACCEPTED}}
- {{TRADE_OFF_ACCEPTED}}

**Alternatives rejected:**
- Candidate {{X}}: rejected because {{REASON}}
- Candidate {{Y}}: rejected because {{REASON}}

**Revisit conditions:** Re-evaluate if {{CONDITION_1}} OR {{CONDITION_2}}.

---

## 6. Component Design

### Component diagram

```
{{ASCII_OR_MERMAID — show major components, dependencies, external systems}}
```

### Component inventory

| Component | Purpose | Public interface | Depends on | Boundary (does NOT do) |
|-----------|---------|------------------|------------|-------------------------|
| {{COMPONENT}} | {{ONE_LINE}} | {{INTERFACE_SUMMARY}} | {{LIST}} | {{LIST}} |
| {{COMPONENT}} | {{...}} | {{...}} | {{...}} | {{...}} |

### Folder / package structure (target)

```
{{TARGET_FOLDER_STRUCTURE — if architecture implies specific layout, show it}}
```

If migrating from current structure, link to `CODEBASE_MAP.md` Section 3 for comparison.

---

## 7. Data Evolution

### Current state
{{REFERENCE_TO_DATA_ARCHITECTURE_MD — 1 paragraph summary of where we are}}

### Target state
{{1-2 PARAGRAPHS — what the data layer looks like after this design lands}}

### Schema changes

| Change | Type | Migration approach | Rollback |
|--------|------|---------------------|----------|
| Add table `xyz` | Additive | Online (no downtime) | Drop table |
| Add column `users.x` | Additive | Online with default | Drop column |
| Rename column `a → b` | Breaking | Dual-write through transition | Revert + dual-write |
| Drop table `legacy_x` | Breaking | Wait for read traffic = 0; archive; drop | Restore from archive |

### Data migration plan

- **Strategy:** {{Online dual-write / Offline batch / Backfill + cut-over / Lazy on read}}
- **Reconciliation:** {{How drift is detected and corrected}}
- **Compatibility window:** {{During transition, both old and new code paths work because…}}

---

## 8. Integration Plan

### Internal integrations

| System | Protocol | Contract | Failure mode | Monitoring |
|--------|---------|----------|---------------|------------|
| {{e.g., Existing payment service}} | {{HTTP/gRPC/Events}} | {{Schema or doc}} | {{Behavior on failure}} | {{Alerts}} |

### External integrations

| Vendor | Protocol | SLA | Failure mode | Monitoring |
|--------|---------|-----|---------------|------------|
| {{e.g., Stripe}} | {{HTTPS Webhooks}} | {{99.9%}} | {{Retry queue + alert}} | {{...}} |

### Cross-cutting concerns

- **Authentication:** {{How identity flows through the system}}
- **Authorization:** {{Where authz checks happen}}
- **Observability:** {{Logging, tracing, metrics conventions}}
- **Error handling:** {{Common patterns}}
- **Configuration:** {{Where config lives, how it propagates}}

---

## 9. Rollout Strategy

### Phasing

| Phase | What ships | Behind feature flag? | Rollout % | Cutover criterion |
|-------|------------|----------------------|-----------|--------------------|
| 1 | {{e.g., Infrastructure deploy, no traffic}} | n/a | 0% | Infra healthchecks pass |
| 2 | {{e.g., Dual-write to new system, reads from old}} | Yes (`enable_new_writes`) | 0% reads | Reconciliation drift < 0.01% for 7 days |
| 3 | {{e.g., Gradual read switch}} | Yes (`new_reads_pct`) | 5% → 25% → 50% → 100% | Latency, error rate stable per stage |
| 4 | {{e.g., Old system decom}} | n/a | n/a | 0% reads to old for 30 days |

### Cutover gates

Each phase must satisfy gate criteria before advancing. Document criteria + how measured + who approves.

### Rollback strategy (per phase)

| Phase | Rollback approach | Data implications |
|-------|-------------------|-------------------|
| 1 | Tear down infra | None |
| 2 | Disable flag; halt dual-write | New system has stale data; OK because reads still old |
| 3 | Flip rollout back to 0% | Investigate before retry |
| 4 | Difficult — old decommissioned | Forward-fix preferred |

---

## 10. NFR Verification Plan

For each NFR class, how will this design demonstrate compliance?

| NFR | Target | Verification approach |
|-----|--------|------------------------|
| Performance (NFR-PERF-*) | {{e.g., p95 ≤ 200ms}} | {{Load test in staging at production-equivalent load; production APM monitoring}} |
| Security (NFR-SEC-*) | {{...}} | {{Pen test pre-launch; ongoing CSPM}} |
| Reliability (NFR-REL-*) | {{e.g., 99.9% uptime}} | {{Load test, chaos engineering, DR drill}} |
| Compliance (NFR-COMP-*) | {{...}} | {{External audit; control inventory mapped to design components}} |

---

## 11. Risks & Mitigations

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|------------|--------|------------|
| RP-01 | {{e.g., Pattern adoption requires team training}} | {{H/M/L}} | {{H/M/L}} | {{e.g., 4-week ramp-up; pair on first 2 components}} |
| RP-02 | {{e.g., Dual-write phase exposes consistency bugs}} | M | H | Reconciliation cron + alert if drift > 0.01% |
| RP-03 | {{...}} | {{...}} | {{...}} | {{...}} |

---

## 12. Notes & Caveats

- **Architecture mode:** {{A — Standard pattern / B — Honor existing / C — User-defined}}
- **Mode rationale:** {{WHY}}
- **If Mode B:** Source = `{{PATH_TO_EXISTING_ADR_OR_DOC}}`
- **Inputs read:** SRS ✅/❌, CODEBASE_MAP ✅/❌, DATA_ARCHITECTURE ✅/❌, TECH_DEBT_AUDIT ✅/❌, BUSINESS_CONTEXT ✅/❌, FEASIBILITY ✅/❌
- **Time spent on design:** {{HOURS}}
- **Confidence:** {{HIGH/MEDIUM/LOW}}

---

## 13. Open Questions

| ID | Question | Suggested next step |
|----|----------|---------------------|
| OQ-1 | {{e.g., Does Postgres logical replication support our LARGE OBJECT columns?}} | Spike WP in Phase 0 |
| OQ-2 | {{e.g., Vendor X SLA covers our peak hours?}} | Contract review |

---

## 14. Next Steps

1. Review with {{REVIEWERS}}; resolve Open Questions
2. Approve ADR-{{NN}} (status: Proposed → Accepted)
3. Pass to `implementation-planning` skill to decompose into WPs
4. Update relevant SRS sections if design reveals requirement gaps

---

*This is the chosen direction, with rationale. Implementation plan converts this into work packages.*
