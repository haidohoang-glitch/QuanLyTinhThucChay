# Function: `ThucChay_GetThanhTienTCDen_25082013`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-26 17:25:54.400000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.803000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPham` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienTCDen_25082013]
(
	-- Add the parameters for the function here
	@HopDongID INT, 
	@DmSanPham INT 
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChay FLOAT
	SET @ThanhTienThucChay = 
	(
		SELECT sum(tcdt.ThanhTienSauTrietKhauThucChay) thanhtientc 
		FROM ThucChayDaTinh tcdt
		WHERE tcdt.HopDongID = @HopDongID
		AND tcdt.DmSanPhamREF = @DmSanPham
		AND convert(date,TCDT.NgayThucHien) <= '2013-08-25'
	)	

	RETURN @ThanhTienThucChay

END

```
