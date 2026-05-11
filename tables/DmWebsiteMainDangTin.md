# Table: `DmWebsiteMainDangTin`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmWebsiteMainDangTinID` | `INT` PK |  |
| `TenWebsite` | `NVARCHAR(200)` nullable |  |
| `DmDomainWebsiteID` | `INT` nullable |  |
| `TenDomainWebsite` | `NVARCHAR(200)` nullable |  |
| `Code` | `NVARCHAR(100)` nullable |  |
| `ListDomainWebsite` | `NVARCHAR(1000)` nullable |  |
| `Note` | `NVARCHAR(500)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmWebsiteMainDangTin` | `DmWebsiteMainDangTinID` | PRIMARY KEY |
