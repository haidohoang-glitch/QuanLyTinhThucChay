# Luồng Thực hiện Chi tiết — Pre-Phase 0 → Phase 4

> **Tài liệu này khác gì với [GETTING_STARTED.md](GETTING_STARTED.md)?**
>
> - `GETTING_STARTED.md` = giá trị + quyết định **dùng hay không**, đọc 5-15 phút.
> - `WORKFLOW_GUIDE.md` (file này) = vận hành chi tiết **từng skill, từng bước**, dùng khi bạn đã quyết định chạy.
>
> **Cách đọc:**
> - Lần đầu: đọc Phần 1 (tổng quan) + phase mà bạn đang ở.
> - Khi chạy 1 skill: nhảy thẳng tới mục skill đó (Ctrl+F tên skill).
> - Mỗi mục skill có cấu trúc giống nhau: Mục tiêu → Inputs → Prompt mẫu → Quy trình bên trong → Output → Hand-off → Tips.

---

## 1. Tổng quan luồng — Pre-Phase 0 đến Phase 4

```
┌──────────────────────────────────────────────────────────────────┐
│  PRE-PHASE 0: project-context-ingestion                          │
│  Inputs thô (phỏng vấn, email, RFP, regulatory) → CONTEXT_PACK.md│
└────────────────┬─────────────────────────────────────────────────┘
                 │
        ┌────────┴─────────┐
        │                  │
   Có code sẵn?       Chưa có code?
   (LEGACY)           (GREENFIELD)
        │                  │
        ▼                  ▼
┌──────────────────┐  (Bỏ qua Phase 1)
│ PHASE 1 Discovery │
│ codebase-discovery│
│ data-arch-audit   │
│ tech-debt-audit   │
│ business-ctx-cap  │
└─────────┬────────┘
          │
          ▼                   ▼
┌──────────────────────────────────────────┐
│  PHASE 0 Requirements                     │
│  ├─ srs-reverse-engineer (legacy)         │
│  │  HOẶC srs-greenfield-author (mới)     │
│  ├─ nfr-specification (M9)                │
│  └─ requirements-traceability (M10)       │
└─────────┬─────────────────────────────────┘
          │
          ▼
┌──────────────────────────────────────────┐
│  PHASE 2 Strategic                        │
│  ├─ feasibility-assessment                │
│  │  ⚠️ STAKEHOLDER APPROVAL GATE           │
│  ├─ tech-solution-design                  │
│  └─ implementation-planning               │
└─────────┬─────────────────────────────────┘
          │
          ▼
┌──────────────────────────────────────────┐
│  PHASE 3 Execution                        │
│  ├─ ai-operator-protocol                  │
│  ├─ multi-tier-ai-routing                 │
│  └─ work-package-decomposer (lặp/WP)     │
│  ⚠️ DEPLOY TO PRODUCTION GATE              │
└─────────┬─────────────────────────────────┘
          │
          ▼
┌──────────────────────────────────────────┐
│  PHASE 4 Maintenance (ONGOING)            │
│  ├─ documentation-sync (hàng tháng)       │
│  ├─ feature-extension-planning (per feat) │
│  └─ incident-response-playbook (per fail) │
└──────────────────────────────────────────┘

Cross-cutting (chèn vào bất kỳ phase nào):
  • document-index-master           — sau Phase 0/1
  • document-consistency-review     — quý 1 lần
```

### 1.1 Lưu ý thứ tự đặc biệt

**Với dự án LEGACY** (đã có code, chưa có docs):
- Phase 1 chạy TRƯỚC Phase 0. Lý do: cần hiểu code trước khi reverse-engineer SRS.
- Thứ tự: Pre-P0 → P1 → P0 → P2 → P3 → P4

**Với dự án GREENFIELD** (chưa có code):
- Bỏ qua hoàn toàn Phase 1.
- Thứ tự: Pre-P0 → P0 → P2 → P3 (tạo code) → P4

**Với MAINTENANCE** (production đã chạy):
- Chỉ Phase 4 + cross-cutting; chỉ về Phase 0-3 khi có thay đổi lớn (rewrite, pivot).

### 1.2 Cổng quyết định (Decision Gates)

Có 3 cổng bắt buộc dừng chờ con người:

| Cổng | Vị trí | Quyết định cần |
|------|--------|----------------|
| **G1 — Feasibility approval** | Sau `feasibility-assessment` | Stakeholder chọn 1 trong 3 kịch bản (Full/Partial/Minimum/Do nothing). KHÔNG cho AI tự chọn. |
| **G2 — Solution design approval** | Sau `tech-solution-design` | Tech lead/CTO ký duyệt ADR trước khi vào planning chi tiết. |
| **G3 — Deploy to production** | Cuối Phase 3 | Operator + ops team approve go-live. Không phải chuyện của skills. |

Đừng pipeline qua các cổng này.

---

## 2. PRE-PHASE 0 — Project Context Ingestion

Phase này thực ra không phải "Phase 0" theo nghĩa output formal docs, mà là **chuẩn bị nguyên liệu** cho mọi phase sau. Bỏ qua phase này = AI "đoán" intent stakeholders, dẫn tới SRS sai chiều.

### Skill: `project-context-ingestion`

**Mục tiêu:** Biến đống raw materials (phỏng vấn, email, RFP, screenshot, regulatory PDF, dashboard, Slack archive) thành 1 file `CONTEXT_PACK.md` có cấu trúc, có citation, có anonymization.

**Khi chạy:** Đầu tiên, trước mọi skill khác. Hoặc khi có thay đổi stakeholder lớn (CEO mới, regulation mới, pivot).

**Inputs cần có:**
- Một thư mục chứa raw materials (Drive export, Notion export, transcripts, PDFs, screenshots)
- Lý tưởng: ≥3 trong 6 categories (User research / Internal comms / Informal docs / External / Operational data / Constraints & compliance)

**Prompt mẫu:**
```
Tôi có raw materials cho dự án [TÊN] ở folder _handover/.
Chạy skill project-context-ingestion theo Mode A (6 categories standard).
Anonymize PII mặc định. Output ghi vào docs/00_REQUIREMENTS/CONTEXT_PACK.md
+ folder _sources/ với từng file SRC-NNN.

Sau khi chạy, dừng lại liệt kê:
1. Có bao nhiêu nguồn ở mỗi category
2. Top 3 contradictions phát hiện
3. Open Questions cần stakeholder resolve trước khi vào Phase 0
```

