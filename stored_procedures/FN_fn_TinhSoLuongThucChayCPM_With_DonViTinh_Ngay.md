# Function: `fn_TinhSoLuongThucChayCPM_With_DonViTinh_Ngay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2018-02-22 17:10:18.547000
- **Ngày sửa cuối**: 2019-09-03 09:57:41.703000

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
| `@TongViewThucChayBanner` | `bigint(8)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[fn_TinhSoLuongThucChayCPM_With_DonViTinh_Ngay] 
(
	@HopDongChiTietREF  INT,
	@NgayThucHien DATETIME,
	@DonGia FLOAT,
	@TiLeBannerSiteHDCT FLOAT,
	@ThanhTien FLOAT,
	@ChietKhau FLOAT,
	@TongViewThucChayBanner BIGINT
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out BIGINT =0, @TongTienThucChay BIGINT =0, @ThanhTienThucChayNgay BIGINT =0,
	@TienThucChayThucThu BIGINT = 0, @DmDonViTinhREF INT

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

	
	SET @TongTienThucChay = ISNULL((SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh
								WHERE HopDongChiTietREF = @HopDongChiTietREF 
								AND NgayThucHien BETWEEN '2017-12-31' AND @NgayThucHien 
								AND TrangThaiHopDong <> 3),0)

	SET @ThanhTienThucChayNgay =  (@DonGia*(100-@ChietKhau)/100)*@TiLeBannerSiteHDCT

	IF(@ThanhTien > @TongTienThucChay)
	BEGIN
	    IF(@ThanhTien >= @ThanhTienThucChayNgay + @TongTienThucChay )
		BEGIN
		    SET @out = @TongViewThucChayBanner
		END
		ELSE
		BEGIN
			SET @TienThucChayThucThu = (@ThanhTien - @TongTienThucChay)
			SET @out = CASE WHEN @ThanhTienThucChayNgay <> 0 THEN (CONVERT(FLOAT,@TienThucChayThucThu)/CONVERT(FLOAT,@ThanhTienThucChayNgay))*@TongViewThucChayBanner
						ELSE 0
						END
		END
			
	END
	ELSE
    BEGIN
        SET @out = 0
    END
	RETURN @out;
END
```
