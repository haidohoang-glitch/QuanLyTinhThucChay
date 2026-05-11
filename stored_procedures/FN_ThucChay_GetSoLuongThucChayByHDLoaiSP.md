# Function: `ThucChay_GetSoLuongThucChayByHDLoaiSP`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-06 18:20:19.310000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.967000

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
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongThucChayByHDLoaiSP]
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
	--LAY TONG VIEW THUC CHAY CUA HOP DONG TU THUCCHAY (NGAYTHUCCHAY<= NGAYTHUCHIEN)
	SET @v_tongviewthucchay =
	(
		SELECT SUM(ISNULL(tc.SoLuongThucChay,0)) FROM ThucChayDaTinh tc
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
		AND hdct.DeletedStatus = 0
		AND (hdct.IsKhuyenMai = 0 OR hdct.ChietKhau <> 100)	
	)
	SET @v_tongviewphanbo = ISNULL(@v_tongviewphanbo,0)
	IF(@v_tongviewthucchay < @v_tongviewphanbo)
		BEGIN
			IF((@v_tongviewthucchay + @ViewThucChay) > @v_tongviewphanbo)
				SET @v_result = (@v_tongviewphanbo- @v_tongviewthucchay)
			ELSE
				SET @v_result = @ViewThucChay
		END
	-- Return the result of the function
	RETURN @v_result;

END

```
