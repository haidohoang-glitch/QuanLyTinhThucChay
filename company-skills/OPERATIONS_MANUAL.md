# Cẩm nang Vận hành — Người + AI Agents khi Dự án đã có Skills + Docs

> **Tài liệu này khác gì với các tài liệu khác?**
>
> | Doc | Trả lời câu hỏi |
> |-----|------------------|
> | [INDEX.md](INDEX.md) | "Có những skills gì?" |
> | [GETTING_STARTED.md](GETTING_STARTED.md) | "Skills là gì, có nên dùng không?" |
> | [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) | "Lần đầu tạo docs, chạy skills theo thứ tự nào?" |
> | [VALUE_COMPARISON.md](VALUE_COMPARISON.md) | "ROI của skills so với không có?" |
> | **`OPERATIONS_MANUAL.md` (file này)** | **"Đã có skills + docs rồi, ngày-qua-ngày làm gì?"** |
>
> **Audience kép:**
> - **Người** (operator, dev, PM, tech lead, stakeholder)
> - **AI agents** (Claude / GPT / agent autonomy)
>
> **Đọc:** Phần 1-3 cho người mới (~15 phút). Phần 4-12 tra cứu khi gặp tình huống.

---

## 1. Cấu trúc dự án chuẩn

Dự án đã setup skills + docs có cấu trúc:

```
project-root/
├── INDEX.md                              ← Master nav (sinh bởi document-index-master)
├── PROGRESS.md                           ← Tracker per-skill run
├── company-skills/                       ← 19 skills (symlink hoặc submodule)
│   ├── INDEX.md
│   ├── GETTING_STARTED.md
│   ├── WORKFLOW_GUIDE.md
│   ├── VALUE_COMPARISON.md
│   ├── OPERATIONS_MANUAL.md              ← file này
│   └── 00_REQUIREMENTS/, 01_DISCOVERY/, ...
│
├── docs/                                 ← Output của skills
│   ├── 00_REQUIREMENTS/
│   │   ├── CONTEXT_PACK.md               ← project-context-ingestion
│   │   ├── _sources/                     ← raw sources, anonymized
│   │   │   └── SRC-001.md, SRC-002.md, ...
│   │   ├── SRS_VI/
│   │   │   ├── M1_Introduction.md
│   │   │   ├── M2_Overall_Description.md
│   │   │   ├── M3_<Domain>.md ... Mx_<Domain>.md
│   │   │   ├── M9_Non_Functional_Requirements.md
│   │   │   └── M10_RTM_Issues_Appendix.md
│   │   └── _archive/                     ← Bản cũ khi re-run skill
│   │
│   ├── 01_DISCOVERY/
│   │   ├── CODEBASE_MAP.md
│   │   ├── DATA_ARCHITECTURE.md
│   │   ├── BUSINESS_CONTEXT.md
│   │   ├── TECH_DEBT_AUDIT.md
│   │   └── _archive/
│   │
│   ├── 02_STRATEGIC/
│   │   ├── FEASIBILITY_ASSESSMENT.md
│   │   ├── TECH_SOLUTION_DESIGN.md
│   │   ├── MASTER_PLAN.md
│   │   └── _archive/
│   │
│   ├── 03_EXECUTION/
│   │   ├── AI_OPERATOR_GUIDE.md
│   │   ├── AI_AGENT_TASK_DISTRIBUTION.md
│   │   ├── work-packages/
│   │   │   ├── PHASE_0_*.md, PHASE_1_*.md, ...
│   │   │   └── decomposed/<WP-ID>_tasks.md
│   │   └── _archive/
│   │
│   └── 04_MAINTENANCE/
│       ├── DOC_SYNC_REPORT.md
│       ├── CONSISTENCY_REVIEW_REPORT.md
│       ├── runbooks/INCIDENT_*.md
│       ├── feature-extensions/FEAT_*.md
│       └── _archive/
│
└── src/, tests/, ...                     ← codebase
```

**Quy ước:**
- `_archive/` lưu bản cũ khi re-run skill (timestamped: `<DOC>_2026-04-15.md`)
- `_sources/` chỉ trong `00_REQUIREMENTS/`, lưu raw inputs đã anonymize
- File ở root project (`INDEX.md`, `PROGRESS.md`) — phần còn lại trong `docs/`

