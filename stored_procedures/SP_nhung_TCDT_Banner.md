# Stored Procedure: `nhung_TCDT_Banner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:17:14.457000
- **Ngày sửa cuối**: 2026-03-05 14:17:14.457000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_TCDT_Banner
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
SELECT
    CASE WHEN GROUPING(DmBannerREF) = 1 THEN N'Tổng'
         ELSE CAST(DmBannerREF AS NVARCHAR(50)) END AS DmBannerREF,
    CASE WHEN GROUPING(DonViTinh) = 1 THEN NULL ELSE DonViTinh END AS DonViTinh,

    dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi))              AS Soluong_TC,
    dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)) AS Thanhtien_TC,
    dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi))          AS Soluong_KM,
    dbo.FormatNumber(SUM(ThanhTienKM))                                   AS ThanhTienKM
FROM dbo.ThucChayDaTinh
WHERE HopDongChiTietREF = @HopDongChiTietID
GROUP BY GROUPING SETS
(
    (DmBannerREF, DonViTinh),
    ()
)
ORDER BY
    GROUPING(DmBannerREF),     -- 0 = chi tiết, 1 = tổng  => tổng xuống cuối
    DmBannerREF;

END

```
