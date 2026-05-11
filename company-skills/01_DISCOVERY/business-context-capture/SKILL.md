---
name: business-context-capture
description: Extract business context from a codebase to produce a standardized BUSINESS_CONTEXT.md covering actors, use cases, domain entities, business rules, workflows, and invariants. Use when reverse-engineering domain knowledge from existing code, onboarding to an unfamiliar product, capturing tribal knowledge before team handover, or generating Phase 1 Discovery output. Triggers include "what does this product do", "extract business logic", "domain map", "capture business context", "generate BUSINESS_CONTEXT", or "Phase 1 Discovery domain".
---

# Business Context Capture

Reverse-engineer the BUSINESS view of a codebase: who uses it, what they do, what rules govern those actions, what invariants must hold. This is distinct from technical structure (`codebase-discovery`), data architecture (`data-architecture-audit`), and code quality (`tech-debt-audit`).

## When this skill applies

Use when:
- Onboarding to a product whose domain is unclear
- Tribal knowledge capture before key engineer departs
- Pre-rewrite or pre-major-feature work to ensure domain understanding survives the rewrite
- Generating Phase 1 Discovery business output for the company doc standard
- Bridging from code to SRS (this often becomes input to formal requirements)

Do NOT use for:
- Greenfield product definition (use `srs-greenfield-author`)
- Pure technical mapping (use `codebase-discovery`)
- Recommending changes to the product (this skill is descriptive only)

## Inputs (recommended)

This skill primarily reads code, but is significantly stronger when paired with raw stakeholder voice:

