# 📚 INDEX — Hệ thống Tài liệu Dự án: Project "Quan ly tinh thuc chay" (ABM_Data_ThucChay)

> **Sinh tự động bởi:** `document-index-master` skill
> **Cập nhật lần cuối:** _(chưa sinh)_
> **Trạng thái tổng:** 🔴 Đang khởi tạo khung

---

## Mục lục Master Navigation

### Phase 0 — Requirements (Yêu cầu & Đặc tả)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [CONTEXT_PACK.md](./00_REQUIREMENTS/CONTEXT_PACK.md) | 🟡 Skeleton | Tổng hợp ngữ cảnh dự án từ mọi nguồn |
| [SRS_VI/M3-M8_FUNCTIONAL_REQUIREMENTS.md](./00_REQUIREMENTS/SRS_VI/M3-M8_FUNCTIONAL_REQUIREMENTS.md) | 🟢 Partial | Đặc tả yêu cầu phần mềm (Module M3-M8) |

### Phase 1 — Discovery (Khám phá & Kiểm kê)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [CODEBASE_MAP.md](./01_DISCOVERY/CODEBASE_MAP.md) | 🟡 Skeleton | Bản đồ codebase: SP/FN, Jobs, Tables |
| [DATA_ARCHITECTURE.md](./01_DISCOVERY/DATA_ARCHITECTURE.md) | 🟡 Skeleton | Kiến trúc dữ liệu & mối quan hệ |
| [TECH_DEBT_AUDIT.md](./01_DISCOVERY/TECH_DEBT_AUDIT.md) | 🟡 Skeleton | Đánh giá nợ kỹ thuật |
| [BUSINESS_CONTEXT.md](./01_DISCOVERY/BUSINESS_CONTEXT.md) | 🟡 Skeleton | Ngữ cảnh nghiệp vụ: hệ thống tính thực chạy |

### Phase 2 — Strategic (Chiến lược & Thiết kế)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [FEASIBILITY_ASSESSMENT.md](./02_STRATEGIC/FEASIBILITY_ASSESSMENT.md) | 🟡 Skeleton | Đánh giá khả thi |
| [TECH_SOLUTION_DESIGN.md](./02_STRATEGIC/TECH_SOLUTION_DESIGN.md) | 🟡 Skeleton | Thiết kế giải pháp kỹ thuật & ADRs |
| [MASTER_PLAN.md](./02_STRATEGIC/MASTER_PLAN.md) | 🟡 Skeleton | Kế hoạch triển khai tổng thể |

### Phase 3 — Execution (Thực thi)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [AI_OPERATOR_GUIDE.md](./03_EXECUTION/AI_OPERATOR_GUIDE.md) | 🟡 Skeleton | Hướng dẫn vận hành AI agent |
| [AI_AGENT_TASK_DISTRIBUTION.md](./03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md) | 🟡 Skeleton | Phân phối task cho AI theo tier |
| [work-packages/](./03_EXECUTION/work-packages/) | 🔴 Chưa tạo | Gói công việc chi tiết |

### Phase 4 — Maintenance (Bảo trì & Vận hành)

| Tài liệu | Trạng thái | Mô tả |
|-----------|------------|-------|
| [runbooks/](./04_MAINTENANCE/runbooks/) | 🟡 Skeleton | Playbook xử lý sự cố |
| [feature-extensions/](./04_MAINTENANCE/feature-extensions/) | 🟡 Skeleton | Kế hoạch mở rộng tính năng |
| [DOC_SYNC_REPORT.md](./04_MAINTENANCE/DOC_SYNC_REPORT.md) | 🟡 Skeleton | Báo cáo đồng bộ tài liệu |

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