---

## 2. Roles & Trách nhiệm

### 2.1 Roles của người

| Role | Trách nhiệm chính | Skills tương tác chủ yếu |
|------|---------------------|---------------------------|
| **Operator** | Chạy skills, dispatch AI agents, maintain docs | Mọi skill — chính là người vận hành |
| **Tech Lead / Architect** | Approve ADR, review tech-solution-design, ký gate G2 | `tech-solution-design`, `implementation-planning` |
| **PM / Project Owner** | Quản lý timeline, communicate stakeholder, ký gate G1 | `feasibility-assessment`, `feature-extension-planning` |
| **Stakeholder** (CEO, CFO, customer) | Quyết định scope/budget; resolve contradictions từ CONTEXT_PACK | Pre-Phase 0, Phase 2 |
| **Compliance / Legal** | Verify NFR + regulatory; audit prep | `nfr-specification`, `requirements-traceability`, `document-consistency-review` |
| **On-call engineer** | Vận hành runbook khi có sự cố | `incident-response-playbook` |
| **QA / Reviewer** | Verify per-skill checklist, sign quality gate | All skills (read `references/checklist.md`) |

**Một người có thể đảm nhiệm nhiều role** (ví dụ Operator kiêm QA cho team nhỏ). Quan trọng là **mỗi role bắt buộc có người** ở giai đoạn của role đó.

### 2.2 Roles của AI agents

| Role | Mô tả | Tier khuyến nghị |
|------|-------|--------------------|
| **Orchestrator** | Đọc operator request → chọn skill phù hợp → dispatch executor | Tier 3 (Opus-class) — quyết định phức tạp |
| **Executor** | Chạy 1 skill cụ thể, sinh output theo template | Tier 2 (Sonnet-class) cho hầu hết, Tier 3 cho SRS/feasibility |
| **Reviewer** | Verify output qua `references/checklist.md`, flag issue | Tier 2 — đủ để check format |
| **Scaffolder** | Sinh boilerplate, tạo placeholder, format Markdown | Tier 1 (Haiku-class) — rẻ, nhanh |
| **Decomposer** | Chia WP thành micro-tasks (chạy `work-package-decomposer`) | Tier 3 — vì cần judgment routing |

**Quy ước phân vai:**
- 1 conversation/session = thường 1 vai trò AI. Đừng để 1 AI vừa orchestrate vừa execute — context sẽ pollute.
- Operator (người) là điều phối tối cao. AI orchestrator đề xuất, người quyết.

---

## 3. Lifecycle của 1 document

Mỗi doc trong `docs/` đi qua 6 trạng thái:

```
[1] CREATED          ← Skill chạy lần đầu, sinh từ template
       ↓
[2] DRAFT REVIEW     ← Operator + reviewer kiểm checklist
       ↓
[3] STAKEHOLDER OK   ← (Phase 0/2/4 docs) — stakeholder ký
       ↓
[4] ACTIVE           ← Used as reference, có thể edit thủ công cho update nhỏ
       ↓
[5] DRIFT DETECTED   ← documentation-sync hoặc consistency-review báo
       ↓
[6] REFRESHED        ← Re-run skill, archive bản cũ
       ↓ (loop về [4])
```

**Mỗi doc có metadata header bắt buộc:**

```markdown
---
doc_id: SRS-M3-CUSTOMER
title: M3 — Customer Management Functional Requirements
status: ACTIVE
phase: 0
source_skill: srs-reverse-engineer
generated_at: 2026-04-12
last_edited: 2026-05-01 (operator: jane@company)
last_skill_refresh: 2026-04-12
owner: Tech Lead
review_cadence: quarterly
---

# M3 — Customer Management ...
```

**Quy tắc edit:**
- Update nhỏ (typo, thêm 1 FR, clarify câu) → edit trực tiếp + bump `last_edited`
- Update lớn (restructure, scope change, contradiction) → re-run skill, đừng patch

---

## 4. Vận hành hằng ngày

### 4.1 Operator daily routine (~30-60 phút/ngày cho project active)

**Mỗi sáng:**

