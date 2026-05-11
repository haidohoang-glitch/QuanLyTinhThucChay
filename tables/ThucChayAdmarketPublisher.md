# Table: `ThucChayAdmarketPublisher`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayAdmarketPublisherID` | `INT` PK IDENTITY |  |
| `DmHinhThucQuangCao` | `INT` DEFAULT 7 nullable |  |
| `TenHinhThucQuangCao` | `NVARCHAR(50)` DEFAULT N'CPC' nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `SiteID` | `INT` NN |  |
| `SiteName` | `NVARCHAR(50)` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(50)` nullable |  |
| `ttClick` | `BIGINT` nullable |  |
| `ttView` | `INT` nullable |  |
| `Price` | `FLOAT` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `IsPheDuyet` | `INT` nullable |  |
| `PheDuyetBy` | `NVARCHAR(50)` nullable |  |
| `PheDuyetAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(1)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(1)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csThucChayAdmarketPublisher` | `ThucChayAdmarketPublisherID` | PRIMARY KEY |
