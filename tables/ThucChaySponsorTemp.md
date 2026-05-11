# Table: `ThucChaySponsorTemp`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChaySponsorId` | `INT` PK IDENTITY |  |
| `typeproduct` | `INT` nullable |  |
| `ProductId` | `INT` nullable |  |
| `ProductName` | `NVARCHAR(50)` nullable |  |
| `Contract` | `NVARCHAR(50)` nullable |  |
| `CampaignId` | `INT` nullable |  |
| `BannerId` | `INT` nullable |  |
| `BannerType` | `INT` nullable |  |
| `SiteId` | `BIGINT` nullable |  |
| `SiteName` | `NVARCHAR(50)` nullable |  |
| `dt` | `DATETIME` nullable |  |
| `TotalView` | `BIGINT` nullable |  |
| `TotalClick` | `BIGINT` nullable |  |
| `UnitID` | `INT` nullable |  |
| `UnitName` | `NVARCHAR(50)` nullable | 1: Click
2: View |
| `Activate` | `DATETIME` nullable |  |
| `Expire` | `DATETIME` nullable |  |
| `UserName` | `NVARCHAR(50)` nullable |  |
| `SaleName` | `NVARCHAR(1024)` nullable |  |
| `Email` | `NVARCHAR(512)` nullable |  |
| `HopDongChiTietRER` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChaySponsorTemp` | `ThucChaySponsorId` | PRIMARY KEY |
