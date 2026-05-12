# DOC_SYNC_REPORT — Hệ thống Tính Thực Chạy

> **Skill:** `documentation-sync` | **Trạng thái:** 🟢 Complete
> **Ngày tạo:** 2026-05-12 | **Phiên bản:** v1.0

---

## Lần kiểm tra gần nhất

| Thuộc tính | Giá trị |
|------------|---------|
| **Ngày kiểm tra** | 2026-05-12 |
| **Người thực hiện** | AI Agent (T2) |
| **Drift detected** | Không (Phase A documentation vừa hoàn thành) |
| **Files cần cập nhật** | Không |

---

## Trạng thái tài liệu hiện tại (Baseline 2026-05-12)

| Tài liệu | Trạng thái | Ngày cập nhật cuối |
|----------|------------|-------------------|
| `context/01_JOBS_AND_STEPS.md` | 🟢 Sync | 2026-05-08 |
| `context/02_DM_SANPHAM.md` | 🟢 Sync | 2026-05-08 |
| `context/03_SP_LIST.md` | 🟢 Sync | 2026-05-08 |
| `context/04_JOB_DESC.md` | 🟢 Sync | 2026-05-08 |
| `context/05_TABLE_DESC.md` | 🟢 Sync | 2026-05-08 |
| `context/06_DATA_ARCHITECTURE.md` | 🟢 Sync | 2026-05-08 |
| `docs/01_DISCOVERY/BUSINESS_CONTEXT.md` | 🟢 Sync | 2026-05-08 |
| `docs/01_DISCOVERY/CODEBASE_MAP.md` | 🟢 Sync | 2026-05-08 |
| `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` | 🟢 Sync | 2026-05-08 |
| `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md` | 🟢 Sync | 2026-05-08 |
| `docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md` | 🟢 Sync | 2026-05-12 |
| `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` | 🟢 Sync | 2026-05-12 |
| `docs/02_STRATEGIC/MASTER_PLAN.md` | 🟢 Sync | 2026-05-12 |
| `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md` | 🟢 Sync | 2026-05-12 |
| `docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md` | 🟢 Sync | 2026-05-12 |
| `docs/04_MAINTENANCE/runbooks/INCIDENT_JOB_FAILURE.md` | 🟢 Sync | 2026-05-12 |
| `docs/04_MAINTENANCE/runbooks/INCIDENT_WRONG_REVENUE.md` | 🟢 Sync | 2026-05-12 |
| `docs/04_MAINTENANCE/runbooks/INCIDENT_DATA_SYNC_FAIL.md` | 🟢 Sync | 2026-05-12 |
| `docs/00_REQUIREMENTS/SRS_VI/M1_INTRODUCTION.md` | 🟢 Sync | 2026-05-08 |
| `docs/00_REQUIREMENTS/SRS_VI/M3-M8_FUNCTIONAL_REQUIREMENTS.md` | 🟢 Sync | 2026-05-08 |
| `docs/00_REQUIREMENTS/SRS_VI/M9_NFR.md` | 🟢 Sync | 2026-05-08 |
| `docs/00_REQUIREMENTS/SRS_VI/M10_TRACEABILITY.md` | 🟡 Có open issues | 2026-05-08 |

---

## Quy trình Đồng bộ

### Scripts auto-gen (chạy theo thứ tự)

```
1. python generate_sp_flow_mssql.py    → Cập nhật FLOW_*.md
2. python generate_sp_from_mssql.py    → Cập nhật SP_*.md (SPs trong luồng)
3. python generate_md_from_mssql.py    → Cập nhật tables/*.md
4. python generate_context_for_ai.py   → Cập nhật context/01, 02, 03
5. python generate_job_table_desc.py   → Cập nhật context/04, 05
6. python generate_data_architecture_audit.py → Cập nhật context/06
```

### Tần suất khuyến nghị

| Khi nào | Scripts cần chạy |
|---------|-----------------|
| Thêm/sửa SP | 1 + 2 |
| Thêm/sửa Table | 3 |
| Thay đổi Job | 4 |
| Cập nhật mô tả (desc) | 5 + 6 |
| Review định kỳ (hàng tháng) | Tất cả |

---

## Incident Log (Lịch sử sự cố)

| Ngày | Sự cố | Nguyên nhân | Thời gian xử lý | Kết quả |
|------|-------|------------|----------------|---------|
| _(chưa có sự cố ghi nhận)_ | | | | |

---

## Open Issues từ M10_TRACEABILITY

| ID | Mô tả | Trạng thái |
|----|-------|-----------|
| ISS-01 | Cần xác nhận logic tính cho nhóm Mobile edge cases | 🟡 Pending |
| ISS-02 | Cần xác nhận scope GGFB sản lượng chốt | 🟡 Pending |
| ISS-03 | Review anti-overcap logic CPM đơn vị gói | 🟡 Pending |
| ISS-04 | Clarify offset logic khi phân bổ bị gán lại | 🟡 Pending |

> ⚠️ Các open issues trên cần xác nhận với Stakeholders trước khi thực hiện thay đổi logic lớn.

---

## Lịch Review tiếp theo

| Kỳ review | Ngày dự kiến | Scope |
|-----------|-------------|-------|
| Review tháng 6/2026 | 2026-06-12 | Full sync tất cả scripts |
| Resolve ISS-01..04 | Q2/2026 | Business stakeholder meeting |
