# DOC_SYNC_REPORT — Hệ thống Tính Thực Chạy

> **Skill:** `documentation-sync` | **Trạng thái:** 🟡 Skeleton
>
> Báo cáo đồng bộ giữa code thực tế và tài liệu.

---

## Lần kiểm tra gần nhất

| Thuộc tính | Giá trị |
|------------|---------|
| **Ngày kiểm tra** | _(chưa chạy)_ |
| **Drift detected** | _(tbd)_ |
| **Files cần cập nhật** | _(tbd)_ |

---

## Quy trình Đồng bộ

### Scripts auto-gen (chạy theo thứ tự)

1. `python generate_sp_flow_mssql.py` — Cập nhật FLOW_*.md
2. `python generate_sp_from_mssql.py` — Cập nhật SP_*.md (chỉ SP trong luồng)
3. `python generate_md_from_mssql.py` — Cập nhật tables/*.md
4. `python generate_context_for_ai.py` — Cập nhật 01, 02, 03
5. `python generate_job_table_desc.py` — Cập nhật 04, 05
6. `python generate_data_architecture_audit.py` — Cập nhật 06

### Tần suất khuyến nghị

| Khi nào | Scripts cần chạy |
|---------|------------------|
| Thêm/sửa SP | 1 + 2 |
| Thêm/sửa Table | 3 |
| Thay đổi Job | 4 |
| Cập nhật mô tả (desc) | 5 + 6 |
| Review định kỳ (hàng tháng) | Tất cả |
