# Function: `Admarket_fn_CheckThauChi`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-14 15:06:03.380000
- **Ngày sửa cuối**: 2016-04-11 16:21:18.297000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@User` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANNV
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[Admarket_fn_CheckThauChi]
(
	@User NVARCHAR(50),
	@DmSanPhamREF INT,
	@NgayThucHien DATETIME
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultVar INT = 0 
	DECLARE @TienDauNgay FLOAT
	
	-- Add the T-SQL statements to compute the return value here
	SET @TienDauNgay = (SELECT TOP 1 UserBalance FROM dbo.AdmarketBalanceUserDaily 
	WHERE userName = @User 
	AND DmSanPhamREF = @DmSanPhamREF
	AND CONVERT(DATE,NgayThucHien) = CONVERT(DATE,@NgayThucHien))
	
	SET @TienDauNgay = ISNULL(@TienDauNgay,-1)
	
    IF @TienDauNgay <= 0 SET @ResultVar = 1

	-- Return the result of the function
	RETURN @ResultVar
END

```
