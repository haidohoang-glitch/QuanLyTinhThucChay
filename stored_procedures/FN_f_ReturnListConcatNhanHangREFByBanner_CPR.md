# Function: `f_ReturnListConcatNhanHangREFByBanner_CPR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-17 09:20:57.763000
- **Ngày sửa cuối**: 2016-03-17 09:20:57.763000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
select [dbo].[f_ReturnListConcatNhanHangREFByBanner_CPR] ('qc1110000',)
* */
CREATE FUNCTION [dbo].[f_ReturnListConcatNhanHangREFByBanner_CPR] 
(
	@HopDongID INT,
	@NgayThucHien DATETIME,
	@TypeProduct INT,
	@HopDongChiTietREF  INT
	
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out NVARCHAR(2000);
	SELECT @out = COALESCE(@out + ',', '') + CAST(T.DsNhanHangREF AS VARCHAR(1000))
	FROM   (
			SELECT distinct 
				B.DsNhanHangREF
			FROM  
			(
				SELECT distinct b.DmBannerID, b.HopDongChiTietREF, b.HopDongREF, b.DsNhanHangREF, isnull(b.TiLeThucChayHDCTSoVoiBanner,0)TiLeThucChayHDCTSoVoiBanner,
				b.DeletedStatus, b.DaThucHienUpdateTiLe
			   from dbo.ThucChayHopDongChiTietAndBanner b
			) B INNER JOIN ThucChayCPRTemp tcc ON Convert(nvarchar(50),tcc.bannerid) = B.DmBannerID
			WHERE b.HopDongREF = @HopDongID 
			AND tcc.TypeProduct = @TypeProduct 
			AND tcc.NgayThucHien = @NgayThucHien
			AND B.HopDongChiTietREF = @HopDongChiTietREF
			AND B.DeletedStatus = 0
	       ) T	       	
	
	RETURN @out;
END
```
