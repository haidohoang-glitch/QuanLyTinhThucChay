# Bộ Skills Công ty — Hệ Phương pháp Tài liệu hóa

> **Mục đích:** Bộ skills tái sử dụng được, sản xuất tài liệu chuẩn cho mọi codebase. Mỗi skill ghi lại một **phương pháp** (cách làm), KHÔNG phải nội dung dự án. Output là bộ tài liệu cụ thể của từng project, theo định dạng chuẩn công ty.
>
> **Đối tượng:** AI agent thực thi nhiệm vụ tài liệu hóa; tech lead giám sát; engineering manager thiết lập chuẩn mực.
>
> **🇻🇳 Tài liệu tiếng Việt (đọc theo mục đích):**
> - [GETTING_STARTED.md](GETTING_STARTED.md) — overview + cách dùng (đọc trước, 5-15 phút)
> - [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) — workflow chi tiết Pre-Phase 0 → Phase 4
> - [OPERATIONS_MANUAL.md](OPERATIONS_MANUAL.md) — cẩm nang vận hành hằng ngày cho người + AI agents
> - [VALUE_COMPARISON.md](VALUE_COMPARISON.md) — so sánh giá trị: bộ skills vs chỉ có `docs/`
>
> **Hướng dẫn từng phase** (mở thư mục phase tương ứng):
> - [00_REQUIREMENTS/PHASE_GUIDE.md](00_REQUIREMENTS/PHASE_GUIDE.md) — Phase 0
> - [01_DISCOVERY/PHASE_GUIDE.md](01_DISCOVERY/PHASE_GUIDE.md) — Phase 1
> - [02_STRATEGIC/PHASE_GUIDE.md](02_STRATEGIC/PHASE_GUIDE.md) — Phase 2 (có CỔNG CỨNG)
> - [03_EXECUTION/PHASE_GUIDE.md](03_EXECUTION/PHASE_GUIDE.md) — Phase 3
> - [04_MAINTENANCE/PHASE_GUIDE.md](04_MAINTENANCE/PHASE_GUIDE.md) — Phase 4

---

## Bộ skills này giải quyết vấn đề gì

**Khi không chuẩn hóa:**
- Mỗi dự án có format docs khác nhau → chi phí onboarding cho mỗi dự án
- AI agent không thể sản xuất output có thể so sánh được → tri thức tribal vẫn ở dạng tribal
- Audit/handover phải làm bespoke mỗi lần

**Với bộ skills này:**
- Bất kỳ AI agent + bất kỳ codebase → output chuẩn theo format công ty
- Cấu trúc output cố định; nội dung thích nghi với từng domain
- Phương pháp được capture 1 lần, áp dụng 60+ lần

---

## Cấu trúc thư mục

Cấu trúc skills mirror cấu trúc phase của `docs/` để nhất quán:

```
company-skills/
├── INDEX.md                              (file này)
├── GETTING_STARTED.md, WORKFLOW_GUIDE.md, OPERATIONS_MANUAL.md, VALUE_COMPARISON.md (hướng dẫn tiếng Việt)
├── 00_REQUIREMENTS/                      (Phase 0 — sinh ra docs/00_REQUIREMENTS/)
│   ├── PHASE_GUIDE.md                    (hướng dẫn phase tiếng Việt)
│   ├── phase-0-orchestrator/             (★ orchestrator — chạy cả cụm tuần tự)
│   ├── project-context-ingestion/        (upstream của SRS — raw → CONTEXT_PACK.md)
│   ├── srs-greenfield-author/
│   ├── srs-reverse-engineer/
│   ├── nfr-specification/
│   └── requirements-traceability/
├── 01_DISCOVERY/                         (Phase 1 — sinh ra docs/01_DISCOVERY/)
│   ├── PHASE_GUIDE.md
│   ├── phase-1-orchestrator/             (★ orchestrator)
│   ├── codebase-discovery/
│   ├── data-architecture-audit/
│   ├── tech-debt-audit/
│   └── business-context-capture/
├── 02_STRATEGIC/                         (Phase 2 — sinh ra docs/02_STRATEGIC/)
│   ├── PHASE_GUIDE.md
│   ├── phase-2-orchestrator/             (★ orchestrator — có cổng cứng G1+G2)
│   ├── feasibility-assessment/
│   ├── tech-solution-design/
│   └── implementation-planning/
├── 03_EXECUTION/                         (Phase 3 — sinh ra docs/03_EXECUTION/)
│   ├── PHASE_GUIDE.md
│   ├── phase-3-orchestrator/             (★ orchestrator — bimodal: setup + WP loop)
│   ├── work-package-decomposer/
│   ├── ai-operator-protocol/
│   └── multi-tier-ai-routing/
├── 04_MAINTENANCE/                       (Phase 4 — sinh ra docs/04_MAINTENANCE/)
│   ├── PHASE_GUIDE.md
│   ├── phase-4-orchestrator/             (★ orchestrator — ongoing 4 modes)
│   ├── incident-response-playbook/
│   ├── feature-extension-planning/
│   └── documentation-sync/
└── cross-cutting/                        (skills tiện ích xuyên phase)
    ├── document-index-master/
    └── document-consistency-review/
```

