# Stored Procedure: `CONTRACT_Get_WebsiteMapping_HDCN_Reportingdb`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-19 15:51:11.847000
- **Ngày sửa cuối**: 2017-06-19 15:51:11.847000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Dmwebsite_HDCN_ID` | `int(4)` | No |
| `@Dmwebsite_Reportingdb_ID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 2016-07-17
-- Description:	Insert du lieu thuc chay dung chung cho cac san pham tinh theo phuong phap SelfServing

/*
exec [dbo].[CONTRACT_Get_DmWebsiteReportingdb] 'dantri'
*/    	
CREATE PROCEDURE [dbo].[CONTRACT_Get_WebsiteMapping_HDCN_Reportingdb] 
	@Dmwebsite_HDCN_ID INT,
	@Dmwebsite_Reportingdb_ID INT
AS
BEGIN
	SELECT DmWebsiteID, WebsiteLink, DmWebsiteReportingdbID FROM dbo.WebsiteMapping_HDCN_Reporting
	WHERE 1=1 
	AND (DmWebsiteID = @Dmwebsite_HDCN_ID OR DmWebsiteReportingdbID = @Dmwebsite_Reportingdb_ID)

END




```
