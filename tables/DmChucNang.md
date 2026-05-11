# Table: `DmChucNang`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmChucNangID` | `INT` PK |  |
| `TenChucNang` | `NVARCHAR(200)` nullable |  |
| `Code` | `NVARCHAR(200)` nullable |  |
| `ParentCode` | `NVARCHAR(200)` nullable |  |
| `TenHienThi` | `NVARCHAR(200)` nullable |  |
| `ThuTuHienThi` | `NVARCHAR(200)` nullable |  |
| `HasChildren` | `BIGINT` nullable |  |
| `TrangThai` | `INT` nullable |  |
| `Description` | `NVARCHAR(200)` nullable |  |
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
| `PK_DmChucNang` | `DmChucNangID` | PRIMARY KEY |
