# Table: `DmWebsite`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmWebsiteID` | `INT` PK |  |
| `TenWebsite` | `NVARCHAR(200)` nullable |  |
| `WebsiteLink` | `NVARCHAR(255)` nullable |  |
| `GhiChu` | `NVARCHAR(4000)` nullable |  |
| `Code` | `NVARCHAR(200)` nullable |  |
| `DmGroupTypeREF` | `INT` nullable |  |
| `IsThuongMaiDienTu` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `DomainWebsite` | `NVARCHAR(200)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csDmWebsite` | `DmWebsiteID` | PRIMARY KEY |
