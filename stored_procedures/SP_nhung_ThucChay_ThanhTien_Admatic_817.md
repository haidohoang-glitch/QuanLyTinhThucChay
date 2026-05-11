# Stored Procedure: `nhung_ThucChay_ThanhTien_Admatic_817`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-10 09:57:16.657000
- **Ngày sửa cuối**: 2026-03-10 09:57:16.657000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThucChay_ThanhTien_Admatic_817
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
	SELECT
    CASE 
        WHEN GROUPING(DmBannerID) = 1 THEN N'Tổng'
        ELSE CAST(DmBannerID AS NVARCHAR(50))
    END AS DmBannerID,

    CASE 
        WHEN GROUPING(DmSanPhamREF) = 1 THEN NULL
        ELSE CAST(DmSanPhamREF AS NVARCHAR(50))
    END AS DmSanPhamREF,

    dbo.FormatNumber(SUM(SoLuongThucChay))                AS SoLuongThucChay,
    dbo.FormatNumber(SUM(ThanhTienThucChaySauCK_ChuaVAT)) AS ThanhTienThucChaySauCK_ChuaVAT,
    dbo.FormatNumber(SUM(SoLuongThucChayKM))              AS SoLuongThucChay_KM,
    dbo.FormatNumber(SUM(ThanhTienThucChayKM))            AS ThanhTienKM_ChuaVAT,
    MIN(NgayThucHien)                                     AS MinNgayThucHien,
    MAX(NgayThucHien)                                     AS MaxNgayThucHien,

    CASE 
        WHEN GROUPING(VAT) = 1 THEN N'ALL'
        ELSE CAST(VAT AS NVARCHAR(20))
    END AS VAT
FROM dbo.ThucChay_ThanhTien_Admatic t
WHERE EXISTS (
    SELECT 1
    FROM dbo.ThucChayHopDongChiTiet c
    WHERE c.HopDongChiTietREF = @HopDongChiTietID
      AND c.DeletedStatus = 0
      AND c.DmBannerREF  = t.DmBannerID
      AND c.DmSanPhamREF = t.DmSanPhamREF
	  AND c.DmSanPhamREF = 817
)
AND t.DmSanPhamREF = 817
AND t.HopDongChiTietREF = @HopDongChiTietID
GROUP BY GROUPING SETS
(
    (DmBannerID, DmSanPhamREF, VAT),
    ()
)
ORDER BY
    CASE WHEN GROUPING(DmBannerID) = 1 THEN 1 ELSE 0 END,
    DmBannerID,
    DmSanPhamREF;

END

```
