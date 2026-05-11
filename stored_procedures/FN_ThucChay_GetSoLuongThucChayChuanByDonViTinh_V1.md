# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-23 14:36:18.267000
- **Ngày sửa cuối**: 2017-04-03 12:06:35.883000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TongViewThucChay` | `float(8)` | No |
| `@SoLuong` | `int(4)` | No |
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
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_V1] 
(
	-- Add the parameters for the function here
	@TongViewThucChay FLOAT,
	@SoLuong INT,
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT, @v_tongviewthucchay FLOAT, @TongSLTC INT, @TongSLHD INT, @HopDongID INT
	DECLARE @SoLuongTheoDonViTinh BIGINT, @IsKM INT, @Count_HD_SP INT, @DmSanPhamID INT
	--DECLARE @MinDate DATETIME
	SET @Count_HD_SP = 0
	SET @TongSLHD = 0
	SET @TongSLTC = 0
	SET @SoLuongThucChay =0
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	SET @SoLuongTheoDonViTinh = @SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(@DonViTinh)

	--XAC DINH HD CO TINH THEO PP SAN PHAM KHONG
	SET @Count_HD_SP =
	(
		SELECT COUNT(tcdt.HopDongID) 
		FROM ThucChayDaTinh tcdt INNER JOIN HopDongChiTiet hdct
		ON tcdt.HopDongID = hdct.HopDongFK
		AND tcdt.DmSanPhamREF = hdct.DmSanPhamREF
		WHERE hdct.HopDongChiTietID = @HopDongChiTietREF
		AND tcdt.HopDongChiTietREF = 0
	)
	
	SELECT @TongSLTC = SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThucChayKM + tcdt.SoLuongThayDoi + tcdt.SoLuongKMThayDoi)
	, @HopDongID = max(tcdt.HopDongID)
	, @DmSanPhamID = MAX(hdct.DmSanPhamREF)
	FROM ThucChayDaTinh tcdt INNER JOIN HopDongChiTiet hdct
	ON tcdt.HopDongID = hdct.HopDongFK
	AND tcdt.DmSanPhamREF = hdct.DmSanPhamREF
	WHERE hdct.HopDongChiTietID = @HopDongChiTietREF
	

	SET @TongSLHD =
	(
		SELECT SUM(hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))
		FROM HopDongChiTiet hdct
		WHERE hdct.HopDongFK = @HopDongID
		AND hdct.DmSanPhamREF = @DmSanPhamID
	)
	
	IF((@Count_HD_SP = 0) OR (@Count_HD_SP >0 AND @TongSLTC < @TongSLHD))
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
			SET @v_tongviewthucchay =
			(
				SELECT SUM(ISNULL(tc.SoLuongThucChay,0) + ISNULL(tc.SoLuongThayDoi,0)) FROM ThucChayDaTinh tc
				WHERE tc.HopDongChiTietREF = @HopDongChiTietREF
				--AND tc.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
				AND tc.NgayThucHien <= @NgayThucHien
			)	
		END
		ELSE
			BEGIN
				SET @v_tongviewthucchay =
				(
					SELECT SUM(ISNULL(tc.SoLuongThucChayKM,0) + ISNULL(tc.SoLuongKMThayDoi,0)) FROM ThucChayDaTinh tc
					WHERE tc.HopDongChiTietREF = @HopDongChiTietREF
					--AND tc.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
					AND tc.NgayThucHien <= @NgayThucHien
				)	
			END
		
		SET @v_tongviewthucchay = ISNULL(@v_tongviewthucchay,0)
		IF(@v_tongviewthucchay < @SoLuongTheoDonViTinh)
		BEGIN
			IF((@v_tongviewthucchay + @TongViewThucChay)> @SoLuongTheoDonViTinh)
				BEGIN
					SET  @SoLuongThucChay =(@SoLuongTheoDonViTinh - @v_tongviewthucchay)--((@v_tongviewthucchay+ @TongViewThucChay)- @SoLuongTheoDonViTinh)
				END
			ELSE
				BEGIN
					SET  @SoLuongThucChay = @TongViewThucChay
				END
			
		END 
	END
	
	-- Return the result of the function
	--RETURN @SoLuongThucChay
	RETURN @SoLuongThucChay

END

```
