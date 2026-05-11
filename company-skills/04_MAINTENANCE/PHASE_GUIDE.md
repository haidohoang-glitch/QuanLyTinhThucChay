# Phase 4 — Maintenance: Hướng dẫn vận hành

> **Đặc thù:** Phase 4 là **ONGOING** — không có "complete" state. Chạy theo trigger (event-driven) hoặc schedule (cadence) trong toàn vòng đời production.
>
> **Tham khảo:**
> - [phase-4-orchestrator/SKILL.md](phase-4-orchestrator/SKILL.md)
> - [phase-4-orchestrator/references/runbook.md](phase-4-orchestrator/references/runbook.md)

---

## 1. Mục tiêu Phase 4

Giữ project **vận hành ổn định** trong production:
- Sự cố có runbook để xử lý nhanh
- Drift doc-vs-code phát hiện hàng tháng
- Inconsistency doc-vs-doc phát hiện hàng quý
- Feature mới có spec trước khi code

**Output Phase 4 (continuous):**
- `docs/04_MAINTENANCE/runbooks/INCIDENT_*.md` (build progressively)
- `docs/04_MAINTENANCE/feature-extensions/FEAT_*.md` (per feature)
- `docs/04_MAINTENANCE/DOC_SYNC_REPORT.md` (monthly, overwrites)
- `docs/04_MAINTENANCE/CONSISTENCY_REVIEW_REPORT.md` (quarterly)
- `_archive/` — mọi report cũ giữ lại

---

## 2. Skills trong Phase 4

| # | Skill | Trigger | Cadence |
|---|-------|---------|---------|
| 1 | `incident-response-playbook` | Pre-deploy + post-incident review + new failure mode | Per failure mode + per incident |
| 2 | `feature-extension-planning` | Feature request | Per feature |
| 3 | `documentation-sync` | Monthly + per significant PR | Monthly + ad-hoc |
| 4 | `document-consistency-review` (cross-cutting) | Quarterly + audit prep | Quarterly + audit |

**Orchestrator:** [`phase-4-maintenance-orchestrator`](phase-4-orchestrator/) — coordinate per trigger/schedule.

---

## 3. 4 Modes của orchestrator

| Mode | Description | Khi nào |
|------|-------------|---------|
| **A — Setup** | Build runbook library + schedule recurring tasks | One-time tại go-live |
| **B — Triggered** | Dispatch 1 skill per event (operator-driven) | Day-to-day operations |
| **C — Scheduled** | Run scheduled batch (monthly/quarterly/yearly) | Cron-like |
| **D — Audit prep** | Run multiple skills cho audit | Pre-audit |

---

## 4. Mode A — Setup tại go-live (BẮT BUỘC)

### 4.1 Khi nào

Trước go-live HOẶC trong tuần đầu sau go-live. KHÔNG skip.

### 4.2 Workflow

```
Step 1: Inventory failure modes (từ TECH_SOLUTION_DESIGN)
        → Typically 10-30 failure modes cho dự án trung bình

Step 2: Run incident-response-playbook per failure mode
        → P0/P1 trước (8-12 runbooks)
        → P2/P3 sau (trong 30 ngày)

Step 3: Schedule recurring:
        - Hàng tháng: documentation-sync (1st of month)
        - Hàng quý: document-consistency-review (Q-start)
        - Hàng năm: full Phase 4 review

Step 4: On-call training
        → Tabletop exercise top 3 P0 runbooks
        → On-call team đi qua từng step

Step 5: Setup report
        → docs/04_MAINTENANCE/_setup_report_<DATE>.md
```

**Prompt mẫu:**
```
Chạy phase-4-maintenance-orchestrator Mode A Setup.
TECH_SOLUTION_DESIGN ở docs/02_STRATEGIC/.
On-call: 4 engineers in rotation.
Go-live target: 2026-09-15.
```

---

## 5. Mode B — Triggered (day-to-day)

### 5.1 Trigger: Feature request

```
PM: "Bulk Customer Export feature"
    ↓
Operator triggers Mode B
    ↓
Orchestrator runs feature-extension-planning
    ↓
Output: docs/04_MAINTENANCE/feature-extensions/FEAT-042_*.md
    ↓
Operator decides routing:
    - Small (<1 tuần): direct to work-package-decomposer
    - Medium (1-4 tuần): mini Phase 2 (feasibility + design)
    - Large (>1 tháng): full Phase 2 orchestrator
    ↓
Hand-off Phase 3
```

### 5.2 Trigger: Sự cố

```
Alert: P0 incident
    ↓
On-call opens runbook (đã có sẵn từ Mode A)
    ↓
Follow NIST IR 6 phases per runbook
    ↓
Recovery confirmed
    ↓
Within 48 hr: post-incident review
    ↓
Update runbook với lessons
    ↓
If new failure mode: tạo runbook mới
```

