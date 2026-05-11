# Bộ Skills Tài liệu hóa Dự án — Hướng dẫn vận hành

> **Tài liệu này dành cho ai?** Bất kỳ ai chuẩn bị dùng bộ skills này — nhân viên mới, project manager, kỹ sư, hay AI agent. Không cần kinh nghiệm trước với "skills" để đọc.
>
> **Đọc trong 5 phút:** Phần 1-2-3.
> **Đọc kỹ khi sắp vận hành:** thêm Phần 4-5-6.
> **Tra cứu khi gặp tình huống cụ thể:** Phần 7-8.
>
> **Cần chi tiết hơn?** Sau khi đọc file này, mở [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) — hướng dẫn chi tiết từng skill, từng bước, prompt mẫu, hand-off giữa các phase.

---

## 1. Tóm tắt 1 phút

Công ty có 60+ dự án phần mềm. Mỗi dự án có một bộ tài liệu (requirements, kiến trúc, kế hoạch, runbook) — và mỗi dự án viết theo một kiểu khác nhau. Hậu quả:

- Onboarding mỗi dự án tốn ~1-2 tuần đọc tài liệu
- AI không thể tự sinh tài liệu chuẩn vì không có mẫu
- Người chủ chốt rời đi → tri thức mất theo
- Audit / handover làm lại từ đầu mỗi lần

**Bộ skills này là gì:** 19 "công thức" (skills) chuẩn hóa **cách làm tài liệu**, KHÔNG phải nội dung tài liệu. Mỗi skill là một thư mục có 5 file:

```
<skill-name>/
├── SKILL.md                      # Quy trình từng bước
├── assets/<TEMPLATE>.md          # Mẫu output có sẵn placeholder
└── references/
    ├── checklist.md              # Tiêu chí chất lượng
    ├── adaptation.md             # Biến thể theo loại dự án
    └── examples.md               # Ví dụ thực tế (đã ẩn danh)
```

AI agent + bộ skills này + bất kỳ codebase/đầu vào nào → tài liệu chuẩn theo định dạng công ty.

**Lợi ích đo được:**
- Tài liệu giữa 60 dự án **giống nhau về cấu trúc** — đọc dự án mới chỉ cần biết "phần X ở module Y"
- Một AI agent duy nhất có thể vận hành cả 60 dự án (không cần huấn luyện riêng)
- Tri thức methodology lưu trong skills → người đến/đi không ảnh hưởng
- Audit chỉ cần kiểm 1 bộ skills, áp dụng được cho mọi dự án

---

## 2. Vấn đề thực tế mà skills giải quyết

### 2.1 Trước khi có skills

Một tình huống điển hình:

> Dự án A do team Hà Nội làm, có file `requirements.docx` 80 trang.
> Dự án B do team HCM làm, có Notion với 200 page rời rạc.
> Dự án C do nhà thầu ngoài làm, để lại 1 README.md dài 500 dòng.
>
> Khi cần audit cả 3, kiểm toán viên hỏi: "Cho tôi xem requirements". 3 dự án trả lời 3 kiểu. Mỗi dự án mất 3 ngày tìm thông tin tương đương.

Vấn đề không phải các team viết kém — mà là **không có chuẩn**, nên không tận dụng được kết quả của nhau.

### 2.2 Sau khi có skills

> Cùng tình huống. Mỗi dự án chạy `srs-reverse-engineer` skill (nếu đã có code) hoặc `srs-greenfield-author` (nếu chưa). Output cùng format: `docs/00_REQUIREMENTS/SRS_VI/M1_Introduction.md` đến `M10_RTM_Issues_Appendix.md`.
>
> Auditor hỏi cả 3 dự án: "Cho tôi xem M3 Functional Requirements". Cùng 1 vị trí, cùng 1 cấu trúc. 30 phút thay vì 3 ngày.

### 2.3 Skills KHÔNG làm gì

Để tránh kỳ vọng sai:

