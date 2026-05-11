# Table: `DmTaiKhoanAdmarket`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmTaiKhoanAdmarketID` | `NVARCHAR(100)` PK |  |
| `TenTaiKhoanAdMarket` | `NVARCHAR(2000)` NN |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmTaiKhoanAdmarket` | `DmTaiKhoanAdmarketID` | PRIMARY KEY |