---

## Tổng quan — 19 component skills + 5 phase orchestrators (v1) ✅

| Phase | Skill | Output (trong `docs/` của project đích) | Trạng thái |
|-------|-------|-------------------------------------------|-------------|
| **0 — Requirements** | ★ [`phase-0-requirements-orchestrator`](00_REQUIREMENTS/phase-0-orchestrator/) | Coordinate Step 1-4 → pipeline `00_REQUIREMENTS/` đầy đủ | ✅ v1 |
| | [`project-context-ingestion`](00_REQUIREMENTS/project-context-ingestion/) | `00_REQUIREMENTS/CONTEXT_PACK.md` + `_sources/` (upstream của SRS) | ✅ v1 |
| | [`srs-greenfield-author`](00_REQUIREMENTS/srs-greenfield-author/) | `00_REQUIREMENTS/SRS_VI/M1-M10` (greenfield) | ✅ v1 |
| | [`srs-reverse-engineer`](00_REQUIREMENTS/srs-reverse-engineer/) | `00_REQUIREMENTS/SRS_VI/M1-M10` (từ code đã có) | ✅ v1 |
| | [`nfr-specification`](00_REQUIREMENTS/nfr-specification/) | `00_REQUIREMENTS/SRS_VI/M9_*` | ✅ v1 |
| | [`requirements-traceability`](00_REQUIREMENTS/requirements-traceability/) | `00_REQUIREMENTS/SRS_VI/M10_*` | ✅ v1 |
| **1 — Discovery** | ★ [`phase-1-discovery-orchestrator`](01_DISCOVERY/phase-1-orchestrator/) | Coordinate 4 skills discovery (sequential hoặc parallel) | ✅ v1 |
| | [`codebase-discovery`](01_DISCOVERY/codebase-discovery/) | `01_DISCOVERY/CODEBASE_MAP.md` | ✅ v1 |
| | [`data-architecture-audit`](01_DISCOVERY/data-architecture-audit/) | `01_DISCOVERY/DATA_ARCHITECTURE.md` | ✅ v1 |
| | [`tech-debt-audit`](01_DISCOVERY/tech-debt-audit/) | `01_DISCOVERY/TECH_DEBT_AUDIT.md` | ✅ v1 |
| | [`business-context-capture`](01_DISCOVERY/business-context-capture/) | `01_DISCOVERY/BUSINESS_CONTEXT.md` | ✅ v1 |
| **2 — Strategic** | ★ [`phase-2-strategic-orchestrator`](02_STRATEGIC/phase-2-orchestrator/) | Coordinate với CỔNG CỨNG G1 (stakeholder) + G2 (tech lead) | ✅ v1 |
| | [`feasibility-assessment`](02_STRATEGIC/feasibility-assessment/) | `02_STRATEGIC/FEASIBILITY_ASSESSMENT.md` | ✅ v1 |
| | [`tech-solution-design`](02_STRATEGIC/tech-solution-design/) | `02_STRATEGIC/TECH_SOLUTION_DESIGN.md` | ✅ v1 |
| | [`implementation-planning`](02_STRATEGIC/implementation-planning/) | `02_STRATEGIC/MASTER_PLAN.md` + `03_EXECUTION/work-packages/PHASE_*.md` | ✅ v1 |
| **3 — Execution** | ★ [`phase-3-execution-orchestrator`](03_EXECUTION/phase-3-orchestrator/) | Bimodal: Sub-A setup (one-time) + Sub-B WP loop (per WP) | ✅ v1 |
| | [`work-package-decomposer`](03_EXECUTION/work-package-decomposer/) | Decompose WP → micro-tasks (per WP) | ✅ v1 |
| | [`ai-operator-protocol`](03_EXECUTION/ai-operator-protocol/) | `03_EXECUTION/AI_OPERATOR_GUIDE.md` | ✅ v1 |
| | [`multi-tier-ai-routing`](03_EXECUTION/multi-tier-ai-routing/) | `03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md` | ✅ v1 |
| **4 — Maintenance** | ★ [`phase-4-maintenance-orchestrator`](04_MAINTENANCE/phase-4-orchestrator/) | 4 modes: Setup / Triggered / Scheduled / Audit prep | ✅ v1 |
| | [`incident-response-playbook`](04_MAINTENANCE/incident-response-playbook/) | `04_MAINTENANCE/runbooks/INCIDENT_*.md` | ✅ v1 |
| | [`feature-extension-planning`](04_MAINTENANCE/feature-extension-planning/) | `04_MAINTENANCE/feature-extensions/FEAT_*.md` | ✅ v1 |
| | [`documentation-sync`](04_MAINTENANCE/documentation-sync/) | `04_MAINTENANCE/DOC_SYNC_REPORT.md` | ✅ v1 |
| **Cross-cutting** | [`document-index-master`](cross-cutting/document-index-master/) | `INDEX.md` (master nav của project đích) | ✅ v1 |
| | [`document-consistency-review`](cross-cutting/document-consistency-review/) | `04_MAINTENANCE/CONSISTENCY_REVIEW_REPORT.md` | ✅ v1 |

