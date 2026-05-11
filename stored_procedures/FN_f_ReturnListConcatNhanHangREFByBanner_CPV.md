# Function: `f_ReturnListConcatNhanHangREFByBanner_CPV`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-17 09:20:57.510000
- **Ngày sửa cuối**: 2016-03-17 09:20:57.510000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
select [dbo].[f_ReturnListConcatNhanHangREFByBanner] ('qc1110000',)
* */
CREATE FUNCTION [dbo].[f_ReturnListConcatNhanHangREFByBanner_CPV] 
(
	@SoHopDong NVARCHAR(100),
	@TypeProduct INT,
	@HopDongChiTietREF  INT,
	@DmWebsiteREF INT
	
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out NVARCHAR(2000);
	SELECT @out = COALESCE(@out + ',', '') + CAST(T.DsNhanHangREF AS VARCHAR(1000))
	FROM   (
			SELECT distinct
			B.DsNhanHangREF
			from (
				select tc.NgayThucHien, tc.TongViewThucChay, tc.TongClickThucChay
				, tc.TongSoBaiViet,tc.SoHopDong,
				(
					CASE WHEN ISNULL(tcc.totalview,0) = 0 THEN 0
					ELSE (tc.TongViewThucChay/tcc.totalview)*tcc.CPV
					END
				)SoLuongCPV
				, tc.TypeProduct, tc.DmWebsiteREF, tc.TenWebsite, tc.DmBannerREF
				  from ThucChayTemp tc INNER JOIN ThucChayCPVTemp tcc ON tc.DmBannerREF = tcc.bannerid
				  AND tcc.NgayThucHien = tc.NgayThucHien
			) A
			INNER JOIN  
			(
				SELECT DISTINCT b.DmBannerID,
				       b.HopDongChiTietREF,
				       b.HopDongREF,
				       b.DsNhanHangREF,
				       b.TiLeThucChayHDCTSoVoiBanner,
				       b.DeletedStatus,
				       b.DaThucHienUpdateTiLe
				FROM   dbo.ThucChayHopDongChiTietAndBanner b
				       INNER JOIN HopDongChiTiet hdct
				            ON  hdct.HopDongChiTietID = b.HopDongChiTietREF
				WHERE  hdct.DeletedStatus = 0
				       AND hdct.DonViTinhREF = 22 --CPV
			) B on B.DmBannerID = Convert(nvarchar(50),A.DmBannerREF)
			WHERE A.SoHopDong = @SoHopDong AND a.TypeProduct = @TypeProduct        
			AND A.DmWebsiteREF = @DmWebsiteREF
			AND B.HopDongChiTietREF = @HopDongChiTietREF
			AND B.DeletedStatus = 0
	       ) T	       	
	
	RETURN @out;
END
```
