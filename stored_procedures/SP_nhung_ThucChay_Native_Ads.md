# Stored Procedure: `nhung_ThucChay_Native_Ads`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:05:49.537000
- **Ngày sửa cuối**: 2026-03-05 14:06:23.900000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThucChay_Native_Ads
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

    dbo.FormatNumber(SUM(SoLuongThucChay))        AS SoLuongThucChay,
    dbo.FormatNumber(SUM(ThanhTienThucChaySauCK)) AS ThanhTienThucChaySauCK,
    dbo.FormatNumber(SUM(SoLuongThucChayKM))      AS SoLuongThucChayKM,
    dbo.FormatNumber(SUM(ThanhTienThucChayKM))    AS ThanhTienThucChayKM,
    MIN(NgayThucHien)                             AS MinNgayThucHien,
    MAX(NgayThucHien)                             AS MaxNgayThucHien
FROM dbo.ThucChay_Native_Ads
WHERE DmBannerID IN (
    SELECT DmBannerREF
    FROM dbo.ThucChayHopDongChiTiet
    WHERE HopDongChiTietREF = @HopDongChiTietID
      AND DeletedStatus = 0
)
GROUP BY GROUPING SETS (
    (DmBannerID),  -- dòng chi tiết
    ()             -- dòng tổng
)
ORDER BY
    GROUPING(DmBannerID),  -- đảm bảo dòng Tổng ở cuối
    DmBannerID;
END

```