**Quy trình bên trong (8 bước):**
1. Inventory mọi nguồn → bảng SRC-001..N
2. Choose Mode (A/B/C)
3. Anonymize PII
4. Extract insight per source (claim + quote + implied requirement + constraint + open question + confidence)
5. Cross-reference: consensus / contradictions / gaps
6. Identify open questions cho stakeholder
7. Produce CONTEXT_PACK.md theo template 14 sections
8. Self-review qua `references/checklist.md`

**Output:**
- `docs/00_REQUIREMENTS/CONTEXT_PACK.md` (chính)
- `docs/00_REQUIREMENTS/_sources/SRC-NNN_<slug>.md` (raw đã anonymize)

**Hand-off → skill tiếp theo:**
- Section 3 (Stakeholder Voice) → `srs-greenfield-author` / `srs-reverse-engineer`
- Section 4 (Business Context) → `business-context-capture` / `feasibility-assessment`
- Section 6 (Operational Reality) → `feasibility-assessment`
- Section 7 (Constraints) → `nfr-specification` + `tech-solution-design`
- Section 8 (Contradictions) → STAKEHOLDER MEETING (resolve trước khi vào Phase 0)
- Section 12 (Open Questions) → M10 RTM Issues sau này

**Tips:**
- ⚠️ Đừng skip ngay cả khi nguyên liệu mỏng. Pack 3 nguồn vẫn tốt hơn 0 nguồn — Section 9 (Gaps) tự khai báo cái gì còn thiếu.
- ⚠️ Contradictions là vàng. Nếu pack không có contradictions = AI đang "synthesize" (bỏ sót xung đột thật).
- 💡 Re-run sau 6 tháng nếu dự án dài. Stakeholder và regulation đổi.

---

## 3. PHASE 1 — Discovery (chỉ áp dụng cho LEGACY)

Bỏ qua phase này nếu dự án greenfield (chưa có code). Với legacy: **hiểu code trước khi viết SRS**.

Thứ tự khuyến nghị: `codebase-discovery` → `data-architecture-audit` → `business-context-capture` → `tech-debt-audit`. Logic: bản đồ kỹ thuật trước, sau đó dữ liệu, sau đó nghiệp vụ, cuối cùng nợ kỹ thuật.

### Skill: `codebase-discovery`

**Mục tiêu:** Bản đồ kỹ thuật — entry points, modules, dependencies, build/run.

**Khi chạy:** Đầu Phase 1, sau khi đã có CONTEXT_PACK.md.

**Inputs:**
- Quyền đọc codebase
- (Lý tưởng) `docs/00_REQUIREMENTS/CONTEXT_PACK.md`

**Prompt mẫu:**
```
Chạy codebase-discovery cho repo này.
Xuất docs/01_DISCOVERY/CODEBASE_MAP.md.
Sample-based: đọc kỹ src/, scan tests/, ghi chú config/.
Sau khi xong, báo % code đã đọc trực tiếp vs sample.
```

**Quy trình bên trong:**
1. Identify entry points (main, server.js, app.tsx, ...)
2. Map module structure (per top-level folder)
3. Trace dependency graph
4. Document build/run/test commands
5. Note framework versions + critical dependencies
6. Highlight unusual patterns
7. Self-review checklist

**Output:** `docs/01_DISCOVERY/CODEBASE_MAP.md`

**Hand-off:**
- → `srs-reverse-engineer` (M2.1 product perspective + M2.4 operating environment)
- → `data-architecture-audit` (technical context)
- → `tech-debt-audit` (codebase shape)

**Tips:**
- 💡 Output không cần kể mọi file. Tập trung structure + entry + dependency, không phải file inventory.
- ⚠️ Đừng confuse với business context. Skill này KHÔNG nói "ai dùng" — chỉ "code chạy thế nào".

### Skill: `data-architecture-audit`

**Mục tiêu:** Bản đồ dữ liệu — schemas, storage layers, data flow, governance.

**Khi chạy:** Sau `codebase-discovery`.

**Inputs:**
- Codebase + DB schemas (migrations, ORM models)
- Cloud config (S3, BigQuery, Redshift, ...)
- (Optional) `docs/01_DISCOVERY/CODEBASE_MAP.md`

**Prompt mẫu:**
```
Chạy data-architecture-audit. Xuất docs/01_DISCOVERY/DATA_ARCHITECTURE.md.
Đặc biệt chú ý: PII storage, data retention, cross-border transfer.
Cite migration files cụ thể cho mỗi schema claim.
```

**Quy trình bên trong:**
1. Identify storage layers (DB, cache, blob, queue, search)
2. Document schemas + relationships
3. Trace data flow (ingestion → transformation → output)
4. Note governance: PII, retention, encryption, access control
5. Identify data risks
6. Self-review

**Output:** `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`

**Hand-off:**
- → `srs-reverse-engineer` (M2.5 constraints)
- → `nfr-specification` (input cho NFR security/privacy)
- → `feasibility-assessment` (data migration cost projection)

**Tips:**
- ⚠️ PII và retention là điểm nóng compliance. Đừng paraphrase — cite chính xác file:line.
- 💡 Cross-reference với CONTEXT_PACK Section 7.1 (Regulatory) — match data thực tế với requirement.

### Skill: `business-context-capture`

**Mục tiêu:** Bản đồ nghiệp vụ — actors, use cases, business rules, workflows, invariants.

**Khi chạy:** Sau `codebase-discovery` + `data-architecture-audit`.

**Inputs:**
- Codebase
- `docs/01_DISCOVERY/CODEBASE_MAP.md`
- `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`
- (Lý tưởng) `docs/00_REQUIREMENTS/CONTEXT_PACK.md` để cross-check stakeholder voice

**Prompt mẫu:**
```
Chạy business-context-capture. Mode A (DDD-lite default).
Xuất docs/01_DISCOVERY/BUSINESS_CONTEXT.md.

Đặc biệt: cross-reference với CONTEXT_PACK.md Section 3 (stakeholder voice).
Nếu code mâu thuẫn với stakeholder voice → flag trong Section 9 Open Questions.
```

