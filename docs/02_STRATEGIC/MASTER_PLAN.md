# MASTER_PLAN — Hệ thống Tính Thực Chạy

> **Skill:** `implementation-planning` | **Trạng thái:** 🟢 Complete
> **Ngày tạo:** 2026-05-12 | **Phiên bản:** v1.0

---

## 1. Plan Overview

### Mục tiêu

Dự án **ABM_Data_ThucChay** đang ở giai đoạn **Vận hành Ổn định (Steady-State Operations)** — hệ thống đang chạy production hàng ngày. Master Plan này tập trung vào **3 mục tiêu song song**:

| Mục tiêu | Mô tả | Timeline |
|----------|-------|---------|
| **A. Tài liệu hóa toàn diện** | Hoàn thiện bộ docs Phase 0→4 theo Company-Skill framework | Q2/2026 |
| **B. Giải quyết Tech Debt P1** | Fix TD-004 (Error Handling), lộ trình TD-001 (FK cứng) | Q2-Q3/2026 |
| **C. Monitoring & Observability** | Cải thiện khả năng giám sát Job và phát hiện sự cố sớm | Q3/2026 |

### Nguyên tắc

- **No breaking changes on live system** — mọi thay đổi phải có rollback plan
- **Documentation first** — không fix tech debt khi chưa có tài liệu đầy đủ
- **Incremental improvement** — từng bước nhỏ, verify sau mỗi bước

---

## 2. Phases

### Phase A — Documentation (Tài liệu hóa)

**Mục tiêu:** Hoàn thiện 100% bộ tài liệu theo Company-Skill framework
**Timeline:** Q2/2026 (2-3 tuần)
**Owner:** AI Agent + Tech Lead review

#### Trạng thái hiện tại (khi lập plan)

| Tài liệu | Trạng thái |
|----------|------------|
| SRS M1-M10 | 🟢 Done |
| BUSINESS_CONTEXT.md | 🟢 Done |
| CODEBASE_MAP.md | 🟢 Done |
| DATA_ARCHITECTURE.md | 🟢 Done |
| TECH_DEBT_AUDIT.md | 🟢 Done |
| FEASIBILITY_ASSESSMENT.md | 🟢 Done |
| TECH_SOLUTION_DESIGN.md | 🟢 Done |
| **MASTER_PLAN.md** (tài liệu này) | 🟢 Done |
| AI_OPERATOR_GUIDE.md | 🔴 Cần hoàn thiện |
| AI_AGENT_TASK_DISTRIBUTION.md | 🔴 Cần hoàn thiện |
| Runbooks (3 loại incident) | 🔴 Chưa có |
| DOC_SYNC_REPORT.md | 🔴 Cần hoàn thiện |
| INDEX.md (cập nhật status) | 🔴 Cần cập nhật |

#### Work Packages Phase A

| WP | Tên | Output | Effort | Tier |
|----|-----|--------|--------|------|
| WP-A01 | AI Operator Guide | `03_EXECUTION/AI_OPERATOR_GUIDE.md` | S | T2 |
| WP-A02 | AI Task Distribution | `03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md` | S | T2 |
| WP-A03 | Runbook: Job Failure | `04_MAINTENANCE/runbooks/INCIDENT_JOB_FAILURE.md` | M | T2 |
| WP-A04 | Runbook: Wrong Revenue | `04_MAINTENANCE/runbooks/INCIDENT_WRONG_REVENUE.md` | M | T2 |
| WP-A05 | Runbook: Data Sync Fail | `04_MAINTENANCE/runbooks/INCIDENT_DATA_SYNC_FAIL.md` | M | T2 |
| WP-A06 | DOC_SYNC_REPORT update | `04_MAINTENANCE/DOC_SYNC_REPORT.md` | S | T1 |
| WP-A07 | INDEX.md refresh | `docs/INDEX.md` | S | T1 |

---

### Phase B — Tech Debt Resolution (Giải quyết Nợ Kỹ thuật)

**Mục tiêu:** Xử lý TD-004 (dễ) và lập lộ trình TD-001 (khó)
**Timeline:** Q2-Q3/2026 (4-8 tuần)
**Owner:** Developer + DBA

#### Work Packages Phase B

| WP | Tên | Mô tả | Effort | Risk | Prerequisite |
|----|-----|-------|--------|------|-------------|
| WP-B01 | TD-004: Standardize Error Handling | Thêm TRY-CATCH + RAISERROR logging vào các SP tính chính | S | Low | Phase A done |
| WP-B02 | Audit Orphan Records | Script kiểm tra orphan records trong ThucChayDaTinh → HopDongChiTiet | S | Low | Phase A done |
| WP-B03 | TD-001: Data Cleanup | Dọn sạch orphan records phát hiện ở WP-B02 | M | Medium | WP-B02 done |
| WP-B04 | TD-001: FK Plan Design | Thiết kế chi tiết FK cho core tables | M | Low | WP-B02 done |
| WP-B05 | TD-001: FK Implementation | Add FK constraints theo rolling (từng bảng) | L | High | WP-B03 + WP-B04 done |

#### Thứ tự thực hiện Phase B

