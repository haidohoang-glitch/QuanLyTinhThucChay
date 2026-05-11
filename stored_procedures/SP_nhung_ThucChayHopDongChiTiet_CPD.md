# Stored Procedure: `nhung_ThucChayHopDongChiTiet_CPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 15:59:56.550000
- **Ngày sửa cuối**: 2026-03-06 15:59:56.550000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThucChayHopDongChiTiet_CPD
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS (
        SELECT
            HopDongREF,
            HopDongChiTietREF,
            ThucChayHopDongChiTietID,
            DmNhanHangREF,	
            NhanHang,	
            TenHinhThucQuangCao,
            DmSanPhamREF,
            CAST(BookingREF AS NVARCHAR(50)) AS BookingREF,

            TRY_CONVERT(DATE, ThoiGianBatDau)  AS ThoiGianBatDau,
            TRY_CONVERT(DATE, ThoiGianKetThuc) AS ThoiGianKetThuc,

            CASE 
                WHEN TRY_CONVERT(DATE, ThoiGianBatDau) IS NOT NULL
                 AND TRY_CONVERT(DATE, ThoiGianKetThuc) IS NOT NULL
                THEN DATEDIFF(
                        DAY,
                        TRY_CONVERT(DATE, ThoiGianBatDau),
                        TRY_CONVERT(DATE, ThoiGianKetThuc)
                     ) + 1
                ELSE NULL
            END AS SoNgayChay,

            DmBannerREF,	
            RecordStatus,	
            DeletedStatus,	
            CreatedAt,	
            CreatedBy,
            LastModifiedAt,
            LastModifiedBy,
            Id
        FROM dbo.ThucChayHopDongChiTiet
        WHERE HopDongChiTietREF = @HopDongChiTietID
          AND DeletedStatus = 0
    ),

    -- DISTINCT theo BookingREF + ngày
    DISTINCT_NGAY AS (
        SELECT DISTINCT
            BookingREF,
            ThoiGianBatDau,
            ThoiGianKetThuc,
            SoNgayChay
        FROM DATA
    ),

    FINAL AS (
        -- Chi tiết
        SELECT
            0 AS SortKey,
            HopDongREF,
            HopDongChiTietREF,
            ThucChayHopDongChiTietID,
            DmNhanHangREF,	
            NhanHang,	
            TenHinhThucQuangCao,
            DmSanPhamREF,
            BookingREF,
            SoNgayChay,
            ThoiGianBatDau,
            ThoiGianKetThuc,
            DmBannerREF,	
            RecordStatus,	
            DeletedStatus,	
            CreatedAt,	
            CreatedBy,
            LastModifiedAt,
            LastModifiedBy,
            Id
        FROM DATA

        UNION ALL

        -- Dòng tổng (distinct ngày)
        SELECT
            1 AS SortKey,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            N'TỔNG',
            SUM(SoNgayChay),
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL
        FROM DISTINCT_NGAY
    )

    SELECT
        HopDongREF,
        HopDongChiTietREF,
        ThucChayHopDongChiTietID,
        DmNhanHangREF,	
        NhanHang,	
        TenHinhThucQuangCao,
        DmSanPhamREF,
        BookingREF,
        SoNgayChay,
        ThoiGianBatDau,
        ThoiGianKetThuc,
        DmBannerREF,	
        RecordStatus,	
        DeletedStatus,	
        CreatedAt,	
        CreatedBy,
        LastModifiedAt,
        LastModifiedBy,
        Id
    FROM FINAL
    ORDER BY SortKey, ThoiGianBatDau;

END

```
