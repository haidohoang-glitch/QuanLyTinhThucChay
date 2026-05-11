# Function: `ThucChay_GetSoLuongThucChay_Admatic`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-11-29 16:53:09.140000
- **Ngày sửa cuối**: 2016-12-15 17:58:19.377000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |
| `@DonGia_Banner` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChay_Admatic] 
(
	-- Add the parameters for the function here
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT,
	@DonGia_Banner INT,
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT, @v_TongViewThucChayThucThu FLOAT, @v_TongViewThucChayKhuyenMai INT, @v_TongViewThucChay BIGINT, @TongSLHD INT, @HopDongID INT
	DECLARE @SoLuongTheoDonViTinh BIGINT, @IsKM INT, @DmSanPhamID INT, @DonViQuyDoi INT = 1
	--DECLARE @MinDate DATETIME
	IF(@DonGia_Banner = 0)
		SET @DonGia_Banner = 1
	IF (UPPER(@DonViTinh) = 'CPM')
		SET @DonViQuyDoi = 1000
	IF (UPPER(@DonViTinh) = 'CPC')
		SET @DonViQuyDoi = 1
	SET @TongSLHD = 0
	SET @v_TongViewThucChayKhuyenMai = 0
	SET @SoLuongThucChay =0

	
	SELECT @v_TongViewThucChayKhuyenMai = SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi)
	, @HopDongID = max(tcdt.HopDongID)
	, @DmSanPhamID = MAX(hdct.DmSanPhamREF)
	, @v_TongViewThucChayThucThu = SUM(tcdt.SoLuongThucChay  + tcdt.SoLuongThayDoi)
	FROM ThucChayDaTinh tcdt INNER JOIN HopDongChiTiet hdct
	ON tcdt.HopDongID = hdct.HopDongFK
	AND tcdt.DmSanPhamREF = hdct.DmSanPhamREF
	WHERE hdct.HopDongChiTietID = @HopDongChiTietREF
	
	SET @v_TongViewThucChayKhuyenMai = ISNULL(@v_TongViewThucChayKhuyenMai,0)
	SET @v_TongViewThucChayThucThu = ISNULL(@v_TongViewThucChayThucThu,0)

	SET @SoLuongTheoDonViTinh =
	ISNULL((
		SELECT ((hdct.soluong*hdct.dongia)/@DonGia_Banner)*@DonViQuyDoi
		FROM HopDongChiTiet hdct
		WHERE 1=1
		AND hdct.HopDongChitietID = @HopDongChiTietREF
	),0)

	IF((@v_TongViewThucChayKhuyenMai + @TongViewThucChay) < @SoLuongTheoDonViTinh)
	BEGIN
		--XAC DINH LA PHAN BO KHUYEN MAI HAY KHONG
		SET @IsKM =
		(
			SELECT count(hdct.HopDongChiTietID) FROM HopDongChiTiet hdct
			WHERE hdct.HopDongChiTietID = @HopDongChiTietREF
			AND hdct.DeletedStatus = 0
			AND (hdct.IsKhuyenMai = 1 OR hdct.ChietKhau = 100)
		)
		IF(@IsKM = 0)
		BEGIN
			SET @v_TongViewThucChay = @v_TongViewThucChayThucThu
			
		END
		ELSE
			BEGIN
				SET @v_TongViewThucChay = @v_TongViewThucChayKhuyenMai
			END
		
		SET @v_TongViewThucChay = ISNULL(@v_TongViewThucChay,0)
		IF(@v_TongViewThucChay < @SoLuongTheoDonViTinh)
		BEGIN
			IF((@v_TongViewThucChay + @TongViewThucChay)> @SoLuongTheoDonViTinh)
				BEGIN
					SET  @SoLuongThucChay =(@SoLuongTheoDonViTinh - @v_TongViewThucChay)
				END
			ELSE
				BEGIN
					SET  @SoLuongThucChay = @TongViewThucChay
				END
			
		END 
	END
	
	-- Return the result of the function
	RETURN @SoLuongThucChay

END

```