---

## Cấu trúc chuẩn của 1 skill

Mỗi skill (component) trong bộ này theo cấu trúc:

```
<phase>/<skill-name>/
├── SKILL.md                    Frontmatter (name + description) + quy trình
├── assets/
│   └── <OUTPUT>_template.md    Bộ skeleton Markdown với {{PLACEHOLDER}}
└── references/
    ├── checklist.md            Quality gate output phải pass
    ├── adaptation.md           Biến thể theo loại dự án / ngữ cảnh
    └── examples.md             Ví dụ thực tế (đã ẩn danh)
```

Orchestrator có cấu trúc gọn hơn (3 file):

```
<phase>/phase-N-orchestrator/
├── SKILL.md                    Logic orchestration + checkpoints + error recovery
└── references/
    ├── checklist.md            Quality gates orchestrator-level
    └── runbook.md              Worked examples + troubleshooting
```

**Nhất quán này nghĩa là:**
- AI agent học pattern 1 lần, áp dụng cho mọi skill
- Operator biết tìm thông tin ở đâu (cần checklist? → `references/checklist.md`)
- Thêm skill mới = điền vào cùng cấu trúc

---

## Pattern chung: 3-Mode Classification

Mọi skill có 1 step chọn taxonomy phân loại. 3 modes:

| Mode | Khi nào dùng |
|------|---------------|
| **A — Standard taxonomy** *(mặc định)* | Không có chỉ dẫn đặc biệt; codebase chưa khai báo cấu trúc |
| **B — Honor existing classification** | Codebase có doc kiến trúc/domain khai báo model riêng |
| **C — User-defined classification** | Người dùng cung cấp taxonomy custom trong yêu cầu |

**Logic chọn mode (nhất quán giữa các skill):**
1. User chỉ định rõ → dùng cái đó
2. User cung cấp taxonomy custom → Mode C
3. Codebase có doc classification rõ → **HỎI** user (Mode A hay B?), KHÔNG tự chọn
4. Mặc định → Mode A

Step 2 trong mỗi `SKILL.md` ghi rõ các modes đặc thù của skill đó.

---

## Pattern chung: Scope Discipline (kỷ luật phạm vi)

Mỗi skill **descriptive trong scope của mình**, KHÔNG prescriptive sang scope khác.

| Skill | Sản xuất | KHÔNG sản xuất |
|-------|----------|------------------|
| `codebase-discovery` | Cấu trúc kỹ thuật (HIỆN TẠI) | Giải thích nghiệp vụ, đề xuất fix, plan |
| `data-architecture-audit` | Trạng thái lớp dữ liệu + rủi ro | Lỗi code quality, fix, plan |
| `tech-debt-audit` | Findings + severity | Thiết kế fix, kế hoạch implementation |
| `business-context-capture` | View nghiệp vụ (sản phẩm LÀM gì) | Cấu trúc code, thay đổi kỹ thuật |
| `feasibility-assessment` | Business case cho công việc đề xuất | Solution design, kế hoạch thực thi |
| `tech-solution-design` | Kiến trúc đã chọn + ADRs | Kế hoạch thực thi; chi tiết per-WP |
| `implementation-planning` | Decompose Phase + WP | Solution design, business case |
| `work-package-decomposer` | Task list per-WP (đã phân tier) | Author WP; chính sách tier |
| `ai-operator-protocol` | Quy tắc giám sát | Chính sách tier; thực thi WP cụ thể |
| `multi-tier-ai-routing` | Chính sách tier AI | Áp dụng per-WP |
| `srs-*-author` | SRS chính thức (M1-M10) | Solution design; implementation |
| `nfr-specification` | NFRs (M9 của SRS) | FRs; design |
| `requirements-traceability` | RTM (M10 của SRS) | Author requirements; tạo test mới |
| `incident-response-playbook` | Runbook per-incident | Runbook ops thường; feature work |
| `feature-extension-planning` | Spec single-feature | Redesign hệ thống |
| `documentation-sync` | Detection drift code-vs-doc | Consistency doc-vs-doc |
| `document-index-master` | Master nav INDEX | Detection issues |
| `document-consistency-review` | Consistency doc-vs-doc | Drift code-vs-doc |
| `phase-N-orchestrator` | Coordinate component skills + checkpoints | Tự sinh nội dung output (delegate cho component) |

Nếu output của skill drift sang scope của skill khác, output đã sai. Mỗi `references/checklist.md` enforce qua Gate 4 (Scope discipline).

---

## Cách dùng 1 skill

### Là AI agent

Skills tự load bởi Claude Code khi `description` match intent của user. Dùng skill end-to-end như viết. Đừng skip step.

### Là operator

