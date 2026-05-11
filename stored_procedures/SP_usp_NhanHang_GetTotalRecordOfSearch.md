# Stored Procedure: `usp_NhanHang_GetTotalRecordOfSearch`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:41.920000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.377000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@RecordStatus` | `varchar(10)` | No |
| `@TenNhanhang` | `nvarchar(2048)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_GetTotalRecordOfSearch]
	@PageIndex INT = 1,
	@RecordCount INT = 2,
	@RecordStatus VARCHAR(10),
	@TenNhanhang NVARCHAR(1024)
	
AS
BEGIN
	SET NOCOUNT ON;
	--SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	DECLARE @SQL NVARCHAR(MAX);
	
	DECLARE @Review VARCHAR(20);
	DECLARE @sTenNhanhang NVARCHAR(256);		
	set @TenNhanhang = replace(@TenNhanhang,'''', '''''')
	
	IF (@RecordStatus = '')
	    SET @Review = 'AND RecordStatus >=0'
	ELSE
	    SET @Review = 'AND RecordStatus =' + @RecordStatus;
	
	IF (@TenNhanhang <> '')
		SET @sTenNhanhang = 'AND TenNhanHang COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N''%'+ @TenNhanhang +'%''';
	ELSE
		SET @sTenNhanhang = ' ';
		
	SET @SQL = '
		
		SELECT COUNT([DmNhanHangID]) As TotalRecord
	    FROM   DmNhanHang
	    WHERE  DeletedStatus <> 1 '+ @sTenNhanhang + ' ' + @Review + ';';
		
	PRINT @SQL;
	
	EXEC sp_executesql @SQL;
END

```
