# FEASIBILITY_ASSESSMENT — Hệ thống Tính Thực Chạy

> **Skill:** `feasibility-assessment` | **Trạng thái:** 🟢 Complete
> **Ngày tạo:** 2026-05-12 | **Phiên bản:** v1.0

---

## 1. Business Case (Lý do nghiệp vụ)

### 1.1 Bối cảnh

Hệ thống **ABM_Data_ThucChay** là hệ thống tính toán doanh số quảng cáo thực tế (Actual Revenue) cho **21 nhóm sản phẩm**, vận hành hàng ngày phục vụ đội Kiểm soát, Sale và BI. Hệ thống đang ở trạng thái **legacy có code** — vận hành ổn định nhưng chưa được tài liệu hóa đầy đủ và có nợ kỹ thuật P1.

Đánh giá khả thi này tập trung vào **2 sáng kiến** cụ thể:

| Sáng kiến | Mô tả | Ưu tiên |
|-----------|-------|---------|
| **INI-01: Tài liệu hóa toàn diện** | Hoàn thiện bộ tài liệu SRS, Discovery, Runbooks | Must |
| **INI-02: Xử lý Tech Debt P1** | Fix TD-001 (FK cứng), TD-004 (Error Handling) | Should |

### 1.2 Pain Points hiện tại (Vấn đề đang tồn tại)

| ID | Vấn đề | Tác động | Tần suất |
|----|--------|---------|---------|
| PP-01 | Không có tài liệu runbook → mỗi sự cố mất 1-4 giờ điều tra | Cao | Hàng tuần |
| PP-02 | Logic nghiệp vụ embedded trong SP → onboarding developer mới mất 2-4 tuần | Cao | Mỗi khi tuyển dụng |
| PP-03 | Thiếu FK cứng → dữ liệu orphan xuất hiện khó phát hiện | Rất cao | Tiềm ẩn |
| PP-04 | Không có error handling chuẩn → log lỗi không đủ để triage nhanh | Trung bình | Hàng tuần |

### 1.3 ROI Estimate

**INI-01 (Tài liệu hóa):**
- Chi phí: ~20-40 giờ engineer time (1 lần)
- Tiết kiệm: Giảm 60% thời gian điều tra sự cố → ~2-4 giờ/tuần × 52 = 104-208 giờ/năm
- Payback: Trong vòng **2-4 tuần**

**INI-02 (Tech Debt P1):**
- Chi phí: ~40-80 giờ engineer time
- Tiết kiệm: Phòng ngừa 1 sự cố dữ liệu orphan nghiêm trọng (~1 ngày downtime + fix = >80 giờ)
- Payback: Trong vòng **3-6 tháng**

---

## 2. Technical Feasibility (Khả thi kỹ thuật)

### 2.1 Đánh giá INI-01: Tài liệu hóa

| Tiêu chí | Đánh giá | Ghi chú |
|---------|---------|---------|
| Khả năng truy cập source | ✅ Cao | Có đầy đủ SP, table, job scripts |
| Tài liệu nghiệp vụ gốc | ✅ Đầy đủ | `Logic_nghiepvu_tinh_thucchay.md` (21 nhóm SP) |
| Độ phức tạp logic | ⚠️ Trung bình-Cao | CTE Recursive ở Mobile, logic offset 2 chiều |
| Phụ thuộc stakeholder | ✅ Thấp | Tài liệu hóa không cần approval business |
| Rủi ro | 🟢 Thấp | Tài liệu hóa không thay đổi hệ thống live |

**Kết luận:** ✅ **Khả thi hoàn toàn.** Tất cả inputs đã có.

### 2.2 Đánh giá INI-02: Tech Debt P1

| Tech Debt | Effort | Complexity | Rủi ro khi fix |
|-----------|--------|------------|----------------|
| TD-001: FK cứng | Large (L) | Cao | Cao — cần test rollback kỹ |
| TD-004: Error Handling | Small (S) | Thấp | Thấp — add Try-Catch không thay đổi logic |

