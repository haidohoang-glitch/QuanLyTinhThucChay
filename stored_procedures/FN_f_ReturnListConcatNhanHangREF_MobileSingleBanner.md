# Function: `f_ReturnListConcatNhanHangREF_MobileSingleBanner`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-17 09:20:58.260000
- **Ngày sửa cuối**: 2016-03-17 09:20:58.260000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@ProductUnitName` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
/*
select [dbo].[f_ReturnListConcatNhanHangREFByBanner] ('qc1110000',)
* */
CREATE FUNCTION [dbo].[f_ReturnListConcatNhanHangREF_MobileSingleBanner] 
(
	@SoHopDong NVARCHAR(100),
	@TypeProduct INT,
	@HopDongChiTietREF  INT,
	@DmWebsiteREF INT,
	@NgayThucHien DATETIME,
	@ProductUnitName NVARCHAR(100)
	
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out NVARCHAR(2000);
	SELECT @out = COALESCE(@out + ',', '') + CAST(T.DsNhanHangREF AS VARCHAR(1000))
	FROM   (
			SELECT distinct tchdctab.DsNhanHangREF	
			FROM ThucChay_MobileTemp A 
			INNER JOIN ThucChayHopDongChiTietAndBanner tchdctab 
			ON CONVERT(NVARCHAR(50),A.DmBannerREF) = tchdctab.DmBannerID
			WHERE 1=1 
			AND A.NgayThucHien = @NgayThucHien			
			AND tchdctab.HopDongChiTietREF = @HopDongChiTietREF
			AND a.SoHopDong = @SoHopDong
			AND tchdctab.DeletedStatus = 0	
			--AND a.DmWebsiteREF = @DmWebsiteREF		
			AND A.ProductUnitName = @ProductUnitName								            	
	       ) T	       	
	
	RETURN @out;
END
```
