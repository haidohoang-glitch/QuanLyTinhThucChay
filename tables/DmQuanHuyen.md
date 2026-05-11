# Table: `DmQuanHuyen`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmQuanHuyenID` | `INT` PK |  |
| `DmTinhThanhPhoREF` | `INT` NN |  |
| `TenQuanHuyen` | `NVARCHAR(200)` nullable |  |
| `ThuTuHienThi` | `INT` nullable |  |
| `Active` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(200)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmQuanHuyen` | `DmQuanHuyenID` | PRIMARY KEY |