**Quy trình bên trong (10 bước):**
1. Identify primary actors
2. List use cases per actor
3. Choose decomposition mode (A: DDD-lite / B: existing model / C: user-defined)
4. Extract domain entities
5. Find business rules (validation / calculation / eligibility)
6. Document workflows
7. Identify invariants
8. Find ambiguities
9. Fill template
10. Self-review

**Output:** `docs/01_DISCOVERY/BUSINESS_CONTEXT.md`

**Hand-off:**
- → `srs-reverse-engineer` (M2-M8 phần lớn lấy từ đây)
- → `feasibility-assessment` (value at risk if system fails)

**Tips:**
- ⚠️ KHÔNG mô tả code chạy thế nào — đó là `codebase-discovery`. Skill này chỉ business view.
- ⚠️ KHÔNG đề xuất thay đổi sản phẩm — descriptive only.
- 💡 Invariants (Section 7) là phần quý nhất, dễ skip nhất. Cố tìm.

### Skill: `tech-debt-audit`

**Mục tiêu:** Liệt kê nợ kỹ thuật + rủi ro với severity + remediation cost.

**Khi chạy:** Cuối Phase 1, sau 3 skill kia.

**Inputs:**
- Codebase
- 3 outputs từ Phase 1 trước (CODEBASE_MAP, DATA_ARCHITECTURE, BUSINESS_CONTEXT)
- (Optional) Issue tracker, support log

**Prompt mẫu:**
```
Chạy tech-debt-audit. Sample 30% files quan trọng + scan toàn bộ.
Xuất docs/01_DISCOVERY/TECH_DEBT_AUDIT.md.
Xếp severity: Critical (gây outage được) / High (chậm phát triển) / Medium / Low.
Mỗi finding: cost-of-inaction + cost-to-fix.
```

**Quy trình bên trong:**
1. Identify debt categories (code quality, security, performance, maintainability, dependency rot)
2. Sample-based deep dive vs scan
3. Severity calibration
4. Estimate cost-to-fix + cost-of-inaction
5. Pattern recognition (systemic issues)
6. Self-review

**Output:** `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md`

**Hand-off:**
- → `srs-reverse-engineer` (M2.7 assumptions, M10 issues)
- → `feasibility-assessment` (cost of inaction = baseline scenario)
- → `tech-solution-design` (constraints khi pick architecture)

**Tips:**
- ⚠️ "Tất cả Critical" = inflation. Force ranking — tối đa 5-10 Critical cho 1 dự án trung bình.
- 💡 Phân biệt **debt** (intentional shortcut) vs **bug** (unintended). Khác cách xử lý.

---

## 4. PHASE 0 — Requirements

Mục tiêu: Một bộ tài liệu yêu cầu chính thức, audit-grade.

Thứ tự: SRS skill (greenfield HOẶC reverse) → `nfr-specification` (M9) → `requirements-traceability` (M10).

### Skill: `srs-greenfield-author` (chỉ nếu chưa có code)

**Mục tiêu:** Author SRS từ vision + stakeholder input cho dự án mới.

**Khi chạy:** Greenfield, sau Pre-Phase 0.

**Inputs:**
- `docs/00_REQUIREMENTS/CONTEXT_PACK.md` (mạnh khuyên)
- Hoặc thủ công: vision + stakeholders + business goals + constraints + glossary + references

**Prompt mẫu:**
```
Chạy srs-greenfield-author Mode A (IEEE 830 standard).
Đọc CONTEXT_PACK.md trước.
Identify 4-6 functional domains từ Section 3 stakeholder voice.
Output: docs/00_REQUIREMENTS/SRS_VI/M1_Introduction.md ... Mx_<Domain>.md.
M9 + M10 chỉ tạo placeholder — sẽ chạy nfr-specification + requirements-traceability sau.

Mỗi FR: cite [SRC-NNN] từ CONTEXT_PACK. KHÔNG invent FR không có nguồn.
Open Questions từ CONTEXT_PACK Section 12 → đẩy vào M10.
```

**Quy trình bên trong (10 bước):**
1. Confirm scope (3 sentences: who/what/boundary)
2. Choose mode (A: IEEE 830 / B: company template / C: user-defined)
3. Write M1 Introduction
4. Write M2 Overall Description
5. Identify 4-8 functional domains
6. Write M3-Mx Functional modules (FR-XXX-NN format, atomic + testable + traceable)
7. Cross-reference between modules
8. Generate M9 placeholder
9. Generate M10 placeholder
10. Self-review

**Output:**
- `docs/00_REQUIREMENTS/SRS_VI/M1_Introduction.md`
- `docs/00_REQUIREMENTS/SRS_VI/M2_Overall_Description.md`
- `docs/00_REQUIREMENTS/SRS_VI/M3-Mx_<Domain>.md` (4-6 file)
- `docs/00_REQUIREMENTS/SRS_VI/M9_NFR_placeholder.md`
- `docs/00_REQUIREMENTS/SRS_VI/M10_RTM_placeholder.md`

**Hand-off:**
- → `nfr-specification` (M9)
- → `requirements-traceability` (M10)
- → `feasibility-assessment` (FR list = scope baseline cho scenarios)

**Tips:**
- ⚠️ Tránh "should be user-friendly" — replace bằng measurable. "User can complete checkout in ≤3 clicks" là FR; "user-friendly" là wishful thinking.
- ⚠️ Mọi FR trace tới source. "I think we need this" không phải source.
- 💡 Force MoSCoW priority. "All Must" = không có priority.

### Skill: `srs-reverse-engineer` (chỉ nếu có code)

**Mục tiêu:** Extract SRS từ codebase đã có — capture as-is requirements.

**Khi chạy:** Legacy, sau Phase 1 hoàn tất.

**Inputs:**
- `docs/00_REQUIREMENTS/CONTEXT_PACK.md` (mạnh khuyên — layers business intent lên code)
- `docs/01_DISCOVERY/BUSINESS_CONTEXT.md` (bắt buộc)
- `docs/01_DISCOVERY/CODEBASE_MAP.md` (bắt buộc)
- `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`
- `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md` (optional)
- Live UI access (verify workflow)

