# Stored Procedure: `usp_NganhHang_GetListNameByListId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:31.150000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.387000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@LstNganhId` | `nvarchar(2048)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <20.01.2014>
-- Description:	<Description,,>
-- =============================================
--[usp_NganhHang_GetListNameByListId] '1, 2, 3'
CREATE PROCEDURE [dbo].[usp_NganhHang_GetListNameByListId] 
	@LstNganhId NVARCHAR(1024)
AS
BEGIN
	DECLARE @SQL NVARCHAR(MAX)	
	IF(@LstNganhId <> '')
		SET @SQL = 'SELECT STUFF((SELECT ''; '' + TenNghanhHang
					FROM DmNghanhHang
					WHERE DmNghanhHangID IN (' + @LstNganhId + ')
					FOR XML PATH('''')), 1, 1, '''') AS LstIndustryName' 
	    
	PRINT @SQL
	
	EXEC (@SQL)	
END

```