- ❌ Skills KHÔNG tự viết được nội dung dự án nếu không có nguyên liệu (code, phỏng vấn, tài liệu thô)
- ❌ Skills KHÔNG thay thế việc trao đổi với stakeholders
- ❌ Skills KHÔNG quyết định kiến trúc — chúng chỉ ghi lại quyết định của con người theo định dạng chuẩn
- ❌ Skills KHÔNG phải code generator — output là tài liệu Markdown

Skills là **khuôn đúc**: bạn đổ nguyên liệu (codebase + đầu vào thô + quyết định của stakeholders) vào, ra tài liệu đúng hình.

---

## 3. Bản đồ 19 skills

Skills tổ chức theo **5 phase** + **cross-cutting**, mirror cấu trúc thư mục `docs/` của dự án đích.

### Phase 0 — Requirements (5 skills)

Phase đầu tiên: **làm rõ dự án sẽ làm gì**.

| Skill | Vai trò | Output |
|-------|---------|--------|
| `project-context-ingestion` | **Vào trước Phase 0**: Ingest tài liệu thô (phỏng vấn, email, RFP, regulatory PDF, dashboard) → CONTEXT_PACK.md có cấu trúc | `00_REQUIREMENTS/CONTEXT_PACK.md` |
| `srs-greenfield-author` | Viết SRS (Software Requirements Specification — tài liệu yêu cầu phần mềm chính thức) cho dự án mới | `00_REQUIREMENTS/SRS_VI/M1-M10` |
| `srs-reverse-engineer` | Reverse-engineer SRS từ code đã có | `00_REQUIREMENTS/SRS_VI/M1-M10` |
| `nfr-specification` | Đặc tả NFR (Non-Functional Requirements — yêu cầu phi chức năng: hiệu năng, bảo mật, khả dụng) | `00_REQUIREMENTS/SRS_VI/M9_*` |
| `requirements-traceability` | Tạo RTM (Requirements Traceability Matrix — bảng truy vết yêu cầu → test → code) | `00_REQUIREMENTS/SRS_VI/M10_*` |

### Phase 1 — Discovery (4 skills)

**Hiểu cái đã tồn tại** (chỉ áp dụng khi có code).

| Skill | Vai trò | Output |
|-------|---------|--------|
| `codebase-discovery` | Bản đồ kỹ thuật của codebase (entry point, module, dependency) | `01_DISCOVERY/CODEBASE_MAP.md` |
| `data-architecture-audit` | Bản đồ dữ liệu (DB, schema, lưu trữ, governance) | `01_DISCOVERY/DATA_ARCHITECTURE.md` |
| `tech-debt-audit` | Liệt kê nợ kỹ thuật + rủi ro | `01_DISCOVERY/TECH_DEBT_AUDIT.md` |
| `business-context-capture` | Bản đồ nghiệp vụ (actor, use case, business rule, workflow) | `01_DISCOVERY/BUSINESS_CONTEXT.md` |

### Phase 2 — Strategic (3 skills)

**Quyết định nên làm gì và ai trả tiền**.

| Skill | Vai trò | Output |
|-------|---------|--------|
| `feasibility-assessment` | Business case: ROI, chi phí, rủi ro qua 3 kịch bản (Full / Partial / Minimum) | `02_STRATEGIC/FEASIBILITY_ASSESSMENT.md` |
| `tech-solution-design` | Thiết kế giải pháp kỹ thuật + ADR (Architecture Decision Record — biên bản quyết định kiến trúc) | `02_STRATEGIC/TECH_SOLUTION_DESIGN.md` |
| `implementation-planning` | Master plan + chia thành Work Package (gói công việc) | `02_STRATEGIC/MASTER_PLAN.md` + `03_EXECUTION/work-packages/PHASE_*.md` |

### Phase 3 — Execution (3 skills)

**Làm**.

