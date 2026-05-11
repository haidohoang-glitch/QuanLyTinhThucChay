# Function: `fn_TinhTienThucChayLechTreoHaCPM_With_DonViTinh_Ngay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2018-02-22 16:39:48.757000
- **Ngày sửa cuối**: 2020-07-09 17:18:48.857000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DonGia` | `float(8)` | No |
| `@TiLeBannerSiteHDCT` | `float(8)` | No |
| `@ThanhTien` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[fn_TinhTienThucChayLechTreoHaCPM_With_DonViTinh_Ngay] 
(
	@HopDongChiTietREF  INT,
	@NgayThucHien DATETIME,
	@DonGia FLOAT,
	@TiLeBannerSiteHDCT FLOAT,
	@ThanhTien FLOAT,
	@ChietKhau FLOAT
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out BIGINT =0, @TongTienThucChay BIGINT =0, @ThanhTienThucChayNgay BIGINT =0
	, @TongTienThucChayKM BIGINT = 0, @ThanhTienThucChayNgayKM BIGINT = 0
	
	IF(@ChietKhau <> 100)
	BEGIN
		SET @TongTienThucChay = ISNULL((SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh
									WHERE HopDongChiTietREF = @HopDongChiTietREF AND NgayThucHien BETWEEN '2017-12-31' AND @NgayThucHien AND TrangThaiHopDong <> 3),0)
		SET @ThanhTienThucChayNgay = (@DonGia*@TiLeBannerSiteHDCT*(100-@ChietKhau)/100)
		IF(@ThanhTien > @TongTienThucChay)
		BEGIN
			IF(@ThanhTien >= @ThanhTienThucChayNgay + @TongTienThucChay )
				SET @out = 0
			ELSE
				SET @out = ((@TongTienThucChay + @ThanhTienThucChayNgay)- @ThanhTien)/((100-@ChietKhau)/100)
		END
		ELSE
		BEGIN
			SET @out = @DonGia*@TiLeBannerSiteHDCT
		END
	END
	--VOI CHI KHAU = 100
	ELSE
	BEGIN
		SET @TongTienThucChayKM = ISNULL((SELECT SUM(ThanhTienKM + GiaTriKMThayDoi) FROM dbo.ThucChayDaTinh
									WHERE HopDongChiTietREF = @HopDongChiTietREF AND NgayThucHien BETWEEN '2017-12-31' AND @NgayThucHien AND TrangThaiHopDong <> 3),0)
		SET @ThanhTienThucChayNgayKM = @DonGia*@TiLeBannerSiteHDCT
		SET @ThanhTien = isnull((SELECT top (1) hdct.SoLuong*hdct.DonGia FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietREF order by hdct.HopDongChiTietID),0)
		IF(@ThanhTien > @TongTienThucChayKM)
		BEGIN
			IF(@ThanhTien >= @ThanhTienThucChayNgayKM + @TongTienThucChayKM )
				SET @out = 0
			ELSE
				SET @out = ((@TongTienThucChayKM + @ThanhTienThucChayNgayKM)- @ThanhTien)
		END
		ELSE
		BEGIN
			SET @out = @DonGia*@TiLeBannerSiteHDCT
		END
	END
	RETURN @out;
END
```