1. Xác định skill nào áp dụng (từ bảng trên hoặc từ PHASE_GUIDE)
2. Cung cấp AI agent quyền truy cập codebase + inputs liên quan
3. Chỉ định mode preference nếu có (nếu không, AI mặc định Mode A hoặc hỏi)
4. Review output dựa trên `references/checklist.md` của skill
5. Nếu output fail 1 gate → yêu cầu AI sửa (đừng accept output thiếu)

### Là tech lead thiết lập chuẩn

1. Đọc `examples.md` của mỗi skill để calibrate quality kỳ vọng
2. Quyết định có muốn adjust template cho field công ty không
3. Pin version trong dự án (đây là v1; phiên bản tương lai có thể đổi)
4. Đào tạo operator về Mode selection logic

---

## Thứ tự dependency — Khi áp skills cho 1 codebase mới

### Dự án greenfield (chưa có code)

```
project-context-ingestion ──> srs-greenfield-author ──> nfr-specification ──> requirements-traceability
                                                                                    ↑
                                                            (RTM populated khi code được build)

(Skills Phase 1 Discovery KHÔNG áp dụng cho đến khi có code.)
```

### Dự án legacy / có code sẵn

```
project-context-ingestion ──┐
                            │
codebase-discovery       ──┐│
data-architecture-audit  ──┤│
tech-debt-audit          ──┤├── inputs cho ──> srs-reverse-engineer ──> nfr-specification ──> requirements-traceability
business-context-capture ──┘│                                                                          │
                            │                                                                          ▼
                            └────────── inputs cho ──> feasibility-assessment ──> tech-solution-design ──> implementation-planning
                                                                                                                       │
                                                                                                                       ▼
                                                              work-package-decomposer + ai-operator-protocol + multi-tier-ai-routing
                                                                                                                       │
                                                                                                                       ▼
                                                                                                                  (execution)
                                                                                                                       │
                                                                                                                       ▼ (sau go-live)
                                                              incident-response-playbook + feature-extension-planning + documentation-sync
```

### Cross-cutting (chạy bất cứ lúc nào, thường sau khi có Phase 0 docs)

- `document-index-master` — sinh / refresh INDEX.md
- `document-consistency-review` — audit cross-doc hàng quý

### Dependencies chính

| Skill | Yêu cầu (phải chạy trước) | Inputs optional |
|-------|----------------------------|------------------|
| `project-context-ingestion` | (raw materials) | — |
| `srs-greenfield-author` | (stakeholder inputs); CONTEXT_PACK khuyên rất mạnh | Template SRS công ty nếu Mode B |
| `srs-reverse-engineer` | `business-context-capture`, `codebase-discovery`; CONTEXT_PACK khuyên mạnh | `data-architecture-audit`, `tech-debt-audit` |
| `nfr-specification` | SRS exists (M1-M2 + M3-Mx) | `data-architecture-audit`, `tech-debt-audit` cho baseline hiện tại |
| `requirements-traceability` | SRS exists (M1-M9) | Implementation + tests cho RTM non-trivial |
| `codebase-discovery` | (truy cập codebase) | — |
| `data-architecture-audit` | (truy cập codebase) | `codebase-discovery` |
| `tech-debt-audit` | (truy cập codebase) | `codebase-discovery` |
| `business-context-capture` | (truy cập codebase + UI) | `codebase-discovery`, `CONTEXT_PACK` |
| `feasibility-assessment` | Phase 1 outputs (hoặc stakeholder context) | `tech-debt-audit`, `data-architecture-audit`, `CONTEXT_PACK` |
| `tech-solution-design` | Phase 1 outputs + SRS (hoặc `feasibility-assessment`) | All Phase 1 |
| `implementation-planning` | `tech-solution-design` (hoặc solution context) | `feasibility-assessment` |
| `work-package-decomposer` | WP cụ thể từ `implementation-planning` | Chính sách `multi-tier-ai-routing` |
| `ai-operator-protocol` | Project context + setup team | `multi-tier-ai-routing` |
| `multi-tier-ai-routing` | (AI tools available + budget) | — |
| `incident-response-playbook` | Live system + observability tooling | Phase 1 outputs |
| `feature-extension-planning` | Live system + Phase 0/1/2 docs | — |
| `documentation-sync` | All docs để check | — |
| `document-index-master` | Filesystem inventory của `docs/` | — |
| `document-consistency-review` | All docs để check | `document-index-master` cho nav |
| `phase-N-orchestrator` | Output của các phase trước (nếu N>0) | Component skills của phase N |

---

## Khuyến nghị LLM Agents — Chất lượng vs Chi phí

> **Bối cảnh:** Mỗi skill có thể chạy với LLM khác nhau. Lựa chọn sai = output kém HOẶC chi phí cao gấp 8-25 lần. Section này map skills → LLM phù hợp.
>
> **Lưu ý:** Skill `multi-tier-ai-routing` ở Phase 3 sản xuất chính sách **per-project** chi tiết hơn. Section này là **default recommendations** ở cấp suite — project có thể tune theo nhu cầu.

