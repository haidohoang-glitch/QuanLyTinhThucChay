# Table: `HopDongAdmarketCanhBao`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongAdmarketCanhbaoID` | `NVARCHAR(50)` PK |  |
| `HopDongID` | `INT` nullable |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `HopDongChiTietID` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `TK_Admarket` | `NVARCHAR(50)` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(50)` nullable |  |
| `SaleID` | `INT` nullable |  |
| `UserNameSale` | `NVARCHAR(50)` nullable |  |
| `TenSale` | `NVARCHAR(50)` nullable |  |
| `NgayThucHien` | `DATE` nullable |  |
| `SoluongThucChay` | `INT` nullable |  |
| `GiaTriThucChay` | `FLOAT` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `DeletedStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_HopDongAdmarketCanhBao` | `HopDongAdmarketCanhbaoID` | PRIMARY KEY |
