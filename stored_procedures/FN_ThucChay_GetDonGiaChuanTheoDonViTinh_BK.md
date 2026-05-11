# Function: `ThucChay_GetDonGiaChuanTheoDonViTinh_BK`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-19 16:09:45.843000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.423000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--SELECT * FROM HopDongChiTiet hdct
--WHERE hdct.HopDongChiTietID = 51452

--SELECT dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_BK (6, N'Tháng', 7500000, '2014-03-13', 46058)


CREATE FUNCTION [dbo].[ThucChay_GetDonGiaChuanTheoDonViTinh_BK]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50), 
	@DonGia FLOAT,
	--@NgayKyHopDong DATETIME,
	@NgayThucHien datetime,
	@HopDongChiTietID nvarchar(50)	
)
RETURNS FLOAT
AS
BEGIN
	--set @DonGia = dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,@HopDongChiTietID,@DonGia)
	-- Declare the return variable here
	DECLARE @DonGiaTheoDonVi FLOAT
	DECLARE @SoNgayTheoDonViTinh INT 
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	
	IF(@DonViTinh = 'CPM' or @DonViTinh = 'CPC')
	BEGIN
		SET @DonGiaTheoDonVi = @DonGia/1000
	END
	ELSE
		IF(@DonViTinh = 'PR')
		BEGIN
			SET @DonGiaTheoDonVi = @DonGia
		END
		ELSE
			IF(@DonViTinh = 'GOI')
			BEGIN
				SET @SoLuong = 5000
				SET @DonGiaTheoDonVi = @DonGia
			END
			ELSE			
			BEGIN
				SET @SoNgayTheoDonViTinh = isnull(dbo.ThucChay_GetSoLuong_DonViTinh(@SoLuong, @DonViTinh),0)								
				--SET @SoNgayTheoDonViTinh = isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(@SoLuong, @DonViTinh,@HopDongChiTietID),0)				
				SET @DonGiaTheoDonVi = ROUND(@DonGia*@SoLuong / @SoNgayTheoDonViTinh,2)
			END
	-- Return the result of the function
	RETURN @DonGiaTheoDonVi

END

```
