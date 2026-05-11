# Table: `DmNhom`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmNhomID` | `INT` PK |  |
| `TenNhom` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(255)` nullable |  |
| `DmBoPhanREF` | `INT` NN |  |
| `CreatedBy` | `NVARCHAR(50)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csDmNhom` | `DmNhomID` | PRIMARY KEY |
