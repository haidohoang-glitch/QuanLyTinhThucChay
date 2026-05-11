---
name: data-architecture-audit
description: Audit a codebase's data architecture to produce a standardized DATA_ARCHITECTURE.md covering storage layers, schemas, data flow, governance gaps (PII, GDPR, retention, soft delete), consistency risks, and quota/cost concerns. Use when reviewing how a system stores and moves data, preparing data due diligence, generating Phase 1 Discovery output, or before any storage migration. Triggers include phrases like "audit the data layer", "review data governance", "where does data live", "find PII risks", "generate DATA_ARCHITECTURE", or "Phase 1 Discovery data".
---

# Data Architecture Audit

Produce a standardized `DATA_ARCHITECTURE.md` describing how a codebase stores, moves, and governs data. This is a *data view*, distinct from technical structure (codebase-discovery) and code quality (tech-debt-audit).

## When this skill applies

Use when:
- Auditing a system before storage migration (e.g., switching DBs, adding cache tier)
- Preparing for compliance review (GDPR, HIPAA, SOC2)
- Onboarding to a system whose data layer is unclear or undocumented
- Producing Phase 1 Discovery data output in the company doc standard

Do NOT use for:
- Pure code quality review (use `tech-debt-audit`)
- Codebase mapping (use `codebase-discovery`)
- Designing the new data architecture (use `tech-solution-design`)

## Output

A single file: `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`, filled from [assets/DATA_ARCHITECTURE_template.md](assets/DATA_ARCHITECTURE_template.md).

## Workflow

### Step 1 — Inventory data sources

Find every place data lives. Grep and read configs:

```bash
# Connection strings & SDK imports
grep -rE "DATABASE_URL|MONGO_URI|REDIS_URL|SUPABASE_URL|firebase" --include="*.{ts,js,py,go,env*}"
# ORM models
find . -path ./node_modules -prune -o -name "*.{model,schema,entity}.{ts,js,py}" -print
# Migration directories
ls migrations/ db/migrate/ supabase/migrations/ alembic/versions/ 2>/dev/null
# In-memory / browser state
grep -rE "useState|useReducer|createContext|localStorage|sessionStorage|IndexedDB" --include="*.{ts,tsx,js,jsx}"
```

Build a list: every store, where it's referenced, what it holds (one line each).

### Step 2 — Choose classification mode for storage layers

Three modes, same as `codebase-discovery`:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard layered model** *(default)* | No special instruction | Layer model in this skill |
| **B — Honor codebase's declared model** | Codebase has `DATA_GOVERNANCE.md`, `DATA_ARCHITECTURE.md`, or README declaring its model (Lakehouse, CQRS, Event Sourcing, Lambda Architecture) | Codebase docs |
| **C — User-defined classification** | User provides their own model (e.g., "by tenancy: shared / dedicated / hybrid") | User input |

Selection logic:
1. User explicitly named a mode → use it.
2. Codebase has explicit data architecture doc → ask user (Mode A or B?).
3. Default → Mode A.

Document mode and rationale in Section 9 Notes of the output.

#### Mode A — Standard layered storage model

Classify each store into ONE of these layers:

| Layer | Purpose | Examples |
|-------|---------|----------|
| **L1 — UI state** | Ephemeral, lost on page reload | React `useState`, Vuex, Pinia |
| **L2 — Browser persistence** | Survives reload, device-local | localStorage, sessionStorage, IndexedDB, cookies |
| **L3 — Edge/cache tier** | Server-side fast read, eventual consistency | Redis, Memcached, CDN, edge KV |
| **L4 — Primary data store** | Source of truth, transactional | Postgres, MySQL, Mongo, Firestore, DynamoDB |
| **L5 — Analytical/warehouse** | OLAP, batch queries | BigQuery, Snowflake, Redshift, Parquet on S3 |
| **L6 — Object storage** | Files, blobs, immutable | S3, GCS, Azure Blob, Cloudflare R2 |
| **L7 — Backup / archival** | Cold storage, DR | S3 Glacier, snapshots, point-in-time backups |
| **L8 — Third-party data** | Owned by SaaS providers | Stripe, Auth0, SendGrid records |

If a system uses multiple stores in the same layer (e.g., 2 Postgres DBs), list each separately.

#### Mode B — Honor codebase's declared model

Common declared models to map onto:
- **Lakehouse** (Bronze / Silver / Gold layers)
- **CQRS** (Command store + Read model store)
- **Event Sourcing** (Event log + projections)
- **Lambda Architecture** (Batch + Speed + Serving layers)
- **Hexagonal storage adapters** (one adapter per logical store)

Use the codebase's own naming. Cite the source doc in Section 9.

#### Mode C — User-defined classification

Examples: "by tenancy", "by data sensitivity tier", "by team ownership", "by retention class". Confirm categories with user before proceeding.