- **`docs/00_REQUIREMENTS/CONTEXT_PACK.md`** *(strongly recommended, from `project-context-ingestion`)* — gives you stakeholder terminology, intended workflows, and known business rules expressed by humans. Use it to validate code-derived findings, catch where code drifted from intent, and resolve ambiguities (Section 8 contradictions in the pack often map directly to code/stakeholder mismatches you'd otherwise discover the hard way).

If no CONTEXT_PACK exists, the skill still works but produces a code-only view — flag in BUSINESS_CONTEXT.md Section 9 (Open Questions) that stakeholder validation is needed.

## Output

A single file: `docs/01_DISCOVERY/BUSINESS_CONTEXT.md`, filled from [assets/BUSINESS_CONTEXT_template.md](assets/BUSINESS_CONTEXT_template.md).

## Workflow

### Step 1 — Identify primary actors

Look for who uses or triggers the system:

```bash
# Auth/role definitions
grep -rE "role|permission|isAdmin|UserRole|enum.*Role" --include="*.{ts,js,py}" .
# UI: navigation per user type
ls src/pages/admin/ src/pages/customer/ src/pages/dashboard/ 2>/dev/null
# API: route prefixes per audience
grep -rE "router\.use\(.*'/admin'|'/api/internal'|'/customer'" --include="*.{ts,js}"
# External actors: webhooks, cron, system jobs
ls src/webhooks/ src/jobs/ src/cron/ 2>/dev/null
```

Build a list of actors. Common: end-user, admin, system (cron/webhook), third-party API caller.

### Step 2 — List use cases per actor

For each actor, what can they do? Sources:
- UI navigation tree (every clickable feature is a use case)
- API endpoint list (every endpoint serves a use case)
- Cron job list (each scheduled task is a use case)
- Webhook handlers (each webhook represents an external trigger)

Format as: "{Actor} can {verb} {noun} {qualifier?}"

Example: "End-user can transfer funds between own wallets". "Admin can suspend any user account". "System can recompute exchange rates daily".

Aim for 15-50 use cases for a small/medium product. >100 means you should group into modules.

### Step 3 — Choose decomposition mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — DDD-lite** *(default)* | No special instruction | Actors / Use Cases / Entities / Rules / Workflows / Invariants |
| **B — Honor codebase's existing domain model** | Codebase explicitly uses bounded contexts, aggregates, or domain-modular structure | Codebase decomposition |
| **C — User-defined decomposition** | User provides own taxonomy (by persona, by revenue stream, by feature pillar, by customer segment) | User input |

Selection logic:
1. User explicit → use it.
2. Codebase has explicit DDD structure (e.g., `src/contexts/billing/`, ADRs about bounded contexts) → ask user (Mode A or B?).
3. Default → Mode A.

#### Mode A — DDD-lite structure

The output template is organized as:
- Section 3: Actors (who)
- Section 4: Use cases (what — grouped by actor or by domain area)
- Section 5: Domain entities (data nouns the business cares about)
- Section 6: Business rules (validations, calculations, eligibilities)
- Section 7: Workflows (multi-step user/system journeys)
- Section 8: Invariants (must-always-be-true conditions)

#### Mode B — Honor codebase's existing model

If the project explicitly says "we use DDD with bounded contexts: Billing, Identity, Inventory" — follow that:
- Group use cases, entities, and rules per bounded context
- Note context boundaries (ubiquitous language differences)
- Cite the source ADR / architecture doc

#### Mode C — User-defined

Examples:
- By persona: "Free user / Pro user / Admin / Support agent"
- By revenue stream: "Self-serve / Enterprise / White-label"
- By feature pillar: "Trading / Settlement / Reporting / Compliance"

Confirm categories with user before proceeding.

### Step 4 — Extract domain entities

Domain entities = nouns the business cares about. For each:
- Name (use the project's terminology — "Wallet" not "AccountStorage")
- One-line definition in business terms
- Key attributes the business cares about (not every column, just what matters)
- Relationships (1:N, M:N) with other entities

Sources to extract from:
- DB schema (filtered through "what would a product manager call this?")
- TypeScript types in `src/types/` or shared schemas
- API response shapes
- UI components (a "TransactionRow" component reveals what the business calls a transaction)

### Step 5 — Find business rules

Business rules govern HOW use cases execute. Three types:

| Type | Examples |
|------|----------|
| **Validation** | "Email must be unique per tenant", "Amount must be positive", "Username 3-20 chars" |
| **Calculation** | "Tax = subtotal × 8.875% if state=NY", "Late fee = $25 if days_overdue > 7" |
| **Eligibility / Authorization** | "Only Pro users can export", "Admin cannot suspend self", "Soft-deleted users excluded from reports" |

Where to find them:
- Validators (`Zod`/`Joi`/`Yup` schemas)
- Service-layer functions that throw business errors
- UI form validations (often duplicate of server validation)
- Conditionals in business-logic files (`if (user.tier !== 'pro') throw ...`)

Aim for 30-100 rules for a medium product. Cite file:line for each.

### Step 6 — Document workflows

Workflows = multi-step journeys spanning use cases. Examples:
- User registration: signup → email verify → onboarding → first action
- Order fulfillment: place → pay → reserve inventory → ship → confirm delivery
- Refund: request → admin review → process → notify

For each workflow:
- Trigger (what starts it)
- Steps (in order)
- Branches (success path, failure paths, abandonment)
- Termination (success state, failure state)
- Stuck states (workflows that can sit indefinitely — these are bugs or intentional)

### Step 7 — Identify invariants

Invariants = conditions that must ALWAYS hold, regardless of which workflow runs.

Examples:
- "Sum of debits = sum of credits in any user's wallet history"
- "A user always has exactly one default wallet"
- "Order total = sum of line items + tax + shipping (no discount applied yet at this step)"
- "An auth session is exactly one of: pending_email_verify / active / revoked"

Where to find:
- DB constraints (`UNIQUE`, `CHECK`, `FOREIGN KEY ... NOT NULL`)
- Trigger functions enforcing rules
- Tests that look like "verify the invariant after operation X"
- Comments saying "this must always be true"

Invariants are gold for catching bugs and for designing future changes.

### Step 8 — Find ambiguities & conflicts

Things that may signal:
- Same concept named differently in different parts ("account" vs "user" vs "customer" — three names, one or three things?)
- Rules that contradict (UI allows X, server rejects X)
- Workflow forks where success/failure unclear
- Missing termination ("what happens if user never finishes onboarding?")

These become Open Questions (Section 9 of output).

### Step 9 — Fill the template

Open [assets/BUSINESS_CONTEXT_template.md](assets/BUSINESS_CONTEXT_template.md), fill every `{{PLACEHOLDER}}`. Write to `docs/01_DISCOVERY/BUSINESS_CONTEXT.md`.

### Step 10 — Self-review

Run [references/checklist.md](references/checklist.md). Do not deliver until all gates pass.

## Quality bar

A good `BUSINESS_CONTEXT.md` lets a new product manager answer in <10 minutes:
1. Who are the users of this product?
2. What can each user type do?
3. What are the most important rules of the business domain?
4. What are the multi-step journeys users go through?
5. What invariants must never break (or the product is broken)?
6. Where are the domain ambiguities we should clarify?

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations by product type (B2C consumer, B2B SaaS, marketplace, internal tool, ML/AI product, infrastructure platform).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Mosaic", an educational learning platform.

## Failure modes to avoid

- **Don't describe how the code works.** That's `codebase-discovery`. Domain language only — "user can transfer funds" not "POST /api/transfers calls TransferService.execute".
- **Don't recommend product changes.** Descriptive only. If something feels wrong, flag as Open Question or "Tension Found".
- **Don't invent business rules.** If you're not sure a rule exists, say "Inferred from `src/x.ts:42`, needs PM confirmation".
- **Don't conflate UI strings with business rules.** A button label is not a business rule. The condition that hides/shows the button often is.
- **Don't skip invariants.** They are the most valuable part of the output and the easiest to skip.
- **Don't translate every technical term.** "Wallet" is fine. "Transaction" is fine. The goal is the business view, but you're not writing for non-technical readers — you're writing for product/eng who understand both.