**Prompt mẫu:**
```
Chạy srs-reverse-engineer Mode A.
Đọc theo thứ tự: CONTEXT_PACK → BUSINESS_CONTEXT → CODEBASE_MAP → DATA_ARCHITECTURE.
Output 10 modules vào docs/00_REQUIREMENTS/SRS_VI/.

Mỗi FR phải cite cả: stakeholder source [SRC-NNN] (intent) + code path src/...:line (implementation).
Nếu code làm khác stakeholder voice → đẩy vào M10 Open Issues, đừng silently chọn 1 phía.
```

**Quy trình bên trong:** Tương tự greenfield nhưng nguồn là code + Phase 1 outputs thay vì stakeholder vision.

**Output:** Cùng files greenfield (M1-M10).

**Hand-off:** Cùng greenfield.

**Tips:**
- ⚠️ Code-vs-intent mismatch là phát hiện quan trọng nhất. Đừng "synthesize" — surface lên M10.
- 💡 Nếu CONTEXT_PACK thiếu, M10 Open Issues sẽ rất dài. Đó là honest, không phải failure.

### Skill: `nfr-specification`

**Mục tiêu:** Đặc tả NFR (Non-Functional Requirements) — performance, security, availability, scalability, usability, ...

**Khi chạy:** Sau M1-M8 SRS, trước M10.

**Inputs:**
- `docs/00_REQUIREMENTS/SRS_VI/M1-M8` (đã có)
- `docs/00_REQUIREMENTS/CONTEXT_PACK.md` (regulatory + SLA constraints)
- `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` (security/privacy baseline) — nếu legacy

**Prompt mẫu:**
```
Chạy nfr-specification.
Output: docs/00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md (overwrite placeholder).

Coverage 7 categories: Performance, Security, Availability, Scalability, Usability,
Maintainability, Compliance.

Mỗi NFR phải có:
- Số đo (target value)
- Phương pháp đo (how to verify)
- Source (regulatory? SLA? stakeholder? benchmark?)
KHÔNG dùng số tròn không nguồn (vd "99.9% uptime" — phải cite nguồn).
```

**Output:** `docs/00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md`

**Hand-off:**
- → `tech-solution-design` (NFRs ràng buộc kiến trúc choices)
- → `requirements-traceability` (NFRs vào RTM)

**Tips:**
- ⚠️ NFR vô số đo = vô nghĩa. "Phải nhanh" → "p95 < 200ms".
- 💡 Compliance NFRs cite regulation đầy đủ (regulation name + section + version + jurisdiction).

### Skill: `requirements-traceability`

**Mục tiêu:** RTM — bảng truy vết mỗi FR/NFR → test → code → người duyệt.

**Khi chạy:** Cuối Phase 0, sau M1-M9.

**Inputs:**
- Toàn bộ M1-M9 đã hoàn tất
- (Nếu có) test files, code paths

**Prompt mẫu:**
```
Chạy requirements-traceability.
Output: docs/00_REQUIREMENTS/SRS_VI/M10_RTM_Issues_Appendix.md.

3 phần:
1. RTM matrix: FR-ID | Description | Test cases | Code paths | Status | Owner
2. Open Issues: từ CONTEXT_PACK Section 12 + mismatches từ srs-reverse-engineer
3. Appendix: glossary, mock data, supporting tables

Mỗi FR thiếu test → đánh dấu "GAP — needs test plan".
```

**Output:** `docs/00_REQUIREMENTS/SRS_VI/M10_RTM_Issues_Appendix.md`

**Hand-off:**
- → audit (compliance evidence)
- → `implementation-planning` (gaps thành work items)

**Tips:**
- 💡 RTM rỗng cột Test Cases = không phải failure, là honest reporting. Phase 3 sẽ fill.
- ⚠️ Open Issues đừng "close" giả tạo. Nếu chưa resolve, để open.

---

### CỔNG G1 — Sau Phase 0

Trước khi vào Phase 2, kiểm tra:
- [ ] M1-M10 đầy đủ (không có placeholder ngoài M9/M10 nội dung tự sinh)
- [ ] Mọi FR có source citation
- [ ] Open Questions đã review với stakeholder ít nhất 1 lần
- [ ] M9 NFRs có số đo + source

Nếu chưa pass → quay lại fix, đừng vào Phase 2 với requirements yếu.

---

## 5. PHASE 2 — Strategic

Mục tiêu: Quyết định **CÓ làm hay không**, **làm thế nào**, và **kế hoạch**.

Thứ tự cứng: `feasibility-assessment` → ⚠️ G1 STAKEHOLDER APPROVAL → `tech-solution-design` → ⚠️ G2 ARCHITECTURE APPROVAL → `implementation-planning`.

### Skill: `feasibility-assessment`

**Mục tiêu:** Business case — 3 kịch bản (Full / Partial / Minimum) + Do nothing baseline, với ROI/cost/risk/benefit per scenario.

**Khi chạy:** Sau Phase 0 hoàn tất, trước mọi commitment kỹ thuật.

**Inputs:**
- `docs/00_REQUIREMENTS/CONTEXT_PACK.md` (budget cap, regulatory deadline, ops baseline, contradictions)
- Phase 1 outputs nếu legacy (TECH_DEBT, BUSINESS_CONTEXT, DATA_ARCH, CODEBASE_MAP)
- Phase 0 SRS (scope baseline)

**Prompt mẫu:**
```
Chạy feasibility-assessment Mode A (3 scenarios).
Question: "How much of [SCOPE] should we do?"
Output: docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md.

3 scenarios + Do nothing:
- Full: toàn bộ SRS Must+Should
- Partial: chỉ Must
- Minimum: subset Must (drop FR tốn nhất)
- Do nothing: keep current state

Mỗi scenario: cost (one-time + recurring), benefit ($/year), risk (severity + mitigation), timeline.
Bound bởi CONTEXT_PACK Section 7.3 (budget cap + deadline).

Sau khi xong, dừng để stakeholder approve. KHÔNG tự chọn scenario.
```