| Skill | Vai trò | Output |
|-------|---------|--------|
| `work-package-decomposer` | Chia 1 Work Package thành micro-task (Tier 1/2/3) cho AI làm | Decompose per WP |
| `ai-operator-protocol` | Quy tắc vận hành cho AI executor (7 hard rules + 14-step workflow) | `03_EXECUTION/AI_OPERATOR_GUIDE.md` |
| `multi-tier-ai-routing` | Chính sách routing task: dùng AI rẻ cho task đơn giản, AI mạnh cho task phức tạp, người cho task quyết định | `03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md` |

### Phase 4 — Maintenance (3 skills)

**Sau khi đã chạy production**.

| Skill | Vai trò | Output |
|-------|---------|--------|
| `incident-response-playbook` | Runbook xử lý sự cố theo NIST IR (chuẩn ứng cứu sự cố của NIST) | `04_MAINTENANCE/runbooks/INCIDENT_*.md` |
| `feature-extension-planning` | Lập kế hoạch thêm tính năng mới sau khi đã ship | `04_MAINTENANCE/feature-extensions/FEAT_*.md` |
| `documentation-sync` | Audit doc-vs-code drift hàng tháng | `04_MAINTENANCE/DOC_SYNC_REPORT.md` |

### Cross-cutting (2 skills)

**Tiện ích xuyên suốt**.

| Skill | Vai trò | Output |
|-------|---------|--------|
| `document-index-master` | Tạo INDEX.md (master nav) cho dự án | `INDEX.md` |
| `document-consistency-review` | Audit nhất quán doc-vs-doc theo 8 chiều (terminology, numbers, references, versioning, owners, decisions, status, glossary) | `04_MAINTENANCE/CONSISTENCY_REVIEW_REPORT.md` |

---

## 4. Khi nào dùng skill nào — cây quyết định

Bắt đầu ở dòng đầu tiên áp dụng:

```
Bạn đang ở giai đoạn nào của dự án?
│
├── (A) Mới nhận bàn giao, chưa biết gì
│       → Bắt đầu: project-context-ingestion (xử lý nguyên liệu thô trước)
│       → Tiếp: nếu có code → Phase 1 (codebase-discovery, data-architecture-audit, tech-debt-audit, business-context-capture)
│       → Tiếp: srs-reverse-engineer (nếu có code) hoặc srs-greenfield-author (nếu chưa có)
│
├── (B) Dự án mới hoàn toàn (greenfield), có ý tưởng + stakeholders
│       → project-context-ingestion (consolidate phỏng vấn + RFP + ràng buộc)
│       → srs-greenfield-author + nfr-specification
│       → feasibility-assessment + tech-solution-design + implementation-planning
│       → Phase 3 Execution
│
├── (C) Đã có Phase 0+1, cần quyết định "có nên làm rewrite/refactor?"
│       → feasibility-assessment (3 kịch bản với ROI)
│       → Nếu approve → tech-solution-design → implementation-planning
│
├── (D) Đã có plan, cần thực thi với đội AI agent
│       → ai-operator-protocol (set guideline cho AI)
│       → multi-tier-ai-routing (chính sách phân tier)
│       → work-package-decomposer (chia từng WP thành micro-task)
│
├── (E) Đã ship production, vận hành
│       → incident-response-playbook (chuẩn bị runbook trước khi có sự cố)
│       → documentation-sync (chạy hàng tháng)
│       → feature-extension-planning (mỗi feature mới)
│
└── (F) Đã có nhiều tài liệu, cần audit
        → document-consistency-review (quý 1 lần)
        → document-index-master (tạo INDEX nếu chưa có)
```

---

## 5. Vận hành thực tế — 3 con đường

### 5.1 Con đường LEGACY (đã có code, chưa có docs)

Ví dụ: Bàn giao một codebase 4 năm tuổi, không ai biết hết business rules.

**Trình tự:**