### Triết lý 4-tier (đã dùng nhất quán)

| Tier | Mục đích | % task target | Cost ratio |
|------|----------|----------------|------------|
| **T3 Strong** | Architecture, judgment-heavy, regulatory citation, complex reasoning | 5-15% | 25× |
| **T2 Mid** | Logic implementation, code reading, structured extraction | 20-30% | 5× |
| **T1 Simple** | Boilerplate, scaffolding, format check, simple lookup | 60-70% | 1× |
| **Human** | ADR approval, billing/auth/legal decisions, prod deploy | <5% | (operator time) |

### Models khuyến nghị per tier (state of the art ~đầu 2026)

| Tier | Primary recommendation | Alternative | Budget option |
|------|-------------------------|-------------|----------------|
| **T3 Strong** | **Claude Opus 4.7** (excellent at long-context structured output + ADR-style reasoning) | GPT-5 / OpenAI o-series (reasoning-tuned cho strategic decisions) | Gemini 2.x Pro (200K+ context cho codebase lớn) |
| **T2 Mid** | **Claude Sonnet 4.6** (best balance code-reading + instruction following) | GPT-5 mini, Gemini 2.x Pro | DeepSeek-V3 (open weights, ~10× rẻ hơn Sonnet) |
| **T1 Simple** | **Claude Haiku 4.5** (fast, cheap, đủ cho boilerplate) | GPT-5 nano, Gemini 2.x Flash | DeepSeek-V3, Qwen-3 |
| **Human** | (n/a) | (n/a) | (n/a) |

### Tiêu chí so sánh theo workload

| Tiêu chí | Claude (Opus/Sonnet/Haiku) | GPT-5 family | Gemini 2.x | DeepSeek/Qwen (open) |
|----------|----------------------------|--------------|-------------|----------------------|
| **Instruction following** (theo skill template chặt chẽ) | ★★★★★ | ★★★★ | ★★★★ | ★★★ |
| **Long context** (codebase 100K+ LOC, transcripts dài) | ★★★★ (200K) | ★★★★ (huge) | ★★★★★ (1M+) | ★★★ (128K) |
| **Reasoning** (Phase 2 strategy, ADR alternatives) | ★★★★★ (Opus) | ★★★★★ (o-series) | ★★★★ | ★★★ |
| **Structured output** (Markdown templates với citations) | ★★★★★ | ★★★★ | ★★★★ | ★★★ |
| **Code reading** (Phase 1 discovery) | ★★★★★ | ★★★★ | ★★★★ | ★★★★ (Qwen-Coder rất khá) |
| **Cost** | $$ - $$$ | $ - $$$ | $ - $$ | ¢ |
| **Privacy/On-prem** | API only | API only | API only | ★★★★★ (self-host) |

### Per-phase recommendations (ưu tiên chất lượng cho audit-grade output)

#### Phase 0 — Requirements

| Skill | Tier khuyến nghị | Primary | Lý do |
|-------|--------------------|---------|-------|
| `project-context-ingestion` | T3 | **Claude Opus 4.7** | Long transcripts + nuance extraction + cross-source contradictions |
| `srs-greenfield-author` | T3 | **Claude Opus 4.7** | Audit-grade IEEE 830 — sai 1 FR là rework lớn |
| `srs-reverse-engineer` | T3 | **Claude Opus 4.7** | Cần đọc code + cross-reference với CONTEXT_PACK |
| `nfr-specification` | T2 | **Claude Sonnet 4.6** | Format chuẩn + cite regulatory; structured |
| `requirements-traceability` | T2 | **Claude Sonnet 4.6** | Bảng matrix structured, ít judgment |

**Budget config Phase 0:** Pre-ingestion + SRS dùng Sonnet 4.6 thay Opus → giảm ~80% cost, chấp nhận drop quality khoảng 10-15% (operator review nhiều hơn).

**Tránh:** GPT-5 nano hoặc Haiku 4.5 cho SRS — output thiếu nuance, sót requirement.

#### Phase 1 — Discovery (chỉ legacy)

| Skill | Tier | Primary | Lý do |
|-------|------|---------|-------|
| `codebase-discovery` | T2 | **Claude Sonnet 4.6** hoặc **Gemini 2.x Pro** | Long context cho codebase lớn; Gemini 1M context win cho monorepo khổng lồ |
| `data-architecture-audit` | T2 | **Claude Sonnet 4.6** | Schema + governance cần precision |
| `business-context-capture` | T3 | **Claude Opus 4.7** | Domain extraction từ code rất nuanced; invariants đặc biệt khó |
| `tech-debt-audit` | T2-T3 | **Claude Sonnet 4.6** (T2) hoặc **Opus 4.7** (T3) | Severity calibration cần judgment; Opus tốt hơn nhưng Sonnet đủ cho most cases |

**Budget config Phase 1:** Toàn bộ Sonnet 4.6 → ~$25-40 cho dự án ~80K LOC.

