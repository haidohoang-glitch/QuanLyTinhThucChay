# Stored Procedure: `nhung_ThucChay_BrandingMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-27 11:52:07.570000
- **Ngày sửa cuối**: 2026-03-27 11:52:07.570000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE dbo.nhung_ThucChay_BrandingMobile
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        CASE 
            WHEN GROUPING(SoHopDong) = 1 THEN NULL
            ELSE SoHopDong
        END AS SoHopDong,

        CASE 
            WHEN GROUPING(HopDongChiTietREF) = 1 THEN NULL
            ELSE HopDongChiTietREF
        END AS HopDongChiTietREF,

        CASE 
            WHEN GROUPING(DmBannerREF) = 1 THEN N'Tổng'
            ELSE CAST(DmBannerREF AS NVARCHAR(50))
        END AS DmBannerID,

        CASE 
            WHEN GROUPING(DmSanPhamREF) = 1 THEN NULL
            ELSE CAST(DmSanPhamREF AS NVARCHAR(50))
        END AS DmSanPhamREF,

        dbo.FormatNumber(SUM(TongViewThucChay))  AS TongViewThucChay,
        dbo.FormatNumber(SUM(TongClickThucChay)) AS TongClickThucChay,

        MIN(NgayThucHien) AS MinNgayThucHien,
        MAX(NgayThucHien) AS MaxNgayThucHien

    FROM dbo.ThucChay
    WHERE DmBannerREF IN
    (
        SELECT DmBannerREF
        FROM dbo.ThucChayHopDongChiTiet
        WHERE HopDongChiTietREF = @HopDongChiTietID
              AND DeletedStatus = 0
    )

    GROUP BY 
    GROUPING SETS
    (
        (SoHopDong, HopDongChiTietREF, DmBannerREF, DmSanPhamREF), -- chi tiết
        () -- tổng ALL duy nhất
    )

    ORDER BY
        GROUPING(DmBannerREF), -- tổng xuống cuối
        SoHopDong;

END

```
