# Function: `f_ReturnListConcatNhanHangREFByBanner_gttd`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2024-10-14 17:04:12.213000
- **Ngày sửa cuối**: 2024-10-14 17:04:12.213000

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
CREATE FUNCTION [dbo].[f_ReturnListConcatNhanHangREFByBanner_gttd] 
(
	@SoHopDong NVARCHAR(100),
	@TypeProduct INT,
	@HopDongChiTietREF  INT,
	@DmWebsiteREF INT
	
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out NVARCHAR(2000);
	SELECT @out = COALESCE(@out + ',', '') + CAST(isnull(T.dsNhanHangREF,'') AS VARCHAR(1000))
	FROM   (
				SELECT DISTINCT B.dsNhanHangREF
				from ThucChayTemp_TinhLai A
				INNER JOIN  
				(
					SELECT distinct b.DmBannerID, b.dsNhanHangREF, b.HopDongChiTietREF, b.HopDongREF, b.TiLeThucChayHDCTSoVoiBanner,
					b.DeletedStatus, b.DaThucHienUpdateTiLe
				   from dbo.ThucChayHopDongChiTietAndBanner b
				) B on B.DmBannerID = Convert(nvarchar(50),A.DmBannerREF)
				WHERE A.SoHopDong = @SoHopDong AND A.TypeProduct = @TypeProduct 
				--AND A.DmWebsiteREF = @DmWebsiteREF
				AND B.DeletedStatus = 0
				AND B.HopDongChiTietREF = @HopDongChiTietREF
				
				--SELECT DISTINCT B.dsNhanHangREF
				--from ThucChay A
				--INNER JOIN  
				--(
				--	SELECT distinct b.DmBannerID, b.dsNhanHangREF, b.HopDongChiTietREF, b.HopDongREF, b.TiLeThucChayHDCTSoVoiBanner,
				--	b.DeletedStatus, b.DaThucHienUpdateTiLe
				--   from dbo.ThucChayHopDongChiTietAndBanner b
				--) B on B.DmBannerID = Convert(nvarchar(50),A.DmBannerREF)
				--WHERE a.SoHopDong = @SoHopDong AND a.TypeProduct = @TypeProduct 
				--AND A.DmWebsiteREF = @DmWebsiteREF
				--AND B.DeletedStatus = 0
				--AND B.HopDongChiTietREF = @HopDongChiTietREF
				--AND A.NgayThucHien = '2016-02-18'
	       ) T	       	
	
	SET @out = ISNULL(@out,'')
	RETURN @out;
END
```
