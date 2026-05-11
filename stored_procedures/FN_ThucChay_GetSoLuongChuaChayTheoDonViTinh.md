# Function: `ThucChay_GetSoLuongChuaChayTheoDonViTinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-28 17:23:52.097000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.773000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongChuaChayTheoDonViTinh]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50),
	@HopDongChiTietID NVARCHAR(50)
)
RETURNS FLOAT
AS
BEGIN

	-- Declare the return variable here
	DECLARE @SoLuongHopDong FLOAT, @SoLuongThucChay FLOAT, @SoLuongChuaChay FLOAT
	
	SET @SoLuongHopDong = [dbo].[ThucChay_GetSoLuongChuanTheoDonViTinh](@SoLuong,@DonViTinh,@HopDongChiTietID)
		
	SET @SoLuongThucChay = dbo.ThucChay_GetSoLuongThucChayByHopDongChiTietID(@HopDongChiTietID)

	SET @SoLuongChuaChay = @SoLuongHopDong - @SoLuongThucChay
	-- Return the result of the function
	RETURN @SoLuongChuaChay

END

```
