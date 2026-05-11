# Function: `GetProductIDByTypeProduct`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-09-14 14:36:22.493000
- **Ngày sửa cuối**: 2022-12-06 09:33:34.203000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetProductIDByTypeProduct]
(
	-- Add the parameters for the function here
	@TypeProduct int
)
RETURNS int
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result int
            
	-- Add the T-SQL statements to compute the return value here
	set @Result = case @TypeProduct
		when 1 then  140
		when 2 then  228
		when 3 then  231
		when 4 then  238
		when 5 then  339
		when 6 then  239
		when 7 then  337
		when 8 then  240
		when 9 then  370
		WHEN 10 THEN 342
		WHEN 14 THEN 598
		WHEN 15 THEN 613
		WHEN 381 THEN 381
		WHEN 16 THEN 680
		WHEN 17 THEN 732
		WHEN 18 THEN 735
		WHEN 19 THEN 821
		WHEN 20 THEN 5059
		WHEN 585 THEN 585
		WHEN 5056 THEN 5056
		ELSE @TypeProduct
	end
	-- Return the result of the function
	RETURN @Result

END

```
