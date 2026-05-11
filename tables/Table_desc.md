# Table: `Table_desc`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `NhomSanPham` | `NVARCHAR(100)` nullable |  |
| `TenBang` | `NVARCHAR(100)` nullable |  |
| `YNghiaCuaBang` | `NVARCHAR(1000)` nullable |  |
| `NhomSanPhamLevel1` | `NVARCHAR(100)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_Table_desc` | `ID` | PRIMARY KEY |
