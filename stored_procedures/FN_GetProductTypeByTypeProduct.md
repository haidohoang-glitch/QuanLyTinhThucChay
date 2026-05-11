# Function: `GetProductTypeByTypeProduct`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-11 02:05:39.690000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.843000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
create FUNCTION GetProductTypeByTypeProduct
(
	-- Add the parameters for the function here
	@TypeProduct int
)
RETURNS nvarchar(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(50)
            
	-- Add the T-SQL statements to compute the return value here
	set @Result = case @TypeProduct
		when 1 then  N'CPD'
		when 2 then  N'CPD'
		when 3 then  N'CPM'
		when 4 then  N'CPM'
		when 5 then  N'CPM'
		when 6 then  N'CPM'
		when 7 then  N'CPM'
		when 8 then  N'CPM'
		when 9 then  N'CPM'
	end
	-- Return the result of the function
	RETURN @Result

END

```
