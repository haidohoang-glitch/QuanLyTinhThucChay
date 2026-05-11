# Function: `GetDmSanPhamREFByHopDongChiTietREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-02 17:04:14.287000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.610000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION GetDmSanPhamREFByHopDongChiTietREF
(
	-- Add the parameters for the function here
	@HopDongChiTietREF INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DmSanPhamREF INT

	-- Add the T-SQL statements to compute the return value here
	SET @DmSanPhamREF = (SELECT DmSanPhamREF FROM HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietREF)

	-- Return the result of the function
	RETURN @DmSanPhamREF

END

```
