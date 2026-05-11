# Table: `ADS_Operating_Result_Quantity`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK |  |
| `D_Products_Id` | `INT` nullable |  |
| `Operating_Order_Id` | `INT` nullable |  |
| `Quantity` | `DECIMAL(18,4)` nullable |  |
| `UnitPrice` | `DECIMAL(18,4)` nullable |  |
| `TotalMoney` | `DECIMAL(18,4)` nullable |  |
| `FromDate` | `DATE` nullable |  |
| `ToDate` | `DATE` nullable |  |
| `UserConfirm` | `BIGINT` nullable |  |
| `DateConfirm` | `DATETIME2` nullable |  |
| `Status` | `INT` nullable | 1: thêm mới, 2: chốt, 3: hủy |
| `CreatorUserId` | `NVARCHAR(50)` nullable |  |
| `CreationTime` | `DATETIME` nullable |  |
| `LastModificationTime` | `DATETIME` nullable |  |
| `LastModifierUserId` | `NVARCHAR(50)` nullable |  |
| `IsDeleted` | `SMALLINT` NN |  |
| `DeleterUserId` | `NVARCHAR(50)` nullable |  |
| `DeletionTime` | `DATETIME` nullable |  |
| `IsCalc_Result_Quantity` | `SMALLINT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ADS_Operating_Result_Quantity` | `Id` | PRIMARY KEY |
