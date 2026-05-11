# Function: `ThucChay_GetSoLuongThucChayChuanByDonViTinh_BK`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-05-26 16:42:32.917000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.857000

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
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_BK] 
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
	DECLARE @SoLuongThucChay FLOAT, @v_tongviewthucchay FLOAT
	DECLARE @SoLuongTheoDonViTinh BIGINT, @IsKM INT
	--DECLARE @MinDate DATETIME
	SET @SoLuongThucChay =0
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	SET @SoLuongTheoDonViTinh = @SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(@DonViTinh)
	--TINH TONG VIEW THUC CHAY DEN NGAYTHUCHIEN
	--SET @MinDate = 
	--(
	--	SELECT MIN(tcdt.NgayThucHien) FROM ThucChayDaTinh tcdt
	--	WHERE tcdt.HopDongChiTietREF = @HopDongChiTietREF
	--)
	--SET @MinDate = ISNULL(@MinDate,@NgayThucHien)
	
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
			SELECT SUM(ISNULL(tc.SoLuongThucChay,0)) FROM ThucChayDaTinh tc
			WHERE tc.HopDongChiTietREF = @HopDongChiTietREF
			--AND tc.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
			AND tc.NgayThucHien <= @NgayThucHien
		)	
	END
	ELSE
		BEGIN
			SET @v_tongviewthucchay =
			(
				SELECT SUM(ISNULL(tc.SoLuongThucChayKM,0)) FROM ThucChayDaTinh tc
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
	-- Return the result of the function
	RETURN @SoLuongThucChay

END

```
