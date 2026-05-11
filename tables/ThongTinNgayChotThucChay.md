# Table: `ThongTinNgayChotThucChay`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `F_NgayThucHien` | `DATETIME` NN |  |
| `E_NgayThucHien` | `DATETIME` NN |  |
| `TrangThaiChot` | `SMALLINT` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `CreatedBy` | `NVARCHAR(50)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` NN |  |
| `DeletedStatus` | `SMALLINT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThongTinNgayChotThucChay` | `ID` | PRIMARY KEY |
