# Stored Procedure: `spx_ImportFromExcel07`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-08 16:05:33.773000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.430000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SheetName` | `varchar(20)` | No |
| `@FilePath` | `varchar(100)` | No |
| `@HDR` | `varchar(3)` | No |
| `@TableName` | `varchar(50)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[spx_ImportFromExcel07]
	@SheetName varchar(20),
    @FilePath varchar(100),
	@HDR varchar(3),
	@TableName varchar(50)
AS
BEGIN
    DECLARE @SQL nvarchar(1000)
	
	IF OBJECT_ID (@TableName,'U') IS NOT NULL
		SET @SQL = 'INSERT INTO ' + @TableName + ' SELECT * FROM OPENDATASOURCE'
	ELSE
		SET @SQL = 'SELECT * INTO ' + @TableName + ' FROM OPENDATASOURCE'

    SET @SQL = @SQL + '(''Microsoft.ACE.OLEDB.12.0'',''Data Source='
    SET @SQL = @SQL + @FilePath + ';Extended Properties=''''Excel 12.0;HDR=' 
    SET @SQL = @SQL + @HDR + ''''''')...[' 
    SET @SQL = @SQL + @SheetName + ']'
	EXEC sp_executesql @SQL
END

```
