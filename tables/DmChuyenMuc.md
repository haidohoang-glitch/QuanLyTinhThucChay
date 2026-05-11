# Table: `DmChuyenMuc`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmChuyenMucID` | `INT` PK |  |
| `TenChuyenMuc` | `NVARCHAR(200)` NN |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `BIGINT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmChuyenMuc` | `DmChuyenMucID` | PRIMARY KEY |
