# Function: `ThucChay_GetSoLuongThucChayKMByHDLoaiSP`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-06 18:20:19.060000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.340000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@ViewThucChay` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSamPhamID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayKMByHDLoaiSP]
(
	-- Add the parameters for the function here
	@NgayThucHien DATETIME
	, @ViewThucChay INT
	, @SoHopDong NVARCHAR(50)
	, @DmSamPhamID INT
)
RETURNS bigint
AS
BEGIN
	-- Declare the return variable here
	DECLARE @v_count INT
	DECLARE @v_result BIGINT
	DECLARE @v_tongviewthucchay BIGINT, @v_tongviewphanbo BIGINT, @v_tongviewphanbokm BIGINT
	SET @v_result = 0
	--KIEM TRA HD CO TON TAI PHAN BO KHUYEN MAI ?
	SET @v_count =
	(
		SELECT COUNT(hdct.HopDongChiTietID) FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hd.SoHopDong = @SoHopDong
		AND hdct.DmSanPhamREF = @DmSamPhamID--dbo.[GetProductIDByTypeProduct](@TypeProduct)
		AND hdct.IsKhuyenMai = 1
	)
	--HD TON TAI PHAN BO KHUYEN MAI
	IF(@v_count > 0)
	BEGIN
		--LAY TONG VIEW THUC CHAY CUA HOP DONG TU THUCCHAY (NGAYTHUCCHAY<= NGAYTHUCHIEN)
		SET @v_tongviewthucchay =
		(
			SELECT SUM(ISNULL(tc.SoLuongThucChay,0)) + SUM(ISNULL(tc.SoLuongThucChayKM,0)) FROM ThucChayDaTinh tc
			WHERE UPPER(LTRIM(RTRIM(tc.SoHopDong))) = @SoHopDong
			AND tc.DmSanPhamREF = @DmSamPhamID
			AND Convert(date,tc.NgayThucHien) <= @NgayThucHien
		)
		SET @v_tongviewthucchay = ISNULL(@v_tongviewthucchay,0)
		--LAY TONG VIEW CUA CAC PHAN BO KHONG PHAI LA KHUYEN MAI
		SET @v_tongviewphanbo = 
		(
			SELECT SUM(ISNULL(hdct.SoLuong,0)*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) FROM HopDong hd
			INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			WHERE hd.SoHopDong = @SoHopDong
			AND hdct.DmSanPhamREF = @DmSamPhamID
			AND hdct.IsKhuyenMai = 0	
		)
		SET @v_tongviewphanbo = ISNULL(@v_tongviewphanbo,0)
		--LAY TONG VIEW PHAN BO LA KHUYEN MAI
		SET @v_tongviewphanbokm = 
		(
			SELECT SUM(ISNULL(hdct.SoLuong,0)*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) FROM HopDong hd
			INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			WHERE hd.SoHopDong = @SoHopDong
			AND hdct.DmSanPhamREF = @DmSamPhamID
			AND hdct.IsKhuyenMai = 1	
		)
		SET @v_tongviewphanbokm = ISNULL(@v_tongviewphanbokm,0)
		--NEU PHAT SINH VIEW CHO PHAN BO KHUYEN MAI
		IF((@v_tongviewthucchay < @v_tongviewphanbo + @v_tongviewphanbokm) AND (@v_tongviewthucchay + @ViewThucChay > @v_tongviewphanbo))
		BEGIN
			IF(@v_tongviewthucchay < @v_tongviewphanbo)
				IF((@v_tongviewthucchay + @ViewThucChay) >= ( @v_tongviewphanbo + @v_tongviewphanbokm))
					SET @v_result = @v_tongviewphanbokm
				ELSE
					SET @v_result = (@v_tongviewthucchay + @ViewThucChay) - @v_tongviewphanbo
			ELSE
				BEGIN
					IF((@v_tongviewthucchay + @ViewThucChay) <= (@v_tongviewphanbo + @v_tongviewphanbokm))
						SET @v_result = @ViewThucChay
					ELSE
						SET @v_result = (@v_tongviewphanbo + @v_tongviewphanbokm) - @v_tongviewthucchay
				END			
		END
	END	
	-- Return the result of the function
	RETURN @v_result;

END

```
