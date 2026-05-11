# Stored Procedure: `nhung_ThucChayHopDongChiTiet_TongSoNgayChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:06:51.647000
- **Ngày sửa cuối**: 2026-03-06 16:06:51.647000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThucChayHopDongChiTiet_TongSoNgayChay
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH RAW AS (
        SELECT
            CAST(BookingREF AS NVARCHAR(50)) AS BookingREF,
            TRY_CONVERT(DATE, ThoiGianBatDau)  AS NgayBatDau,
            TRY_CONVERT(DATE, ThoiGianKetThuc) AS NgayKetThucGoc
        FROM dbo.ThucChayHopDongChiTiet
        WHERE HopDongChiTietREF = @HopDongChiTietID
          AND DeletedStatus = 0
    ),

    DATA AS (
        SELECT
            BookingREF,
            NgayBatDau,
            CASE 
                WHEN NgayKetThucGoc > DATEADD(DAY, -1, CAST(GETDATE() AS DATE))
                    THEN DATEADD(DAY, -1, CAST(GETDATE() AS DATE))
                ELSE NgayKetThucGoc
            END AS NgayKetThucTinh
        FROM RAW
        WHERE NgayBatDau IS NOT NULL
          AND NgayKetThucGoc IS NOT NULL
    ),

    KQ AS (
        SELECT
            BookingREF,
            NgayBatDau AS ThoiGianBatDau,
            NgayKetThucTinh AS ThoiGianKetThuc,
            CASE 
                WHEN NgayKetThucTinh >= NgayBatDau
                    THEN DATEDIFF(DAY, NgayBatDau, NgayKetThucTinh) + 1
                ELSE 0
            END AS SoNgayChay
        FROM DATA
        GROUP BY BookingREF, NgayBatDau, NgayKetThucTinh
    ),

    FINAL AS (
        -- Chi tiết
        SELECT
            0 AS SortKey,
            BookingREF,
            ThoiGianBatDau,
            ThoiGianKetThuc,
            SoNgayChay
        FROM KQ

        UNION ALL

        -- Tổng
        SELECT
            1 AS SortKey,
            N'TỔNG' AS BookingREF,
            NULL AS ThoiGianBatDau,
            NULL AS ThoiGianKetThuc,
            SUM(SoNgayChay) AS SoNgayChay
        FROM KQ
    )

    SELECT
        BookingREF,
        ThoiGianBatDau,
        ThoiGianKetThuc,
        SoNgayChay
    FROM FINAL
    ORDER BY SortKey, BookingREF, ThoiGianBatDau, ThoiGianKetThuc;

END

```
