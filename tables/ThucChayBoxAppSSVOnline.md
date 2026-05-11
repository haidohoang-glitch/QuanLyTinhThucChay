# Table: `ThucChayBoxAppSSVOnline`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayBoxAppSSVOnlineID` | `NVARCHAR(50)` PK |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(50)` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `SoLuongThucChay` | `INT` DEFAULT 0 nullable |  |
| `ThanhTienThucChay` | `FLOAT` DEFAULT 0 nullable |  |
| `SoLuongKhuyenMai` | `INT` DEFAULT 0 nullable |  |
| `ThanhTienKhuyenMai` | `FLOAT` DEFAULT 0 nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `GhiChu` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModfiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayBoxAppSSVOnline` | `ThucChayBoxAppSSVOnlineID` | PRIMARY KEY |
