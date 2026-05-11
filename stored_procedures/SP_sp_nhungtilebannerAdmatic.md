# Stored Procedure: `sp_nhungtilebannerAdmatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-04-16 09:43:50.603000
- **Ngày sửa cuối**: 2026-04-16 09:55:27.853000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `bigint(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhungtilebannerAdmatic
    @HopDongChiTietID BIGINT
AS
BEGIN
    SET NOCOUNT ON;

    SELECT B.*
    FROM (
        SELECT 
            ThucChayHopDongChiTietID,
            DmBannerREF,
            DmSanPhamREF
        FROM ThucChayHopDongChiTiet 
        WHERE HopDongChiTietREF = @HopDongChiTietID
            AND DeletedStatus = 0
    ) A
    LEFT JOIN ( 
        SELECT 
            ThucChayHopDongChiTietREF,
            HopDongREF,
            HopDongChiTietREF,
            DmSanPhamREF,
            DmBannerREF,
            TiLeThucChayHDCTSoVoiBanner,
			DaThucHienUpdateTiLe,
			DeletedStatus
        FROM ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic 
        WHERE HopDongChiTietREF = @HopDongChiTietID
		 AND DeletedStatus = 0
    ) B 
    ON A.ThucChayHopDongChiTietID = B.ThucChayHopDongChiTietREF;
END;

```
