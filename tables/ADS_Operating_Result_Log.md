# Table: `ADS_Operating_Result_Log`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` NN IDENTITY |  |
| `ADS_Operating_Result_Id` | `INT` NN |  |
| `Product Id` | `INT` nullable |  |
| `Product Name` | `NVARCHAR(50)` nullable |  |
| `Operating_Order_Id` | `INT` nullable |  |
| `AdAccount_Name` | `NVARCHAR(500)` nullable |  |
| `AdAccount_Id` | `NVARCHAR(500)` nullable |  |
| `Campaign_Id` | `NVARCHAR(500)` nullable |  |
| `Campaign_Name` | `NVARCHAR(500)` nullable |  |
| `Exchange_Rate_Id` | `INT` nullable |  |
| `Exchange_Rate` | `DECIMAL(18,4)` nullable |  |
| `Start_Date` | `DATETIME` nullable |  |
| `Result_Type` | `NVARCHAR(100)` nullable |  |
| `Result` | `DECIMAL(18,4)` nullable |  |
| `Reach` | `DECIMAL(18,4)` nullable |  |
| `Impression` | `DECIMAL(18,4)` nullable |  |
| `Amoun_Spent` | `DECIMAL(18,4)` nullable |  |
| `Frequency` | `DECIMAL(18,4)` nullable |  |
| `CPC` | `DECIMAL(18,4)` nullable |  |
| `CTR` | `DECIMAL(18,4)` nullable |  |
| `Cost_Per_Result` | `DECIMAL(18,4)` nullable |  |
| `Clicks` | `DECIMAL(18,4)` nullable |  |
| `CPM` | `DECIMAL(18,4)` nullable |  |
| `Cost_Per_Thousand_People_Reached` | `DECIMAL(18,4)` nullable |  |
| `Page_Likes` | `DECIMAL(18,4)` nullable |  |
| `Post_Engagement` | `DECIMAL(18,4)` nullable |  |
| `Cost_Per_Page_Like` | `DECIMAL(18,4)` nullable |  |
| `Cost_Per_Post_Engagement` | `DECIMAL(18,4)` nullable |  |
| `Leads` | `DECIMAL(18,4)` nullable |  |
| `Total_Money_VND` | `DECIMAL(18,4)` nullable |  |
| `Sell_Money_VND` | `DECIMAL(18,4)` nullable |  |
| `View` | `DECIMAL(18,4)` nullable |  |
| `Conversions` | `DECIMAL(18,4)` nullable |  |
| `CPV` | `DECIMAL(18,4)` nullable |  |
| `CreationTime` | `DATETIME2` nullable |  |
| `Age` | `NVARCHAR(100)` nullable |  |
| `Sex` | `INT` nullable |  |
| `Regions` | `NVARCHAR(100)` nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |
| `LastModificationTime` | `DATETIME2` nullable |  |
| `LastModifiedBy` | `NVARCHAR(100)` nullable |  |
| `IsDeleted` | `SMALLINT` NN |  |
| `DeletedBy` | `NVARCHAR(100)` nullable |  |
| `DeletionTime` | `DATETIME2` nullable |  |
| `Date_result` | `DATE` nullable |  |
| `Log_time` | `DATETIME` NN |  |