1. Mở `PROGRESS.md` → kiểm trạng thái phase hiện tại
2. Mở `docs/04_MAINTENANCE/DOC_SYNC_REPORT.md` (nếu có) → check drift mới
3. Mở issue tracker / Slack → check feedback từ stakeholder/reviewer
4. Chạy AI orchestrator với prompt:

```
Hôm nay đang ở phase [X] của project [TÊN].
Đọc PROGRESS.md + DOC_SYNC_REPORT.md.
Đề xuất 3 việc ưu tiên hôm nay (highest-impact, blocking nhất).
KHÔNG tự execute — chỉ đề xuất.
```

5. Operator approve list → AI execute từng việc → Operator review → commit.

**Cuối ngày:**

1. Update `PROGRESS.md` (skill nào chạy, output gì, checklist passed)
2. Commit + push (xem Section 6 conventions)

### 4.2 Mỗi WP (Work Package) — Phase 3

```
Operator → AI orchestrator: "Bắt đầu WP-X.Y"
↓
AI orchestrator: kiểm dependency (WP trước đã done?)
                 → load WP spec từ docs/03_EXECUTION/work-packages/PHASE_*_*.md
                 → propose: "Chạy work-package-decomposer cho WP-X.Y?"
↓
Operator approve
↓
AI executor: chạy decomposer → sinh tasks file
↓
Operator: review tasks file → approve hoặc adjust tier
↓
AI executor: thực thi từng task theo dependency order
              → mỗi task: prompt → code change → verify command → diff
              → log vào PROGRESS or task tracker
↓
AI reviewer: chạy checklist toàn WP
↓
Operator: final review → commit
```

### 4.3 Cadence định kỳ

| Cadence | Hoạt động | Chủ trì | Skill |
|---------|-----------|---------|-------|
| **Hàng ngày** | Operator daily routine | Operator | (none) |
| **Mỗi WP** | Decompose + execute + verify | Operator + AI | `work-package-decomposer` |
| **Hàng tuần** | Sync với stakeholder, update PROGRESS, triage issues | PM | (none) |
| **Hàng tháng** | Doc-vs-code drift audit | Operator | `documentation-sync` |
| **Mỗi feature mới** | Mini-spec + plan | PM + Tech Lead | `feature-extension-planning` |
| **Hàng quý** | Doc-vs-doc consistency audit | Operator | `document-consistency-review` |
| **Hàng quý** | Skill suite review (cập nhật v?) | Tech Lead | (none — ngoại bộ) |
| **Trước go-live** | Runbook chuẩn bị cho mọi failure mode | Operator + on-call | `incident-response-playbook` |
| **Khi có sự cố** | Run runbook → post-incident review | On-call → Operator | `incident-response-playbook` |
| **Khi pivot/rewrite/stakeholder mới** | Re-ingest context | Operator | `project-context-ingestion` |
| **Hàng năm** | Audit prep, full re-review | Compliance + Tech Lead | nhiều skill |

---

## 5. Cây quyết định: Khi nào dùng skill vs edit doc thẳng?

```
Bạn cần thay đổi 1 doc.
│
├── Lỗi chính tả, format nhỏ?
│       → Edit thẳng. Bump `last_edited`. Commit.
│
├── Bổ sung 1 FR / NFR đơn lẻ vào module đã có?
│       → Edit thẳng + cite source [SRC-NNN] hoặc rationale trong commit message.
│       → Nếu thay đổi >5 FR cùng lúc → re-run skill.
│
├── Restructure 1 module (vd: gộp M3+M4)?
│       → Re-run SRS skill. Đừng patch.
│
├── Có thông tin mới từ stakeholder làm thay đổi nhiều phần?
│       → Re-run upstream skill (project-context-ingestion → cascade)
│
├── Phát hiện code đã đổi, doc chưa update?
│       → Hai lựa chọn:
│         (a) Edit thẳng nếu thay đổi nhỏ (1-2 references)
│         (b) Re-run skill nếu thay đổi systemic
│       → documentation-sync sẽ flag mỗi tháng nếu sót
│
├── Stakeholder đổi quyết định (scenario approval, scope change)?
│       → Re-run feasibility-assessment + cascade tech-solution-design + planning
│
├── Pivot toàn bộ?
│       → Quay lại Pre-Phase 0, full re-ingestion, archive bản cũ
│
└── Không biết?
        → Hỏi orchestrator AI: "Thay đổi này nên edit thẳng hay re-run skill nào?"
```

