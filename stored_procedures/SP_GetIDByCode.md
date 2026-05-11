# Stored Procedure: `GetIDByCode`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-23 08:52:30.837000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.977000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableName` | `nvarchar(100)` | No |
| `@ColumnName` | `nvarchar(100)` | No |
| `@ColumnValue` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
CREATE PROCEDURE [dbo].[GetIDByCode] 
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50),
	@ColumnName nvarchar(50),
	@ColumnValue nvarchar(50)
AS
BEGIN

	Declare @SQL nvarchar(4000)
	Declare @DauNhay nvarchar(50)
	
	set @DauNhay = ''''
	set @SQL = 'select '+@TableName+'ID'+' from '+ @TableName+' where [DeletedStatus] <> 1 and ' + @ColumnName + '=' + @DauNhay + @ColumnValue + @DauNhay
	EXEC sp_executesql @SQL



END

--exec [GetIDByCode] 'DmNgonNgu','MaNgonNgu','VN'

```
