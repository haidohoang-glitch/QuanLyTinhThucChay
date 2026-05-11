# Table: `DmSanPham`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmSanPhamID` | `INT` PK |  |
| `TenSanPham` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(4000)` nullable |  |
| `Code` | `NVARCHAR(200)` nullable |  |
| `DmNhomSanPhamREF` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `MaSanPham` | `NVARCHAR(200)` nullable |  |
| `Loai_Treo` | `SMALLINT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmSanPham` | `DmSanPhamID` | PRIMARY KEY |
