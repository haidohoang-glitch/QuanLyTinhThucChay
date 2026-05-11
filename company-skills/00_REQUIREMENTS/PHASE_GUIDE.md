# Phase 0 — Requirements: Hướng dẫn vận hành

> **Tài liệu này dành cho:** Operator + tech lead + AI agent vận hành Phase 0 — chạy từng skill riêng lẻ HOẶC chạy cả cụm qua orchestrator.
>
> **Tham khảo:**
> - [phase-0-orchestrator/SKILL.md](phase-0-orchestrator/SKILL.md) — orchestrator skill
> - [phase-0-orchestrator/references/runbook.md](phase-0-orchestrator/references/runbook.md) — worked examples
> - [../WORKFLOW_GUIDE.md](../WORKFLOW_GUIDE.md) — toàn bộ workflow Pre-P0 → P4

---

## 1. Mục tiêu Phase 0

Sản xuất bộ tài liệu **Requirements chính thức** cho dự án — đủ điều kiện audit, đủ điều kiện stakeholder approval, đủ điều kiện đưa vào Phase 2 Strategic.

**Output cuối Phase 0:**
- `docs/00_REQUIREMENTS/CONTEXT_PACK.md` (+ `_sources/`)
- `docs/00_REQUIREMENTS/SRS_VI/M1_Introduction.md`
- `docs/00_REQUIREMENTS/SRS_VI/M2_Overall_Description.md`
- `docs/00_REQUIREMENTS/SRS_VI/M3-Mx_<Domain>.md` (4-6 file functional)
- `docs/00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md`
- `docs/00_REQUIREMENTS/SRS_VI/M10_RTM_Issues_Appendix.md`

---

## 2. Skills trong Phase 0

| # | Skill | Vai trò | Bắt buộc? |
|---|-------|---------|-----------|
| 0 | `project-context-ingestion` | Pre-P0: ingest raw materials → CONTEXT_PACK | Khuyên rất mạnh (skip = SRS sai chiều) |
| 1A | `srs-greenfield-author` | Author SRS từ vision (cho greenfield) | Bắt buộc nếu greenfield |
| 1B | `srs-reverse-engineer` | Reverse-engineer SRS từ code (cho legacy) | Bắt buộc nếu legacy |
| 2 | `nfr-specification` | Đặc tả M9 NFR | Bắt buộc |
| 3 | `requirements-traceability` | M10 RTM + Issues + Appendix | Bắt buộc |

**Orchestrator:** [`phase-0-requirements-orchestrator`](phase-0-orchestrator/) — chạy cả cụm tuần tự với checkpoints.

---

## 3. Hai cách vận hành

### 3.1 Cách A — Chạy từng skill riêng lẻ (khi nào)

Dùng khi:
- Chỉ cần update 1 phần (ví dụ refresh M9 NFR sau khi có regulatory mới)
- Đang debug 1 skill, muốn rerun nhỏ
- Operator muốn kiểm soát chi tiết từng bước

**Prompt mẫu (chạy 1 skill):**
```
Chạy skill nfr-specification cho project Pegasus.
Inputs:
- docs/00_REQUIREMENTS/SRS_VI/M1-M8 (đã có)
- docs/00_REQUIREMENTS/CONTEXT_PACK.md Section 7.1
Output: overwrite docs/00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md
Archive bản cũ trước.
Sau khi xong, chạy references/checklist.md.
```

### 3.2 Cách B — Chạy cả cụm qua orchestrator (khi nào)

Dùng khi:
- Khởi động dự án mới (lần đầu chạy Phase 0)
- Refresh toàn bộ Phase 0 sau pivot
- Audit prep (cần đảm bảo mọi skill cập nhật)

**Prompt mẫu (chạy orchestrator):**
```
Chạy phase-0-requirements-orchestrator cho project Pegasus.
Mode A Supervised.
Inputs raw materials ở _handover/.
Output đến docs/00_REQUIREMENTS/.
Pause sau mỗi step để tôi review.
```

Orchestrator sẽ tự:
1. Pre-flight check (greenfield/legacy detection)
2. Run Step 1 (project-context-ingestion) → pause
3. Run Step 2 (SRS skill phù hợp) → pause
4. Run Step 3 (nfr-specification) → pause
5. Run Step 4 (requirements-traceability) → pause
6. Generate phase report

---

## 4. Lưu ý đặc biệt cho Phase 0

### 4.1 Greenfield vs Legacy — orchestrator tự detect

- **Greenfield (chưa có code):** Skip Phase 1, chạy `srs-greenfield-author`
- **Legacy (có code):** **Phải chạy Phase 1 TRƯỚC** rồi mới chạy `srs-reverse-engineer`

Nếu legacy mà chưa có Phase 1 docs → orchestrator sẽ ABORT với hướng dẫn rõ ràng.

### 4.2 CONTEXT_PACK là input-quyết-định-chiều

Nếu skip `project-context-ingestion`:
- ❌ SRS sẽ chỉ phản ánh code (legacy) hoặc giả định operator (greenfield)
- ❌ Không có dấu vết tới stakeholder voice
- ❌ M10 Open Questions sẽ trống hoặc invented

→ **Đừng skip Pre-P0** trừ khi operator chấp nhận degraded quality.

### 4.3 Mode A Supervised mặc định, KHÔNG chuyển B Express dễ dãi

Phase 0 output là audit-grade. Mode B Express hợp lý cho:
- Refresh sau khi đã có baseline
- Internal draft, không show stakeholder

