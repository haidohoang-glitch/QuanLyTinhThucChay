# Function: `CheckContractExistsProduct`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-12-01 10:41:04.200000
- **Ngày sửa cuối**: 2014-12-01 10:41:04.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@hopDongId` | `int(4)` | No |
| `@sanPhamIdList` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ	
-- Create date: 2014-12-01
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.CheckContractExistsProduct
(
	-- Add the parameters for the function here
	@hopDongId	INT,
	@sanPhamIdList	NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @resultVarlue	INT

	IF EXISTS(
		SELECT hd.HopDongID
		FROM HopDong AS hd
			INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
		WHERE 1=1
			AND hd.TrangThaiHopDong <> 3
			AND hdct.DeletedStatus = 0
			AND hd.HopDongID = @hopDongId
			AND hdct.DmSanPhamREF IN (144,299,337,585)
	)
		SET @resultVarlue = 1
	ELSE
		SET @resultVarlue = 0;

	-- Return the result of the function
	RETURN @resultVarlue

END

```
