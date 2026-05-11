# Function: `ThucChay_GetSoLuongLechTreoHa_CPR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-12-10 17:03:32.643000
- **Ngày sửa cuối**: 2016-11-10 15:52:18.917000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTiet` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(200)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@uvNgay` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongLechTreoHa_CPR]
(
	-- Add the parameters for the function here
	@NgayThucHien DATETIME
	, @HopDongChiTiet INT
	, @SoLuong INT
	, @DonViTinh NVARCHAR(100)
	, @DmSanPhamID INT
	, @uvNgay INT
)
RETURNS bigint
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue BIGINT, @TongSLTC bigINT, @TongSLHD INT, @HopDongID INT
		
	SET @TongSLTC = 0
	SET @ResultValue = 0
	
	SET @TongSLHD = @SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(@DonViTinh)
		
	SELECT @TongSLTC = SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThucChayKM + tcdt.SoLuongThayDoi + tcdt.SoLuongKMThayDoi)
	, @HopDongID = max(tcdt.HopDongID)
	FROM ThucChayDaTinh tcdt INNER JOIN HopDongChiTiet hdct
	ON tcdt.HopDongID = hdct.HopDongFK
	AND tcdt.DmSanPhamREF = hdct.DmSanPhamREF
	AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
	WHERE hdct.HopDongChiTietID = @HopDongChiTiet
	AND tcdt.NgayThucHien <= @NgayThucHien
	
	--NEU TRUONG HOP TONGVIEWTHUCCHAY < TONGVIEWPHANBO, CO PHAT SINH LECH TREO HA
	IF((@TongSLTC + @uvNgay) > @TongSLHD)
	BEGIN
		IF(@TongSLTC < @TongSLHD)
			SET @ResultValue = (@TongSLTC + @uvNgay) - @TongSLHD
		ELSE
			SET @ResultValue = @uvNgay		
	END
	-- Return the result of the function
	RETURN @ResultValue;

END

```