**Quy tắc vàng:** Nếu phải sửa >20% nội dung của 1 doc → re-run skill. Nếu <20% → edit thẳng. Lý do: edit lớn thủ công thường thiếu nhất quán; re-run skill đảm bảo qualityskeleton.

---

## 6. Conventions — Git, branch, commit

### 6.1 Branch naming

| Prefix | Mục đích | Ví dụ |
|--------|----------|-------|
| `skill/<skill-name>/<date>` | Re-run 1 skill, output mới | `skill/srs-reverse-engineer/2026-05-06` |
| `wp/<wp-id>` | Thực thi 1 Work Package | `wp/0.E-error-boundaries` |
| `doc/<doc-id>` | Edit thủ công 1 doc | `doc/m3-customer-add-fr-export` |
| `incident/<id>` | Xử lý sự cố | `incident/2026-05-06-pg-primary-down` |
| `feature/<feat-id>` | Feature mới | `feature/feat-042-bulk-export` |

### 6.2 Commit message convention

```
<type>(<scope>): <summary>

<body — what changed and why>

<refs — skill version, source skill run, related FRs/ADRs>

<co-author — if AI executed>
```

**Types:**
- `skill` — output của skill chạy
- `doc` — edit thủ công vào doc
- `wp` — code change từ work package execution
- `incident` — incident response artifact
- `audit` — output của audit skill (sync, consistency)

**Ví dụ:**

```
skill(00_REQUIREMENTS): refresh CONTEXT_PACK after CEO interview update

Re-ran project-context-ingestion với 3 nguồn mới (SRC-018..020).
Surface 1 contradiction mới về timeline (CON-4).
Bản cũ đã archive: docs/00_REQUIREMENTS/_archive/CONTEXT_PACK_2026-04-12.md

Skill version: project-context-ingestion v1
Run by: AI executor (Sonnet) supervised by jane@company
```

```
doc(SRS-M3): add FR-CUSTOMER-09 bulk import

Thêm 1 FR theo yêu cầu sales team (ticket #4521).
Source: support log [SRC-012] — top-3 unmet request.
RTM cập nhật trong follow-up commit.

Co-Authored-By: Claude (operator approved 2026-05-06)
```

### 6.3 Archive rule

Khi re-run skill:

1. Move bản hiện tại vào `_archive/<DOC>_<YYYY-MM-DD>.md`
2. Ghi changelog vào commit body
3. Update `PROGRESS.md` row tương ứng

```bash
# Pseudocode mà operator/AI follow
cp docs/00_REQUIREMENTS/CONTEXT_PACK.md docs/00_REQUIREMENTS/_archive/CONTEXT_PACK_$(date +%F).md
# rồi mới re-run skill ghi đè CONTEXT_PACK.md
```

### 6.4 Tagging important versions

```
git tag -a docs-phase0-complete-2026-05-01 -m "All M1-M10 + INDEX done, stakeholder approved"
git tag -a audit-prep-2026-Q2 -m "Snapshot for SOC2 audit Q2 2026"
```

Tags để rollback hoặc reference khi audit.

---

## 7. Communication protocol

### 7.1 Người → AI (prompts hằng ngày)

**Pattern 1 — Discovery prompt (lúc bắt đầu):**
```
Project: [TÊN]
Current phase: [P0/P1/P2/P3/P4]
Last skill run: [SKILL_NAME] on [DATE]
Goal hôm nay: [GOAL]

Đọc INDEX.md + PROGRESS.md + relevant docs trong docs/[PHASE]/.
Đề xuất plan + list skill cần chạy. KHÔNG tự execute.
```

**Pattern 2 — Skill run prompt (sau khi đã align):**
```
Chạy skill <skill-name> với inputs:
- [list inputs]

Mode: [A/B/C]
Output: <path>
Constraints: [budget cap, deadline, must-honor things]

Sau khi xong:
1. Run references/checklist.md
2. Tóm tắt changes vs bản cũ (nếu re-run)
3. List Open Questions / blockers
4. KHÔNG tự commit — đợi tôi review
```

**Pattern 3 — Verify prompt:**
```
Verify output của skill vừa chạy (file: <path>).
Đi qua references/checklist.md mục một.
Trả: PASS / FAIL per gate + lý do nếu FAIL.
```

