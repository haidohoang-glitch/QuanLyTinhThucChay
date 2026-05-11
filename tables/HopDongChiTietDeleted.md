# Table: `HopDongChiTietDeleted`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongChiTietDeletedID` | `INT` PK |  |
| `HopDongChiTietID` | `INT` NN |  |
| `NgayThucHien` | `DATETIME` NN |  |
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
| `PK_HopDongChiTietDeleted` | `HopDongChiTietDeletedID` | PRIMARY KEY |
