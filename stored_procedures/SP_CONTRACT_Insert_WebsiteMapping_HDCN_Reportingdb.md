# Stored Procedure: `CONTRACT_Insert_WebsiteMapping_HDCN_Reportingdb`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-19 15:55:18.337000
- **Ngày sửa cuối**: 2017-06-19 15:55:18.337000

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
CREATE PROCEDURE [dbo].[CONTRACT_Insert_WebsiteMapping_HDCN_Reportingdb] 
	@Dmwebsite_HDCN_ID INT,
	@Dmwebsite_Reportingdb_ID INT
AS
BEGIN
	DECLARE @v_WebsiteLink NVARCHAR(1000) = ''
IF(EXISTS(SELECT DmWebsiteID, WebsiteLink, DmWebsiteReportingdbID FROM dbo.WebsiteMapping_HDCN_Reporting
	WHERE 1=1 
	AND (DmWebsiteID = @Dmwebsite_HDCN_ID OR DmWebsiteReportingdbID = @Dmwebsite_Reportingdb_ID))
	)
	PRINT 'KHong lam gi ca'
ELSE
	BEGIN
		SET @v_WebsiteLink =
		(
			SELECT TOP 1 TenWebsite FROM dbo.DmWebsiteReportingdb
			WHERE DmWebsiteReportingdbID =  @Dmwebsite_Reportingdb_ID
		)
			INSERT dbo.WebsiteMapping_HDCN_Reporting
					( DmWebsiteID ,
					  WebsiteLink ,
					  DmWebsiteReportingdbID
					)
			VALUES  (@Dmwebsite_HDCN_ID , -- DmWebsiteID - int
					  @v_WebsiteLink , -- WebsiteLink - nvarchar(200)
					  @Dmwebsite_Reportingdb_ID  -- DmWebsiteReportingdbID - int
					)
	END

END




```