**Quy trình bên trong:**
1. Define question precisely (Should we / How much / X-vs-Y?)
2. Choose scenario mode (A: 3-tier / B: company template / C: custom)
3. For each scenario: scope, cost, benefit, risk, timeline
4. Compute ROI per scenario
5. Sensitivity analysis (what if 30% over budget?)
6. Recommendation (operator suggestion, NOT decision)
7. Self-review

**Output:** `docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md`

**Hand-off:**
- → ⚠️ STAKEHOLDER APPROVAL GATE G1
- → `tech-solution-design` (scope đã chọn)

**Tips:**
- ⚠️ "Do nothing" baseline bắt buộc. Không có baseline = không thấy được tại sao cần đầu tư.
- ⚠️ Operator đề xuất — stakeholder quyết. Đừng để AI claim "scenario X is best".
- 💡 Cite nguồn cho mọi số (revenue projection, cost estimate). Numbers without source = vibes.

### CỔNG G1 — Stakeholder approval

**Trước khi chạy `tech-solution-design`:**
- Stakeholder đã chính thức chọn 1 scenario
- Quyết định ghi vào quyết định note (PDF / email / meeting minutes)
- Reference quyết định trong tech-solution-design Mode B (Honor decision) hoặc Mode C

Nếu stakeholder chưa quyết → DỪNG. Đừng cho AI "đoán" và chạy tiếp.

### Skill: `tech-solution-design`

**Mục tiêu:** Thiết kế kỹ thuật cho scenario đã chọn — kiến trúc, công nghệ, ADRs.

**Khi chạy:** Sau G1 (stakeholder approve scenario).

**Inputs:**
- `docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md` + chosen scenario
- `docs/00_REQUIREMENTS/SRS_VI/M9_NFR.md`
- `docs/00_REQUIREMENTS/CONTEXT_PACK.md` Section 7.2 (vendor lock-ins)
- Phase 1 outputs nếu legacy

**Prompt mẫu:**
```
Chạy tech-solution-design.
Scenario đã approve: Partial ($900K, 14 tháng).
Output: docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md.

So sánh ≥3 candidate architectures với decision matrix.
Document mỗi major decision như ADR (Architecture Decision Record):
- Context, Decision, Alternatives Considered, Consequences.

Constraints bắt buộc honor:
- Vendor lock từ CONTEXT_PACK 7.2
- NFRs từ M9 (đặc biệt performance + security)
- Budget từ approved scenario.
```

**Quy trình bên trong:**
1. Re-read approved scenario + NFRs + constraints
2. Identify major architecture decisions needed (DB, framework, hosting, integration, ...)
3. For each decision: ≥3 candidates + comparison matrix
4. Document decision as ADR
5. System diagram (component-level, not deployment-level yet)
6. Self-review

**Output:** `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` (chứa multiple ADRs trong appendix hoặc separate ADR files)

**Hand-off:**
- → ⚠️ G2 ARCHITECTURE APPROVAL
- → `implementation-planning` (architecture defines work breakdown)

**Tips:**
- ⚠️ ADR mỗi decision — sau này Phase 4 sẽ tham chiếu lại.
- ⚠️ Không skip "Alternatives Considered". Decision không có alternatives = mệnh lệnh, không phải design.
- 💡 Nếu CONTEXT_PACK lock vendor → ADR ghi rõ "constrained choice", không phải "best choice".

### CỔNG G2 — Architecture approval

Tech lead / CTO ký duyệt ADR trước khi vào planning chi tiết.

### Skill: `implementation-planning`

**Mục tiêu:** Master plan — phases, work packages (WPs), milestones, ownership.

**Khi chạy:** Sau G2.

**Inputs:**
- `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` (architecture)
- `docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md` (scenario + timeline)
- `docs/00_REQUIREMENTS/SRS_VI/M*` (FR scope)

**Prompt mẫu:**
```
Chạy implementation-planning.
Output:
- docs/02_STRATEGIC/MASTER_PLAN.md (overall)
- docs/03_EXECUTION/work-packages/PHASE_0_*.md ... PHASE_N_*.md (per phase)

Decompose theo architecture từ TECH_SOLUTION_DESIGN.
Mỗi WP: scope, FR coverage (cite FR-IDs), estimated effort, dependencies, owner role.
Critical path tô đỏ.

Timeline khớp với approved scenario (14 tháng).
```

**Quy trình bên trong:**
1. Identify execution phases (typically 0: bootstrap, 1: foundation, 2-N: features, +1: hardening)
2. Per phase: enumerate Work Packages
3. Per WP: scope + FR coverage + dependencies + effort + owner role
4. Build dependency graph + critical path
5. Identify risks per WP
6. Self-review

**Output:**
- `docs/02_STRATEGIC/MASTER_PLAN.md`
- `docs/03_EXECUTION/work-packages/PHASE_0_*.md`, ..., `PHASE_N_*.md`

**Hand-off:**
- → `work-package-decomposer` (per WP)
- → `multi-tier-ai-routing` (chính sách phân tier dựa trên WP shape)
- → `ai-operator-protocol` (operator guideline)

**Tips:**
- ⚠️ WP quá lớn (>2 tuần effort) = decompose thêm. WP quá nhỏ (<1 ngày) = merge.
- 💡 Critical path là cảnh báo, không phải mệnh lệnh — dependencies có thể relax được nhưng phải explicit.

---

## 6. PHASE 3 — Execution

Mục tiêu: Build cái đã plan, dùng AI tier routing.

Thứ tự setup: `ai-operator-protocol` → `multi-tier-ai-routing` → `work-package-decomposer` (lặp per WP).

### Skill: `ai-operator-protocol`

**Mục tiêu:** Bộ quy tắc + workflow cho operator quản lý AI executors.

**Khi chạy:** Đầu Phase 3, một lần (file ổn định cho cả phase).

**Inputs:**
- `docs/02_STRATEGIC/MASTER_PLAN.md`
- (Optional) Existing CI/CD pipeline docs

**Prompt mẫu:**
```
Chạy ai-operator-protocol.
Output: docs/03_EXECUTION/AI_OPERATOR_GUIDE.md.

Bao gồm:
- 7 hard rules (vd: "Never auto-merge", "Always run tests", "Block on type errors", ...)
- 14-step workflow per WP execution
- System prompt templates cho Orchestrator / Executor / Reviewer AI
- Escalation rules (when human?)
```

