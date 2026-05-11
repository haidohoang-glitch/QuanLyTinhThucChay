# Table: `ThucChayHopDongChiTietLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayHopDongChiTietLogID` | `BIGINT` PK IDENTITY |  |
| `ThucChayHopDongChiTietID` | `BIGINT` nullable |  |
| `HopDongREF` | `BIGINT` nullable |  |
| `HopDongChiTietREF` | `BIGINT` nullable |  |
| `DmBannerREF` | `NVARCHAR(200)` nullable |  |
| `TenBanner` | `NVARCHAR(200)` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `ViTri` | `NVARCHAR(200)` nullable |  |
| `DmNhanHangREF` | `NVARCHAR(200)` nullable |  |
| `NhanHang` | `NVARCHAR(200)` nullable |  |
| `BookingREF` | `BIGINT` nullable |  |
| `ThoiGianBatDau` | `DATE` nullable |  |
| `ThoiGianKetThuc` | `DATE` nullable |  |
| `SoLuongThucTreo` | `FLOAT` nullable |  |
| `SoLuongThucChay` | `FLOAT` nullable |  |
| `DmDonViTinhREF` | `INT` nullable |  |
| `DonViTinh` | `NVARCHAR(200)` nullable |  |
| `TypeThucChay` | `INT` nullable |  |
| `Link` | `NVARCHAR(MAX)` nullable |  |
| `GhiChu` | `NVARCHAR(MAX)` nullable |  |
| `DmHinhThucQuangCaoREF` | `INT` nullable |  |
| `TenHinhThucQuangCao` | `NVARCHAR(200)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(200)` nullable |  |
| `InputType` | `INT` nullable |  |
| `IsReadBooking` | `INT` nullable |  |
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
| `LoaiThucTreo` | `NVARCHAR(100)` nullable |  |
| `DonGia` | `FLOAT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `TrangThaiTreo` | `INT` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(200)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `index_log` | `ThucChayHopDongChiTietID, HopDongREF, HopDongChiTietREF` | BTREE |
| `PK_ThucChayHopDongChiTietLog` | `ThucChayHopDongChiTietLogID` | PRIMARY KEY |
