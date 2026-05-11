# Function: `GetProductNameByDmSanPhamREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-21 16:23:38.290000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.907000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetProductNameByDmSanPhamREF]
(
	-- Add the parameters for the function here
	@DmSanPhamREF int
)
RETURNS nvarchar(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(50)
            
	-- Add the T-SQL statements to compute the return value here
	set @Result = case @DmSanPhamREF
		when 140 then  N'Banner'
		when 370 then  N'Box App'
	end
	-- Return the result of the function
	RETURN @Result

END

```