**KHÔNG dùng orchestrator trong lúc P0 active** — on-call follow runbook trực tiếp. Orchestrator dùng cho post-incident.

### 5.3 Trigger: Code merge

```
PR merged
    ↓
CI hook: documentation-sync --scope=changed-files-only
    ↓
If drift: comment PR or open follow-up
    ↓
If material API/schema change: trigger feature-extension-planning để update SRS/ADR
```

---

## 6. Mode C — Scheduled cycles

### 6.1 Monthly (1st of month)

```
Step 1: documentation-sync (full scope)
Step 2: Operator review DOC_SYNC_REPORT.md
Step 3: For each High/Critical drift:
        - Create remediation ticket
        - Assign owner + target
Step 4: document-index-master refresh INDEX.md
Step 5: PROGRESS.md monthly cycle ✅
```

**Prompt:**
```
Chạy Mode C Monthly cycle. Today is 1st of [month].
```

### 6.2 Quarterly (Q-start)

```
Step 1: document-consistency-review (full)
Step 2: Operator + tech lead review CONSISTENCY_REVIEW_REPORT.md
Step 3: Address Critical/High findings within 1 sprint
Step 4: Skill suite review (skills v? available?)
Step 5: Phase 4 health report
```

### 6.3 Yearly

```
Step 1: Full re-audit (sync + consistency)
Step 2: Re-run project-context-ingestion (year of stakeholder change)
Step 3: Phase 0 freshness check (NFRs, regulations)
Step 4: Phase 2 strategy review (approved scenario còn đúng?)
Step 5: Skill version upgrade
Step 6: Major report → CEO/CTO
```

---

## 7. Mode D — Audit prep

### 7.1 Workflow

```
Pre-flight: Auditor + scope + deadline
    ↓
Step 1: documentation-sync full
Step 2: document-consistency-review full
Step 3: Address Critical findings (1-2 tuần)
Step 4: Spot-check 3 random runbooks
Step 5: Generate audit binder:
        - All Phase 0-4 docs current
        - Sync + Consistency reports
        - Runbook samples
        - Setup report
Step 6: Git tag snapshot
Step 7: Deliver to auditor before deadline
```

---

## 8. Hai cách vận hành (như các phase khác)

### 8.1 Cách A — Chạy từng skill riêng

Dùng khi:
- Single trigger event (1 feature, 1 incident review)
- Targeted update (chỉ documentation-sync, không quarterly)

**Prompt mẫu:**
```
Chạy skill feature-extension-planning cho FEAT-042 Bulk Customer Export.
Output: docs/04_MAINTENANCE/feature-extensions/FEAT-042_*.md.
Cite existing FRs nó touch.
```

### 8.2 Cách B — Qua orchestrator

Dùng khi:
- Mode A Setup (one-time tại go-live)
- Mode C Scheduled (monthly/quarterly/yearly cycles)
- Mode D Audit prep (multi-skill batch)
- Mode B per trigger nếu cần coordination với Phase 3 hand-off

---

## 9. Quality gate (per mode)

### Mode A Setup
- [ ] Runbook count ≥ 80% failure modes
- [ ] Schedules trong calendar
- [ ] On-call trained top 3 P0
- [ ] Setup report generated

### Mode B per trigger
- [ ] Trigger logged with timestamp
- [ ] Correct skill dispatched
- [ ] Output committed
- [ ] PROGRESS.md updated

### Mode C per cycle
- [ ] Cycle ran on schedule (or delayed rationale)
- [ ] Reports generated + reviewed
- [ ] Action items assigned
- [ ] Prior cycle items closed/rolled

### Mode D audit prep
- [ ] All evidence gathered
- [ ] Critical findings addressed
- [ ] Snapshot tag created
- [ ] Binder delivered before deadline

---

## 10. Cadence overall

| Cadence | Hoạt động |
|---------|-----------|
| **Hàng ngày** | (nothing scheduled — operator just monitor) |
| **Per feature** | feature-extension-planning |
| **Per incident** | runbook execution + post-incident review |
| **Per code merge** | quick doc-sync (changed files only, optional CI hook) |
| **Hàng tháng** | documentation-sync full + INDEX refresh |
| **Hàng quý** | document-consistency-review + skill suite review |
| **Hàng năm** | full re-audit + CONTEXT_PACK refresh + strategy review |
| **Pre-audit** | Mode D batch |
| **Major change** | trigger Phase 0/1/2 cascade tùy scope |

---

## 11. Common pitfalls

### 11.1 Skip Mode A Setup vì "go-live gấp"

**Hậu quả:** P0 lúc 2h sáng → on-call mò mẫm. MTTR thảm họa.

