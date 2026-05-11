# Function: `ThucChay_GetThanhTienChuanThucChay_Mobile`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-09-23 14:22:16.930000
- **Ngày sửa cuối**: 2015-09-17 18:27:51.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@ProductUnitName` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |
| `@BannerType` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--select dbo.[ThucChay_GetThanhTienChuanThucChay_Mobile] ('2014-07-21',61676,'CPC',-1,13388,3)
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_Mobile]
(
	-- Add the parameters for the function here
	--@NgayThucHien datetime,
	--@HopDongChiTietID INT,
	--@ProductUnitName NVARCHAR(50),
	--@BannerType INT,
	--@TongViewThucChay FLOAT,
	--@TongClickThucChay FLOAT
	
	@SoLuong INT, 
	@ProductUnitName nvarchar(50), 
	@DonGia FLOAT,
	@NgayKyHopDong DATETIME,
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT,
	@BannerType INT,
	@NgayThucHien datetime,
	@HopDongChiTietID nvarchar(50)	

)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChay FLOAT,
			@DonGiaTheoDonVi FLOAT,
			@SoLuongThucChay INT,@SoLuongThucChayKM INT,
			@IsKhuyenMai INT, @ChietKhau INT, @DonViTinh NVARCHAR(50), @DmSanPhamREF INT 
			
	SELECT @IsKhuyenMai = IsKhuyenMai,
		   @ChietKhau   = hdct.ChietKhau,
		   @DonViTinh   = hdct.DonViTinh,
		   @DmSanPhamREF = hdct.DmSanPhamREF		   
	FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	
	SELECT @DonViTinh = (CASE WHEN @DonViTinh = 'CPC' THEN @DonViTinh
						         WHEN @DonViTinh = 'CPM' THEN @DonViTinh
						         WHEN @DonViTinh = 'CPV' THEN @DonViTinh
						         ELSE @ProductUnitName
						    END) 
	
	SET @DonGiaTheoDonVi = (select CASE WHEN @DmSanPhamREF = 342 THEN dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(@HopDongChiTietID,@ProductUnitName,@BannerType,@NgayThucHien)
							            WHEN @DmSanPhamREF = 381 THEN 3000
							            ELSE 0
								END)
	 
	SET @SoLuongThucChay = dbo.[ThucChay_GetSoLuongThucChayMobile](@HopDongChiTietID, 
											@DonGiaTheoDonVi,-- as DonGia,
											@NgayThucHien, 
											@TongViewThucChay,
											@TongClickThucChay,
											@ProductUnitName)	
	
												
	SET @SoLuongThucChayKM = 
				(CASE when (((@IsKhuyenMai = 1) OR (@ChietKhau = 100))AND (@DonViTinh = 'CPM')) 
						then ISNULL(dbo.ThucChay_GetSoLuongThucChayKMMobile(@HopDongChiTietID,1,@DonGiaTheoDonVi,@NgayThucHien,@TongViewThucChay),0)
					  when (((@IsKhuyenMai = 1) OR (@ChietKhau = 100))AND (@DonViTinh = 'CPC')) 
						then ISNULL(dbo.ThucChay_GetSoLuongThucChayKMMobile(@HopDongChiTietID,1,@DonGiaTheoDonVi,@NgayThucHien,@TongClickThucChay),0)
					else 0
				 END
				)
	IF (@IsKhuyenMai = 1 OR @ChietKhau = 100)
		SET @ThanhTienThucChay = @DonGiaTheoDonVi * @SoLuongThucChayKM
	ELSE
		SET @ThanhTienThucChay = @DonGiaTheoDonVi * @SoLuongThucChay
	
	RETURN @ThanhTienThucChay

END

```
