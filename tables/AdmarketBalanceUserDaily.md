# Table: `AdmarketBalanceUserDaily`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdmarketBalanceUserDailyID` | `BIGINT` PK IDENTITY |  |
| `Code` | `NVARCHAR(200)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(200)` nullable |  |
| `UserID` | `INT` nullable |  |
| `UserName` | `NVARCHAR(200)` nullable |  |
| `DateCreated` | `DATETIME` nullable |  |
| `UserBalance` | `BIGINT` nullable |  |
| `UserPromotion` | `BIGINT` nullable |  |
| `EchargeMoney` | `BIGINT` nullable |  |
| `SpentBalance` | `BIGINT` nullable |  |
| `SpentPromotion` | `BIGINT` nullable |  |
| `NgayThucHien` | `DATE` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `DeletedStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AdmarketBalanceUserDaily` | `AdmarketBalanceUserDailyID` | PRIMARY KEY |
