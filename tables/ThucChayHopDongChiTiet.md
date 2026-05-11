# Table: `ThucChayHopDongChiTiet`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayHopDongChiTietID` | `INT` NN | ID Primary key của table ThucChayHopDongChiTiet |
| `HopDongREF` | `INT` nullable | ID foreign key của table HopDong (HopDongID) |
| `NhanHang` | `NVARCHAR(1000)` nullable | Tên nhãn hàng chạy của phân bổ (HopDongChiTiet) |
| `ThoiGianBatDau` | `DATETIME` nullable | Ngày bắt đầu chạy của đợt chạy của banner |
| `ThoiGianKetThuc` | `DATETIME` nullable | Ngày kết thúc chạy của banner |
| `Link` | `NVARCHAR(2000)` nullable | Link thông tin site chạy thực tế |
| `DmBannerREF` | `NVARCHAR(255)` nullable | ID của Banner |
| `TenBanner` | `NVARCHAR(255)` nullable | Tên banner |
| `ViTri` | `NVARCHAR(255)` nullable | Tên vị trí |
| `GhiChu` | `NVARCHAR(2555)` nullable |  |
| `BookingREF` | `INT` nullable | ID của Booking |
| `HopDongChiTietREF` | `INT` nullable | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `TypeThucChay` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `DmViTriREF` | `INT` nullable | ID của DmVitri |
| `DmNhanHangREF` | `NVARCHAR(200)` nullable | ID Foreign key từ table NhanHang |
| `SoLuongThucTreo` | `FLOAT` nullable | Thông tin số lượng treo |
| `SoLuongThucChay` | `FLOAT` nullable | Thông tin số lượng chạy |
| `DmDonViTinhREF` | `BIGINT` nullable | ID Foreign key từ table DmDonvitinh |
| `DonViTinh` | `NVARCHAR(200)` nullable | Mã đơn vị tính |
| `DmHinhThucQuangCaoREF` | `INT` nullable | ID Foreign key từ table DmHinhThucQuangCao |
| `TenHinhThucQuangCao` | `NVARCHAR(200)` nullable | Tên hình thức quảng cáo từ table DmHinhThucQuangCao |
| `DmSanPhamREF` | `INT` nullable | ID Foreign key từ table DmSanPham |
| `TenSanPham` | `NVARCHAR(200)` nullable | Tên sản phảm từ table DmSanPham |
| `InputType` | `INT` nullable | Nguồn dữ liệu phát sinh từ treo trên nhóm chi phí hay treo trên các nhóm Media ( = 0 |
| `IsReadBooking` | `INT` nullable |  |
| `KichThuoc` | `NVARCHAR(300)` nullable |  |
| `DonGia` | `FLOAT` nullable | Đơn giá của thực treo |
| `ChietKhau` | `FLOAT` nullable | Chiết khấu thực treo |
| `ThanhTien` | `FLOAT` nullable | Thành tiền sau chiết khấu của thực treo hoặc thực chạy |
| `Id` | `INT` PK IDENTITY | ID primary key tự tăng của table ThucChayHopDongChiTiet, ID phục vụ việc lấy dữ liệu của BI theo CDC |
| `LoaiThucTreo` | `NVARCHAR(50)` nullable | Loại thực treo là "ChiPhi", hay là không phải ChiPhi |
| `DmWebsiteREF` | `INT` nullable | ID Foreign key từ table DmWebsite |
| `TenWebsite` | `NVARCHAR(100)` nullable | Tên website từ table DmWebsite |
| `TrangThaiTreo` | `SMALLINT` nullable | Trạng thái nghiệp vụ của bản ghi thực treo |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csThucChayHopDongChiTiet` | `Id` | PRIMARY KEY |
| `nonix_DmBannerREF` | `DmBannerREF, DmSanPhamREF` | BTREE |
| `tchdct` | `HopDongChiTietREF, DeletedStatus, RecordStatus, ThoiGianBatDau` | BTREE |
| `ThucChayHDCT_1` | `ThoiGianBatDau, ThoiGianKetThuc, HopDongChiTietREF, DeletedStatus` | BTREE |
