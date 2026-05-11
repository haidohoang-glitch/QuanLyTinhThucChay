# SRS: Đặc tả Yêu cầu Chức năng (Functional Requirements)

> **Dự án:** Quản lý tính thực chạy | **Phạm vi:** Module M3 - M8
> **Tiêu chuẩn:** Tài liệu hóa theo chuẩn Company-Skill
> **Ngày tạo:** 2026-05-08

---

## M3 — Logic Tính Mới (New Calculation)

### 3.1 Domain Overview
Domain này chịu trách nhiệm xác định và ghi nhận doanh số thực chạy lần đầu cho các phân bổ hợp đồng (HopDongChiTiet) dựa trên dữ liệu vận hành thực tế (treo, view, click). Logic này đảm bảo doanh số chỉ được tính khi có bằng chứng vận hành và chưa từng được ghi nhận trong bảng `ThucChayDaTinh`.

### 3.2 Functional Requirements

#### FR-M3-01 — Xác định điều kiện tính mới
**Statement:** Hệ thống phải tự động nhận diện các phân bổ có dữ liệu vận hành nhưng chưa có dữ liệu thực chạy tương ứng tại ngày tính.
- **Chi tiết:** Kiểm tra sự tồn tại của bản ghi trong `ThucChayDaTinh` cho cặp (HopDongChiTietREF, NgayThucHien).
- **Tiêu chí nghiệm thu:** [ ] Không tính trùng lặp cho dữ liệu đã tồn tại.
**Priority:** Must
**Verification method:** Acceptance test / Analysis

#### FR-M3-02 — Tính toán cho nhóm CPD
**Statement:** Hệ thống thực hiện tính thực chạy cho nhóm Cost Per Day theo 3 kịch bản: đợt chạy, không đợt chạy và đơn vị gói.
- **Chi tiết:**
  - CPD đợt chạy: `SL_danhso * DG_danhso / songaydotchay_danhso * (1 - CK%)`.
  - CPD không đợt chạy: `SL_danhso * DG_danhso / tongsongaytreo * (1 - CK%)`.
  - CPD đơn vị gói: Ghi nhận 100% giá trị phân bổ khi phát sinh treo.
**Priority:** Must
**Verification method:** Demo / Inspection

#### FR-M3-03 — Tính toán cho nhóm Mobile (Cơ chế chống vượt)
**Statement:** Tính thực chạy cho nhóm Mobile sử dụng thuật toán đệ quy (CTE Recursive) để kiểm soát trần giá trị theo từng loại xử lý.
- **Chi tiết:** 
  - LoaiXuLy 1 (Gói): Chốt chặn theo Thành tiền.
  - LoaiXuLy 2 (Thường): Chốt chặn theo Số lượng.
**Priority:** Must
**Verification method:** Analysis / Test Case

---

## M4 — Logic Tính Thay Đổi (Change Detection & Recalculation)

### 4.1 Domain Overview
Domain này giám sát sự thay đổi trên dữ liệu gốc để thực hiện điều chỉnh doanh số thông qua cơ chế Đối trừ (Offset).

### 4.2 Functional Requirements

#### FR-M4-01 — Phát hiện sự kiện thay đổi
**Statement:** Hệ thống phải kích hoạt tính lại khi phát hiện thay đổi về Đánh số, Thuộc tính, Thông tin treo hoặc Hủy phân bổ.
**Priority:** Must
**Verification method:** Analysis

#### FR-M4-02 — Thực hiện đối trừ (Offset)
**Statement:** Hệ thống thực hiện điều chỉnh theo công thức: `GiaTriThayDoi = Sau_thay_đổi - Trước_thay_đổi`.
**Priority:** Must
**Verification method:** Analysis

---

## M5 — Lập lịch & Điều phối Job (Job Scheduling)

### 5.1 Domain Overview
Quản lý luồng thực thi của các SQL Server Agent Jobs.

### 5.2 Functional Requirements

#### FR-M5-01 — Điều phối thứ tự chạy (Orchestration)
**Statement:** Các Job phải chạy theo tuần tự:
- **B1:** Lấy dữ liệu nguồn (RecurringJob).
- **B2:** Sync & Chuẩn hóa đầu vào.
- **B3:** Tính toán tự động (08:00 AM).
- **B4:** Kiểm soát, Hỗ trợ & Fix lỗi (09:00 AM).
**Priority:** Must

#### FR-M5-02 — Xử lý các yêu cầu phát sinh từ Kiểm soát
**Statement:** Hệ thống phải hỗ trợ việc viết các Stored Procedure mới để xử lý các case thực chạy đặc thù hoặc sửa đổi logic theo phản ánh của đội Kiểm soát.
**Priority:** Must

---

## M6 — Kiểm soát & Toàn vẹn dữ liệu (Quality Control)

### 6.1 Domain Overview
Thực hiện các thủ tục hậu kiểm để đảm bảo dữ liệu không bị sai lệch sau tính toán.

### 6.2 Functional Requirements

#### FR-M6-01 — Tự động kiểm soát sau Job
**Statement:** Hệ thống tự động kích hoạt `KiemSoat_ThucChayDaTinh` sau khi các Job tính toán hoàn tất.
**Priority:** Should

---

## M7 — Cảnh báo & Xử lý Sự cố (Alerting)

### 7.1 Domain Overview
Giám sát và thông báo lỗi vận hành.

### 7.2 Functional Requirements

#### FR-M7-01 — Cảnh báo Email khi lỗi Job
**Statement:** Hệ thống gửi email cảnh báo tự động khi có bất kỳ Step nào trong Job bị Fail.
**Priority:** Must

---

## M8 — Quản lý Dữ liệu Đích (Output & Destination)

### 8.1 Domain Overview
Quản lý các bảng lưu trữ kết quả cuối cùng.

### 8.2 Functional Requirements

#### FR-M8-01 — Lưu trữ tập trung tại ThucChayDaTinh
**Statement:** Toàn bộ kết quả thực chạy và thay đổi (bao gồm cả các bản ghi fix lỗi hoặc tính bổ sung) phải được ghi nhận vào bảng `ThucChayDaTinh`.
**Priority:** Must
