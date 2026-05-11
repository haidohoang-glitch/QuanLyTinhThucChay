# Stored Procedure: `CONTRACT_Get_DmWebsiteReportingdb`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-19 15:42:18.493000
- **Ngày sửa cuối**: 2017-06-19 15:42:39.867000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenWebsite` | `nvarchar(600)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 2016-07-17
-- Description:	Insert du lieu thuc chay dung chung cho cac san pham tinh theo phuong phap SelfServing

    	
CREATE PROCEDURE [dbo].[CONTRACT_Get_DmWebsiteReportingdb] 
	@TenWebsite NVARCHAR(300)
AS
BEGIN
	SELECT DmWebsiteReportingdbID, TenWebsite FROM dbo.DmWebsiteReportingdb
	WHERE 1=1 AND DeletedStatus = 0 
	AND TenWebsite LIKE N'%' + @TenWebsite + '%'
END


```
