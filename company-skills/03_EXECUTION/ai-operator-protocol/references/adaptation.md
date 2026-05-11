# AI Operator Protocol — Adaptation

Variations by team and project context.

> **Applies to Mode A only.** Mode B/C follow company/user conventions.

## Solo operator (one person)

When one person operates AND fills additional roles:

**Adjust:**
- Operator gates remain mandatory (don't skip just because solo)
- Add explicit "second-set-of-eyes" step before high-risk merges (e.g., async peer review or tools like CodeRabbit)
- Cost monitoring more important (solo operator can lose track)

**Watch for:**
- Burnout from gate frequency; consider batching gates per WP rather than per task
- Tribal-knowledge accumulation (only operator understands AI behavior); document as you go

## Multi-operator team

When 2+ operators rotate:

**Adjust:**
- Standardize tooling (same AI vendors, same prompt templates) so handoffs work
- Shared PROGRESS_TRACKER must be live (Notion / Linear / shared markdown)
- Operator rotation cadence (weekly?) and how WP-in-progress hands off

**Add:**
- "Operator on call" rotation
- Daily standup snippet for AI-supervised WPs (5 min)
- Cross-operator review for system prompt changes (not unilateral)

## Senior operator team

When operators are senior engineers / tech leads:

**Adjust:**
- Trust on plan review can be lighter (skim vs. line-by-line)
- More Tier 3 freedom acceptable (senior catches issues fast)
- Cost monitoring less rigid (senior intuition catches anomalies)

**Watch for:**
- Senior overconfidence; AI can fool experienced engineers too
- "I'd write this myself" temptation; resist; trust the protocol

## Junior operator team

When operators are newer engineers:

**Adjust:**
- More gates; smaller batches per gate
- Restrict Tier 3 use (juniors can't easily detect Tier 3 mistakes)
- Pair-operate first 5-10 WPs
- Add "checkpoint with senior" rule for any new WP type

**Add:**
- Senior reviewer on every PR (not just rotating)
- "If unsure, pause" reinforcement

## Single AI vendor

When using only one vendor (e.g., only Claude):

**Adjust:**
- System prompts can be vendor-specific (use Claude's preferred patterns)
- Tier 1 / 2 / 3 map to specific Claude models (Haiku / Sonnet / Opus)
- Cost monitoring uses vendor's pricing

**Watch for:**
- Single point of failure (vendor outage stalls all WPs); have fallback plan

## Multi AI vendor

When using mix (e.g., Gemini Flash for Tier 1, Claude for Tier 2-3):

**Adjust:**
- System prompts must be vendor-agnostic where possible
- Document tier-to-vendor mapping
- Consistency: prompts produce equivalent output across vendors (test before relying)

**Add:**
- Per-vendor quirks documented (some vendors handle long prompts better; some are stricter on instructions)
- Fallback: if Vendor A unavailable, swap to Vendor B for that tier

## Regulated industries

When project handles PII / PHI / financial data:

**Adjust:**
- Hard rule: AI cannot read PII directly (anonymize before prompting OR use vendor with BAA/DPA)
- Audit log of every AI interaction required (some regulators)
- Reviewer for compliance-relevant changes mandatory

**Add:**
- Explicit data classification per WP (PII/PHI involved? if yes, extra checks)
- Compliance reviewer auto-assigned to PRs touching sensitive code
- "Tier 3 review" for any change affecting compliance controls

## High-security projects

When security is paramount:

**Adjust:**
- AI never sees secrets, even in prompt examples (use placeholder)
- AI never modifies security primitives (auth flow, crypto config) without human pair
- Secrets-in-diff scanner required in CI
- All AI commits signed (Sigstore / GPG) so verifiable later

**Add:**
- Security Lead approval gate for security-touching WPs
- Threat model review for changes affecting attack surface

## Customer-facing systems

When changes can impact users:

**Adjust:**
- UI changes require visual diff tool (Percy, Chromatic) before merge
- API changes require contract test
- Performance-sensitive changes require benchmark before merge

**Add:**
- Deployment timing rules (don't deploy to prod after 3pm Friday, etc.)
- Customer comms for visible changes

## Open-source projects

When project is open source:

**Adjust:**
- AI-authored commits clearly attributed (in commit message or co-author trailer)
- Public PR comments by AI labeled
- License compliance check on AI-generated dependencies

**Add:**
- Disclosure: "this PR includes AI-assisted changes"
- Contribution guidelines for AI-assisted PRs

---

## Per-project rule patterns

Common project-specific rules to consider:

| Pattern | Common in | Rule |
|---------|-----------|------|
| PHI handling | Healthcare | Compliance Lead in PR reviewers for any code touching PHI |
| Card data | Fintech | PCI scope reviewer for any change in CDE |
| Financial logic | Fintech | Two-engineer review (4-eye principle) on accounting code |
| Critical infra | Platform | Approval from infra owner on any IaC change |
| Schema changes | All | DBA review on migrations |
| Auth changes | All | Security Lead review on auth flow changes |
| Public API | Platform | API design review for new endpoints |
| Cron / scheduled jobs | Operations | Ops review for new scheduled jobs |

Pick the patterns that match your project; codify in Section 2 of operator guide.

---

## Avoiding protocol drift

Over time, teams may relax rules. Counter:

- Quarterly retrospective: verify each hard rule is still being followed
- New-team-member quiz: have new operators re-read and answer "what would you do if X?"
- Track violations: every protocol breach logged (PROGRESS_TRACKER notes); review trends

When 1 rule is repeatedly violated → either tighten enforcement OR retire the rule (if no longer load-bearing). Don't let rules silently rot.