**Tránh:** Mode A bắt buộc trước hoặc trong tuần đầu go-live. Tối thiểu top 8-12 P0 runbooks.

### 11.2 Sự cố fix rồi không post-incident review

**Hậu quả:** Lần sau lại sự cố tương tự. Runbook outdated. Lessons mất.

**Tránh:** 48-hour post-incident review là hard rule. Update runbook luôn.

### 11.3 Skip monthly documentation-sync vì "docs đang đúng"

**Hậu quả:** Drift tích lũy. 6 tháng sau = 1 tháng khắc phục.

**Tránh:** Hàng tháng = 30 phút. Discipline.

### 11.4 Feature ship không có FEAT_*.md

**Hậu quả:** SRS không update. Drift. Audit fail. New devs confused.

**Tránh:** No feature ships without spec. Even mini-spec OK; KHÔNG có spec không OK.

### 11.5 Audit prep cramming (chạy lần đầu 1 tuần trước audit)

**Hậu quả:** Critical findings phát hiện trễ. Không kịp fix. Audit fail.

**Tránh:** Quarterly Mode C đều đặn → audit prep chỉ là copy compile.

### 11.6 Runbook không cập nhật sau env change

**Hậu quả:** Runbook commands fail trong P0 thực sự. Improvise → mistake.

**Tránh:** Quarterly runbook spot-check. Mỗi env change → audit affected runbooks.

### 11.7 Multiple incidents same root cause

**Hậu quả:** Treat individually = miss systemic issue.

**Tránh:** Pattern recognition. 3 incidents related → root cause analysis (có thể trigger Phase 2 partial re-loop).

---

## 12. Hand-off pattern Phase 4 → các phase khác

Phase 4 không có terminal hand-off (continuous), nhưng specific events trigger phase shift:

| Event | Trigger phase |
|-------|----------------|
| Feature request small | → Phase 3 directly (work-package-decomposer) |
| Feature request large | → Phase 2 orchestrator (mini-feasibility + design) |
| Major refactor needed | → Phase 1 re-discovery |
| Pivot / strategy change | → Pre-Phase 0 (re-ingest CONTEXT_PACK) → cascade |
| Pattern of incidents | → Phase 2 partial (architecture revisit) |

---

## 13. Time + cost (per year, medium project)

| Activity | Frequency | Cost/event | Total/year |
|----------|-----------|------------|------------|
| Mode A Setup | One-time | $30-100 | $30-100 |
| Mode B per feature (10/year) | 10× | $5-20 | $50-200 |
| Mode B per incident (~30/year) | 30× | $0-5 | $0-150 |
| Mode C monthly (12) | 12× | $5-15 | $60-180 |
| Mode C quarterly (4) | 4× | $10-30 | $40-120 |
| Mode C yearly | 1× | $30-100 | $30-100 |
| Mode D audit prep (typically 1-2/year) | 1-2× | $15-50 | $15-100 |
| **Total** | | | **~$225-950/year** |

Rất rẻ so với value của catching drift sớm + fast incident recovery.

---

## 14. FAQ Phase 4

**Q: Bao nhiêu runbook đủ tại go-live?**
→ Top 8-12 P0 (DB, auth, payment, deploy rollback, ...). P1/P2 trong 30 ngày sau. P3 khi có capacity.

**Q: Sự cố lúc ngoài giờ — operator (chính) có cần phối hợp?**
→ Không. On-call follow runbook trực tiếp. Operator chính nhận report sáng hôm sau, schedule post-incident review.

**Q: Feature small (<1 ngày work) có cần feature-extension-planning?**
→ Cho features có schema/API change: bắt buộc. Cho UI text change, version bump, typo fix: log entry trong PROGRESS.md đủ.

**Q: Monthly cycle bị skip 1 tháng — sao?**
→ Skip 1 OK, catch up next month. Skip 2+ → discipline broken, escalate.

**Q: documentation-sync có thể chạy CI per PR không?**
→ Có. Use `--scope=changed-files-only` cho quick check trên PR. Full scope chạy hàng tháng.

**Q: document-consistency-review tốn bao lâu?**
→ Quarterly full: 2-4 hr AI work + 1-2 hr operator review. Tổng 4-6 hr per quarter — chấp nhận được.

**Q: Audit deadline 1 tuần — có kịp Mode D?**
→ Nếu Mode C đã chạy đều: chỉ 4-8 hr work + remediation. Nếu chưa từng: 1-2 tuần work + likely Critical findings không kịp fix → negotiate extension.

**Q: Skills version mới — có phải migrate ngay?**
→ Test 1 dự án pilot trước. Sau 1-2 cycles ổn → rollout. Rush migration = bug nhân lên.