### Step 3 — Map schemas

For each L4/L5 primary store, list tables/collections. For each:
- Name
- Purpose (1 line)
- Row count estimate (if accessible)
- Key columns (PK, FKs, indexes worth noting)
- Sensitive fields (PII, secrets, credentials)

Do NOT paste full DDL. Curate.

### Step 4 — Trace data flow

For each major data type (user, transaction, product, etc.), draw the flow:

```
[Source] → [Validation] → [L4 write] → [L3 cache invalidate] → [L5 sync (batch?)]
[Read] ← [L3 cache] ← [L4 fallback] ← [L7 restore (if L4 lost)]
```

Identify:
- **Write paths**: who writes, sync vs async, transaction boundaries
- **Read paths**: where reads come from, cache strategy
- **Sync mechanisms**: ETL jobs, CDC streams, dual writes
- **Failure modes**: what happens if a store is unreachable

### Step 5 — Quantify quotas & costs

For each store:
- Quota (free tier limit, current plan limit)
- Current usage estimate (rows, GB, requests/day)
- Cost ($/month at current scale, projected at 10x scale)
- Bottleneck (which limit hits first as growth happens)

If unknown, mark "Unknown — needs measurement". This becomes Open Question.

### Step 6 — Detect governance gaps

Check explicitly for each:

| Concern | What to look for |
|---------|------------------|
| **PII inventory** | Which fields contain personal data (email, phone, address, IDs)? Are they tagged? |
| **GDPR right-to-export** | Is there a function to export all user data? Does it cover every store? |
| **GDPR right-to-delete** | Is there a function to purge user data? Does it cascade? Hard or soft delete? |
| **Retention policy** | Are old records deleted/archived after N days? Where is the policy defined? |
| **Audit trail** | Are mutations logged? Tamper-resistant? |
| **Encryption at rest** | Configured per store? Customer-managed keys? |
| **Encryption in transit** | TLS enforced for every connection? |
| **Access control** | Row-level security? Tenant isolation? Service accounts scoped? |
| **Backup & DR** | Backup frequency? Retention? Tested restore? RTO/RPO defined? |

Each gap is a finding for Section 7 of the output.

### Step 7 — Find consistency risks

Look for:
- **Dual writes without reconciliation**: code that writes to 2 stores in sequence, no rollback if second fails
- **Race conditions**: same data updated from multiple paths without optimistic concurrency (no `version` column, no transactions)
- **Eventual consistency leaks**: code reads its own writes from a cache and may see stale data
- **Distributed transactions**: 2PC, saga patterns — usually an indicator of complexity
- **Schema drift**: migrations not applied to all environments; staging vs prod schema differ

### Step 8 — Find data risks

- **Duplicates**: lack of unique constraints; "find by email" without case-insensitivity guarantee
- **Dangling references**: FKs that aren't enforced (some NoSQL, some sloppy SQL)
- **Hard deletes that lose history**: rows deleted with no soft-delete column
- **Hardcoded test data**: fixtures or seed data that leak into production
- **Multi-currency / multi-locale**: amounts stored without currency, dates without timezone

### Step 9 — Fill the template

Open [assets/DATA_ARCHITECTURE_template.md](assets/DATA_ARCHITECTURE_template.md), fill every `{{PLACEHOLDER}}`. Write to `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`.

### Step 10 — Self-review

Run [references/checklist.md](references/checklist.md). Do not deliver until all gates pass.

## Quality bar

A good `DATA_ARCHITECTURE.md` lets a reader answer in <10 minutes:
1. Where does each piece of data live?
2. How does data move between stores?
3. What happens to data when a user is deleted?
4. What's the cost trajectory at 10x growth?
5. What governance gaps exist (PII, GDPR, retention)?
6. What consistency risks should we worry about?

If any answer requires reading source code, the audit is incomplete.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations by primary store type (relational vs document vs key-value vs event log) and by app shape (SaaS multi-tenant vs single-tenant vs B2C consumer vs internal tool).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Helix", a healthcare records system with 4-layer storage and HIPAA constraints.

## Failure modes to avoid

- **Don't audit code quality.** That's `tech-debt-audit`. Stay on the data layer.
- **Don't propose fixes.** Findings are descriptive — what IS, what's RISKY. Solution proposals belong in Phase 2.
- **Don't list every column.** Curate. Highlight PII and primary keys, group the rest.
- **Don't trust env names blindly.** A var named `DATABASE_URL` may point to multiple things across deploys. Confirm.
- **Don't skip the governance section.** Even if everything looks fine, document what was checked. The audit value is the explicit check, not the absence of findings.
- **Don't conflate Mode A layers** when project clearly uses a different model. If forced into Mode A, the analysis becomes wrong, not just imprecise.