```
Tuần 1:  project-context-ingestion       ← phỏng vấn + email + Slack archive
Tuần 1:  codebase-discovery              ← bản đồ kỹ thuật
Tuần 2:  data-architecture-audit         ← bản đồ dữ liệu
Tuần 2:  business-context-capture        ← bản đồ nghiệp vụ
Tuần 3:  tech-debt-audit                 ← liệt kê nợ + rủi ro
Tuần 4:  srs-reverse-engineer            ← SRS chính thức từ code
Tuần 4:  nfr-specification               ← M9 NFR
Tuần 5:  requirements-traceability       ← M10 RTM
Tuần 5:  document-index-master           ← INDEX
```

**Output sau 5 tuần:** Bộ tài liệu hoàn chỉnh, có thể audit được, người mới đọc 1-2 ngày là vào việc.

**Chi phí ước tính:** 1 senior engineer chạy AI + supervise ~30-40 giờ thuần thay vì 200-300 giờ tự viết.

### 5.2 Con đường GREENFIELD (chưa có code)

Ví dụ: Khởi động dự án mới sau khi có decision kick-off.

**Trình tự:**

```
Tuần 1:  project-context-ingestion       ← phỏng vấn stakeholders + RFP + ràng buộc
Tuần 2:  srs-greenfield-author           ← SRS M1-M8 (functional)
Tuần 2:  nfr-specification               ← M9 NFR
Tuần 3:  feasibility-assessment          ← 3 kịch bản, business case
         ↑ DỪNG: stakeholder approval
Tuần 4:  tech-solution-design            ← kiến trúc + ADR
Tuần 5:  implementation-planning         ← master plan + work packages
Tuần 5:  ai-operator-protocol            ← AI guideline
Tuần 5:  multi-tier-ai-routing           ← phân tier
         ↑ Bắt đầu Phase 3 Execution
Tuần 6+: work-package-decomposer (chạy lặp lại từng WP)
```

**Lưu ý quan trọng:** Sau Tuần 3 phải dừng lại chờ stakeholder approve feasibility. Đừng để AI chạy thẳng từ SRS sang execution mà bỏ qua quyết định kinh doanh.

### 5.3 Con đường MAINTENANCE (đã ship)

Khi production đang chạy:

**Định kỳ:**
- **Hàng tháng:** `documentation-sync` → audit doc-vs-code drift
- **Hàng quý:** `document-consistency-review` → audit doc-vs-doc

**Theo sự kiện:**
- **Trước go-live module mới:** `incident-response-playbook` cho mọi failure mode đã biết
- **Mỗi feature mới:** `feature-extension-planning` (mini-SRS cho phạm vi nhỏ)
- **Khi có sự cố:** mở runbook đã chuẩn bị → xử lý → cập nhật runbook

---

## 6. Cách dùng skills với AI agent

Skills được thiết kế để AI agent (Claude, GPT, ...) dùng tự động. Không cần con người đọc qua từng dòng SKILL.md.

### 6.1 Khi nào AI tự kích hoạt skill

Mỗi `SKILL.md` có frontmatter dạng:

```yaml
---
name: srs-greenfield-author
description: ... Triggers include "write SRS", "create requirements doc", ...
---
```

AI đọc `description` + `Triggers`. Khi user nói câu khớp với trigger ("Hãy viết SRS cho dự án X"), AI tự nạp skill.

### 6.2 Mẫu prompt thực tế

**Trường hợp đơn giản** — AI tự chọn skill:
```
Tôi vừa nhận codebase dự án Helix. Cần phải có docs đầy đủ để audit.
Bạn xem qua bộ skills trong company-skills/ và đề xuất quy trình.
```

**Trường hợp chỉ định** — bạn biết chính xác cần skill nào:
```
Chạy skill srs-reverse-engineer cho codebase này.
Inputs đã có: docs/01_DISCOVERY/BUSINESS_CONTEXT.md, CODEBASE_MAP.md, DATA_ARCHITECTURE.md.
Output ghi vào docs/00_REQUIREMENTS/SRS_VI/.
```

