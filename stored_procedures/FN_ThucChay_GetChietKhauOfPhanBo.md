# Function: `ThucChay_GetChietKhauOfPhanBo`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-09 11:47:05.583000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.593000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-30
-- Description:	Get Chiet khau cua phan bo hop dong
-- =============================================
CREATE FUNCTION dbo.ThucChay_GetChietKhauOfPhanBo 
(
	-- Add the parameters for the function here
	@HopDongREF INT,
	@DmSanPhamREF INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue INT = 0

	SET @ReturnValue = (
						SELECT 
							MAX(A.ChietKhau)
						FROM HopDongChiTiet A
						WHERE A.HopDongFK = @HopDongREF
							AND A.DmSanPhamREF = @DmSanPhamREF 
							AND A.IsKhuyenMai = 0
						)

	-- Return the result of the function
	RETURN @ReturnValue

END

```
