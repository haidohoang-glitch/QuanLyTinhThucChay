# Table: `DmTinhThanhPho`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmTinhThanhPhoID` | `INT` PK |  |
| `MaTinhThanhPho` | `NVARCHAR(50)` nullable |  |
| `TenTinhThanhPho` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(4000)` nullable |  |
| `Active` | `INT` NN |  |
| `CreatedBy` | `NVARCHAR(50)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `DmDatNuocREF` | `INT` nullable |  |
| `ThuTuHienThi` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csDmTinhThanhPho` | `DmTinhThanhPhoID` | PRIMARY KEY |
