# M9 — Các yêu cầu phi chức năng (Non-Functional Requirements)

> **SRS Module 9 trong 10** | Dự án: Quản lý tính thực chạy

---

## 9.1 Hiệu năng (Performance)
- **NFR-PER-01:** Các Job tính toán thực chạy hàng ngày phải hoàn tất trước 08:00 AM để bộ phận kinh doanh có dữ liệu báo cáo.
- **NFR-PER-02:** Thời gian phản hồi của các truy vấn báo cáo trên bảng `ThucChayDaTinh` (với dữ liệu hàng triệu dòng) không được quá 5 giây.
- **NFR-PER-03:** Các Stored Procedure phải được tối ưu hóa chỉ số (Indexing) để tránh tình trạng Table Scan trên các bảng lớn.

## 9.2 Độ tin cậy & Toàn vẹn (Reliability & Integrity)
- **NFR-REL-01:** Dữ liệu doanh số tính toán phải khớp 100% với logic đã định nghĩa (Sai số 0%).
- **NFR-REL-02:** Hệ thống phải đảm bảo tính toàn vẹn dữ liệu khi có lỗi xảy ra trong quá trình chạy Job (sử dụng Transaction nếu cần thiết).
- **NFR-REL-03:** Cơ chế chốt chặn (Cap) phải đảm bảo tuyệt đối không bao giờ tính thực chạy vượt quá giá trị phân bổ của hợp đồng.

## 9.3 Khả năng bảo trì (Maintainability)
- **NFR-MAI-01:** Mọi Stored Procedure phải có header chứa thông tin: Tác giả, Ngày tạo, Mục đích và Lịch sử thay đổi.
- **NFR-MAI-02:** Code SQL phải tuân thủ quy tắc đặt tên và định dạng chuẩn của công ty để AI và Developer dễ dàng rà soát.

## 9.4 Khả năng kiểm toán (Auditability)
- **NFR-AUD-01:** Mọi thao tác điều chỉnh doanh số do thay đổi dữ liệu gốc phải được ghi nhận qua cột `GiaTriThayDoi` và `SoLuongThayDoi` để có thể truy xuất nguồn gốc (Audit Trail).
- **NFR-AUD-02:** Lưu giữ log lịch sử chạy của các SQL Agent Jobs ít nhất trong vòng 6 tháng.

## 9.5 Khả năng mở rộng (Scalability)
- **NFR-SCA-01:** Hệ thống phải có khả năng xử lý lượng dữ liệu tăng trưởng 20% mỗi năm mà không yêu cầu thay đổi kiến trúc cốt lõi.
- **NFR-SCA-02:** Hỗ trợ việc thêm mới các nhóm sản phẩm Level 1 mới bằng cách thêm các Step vào Job điều phối hiện có.