**Trường hợp pipeline** — chuỗi nhiều skill:
```
Chạy lần lượt cho codebase này:
1. project-context-ingestion (raw inputs ở folder _handover/)
2. business-context-capture
3. srs-reverse-engineer
4. nfr-specification

Sau mỗi skill, dừng lại tóm tắt để tôi review trước khi chạy skill tiếp theo.
```

### 6.3 Nguyên tắc khi để AI vận hành

1. **Luôn để AI dừng giữa các phase** để con người review. Đừng pipeline hết Phase 0 → Phase 4 không gián đoạn — quyết định stakeholder phải vào ở Phase 2.
2. **Luôn cung cấp inputs đầy đủ.** Nếu skill yêu cầu CONTEXT_PACK.md mà bạn không có, đừng để AI "đoán" — chạy `project-context-ingestion` trước.
3. **Đọc Section "Failure modes to avoid" của mỗi SKILL.md** ít nhất 1 lần. Đó là nơi tóm tắt các lỗi điển hình AI hay phạm.
4. **Kiểm `references/checklist.md` của mỗi skill** sau khi AI chạy xong. Đây là quality gate trước khi giao output cho stakeholder.

---

## 7. Câu chuyện thực tế (anonymized)

### 7.1 "Project Pegasus" — logistics rewrite

**Tình huống:** CEO muốn rewrite hệ thống dispatch logistics 9 năm tuổi. CTO mới 1 năm, founding engineer đã rời. Có $1.4M / 14 tháng.

**Áp dụng:**
1. **Tuần 1:** `project-context-ingestion` xử lý 17 nguồn (6 phỏng vấn khách hàng, 4 phỏng vấn nội bộ, 3 báo cáo, 4 doc khác). Output: CONTEXT_PACK.md surface 1 contradiction quan trọng — CEO muốn "rewrite", CTO muốn "incremental refactor". **Phát hiện trước Phase 2 thay vì sau khi đã đầu tư 2 tháng.**
2. **Tuần 2-3:** Joint call CEO+CTO, quyết định rewrite có scope giới hạn.
3. **Tuần 4-5:** `srs-greenfield-author` + `nfr-specification`. SRS có dấu vết tới CONTEXT_PACK — mỗi FR cite [SRC-NNN].
4. **Tuần 6:** `feasibility-assessment` 3 kịch bản: Full $1.4M, Partial $900K, Minimum $400K. Stakeholder chọn Partial vì timeline ép.
5. **Tuần 7-8:** `tech-solution-design` + `implementation-planning`. Master plan 18 Work Packages.
6. **Tuần 9+:** Phase 3 Execution với AI routing — 88% task chạy bằng tier rẻ.

**Kết quả:** Chi phí methodology ~6% tổng budget. Phát hiện vấn đề rewrite-vs-refactor sớm tiết kiệm ước tính $200K rework.

### 7.2 "Project Atrium" — invoicing SaaS audit

**Tình huống:** Khách hàng yêu cầu SOC2 audit. Codebase đã chạy 3 năm, không có SRS.

**Áp dụng:**
1. `business-context-capture` + `codebase-discovery` (2 tuần)
2. `srs-reverse-engineer` + `nfr-specification` + `requirements-traceability` (2 tuần)
3. Audit pass.

**Kết quả:** Methodology cost: 4 tuần. Tự viết tay: ước tính 3 tháng + 1 consultant.

### 7.3 "Living maintenance" — SaaS đã ship 2 năm

**Áp dụng định kỳ:**
- Mỗi feature mới: `feature-extension-planning` (~30 phút/feature thay vì viết tự do mất 2-3 giờ + chất lượng không đồng đều)
- Mỗi quý: `document-consistency-review` phát hiện ~10-15 inconsistency
- Mỗi tháng: `documentation-sync` — drift nhỏ phát hiện sớm thay vì tích lũy

