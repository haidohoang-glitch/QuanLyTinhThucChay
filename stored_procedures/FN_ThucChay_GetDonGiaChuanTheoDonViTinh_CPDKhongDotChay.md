# Function: `ThucChay_GetDonGiaChuanTheoDonViTinh_CPDKhongDotChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-07-01 14:31:36.277000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.387000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetDonGiaChuanTheoDonViTinh_CPDKhongDotChay]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50), 
	@DonGia FLOAT,
	@NgayKyHopDong DATETIME,
	@NgayThucHien datetime,
	@HopDongChiTietID nvarchar(50)	
)
RETURNS FLOAT
AS
BEGIN
	SET @DonGia = dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien, @HopDongChiTietID, @DonGia)
	-- Declare the return variable here
	DECLARE @DonGiaTheoDonVi FLOAT
	DECLARE @SoNgayTheoDonViTinh INT 
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	IF (
	       @DonViTinh = 'CPM'
	       OR @DonViTinh = 'CPC'
	       OR @DonViTinh = N'BÀI'
	       OR @DonViTinh = N'GÓI'
	       OR @DonViTinh = N'Ð/V'
	       OR @DonViTinh = 'CPA'
	   )
	BEGIN
	    SET @DonGiaTheoDonVi = @DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(@DonViTinh)
	END
	ELSE
	BEGIN
	    SET @SoNgayTheoDonViTinh = ISNULL([dbo].[GetSoLuongDotChayThucTreoByHopDongChiTiet](@HopDongChiTietID),0) 
	    
	    IF (@SoNgayTheoDonViTinh = 0)
	        SET @DonGiaTheoDonVi = 0
	    ELSE
	        SET @DonGiaTheoDonVi = ROUND((@SoLuong * @DonGia) / @SoNgayTheoDonViTinh, 2)
	END
	-- Return the result of the function
	RETURN @DonGiaTheoDonVi

END

```
