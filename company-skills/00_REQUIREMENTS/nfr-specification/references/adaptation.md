# NFR Specification — Adaptation

Variations by project context.

> **Applies to Mode A (ISO 25010) only.** Mode B/C follow their own taxonomies but adapt the principles below.

## Healthcare (HIPAA, FDA-regulated software)

**Expand:**
- **Security:** PHI inventory, BAA-bound subprocessors, access logging granularity (who accessed what, when)
- **Compliance:** HIPAA Privacy Rule, Security Rule, Breach Notification Rule — each gets dedicated NFR
- **Reliability:** for medical devices, often SLA stricter than typical (e.g., 99.99% for clinical decision support)
- **Maintainability:** for FDA-regulated software, change control NFR (validation requirements per change)

**Add:**
- NFR-COMP for ALCOA+ principles (Attributable, Legible, Contemporaneous, Original, Accurate, Complete, Consistent, Enduring, Available)
- NFR-COMP for 21 CFR Part 11 (electronic signatures, audit trail)
- NFR-SEC for de-identification thresholds (safe harbor vs expert determination)

**Watch for:** SaMD (Software as Medical Device) classifications change NFR rigor; Class II device much stricter than wellness app.

## Financial services (PCI-DSS, SOX)

**Expand:**
- **Security:** card data handling NFRs are often binary (in scope or out of scope of CDE)
- **Compliance:** SOX-specific NFRs around segregation of duties, change control, financial reporting accuracy
- **Reliability:** typically tighter SLAs (99.95-99.99% for trading-related systems)

**Add:**
- NFR-SEC for tokenization (storage, transit, lifecycle of tokens)
- NFR-COMP for PCI-DSS sub-requirements (3.2 storage, 3.4 encryption, 8.x access)
- NFR-MAINT for code review trail (SOX section 404)

## EU-resident user data (GDPR, eIDAS)

**Expand:**
- **Compliance:** GDPR articles 5-32 each may inform NFRs
- **Security:** specific to GDPR-mandated controls (pseudonymization, encryption)

**Add:**
- NFR-COMP for right-to-export timeframe (Art. 12)
- NFR-COMP for breach notification (Art. 33 — 72 hours to authority)
- NFR-COMP for data residency (some controllers require EU-only processing)
- NFR-COMP for sub-processor management (DPA chain documented)

## High-availability systems (financial trading, healthcare critical, infra)

**Expand:**
- **Reliability:** uptime targets at 99.95%, 99.99%, even 99.999% require very different architectures
- Specify per-component RTO/RPO (not just system-wide)
- **Performance:** latency budgets at percentile depth (p999, p9999) for trading systems

**Add:**
- NFR-REL for active-active vs active-passive expectations
- NFR-REL for graceful degradation behavior
- NFR-PERF for tail latency (p99.9) explicitly

## Latency-critical systems (real-time, gaming, ad-tech)

**Expand:**
- **Performance:** response time NFRs measured at edge, not just server
- Additional metric: jitter (variance), not just average
- **Compatibility:** geographic latency NFRs (per-region targets)

**Add:**
- NFR-PERF for end-to-end latency including network
- NFR-PERF for capacity (max concurrent users, sustained req/s)

## Accessibility-critical products (public sector, education, large user base)

**Expand:**
- **Usability:** WCAG conformance level (A, AA, AAA) explicit
- Multiple verification methods: automated scan + manual audit + user testing with people with disabilities

**Add:**
- NFR-USE for keyboard-only navigation
- NFR-USE for screen reader compatibility (NVDA, JAWS, VoiceOver)
- NFR-USE for cognitive accessibility (plain language, consistent navigation)
- NFR-COMP for ADA, EAA (EU), or Section 508 (US gov) requirements

## Multi-tenant SaaS

**Expand:**
- **Performance:** per-tenant quotas (rate limits, storage caps)
- **Security:** tenant isolation NFRs explicit (no cross-tenant leakage; defense in depth)
- **Compliance:** per-tenant compliance obligations may differ (some tenants subject to HIPAA, others not)

**Add:**
- NFR-PERF for noisy neighbor mitigation (one tenant's load doesn't impact others)
- NFR-SEC for tenant data separation (logical or physical; document choice)
- NFR-MAINT for per-tenant configuration management

## Consumer mobile apps

**Expand:**
- **Performance:** app launch time, jank/dropped frames, battery impact
- **Compatibility:** OS version matrix, device class matrix
- **Reliability:** offline behavior NFRs

**Add:**
- NFR-PERF for app size (download + on-disk)
- NFR-PERF for cold start time
- NFR-COMPAT for App Store / Play Store guideline compliance
- NFR-SEC for secure storage (Keychain / Keystore usage; certificate pinning)
- NFR-USE for permission request UX (don't trigger system prompts before user understands why)

## ML / AI products

**Expand:**
- **Performance:** inference latency, training time, throughput
- **Reliability:** model accuracy / quality metrics per use case
- **Compliance:** for regulated decisions, explainability and contestability

**Add:**
- NFR-PERF for model accuracy threshold (precision, recall, F1, AUC depending on task)
- NFR-REL for model drift detection (when do we retrain?)
- NFR-COMP for fairness metrics (demographic parity, equal opportunity)
- NFR-MAINT for training data lineage (reproducibility)

## API-only / Platform products

**Expand:**
- **Compatibility:** API versioning policy as NFR
- **Performance:** per-endpoint latency targets (different for read vs write vs aggregate)

**Add:**
- NFR-COMPAT for API stability commitment (semver discipline)
- NFR-PERF for rate limiting (per-key, per-tier)
- NFR-SEC for API authentication (key vs OAuth vs mTLS)
- NFR-MAINT for API documentation completeness (OpenAPI ≥80% coverage of endpoints)

## Internal tools / B2B back-office

**Adjust:**
- **Reliability:** lower SLA acceptable (99% during business hours often enough)
- **Usability:** internal users tolerate more friction; usability NFRs less stringent
- **Performance:** lower scale, lower urgency

**Watch for:** Often skipped: encryption, audit, PII handling. Internal tools often handle MORE sensitive data than consumer products. Don't lower Security/Compliance NFRs just because users are employees.

## Greenfield vs reverse-engineered NFRs

**Greenfield:** Targets are aspirational; current state is "Not yet built". Focus on choosing realistic targets.

**Reverse-engineered:** Current state is measurable from production. Focus on **honestly capturing** current performance and **distinguishing** which targets the system already meets vs which are aspirational. The gap becomes input to remediation planning.

For reverse-engineered: a healthy M9 has 30-50% of NFRs marked "current state does not meet target" — this is normal and useful, not failure.

---

## Cross-cutting: NFR vs FR boundary

When unsure if something is an FR or NFR, ask: "Is this WHAT the system does, or HOW WELL it does it?"

- "User can transfer funds" — FR (what)
- "Fund transfer completes within 2s" — NFR-PERF (how well)
- "Audit log records mutations" — FR (what)
- "Audit log retained for 7 years, tamper-resistant" — NFR-COMP + NFR-SEC (how well)
- "User can export their data" — FR (what)
- "Export completes within 30 days of request" — NFR-COMP (how well; per GDPR)

When in doubt, write both: an FR for the existence and an NFR for the quality envelope.
