# Function: `GetDmSanPhamIDByTypeProductID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-09-14 14:36:22.063000
- **Ngày sửa cuối**: 2018-09-12 11:05:32.797000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetDmSanPhamIDByTypeProductID]
(
	-- Add the parameters for the function here
	@DmSanPhamREF int
)
RETURNS int
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result int
            
	-- Add the T-SQL statements to compute the return value here
	set @Result = case @DmSanPhamREF
		when 140 THEN 1
		when 228 THEN 2  
		when 231 THEN 3
		when 238 THEN 4  
		when 339 THEN 5  
		when 342 THEN 10  
		when 337 THEN 7  
		when 240 THEN 8  
		when 370 THEN 9  
		when 598 THEN 14
		when 613 THEN 15
		when 680 THEN 16
		when 732 THEN 17
		when 735 THEN 18
		when 821 THEN 19
		when 585 THEN 585
	end
	-- Return the result of the function
	RETURN @Result

END


```