**Long context win:** Codebase >300K LOC monorepo → **Gemini 2.x Pro** (1M+ context) đọc được toàn repo trong 1 pass thay vì sample.

#### Phase 2 — Strategic (highest stakes)

| Skill | Tier | Primary | Lý do |
|-------|------|---------|-------|
| `feasibility-assessment` | T3 | **Claude Opus 4.7** hoặc **GPT-5 / o-series** | Scenario analysis + ROI math + risk reasoning. Sai = stakeholder approve nhầm. |
| `tech-solution-design` | T3 | **Claude Opus 4.7** | ADRs cần cân nhắc alternatives; structured decision rationale |
| `implementation-planning` | T2-T3 | **Claude Opus 4.7** (recommended) hoặc Sonnet 4.6 | Critical path + WP decomposition cần judgment |

**KHÔNG xuống tier ở Phase 2.** Tiết kiệm vài $ → mất hàng tháng rework. Phase 2 chỉ ~$50-80 dù dùng Opus full — rất rẻ so với decision impact.

**Reasoning option:** Cho `feasibility-assessment` với scenarios phức tạp (3+ chiều: cost/timeline/risk/regulatory), **GPT-5 reasoning** hoặc **OpenAI o-series** đôi khi cho output sắc bén hơn Opus về chain-of-thought.

#### Phase 3 — Execution (multi-tier aggressive)

| Skill | Tier | Primary | Lý do |
|-------|------|---------|-------|
| `ai-operator-protocol` | T3 | **Claude Opus 4.7** | Hard rules + escalation logic — cần precision |
| `multi-tier-ai-routing` | T3 | **Claude Opus 4.7** | Cost projection + tier mapping policy |
| `work-package-decomposer` | T3 | **Claude Opus 4.7** | Mỗi WP decompose 1 lần, chất lượng quan trọng cho cost saving downstream |

**Per-task execution (output thực tế):**

| Task type | Tier | Primary | Cost saving |
|-----------|------|---------|-------------|
| Boilerplate, scaffolding, format | T1 | **Haiku 4.5** | 25× rẻ hơn Opus |
| CRUD logic, refactor, simple feature | T2 | **Sonnet 4.6** | 5× rẻ hơn Opus |
| Architecture-altering, security-critical, complex algo | T3 | **Opus 4.7** | (full cost) |
| Boilerplate volume cao (>100 task/WP) | T1 budget | **DeepSeek-V3** | ~3× rẻ hơn Haiku |

**Tổng Phase 3 (~18 WPs medium project):** ~$25-40 với multi-tier mix vs ~$200-300 nếu all-Opus = **~88% saving**.

#### Phase 4 — Maintenance

| Skill | Tier | Primary | Lý do |
|-------|------|---------|-------|
| `incident-response-playbook` (preparation) | T2 | **Claude Sonnet 4.6** | Runbook structured; precision matters cho 2h sáng on-call |
| `incident-response-playbook` (post-incident review) | T3 | **Claude Opus 4.7** | Lessons learned cần insight |
| `feature-extension-planning` | T2 | **Claude Sonnet 4.6** | Mini-spec, không quá phức tạp |
| `documentation-sync` | T1-T2 | **Haiku 4.5** (T1) hoặc Sonnet (T2) | Pattern matching code-vs-doc; T1 đủ cho most |
| `document-consistency-review` | T2 | **Claude Sonnet 4.6** | Cross-doc analysis |
| `document-index-master` | T1 | **Haiku 4.5** | Filesystem nav, format-heavy |

**Budget config Phase 4 cho 1 năm:**
- Monthly doc-sync (12×): Haiku 4.5 → ~$3/tháng × 12 = ~$36/year
- Quarterly consistency (4×): Sonnet 4.6 → ~$10/quarter × 4 = ~$40/year
- Per-feature (~10/year): Sonnet 4.6 → ~$8 × 10 = ~$80/year
- Per-incident review (~30/year): Sonnet 4.6 → ~$3 × 30 = ~$90/year
- **Tổng/year cho project trung bình: ~$250-400** — rất rẻ.

### Cost projection toàn bộ lifecycle (medium project)

| Phase | Duration | Default (Opus-heavy) | Optimized (multi-tier) | Budget (Sonnet-heavy) |
|-------|----------|------------------------|--------------------------|------------------------|
| Pre-P0 | 1 tuần | $20-30 | $15-25 | $8-15 |
| P1 | 2-3 tuần | $40-60 | $25-40 | $15-25 |
| P0 | 1-2 tuần | $30-50 | $20-35 | $12-22 |
| P2 | 1-2 tuần | $50-80 | $50-80 (KHÔNG xuống) | $50-80 |
| P3 setup + 18 WPs | 6-8 tuần | $200-300 (all-Opus) | $25-40 (multi-tier) | $20-30 |
| P4 (per year) | ongoing | $400-600 | $250-400 | $150-250 |
| **Tổng (lifecycle ~6 tháng + năm 1 maintenance)** | | **~$740-1,120** | **~$385-620** | **~$255-422** |