**Pattern 4 — Cascade prompt (khi update upstream → downstream):**
```
CONTEXT_PACK.md vừa refresh (xem _archive/CONTEXT_PACK_<DATE>.md để diff).
Skill nào downstream bị affect? List + đề xuất re-run order.
KHÔNG tự re-run — chờ tôi approve.
```

### 7.2 AI → AI handoff (trong agent system phức tạp)

Nếu có nhiều AI agent (orchestrator → executor → reviewer):

```
[Agent A → Agent B handoff message format]

FROM: orchestrator
TO: executor
TASK: Run skill <name>
INPUTS: [paths]
CONSTRAINTS: [list]
SUCCESS CRITERIA: [from checklist.md]
DEADLINE: [optional]
ESCALATION: if blocked, return to orchestrator with: blocker + tried + recommended next
```

### 7.3 Người ↔ Người (escalation paths)

| Tình huống | Escalate tới |
|------------|--------------|
| Skill output có lỗi hệ thống (>3 dự án gặp) | Skill maintainer (Tech Lead pháp định) |
| Stakeholder contradict — Operator không resolve được | PM → CEO (chỉ contradiction critical) |
| AI agent rule violation (vi phạm hard rule trong AI_OPERATOR_GUIDE) | Operator → kill session, log incident |
| Sự cố production | On-call → tech lead → CEO (tùy severity) |
| Audit finding | Compliance → Tech Lead → CEO |

---

## 8. Conflict resolution

### 8.1 Skill output vs manual edit

Tình huống: Doc có manual edits + bạn muốn re-run skill (sẽ ghi đè).

**Quy trình:**
1. Diff bản hiện tại với `_archive/` (bản skill sinh lần trước)
2. List các manual edit (mỗi edit = 1 commit/diff hunk)
3. Cho mỗi edit, hỏi:
   - Edit này có cần preserve trong bản mới? Nếu có → ghi vào `MANUAL_EDITS_TO_PRESERVE.md` tạm
4. Re-run skill
5. Manual port các edit cần preserve sang bản mới (nếu skill không đã handle)
6. Commit với note "preserved manual edits from <commit-hash>"

**Tools:**
```bash
git log --follow docs/00_REQUIREMENTS/SRS_VI/M3_*.md  # see edit history
git diff <archive-hash> HEAD -- docs/00_REQUIREMENTS/SRS_VI/M3_*.md  # see manual edits
```

### 8.2 Doc vs code drift

`documentation-sync` flag drift. Resolution:

| Drift type | Action |
|------------|--------|
| Code đúng, doc sai | Update doc (edit thẳng nếu nhỏ; re-run skill nếu lớn) |
| Doc đúng (per stakeholder), code sai | Open ticket — code bug, fix code |
| Cả hai đều outdated (specification đổi) | Re-ingest CONTEXT_PACK → cascade |
| Không rõ cái nào đúng | Escalate: hỏi stakeholder hoặc reviewer |

### 8.3 Stakeholder disagreement

`project-context-ingestion` Section 8 surface contradictions. Resolution:

1. Operator schedule meeting với conflicting stakeholders
2. Meeting có agenda là contradiction list
3. Decision documented:
   - Vào CONTEXT_PACK Section 8 (resolved column)
   - Vào ADR (nếu là architectural decision)
   - Vào meeting minutes (file ở `_sources/` luôn)
4. Re-run downstream skills nếu decision affect Phase 0+

### 8.4 Multi-AI disagreement

Nếu 2 AI agents (executor vs reviewer) bất đồng:

1. Reviewer flag specific finding
2. Operator đọc cả hai output
3. Operator quyết → log decision với reasoning
4. Update skill `references/examples.md` để skill học pattern này lần sau

---

## 9. Quality gates — Ai approve khi nào?

### 9.1 Per-skill output gate

| Gate | Người approve | Khi nào |
|------|---------------|---------|
| Checklist completion | AI Reviewer | Auto sau khi skill run |
| Format/structure | Operator | Trước commit |
| Content accuracy | Domain expert (PM/Tech Lead) | Trước stakeholder review |
| Stakeholder approval | Stakeholder | Critical docs only (FEASIBILITY, M9 NFR, ADR) |