**Output:** `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md`

**Hand-off:**
- → mọi WP execution (operator follow guide)

**Tips:**
- ⚠️ Hard rules tuyệt đối. AI thấy rule đỏ thì dừng, không "judgment call".
- 💡 Customize 7 rules theo project. Skill cho default, không phải cứng.

### Skill: `multi-tier-ai-routing`

**Mục tiêu:** Chính sách phân tier — AI rẻ cho task đơn giản, AI mạnh cho phức tạp, người cho quyết định.

**Khi chạy:** Đầu Phase 3, một lần.

**Inputs:**
- `docs/02_STRATEGIC/MASTER_PLAN.md`
- (Optional) Cost projections, vendor SLAs

**Prompt mẫu:**
```
Chạy multi-tier-ai-routing.
Output: docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md.

4 tiers:
- Tier 1 Simple (Haiku-class): boilerplate, scaffolding, format
- Tier 2 Mid (Sonnet-class): logic implementation, refactor
- Tier 3 Strong (Opus-class): architecture, complex algorithm, security
- Tier Human: ADR change, prod deploy, billing/auth/legal

Cost projections vs all-Tier-3 baseline.
Vendor outage fallback (Anthropic down → fallback to ?).
```

**Output:** `docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md`

**Hand-off:**
- → `work-package-decomposer` (decomposer dùng tier policy này)

**Tips:**
- 💡 Sample 5-10 WP đầu tiên để fine-tune tier mapping. Đừng deploy full mà không test.
- ⚠️ Vendor outage fallback bắt buộc. Single-vendor = single point of failure.

### Skill: `work-package-decomposer`

**Mục tiêu:** Decompose 1 WP thành micro-tasks Tier 1/2/3, mỗi task có prompt + verify command.

**Khi chạy:** Mỗi WP, ngay trước khi assign cho AI executor.

**Inputs:**
- 1 WP cụ thể (`PHASE_X_*.md`)
- `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md`
- `docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md`

**Prompt mẫu:**
```
Chạy work-package-decomposer cho WP-0.E (Error Boundaries).
Đọc spec từ docs/03_EXECUTION/work-packages/PHASE_0_*.md.

Output: docs/03_EXECUTION/work-packages/decomposed/WP-0.E_tasks.md với:
- 10-20 micro-tasks
- Mỗi task: tier (T1/T2/T3/Human), prompt template, verify command, expected diff size
- Dependency graph between tasks
- Total cost estimate

Khớp với routing policy từ AI_AGENT_TASK_DISTRIBUTION.md.
```

**Quy trình bên trong:**
1. Parse WP spec → identify deliverables
2. Decompose into atomic tasks (1 task = 1 file or 1 small change)
3. Assign tier per task (use routing policy)
4. Write prompt template per task
5. Define verify command per task (test, lint, type-check)
6. Build dependency graph
7. Estimate total cost (sum of tier costs × token estimate)
8. Self-review

**Output:** `docs/03_EXECUTION/work-packages/decomposed/<WP-ID>_tasks.md`

**Hand-off:**
- → AI executor (operator dispatch tasks per dependency order)
- → operator dashboard (progress tracking)

**Tips:**
- ⚠️ Verify command bắt buộc per task. Không có verify = không có completion criterion.
- 💡 Tier 1 chiếm 60-70% task = đúng. Nếu Tier 3 chiếm >30% = decompose thêm hoặc routing policy sai.
- 💡 Re-run decomposer khi WP scope đổi. Đừng patch task list.

### CỔNG G3 — Pre-deploy

Sau khi WP hoàn tất, trước go-live:
- [ ] Tất cả tasks completed + verified
- [ ] Test coverage passed
- [ ] Operator review trước deploy
- [ ] Runbook chuẩn bị (xem Phase 4: `incident-response-playbook`)

---

## 7. PHASE 4 — Maintenance (ONGOING)

Phase này không có "endpoint" — chạy định kỳ + theo sự kiện trong toàn vòng đời production.

### Skill: `incident-response-playbook`

**Mục tiêu:** Runbook xử lý sự cố theo NIST IR phases (Preparation / Detection / Containment / Eradication / Recovery / Post-incident).

**Khi chạy:**
- **Trước go-live:** runbook cho mọi failure mode đã biết (DB down, API rate limit hit, queue backlog, disk full, ...)
- **Sau mỗi sự cố:** post-incident review cập nhật runbook

**Inputs:**
- `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` (architecture → failure modes)
- `docs/00_REQUIREMENTS/SRS_VI/M9_NFR.md` (SLAs đã commit)
- (Sau sự cố) timeline + logs

**Prompt mẫu:**
```
Chạy incident-response-playbook cho failure mode "Postgres primary unreachable".
Output: docs/04_MAINTENANCE/runbooks/INCIDENT_postgres_primary_down.md.

6 NIST IR phases:
1. Preparation: monitoring, alerts, on-call rotation
2. Detection: signal patterns
3. Containment: cut blast radius (failover steps)
4. Eradication: root cause fix
5. Recovery: validate + reopen traffic
6. Post-incident: timeline + lessons + action items

Severity: P0. SLA per M9: RTO 15 min, RPO 5 min.
Step-by-step commands for on-call engineer.
```

**Output:** `docs/04_MAINTENANCE/runbooks/INCIDENT_<id>.md` (1 file per failure mode)

**Hand-off:**
- → on-call rotation (immediate use)
- → quarterly drill (test runbooks)

**Tips:**
- ⚠️ Step-by-step commands. "Failover the database" không đủ — phải `pg_promote_replica.sh` cụ thể.
- 💡 Mỗi runbook test bằng tabletop exercise trước khi cần thật.

### Skill: `feature-extension-planning`

**Mục tiêu:** Mini-SRS + plan cho feature mới sau go-live.

**Khi chạy:** Mỗi feature/extension request.

**Inputs:**
- Feature request (1-pager hoặc ticket)
- Existing SRS (M1-M10) để check compatibility
- `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` (architecture constraint)

