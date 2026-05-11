# Table: `ThucChayAdmarketOnlineHistory`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayAdmarketOnlineHistoryID` | `NVARCHAR(50)` PK |  |
| `DayHistory` | `DATETIME` nullable |  |
| `ThucChayAdmarketOnlineID` | `NVARCHAR(50)` NN |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `TaiKhoan` | `NVARCHAR(50)` nullable |  |
| `TotalView` | `BIGINT` DEFAULT 0 nullable |  |
| `TotalClick` | `BIGINT` DEFAULT 0 nullable |  |
| `SoLuong` | `BIGINT` DEFAULT 0 nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `TienThucChay` | `FLOAT` DEFAULT 0 nullable |  |
| `TienKhuyenMai` | `FLOAT` DEFAULT 0 nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `IsNoiBo` | `INT` nullable |  |
| `GhiChu` | `NVARCHAR(255)` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(50)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayAdmarketOnlineHistory` | `ThucChayAdmarketOnlineHistoryID` | PRIMARY KEY |
