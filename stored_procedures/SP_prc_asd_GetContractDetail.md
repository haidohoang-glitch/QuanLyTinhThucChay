# Stored Procedure: `prc_asd_GetContractDetail`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-26 11:54:08.697000
- **Ngày sửa cuối**: 2017-04-26 16:07:36.377000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@CONTRACT_NO` | `varchar(200)` | No |
| `@PRODUCT_ID` | `int(4)` | No |

## Definition (Source Code)

```sql

-- dbo.prc_asd_GetListCommitContractDetail @pageIndex = 1, @CONTRACT_ID='',@pageSize = 10

CREATE PROCEDURE [dbo].prc_asd_GetContractDetail
    @CONTRACT_NO VARCHAR(200) = '',
    @PRODUCT_ID INT = 0
AS
    BEGIN
	SELECT TOP 1
            h.HopDongID ,
            h.SoHopDong ,
            hq.TenHinhThucQuangCao ,
            db.TenLoaiBanner ,
            ds.TenSanPham ,
            h.GiaTriHopDong
    FROM     HopDong h
            LEFT JOIN dbo.HopDongChiTiet hc ON h.HopDongID = hc.HopDongFK
            LEFT JOIN dbo.DmSanPham ds ON hc.DmSanPhamREF = ds.DmSanPhamID
            LEFT JOIN dbo.DmLoaiBanner db ON hc.DmLoaiBannerREF = db.DmLoaiBannerID
            LEFT JOIN dbo.DmHinhThucQuangCao hq ON hc.DmLoaiREF = hq.DmHinhThucQuangCaoID
    WHERE    (@CONTRACT_NO = '' OR h.SoHopDong = @CONTRACT_NO)
            AND (@PRODUCT_ID = 0 OR hc.DmSanPhamREF = @PRODUCT_ID )
    END;

```
