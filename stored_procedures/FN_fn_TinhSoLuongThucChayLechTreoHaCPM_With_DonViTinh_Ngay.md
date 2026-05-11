# Function: `fn_TinhSoLuongThucChayLechTreoHaCPM_With_DonViTinh_Ngay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2018-02-22 16:57:57.490000
- **Ngày sửa cuối**: 2018-02-23 10:49:44.200000

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
| `@TongViewThucChay` | `bigint(8)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[fn_TinhSoLuongThucChayLechTreoHaCPM_With_DonViTinh_Ngay] 
(
	@HopDongChiTietREF  INT,
	@NgayThucHien DATETIME,
	@DonGia FLOAT,
	@TiLeBannerSiteHDCT FLOAT,
	@ThanhTien FLOAT,
	@ChietKhau FLOAT, 
	@TongViewThucChay BIGINT
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out BIGINT =0, @TongTienThucChay BIGINT =0, @ThanhTienThucChayNgay BIGINT =0
	, @TienThucChayLechTreoHa BIGINT = 0, @SoLuongThucChayLechTreoHa BIGINT = 0
	
	SET @TongTienThucChay = ISNULL((SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh
								WHERE HopDongChiTietREF = @HopDongChiTietREF AND NgayThucHien BETWEEN '2017-12-31' AND @NgayThucHien AND TrangThaiHopDong <> 3),0)
	SET @ThanhTienThucChayNgay = (@DonGia*(100-@ChietKhau)/100)*@TiLeBannerSiteHDCT
	IF(@ThanhTien > @TongTienThucChay)
	BEGIN
	    IF(@ThanhTien >= @ThanhTienThucChayNgay + @TongTienThucChay )
		BEGIN
		    SET @TienThucChayLechTreoHa = 0
			SET @SoLuongThucChayLechTreoHa = 0
		END
		
		ELSE
			BEGIN
			    SET @TienThucChayLechTreoHa = ((@TongTienThucChay + @ThanhTienThucChayNgay)- @ThanhTien)
				SET @SoLuongThucChayLechTreoHa = (CONVERT(FLOAT, @TienThucChayLechTreoHa)/CONVERT(FLOAT,@ThanhTienThucChayNgay))*@TongViewThucChay
			END
			
	END
	ELSE
    BEGIN
		SET @SoLuongThucChayLechTreoHa = @TongViewThucChay
    END
	
	SET @out = ISNULL(@SoLuongThucChayLechTreoHa,0)
	RETURN @out;
END
```