KHÔNG hợp lý cho:
- Lần đầu của dự án
- Audit prep
- Sau pivot lớn

---

## 5. Quality gate cuối Phase 0

Trước khi vào Phase 2:

- [ ] M1-M10 đầy đủ (không placeholder ngoài M9/M10 nội dung sinh)
- [ ] Mỗi FR cite source ([SRC-NNN] hoặc file:line cho legacy)
- [ ] M9 NFR mỗi cái có target value + measurement + source
- [ ] M10 RTM có FR-ID + test refs (hoặc "GAP" marker rõ ràng)
- [ ] Open Questions từ CONTEXT_PACK Section 12 đã review với stakeholder
- [ ] Phase report `_phase_report_<DATE>.md` generated

Nếu chưa pass → **DỪNG, fix trước khi vào Phase 2**.

---

## 6. Cadence vận hành

| Cadence | Hoạt động |
|---------|-----------|
| **Lần đầu** | Run orchestrator full pipeline |
| **Mỗi feature lớn (>10% SRS)** | Re-run partial: SRS + RTM (qua Mode C Selective) |
| **Sau stakeholder pivot** | Re-run từ Pre-P0 (cascade) |
| **Hàng quý** | Spot-check: chạy `documentation-sync` để detect drift M1-M10 vs code |
| **Trước audit** | Re-run orchestrator full hoặc partial tùy framework |

---

## 7. Common pitfalls

### 7.1 Skip Pre-P0 vì "có code rồi đủ"

**Hậu quả:** SRS reverse-engineer sẽ chỉ ghi WHAT, không có WHY. Stakeholder sau này sẽ challenge từng FR.

**Tránh:** Luôn chạy `project-context-ingestion` ít nhất 1 lần, dù raw materials có ít.

### 7.2 SRS có "should be user-friendly"

**Hậu quả:** Không testable. Audit reject. Operator phải viết lại sau.

**Tránh:** Mỗi FR phải có observable success/failure criteria. Nếu không đo được, không phải FR.

### 7.3 Mọi FR đều "Must" priority

**Hậu quả:** Không có ưu tiên thực sự. Phase 2 feasibility không có gì để cắt.

**Tránh:** Force MoSCoW: 30-50% Must, 30-40% Should, rest Could/Won't.

### 7.4 M10 Open Questions trống

**Hậu quả:** AI/operator giả vờ biết hết. Stakeholder phát hiện sau, mất thời gian fix.

**Tránh:** Open Questions trống = suspicious. Mọi project đều có ambiguity. Capture nó.

### 7.5 Skip M9 NFR vì "sẽ làm sau"

**Hậu quả:** Phase 2 tech-solution-design không có constraints; ADR sai. Phase 3 build sai performance/security.

**Tránh:** M9 bắt buộc trước Phase 2. Có thể minimal nhưng không skip.

---

## 8. Hand-off ra Phase 1/2

### Sau khi Phase 0 complete:

| Output | Đi tới |
|--------|--------|
| CONTEXT_PACK.md | Phase 1 (BUSINESS_CONTEXT validation) + Phase 2 (FEASIBILITY constraints) |
| SRS M1-M8 | Phase 2 (FEASIBILITY scope baseline) |
| M9 NFR | Phase 2 (TECH_SOLUTION_DESIGN constraints) |
| M10 RTM | Phase 3 (test plans), audit prep |
| Open Questions | Stakeholder meetings |

### Cập nhật INDEX.md

Sau Phase 0:
- Chạy `document-index-master` để refresh INDEX.md
- INDEX.md có quick links tới M1-M10 chính

---

## 9. Time + cost (ước tính)

| Mode | AI work | Operator | Elapsed | Cost |
|------|---------|----------|---------|------|
| Mode A Supervised | 6-8 hr | 2-4 hr | 2-3 ngày | ~$15-25 |
| Mode B Express | 3-5 hr | 0.5-1 hr | <1 ngày | ~$10-18 |
| Mode C Selective (1 skill) | 0.5-2 hr | 15-30 min | <2 hr | ~$2-5 |

Plus stakeholder time cho Open Questions (variable, không tính ở đây).

---

## 10. FAQ Phase 0

**Q: Có thể skip CONTEXT_PACK nếu chỉ có 2 sources không?**
→ Có thể chạy với 2 sources. Pack sẽ tự đánh dấu LOW confidence. Section 9 (Gaps) sẽ list missing categories. Đó là honest, không phải failure.

**Q: SRS phải tiếng Việt hay tiếng Anh?**
→ Output ngôn ngữ tùy yêu cầu. Mặc định template tiếng Anh; AI có thể sinh tiếng Việt. Folder name `SRS_VI` là quy ước "Vietnamese SRS" — đổi tên nếu dùng tiếng khác.

**Q: Bao nhiêu functional domain (M3-Mx) là phù hợp?**
→ 4-8. Dưới 4 = under-decomposed. Trên 8 = over-decomposed (gộp lại).

**Q: M9 NFR phải có bao nhiêu NFR?**
→ Tùy domain, thường 15-30 NFRs phân bổ trên 7 categories. Quá ít = thiếu rigor. Quá nhiều = vô thực thi.

**Q: Audit yêu cầu Mã FR theo định dạng khác (ví dụ REQ-001 thay vì FR-AUTH-04)?**
→ Mode B (Honor company template) hoặc Mode C (User-defined). Tell skill ở step 2.
