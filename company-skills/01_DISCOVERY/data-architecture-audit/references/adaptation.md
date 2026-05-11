# Data Architecture Audit — Adaptation

Variations to the base workflow. Read only the section matching your project.

> **Applies to Mode A only.** If using Mode B (honor codebase) or Mode C (user-defined), adapt principles but follow your chosen taxonomy.

## By primary store type

### Relational (Postgres, MySQL, SQL Server)

**Expand:**
- Schema inventory: include indexes, constraints, triggers
- Consistency: emphasize transaction isolation level, optimistic concurrency (`version` columns), foreign key enforcement
- Backup: PITR (point-in-time recovery), WAL archiving

**Watch for:** Missing indexes on frequently queried columns; missing FK constraints; outdated `pg_stat_statements`.

### Document store (MongoDB, Firestore, DynamoDB)

**Expand:**
- Schema inventory: document shape per collection (best-effort — schema is implicit)
- Consistency: which operations are atomic, which require multi-document transactions
- Cost: read/write counts, NOT row counts (different cost model)

**Watch for:** Inconsistent document shapes within a collection; large arrays nested in documents; queries that require full collection scan; quota traps (Firestore: 50K reads/day on free tier).

### Key-value / cache (Redis, Memcached, edge KV)

**Expand:**
- Eviction policy (LRU, LFU, none)
- Persistence (RDB snapshots, AOF, none)
- Cluster topology (sharded? replicated?)

**Watch for:** Used as primary store accidentally (data loss on flush); keys with no TTL piling up; cache stampede risks.

### Event log (Kafka, Kinesis, EventBridge)

**Expand:**
- Topic inventory (purpose, schema, retention)
- Consumer groups and lag
- Schema evolution policy (Avro/Protobuf? backwards compatible?)
- Replay/reprocessing capability

**Watch for:** Schema drift; long consumer lag; topics with PII and unbounded retention.

### Object storage (S3, GCS)

**Expand:**
- Bucket inventory (purpose, versioning, lifecycle policies)
- Access policies (public? signed URLs? IAM)
- Lifecycle (auto-transition to cheaper tier? auto-delete after N days?)

**Watch for:** Public buckets containing sensitive data; no lifecycle policy → unbounded cost growth; "all public via Cloudflare" patterns that bypass bucket ACLs.

### Analytical / warehouse (BigQuery, Snowflake, Redshift)

**Expand:**
- Dataset inventory (raw, cleaned, marts)
- ETL/ELT pipeline orchestrator (Airflow, dbt, Fivetran)
- Query cost model (per-query? per-slot? per-second?)

**Watch for:** Full-table scans on large tables (cost spike); raw PII landing in analytical layer without masking; data freshness mismatches.

---

## By application archetype

### SaaS multi-tenant (shared schema)

**Critical concerns:**
- Tenant isolation: every query MUST filter by `tenant_id`. Audit for missing filters.
- Row-level security: enforced at DB layer, not just application?
- Cross-tenant leakage: aggregate queries that accidentally span tenants
- Per-tenant quotas: rate limits, storage caps

### SaaS multi-tenant (schema-per-tenant or DB-per-tenant)

**Critical concerns:**
- Migration story: how schema changes propagate
- Operational complexity: backup, monitoring, debugging across N tenants
- Tenant onboarding: schema creation automation
- Tenant offboarding: full DB wipe, including backups

### Single-tenant SaaS / on-premise install

**Critical concerns:**
- Customer-controlled keys (BYOK) for encryption
- Data residency (where the customer's data physically sits)
- Upgrade path (schema migrations against running customer DB)
- Audit logs the customer can export

### B2C consumer app

**Critical concerns:**
- High user count → quota math very different
- GDPR / CCPA / regional law compliance
- Account deletion is end-user feature, not internal admin
- Anonymous → authenticated transition (preserving anonymous data?)

### Internal tool / B2B back-office

**Critical concerns:**
- Often skipped: encryption, PII tagging, audit trail (because "internal users")
- BUT: still required for SOC2, often more sensitive data than consumer apps
- Watch for "trust model" assumptions that don't survive employee turnover

### Mobile-first

**Critical concerns:**
- Offline-first sync mechanism — usually a major source of consistency bugs
- Local SQLite / Realm / IndexedDB on device
- Encrypted device storage (Keychain / Keystore)
- Backup behavior (iCloud? Google Backup? does it include the app's data?)

### ML / data science

**Critical concerns:**
- Training data lineage (where did it come from? was consent collected?)
- Model artifacts (where do .pkl/.pt files live? versioned?)
- Feature store consistency (same definition between training and serving)
- PII in training data (often present, often forgotten)

---

## Cross-cutting: regulated industries

If the project handles **healthcare data**, add HIPAA-specific checks (BAA with subprocessors, PHI inventory, access logs).

If **financial data**, add PCI-DSS-specific checks (CHD storage, tokenization).

If **EU-resident user data**, add GDPR-specific checks (DPA records, transfer mechanisms, consent flow data).

These are NOT alternative modes — they are additional checks layered on top of whichever mode (A/B/C) you chose.
