# Stored Procedure: `nhung_ThucChay_Branding`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 17:04:14.643000
- **Ngày sửa cuối**: 2026-03-27 11:52:26.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThucChay_Branding
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        SoHopDong,

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
        SoHopDong,
        GROUPING SETS
        (
            (DmBannerREF, DmSanPhamREF), -- chi tiết
            ()                           -- tổng
        )

    ORDER BY
        GROUPING(DmBannerREF),  -- đảm bảo dòng tổng ở cuối
        SoHopDong,
        DmBannerID;

END

```
