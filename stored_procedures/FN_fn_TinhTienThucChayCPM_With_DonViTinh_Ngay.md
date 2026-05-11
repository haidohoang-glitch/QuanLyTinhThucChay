# Function: `fn_TinhTienThucChayCPM_With_DonViTinh_Ngay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2018-02-22 16:18:05.943000
- **Ngày sửa cuối**: 2020-07-09 17:07:23.260000

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

CREATE FUNCTION [dbo].[fn_TinhTienThucChayCPM_With_DonViTinh_Ngay] 
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
	DECLARE @out BIGINT =0, @TongTienThucChay BIGINT =0, @ThanhTienThucChayNgay BIGINT =0, @DmDonViTinhREF INT
	, @TongTienThucChayKM BIGINT = 0, @ThanhTienThucChayNgayKM BIGINT = 0

	SET @DmDonViTinhREF =
	ISNULL((
		SELECT TOP (1) DonViTinhREF FROM dbo.HopDongChiTiet
		WHERE HopDongChiTietID = @HopDongChiTietREF
		ORDER BY HopDongChiTietID
	),0)

	SET @DonGia = 
	(CASE WHEN @DmDonViTinhREF = 3 THEN @DonGia --NGAY
		WHEN @DmDonViTinhREF = 4 THEN @DonGia/7 --TUAN -> NGAY
		ELSE @DonGia
	END
	)
	
	IF(@ChietKhau <> 100)
	BEGIN
		SET @TongTienThucChay = ISNULL((SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh
									WHERE HopDongChiTietREF = @HopDongChiTietREF AND NgayThucHien BETWEEN '2017-12-31' AND @NgayThucHien AND TrangThaiHopDong <> 3),0)
		SET @ThanhTienThucChayNgay = (@DonGia*(100-@ChietKhau)/100)*@TiLeBannerSiteHDCT
		IF(@ThanhTien > @TongTienThucChay)
		BEGIN
			IF(@ThanhTien >= @ThanhTienThucChayNgay + @TongTienThucChay )
				SET @out = @DonGia*@TiLeBannerSiteHDCT
			ELSE
				SET @out = CASE WHEN @ChietKhau <> 100 THEN (@ThanhTien - @TongTienThucChay)/((100-@ChietKhau)/100)
							ELSE 0
						   END
		END
		ELSE
		BEGIN
			SET @out = 0
		END
	END
	--check voi truong hop la khuyen mai
	ELSE
	BEGIN
		SET @TongTienThucChayKM = ISNULL((SELECT SUM(ThanhTienKM + GiaTriKMThayDoi) FROM dbo.ThucChayDaTinh
									WHERE HopDongChiTietREF = @HopDongChiTietREF AND NgayThucHien BETWEEN '2017-12-31' AND @NgayThucHien AND TrangThaiHopDong <> 3),0)
		SET @ThanhTienThucChayNgayKM = @DonGia*@TiLeBannerSiteHDCT
		SET @ThanhTien = isnull((select top (1) SoLuong*DonGia from HopDongChiTiet where HopDongChiTietID = @HopDongChiTietREF order by HopDongChiTietID),0)
		IF(@ThanhTien > @TongTienThucChayKM)
		BEGIN
			IF(@ThanhTien >= @ThanhTienThucChayNgayKM + @TongTienThucChayKM )
				SET @out = @DonGia*@TiLeBannerSiteHDCT
			ELSE
				SET @out = @ThanhTien - @TongTienThucChayKM
		END
		ELSE
		BEGIN
			SET @out = 0
		END
	END
	RETURN @out;
END
```
