# Table: `ThucChayAdmarketTotal`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayAdmarketTotalID` | `INT` PK IDENTITY |  |
| `NgayThucHien` | `DATETIME` NN |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `TongClick` | `BIGINT` nullable |  |
| `TongView` | `BIGINT` nullable |  |
| `TongTienThucChay` | `FLOAT` nullable |  |
| `TongTienKhuyenMai` | `FLOAT` nullable |  |
| `GhiChu` | `NVARCHAR(255)` nullable |  |
| `DataType` | `INT` nullable | =1: Theo Domain;<br>=2: Theo HopDong;<br>=3: Theo Sale; |
| `CreatedBy` | `NVARCHAR(50)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `NonClusteredIndex-1` | `NgayThucHien, DmSanPhamREF, DataType` | BTREE |
| `PK_ThucChayAdmarketTotal` | `ThucChayAdmarketTotalID` | PRIMARY KEY |
