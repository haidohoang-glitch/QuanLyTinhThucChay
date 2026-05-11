# Stored Procedure: `sp_ThongKeThucChayAdmarketTheoNgay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 16:56:12.193000
- **Ngày sửa cuối**: 2026-03-05 16:56:12.193000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_ThongKeThucChayAdmarketTheoNgay
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS (
        SELECT
            NgayThucHien,
            SUM(SoLuongThucChay + SoLuongThayDoi)               AS SoluongTC,
            SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)  AS ThanhtienTC,
            SUM(SoLuongThucChayKM + SoLuongKMThayDoi)           AS SoluongKM,
            SUM(ThanhTienKM + GiaTriKMThayDoi)                  AS ThanhtienKM
        FROM dbo.ThucChayDaTinhAdmarket
        WHERE HopDongChiTietREF = @HopDongChiTietID
        GROUP BY NgayThucHien
    ),
    FINAL AS (
        -- Chi tiết theo ngày
        SELECT
            0 AS SortKey,
            NgayThucHien,
            SoluongTC,
            ThanhtienTC,
            SoluongKM,
            ThanhtienKM
        FROM DATA

        UNION ALL

        -- Tổng
        SELECT
            1 AS SortKey,
            NULL AS NgayThucHien,
            SUM(SoluongTC),
            SUM(ThanhtienTC),
            SUM(SoluongKM),
            SUM(ThanhtienKM)
        FROM DATA
    )

    SELECT
        CASE 
            WHEN SortKey = 1 THEN N'TỔNG' 
            ELSE CONVERT(NVARCHAR(10), NgayThucHien, 23) 
        END AS NgayThucHien,
        dbo.FormatNumber(SoluongTC)   AS SoluongTC,
        dbo.FormatNumber(ThanhtienTC) AS ThanhtienTC,
        dbo.FormatNumber(SoluongKM)   AS SoluongKM,
        dbo.FormatNumber(ThanhtienKM) AS ThanhtienKM
    FROM FINAL
    ORDER BY SortKey, NgayThucHien DESC;

END

```
