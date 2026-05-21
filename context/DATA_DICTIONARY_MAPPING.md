# TỪ ĐIỂN DỮ LIỆU & ÁNH XẠ (DATA MAPPING CONTEXT)

> **Mục đích:** Cung cấp thông tin ánh xạ (mapping) chính xác giữa các khái niệm/biến số trong công thức tính toán nghiệp vụ (file `Logic_nghiepvu_tinh_thucchay.md`) với các cột thực tế trong cơ sở dữ liệu.
> **Đối tượng sử dụng:** AI Agent (làm ngữ cảnh tri thức để tạo các bộ Skill) và Kỹ sư dữ liệu.

---

## 1. Nhóm Sản Phẩm CPD (Cost Per Day)

### 1.1. CPD Đợt Chạy (Loại A)
Công thức: `TT = (SL_danhso × DG_danhso / songaydotchay_danhso) × (1 - CK_danhso%)`

| Biến số trong công thức | Bảng nguồn | Cột tương ứng | Ghi chú / Logic SQL |
|---|---|---|---|
| `SL_danhso` | `HopDongChiTiet` | `SoLuong` | |
| `DG_danhso` | `HopDongChiTiet` | `DonGia` | |
| `CK_danhso%` | `HopDongChiTiet` | `ChietKhau` | |
| `songaydotchay_danhso` | `DotChayHopDongChiTiet` | Tính toán: `SUM(DATEDIFF(day, ThoiGianBatDau, ThoiGianKetThuc) + 1)` | Lấy tổng số ngày đợt chạy từ lịch phân bổ đợt chạy ứng với `HopDongChiTietID` |
| `Soluongchay_moingaytreo` | - | Giá trị hằng số = `1` | Không phụ thuộc số lượng thực treo |

### 1.2. CPD Không Đợt Chạy (Loại B)
Công thức: `TT = (SL_danhso × DG_danhso / tongsongaytreo) × (1 - CK_danhso%)`

| Biến số trong công thức | Bảng nguồn | Cột tương ứng | Ghi chú / Logic SQL |
|---|---|---|---|
| `SL_danhso` | `HopDongChiTiet` | `SoLuong` | |
| `DG_danhso` | `HopDongChiTiet` | `DonGia` | |
| `CK_danhso%` | `HopDongChiTiet` | `ChietKhau` | |
| `tongsongaytreo` | `ThucChayHopDongChiTiet` | Tính toán: `SUM(DATEDIFF(day, ThoiGianBatDau, ThoiGianKetThuc) + 1)` | Tổng tất cả ngày treo lịch sử của các dòng treo được duyệt (`TrangThaiDuyet` hợp lệ) ứng với `HopDongChiTietREF` |

---

## 2. Nhóm Sản Phẩm PR

Công thức: `TT = SLtreo × Giatientreo × (1 - CKtreo%)`

| Biến số trong công thức | Bảng nguồn | Cột tương ứng | Ghi chú / Logic SQL |
|---|---|---|---|
| `Giatientreo` | `ThucChayHopDongChiTietPR` | Đơn giá dòng treo | Lấy trực tiếp từ dòng treo thực tế, KHÔNG lấy từ đánh số (`HopDongChiTiet`) |

---

## 3. Nhóm Sản Phẩm Chi Phí Khác (Cost)

Công thức cơ bản: `TT = SoLuongTreo × DonGiaTreo × (1 - CK%)`

### Cột Đích cho dữ liệu Khuyến mãi
- Nếu phát sinh giá trị/tiền (`IsKhuyenMai = 1` hoặc `CK = 100`): Ghi nhận vào cột `ThanhTienKM`.
- Nếu phát sinh số lượng khuyến mãi: Ghi nhận vào cột `SoLuongThucChayKM`.

### Cơ chế chống vượt định mức (Anti-Overcap)
Thực thi tại Stored Procedure: `[dbo].[ThucChay_ChiPhiKhac]`
- **Công cụ tính toán:** Sử dụng `CTE_Recursive` để tính lũy kế số tiền sau chiết khấu (`TichLuyThanhTienSauCK`).
- **Luồng xử lý từ chối (Drop-row):** 
  - Nếu một dòng thực treo mới làm tổng lũy kế vượt quá phân bổ (`ThanhTienSauCKDaTinh + ThanhTienSauCKTreo > ThanhTienSauCKPhanBo`).
  - Hệ thống sẽ **bỏ qua hoàn toàn** dòng đó (ghi nhận TT bằng `0` và không tính mới, hoặc đối trừ thẳng sang `ThucChayDaTinh`).
  - *Lưu ý phân biệt:* KHÔNG giống như nhóm CPM (sẽ tính một phần cho vừa khít phân bổ và ghi dôi dư vào `SoLuongThucChayLechTreoHa`). Chi phí khác sẽ loại bỏ toàn bộ record gây vượt.

---
*(Tài liệu này sẽ liên tục được cập nhật khi AI Agent tiến hành rà soát các nhóm sản phẩm mới từ REVIEW_CHECKLIST.md)*
