# INPUT: Job Schedule & Orchestration

> **Nguồn:** Tổng hợp từ `docs/Logic_nghiepvu_tinh_thucchay.md` và `context/01_JOBS_AND_STEPS.md`
> **Mục đích:** Mô tả thứ tự chạy, lịch biểu và quản lý luồng thực thi của các SQL Server Agent Jobs phục vụ tính thực chạy.
> **Ngày tạo:** 2026-05-08

---

## 1. Danh sách Jobs theo Nhóm Chức năng

Hệ thống tính thực chạy được vận hành bởi các SQL Server Agent Jobs, chia thành các nhóm chính:

### Nhóm 1: Tính Thực Chạy Core (Nhóm sản phẩm chính)
Các job này tính toán trực tiếp trên hệ thống ABM.

| Tên Job | Trạng thái | Sản phẩm liên quan | Mô tả luồng chạy |
|---------|------------|--------------------|------------------|
| `ThucChay_CPD_Chiphi_PR` | Đang bật | CPD, Chi phí, PR | Bước 1: Tính CPD<br>Bước 2: Tính Chi phí<br>Bước 3: Tính PR |
| `ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic` | Đang bật | Admarket, CPM, Mobile, Inventory, Admatic, Performance Base | Bước 1: Admarket phân bổ<br>Bước 2: Admarket điều chỉnh<br>Bước 3: CPM đơn vị ngày<br>Bước 4: Mobile<br>Bước 5: Inventory<br>Bước 6: Các loại CPM khác<br>Bước 7: Admatic |
| `ThucChay_MuaNgoai` | Đang bật | Sản phẩm Mua Ngoài | Bước 1: Tính mua ngoài theo kết quả vận hành |

### Nhóm 2: Lấy dữ liệu & Tính toán Nền tảng ngoài
Các job này đồng bộ dữ liệu từ các nền tảng khác (Google, Facebook...) hoặc từ hợp đồng chữ ký số.

| Tên Job | Trạng thái | Nền tảng/Sản phẩm | Mô tả luồng chạy |
|---------|------------|-------------------|------------------|
| `Job_GetInfo_ThucChay_GGFB` | Đang bật | GG-Facebook | Lấy thông tin vận hành từ GG/FB |
| `ThucChay_GoogleFacebook_MktFee` | Đang bật | GG-Facebook, Marketing Fee | Bước 1: Tính thực chạy GG/FB<br>Bước 2: Tính Marketing fee |
| `Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN` | Đang bật | Branding, Chi phí, Mua ngoài... | Gồm 16 bước: Lấy thực treo từ HĐ chữ ký số (HDCN), lấy thông tin chi phí, kết quả vận hành... (một số bước bị vô hiệu hóa vì đã có job riêng) |

### Nhóm 3: Hệ thống & Khác

| Tên Job | Trạng thái | Nhóm/Mô tả |
|---------|------------|------------|
| `KiemSoat_ThucChayDaTinh` | Đang bật | Chạy các thủ tục kiểm soát dữ liệu sau khi tính toán |
| `job_TinhLaiThucChay` | Đang bật | Tính lại các hợp đồng có sự thay đổi (đối trừ & insert) |
| `cdc.ABM_Data_ThucChay_capture` | Đang bật | Change Data Capture (CDC) - theo dõi thay đổi dữ liệu |
| `cdc.ABM_Data_ThucChay_cleanup` | Đang bật | Dọn dẹp log CDC |
| `Job_XuLy_ThucChay_TamTinh` | Đã tắt | Xử lý thực chạy tạm tính show domain fake |
| `Job_KiemTraTrangThai_JobTinhThucChay` | Đã tắt | Kiểm tra trạng thái job |

---

## 2. Thứ tự ưu tiên & Dependency (Orchestration)

Để đảm bảo dữ liệu toàn vẹn, các job cần tuân thủ thứ tự chạy sau:

1. **Giai đoạn 1: Chuẩn bị dữ liệu**
   - Chạy các job lấy thông tin thực treo, vận hành: `Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN`, `Job_GetInfo_ThucChay_GGFB`
2. **Giai đoạn 2: Tính toán chính (Song song hoặc Tuần tự)**
   - Các job nhóm 1 và nhóm 2 (tính toán) có thể chạy. Tuy nhiên, theo luồng hiện tại thì tính toán được chia theo từng Job độc lập cho từng cụm nhóm sản phẩm.
3. **Giai đoạn 3: Tính lại (Recalculation)**
   - Chạy `job_TinhLaiThucChay` để đối trừ và cập nhật sự thay đổi.
4. **Giai đoạn 4: Kiểm soát & Validate**
   - Chạy `KiemSoat_ThucChayDaTinh` để rà soát lỗi sau cùng.

---

## 3. Cảnh báo lỗi & Giám sát

Hầu hết các job tính toán đều có 1 step cuối cùng đóng vai trò cảnh báo qua email nếu các step trước đó bị lỗi.
Ví dụ:
- Lệnh: `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] <Tên Job>" -smtpBody "Job loi <Tên Job>"`
- Chạy trên DB: `msdb`

*(Cần hệ thống tự động sinh tài liệu Playbook dựa trên danh sách job và cảnh báo này).*
