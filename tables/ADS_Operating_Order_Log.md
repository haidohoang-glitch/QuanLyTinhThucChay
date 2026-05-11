# Table: `ADS_Operating_Order_Log`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` NN IDENTITY |  |
| `ADS_Operating_Order_Id` | `INT` NN |  |
| `Code` | `NVARCHAR(500)` nullable |  |
| `Contract_Id` | `INT` nullable |  |
| `Contract_Number` | `VARCHAR(100)` nullable |  |
| `Submitting_Number` | `NVARCHAR(500)` nullable |  |
| `Contract_Detail_Id` | `INT` nullable |  |
| `Product_Id` | `INT` nullable |  |
| `Brand_id` | `INT` nullable |  |
| `Money_Turnover` | `MONEY` nullable |  |
| `From_Date` | `DATETIME` nullable |  |
| `To_Date` | `DATETIME` nullable |  |
| `Campaign_Type` | `INT` nullable |  |
| `KPI` | `DECIMAL(18,4)` nullable |  |
| `Team` | `NVARCHAR(500)` nullable |  |
| `SetupBy` | `NVARCHAR(100)` nullable |  |
| `Start_Time` | `DATETIME` nullable |  |
| `Receive_Time` | `DATETIME` nullable |  |
| `ReceivedBy` | `NVARCHAR(100)` nullable |  |
| `Units` | `NVARCHAR(500)` nullable |  |
| `ProfitRate` | `DECIMAL(18,4)` nullable |  |
| `Note` | `NVARCHAR(2000)` nullable |  |
| `Status` | `INT` nullable |  |
| `CreationTime` | `DATETIME2` nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |
| `LastModificationTime` | `DATETIME2` nullable |  |
| `LastModifiedBy` | `NVARCHAR(100)` nullable |  |
| `IsDeleted` | `SMALLINT` NN |  |
| `Deletedby` | `NVARCHAR(100)` nullable |  |
| `DeletionTime` | `DATETIME2` nullable |  |
| `Log_time` | `DATETIME` NN |  |
| `DmWebsiteREF` | `INT` nullable |  |
