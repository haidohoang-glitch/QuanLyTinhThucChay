# Table: `DmDatNuoc`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmDatNuocID` | `INT` PK |  |
| `MaDatNuoc` | `NVARCHAR(50)` nullable |  |
| `TenDatNuoc` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(4000)` nullable |  |
| `Active` | `INT` NN |  |
| `CreatedBy` | `NVARCHAR(1)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(1)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csDmDatNuoc` | `DmDatNuocID` | PRIMARY KEY |
