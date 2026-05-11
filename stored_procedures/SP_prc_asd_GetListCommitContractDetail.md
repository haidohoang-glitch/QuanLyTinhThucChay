# Stored Procedure: `prc_asd_GetListCommitContractDetail`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-26 09:30:10.923000
- **Ngày sửa cuối**: 2017-05-09 14:27:51.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FROM_DATE` | `datetime(8)` | No |
| `@TO_DATE` | `datetime(8)` | No |
| `@CONTRACT` | `varchar(200)` | No |
| `@PRODUCT` | `varchar(200)` | No |
| `@HTQC` | `varchar(200)` | No |
| `@MUA_NGOAI` | `bit(1)` | No |

## Definition (Source Code)

```sql

-- dbo.prc_asd_GetListCommitContractDetail @FROM_DATE='2017-04-17',  @TO_DATE='2017-04-25'

CREATE PROCEDURE [dbo].[prc_asd_GetListCommitContractDetail]
    @FROM_DATE DATETIME = NULL ,
    @TO_DATE DATETIME = NULL ,
    @CONTRACT VARCHAR(200) = '' ,
    @PRODUCT VARCHAR(200) = '' ,
    @HTQC VARCHAR(200) = '' ,
    @MUA_NGOAI BIT = 0
AS
    BEGIN
        SELECT TOP 50
                GETDATE() NgayThucHien ,
                h.HopDongID ,
                h.SoHopDong ,
                hc.HopDongChiTietID HopDongChiTietREF,
                hq.TenHinhThucQuangCao ,
                db.TenLoaiBanner ,
                hc.DmSanPhamREF ,
                ds.TenSanPham ,
                h.GiaTriHopDong ,
				h.GiaTriHopDong AS GiaTriThayDoi,
                h.GiaTriHopDong / 2 GiaTriThucChay ,
				CONVERT(MONEY, 50) AS TiLe
        FROM    dbo.HopDong h
                LEFT JOIN dbo.HopDongChiTiet hc ON h.HopDongID = hc.HopDongFK
                LEFT JOIN dbo.DmSanPham ds ON hc.DmSanPhamREF = ds.DmSanPhamID
                LEFT JOIN dbo.DmLoaiBanner db ON hc.DmLoaiBannerREF = db.DmLoaiBannerID
                LEFT JOIN dbo.DmHinhThucQuangCao hq ON hc.DmLoaiREF = hq.DmHinhThucQuangCaoID
        WHERE    ( @CONTRACT = ''
                    OR h.SoHopDong IN (
                    SELECT    *
                    FROM      [dbo].[fnSplitString](@CONTRACT,
                                                ',') )
                )
                AND ( @HTQC = ''
                        OR hc.DmLoaiREF IN (
                        SELECT    *
                        FROM      [dbo].[fnSplitString](@HTQC,
                                                ',') )
                    )
                AND ( @PRODUCT = ''
                        OR CONVERT(VARCHAR(10), hc.DmSanPhamREF) IN (
                        SELECT    *
                        FROM      [dbo].[fnSplitString](@PRODUCT,
                                                ',') )
                    )
				--AND h.NgayThucHien BETWEEN @FROM_DATE AND @TO_DATE
    END;

```
