# Stored Procedure: `nhung_ThucChayHopDongChiTiet_CPD_nguon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:04:41.767000
- **Ngày sửa cuối**: 2026-03-06 16:04:41.767000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThucChayHopDongChiTiet_CPD_nguon
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS (
        SELECT
            id,
            Contract_Id,
            Contract_Detail_Id,
            Product_Id,
            Banner_Id,
            Dm_NhanHang_Id,
            TenNhanHang,
            CAST(Booking_Id AS NVARCHAR(50)) AS Booking_Id,
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

            Deleted_Status,
            Created_At,
            Created_By,
            Last_Modified_At,
            Last_Modified_By,
            GhiChu,
            TenBanner,
            Banner_size
        FROM ASDAG2.ThucTreo.dbo.ThucTreo
        WHERE Contract_Detail_Id = @HopDongChiTietID
          AND Deleted_Status = 0
    ),

    DISTINCT_3KEY AS (
        -- chỉ lấy 1 lần cho mỗi Booking + ngày
        SELECT DISTINCT
            Booking_Id,
            ThoiGianBatDau,
            ThoiGianKetThuc,
            SoNgayChay
        FROM DATA
    ),

    FINAL AS (
        -- Chi tiết
        SELECT
            0 AS SortKey,
            id,
            Contract_Id,
            Contract_Detail_Id,
            Product_Id,
            Banner_Id,
            Dm_NhanHang_Id,
            TenNhanHang,
            Booking_Id,
            ThoiGianBatDau,
            ThoiGianKetThuc,
            SoNgayChay,
            Deleted_Status,
            Created_At,
            Created_By,
            Last_Modified_At,
            Last_Modified_By,
            GhiChu,
            TenBanner,
            Banner_size
        FROM DATA

        UNION ALL

        -- Tổng
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
            NULL,
            NULL,
            SUM(SoNgayChay),
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL
        FROM DISTINCT_3KEY
    )

    SELECT
        id,
        Contract_Id,
        Contract_Detail_Id,
        Product_Id,
        Banner_Id,
        Dm_NhanHang_Id,
        TenNhanHang,
        Booking_Id,
        ThoiGianBatDau,
        ThoiGianKetThuc,
        SoNgayChay,
        Deleted_Status,
        Created_At,
        Created_By,
        Last_Modified_At,
        Last_Modified_By,
        GhiChu,
        TenBanner,
        Banner_size
    FROM FINAL
    ORDER BY SortKey, Booking_Id, ThoiGianBatDau, ThoiGianKetThuc;

END

```
