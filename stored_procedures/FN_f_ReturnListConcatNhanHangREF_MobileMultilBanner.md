# Function: `f_ReturnListConcatNhanHangREF_MobileMultilBanner`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-17 09:20:58.513000
- **Ngày sửa cuối**: 2016-03-17 09:20:58.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@BannerType` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
select [dbo].[f_ReturnListConcatNhanHangREF_MobileMultilBanner] ('qc1110000',)
* */
CREATE FUNCTION [dbo].[f_ReturnListConcatNhanHangREF_MobileMultilBanner] 
(
	@SoHopDong NVARCHAR(100),
	@DmWebsiteREF INT,
	@NgayThucHien DATETIME,
	@BannerType INT
	
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
			AND a.SoHopDong = @SoHopDong
			AND tchdctab.DeletedStatus = 0	
			--AND a.DmWebsiteREF = @DmWebsiteREF		
			AND a.BannerType = @BannerType
	       ) T	       	
	
	RETURN @out;
END
```