**Prompt mẫu:**
```
Chạy feature-extension-planning cho FEAT-042 "Bulk Customer Export".
Output: docs/04_MAINTENANCE/feature-extensions/FEAT-042_bulk_export.md.

Sections:
- Why (business case, lite version of feasibility)
- What (FR additions, NFR delta)
- How (architecture impact, ADR if breaks design)
- When (effort estimate, dependencies)
- Open questions
- Hand-off to Phase 3 work-package-decomposer.

Cite existing FRs nó touch + flag breaking changes.
```

**Output:** `docs/04_MAINTENANCE/feature-extensions/FEAT_<id>_<slug>.md`

**Hand-off:**
- Nếu feature lớn → mini-feasibility + lại đi qua workflow Phase 2-3
- Nếu nhỏ → trực tiếp sang `work-package-decomposer`

**Tips:**
- ⚠️ Đừng skip "Why". Feature without clear business case = scope creep.
- 💡 Breaking change → cần ADR mới cập nhật TECH_SOLUTION_DESIGN.

### Skill: `documentation-sync`

**Mục tiêu:** Audit doc-vs-code drift hàng tháng.

**Khi chạy:** Định kỳ hàng tháng.

**Inputs:**
- All docs in `docs/`
- Current codebase state

**Prompt mẫu:**
```
Chạy documentation-sync.
Output: docs/04_MAINTENANCE/DOC_SYNC_REPORT.md (overwrite, archive trước).

Detect:
- FR cite hàm mà code đã rename
- API path trong docs vs router thực tế
- Schema doc vs migration files
- Version mismatch (doc bảo Postgres v15, code v16)
- Broken cross-references

Severity: Critical / High / Medium / Low.
Mỗi finding: doc:line + code:line + recommendation.
```

**Output:** `docs/04_MAINTENANCE/DOC_SYNC_REPORT.md` (mới mỗi lần) + archive cũ

**Hand-off:**
- → operator (action items)
- → `feature-extension-planning` nếu drift do feature đã ship nhưng chưa update doc

**Tips:**
- ⚠️ Drift tích lũy nguy hiểm hơn drift cấp tốc. Hàng tháng > hàng năm.
- 💡 Tích hợp vào CI: chạy quick doc-sync mỗi PR (chỉ scan files PR touch).

---

## 8. CROSS-CUTTING — Chèn vào bất kỳ phase nào

### Skill: `document-index-master`

**Mục tiêu:** Tạo `INDEX.md` master nav cho dự án.

**Khi chạy:**
- Lần đầu: cuối Phase 0 (đã có SRS), hoặc sau Phase 1 (legacy)
- Refresh: sau mỗi phase major hoặc khi cấu trúc docs đổi

**Prompt mẫu:**
```
Chạy document-index-master.
Output: INDEX.md (root project, NOT docs/).

8 sections per template:
1. Project elevator pitch
2. Current phase + status
3. Quick links (most-used docs)
4. Phase navigation (P0-P4)
5. Cross-cutting docs
6. Last updated dates per major doc
7. Owner directory
8. How to contribute / PR process
```

**Output:** `INDEX.md` (root)

**Tips:**
- 💡 INDEX.md đầu tiên người mới đọc — cập nhật sau mọi phase change.

### Skill: `document-consistency-review`

**Mục tiêu:** Audit doc-vs-doc inconsistency theo 8 chiều (Terminology, Numbers, References, Versioning, Owners, Decisions, Status, Glossary).

**Khi chạy:** Quý 1 lần. Hoặc trước milestone audit.

**Prompt mẫu:**
```
Chạy document-consistency-review Mode A (8 dimensions).
Output: docs/04_MAINTENANCE/CONSISTENCY_REVIEW_REPORT.md.

Report cấu trúc:
- Executive summary
- Findings per dimension với severity
- Terminology audit (special section)
- Reference validity check
- Version + status consistency
- Decision reflection
- Action items
- Patterns + systemic findings

Compare vs prior run nếu có.
```

**Output:** `docs/04_MAINTENANCE/CONSISTENCY_REVIEW_REPORT.md`

**Tips:**
- ⚠️ Khác `documentation-sync`: skill này doc-vs-doc, không phải doc-vs-code.
- 💡 Combined report option: chạy cùng `documentation-sync` cho health check toàn diện.

---

## 9. Pipeline cho 3 use cases điển hình

### 9.1 LEGACY full audit (5 tuần)

```
Tuần 1: project-context-ingestion
        → CONTEXT_PACK.md
        → STAKEHOLDER MEETING resolve top contradictions

Tuần 1: codebase-discovery (parallel)
        → CODEBASE_MAP.md
Tuần 2: data-architecture-audit
        → DATA_ARCHITECTURE.md
Tuần 2: business-context-capture
        → BUSINESS_CONTEXT.md
Tuần 3: tech-debt-audit
        → TECH_DEBT_AUDIT.md

Tuần 4: srs-reverse-engineer
        → M1-M8 SRS
Tuần 4: nfr-specification
        → M9
Tuần 5: requirements-traceability
        → M10
Tuần 5: document-index-master
        → INDEX.md
```

**Stop point:** Cuối tuần 5. Có thể audit, handover, hoặc decide rewrite.

### 9.2 GREENFIELD full lifecycle (5 tuần planning + N tuần execution)

```
Tuần 1: project-context-ingestion → CONTEXT_PACK.md
        → STAKEHOLDER MEETING

Tuần 2: srs-greenfield-author → M1-M8
Tuần 2: nfr-specification → M9
Tuần 3: feasibility-assessment → FEASIBILITY.md
        ⚠️ G1: Stakeholder choose scenario

Tuần 4: tech-solution-design → TECH_SOLUTION.md
        ⚠️ G2: Architecture approval

Tuần 5: implementation-planning → MASTER_PLAN + WPs
Tuần 5: ai-operator-protocol → AI_OPERATOR_GUIDE.md
Tuần 5: multi-tier-ai-routing → AI_TASK_DISTRIBUTION.md
Tuần 5: requirements-traceability → M10
Tuần 5: document-index-master → INDEX.md

Tuần 6+: work-package-decomposer (per WP, lặp)
        → execute WPs
        ⚠️ G3 cho mỗi WP

Sau go-live: chuyển sang Phase 4
```

