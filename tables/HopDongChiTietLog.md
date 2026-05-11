# Table: `HopDongChiTietLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongChiTietLogID` | `INT` PK IDENTITY | ID primary key của table HopDongChiTietLog phát sinh tự tăng trên table syn xử lý |
| `HopDongChiTietREF` | `INT` NN | ID Foreign key từ table HopDongChiTiet (HopDongChiTietID) |
| `HopDongFK` | `INT` NN | ID Foreign key từ table HopDong (HopDongID) |
| `DanhSachNhanHangREF` | `NVARCHAR(250)` nullable | DanhSachNhanHangREF từ table HopDongChiTiet |
| `NhanHang` | `NVARCHAR(2000)` nullable |  |
| `DmNhomNganhREF` | `NVARCHAR(300)` nullable |  |
| `TenNhomNganh` | `NVARCHAR(2000)` nullable |  |
| `DmLoaiREF` | `BIGINT` nullable |  |
| `TenLoai` | `NVARCHAR(500)` nullable |  |
| `DmNhomWebsiteREF` | `NVARCHAR(500)` nullable |  |
| `TenNhomWebsite` | `NVARCHAR(300)` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(200)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(500)` nullable |  |
| `DmLoaiBannerREF` | `INT` nullable |  |
| `TenLoaiBanner` | `NVARCHAR(300)` nullable |  |
| `DmChuyenMucREF` | `INT` nullable |  |
| `TenChuyenMuc` | `NVARCHAR(500)` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
| `TenBanner` | `NVARCHAR(500)` nullable |  |
| `ThoiGian` | `NVARCHAR(200)` nullable |  |
| `SoLuong` | `BIGINT` nullable |  |
| `DonViTinhREF` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(200)` nullable |  |
| `DonGia` | `FLOAT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `GiamGia` | `FLOAT` nullable |  |
| `TiLeTuVan` | `FLOAT` nullable |  |
| `KhuyenMai` | `NVARCHAR(200)` nullable |  |
| `IsKhuyenMai` | `INT` nullable |  |
| `ChiPhiTuVan` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `GhiChu` | `NVARCHAR(MAX)` nullable |  |
| `DmSanphamREF_old` | `BIGINT` nullable |  |
| `TK_AdMarket` | `NVARCHAR(1000)` nullable |  |
| `TK_AdMarketID` | `NVARCHAR(200)` nullable |  |
| `SoLuongThucChay` | `FLOAT` nullable |  |
| `ThanhTienThucChay` | `FLOAT` nullable |  |
| `TrangThaiThucChay` | `INT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `ThoiGianKetThuc` | `DATETIME` nullable |  |
| `ThucChayDenNgay` | `DATETIME` nullable |  |
| `ThoiGianLog` | `DATETIME` nullable |  |
| `NguoiLog` | `NVARCHAR(200)` nullable |  |
| `LoaiLog` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `contract_detail_log_id` | `BIGINT` nullable | ID từ table nguồn Contract_details nghiệp vụ |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_HopDongChiTietLog` | `HopDongChiTietLogID` | PRIMARY KEY |
