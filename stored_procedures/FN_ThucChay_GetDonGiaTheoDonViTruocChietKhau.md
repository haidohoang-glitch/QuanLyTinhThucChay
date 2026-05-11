# Function: `ThucChay_GetDonGiaTheoDonViTruocChietKhau`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-09-26 16:53:03.260000
- **Ngày sửa cuối**: 2015-04-10 10:20:30.750000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@ProductUnitName` | `nvarchar(100)` | No |
| `@BannerType` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--select dbo.[ThucChay_GetDonGiaTheoDonViTruocChietKhau] (62625)
CREATE FUNCTION [dbo].[ThucChay_GetDonGiaTheoDonViTruocChietKhau]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT,
	@ProductUnitName NVARCHAR(50),
	@BannerType INT,
	@NgayThucHien DATETIME
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue FLOAT,@DonViTinh NVARCHAR(50), @DonGia FLOAT, @DmSanPhamREF INT, @Unit INT;
	
	SELECT @DonViTinh = DonViTinh ,
		   @DonGia    = hdct.DonGia,
		   @DmSanPhamREF = hdct.DmSanPhamREF
	FROM HopDongChiTiet hdct 
	WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	
	
	
	SELECT @ResultValue =  
		CASE 
			WHEN @DonViTinh = 'CPC' THEN @DonGia
			WHEN @DonViTinh = 'CPM' THEN @DonGia/1000
			WHEN @DonViTinh = 'CPV' THEN @DonGia
			ELSE  dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien,@DmSanPhamREF,@BannerType,@ProductUnitName)	
		END	
		-- Return the result of the function
	RETURN @ResultValue

END

```
