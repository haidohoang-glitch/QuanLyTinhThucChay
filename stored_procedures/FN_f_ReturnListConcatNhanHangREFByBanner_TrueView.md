# Function: `f_ReturnListConcatNhanHangREFByBanner_TrueView`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-12-21 09:23:05.917000
- **Ngày sửa cuối**: 2018-08-28 15:01:50.410000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmBannerREF` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
select [dbo].[f_ReturnListConcatNhanHangREFByBanner] ('qc1110000',)
* */
CREATE FUNCTION [dbo].[f_ReturnListConcatNhanHangREFByBanner_TrueView]
    (
      @HopDongChiTietREF INT
    , @DmBannerREF INT
	
    )
RETURNS VARCHAR(2000)
    BEGIN
        DECLARE @out NVARCHAR(2000);
        SELECT  @out = COALESCE(@out + ',', '') + CAST(T.DsNhanHangREF AS VARCHAR(1000))
			FROM    ( SELECT DISTINCT
                            B.DsNhanHangREF
							FROM      ( SELECT DISTINCT
                                                B.DmBannerID
                                              , B.HopDongChiTietREF
                                              , B.HopDongREF
                                              , B.DsNhanHangREF
                                              , B.TiLeThucChayHDCTSoVoiBanner
                                              , B.DeletedStatus
                                              , B.DaThucHienUpdateTiLe
                                         FROM   dbo.ThucChayHopDongChiTietAndBanner B
										 INNER JOIN dbo.HopDongChiTiet hdct ON B.HopDongChiTietREF = hdct.HopDongChiTietID
                                         WHERE  1=1 AND B.HopDongChiTietREF = @HopDongChiTietREF
                                                AND (hdct.DonViTinhREF = 32 OR hdct.DonViTinhREF = 31)
												AND B.DeletedStatus = 0
										AND B.DmBannerID = CONVERT(NVARCHAR(100),@DmBannerREF)
					
						) B
				)T

        RETURN @out;
    END

```
