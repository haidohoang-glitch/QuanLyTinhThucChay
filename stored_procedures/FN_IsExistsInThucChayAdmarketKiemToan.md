# Function: `IsExistsInThucChayAdmarketKiemToan`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-04-13 15:14:21.120000
- **Ngày sửa cuối**: 2015-04-13 15:14:21.120000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.IsExistsInThucChayAdmarketKiemToan
(
	-- Add the parameters for the function here
	@SoHopDong NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	 
	-- Declare the return variable here
	DECLARE @Result INT, @count INT
	
	SET @Result = 0
	-- Add the T-SQL statements to compute the return value here
	set @count  = (SELECT COUNT(*) FROM ThucChayAdmarketKiemToan2013 tcakt WHERE tcakt.SoHopDong = @SoHopDong)
	IF @count >0 
		SET @Result = 1
	ELSE 
		SET @Result = 0
	-- Return the result of the function
	RETURN @Result

END

```