**Kết luận INI-02:**
- **TD-004 (Error Handling):** ✅ Khả thi ngay — effort nhỏ, rủi ro thấp
- **TD-001 (FK cứng):** ⚠️ Khả thi nhưng cần lập kế hoạch kỹ — effort lớn, rủi ro cao (có thể break các SP hiện có nếu có orphan records trong DB)

### 2.3 Dependency Analysis

```
INI-01 (Tài liệu) ──► không phụ thuộc gì
INI-02 (Tech Debt) ──► cần INI-01 hoàn thành TRƯỚC
                        (vì cần hiểu rõ toàn bộ SP trước khi thêm FK)
```

---

## 3. Risk Assessment (Đánh giá rủi ro)

| # | Rủi ro | Xác suất | Impact | Mitigation |
|---|--------|----------|--------|------------|
| R1 | Tài liệu không đồng bộ với code sau khi update | Trung bình | Trung bình | Dùng auto-gen scripts (`generate_*.py`) + lịch review hàng tháng |
| R2 | TD-001 fix phát hiện orphan records chưa biết | Cao | Cao | Chạy script kiểm tra orphan TRƯỚC khi add FK; xử lý data cleanup |
| R3 | Logic nghiệp vụ bị hiểu sai khi tài liệu hóa | Thấp | Cao | Review với Business Analyst + đội Kiểm soát trước khi publish |
| R4 | Scope creep khi fix TD-001 ảnh hưởng SP khác | Trung bình | Trung bình | Fix từng bảng một, test regression sau mỗi bước |

---

## 4. Recommendation (Khuyến nghị)

### 4.1 Quyết định

| Sáng kiến | Quyết định | Lý do |
|-----------|-----------|-------|
| **INI-01: Tài liệu hóa** | ✅ **GO — Thực hiện ngay** | ROI cao, rủi ro thấp, payback trong 2-4 tuần |
| **INI-02: Error Handling (TD-004)** | ✅ **GO — Sau INI-01** | Effort nhỏ, rủi ro thấp, cải thiện rõ rệt |
| **INI-02: FK cứng (TD-001)** | ⚠️ **GO with caution — Q3/2026** | Cần plan kỹ, test kỹ; không rush |

### 4.2 Thứ tự thực hiện đề xuất

```
Q2/2026:
  └─► Hoàn thiện tài liệu hóa (INI-01) — ưu tiên cao nhất
       ├─ SRS hoàn chỉnh (đã xong)
       ├─ Runbooks cho 3 loại incident phổ biến
       ├─ Tech Solution Design (ADRs)
       └─ Master Plan + Work Packages

Q2-Q3/2026:
  └─► Fix TD-004 Error Handling (INI-02 phần dễ)
       └─ Add Try-Catch + logging chuẩn vào các SP tính chính

Q3/2026 (sau stakeholder review):
  └─► Kế hoạch chi tiết fix TD-001 FK cứng
       ├─ Audit orphan records
       ├─ Data cleanup plan
       └─ Migration plan theo rolling (từng bảng)
```

### 4.3 Success Metrics

| KPI | Target | Đo lường |
|-----|--------|---------|
| Thời gian triage sự cố | < 30 phút (hiện tại: 1-4h) | Đo qua incident log |
| Onboarding time cho developer mới | < 1 tuần (hiện tại: 2-4 tuần) | Survey developer |
| Số lần dữ liệu orphan phát hiện muộn | 0 (hiện tại: unknown) | Audit hàng tháng |

---

## 5. Ghi chú & Caveats

- **Phạm vi:** Đánh giá này chỉ cho 2 sáng kiến trên, không bao gồm greenfield features
- **Tiền đề:** Phase 1 Discovery đã hoàn thành và được xác nhận
- **Chế độ phân tích:** Dự án legacy có code sẵn — áp dụng standard assessment framework
