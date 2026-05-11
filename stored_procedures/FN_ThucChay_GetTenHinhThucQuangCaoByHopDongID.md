# Function: `ThucChay_GetTenHinhThucQuangCaoByHopDongID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-12 01:49:27.223000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.177000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(200)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetTenHinhThucQuangCaoByHopDongID]
(
	-- Add the parameters for the function here
	@HopDongID INT,
	@DmSanPhamREF INT
)
RETURNS NVARCHAR(100)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue NVARCHAR(100)

	-- Add the T-SQL statements to compute the return value here
	SET @ResultValue = 
	(
		SELECT TOP 1 B.TenLoai
		FROM HopDong A
		INNER JOIN HopDongChiTiet B ON B.HopDongFK = A.HopDongID
			AND A.HopDongID = @HopDongID
			AND B.DmSanPhamREF = @DmSanPhamREF
	)
	
	SET @ResultValue = ISNULL(@ResultValue,'');

	-- Return the result of the function
	RETURN @ResultValue

END

```
