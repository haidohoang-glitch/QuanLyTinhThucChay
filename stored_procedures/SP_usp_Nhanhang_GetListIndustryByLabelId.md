# Stored Procedure: `usp_Nhanhang_GetListIndustryByLabelId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:45.553000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.130000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <20.01.2014>
-- Description:	<Description,,>
-- =============================================
--[usp_Nhanhang_GetListIndustryByLabelId] 1755
CREATE PROCEDURE [dbo].[usp_Nhanhang_GetListIndustryByLabelId] 
	@DmNhanHangId INT
AS
BEGIN
	DECLARE @SQL NVARCHAR(MAX);
	SET @SQL = '
	    SELECT DmNghanhHangID AS Id, TenNghanhHang AS [Name]           
	    FROM DmNghanhHang n
	    WHERE n.DeletedStatus <> 1 AND n.DmNghanhHangID IN ('
					 + CONVERT(NVARCHAR(512), (SELECT DmNghanhHangREF FROM DmNhanHang WHERE DmNhanHangID = @DmNhanHangId)) +')'
	PRINT @SQL;
	
	EXEC sp_executesql @SQL;	
END

```
