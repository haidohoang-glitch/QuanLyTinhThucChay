# Function: `AdmarketGetViTriLamViecByNhanVien`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-25 17:19:27.410000
- **Ngày sửa cuối**: 2014-10-14 10:39:38.100000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@TenPhongBan` | `nvarchar(400)` | No |
| `@TenBoPhan` | `nvarchar(400)` | No |
| `@TenNhomlamViec` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-18
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.AdmarketGetViTriLamViecByNhanVien 
(
	-- Add the parameters for the function here
	@TenPhongBan	nvarchar(200),
	@TenBoPhan		nvarchar(200),
	@TenNhomlamViec nvarchar(200)
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max);
	
	SET @ReturnValue = '';

	IF @TenPhongBan <> ''
		SET @ReturnValue = @TenPhongBan;

	IF @TenBoPhan <> '' 
		SET @ReturnValue += ' - ' + @TenBoPhan;

	IF @TenNhomlamViec <> '' 
		SET @ReturnValue += ' - ' + @TenNhomlamViec;

	-- Return the result of the function
	RETURN @ReturnValue;

END

```