**Kết quả:** Doc rot không xảy ra. Onboarding dev mới: 1 ngày thay vì 1 tuần.

---

## 8. Quality bar — làm sao biết output tốt

### 8.1 Test 5 phút

Sau khi skill chạy xong, áp dụng test này:

1. **Mở `references/checklist.md`** của skill đó. Đi qua từng Gate. Có Gate nào fail?
2. **Đưa output cho 1 người mới** (chưa biết dự án) và hỏi: "Đọc 10 phút, kể tôi nghe dự án này làm gì?" Nếu họ không kể được — output thiếu rõ ràng.
3. **Đưa output cho 1 stakeholder** và hỏi: "Có gì sai không?" Stakeholder feedback > AI tự verify.

### 8.2 Dấu hiệu output kém (red flags)

- Tài liệu dài nhưng nói chung chung ("hệ thống cần thân thiện với người dùng")
- Không có citation (claim không có dấu vết tới nguồn)
- Mọi requirement đều "Must" priority (không có sự ưu tiên thực sự)
- Section Open Questions trống (= AI giả vờ biết hết)
- Mọi NFR đều dùng số tròn ("99.9% uptime") không dẫn nguồn

### 8.3 Dấu hiệu output tốt

- Mỗi claim có citation [SRC-NNN] hoặc file:line
- Open Questions có ít nhất 3-5 mục
- Contradictions/Conflicts được surface, không bị "synthesize" mất
- Coverage statement honest ("Đã review 80% code, sample 20%")
- Confidence rating thấp khi đầu vào ít

---

## 9. FAQ

### Q1: Tôi không biết tiếng Anh tốt — skills viết tiếng Anh tôi đọc được không?

Skills (SKILL.md, template) viết tiếng Anh chủ yếu để AI đọc — không cần bạn đọc trực tiếp. Output (tài liệu cuối cùng) AI có thể sinh tiếng Việt nếu bạn yêu cầu. Khi prompt AI: "Output viết tiếng Việt, giữ nguyên tên skill và placeholder tiếng Anh trong template."

### Q2: Tôi có cần đọc hết 19 SKILL.md không?

Không. Đọc INDEX.md + GETTING_STARTED.md (file này) là đủ để biết khi nào dùng skill nào. Khi AI chạy 1 skill cụ thể, AI sẽ tự đọc SKILL.md đó. Bạn chỉ cần đọc kỹ SKILL.md khi muốn debug output không như ý.

### Q3: Skills này có chạy được không qua Claude Code / Cursor / ChatGPT?

Có. Skills là Markdown thuần — bất kỳ AI nào đọc Markdown đều dùng được. Format frontmatter chuẩn Anthropic Skill (name + description) — Claude Code tự động phát hiện và kích hoạt. Các IDE khác cần copy nội dung skill vào prompt thủ công.

### Q4: Output cần lưu ở đâu?

Mỗi skill khai báo trong SKILL.md. Convention chung:
```
docs/
├── 00_REQUIREMENTS/
├── 01_DISCOVERY/
├── 02_STRATEGIC/
├── 03_EXECUTION/
└── 04_MAINTENANCE/
```
Mirror y hệt cấu trúc skills folder. Skill biết tự ghi đúng chỗ.

### Q5: Có thể tùy biến template không?

Có. 3 cách:

- **Mode B** (Honor company template): nếu công ty đã có template SRS riêng, skill sẽ tôn trọng template đó
- **Mode C** (User-defined): bạn cung cấp cấu trúc riêng
- **Sửa trực tiếp** template trong `assets/`: được, nhưng cân nhắc — sẽ phải maintain bản sửa khi skill nâng cấp

Đừng tùy biến vì sở thích cá nhân — chỉ tùy biến khi có lý do nghiệp vụ thật (compliance, format do regulator yêu cầu).

### Q6: Skills có bị lỗi thời không?

