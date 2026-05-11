# AI_AGENT_TASK_DISTRIBUTION — Hệ thống Tính Thực Chạy

> **Skill:** `multi-tier-ai-routing` | **Trạng thái:** 🟡 Skeleton
>
> Phân phối task cho AI agents theo tier để tối ưu chi phí.

---

## 1. Tier Definitions (cho dự án này)

| Tier | Mục đích | Model khuyến nghị |
|------|----------|-------------------|
| **T3 Strong** | Phân tích logic nghiệp vụ, debug SP phức tạp, viết SRS | Claude Opus 4 / Gemini Pro |
| **T2 Mid** | Gen tài liệu từ data có sẵn, đọc SP, tổng hợp | Claude Sonnet 4 / Gemini Pro |
| **T1 Simple** | Chạy scripts, format, cập nhật links, gen boilerplate | Claude Haiku / Gemini Flash |

---

## 2. Task Routing cho Dự án này

| Task | Tier | Lý do |
|------|------|-------|
| Chạy `generate_*.py` scripts | T1 | Đơn giản, chỉ execute |
| Cập nhật links trong MASTER_INDEX | T1 | Format-only |
| Gen CODEBASE_MAP từ data đã có | T2 | Tổng hợp structured data |
| Gen DATA_ARCHITECTURE từ 06 + tables/ | T2 | Structured extraction |
| Viết BUSINESS_CONTEXT (logic nghiệp vụ) | T3 | Cần hiểu domain sâu |
| Reverse-engineer SRS từ SP code | T3 | Judgment + long context |
| Tạo Incident Playbook | T2 | Template-based + user input |
| Debug lỗi tính sai doanh số | T3 | Multi-SP analysis |

---

## 3. Cost Projection

| Phase | Tasks | Tier mix | Est. cost |
|-------|-------|----------|-----------|
| Phase 0 (SRS) | 5-7 | T3 heavy | _(tbd)_ |
| Phase 1 (Discovery) | 4-6 | T2 heavy | _(tbd)_ |
| Phase 2 (Strategic) | 3-4 | T3 | _(tbd)_ |
| Phase 3 (Execution) | 10+ | T1+T2 mix | _(tbd)_ |
| Phase 4 (Maintenance) | Ongoing | T1+T2 | _(tbd)_ |
