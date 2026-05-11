# Table: `ThucChayDaTinhBySanPhamThoiGian`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayDaTinhBySanPhamThoiGianID` | `NVARCHAR(50)` PK |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `DmHinhThucQuangCao` | `INT` nullable |  |
| `TenHinhThucQuangCao` | `NVARCHAR(50)` nullable |  |
| `HopDongID` | `INT` nullable |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `DmMaHopDongREF` | `INT` nullable |  |
| `TenMaHopDong` | `NVARCHAR(50)` nullable |  |
| `DmPhongBanREF` | `INT` nullable |  |
| `TenPhongBan` | `NVARCHAR(50)` nullable |  |
| `DmBoPhanREF` | `INT` nullable |  |
| `TenBoPhan` | `NVARCHAR(50)` nullable |  |
| `DmNhomLamViecREF` | `INT` nullable |  |
| `TenNhomLamViec` | `NVARCHAR(50)` nullable |  |
| `SysNhanVienREF` | `INT` nullable |  |
| `TenDangNhap` | `NVARCHAR(50)` nullable |  |
| `TenNhanVien` | `NVARCHAR(255)` nullable |  |
| `SoLuongThucChayNoiBo` | `BIGINT` nullable |  |
| `SoLuongThucChayKhuyenMai` | `BIGINT` nullable |  |
| `SoLuongThucChay` | `BIGINT` nullable |  |
| `ThanhTienThucChayNoiBo` | `FLOAT` nullable |  |
| `ThanhTienThucChayKhuyenMai` | `FLOAT` nullable |  |
| `ThanhTienThucChay` | `FLOAT` nullable |  |
| `GiaTriThayDoiNoiBo` | `FLOAT` nullable |  |
| `GiaTriThayDoiThucChay` | `FLOAT` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `GhiChu` | `NVARCHAR(512)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayDaTinhBySanPhamThoiGian` | `ThucChayDaTinhBySanPhamThoiGianID` | PRIMARY KEY |