Có, sau ~6-12 tháng. Cần cơ chế version + review:
- Mỗi skill ghi `v1` trong INDEX
- Khi nâng v2, lưu v1 vào `_archive/`
- Review skill suite quý 1 lần — feedback từ team thực sự dùng

### Q7: Tôi cần biết AI / programming để dùng được skills?

Không. Bạn chỉ cần:
- Biết phase nào của dự án (5 phase trên)
- Biết đầu vào bạn có (code? phỏng vấn? regulatory doc?)
- Biết yêu cầu prompt AI (xem mẫu Section 6.2)

Phần còn lại AI lo.

### Q8: Tài liệu sinh ra có thay thế được consultant không?

Một phần. Skills tạo **draft** chất lượng nền. Consultant vẫn cần cho:
- Quyết định chiến lược (rewrite vs refactor)
- Đàm phán stakeholders đối kháng
- Chuyên môn hẹp (regulatory deep dive, security audit)

Nhưng phần "viết và format tài liệu" — skills xử lý 70-80%.

### Q9: Khi AI sinh sai thì làm gì?

1. Đọc `references/failure-modes` (cuối SKILL.md) — kiểm tra có rơi vào pattern lỗi điển hình không
2. Chạy lại skill với input rõ hơn (thường lỗi do input thiếu)
3. Sửa output thủ công + ghi feedback vào skill (cập nhật `examples.md`)
4. Báo bug nếu skill có vấn đề chung

### Q10: Skills này có IP của ai?

Skills là tài sản công ty, lưu trong repo `company-skills/`. Mọi dự án nội bộ được dùng. Không đẩy public.

---

## 10. Bắt đầu nhanh (TL;DR)

Nếu bạn vừa đọc đến đây và muốn thử ngay:

1. **Mở Claude Code / Cursor / Copilot** trong thư mục dự án
2. **Copy file `company-skills/`** vào dự án (hoặc symlink)
3. **Prompt AI:**
   ```
   Tôi có codebase dự án [TÊN]. Cần làm tài liệu chuẩn theo company-skills/.
   Bắt đầu bằng việc đọc INDEX.md và GETTING_STARTED.md, rồi đề xuất quy trình.
   ```
4. **AI sẽ đề xuất** 5-10 skill theo thứ tự + lý do. Bạn approve.
5. **AI chạy từng skill**, dừng giữa phase để bạn review.
6. **Sau 1-5 tuần** (tùy size), bạn có bộ tài liệu chuẩn.

---

## 11. Tham khảo

- **Cấu trúc skills:** [INDEX.md](INDEX.md) — bản đồ 19 skills
- **Format chuẩn:** Mỗi skill có frontmatter Anthropic Skill format (name + description) + 5 file (SKILL + 4 references/assets)
- **Methodology gốc:** Built từ kinh nghiệm vận hành dự án FinanceOS, anonymized + generalized
- **Phản hồi:** Issue/PR vào repo `company-skills/`. Mọi skill đều có examples — đóng góp ví dụ từ dự án thực giúp skill mạnh hơn.

---

## 12. Khi nào KHÔNG dùng skills này

Để cân bằng — đừng dùng ceremonially:

- **Dự án 1-tuần** (PoC, prototype): Skills overhead lớn hơn output. Viết 1-pager là đủ.
- **Bug fix nhỏ**: không cần SRS để sửa 5 dòng code.
- **Internal tool 5 user**: feasibility-assessment + 3 scenario là quá. Dùng decision đơn giản hơn.
- **Đã có team docs đang chạy tốt**: Đừng phá vỡ thứ đang work — chỉ áp dụng khi vấn đề thực tế xuất hiện.

Skills xứng đáng chi phí khi: dự án đa team, kéo dài ≥3 tháng, có audit/compliance, hoặc handover giữa người/team.

---

*Skills là khuôn — quyết định và tri thức nghiệp vụ vẫn là của bạn. Đừng để khuôn dẫn dắt nội dung; để nội dung lấp đầy khuôn.*
