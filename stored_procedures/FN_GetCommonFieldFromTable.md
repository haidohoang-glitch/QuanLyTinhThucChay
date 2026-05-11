# Function: `GetCommonFieldFromTable`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-23 08:52:32.570000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.030000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@FieldList` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[GetCommonFieldFromTable] 
(
	-- Add the parameters for the function here
	@FieldList nvarchar(4000)
)
RETURNS nvarchar(4000)
AS
BEGIN
	Declare @ColumnName nvarchar(50)
	Declare @Result nvarchar(4000)

	DECLARE Record_Cursor CURSOR FOR select item from dbo.ArrayToTable(dbo.Array(@FieldList,','))
	OPEN Record_Cursor
	FETCH NEXT FROM Record_Cursor into @ColumnName
	set @Result = @ColumnName
	WHILE @@FETCH_STATUS = 0
	BEGIN

		if(Charindex('CreatedAt',@ColumnName)<=0  and Charindex('CreatedBy',@ColumnName)<=0 and Charindex('LastModifiedBy',@ColumnName)<=0 and Charindex('LastModifiedAt',@ColumnName)<=0 and Charindex('DeletedStatus',@ColumnName)<=0 and Charindex('PrintStatus',@ColumnName)<=0 and Charindex('RecordStatus',@ColumnName)<=0)
		Begin
			set @Result = @Result + ',' + @ColumnName
		End

	FETCH NEXT FROM Record_Cursor into @ColumnName
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor

	return @Result
END

```
