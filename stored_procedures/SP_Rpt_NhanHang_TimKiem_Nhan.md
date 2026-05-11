# Stored Procedure: `Rpt_NhanHang_TimKiem_Nhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-21 10:54:30.040000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.237000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Keyword` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- Rpt_NhanHang_TimKiem_Nhan 'Close-up Valentine'
CREATE  PROC [dbo].[Rpt_NhanHang_TimKiem_Nhan]	
	@Keyword NVARCHAR(4000)	
AS
BEGIN
	DECLARE @SQL NVARCHAR(MAX);
	DECLARE @LabelName NVARCHAR(512);	
	SET @Keyword = replace(@Keyword,'''', '''''')
	
	IF (@Keyword <> '')
		SET @LabelName = 'TenNhanHang COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N''%' + @Keyword + '%''';
	ELSE
		SET @LabelName = ' ';
	
	SET @SQL = '
	SELECT TOP 30 DmNhanHangId, TenNhanHang FROM DmNhanHang dnh
	WHERE ' + @LabelName + ' AND dnh.RecordStatus = 1 AND dnh.DeletedStatus = 0
	ORDER BY dnh.TenNhanHang ASC'
	
	PRINT @SQL;
	
	EXEC sp_executesql @SQL;
	
	--DECLARE @Sql NVARCHAR(4000)
	--SET @Sql = 'SELECT TOP 50 DmNhanHangId, TenNhanHang FROM DmNhanHang dnh
	--			WHERE (' + @Keyword + ') AND dnh.RecordStatus = 1 AND dnh.DeletedStatus <> 1
	--			ORDER BY dnh.TenNhanHang ASC'	
	--PRINT @Sql 
	--EXEC (@Sql)	
END

```
