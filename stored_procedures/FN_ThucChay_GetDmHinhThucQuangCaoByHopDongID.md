# Function: `ThucChay_GetDmHinhThucQuangCaoByHopDongID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-12 01:47:52.563000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.527000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetDmHinhThucQuangCaoByHopDongID]
(
	-- Add the parameters for the function here
	@HopDongID INT,
	@DmSanPhamREF INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue INT
	
	SET @ResultValue = 
	(
		SELECT TOP 1 B.DmLoaiREF
		FROM HopDong A
		INNER JOIN HopDongChiTiet B ON B.HopDongFK = A.HopDongID
			AND A.HopDongID = @HopDongID
			AND B.DmSanPhamREF = @DmSanPhamREF
	)
	
	
	SET @ResultValue = ISNULL(@ResultValue,0);

	-- Return the result of the function
	RETURN @ResultValue

END

```
