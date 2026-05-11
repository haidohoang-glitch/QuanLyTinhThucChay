# Stored Procedure: `sp_DotChayHopDongChiTiet_TongNgay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:13:04.720000
- **Ngày sửa cuối**: 2026-03-06 16:16:21.003000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE sp_DotChayHopDongChiTiet_TongNgay
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS (
        SELECT 
            HopDongChiTietREF,
            CAST(bookingREF AS NVARCHAR(50)) AS bookingREF,

            -- Ép kiểu an toàn
            TRY_CONVERT(DATETIME, ThoiGianBatDau)  AS ThoiGianBatDau,
            TRY_CONVERT(DATETIME, ThoiGianKetThuc) AS ThoiGianKetThuc,

            -- Tính số ngày chạy
            CASE 
                WHEN TRY_CONVERT(DATETIME, ThoiGianBatDau) IS NOT NULL
                 AND TRY_CONVERT(DATETIME, ThoiGianKetThuc) IS NOT NULL
                THEN DATEDIFF(
                        DAY,
                        TRY_CONVERT(DATETIME, ThoiGianBatDau),
                        TRY_CONVERT(DATETIME, ThoiGianKetThuc)
                     ) + 1
                ELSE NULL
            END AS SoNgayChay,

            RecordStatus,
            DeletedStatus,
            CreatedAt,
            CreatedBy,
            LastModifiedAt,
            LastModifiedBy,
            dotChayHopDongChiTietID,
            ViTri,
            TenWebsite,
            HopDongREF,
            GhiChu
        FROM dbo.DotChayHopDongChiTiet
        WHERE HopDongChiTietREF = @HopDongChiTietID
          AND DeletedStatus = 0
    ),

    FINAL AS (
        -- Chi tiết
        SELECT
            0 AS STT,
            HopDongChiTietREF,
            bookingREF,
            ThoiGianBatDau,
            ThoiGianKetThuc,
            SoNgayChay,
            RecordStatus,
            DeletedStatus,
            CreatedAt,
            CreatedBy,
            LastModifiedAt,
            LastModifiedBy,
            dotChayHopDongChiTietID,
            ViTri,
            TenWebsite,
            HopDongREF,
            GhiChu
        FROM DATA

        UNION ALL

        -- Tổng
        SELECT
            1 AS STT,
            NULL AS HopDongChiTietREF,
            N'TỔNG' AS bookingREF,
            NULL AS ThoiGianBatDau,
            NULL AS ThoiGianKetThuc,
            SUM(SoNgayChay) AS SoNgayChay,
            NULL AS RecordStatus,
            NULL AS DeletedStatus,
            NULL AS CreatedAt,
            NULL AS CreatedBy,
            NULL AS LastModifiedAt,
            NULL AS LastModifiedBy,
            NULL AS dotChayHopDongChiTietID,
            NULL AS ViTri,
            NULL AS TenWebsite,
            NULL AS HopDongREF,
            NULL AS GhiChu
        FROM DATA
    )

    SELECT *
    FROM FINAL
    ORDER BY STT, ThoiGianBatDau;

END

```
