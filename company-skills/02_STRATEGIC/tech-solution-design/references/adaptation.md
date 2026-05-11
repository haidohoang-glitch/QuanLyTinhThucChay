# Tech Solution Design — Adaptation

Variations by project context.

> **Applies to Mode A (standard pattern selection) only.** Mode B/C follow conventions.

## Greenfield project

When designing a system with no existing code:

**Adjust:**
- Section 1 "What we have" = "Nothing — greenfield"
- Section 7 (Data evolution) is "data design" not "data migration"
- Section 9 (Rollout) is launch strategy, not migration phasing
- Section 11 risks emphasize "untested architecture" + team learning curve

**Add:**
- Tech stack selection rationale (each major dep choice)
- Hiring/training plan if architecture requires unfamiliar skills

## Modernization (legacy refactor)

When updating an existing system:

**Adjust:**
- Heavy emphasis on Section 7 data evolution — most risk is here
- Section 9 rollout dominates — strangler fig vs big-bang vs blue-green
- Anti-scope becomes critical (don't expand beyond modernization)

**Watch for:** "While we're at it" syndrome — keep modernization focused.

## Migration (X → Y)

When replacing technology:

**Specific scenarios per phase template:**
1. Y deployed parallel, no traffic
2. Y receives writes (dual-write); X still primary read
3. Y becomes primary read; X passive
4. X decommissioned

This is FinanceOS-style; matches `implementation-planning` Phase 0-4 template.

**Add:**
- Reconciliation strategy explicit
- Cost during dual-running period (often substantial)
- Knowledge preservation (decommissioning X loses team knowledge)

## Monolith → service-oriented

Specific concerns:

**Add:**
- Service boundary rationale per service (don't split for splitting's sake)
- Data ownership decisions (which service owns which data)
- Cross-service consistency strategy (saga, choreography, orchestration)
- Service contract format and versioning

**Watch for:** Distributed monolith antipattern (services that share databases or are tightly coupled).

## Service-oriented → monolith (rare but happens)

When consolidating:

**Add:**
- What does monolith do that microservices don't?
- Failure isolation impact
- Team coordination model change

## Data-heavy systems (analytics, ML, logs)

**Adjust:**
- Section 6 components emphasize data flow, not service interfaces
- Section 7 dominates — schema and pipeline design
- Section 10 NFR verification includes data quality NFRs

**Add:**
- Data lineage tracking
- Schema evolution policy (Avro/Protobuf compatibility)
- Reprocessing/backfill capability
- Cost model (compute + storage + transfer)

## Compute-heavy / latency-critical systems

**Adjust:**
- Performance NFRs drive architecture choice
- Section 10 verification includes load tests at scale
- Section 8 emphasizes caching layer design

**Add:**
- Capacity planning section (peak vs average)
- Tail latency strategy (p99, p999)
- Backpressure / circuit breaker design

## Regulated industries

**Adjust:**
- ADR (Section 5) must cite regulation clauses driving the decision
- Section 10 NFR verification audit-grade (external evidence)
- Section 11 risks include regulatory exposure
- Sign-off requires Compliance + Legal in addition to engineering

**Add:**
- Compliance control mapping (which architecture component implements which control)
- Audit trail design (immutable, queryable, exportable)
- Data residency design

## Open-source-first projects

**Adjust:**
- Vendor lock-in is a deal-breaker; weight heavily in Section 4
- Self-hostable design preferred over SaaS
- Open standards (OpenAPI, AsyncAPI) for contracts

**Add:**
- License compatibility matrix
- Self-hosting documentation requirements
- Build-from-source verifiability

## Enterprise / on-prem deployment

**Adjust:**
- Cannot assume cloud features (managed services may not exist)
- Air-gapped deployment may be required
- Customer-managed keys throughout

**Add:**
- Deployment model variations (cloud / on-prem / hybrid)
- Update mechanism for customer environments
- Telemetry that respects privacy

## Multi-tenant SaaS

**Add:**
- Tenant isolation strategy (logical / dedicated / hybrid per tier)
- Per-tenant config / customization model
- Noisy neighbor mitigation
- Tenant lifecycle (onboarding, offboarding, data preservation)

## Mobile-first

**Add:**
- Offline-first sync strategy (CRDT, vector clocks, last-write-wins)
- Local storage encryption
- App version compatibility matrix
- Background task design (limited by OS)

---

## Cross-cutting: when to write a separate SERVER_ARCHITECTURE.md

If the architecture refactor is substantial enough to warrant its own deep dive, create a sibling `SERVER_ARCHITECTURE.md`. Examples:

- Folder restructure across many directories
- Layer/boundary changes affecting most services
- Adoption of a specific architectural pattern requiring detailed migration

The main `TECH_SOLUTION_DESIGN.md` then has a Section pointing to `SERVER_ARCHITECTURE.md` for details.

For most projects, one document is enough.
