# Table: `ADS_Operating_Order`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` NN |  |
| `Code` | `NVARCHAR(100)` nullable |  |
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
| `Team` | `NVARCHAR(100)` nullable |  |
| `SetupBy` | `NVARCHAR(100)` nullable |  |
| `Start_Time` | `DATETIME` nullable |  |
| `Receive_Time` | `DATETIME` nullable |  |
| `ReceivedBy` | `NVARCHAR(100)` nullable |  |
| `Units` | `NVARCHAR(200)` nullable |  |
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
| `DmWebsiteREF` | `INT` nullable |  |