### 9.2 Per-phase exit gate

| Phase | Exit gate | Approver |
|-------|-----------|----------|
| Pre-P0 | CONTEXT_PACK contradictions resolved hoặc explicitly deferred | PM |
| Phase 0 | M1-M10 complete, RTM gaps acknowledged | Tech Lead |
| Phase 1 | All 4 docs done, debt prioritized | Tech Lead |
| Phase 2 (G1) | Scenario chosen | Stakeholder (CEO/CFO) |
| Phase 2 (G2) | ADR approved | Tech Lead/CTO |
| Phase 3 per WP | Tasks completed + verify pass | Operator |
| Phase 3 (G3) | Pre-deploy review | Tech Lead + Ops |
| Phase 4 ongoing | (no gate — continuous) | (Operator weekly check) |

### 9.3 Emergency override

Có 1 hard rule: **Critical sự cố production có thể skip mọi gate documentation.** Fix trước, document sau (post-incident review). Nhưng phải document trong vòng 48h.

---

## 10. Onboarding checklist cho operator mới

### Day 1 (4 giờ)

- [ ] Đọc `INDEX.md` (~10 phút)
- [ ] Đọc `GETTING_STARTED.md` Phần 1-3 (~20 phút)
- [ ] Đọc `OPERATIONS_MANUAL.md` (file này) Phần 1-4 (~30 phút)
- [ ] Đi tour repo: mở từng folder trong `docs/<phase>/`, đọc 1-2 doc mẫu
- [ ] Đọc `PROGRESS.md` để hiểu trạng thái dự án
- [ ] Setup AI client (Claude Code / Cursor / etc)

### Day 2 (4 giờ)

- [ ] Đọc `WORKFLOW_GUIDE.md` Phần liên quan tới phase hiện tại
- [ ] Mở 1 SKILL.md mà dự án vừa chạy gần nhất → đọc step-by-step
- [ ] Mở `references/checklist.md` của skill đó → hiểu quality gate
- [ ] Mở `references/examples.md` → đọc worked example
- [ ] Trial run: chạy `documentation-sync` (skill nhẹ nhất, output rõ) trên 1 sub-folder, observe

### Day 3 (4 giờ)

- [ ] Shadow operator hiện tại 1 daily routine
- [ ] Tự chạy 1 skill thật (vd: `feature-extension-planning` cho 1 feature giả)
- [ ] Review output qua checklist
- [ ] Hỏi 1 senior 3 câu khó nhất

### Tuần 1

- [ ] Xử lý 1-2 issue thực (drift, missing doc, simple FR add)
- [ ] Lead 1 daily routine với supervision
- [ ] Đọc `VALUE_COMPARISON.md` để hiểu tại sao lại làm vậy

### Tháng 1

- [ ] Lead 1 phase transition (vd: WP execution complete)
- [ ] Contribute 1 example vào skill `references/examples.md`
- [ ] Tự lập checklist quality bar cá nhân

**Sau 1 tháng:** đủ độc lập vận hành 1 dự án ổn định. 3 tháng: handle multi-project.

---

## 11. Anti-patterns vận hành (khác setup anti-patterns)

### 11.1 "AI tự pipeline qua decision gate"

❌ "Để AI chạy thẳng từ feasibility → tech-solution-design → implementation-planning, tiết kiệm 1 tuần stakeholder."

→ Stakeholder approval gate G1 BẮT BUỘC. Skip = decision không có ownership, sau hối hận không kịp.

### 11.2 "Edit doc lớn thủ công thay vì re-run skill"

❌ "Sửa 50% SRS bằng tay nhanh hơn re-run skill."

→ Edit lớn thủ công phá quality skeleton (citation, format, traceability). Re-run skill mất 1 giờ AI work + giữ skeleton. Manual edit lớn 4 giờ + thường lỗi.

### 11.3 "Bỏ qua _archive/, ghi đè trực tiếp"

❌ "Thư mục _archive/ tốn dung lượng, xóa cho gọn."

→ Mất khả năng diff lịch sử. Mất khả năng audit "tại sao thay đổi". Git log không đủ — _archive/ giữ snapshot có context.

### 11.4 "Không update PROGRESS.md"

