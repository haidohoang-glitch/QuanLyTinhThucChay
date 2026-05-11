# M2 — Overall Description

> **SRS Module 2 of 10** | Project: {{PROJECT_NAME}} | Version: v0.1 (DRAFT)

---

## 2.1 Product Perspective

### Context
{{PARAGRAPH — Is this product:
- Standalone? Part of a larger system? Replacing an existing system? An extension/integration?
- New to the market or an alternative to known products?
- Self-hosted, cloud SaaS, mobile app, embedded, hybrid?
}}

### System context diagram

```
{{ASCII_OR_MERMAID — show {{PROJECT_NAME}} as a box, with arrows to/from external systems, users, and data sources}}
```

External systems this product interacts with:

| External System | Direction | Purpose |
|-----------------|-----------|---------|
| {{SYSTEM}} | {{IN/OUT/BOTH}} | {{e.g., User authentication via SSO}} |
| {{SYSTEM}} | {{IN/OUT/BOTH}} | {{...}} |

---

## 2.2 Product Functions (Summary)

High-level capabilities. Detailed FRs are in M3-Mx.

- **{{FUNCTION_GROUP_1}}** — {{ONE_LINE_DESCRIPTION}}
- **{{FUNCTION_GROUP_2}}** — {{ONE_LINE_DESCRIPTION}}
- **{{FUNCTION_GROUP_3}}** — {{ONE_LINE_DESCRIPTION}}
- ...

This list maps to functional modules M3-Mx.

---

## 2.3 User Classes & Characteristics

| User class | Description | Tech literacy | Frequency of use | Privileges |
|------------|-------------|---------------|------------------|-----------|
| {{e.g., End-user (Customer)}} | {{DESCRIPTION}} | {{Low/Med/High}} | {{Daily/Weekly/Occasional}} | Read own data; create/update own records |
| {{e.g., Admin}} | {{DESCRIPTION}} | {{Tech-savvy}} | {{Daily}} | Manage all users, configure settings |
| {{e.g., Support Agent}} | {{DESCRIPTION}} | {{Med}} | {{Daily}} | Read all data; impersonate users for support |
| {{e.g., External API consumer}} | {{DESCRIPTION}} | {{High}} | {{Continuous}} | Scoped via API key |

User classes drive M3-Mx FRs (each FR usually applies to one or more classes) AND M9 NFRs (especially usability, performance per class).

---

## 2.4 Operating Environment

### Platforms

| Platform | Versions supported | Notes |
|----------|---------------------|-------|
| {{e.g., Web browser (desktop)}} | {{Chrome ≥110, Firefox ≥110, Safari ≥16, Edge ≥110}} | {{Notes}} |
| {{e.g., Web browser (mobile)}} | {{iOS Safari ≥15, Chrome Android ≥100}} | {{Notes}} |
| {{e.g., Native mobile app}} | {{iOS ≥15, Android ≥10}} | {{Notes}} |

### Server-side environment (if applicable)

- Cloud provider: {{e.g., AWS / GCP / Azure / multi-cloud / on-prem}}
- Region(s): {{e.g., us-east-1 primary; eu-west-1 read replica}}
- Runtime: {{e.g., Node.js 20+, Python 3.11+, JVM 17+}}
- Container platform: {{e.g., ECS Fargate / Kubernetes / serverless}}

### Integration environment

- Identity providers: {{e.g., Auth0, Okta, Azure AD}}
- Payment providers: {{e.g., Stripe, PayPal}}
- Email providers: {{e.g., SendGrid, AWS SES}}
- Other SaaS: {{LIST}}

---

## 2.5 Design and Implementation Constraints

These constraints are **non-negotiable** unless explicitly relaxed via change request. They limit the design space.

### Regulatory / Legal

| ID | Constraint | Source |
|----|------------|--------|
| CON-REG-01 | {{e.g., GDPR right-to-export within 30 days of request}} | EU Regulation 2016/679 |
| CON-REG-02 | {{e.g., PII encrypted at rest with customer-managed keys}} | {{REGULATION}} |
| CON-REG-03 | {{e.g., All financial transactions ≥ $10K logged with non-tamperable audit trail}} | {{INDUSTRY}} |

### Technology

| ID | Constraint | Reason |
|----|------------|--------|
| CON-TECH-01 | {{e.g., Backend in Node.js / TypeScript}} | {{Company standard / team skills / existing infra}} |
| CON-TECH-02 | {{e.g., Database: Postgres only}} | {{Compliance / DBA team support}} |
| CON-TECH-03 | {{e.g., Cannot introduce new vendor SaaS}} | {{Procurement freeze / DPA process}} |

### Operational

| ID | Constraint | Reason |
|----|------------|--------|
| CON-OPS-01 | {{e.g., Deploy via existing GitHub Actions → ECS pipeline}} | DevOps standard |
| CON-OPS-02 | {{e.g., RTO ≤ 4 hours, RPO ≤ 1 hour}} | Customer SLA |

### Business

| ID | Constraint | Reason |
|----|------------|--------|
| CON-BIZ-01 | {{e.g., Total annual cloud cost ≤ $X}} | Budget |
| CON-BIZ-02 | {{e.g., Must launch by {{DATE}} for {{EVENT}}}} | Commitment |

These constraints feed into M9 NFRs (often verbatim) and shape M3-Mx FRs (e.g., constraint says "no SaaS vendor" → cannot use third-party email API → email must be self-hosted SMTP).

---

## 2.6 User Documentation

What user-facing documentation will exist when the product ships:

| Documentation | Audience | Format | Owner |
|---------------|----------|--------|-------|
| {{e.g., User Manual / Help Center}} | End-user | {{Web / PDF}} | {{TEAM}} |
| {{e.g., API Reference}} | Developer integrators | {{OpenAPI HTML site}} | Engineering |
| {{e.g., Admin Guide}} | Admin user | {{Web}} | Product |
| {{e.g., Compliance Documentation}} | Auditors | {{PDF}} | Legal/Security |

---

## 2.7 Assumptions and Dependencies

### Assumptions (treated as true; if invalid, plan breaks)

| ID | Assumption | Risk if false |
|----|-----------|----------------|
| ASM-01 | {{e.g., Stripe webhook signature verification API stable through 2026}} | {{Re-implement webhook integration}} |
| ASM-02 | {{e.g., User base will not exceed 100K MAU in Year 1}} | {{Architecture rework for scale}} |
| ASM-03 | {{e.g., Existing SSO provider remains corporate standard}} | {{Auth flow rework}} |

### Dependencies (external; may slip)

| ID | Dependency | Owner | Impact if delayed |
|----|------------|-------|-------------------|
| DEP-01 | {{e.g., Compliance team approval of DPA template}} | Legal | Cannot launch in EU |
| DEP-02 | {{e.g., DevOps to provision VPC for new region}} | DevOps | Cannot deploy multi-region |
| DEP-03 | {{e.g., Vendor X SDK v2 release}} | Vendor X | Use SDK v1 (deprecated) |

---

## Cross-references for downstream modules

- **Constraints (2.5)** → influence many FRs in M3-Mx and most NFRs in M9
- **User classes (2.3)** → each FR in M3-Mx specifies which class triggers it
- **External systems (2.1)** → integration FRs in M3-Mx; SLA NFRs in M9
- **Assumptions (2.7)** → if invalidated, may require SRS amendment
