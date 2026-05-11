# Table: `DmDoiTuongQuyen`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmDoiTuongQuyenID` | `INT` PK |  |
| `TenDoiTuongQuyen` | `NVARCHAR(200)` nullable |  |
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
| `PK_DmDoiTuongQuyen` | `DmDoiTuongQuyenID` | PRIMARY KEY |
