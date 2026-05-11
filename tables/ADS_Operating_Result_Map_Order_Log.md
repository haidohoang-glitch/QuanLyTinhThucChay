# Table: `ADS_Operating_Result_Map_Order_Log`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` NN IDENTITY |  |
| `ADS_Operating_Result_Map_Order_Id` | `INT` NN |  |
| `Operating_Order_Id` | `INT` nullable |  |
| `operating_Result_Id` | `INT` nullable |  |
| `Result` | `DECIMAL(18,4)` nullable |  |
| `Sell_Money_VND` | `DECIMAL(18,4)` nullable |  |
| `CreationTime` | `DATETIME2` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModificationTime` | `DATETIME2` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `IsDeleted` | `SMALLINT` nullable |  |
| `DeletedBy` | `NVARCHAR(50)` nullable |  |
| `DeletionTime` | `DATETIME2` nullable |  |
| `IsCaculatedActual` | `SMALLINT` nullable |  |
| `Log_time` | `DATETIME` NN |  |
