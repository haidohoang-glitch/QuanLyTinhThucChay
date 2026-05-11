# Quan lý tính thuc chay — Tech Debt Audit

> **Mục đích:** Xác định và xếp hạng nợ kỹ thuật trên các danh mục. Cung cấp cái nhìn về rủi ro vận hành và bảo trì.
> **Trạng thái:** 🟢 Complete
> **Ngày cập nhật:** 2026-05-08

---

## 1. Executive Summary

**Mức độ nợ kỹ thuật tổng thể:** 🔴 HIGH

**Điểm nổi bật:**
- Tổng số phát hiện: 04 (0 P0, 02 P1, 02 P2, 0 P3)
- Danh mục nợ nhiều nhất: Data Integrity, Maintainability.
- Rủi ro lớn nhất là việc thiếu các ràng buộc cứng trên Database và logic nghiệp vụ bị phân mảnh trong nhiều Stored Procedure riêng biệt.

**Top 3 rủi ro:**
1. **TD-001** — Không sử dụng Foreign Keys cứng (P1)
2. **TD-002** — Logic nghiệp vụ bị hardcoded (P1)
3. **TD-003** — Độ phức tạp của CTE Recursive (P2)

---

## 2. Quality Signals (Tín hiệu chất lượng)

| Tín hiệu | Giá trị | Ghi chú |
|--------|-------|-------|
| Độ phủ bài test | 0% | Chưa có hệ thống Unit Test tự động cho SQL |
| Lỗi Lint/Format | N/A | Không áp dụng công cụ lint cho T-SQL |
| File lớn nhất | SP_ThucChay_Mobile_GhiNhanPhatSinh_ThucChayDaTinh | ~500 lines |

---

## 3. Findings (Phát hiện theo danh mục)

### DATA INTEGRITY (Toàn vẹn dữ liệu)

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| TD-001 | P1 | L | Không sử dụng Foreign Keys cứng | Toàn bộ Database | Integrity dựa hoàn toàn vào logic SP. |

### MAINTAINABILITY (Khả năng bảo trì)

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| TD-002 | P1 | M | Logic nghiệp vụ bị phân mảnh & Hardcoded | Hệ thống SP tính toán | Khó mở rộng khi có nhóm SP mới. |

### PERFORMANCE (Hiệu năng)

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| TD-003 | P2 | M | Phức tạp trong thuật toán CTE Recursive | SP Nhóm Mobile | Rủi ro chậm khi dữ liệu lớn. |

### RELIABILITY (Độ tin cậy)

| ID | Severity | Effort | Title | Evidence | Notes |
|----|----------|--------|-------|----------|-------|
| TD-004 | P2 | S | Thiếu chuẩn hóa Xử lý lỗi (Error Handling) | Try-Catch blocks | Khó truy vết sự cố Job. |

---

## 4. Top 10 Punch List (Ưu tiên xử lý)

| Thứ tự | ID | Lý do ưu tiên | Công sức |
|-------|---------|-------------------|--------|
| 1 | TD-001 | Ngăn chặn rủi ro dữ liệu mồ côi (Orphan Records). | L |
| 2 | TD-004 | Cải thiện khả năng giám sát và xử lý sự cố. | S |
| 3 | TD-002 | Tăng tốc độ phát triển các tính năng mới. | M |
| 4 | TD-003 | Đảm bảo hệ thống chạy mượt khi scale dữ liệu. | M |

---

## 5. Ghi chú & Caveats

- **Chế độ phân loại:** Mode A (7 danh mục chuẩn).
- **Phạm vi kiểm tra:** Quét mã nguồn 11 luồng tính toán chính.
- **Thời gian thực hiện:** 2 giờ.
- **Độ tin tưởng:** Trung bình (Medium).
