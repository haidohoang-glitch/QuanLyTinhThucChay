# Table: `AdmarketUserLastRecharge`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdmarketUserLastRechargeID` | `BIGINT` PK IDENTITY |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(100)` nullable |  |
| `Code` | `NVARCHAR(30)` nullable |  |
| `UserID` | `INT` nullable |  |
| `UserName` | `NVARCHAR(200)` nullable |  |
| `LastDateRecharge` | `DATETIME` nullable |  |
| `RechargeMoney` | `BIGINT` nullable |  |
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
| `PK_AdmarketUserLastRecharge` | `AdmarketUserLastRechargeID` | PRIMARY KEY |