**Khuyến nghị production:** Optimized config (~$385-620 cho năm đầu) — balance chất lượng + cost.

### Decision factors khi chọn vendor

| Factor | Anthropic (Claude) | OpenAI (GPT-5) | Google (Gemini 2.x) | Open (DeepSeek/Qwen) |
|--------|---------------------|------------------|----------------------|------------------------|
| **Default cho audit-grade docs** | ★★★★★ | ★★★★ | ★★★ | ★★ |
| **Codebase 1M+ LOC monorepo** | ★★★ | ★★★★ | ★★★★★ (1M context) | ★★ |
| **Strategic reasoning (Phase 2)** | ★★★★★ (Opus) | ★★★★★ (o-series) | ★★★ | ★★★ |
| **Cost-sensitive Phase 3 boilerplate** | ★★★★ (Haiku) | ★★★★ (nano) | ★★★★★ (Flash) | ★★★★★ |
| **Privacy / on-prem requirement** | ★ | ★ | ★★ (Vertex AI on-prem option) | ★★★★★ |
| **Vendor lock-in risk** | medium | medium | medium | low (open weights) |
| **Vietnamese language quality** | ★★★★ | ★★★★ | ★★★★ | ★★★ |

### Multi-vendor fallback strategy

**Đơn-vendor risk:** Anthropic outage 4 giờ → Phase 3 đứng. Cần fallback.

**Khuyến nghị fallback policy** (document trong `AI_AGENT_TASK_DISTRIBUTION.md`):

| Primary | Fallback 1 | Fallback 2 | Quality drop |
|---------|------------|------------|---------------|
| Claude Opus 4.7 | GPT-5 (reasoning) | Gemini 2.x Pro | ~10-15% |
| Claude Sonnet 4.6 | GPT-5 mini | Gemini 2.x Pro | ~5-10% |
| Claude Haiku 4.5 | GPT-5 nano | Gemini 2.x Flash | ~5% |

**Quy tắc:** Fallback flag commits với note `[fallback: vendor X]`. Khi primary online lại, có thể re-review critical commits.

### Khi NÀO override default

- **Compliance/HIPAA/financial:** Bắt buộc on-prem → DeepSeek/Qwen self-host (chấp nhận quality drop)
- **Codebase 1M+ LOC:** Gemini 2.x Pro thay Claude cho Phase 1 codebase-discovery
- **Reasoning-heavy decisions:** GPT-5 / OpenAI o-series cho `feasibility-assessment` với 5+ scenarios
- **Cost ceiling cứng (<$100 toàn project):** All-Sonnet 4.6 + DeepSeek cho Phase 3 boilerplate
- **Tiếng Việt-only project:** Test Vietnamese output quality từng vendor; Claude và GPT-5 thường tốt nhất

### Anti-patterns

- ❌ **All-Opus mọi skill** — overkill cho boilerplate, đốt cost
- ❌ **All-Haiku/Flash mọi skill** — output kém ở Phase 0/2, sót requirement, audit fail
- ❌ **Free tier cho production** — rate limit + censoring có thể cắt mid-pipeline
- ❌ **Single vendor cho cả 60 project** — vendor outage = catastrophic; có fallback
- ❌ **Pin model version cũ "vì familiar"** — model improvements 6 tháng/lần; review hàng quý

---

## Versioning

Tất cả skills ở **v1**. Lần lặp tương lai sẽ:
- Tinh chỉnh quy trình dựa trên feedback từ usage thực tế
- Thêm skills chuyên biệt khi cần (ví dụ: variants theo ngôn ngữ)
- Có thể tách `references/examples.md` ra thư viện ví dụ riêng nếu phình to
- Cập nhật model list trong `multi-tier-ai-routing` hàng quý (AI landscape thay đổi nhanh)

Version ghi trong INDEX này, KHÔNG ghi trong skill frontmatter (frontmatter format chỉ allow `name` + `description`).

---

## Validation

Cấu trúc mỗi skill được validate bởi `skill-creator/scripts/quick_validate.py`. Để re-validate:

```bash
python skill-creator/scripts/quick_validate.py company-skills/<phase>/<skill-name>

# Ví dụ
python skill-creator/scripts/quick_validate.py company-skills/00_REQUIREMENTS/srs-greenfield-author
python skill-creator/scripts/quick_validate.py company-skills/03_EXECUTION/ai-operator-protocol
python skill-creator/scripts/quick_validate.py company-skills/cross-cutting/document-index-master
```

Để package 1 skill thành `.skill` distributable:

```bash
python skill-creator/scripts/package_skill.py company-skills/<phase>/<skill-name>
```

Validate TẤT CẢ skills cùng lúc:

```bash
for f in company-skills/0[0-4]_*/* company-skills/cross-cutting/*; do
  printf "%-70s " "$f"
  python skill-creator/scripts/quick_validate.py "$f"
done
```

---

## Inventory file (v1)

### Phase 0 — Requirements (5 component skills + 1 orchestrator)

