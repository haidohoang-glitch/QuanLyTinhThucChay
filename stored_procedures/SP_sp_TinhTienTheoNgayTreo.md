# Stored Procedure: `sp_TinhTienTheoNgayTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:08:56.487000
- **Ngày sửa cuối**: 2026-03-06 16:08:56.487000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_TinhTienTheoNgayTreo
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH TREO_RAW AS (
        SELECT
            CAST(BookingREF AS NVARCHAR(50)) AS BookingREF,
            TRY_CONVERT(DATE, ThoiGianBatDau)  AS NgayBatDau,
            TRY_CONVERT(DATE, ThoiGianKetThuc) AS NgayKetThucGoc
        FROM dbo.ThucChayHopDongChiTiet
        WHERE HopDongChiTietREF = @HopDongChiTietID
          AND DeletedStatus = 0
    ),
    TREO_DATA AS (
        SELECT
            BookingREF,
            NgayBatDau,
            CASE 
                WHEN NgayKetThucGoc > DATEADD(DAY, -1, CAST(GETDATE() AS DATE))
                    THEN DATEADD(DAY, -1, CAST(GETDATE() AS DATE))
                ELSE NgayKetThucGoc
            END AS NgayKetThucTinh
        FROM TREO_RAW
        WHERE NgayBatDau IS NOT NULL
          AND NgayKetThucGoc IS NOT NULL
    ),
    TREO_DISTINCT AS (
        SELECT DISTINCT
            BookingREF,
            NgayBatDau,
            NgayKetThucTinh,
            CASE 
                WHEN NgayKetThucTinh >= NgayBatDau
                    THEN DATEDIFF(DAY, NgayBatDau, NgayKetThucTinh) + 1
                ELSE 0
            END AS SoNgayTreo
        FROM TREO_DATA
    ),
    TONG_TREO AS (
        SELECT SUM(SoNgayTreo) AS TongSoNgayTreo
        FROM TREO_DISTINCT
    ),
    TONG_DOTCHAY AS (
        SELECT 
            SUM(
                DATEDIFF(DAY,
                    TRY_CONVERT(DATE, ThoiGianBatDau),
                    TRY_CONVERT(DATE, ThoiGianKetThuc)
                ) + 1
            ) AS TongSoNgayDotChay
        FROM dbo.DotChayHopDongChiTiet
        WHERE HopDongChiTietREF = @HopDongChiTietID
          AND DeletedStatus = 0
          AND TRY_CONVERT(DATE, ThoiGianBatDau) IS NOT NULL
          AND TRY_CONVERT(DATE, ThoiGianKetThuc) IS NOT NULL
    )

    SELECT
        dbo.FormatNumber(hdct.ThanhTien) AS ThanhTienHopDong,
        tt.TongSoNgayTreo,
        td.TongSoNgayDotChay,

        dbo.FormatNumber(
            CASE WHEN td.TongSoNgayDotChay > 0
                 THEN hdct.ThanhTien * 1.0 / td.TongSoNgayDotChay
                 ELSE NULL
            END
        ) AS DonGia_1_Ngay,

        dbo.FormatNumber(
            CASE WHEN td.TongSoNgayDotChay > 0
                 THEN tt.TongSoNgayTreo * (hdct.ThanhTien * 1.0 / td.TongSoNgayDotChay)
                 ELSE NULL
            END
        ) AS SoTien_TinhTheoNgayTreo

    FROM dbo.HopDongChiTiet hdct
    CROSS JOIN TONG_TREO tt
    CROSS JOIN TONG_DOTCHAY td
    WHERE hdct.HopDongChiTietID = @HopDongChiTietID
      AND hdct.DeletedStatus = 0;

END

```
