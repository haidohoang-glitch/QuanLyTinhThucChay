# Function: `FormatStringIDList`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-23 08:52:32.670000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.247000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@IDList` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[FormatStringIDList] 
(
	@IDList nvarchar(4000)
)
RETURNS nvarchar(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(4000)
	declare @Index int 
	declare @ID nvarchar(50)
	declare @DauNhay nvarchar(50)
		
	set @DauNhay = ''''
	set @Result = '' 
	DECLARE ID_Cursor CURSOR FOR select item from dbo.ArrayToTable(dbo.Array(@IDList,','))
	Open ID_Cursor
	FETCH NEXT FROM ID_Cursor into @ID

	WHILE @@FETCH_STATUS = 0
	BEGIN
	set @Result = @Result + @DauNhay + @ID + @DauNhay + ','
	FETCH NEXT FROM ID_Cursor into @ID
	END	
	
	if(@Result <> '')
	Begin
		set @Result = substring(@Result,0,len(@Result))
	End

	CLOSE ID_Cursor
	DEALLOCATE ID_Cursor

	RETURN @Result

END

```