### 9.3 LIVING product (ongoing)

```
Hàng tháng: documentation-sync → DOC_SYNC_REPORT
Hàng quý:   document-consistency-review → CONSISTENCY_REVIEW_REPORT

Per feature: feature-extension-planning → FEAT_*.md
             → (nếu lớn) work-package-decomposer → execute
             → (nếu nhỏ) trực tiếp execute với operator guide

Per failure mode: incident-response-playbook → INCIDENT_*.md
                  (chuẩn bị trước, không phải sau)

Per pivot/rewrite: quay lại Pre-Phase 0 với re-ingestion
```

---

## 10. Anti-patterns (sai lầm hay gặp)

### 10.1 Pipeline qua quyết định gate

❌ "Chạy tự động từ Phase 0 đến hết Phase 3, khỏi cần stakeholder."

→ Cổng G1, G2, G3 bắt buộc dừng. AI không thay người trong quyết định kinh doanh.

### 10.2 Skip Pre-Phase 0

❌ "Chỉ có code, đủ rồi, vào srs-reverse-engineer luôn."

→ SRS sinh ra chỉ có WHAT, không có WHY. Sau này stakeholder sẽ challenge từng FR. Mất time gấp đôi.

### 10.3 Phase 1 cho greenfield

❌ "Greenfield mà chạy codebase-discovery cho đẹp."

→ Vô nghĩa. Không có code thì map cái gì? Bỏ qua Phase 1.

### 10.4 Run Phase 4 quá sớm

❌ "Chưa go-live nhưng chạy documentation-sync."

→ Doc-vs-code drift trước khi production stable = noise. Đợi go-live ≥1 tháng.

### 10.5 All-tier-3 routing

❌ "Dùng Opus cho mọi task vì chất lượng cao."

→ Cost gấp 8-10x. Tier 1 cho boilerplate đủ tốt. Routing exists for a reason.

### 10.6 Skip decomposer

❌ "WP có spec rồi, AI executor đọc thẳng, khỏi decompose."

→ AI mất context khi WP >2 ngày effort. Decompose = bảo hiểm chất lượng + cost.

### 10.7 Runbook sau sự cố

❌ "Chờ có sự cố rồi mới viết runbook."

→ Sự cố P0 lúc 2h sáng — on-call có 15 phút. Không có runbook = thảm họa. Viết TRƯỚC.

### 10.8 Đo "completion %" thay vì "quality"

❌ "Chạy 18/19 skills xong rồi, dự án done."

→ Skills chạy không có nghĩa output đạt. Mỗi skill có `references/checklist.md` — đó mới là gate thật.

---

## 11. Gợi ý tracking

Cho mỗi dự án, maintain 1 file ở root: `PROGRESS.md` với bảng:

```markdown
| Phase | Skill | Run date | Output | Checklist passed | Notes |
|-------|-------|----------|--------|-------------------|-------|
| Pre-P0 | project-context-ingestion | 2026-04-12 | CONTEXT_PACK.md | ✅ | 17 sources, 6/6 categories |
| P1 | codebase-discovery | 2026-04-15 | CODEBASE_MAP.md | ✅ | |
| P1 | data-architecture-audit | 2026-04-16 | DATA_ARCHITECTURE.md | ✅ | |
| P1 | business-context-capture | 2026-04-18 | BUSINESS_CONTEXT.md | ⏳ | re-running with CONTEXT_PACK |
| P1 | tech-debt-audit | — | — | — | blocked |
| P0 | srs-reverse-engineer | — | — | — | needs P1 done |
| ... | ... | ... | ... | ... | ... |
```

Đủ để stakeholder + auditor tracking.

---

## 12. Câu hỏi thường gặp

### Q: Thứ tự skills trong 1 phase có cứng không?

Một phần. Trong Phase 1: `codebase-discovery` → `data-arch-audit` → `business-context-capture` → `tech-debt-audit` là khuyến nghị. Có thể swap 2-3 với 4 nếu hiểu lý do, nhưng đừng đảo ngược.

Trong Phase 0: bắt buộc có thứ tự M1-M8 → M9 → M10. Trong Phase 2: cứng (feasibility → solution → planning).

### Q: Có skill nào chạy parallel được không?

Có. Trong Phase 1, `codebase-discovery` + `data-architecture-audit` có thể parallel (2 AI agents khác). Phase 4 maintenance skills hoàn toàn parallel.

Trong Phase 0/2: sequential, vì output trước feed vào sau.

### Q: 1 skill chạy bao lâu?

Phụ thuộc input size + AI tier:
- Phase 1 skills (mỗi cái): 1-3 giờ AI work + 1-2 giờ operator review cho dự án trung bình
- SRS skills: 4-8 giờ (lớn nhất)
- Feasibility / Solution: 3-5 giờ + stakeholder time
- Decomposer: 30 phút - 2 giờ per WP
- Maintenance skills: 30 phút - 1 giờ

Operator overhead ~30-50% AI work time.

### Q: Skill output cần gì để "pass"?

`references/checklist.md` của skill đó. Nếu pass tất cả gate = output đạt minimum. Quality cao cần thêm stakeholder validation.

### Q: Khi nào cần re-run skill?

- Pre-P0: stakeholder change, regulation new
- Phase 1: mỗi quarter (refresh) hoặc sau major refactor
- Phase 0: khi feature scope đổi đáng kể
- Phase 2: chỉ khi pivot / rewrite
- Phase 3 decomposer: per WP (luôn fresh)
- Phase 4: định kỳ (đã nói)

---

## 13. Tham khảo

- [INDEX.md](INDEX.md) — bản đồ skills
- [GETTING_STARTED.md](GETTING_STARTED.md) — overview + giá trị
- Mỗi `<phase>/<skill>/SKILL.md` — chi tiết quy trình
- Mỗi `<phase>/<skill>/references/checklist.md` — quality gates
- Mỗi `<phase>/<skill>/references/examples.md` — ví dụ thực tế

---

*Workflow là hướng dẫn, không phải mệnh lệnh. Khi tình huống dự án đặc biệt, judgment > recipe. Nhưng nếu vừa bắt đầu — follow recipe trước, customize sau.*
