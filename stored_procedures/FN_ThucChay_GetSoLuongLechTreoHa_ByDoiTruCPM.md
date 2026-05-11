# Function: `ThucChay_GetSoLuongLechTreoHa_ByDoiTruCPM`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2023-08-15 16:01:27.973000
- **Ngày sửa cuối**: 2023-08-15 16:01:33.783000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTiet` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@ViewThucChay` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongLechTreoHa_ByDoiTruCPM]
(
	-- Add the parameters for the function here
	@NgayThucHien DATETIME
	, @SoHopDong NVARCHAR(50)
	, @HopDongChiTiet INT
	, @SoLuong INT
	, @DmSanPhamID INT
	, @ViewThucChay INT
)
RETURNS bigint
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue BIGINT, @MinDate DATETIME, @TongSLTC INT, @TongSLHD INT, @HopDongID INT
	DECLARE @v_tongviewthucchay BIGINT, @v_tongviewphanbo BIGINT, @v_viewthucchay BIGINT, @Count_HD_SP INT
	
	SET @v_tongviewphanbo = @SoLuong
	SET @v_tongviewthucchay = ISNULL(@v_tongviewthucchay,0)
	SET @ResultValue = 0
	--XAC DINH HD CO TINH THEO PP SAN PHAM KHONG
	SET @Count_HD_SP = 0
		
	SELECT @TongSLTC = SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThucChayKM + tcdt.SoLuongThayDoi + tcdt.SoLuongKMThayDoi), @HopDongID = max(tcdt.HopDongID)
	FROM dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM] tcdt INNER JOIN HopDongChiTiet hdct
	ON tcdt.HopDongID = hdct.HopDongFK
	AND tcdt.DmSanPhamREF = hdct.DmSanPhamREF
	WHERE hdct.HopDongChiTietID = @HopDongChiTiet
	
	SET @TongSLHD =
	(
		SELECT SUM(hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))
		FROM HopDongChiTiet hdct
		WHERE hdct.HopDongFK = @HopDongID
		AND hdct.DmSanPhamREF = @DmSanPhamID
	)
	IF((@Count_HD_SP = 0) OR (@Count_HD_SP >0 AND @TongSLTC >= @TongSLHD))
	BEGIN
		--KHI TINH THUCCHAY CUA CPM THEO PHUONG PHUONG BANNER (CO HOPDONGCHITIET)
		IF(@HopDongChiTiet <> 0)
			BEGIN
				--SET @MinDate =
				--(
				--	SELECT MIN(tcdt.NgayThucHien) FROM dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM] tcdt
				--	WHERE tcdt.HopDongChiTietREF = @HopDongChiTiet 	
				--)
				--SET @MinDate = ISNULL(@MinDate,@NgayThucHien)
				--TINH TONG VIEW THUCCHAY DEN NGAY
				SET @v_tongviewthucchay =
				(
					SELECT SUM(ISNULL(tc.SoLuongThucChay,0) 
					+ ISNULL(tc.SoLuongThayDoi,0)
					+ ISNULL(tc.SoLuongThucChayKM,0)
					+ ISNULL(tc.SoLuongKMThayDoi,0)
					) FROM dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM] tc
					WHERE tc.HopDongChiTietREF = @HopDongChiTiet
					--AND tc.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
					AND tc.NgayThucHien <= @NgayThucHien
				)
				SET @v_tongviewthucchay = ISNULL(@v_tongviewthucchay,0)
				--NEU TRUONG HOP TONGVIEWTHUCCHAY < TONGVIEWPHANBO, CO PHAT SINH LECH TREO HA
				IF((@v_tongviewthucchay + @ViewThucChay) > @v_tongviewphanbo)
				BEGIN
					IF(@v_tongviewthucchay < @v_tongviewphanbo)
						SET @ResultValue = (@v_tongviewthucchay + @ViewThucChay) - @v_tongviewphanbo
					ELSE
						SET @ResultValue = @ViewThucChay		
				END
			END
		ELSE--KHI THUC HIEN TINH THUCHAY CPM THEO PHUONG PHAP SAN PHAM (HOPDONGCHITIET = 0)
		BEGIN
			--SET @MinDate =
			--	(
			--		SELECT MIN(tc.NgayThucHien) FROM dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM] tc
			--		WHERE UPPER(LTRIM(RTRIM(tc.SoHopDong))) = @SoHopDong
			--		AND tc.DmSanPhamREF = @DmSanPhamID	
			--	)
			--	SET @MinDate = ISNULL(@MinDate,@NgayThucHien)
				
			SET @v_tongviewthucchay =
				(
					SELECT SUM(ISNULL(tc.SoLuongThucChay,0)) 
					 + SUM(ISNULL(TC.SoLuongThucChayKM,0))
					 + SUM(ISNULL(tc.SoLuongThayDoi,0))
					 + SUM(ISNULL(tc.SoLuongKMThayDoi,0)) 
					FROM dbo.[ThucChayDaTinh_DoiTruVaTinhLai_CPM] tc
					WHERE tc.SoHopDong = @SoHopDong 
					--UPPER(LTRIM(RTRIM(tc.SoHopDong))) = @SoHopDong
					AND tc.DmSanPhamREF = @DmSanPhamID
					--AND tc.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
					AND tc.NgayThucHien <= @NgayThucHien
				)
			SET @v_tongviewthucchay = ISNULL(@v_tongviewthucchay,0)
			--LAY TONG VIEW CUA CAC PHAN BO BAO GOM CA KHUYEN MAI VA KHONG KHUYEN MAI
			SET @v_tongviewphanbo = 
			(
				SELECT SUM(ISNULL(hdct.SoLuong,0)*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) FROM HopDong hd
				INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				WHERE hd.SoHopDong = @SoHopDong
				AND hdct.DmSanPhamREF = @DmSanPhamID
				AND hdct.DeletedStatus = 0
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3 --Đơn vị của hình thức CPM
			)
			SET @v_tongviewphanbo = ISNULL(@v_tongviewphanbo,0)
			--NEU TRUONG HOP TONGVIEWTHUCCHAY < TONGVIEWPHANBO, CO PHAT SINH LECH TREO HA
			IF ((@v_tongviewthucchay +@ViewThucChay) > @v_tongviewphanbo)
			BEGIN
				IF (@v_tongviewthucchay < @v_tongviewphanbo)
					SET @ResultValue = (@v_tongviewthucchay + @ViewThucChay) - @v_tongviewphanbo
				ELSE
					SET @ResultValue = @ViewThucChay		
			END
		END
	END
	-- Return the result of the function
	RETURN @ResultValue;

END

```
