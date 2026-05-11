# Feature Extension Planning — Quality Checklist

Run before promoting feature spec from Draft to Approved.

## Gate 1 — Coverage

- [ ] Section 1: What/Who/Why filled; success measure quantified
- [ ] Section 3: Mapped to existing FRs OR new FRs proposed
- [ ] Section 4: Design (user flow, data, API, UI, integration) covered
- [ ] Section 5: Schema migrations listed
- [ ] Section 6: Rollout plan with flag + stages
- [ ] Section 7: Test plan (unit, integration, manual TCs)
- [ ] Section 8: ≥2 risks with mitigations
- [ ] Section 9: Rollback plan specific
- [ ] Section 10: Implementation approach (single WP vs decompose)
- [ ] Section 11: Compliance review (if applicable; skip explicitly otherwise)
- [ ] Section 13: Decision log started

## Gate 2 — SRS alignment

- [ ] Existing FRs that this feature extends/affects are listed
- [ ] New FRs proposed have IDs + statements + priority
- [ ] No proposed FR conflicts with existing FR (resolved if conflict)
- [ ] NFR impact considered (Performance, Security, Compliance, Reliability)

## Gate 3 — Architecture alignment

- [ ] Design doesn't introduce new patterns when existing pattern fits
- [ ] If new pattern needed, escalate to `tech-solution-design`
- [ ] Component touches respect existing module boundaries
- [ ] No "while we're here" scope creep into unrelated code

## Gate 4 — Data discipline

- [ ] Migrations described as additive vs breaking
- [ ] Reversible migrations specified (rollback path)
- [ ] PII / sensitive data handling explicit if applicable
- [ ] Existing data unaffected (or migration plan stated)

## Gate 5 — Rollout rigor

- [ ] Feature flag named and default state specified
- [ ] Gradual stages defined with cutover criteria (not just dates)
- [ ] Backward compatibility addressed
- [ ] Customer communication planned (changelog, docs, announcement)

## Gate 6 — Test plan rigor

- [ ] Unit tests listed for new code paths
- [ ] Integration test covers user flow end-to-end
- [ ] Manual TCs have IDs and reach RTM
- [ ] Performance test if feature changes load profile
- [ ] Security test if feature changes auth surface

## Gate 7 — Risk & rollback

- [ ] Risks have likelihood + impact (not just listed)
- [ ] Each risk has mitigation
- [ ] Rollback plan is mechanical (steps, not "investigate")

## Gate 8 — Effort honesty

- [ ] Effort estimate (XS/S/M/L) matches scope
- [ ] If L, decomposition into WPs done (or planned)
- [ ] Dependencies on other work explicit

## Gate 9 — Compliance (if applicable)

If feature touches regulated data:

- [ ] Section 11 populated (data classification, lawful basis, audit, retention)
- [ ] Required reviewers identified
- [ ] DPIA done if GDPR Article 35 applies (high-risk processing)

## Gate 10 — Mode discipline

- [ ] Mode A: standard template
- [ ] Mode B: company template followed
- [ ] Mode C: user-defined sections; rationale documented

## Gate 11 — Format

- [ ] Output: `docs/04_MAINTENANCE/feature-extensions/FEAT_<NAME>.md`
- [ ] Filename describes feature clearly (snake_case or kebab-case)
- [ ] Status field accurate (Draft / Reviewed / Approved / In Implementation / Shipped)

## Self-review prompt

Read as the engineer who'll implement this. Could you start coding tomorrow without further questions? If not, sharpen.

Read as the QA engineer. Can you write the test plan from this spec? If not, expand Section 7.

Read as the architect. Does this respect existing patterns? If not, either align or escalate to system-level design.

Read as the customer. If something goes wrong, what's the user experience? If unclear, expand Sections 8 + 9.