```
WP-B01 (Error Handling) ─── có thể chạy song song với B02
WP-B02 (Audit Orphan)
    └──► WP-B03 (Data Cleanup)
             └──► WP-B05 (FK Implementation)
WP-B04 (FK Design) ─────────────────────────────► WP-B05
```

---

### Phase C — Monitoring & Observability

**Mục tiêu:** Cải thiện khả năng phát hiện sự cố sớm
**Timeline:** Q3/2026 (4-6 tuần)
**Owner:** Developer + DBA + Ops Team

#### Work Packages Phase C

| WP | Tên | Mô tả | Effort | Priority |
|----|-----|-------|--------|---------|
| WP-C01 | Job Execution Dashboard | Xây dựng view/report theo dõi trạng thái tất cả Jobs theo ngày | M | High |
| WP-C02 | Revenue Anomaly Detection | SP tự động phát hiện bất thường doanh số (vượt phân bổ, âm, null) | M | High |
| WP-C03 | Job Run History Table | Bảng lưu lịch sử chạy Job với duration, status, error message | S | Medium |
| WP-C04 | SLA Monitoring | Alert khi Job chính chưa hoàn thành trước 08:30 AM | M | Medium |

---

## 3. Work Package Details

### WP-A01: AI Operator Guide
- **Input:** Toàn bộ tài liệu Phase 0-2 đã hoàn thành
- **Output:** `03_EXECUTION/AI_OPERATOR_GUIDE.md` — Hướng dẫn đầy đủ cho AI agent và operator
- **Acceptance criteria:**
  - [ ] Bao gồm quy tắc routing theo loại câu hỏi
  - [ ] Bao gồm escalation rules
  - [ ] Bao gồm checklist trước khi trả lời

### WP-A03: Runbook — Job Failure
- **Input:** `context/01_JOBS_AND_STEPS.md`, email alert logs
- **Output:** Playbook xử lý khi SQL Agent Job fail
- **Acceptance criteria:**
  - [ ] Triệu chứng nhận biết rõ ràng
  - [ ] Quy trình triage trong 30 phút
  - [ ] Escalation path nếu không tự xử lý được

### WP-A04: Runbook — Wrong Revenue
- **Input:** `docs/Logic_nghiepvu_tinh_thucchay.md`, SRS M3-M8
- **Output:** Playbook xử lý khi doanh số tính sai
- **Acceptance criteria:**
  - [ ] Phân biệt được "sai logic" vs "sai dữ liệu nguồn"
  - [ ] Các query cụ thể để xác định nguồn gốc sai lệch
  - [ ] Quy trình tính lại an toàn (job_TinhLaiThucChay)

### WP-B01: Standardize Error Handling
- **Input:** Danh sách SP tính chính (11 SP theo Job steps)
- **Output:** 11 SPs được wrap TRY-CATCH + log error ra table/RAISERROR
- **Acceptance criteria:**
  - [ ] Mọi SP tính toán có TRY-CATCH
  - [ ] Error message chứa: SP name, parameters, error code, timestamp
  - [ ] Không thay đổi logic tính toán

---

## 4. Timeline Tổng thể

```
2026-Q2 (Tháng 5-6):
  ├─ WP-A01 → WP-A07 (Phase A Documentation) ─── 2-3 tuần
  └─ WP-B01 (Error Handling) ─────────────────── song song với A

2026-Q2/Q3 (Tháng 6-7):
  ├─ WP-B02 (Audit Orphan) ──────────────────── 1 tuần
  └─ WP-C01, WP-C03 (Quick wins Monitoring) ─── 1-2 tuần

2026-Q3 (Tháng 7-9):
  ├─ WP-B03 + WP-B04 (FK Design) ─────────────── 2-3 tuần
  ├─ WP-C02, WP-C04 (Monitoring nâng cao) ─────── 2 tuần
  └─ WP-B05 (FK Implementation — rolling) ──────── 4-6 tuần
```

---

## 5. Governance

### Review Gates

| Gate | Điều kiện | Approver |
|------|----------|---------|
| G-A | Phase A Documentation 100% done | Tech Lead |
| G-B1 | Audit Orphan report được review | Tech Lead + DBA |
| G-B2 | FK Design được review và approve | Tech Lead + DBA + Business Analyst |
| G-C | Monitoring dashboard live | Ops Team + Tech Lead |

### Rủi ro và mitigation

| Rủi ro | Xác suất | Mitigation |
|--------|---------|-----------|
| Orphan records nhiều hơn dự kiến (WP-B02) | Cao | Cleanup plan trước khi add FK |
| FK gây break SP đang chạy (WP-B05) | Trung bình | Staging test environment + rollback script |
| Documentation drift sau khi deploy | Cao | Monthly doc-sync theo DOC_SYNC_REPORT |

---

## 6. Ghi chú & Caveats

- **Dự án này là legacy** — ưu tiên không gây gián đoạn vận hành hàng ngày
- **Phase A là prerequisite bắt buộc** trước khi làm bất kỳ tech debt nào
- **WP-B05 (FK)** chỉ thực hiện sau khi có stakeholder approval tại Gate G-B2
