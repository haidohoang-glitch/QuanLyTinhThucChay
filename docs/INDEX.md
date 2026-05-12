# 📚 INDEX — Hệ thống Tài liệu Dự án: Project "Quan ly tinh thuc chay" (ABM_Data_ThucChay)

> **Sinh tự động bởi:** `document-index-master` skill
> **Cập nhật lần cuối:** 2026-05-12
> **Trạng thái tổng:** 🟢 Phase A Documentation Complete

---

## Mục lục Master Navigation

### Phase 0 — Requirements (Yêu cầu & Đặc tả)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [CONTEXT_PACK.md](./00_REQUIREMENTS/CONTEXT_PACK.md) | 🟡 Skeleton | Tổng hợp ngữ cảnh dự án từ mọi nguồn |
| [SRS_VI/M1_INTRODUCTION.md](./00_REQUIREMENTS/SRS_VI/M1_INTRODUCTION.md) | 🟢 Complete | Giới thiệu & phạm vi SRS |
| [SRS_VI/M2_OVERVIEW.md](./00_REQUIREMENTS/SRS_VI/M2_OVERVIEW.md) | 🟢 Complete | Tổng quan hệ thống |
| [SRS_VI/M3-M8_FUNCTIONAL_REQUIREMENTS.md](./00_REQUIREMENTS/SRS_VI/M3-M8_FUNCTIONAL_REQUIREMENTS.md) | 🟢 Complete | Đặc tả yêu cầu phần mềm (Module M3-M8) |
| [SRS_VI/M9_NFR.md](./00_REQUIREMENTS/SRS_VI/M9_NFR.md) | 🟢 Complete | Non-functional requirements |
| [SRS_VI/M10_TRACEABILITY.md](./00_REQUIREMENTS/SRS_VI/M10_TRACEABILITY.md) | 🟡 Open Issues (ISS-01..04) | Ma trận truy xuất nguồn gốc |

### Phase 1 — Discovery (Khám phá & Kiểm kê)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [BUSINESS_CONTEXT.md](./01_DISCOVERY/BUSINESS_CONTEXT.md) | 🟢 Complete | Ngữ cảnh nghiệp vụ: hệ thống tính thực chạy |
| [CODEBASE_MAP.md](./01_DISCOVERY/CODEBASE_MAP.md) | 🟢 Complete | Bản đồ codebase: SP/FN, Jobs, Tables |
| [DATA_ARCHITECTURE.md](./01_DISCOVERY/DATA_ARCHITECTURE.md) | 🟢 Complete | Kiến trúc dữ liệu & mối quan hệ |
| [TECH_DEBT_AUDIT.md](./01_DISCOVERY/TECH_DEBT_AUDIT.md) | 🟢 Complete | Đánh giá nợ kỹ thuật (4 findings, P1×2, P2×2) |

### Phase 2 — Strategic (Chiến lược & Thiết kế)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [FEASIBILITY_ASSESSMENT.md](./02_STRATEGIC/FEASIBILITY_ASSESSMENT.md) | 🟢 Complete | Đánh giá khả thi — 2 sáng kiến INI-01, INI-02 |
| [TECH_SOLUTION_DESIGN.md](./02_STRATEGIC/TECH_SOLUTION_DESIGN.md) | 🟢 Complete | Thiết kế giải pháp & 5 ADRs |
| [MASTER_PLAN.md](./02_STRATEGIC/MASTER_PLAN.md) | 🟢 Complete | Kế hoạch 3 phases, 12 Work Packages |

### Phase 3 — Execution (Thực thi)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [AI_OPERATOR_GUIDE.md](./03_EXECUTION/AI_OPERATOR_GUIDE.md) | 🟢 Complete | Routing table, escalation rules, checklist |
| [AI_AGENT_TASK_DISTRIBUTION.md](./03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md) | 🟢 Complete | Task matrix T1-T3, cost projection 3 phases |
| [work-packages/](./03_EXECUTION/work-packages/) | 🔴 Chưa tạo | Gói công việc chi tiết (Phase B+C) |

### Phase 4 — Maintenance (Bảo trì & Vận hành)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [runbooks/INCIDENT_JOB_FAILURE.md](./04_MAINTENANCE/runbooks/INCIDENT_JOB_FAILURE.md) | 🟢 Complete | Playbook khi SQL Agent Job fail |
| [runbooks/INCIDENT_WRONG_REVENUE.md](./04_MAINTENANCE/runbooks/INCIDENT_WRONG_REVENUE.md) | 🟢 Complete | Playbook khi doanh số tính sai |
| [runbooks/INCIDENT_DATA_SYNC_FAIL.md](./04_MAINTENANCE/runbooks/INCIDENT_DATA_SYNC_FAIL.md) | 🟢 Complete | Playbook khi đồng bộ dữ liệu thất bại |
| [feature-extensions/](./04_MAINTENANCE/feature-extensions/) | 🔴 Chưa tạo | Kế hoạch mở rộng tính năng |
| [DOC_SYNC_REPORT.md](./04_MAINTENANCE/DOC_SYNC_REPORT.md) | 🟢 Complete | Báo cáo đồng bộ — baseline 2026-05-12 |

---

## Mapping: Tài liệu cũ → Framework mới

> Các file trong `context/` đã có sẽ được **tham chiếu** (không di chuyển) từ framework mới.

| File cũ (context/) | Maps to Phase | Vai trò |
|--------------------|---------------|---------|
| `00_MASTER_INDEX.md` | Cross-cutting | Master nav cho AI (giữ nguyên) |
| `01_JOBS_AND_STEPS.md` | Phase 1 Discovery | Input cho CODEBASE_MAP |
| `02_DM_SANPHAM.md` | Phase 1 Discovery | Input cho DATA_ARCHITECTURE |
| `03_DM_HINHTHUCQUANGCAO.md` | Phase 1 Discovery | Input cho DATA_ARCHITECTURE |
| `04_JOB_DESC.md` | Phase 0 + Phase 1 | Input cho SRS + BUSINESS_CONTEXT |
| `05_TABLE_DESC.md` | Phase 1 Discovery | Input cho DATA_ARCHITECTURE |
| `06_DATA_ARCHITECTURE.md` | Phase 1 Discovery | Đã có bản v1, cần nâng cấp |
| `stored_procedures/FLOW_*.md` | Phase 1 Discovery | Input cho CODEBASE_MAP |
| `stored_procedures/SP_*.md` | Phase 1 Discovery | Chi tiết kỹ thuật SP |
| `tables/*.md` | Phase 1 Discovery | Schema chi tiết |

---

## Tiến độ Phase A — Documentation

> **Hoàn thành ngày 2026-05-12**

```
Phase 0 (Requirements)  ████████████████████ 90%  (còn CONTEXT_PACK + ISS-01..04)
Phase 1 (Discovery)     ████████████████████ 100% ✅
Phase 2 (Strategic)     ████████████████████ 100% ✅
Phase 3 (Execution)     █████████████████░░░ 85%  (còn work-packages/)
Phase 4 (Maintenance)   █████████████████░░░ 85%  (còn feature-extensions/)
```

**Còn lại:**
- `CONTEXT_PACK.md` — cần tổng hợp cuối cùng
- `work-packages/` — chi tiết WP Phase B+C (khi có stakeholder approval)
- `feature-extensions/` — khi có yêu cầu mở rộng cụ thể
- Resolve ISS-01..04 trong M10_TRACEABILITY