❌ "PROGRESS.md là chi tiết vụn vặt, ai cần đọc."

→ Stakeholder + auditor + người mới đọc đầu tiên. Không update = vô hình hóa tiến độ. Daily update tốn 2 phút.

### 11.5 "Gộp role: 1 AI làm orchestrator + executor + reviewer"

❌ "1 AI làm hết cho gọn."

→ Reviewer cần fresh eyes. Cùng AI vừa làm vừa review = tự chấm bài. Tách session.

### 11.6 "Skip post-incident review"

❌ "Sự cố fix rồi, làm gì còn review."

→ Lần sau lại sự cố tương tự. Runbook không cập nhật. Lessons không học. Bắt buộc 48h sau là đã có post-incident review trong runbook.

### 11.7 "Re-run skill không archive bản cũ"

❌ "Bản cũ sai mà, archive làm gì."

→ Reviewer cần diff. Skill bug có thể khiến bản mới còn tệ hơn — cần rollback. Always archive.

### 11.7 "Stakeholder approve verbally, không document"

❌ "Sếp gật đầu trong cuộc họp là đủ."

→ 6 tháng sau không ai nhớ. Bắt buộc: ký commit / email / meeting minutes ghi rõ "approve scenario X". Lưu vào `_sources/` hoặc ADR.

### 11.8 "Không chạy documentation-sync vì 'docs đang đúng'"

❌ "Tôi biết docs ổn, không cần audit."

→ Drift sneaky. 6 tháng tích lũy = 1 tháng khắc phục. Hàng tháng = 30 phút/tháng. Discipline.

---

## 12. Tooling khuyến nghị

### 12.1 IDE / AI client

| Tool | Vai trò | Note |
|------|---------|------|
| **Claude Code** | AI agent vận hành skills | Khuyến nghị chính — auto-detect Skill format |
| **Cursor / VSCode + Copilot** | Edit thủ công + AI assist | OK nếu đã quen, copy SKILL.md content vào prompt |
| **Notion / Confluence** | Stakeholder reading | Export markdown từ docs/ vào, không edit ngược |
| **Linear / Jira** | Issue tracking | Link mỗi WP-ID, FEAT-ID, INC-ID vào ticket |
| **Slack / Teams** | Real-time comms | Channel #project-<name> + #project-<name>-incidents |

### 12.2 Folder mounting

Có 2 cách mount `company-skills/` vào project:

**Option A — Submodule (khuyến nghị cho nhiều dự án):**
```bash
git submodule add <skills-repo-url> company-skills
git submodule update --init
```

**Option B — Symlink (1 dự án, dev local):**
```bash
ln -s /path/to/central/company-skills company-skills
```

**Option C — Copy (audit isolation):**
```bash
cp -r /central/company-skills ./company-skills
# pin version, không update auto
```

Submodule = update controlled. Symlink = always latest. Copy = frozen.

### 12.3 CI / automation

```yaml
# .github/workflows/doc-quality.yml — pseudocode
on:
  pull_request:
    paths: ['docs/**']
jobs:
  doc-sync-check:
    - run: claude run skill documentation-sync --scope=changed-files-only
    - if: drift_found, comment on PR
```

```yaml
# Schedule monthly full sync
on:
  schedule:
    - cron: '0 9 1 * *'  # 1st of month
jobs:
  full-sync:
    - run: claude run skill documentation-sync --scope=full
    - run: claude run skill document-consistency-review --scope=full
    - notify: slack #project-name with report link
```

---

## 13. FAQ vận hành

### Q1: Operator nghỉ phép, ai backup?

Mỗi project nên có ≥2 operators (chính + phụ). Cross-train trong tháng đầu. Khi nghỉ:
- PROGRESS.md là single source of truth → ai đọc cũng tiếp tục được
- Đừng để session AI dài-hạn không-checkpoint giữa người này → người khác

### Q2: Stakeholder không có thời gian review CONTEXT_PACK?

Cấp tóm tắt 1 trang (Section 1 Executive Summary của pack). Yêu cầu họ review 3 thứ:
1. Top 3 stakeholder priorities — đúng không?
2. Top contradictions — họ resolve được không?
3. Open Questions blocking — họ trả lời được không?

