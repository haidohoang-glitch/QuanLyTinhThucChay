# Stored Procedure: `nhung_DataThucchay_OnImageAds`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 17:12:10.673000
- **Ngày sửa cuối**: 2026-03-05 17:12:10.673000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE dbo.nhung_DataThucchay_OnImageAds
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
SELECT
    CASE WHEN GROUPING(DmBannerID) = 1 THEN N'Tổng'
         ELSE CAST(DmBannerID AS NVARCHAR(50)) END AS DmBannerID,

    dbo.FormatNumber( SUM(TRY_CONVERT(FLOAT, SoLuongThucChay)))          AS SoLuongThucChay,
    dbo.FormatNumber(SUM(TRY_CONVERT(FLOAT, ThanhTienThucChay)))         AS ThanhTienThucChay,
    dbo.FormatNumber(SUM(TRY_CONVERT(FLOAT, SoLuongThucChayKhuyenMai)))   AS SoLuongThucChayKhuyenMai,
    dbo.FormatNumber(SUM(TRY_CONVERT(FLOAT, ThanhTienThucChaykhuyenMai))) AS ThanhTienThucChayKhuyenMai,

    CASE WHEN GROUPING(VAT) = 1 THEN NULL ELSE VAT END  AS VAT,

    dbo.FormatNumber( CASE
        -- Dòng tổng: cộng từng dòng đã loại VAT (đúng khi có nhiều VAT)
        WHEN GROUPING(DmBannerID) = 1 AND GROUPING(VAT) = 1 THEN
            SUM(
                TRY_CONVERT(FLOAT, ThanhTienThucChay) / (1 + TRY_CONVERT(FLOAT, VAT)/100.0)
            )
        -- Dòng chi tiết theo VAT: tổng gross / (1 + VAT)
        ELSE
            SUM(TRY_CONVERT(FLOAT, ThanhTienThucChay)) / (1 + TRY_CONVERT(FLOAT, VAT)/100.0)
    END) AS ThanhTienThucChay_ChuaVat

FROM dbo.DataThucchay_OnImageAds
WHERE DmBannerID IN (
    SELECT DmBannerREF
    FROM dbo.ThucChayHopDongChiTiet
    WHERE HopDongChiTietREF = @HopDongChiTietID
      AND DeletedStatus = 0
)
GROUP BY GROUPING SETS
(
    (DmBannerID, VAT),   -- chi tiết
    ()                   -- tổng
)
ORDER BY GROUPING(DmBannerID), DmBannerID;


END

```
