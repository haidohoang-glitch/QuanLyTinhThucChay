# Business Context Capture — Worked Example

Anonymized. Fictional project: **"Project Mosaic"** — an educational learning platform for K-12 teachers. Mode A.

## Context

**Imagined input:** "Capture the business context — we just hired a new product manager and the original founder is leaving in 4 weeks."

**Time budget:** 5 hours.

---

## Generated output (excerpt)

```markdown
# Project Mosaic — Business Context

> Generated using: business-context-capture skill v1
> Last updated: 2026-04-30

## 1. Product Summary

Project Mosaic is a learning platform that lets K-12 teachers build, share, and assign
lesson plans to their students. Teachers create "Lessons" (multimedia content + practice
questions), organize them into "Units", and assign them to "Classes" (groups of students).
Students complete lessons individually; the platform tracks completion, mastery, and
flags students struggling with specific concepts. Schools subscribe at a per-classroom
rate, with a free tier for individual teachers (limited to 1 class).

**Domain area:** EdTech — K-12 supplemental learning
**Maturity / scale:** Growth stage; ~14K classrooms, ~280K students across 4 countries

## 3. Actors

| Actor | Description | How they enter | Tools |
|-------|-------------|----------------|-------|
| Teacher | Creates lessons, manages classes, reviews student progress | Email signup OR school SSO (Clever, ClassLink) | Web app |
| Student | Completes assigned lessons; sees own progress | Joins via class code OR roster sync from school | Web app + mobile-web |
| School Admin | Manages teachers and classes within a school | Invited by sales OR auto-provisioned via SSO | Web app (admin panel) |
| Sales Operator | Manages billing, plan upgrades, SSO config | Internal tool login | Internal admin panel |
| Content Curator | Reviews shared lessons before featuring them | Internal staff login | Web app (curator queue) |

### External actors (non-human)

| Actor | Trigger | Interface |
|-------|---------|-----------|
| Clever roster sync | Hourly cron | Pulls roster API |
| Stripe webhook | Subscription events | POST /webhooks/stripe |
| Email click tracking | User opens email | Pixel in email body |
| Daily digest cron | 6am school timezone | Builds + sends digest emails |

## 4. Use Cases

### Teacher

- UC-01: Teacher can create a Lesson (text, video, embedded quiz)
- UC-02: Teacher can organize Lessons into a Unit
- UC-03: Teacher can copy another teacher's public Lesson into own library
- UC-04: Teacher can assign a Lesson or Unit to a Class
- UC-05: Teacher can view aggregated Class progress
- UC-06: Teacher can view individual Student progress within their Classes
- UC-07: Teacher can mark a Student as needing extra support (manual flag)
- UC-08: Teacher can submit own Lesson to public library (subject to curator review)
- UC-09: Teacher can invite Students to a Class (via class code OR roster import)
- UC-10: Teacher can archive a Class at school year end

### Student

- UC-11: Student can join a Class via class code
- UC-12: Student can view assigned Lessons (in progress, not started, completed)
- UC-13: Student can complete a Lesson (answer practice questions, mark sections)
- UC-14: Student can see own progress and current "mastery score" per concept
- UC-15: Student can request hints during a Lesson (limited per Lesson)

### School Admin

- UC-16: School Admin can invite Teachers to school workspace
- UC-17: School Admin can deactivate a Teacher (existing Classes archived)
- UC-18: School Admin can configure SSO settings (Clever / ClassLink credentials)
- UC-19: School Admin can view aggregate metrics across all Classes in school
- UC-20: School Admin can request export of all student data (GDPR-style)

### Sales Operator (internal)

- UC-21: Sales can upgrade a school to paid tier
- UC-22: Sales can create custom invoices outside Stripe (for districts billing manually)
- UC-23: Sales can grant trial extensions

### Content Curator (internal)

- UC-24: Curator can approve / reject submitted Lessons
- UC-25: Curator can feature a Lesson in the public library
- UC-26: Curator can flag a Lesson for content policy review

(plus 12 more system/automated cases — daily digest, mastery recompute, etc.)

## 5. Domain Entities

| Entity | Definition (business terms) | Key attributes | Related to |
|--------|------------------------------|----------------|------------|
| Lesson | A learning unit a Student can complete | Title, content blocks, practice questions, mastery concepts tagged | Created by Teacher; assigned to Classes; tracked per Student |
| Unit | An ordered collection of Lessons | Title, ordered Lesson list | Owned by Teacher |
| Class | A group of Students taught by one Teacher | Class name, code, school year, archived flag | Owned by Teacher; contains Students |
| Student | An individual learner | Display name, grade level, masteries, struggle flags | Member of one or more Classes |
| Mastery Score | A 0-100 score for a Student on a specific Concept | Concept ID, score, last updated | Owned by Student; updated as Lessons completed |
| Concept | A learning standard or topic (e.g., "Fractions: equivalent") | Standard code (Common Core), grade level | Tagged on Lessons; referenced by Mastery |
| School | An institution containing Teachers and their Classes | Name, district, plan, SSO config | Contains Teachers, Classes |
| Submission Queue Item | A Teacher-submitted Lesson awaiting curator review | Status (pending/approved/rejected), submitted by, reviewer | Lesson; Teacher; Curator |

### Terminology notes

- Code uses `User` for the base entity; product calls them `Teacher` / `Student` / `School Admin` based on `User.role`. Always use the role name in product discussions.
- "Class" in code is `Classroom`; product team uses both interchangeably; UI uses "Class".
- "Concept" in code is `Standard` (after Common Core "standards"); product team uses "Concept" to be vendor-neutral. Reflected in UI as "Concept".

## 6. Business Rules

### 6.1 Validation Rules

| ID | Rule | Where enforced |
|----|------|----------------|
| BR-V-01 | Teacher email must be unique system-wide | `src/server/services/auth/signup.ts:34` (DB unique constraint on `users.email`) |
| BR-V-02 | Class code is 6 alphanumeric chars, unique per Teacher | `src/server/services/classes/create.ts:18` |
| BR-V-03 | Student display name 1-50 chars; no PII allowed (names get sanitized to first name only on roster sync) | `src/jobs/clever-sync/transform.ts:67` |
| BR-V-04 | Lesson submission requires ≥1 practice question and ≥1 concept tag | `src/server/services/lessons/submit.ts:22` |
| BR-V-05 | Mastery score is 0-100 inclusive | DB CHECK constraint `mastery_scores.score >= 0 AND score <= 100` |

### 6.2 Calculation Rules

| ID | Rule | Where enforced |
|----|------|----------------|
| BR-C-01 | Mastery score = weighted avg of last 5 attempts on Lessons tagged with that concept; recent attempts weighted 1.5x | `src/server/services/mastery/recompute.ts:42` |
| BR-C-02 | Class progress = average of Student completion rates for assigned Lessons | `src/server/services/classes/progress.ts:18` |
| BR-C-03 | Hint usage limit = 3 per Lesson per Student; resets on new attempt | `src/server/services/lessons/hint.ts:14` |
| BR-C-04 | Free tier limit: 1 active Class per Teacher | `src/server/services/classes/create.ts:9` |
| BR-C-05 | Pro tier price = $99/year/Teacher; School tier = $4/student/year billed annually | `src/server/services/billing/pricing.ts:6` |

### 6.3 Eligibility / Authorization Rules

| ID | Rule | Where enforced |
|----|------|----------------|
| BR-A-01 | Teacher can view Students only in own Classes | `src/server/middleware/authorize.ts:30` |
| BR-A-02 | Student can view only own Mastery Scores; cannot view other Students' | `src/server/middleware/authorize.ts:55` |
| BR-A-03 | School Admin can act on Teachers within own School only | `src/server/middleware/authorize.ts:78` |
| BR-A-04 | Student under 13 cannot complete Lesson without parental consent on file (COPPA) | `src/server/services/students/can-complete.ts:8` |
| BR-A-05 | Submitted Lesson goes to public library only after curator approval | `src/server/services/lessons/lifecycle.ts:24` |
| BR-A-06 | Archived Class is read-only (no new assignments, no progress updates) | DB column `classes.archived_at` checked in writes |

(20 more rules omitted for brevity)

## 7. Workflows

### Workflow: Teacher creates and assigns a Lesson

**Trigger:** Teacher clicks "New Lesson" in dashboard

**Happy path:**
```
1. Teacher fills Lesson form (title, content, questions, concept tags)
2. Teacher saves Lesson (BR-V-04 validates)
3. Lesson stored in Teacher's library (private by default)
4. Teacher selects Class(es) and clicks "Assign"
5. Assignment created with due date
6. Each Student in Class receives notification (in-app + email if opted in)
7. Lesson appears in Student's "Not started" queue
```

**Failure paths:**
- Validation fails (BR-V-04) → Teacher sees inline errors, save blocked
- Teacher tries to assign to archived Class → blocked (BR-A-06)
- Student is COPPA-restricted → assignment created but Student cannot start (BR-A-04)

**Termination states:** Assignment created (success); Save aborted (cancellation)

### Workflow: Student completes a Lesson

**Trigger:** Student clicks Lesson in queue

**Happy path:**
```
1. Lesson loads; "in progress" state created
2. Student reads/views content blocks
3. Student answers practice questions
4. On final submit, system calculates Lesson score
5. Mastery scores recomputed for tagged concepts (BR-C-01)
6. Lesson marked complete in Student's history
7. If concept-level mastery dropped, Teacher notified next morning (digest cron)
```

**Failure paths:**
- Network drops mid-Lesson → "in progress" state preserved; resumable
- Student abandons (closes tab) → state stays "in progress" indefinitely (Stuck state INV-related)

**Termination states:** Completed; Abandoned (no auto-cleanup)

### Workflow: Lesson submission to public library

**Trigger:** Teacher clicks "Share to Library"

**Happy path:**
```
1. Lesson enters Submission Queue (BR-A-05) → status pending
2. Curator reviews (typically within 5 business days per internal SLA)
3. Curator approves → Lesson visible in public library; Teacher notified
4. (Optional) Curator features → appears on home page
```

**Failure paths:**
- Curator rejects → Lesson stays private; Teacher notified with reason
- Lesson policy-flagged (BR-A-05 sub-clause) → Curator can suspend Teacher's submission privilege

**Termination states:** Public; Rejected; Policy-suspended
**Stuck states:** Pending status >5 days = SLA breach (no auto-escalation today — flagged in Open Questions)

## 8. Invariants

| ID | Invariant | Why it matters | Where enforced |
|----|-----------|----------------|----------------|
| INV-01 | Each Student belongs to ≥1 active Class OR is fully archived | Orphan students appear in no Teacher's view but consume seat count | App-layer check on Class deactivation |
| INV-02 | Mastery score for a concept is computed from ≥1 Lesson attempt | Otherwise score is meaningless (zero-data score) | `recompute.ts` returns null when no attempts |
| INV-03 | Public Lesson always has curator-approval timestamp | Establishes content provenance for school adoption | DB CHECK + trigger in `lessons.public_at` |
| INV-04 | Free tier Teacher has ≤1 active Class | Plan enforcement | App-layer check; race condition possible (OQ-2) |
| INV-05 | Student under 13 has parental consent record OR cannot start Lessons | COPPA compliance | App-layer check; not enforced at DB |
| INV-06 | Archived Class history is read-only and retained ≥1 school year | Audit / regrade requirements | App-layer; no DB constraint preventing writes |
| INV-07 | Class code is unique within Teacher and within active Classes | Prevents Student joining wrong Class | DB unique constraint |

## 9. Tensions & Ambiguities

| ID | Tension | Where seen | Suggested resolution |
|----|---------|------------|----------------------|
| T-01 | "Teacher" and "User" used interchangeably in code; product team treats them as distinct | `src/types/user.ts` | Adopt naming convention; align with product |
| T-02 | "Concept" (product) vs "Standard" (code) — confuses curator UI which mixes both | `src/components/curator/*` | Pick one for UI; keep DB column name; document mapping |
| T-03 | Free tier limit (BR-C-04) enforced only at create time; doesn't downgrade Teachers who become free again | `src/services/billing/downgrade.ts` (no enforcement found) | Decide: enforce hard or soft (warn + grace period) |
| T-04 | Lesson submissions can be policy-flagged but the Curator workflow does not surface this; relies on email | UI + workflow walkthrough | Build dedicated curator queue feature OR formalize email path |

## 10. Open Questions

| ID | Question | Where | Next step |
|----|----------|-------|-----------|
| OQ-1 | What's the policy on Lesson submissions stuck >5 days? | Workflow 7.3 has no escalation | Interview curator team lead |
| OQ-2 | Is BR-C-04 (free tier 1-class limit) racy? Two parallel POST creates can succeed | `src/services/classes/create.ts:9` no locking | Verify with concurrent test; recommend DB unique partial index |
| OQ-3 | When a Teacher is deactivated (UC-17), what happens to public library submissions they authored? | No code path found | Decide: keep visible (with attribution) vs hide vs anonymize |
| OQ-4 | Is mastery recompute idempotent? Re-running for same input should give same output | `recompute.ts:42` uses real-time clock for weighting | Replace with attempt timestamp; idempotency matters for audit |

## 11. Notes & Caveats

- **Decomposition mode:** A — DDD-lite.
- **Mode rationale:** Codebase has no formal bounded-context structure; standard Actor/UseCase/Entity model fits.
- **Capture scope:** Read all schema definitions; traced 3 critical workflows end-to-end (Lesson create, Student complete, Submission queue); reviewed all auth middleware. NOT done: user interviews; log analysis; revenue model deep dive.
- **Time spent:** 5 hours.
- **Confidence:** Medium-High for use cases and rules (extracted from code); Medium for workflows (some inferred); Lower for tensions T-01..T-04 (need PM validation).
- **Inferred items:** ~15% of business rules tagged "Inferred" — verify with PM/founder before relying on them in product decisions.
```

---

## Calibration notes

- **Use product's vocabulary.** "Mastery Score" not "MasteryScoreEntity". The skill's purpose is to make domain knowledge accessible.
- **Inferred items must be marked.** ~15% inferred is honest. 0% inferred suggests over-confidence; 50%+ suggests the auditor needs interviews not more reading.
- **Tensions are gold.** T-01..T-04 are the kind of finding that prevents bugs in future feature work. Don't skip this section because "code seems consistent at first glance".
- **Don't recommend.** Note "verify with PM" or "decide between options A/B" — but the decision isn't yours to make. This is descriptive, the decision is product/leadership.
- **Workflows surface the most ambiguity.** Especially failure paths and stuck states. These are usually under-documented in code.
