# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-12-10 16:46:27.887000
- **Ngày sửa cuối**: 2017-06-29 09:26:35.327000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@uv` | `float(8)` | No |
| `@uvNgay` | `int(4)` | No |
| `@SoLuongHD` | `int(4)` | No |
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
					  
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPR] 
(
	-- Add the parameters for the function here
	@uv FLOAT,
	@uvNgay INT,
	@SoLuongHD INT,
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT, @v_tongslthucchay FLOAT, @TongSLTC INT, @TongSLHD INT, @HopDongID INT
	DECLARE @SoLuongTheoDonViTinh BIGINT, @IsKM INT, @Count_HD_SP INT, @DmSanPhamID INT
	--DECLARE @MinDate DATETIME
	SET @TongSLHD = 0
	SET @TongSLTC = 0
	SET @SoLuongThucChay =0
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	SET @SoLuongTheoDonViTinh = @SoLuongHD*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(@DonViTinh)
	
	
	SELECT @TongSLTC = SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThucChayKM + tcdt.SoLuongThayDoi + tcdt.SoLuongKMThayDoi)
	, @HopDongID = max(tcdt.HopDongID)
	, @DmSanPhamID = MAX(hdct.DmSanPhamREF)
	FROM ThucChayDaTinh tcdt INNER JOIN HopDongChiTiet hdct
	ON tcdt.HopDongID = hdct.HopDongFK
	AND tcdt.DmSanPhamREF = hdct.DmSanPhamREF
	AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
	WHERE hdct.HopDongChiTietID = @HopDongChiTietREF
	
	SET @TongSLTC = ISNULL(@TongSLTC,0)
	
	IF(@TongSLTC < @SoLuongTheoDonViTinh)
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
			SET @v_tongslthucchay =
			(
				SELECT SUM(ISNULL(tc.SoLuongThucChay,0) + ISNULL(tc.SoLuongThayDoi,0)) FROM ThucChayDaTinh tc
				WHERE tc.HopDongChiTietREF = @HopDongChiTietREF
				AND tc.NgayThucHien <= @NgayThucHien
			)	
		END
		ELSE
			BEGIN
				SET @v_tongslthucchay =
				(
					SELECT SUM(ISNULL(tc.SoLuongThucChayKM,0) + ISNULL(tc.SoLuongKMThayDoi,0)) FROM ThucChayDaTinh tc
					WHERE tc.HopDongChiTietREF = @HopDongChiTietREF
					--AND tc.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
					AND tc.NgayThucHien <= @NgayThucHien
				)	
			END
		
		SET @v_tongslthucchay = ISNULL(@v_tongslthucchay,0)
		IF(@v_tongslthucchay < @SoLuongTheoDonViTinh)
		BEGIN
			IF((@v_tongslthucchay + @uvNgay)> @SoLuongTheoDonViTinh)
				BEGIN
					SET  @SoLuongThucChay =(@SoLuongTheoDonViTinh - @v_tongslthucchay)
				END
			ELSE
				BEGIN
					SET  @SoLuongThucChay = @uvNgay
				END
			
		END 
	END
	
	-- Return the result of the function
	RETURN @SoLuongThucChay

END

```