| Skill | Số file |
|-------|---------|
| `phase-0-requirements-orchestrator` | 3 (SKILL + checklist + runbook) |
| `project-context-ingestion` | 5 |
| `srs-greenfield-author` | 9 (SKILL + 5 module template + 3 references) |
| `srs-reverse-engineer` | 9 (chia sẻ template với greenfield-author) |
| `nfr-specification` | 5 |
| `requirements-traceability` | 5 |

### Phase 1 — Discovery (4 component skills + 1 orchestrator)

| Skill | Số file |
|-------|---------|
| `phase-1-discovery-orchestrator` | 3 |
| `codebase-discovery` | 5 |
| `data-architecture-audit` | 5 |
| `tech-debt-audit` | 5 |
| `business-context-capture` | 5 |

### Phase 2 — Strategic (3 component skills + 1 orchestrator)

| Skill | Số file |
|-------|---------|
| `phase-2-strategic-orchestrator` | 3 |
| `feasibility-assessment` | 5 |
| `tech-solution-design` | 5 |
| `implementation-planning` | 7 (3 template: master plan, phase, WP + 3 references) |

### Phase 3 — Execution (3 component skills + 1 orchestrator)

| Skill | Số file |
|-------|---------|
| `phase-3-execution-orchestrator` | 3 |
| `work-package-decomposer` | 5 |
| `ai-operator-protocol` | 5 |
| `multi-tier-ai-routing` | 5 |

### Phase 4 — Maintenance (3 component skills + 1 orchestrator)

| Skill | Số file |
|-------|---------|
| `phase-4-maintenance-orchestrator` | 3 |
| `incident-response-playbook` | 5 |
| `feature-extension-planning` | 5 |
| `documentation-sync` | 5 |

### Cross-cutting (2 skills)

| Skill | Số file |
|-------|---------|
| `document-index-master` | 5 |
| `document-consistency-review` | 5 |

**Tổng:** **25 skills** (19 component + 5 orchestrators + 1 cross-cutting đã tính trong 2), **135 files**, **~26,300 dòng** (gồm cả tài liệu hướng dẫn tiếng Việt).

---

## Mối quan hệ giữa các skills

Nhiều skills tham chiếu lẫn nhau:

| Nếu bạn dùng... | Bạn có thể cũng cần dùng... |
|------------------|--------------------------------|
| `tech-solution-design` | `feasibility-assessment` (trước), `implementation-planning` (sau) |
| `implementation-planning` | `work-package-decomposer` (per WP), `ai-operator-protocol` (lúc execute) |
| `srs-reverse-engineer` | `business-context-capture` + `codebase-discovery` (inputs); CONTEXT_PACK |
| `nfr-specification` | `srs-*-author` (đồng hành để fill M9) |
| `requirements-traceability` | Tất cả Phase 0 skills (inputs); chạy ongoing khi code lands |
| `documentation-sync` + `document-consistency-review` | Cả 2 chạy hàng quý; bổ sung (sync = code↔docs, consistency = doc↔doc) |
| `document-index-master` | Chạy sau `srs-*-author` hoặc sau khi nhiều Phase 0/1 skills sinh docs |
| `phase-N-orchestrator` | Chạy thay cho việc invoke từng component skill thủ công |

---

## Roadmap

- **Đã xong:** Tất cả 5 phase (Phase 0-4) + Cross-cutting + 5 phase orchestrators — 25 skills v1 hoàn tất ✅
- **Liên tục:** Tinh chỉnh skills v1 dựa trên feedback usage
- **Hàng quý:** Update model list + cost figures trong `multi-tier-ai-routing`
- **Khi cần:** Skills chuyên biệt (regulated industries: HIPAA-specific, FDA-specific; variants theo ngôn ngữ)

Để request thay đổi hoặc report issue, update INDEX này với section `## Change requests` trước khi mở PR.

---

## Thống kê bộ skills

- **Coverage:** Toàn bộ 5 phase doc lifecycle + cross-cutting
- **Anonymization:** Tất cả ví dụ dùng project hư cấu (Project Atlas, Helix, Beacon, Mosaic, Voyager, Atrium, Anchor, Pegasus) — không leak FinanceOS
- **Multi-mode:** Mọi component skill hỗ trợ 3-mode classification (Standard / Honor existing / User-defined)
- **Quality gates:** ~10 gates per skill trong `references/checklist.md`
- **Hướng dẫn adaptation:** 7-12 biến thể ngữ cảnh per skill
- **Worked examples:** 1 ví dụ ẩn danh per skill (~200-500 dòng each)
- **Validation:** Tất cả 25 skills pass `skill-creator/scripts/quick_validate.py`
- **Tài liệu hướng dẫn tiếng Việt:** 5 file root + 5 PHASE_GUIDE per phase = 10 docs vận hành

---

*Bộ skills này capture phương pháp luận trước đây tồn tại dưới dạng tribal knowledge. Giờ đây tái sử dụng được trên 60+ dự án.*