10 phút thay vì 1 giờ. Nếu họ vẫn không có 10 phút → eskalate (không có quyết định = blocker).

### Q3: AI agent generate output sai cấu trúc, không match template?

3 nguyên nhân:
1. Input thiếu (CONTEXT_PACK chưa có) → cung cấp đủ input rồi rerun
2. Mode chọn sai (A/B/C) → confirm với operator
3. Skill version cũ → check skill commit, update nếu cần

Nếu 3 cái trên đều fix mà vẫn sai → log issue, có thể skill bug.

### Q4: Project đã chạy 6 tháng, docs lệch khá nhiều, refresh ra sao?

Quy trình refresh batch:
1. Snapshot hiện tại: tag git + copy `docs/` → `docs.snapshot.<date>/`
2. Chạy `document-consistency-review` → list inconsistencies
3. Chạy `documentation-sync` → list code-vs-doc drift
4. Re-run skills theo cascade order (CONTEXT_PACK → BUSINESS_CONTEXT → SRS → ...)
5. Diff bản mới với snapshot — preserve manual edits còn relevant
6. Stakeholder review delta
7. Replace docs/ với bản refresh
8. Archive snapshot

Effort: 1-2 tuần cho 1 project active 6 tháng.

### Q5: 2 dự án dùng skill khác phiên bản — ổn không?

Ổn nếu mỗi project pin version. Vấn đề khi:
- Compare cross-project (output format khác)
- Skill maintainer fix bug ở v2 mà v1 vẫn có

Khuyến nghị: 1 lần/quý, upgrade tất cả project sang skill version mới nhất, chấp nhận 1 lần migration cost.

### Q6: AI execute task xong tự commit?

KHÔNG khuyến nghị mặc định. AI propose changes → operator review → operator commit. Reasons:
- Audit trail rõ
- Operator ownership
- Tránh "AI committed and now I can't undo without context"

Có thể bật auto-commit cho tier-1 boilerplate task (`scaffolder` AI) sau khi confidence cao.

### Q7: Có skill nào bắt buộc chạy không bỏ được?

Phụ thuộc dự án, nhưng theo kinh nghiệm:

| Skill | Bắt buộc? | Lý do |
|-------|-----------|-------|
| `project-context-ingestion` | Khuyên rất mạnh | Không có = SRS sai chiều |
| `srs-*-author/reverse` | Bắt buộc cho audit/compliance | Audit-grade doc |
| `feasibility-assessment` | Bắt buộc trước commitment >$100K | Stakeholder accountability |
| `tech-solution-design` | Bắt buộc nếu kiến trúc non-trivial | ADR archaeology |
| `incident-response-playbook` | Bắt buộc trước go-live production | On-call survival |
| `documentation-sync` | Khuyên định kỳ | Drift prevention |

Phần còn lại optional theo needs.

### Q8: Compliance auditor hỏi "skills có security review không?"

Skills là Markdown — không có code execution, không có credential, không có network. Security risk = nội dung doc bị giả mạo (Git supply chain attack). Mitigation:
- Skills lưu trong repo có protected branch + signed commits
- Skill maintainer = vai trò Tech Lead, ký mỗi PR
- Audit log mọi commit vào company-skills/

---

## 14. Tổng kết

Khi đã có cả skills + docs:

- **Người** có conventions rõ ràng cho mọi role + cadence
- **AI** có protocol prompt, handoff, escalation
- **Doc** có lifecycle 6 trạng thái, không ai bị "doc orphan"
- **Quality** được enforce qua gates per skill, per phase, per deploy
- **Knowledge** persist trong skills + ADR + runbook → không phụ thuộc cá nhân
- **Cải tiến** lan tỏa: skill v2 → 60 project nâng theo

**Câu hỏi cuối cùng để verify mỗi tuần:**

> Nếu mai operator chính nghỉ 1 tháng, operator phụ có thể tiếp tục dự án ổn định không?

Nếu **có** → vận hành đúng.
Nếu **không** → có gap (PROGRESS không updated? Decision verbal? Knowledge trong đầu?). Fix gap đó.

---

*Vận hành tốt = quy trình vô hình khi mọi thứ ổn, hiển hiện ngay khi có vấn đề. Skills + docs làm được điều này nếu — và chỉ nếu — mọi người tuân thủ conventions.*
