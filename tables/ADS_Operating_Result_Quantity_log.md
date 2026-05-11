# Table: `ADS_Operating_Result_Quantity_log`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` NN IDENTITY |  |
| `ADS_Operating_Result_Quantity_Id` | `INT` NN |  |
| `D_Products_Id` | `INT` nullable |  |
| `Operating_Order_Id` | `INT` nullable |  |
| `Quantity` | `DECIMAL(18,4)` nullable |  |
| `UnitPrice` | `DECIMAL(18,4)` nullable |  |
| `TotalMoney` | `DECIMAL(18,4)` nullable |  |
| `FromDate` | `DATE` nullable |  |
| `ToDate` | `DATE` nullable |  |
| `UserConfirm` | `BIGINT` nullable |  |
| `DateConfirm` | `DATETIME2` nullable |  |
| `Status` | `INT` nullable |  |
| `CreatorUserId` | `NVARCHAR(50)` nullable |  |
| `CreationTime` | `DATETIME` nullable |  |
| `LastModificationTime` | `DATETIME` nullable |  |
| `LastModifierUserId` | `NVARCHAR(50)` nullable |  |
| `IsDeleted` | `SMALLINT` NN |  |
| `DeleterUserId` | `NVARCHAR(50)` nullable |  |
| `DeletionTime` | `DATETIME` nullable |  |
| `IsCalc_Result_Quantity` | `SMALLINT` nullable |  |
| `Log_time` | `DATETIME` NN |  |
