# Function: `ThucChay_GetSoLuongThucChayTheoBooking_CPD`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-08 16:52:51.757000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.243000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayTheoBooking_CPD]
(
	-- Add the parameters for the function here
	@HopDongChiTietID NVARCHAR(50),
	@NgayThucHien DATETIME
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoLuongTheoDonViTinh FLOAT
	DECLARE @SoNgayTheoDonViTinh INT
	DECLARE @Count INT 
	--SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))

	SET @Count =
	(
		SELECT COUNT(*) FROM HopDongChiTietThayDoi hdct
		INNER JOIN HopDongThayDoi hdtd ON hdct.HopDongThayDoiREF = hdtd.HopDongThayDoiID
		WHERE dbo.FormatString(hdct.HopDongChiTietREF) = @HopDongChiTietID
		AND hdct.DmLoaiBannerREF = 5	--Doc quyen
		AND hdtd.NgayThayDoi = @NgayThucHien
	)
	IF(@Count > 0)
		BEGIN
			--SET @SoNgayTheoDonViTinh = dbo.ThucChay_GetSoLuong_DonViTinh(@SoLuong,@DonViTinh)
			SET @SoNgayTheoDonViTinh =
			(
				SELECT TOP 1 (CASE when UPPER(hdcttd.DonViTinh) ='NGÀY' then hdcttd.SoLuong
							when UPPER(hdcttd.DonViTinh) ='TUẦN' then hdcttd.SoLuong*7
							when UPPER(hdcttd.DonViTinh) ='THÁNG' then hdcttd.SoLuong*30
						else hdcttd.SoLuong*365
					  END
					) as SoNgayTheoDonViTinh
				FROM HopDongChiTietThayDoi hdcttd
				INNER JOIN HopDongThayDoi hdtd ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
				AND convert(date,hdtd.NgayThayDoi) = @NgayThucHien
				AND hdcttd.HopDongChiTietREF = @HopDongChiTietID
				ORDER BY hdcttd.HopDongChiTietThayDoiID DESC
			)
		END
	ELSE
	BEGIN
		SET @SoNgayTheoDonViTinh =
		(
			SELECT ISNULL(sum(DATEDIFF(day, b.ThoiGianBatDau, b.ThoiGianKetThuc) + 1),0) FROM
			(
				SELECT DISTINCT dchdcttd.HopDongChiTietREF, dchdcttd.BookingREF
				, dchdcttd.ThoiGianBatDau, dchdcttd.ThoiGianKetThuc, dchdcttd.RecordStatus
				  FROM DotChayHopDongChiTietThayDoi dchdcttd
				INNER JOIN HopDongThayDoi hdtd ON hdtd.HopDongThayDoiID = dchdcttd.HopDongThayDoiREF
				AND convert(date,hdtd.NgayThayDoi) = @NgayThucHien	
				AND dchdcttd.HopDongChiTietREF = @HopDongChiTietID
			)b
		)
	END	
	SET @SoLuongTheoDonViTinh = @SoNgayTheoDonViTinh
	-- Return the result of the function
	RETURN @SoLuongTheoDonViTinh

END

```
