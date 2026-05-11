# AI_OPERATOR_GUIDE — Hệ thống Tính Thực Chạy

> **Skill:** `ai-operator-protocol` | **Trạng thái:** 🟡 Skeleton
>
> Hướng dẫn vận hành AI agent cho dự án này.

---

## 1. Quy tắc Chung

- AI đọc `context/00_MASTER_INDEX.md` TRƯỚC khi trả lời bất kỳ câu hỏi nào
- Từ Master Index, điều hướng sang file chi tiết phù hợp
- KHÔNG suy luận logic nghiệp vụ — luôn tham chiếu tài liệu

---

## 2. Routing theo Loại Câu hỏi

| Loại câu hỏi | File cần đọc | Model khuyến nghị |
|---------------|--------------|-------------------|
| Tổng quan hệ thống | `context/00_MASTER_INDEX.md` | Bất kỳ |
| Job cụ thể | `context/01_JOBS_AND_STEPS.md` + `context/04_JOB_DESC.md` | T1-T2 |
| SP cụ thể | `stored_procedures/SP_*.md` | T2 |
| Luồng nghiệp vụ | `stored_procedures/FLOW_*.md` | T2 |
| Debug doanh số sai | FLOW + SP + `02_DM_SANPHAM.md` | T3 |
| Schema bảng | `tables/*.md` + `context/06_DATA_ARCHITECTURE.md` | T1-T2 |
| Xử lý sự cố | `docs/04_MAINTENANCE/runbooks/` | T2 |

---

## 3. Escalation Rules

<!-- Sẽ điền dựa trên incident playbook -->
