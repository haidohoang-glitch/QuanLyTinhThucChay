# Business Context Capture — Adaptation

Variations by product type. Read only the section matching your project.

> **Applies to Mode A only.** Mode B/C adapt principles to your taxonomy.

## B2C consumer product

**Emphasize:**
- User personas (free vs paid, casual vs power user)
- Acquisition, activation, retention workflows (signup → first action → repeat)
- Notification/email/push triggers (these embed business rules)
- Account lifecycle: anonymous → authenticated → paid → churned

**Watch for:**
- Implicit personas hidden in feature flags
- "Onboarding" as a multi-step workflow that often has stuck states
- Anonymous-to-authenticated transitions (data preservation rules)

## B2B SaaS

**Emphasize:**
- Roles & permissions matrix (Owner / Admin / Member / Viewer / Guest)
- Tenant model (single workspace, multiple orgs, etc.)
- Plan tiers and feature gating rules (these ARE business rules)
- Audit logging requirements (often mandated by customer contracts)
- SLA-related invariants (uptime, response time)

**Watch for:**
- Per-tenant configuration as business rules (e.g., "Tenant X has SSO required")
- Admin override capabilities (often poorly documented)
- Suspended/deactivated tenant handling

## Marketplace (multi-sided)

**Emphasize:**
- Sides separately: Buyers, Sellers, Platform
- Trust & safety rules (KYC, fraud detection thresholds)
- Money flow workflows (escrow, payout, refund, dispute)
- Pricing rules (commission, fees, taxes)

**Watch for:**
- Cross-side rules ("Seller can ship only after Buyer pays AND ID verified")
- Race conditions in inventory/availability
- Dispute workflows with escalation paths

## Internal tool / Admin panel

**Emphasize:**
- Operations the company performs on customer data (this often IS the product)
- Audit trail of who-did-what-to-which-customer
- Override capabilities and their guardrails
- Read vs write distinction (many internal tools should be read-only)

**Watch for:**
- "Power user" personas blurring with "engineer" personas
- Authorization rules buried in conditionals (`if (user.email.endsWith('@ourcompany.com'))`)
- Hardcoded employee IDs

## Mobile-first product

**Emphasize:**
- Offline workflows (what works without connectivity, how sync resolves)
- Push notification rules (when, why, opt-out)
- Permission requests and the workflows that depend on them
- Account recovery flows (often diverge between mobile and web)

**Watch for:**
- Server-side rules vs client-side rules (clients lie; trust server)
- App version compatibility rules ("v3.x server requires app >= v2.5")

## ML / AI product

**Emphasize:**
- Inputs (what data the model consumes; often regulated)
- Outputs (predictions, recommendations) and how users consume them
- Feedback loops (does user behavior train the model?)
- Confidence thresholds as business rules ("show recommendation only if score > 0.7")
- Fallback behavior when model fails

**Watch for:**
- "Why did the model say that?" — explainability is often a business requirement
- Regulated decisions (loan approval, medical triage) — fairness/audit invariants

## Infrastructure platform / DevOps SaaS

**Emphasize:**
- Resource lifecycle (create / configure / monitor / decommission)
- Multi-environment isolation (dev / staging / prod boundaries are domain concepts)
- Quota and billing rules (per-resource, per-org)
- Cascading effects ("delete project deletes all resources within")

**Watch for:**
- Implicit assumptions about cloud provider behaviors
- Cost allocation rules across teams/projects

## Domain-heavy regulated products (Fintech, Healthtech, Legaltech)

**In addition to product type above:**
- Compliance rules ARE business rules (capture them in Section 6)
- Regulator-mandated invariants (capture in Section 8)
- Data residency rules
- Consent capture and audit trail
- Auditor / examiner as an actor (read-only access, periodic review)

These are not "add-ons" — they're often the most load-bearing part of the domain.

---

## Cross-cutting: legacy / acquired products

If capturing context for a product the team didn't originally build:

- Expect terminology drift (different code eras use different words)
- Expect dead code expressing business rules that no longer apply
- Document the *current* business view, but flag historical artifacts as Open Questions
- Interview is irreplaceable — but use this skill to prepare informed interview questions
