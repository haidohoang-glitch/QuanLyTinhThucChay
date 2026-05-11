# Stored Procedure: `nhung_TCDT_IDtreoPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:46:05.020000
- **Ngày sửa cuối**: 2026-03-05 14:46:05.020000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_TCDT_IDtreoPR
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA_NUM AS (
        SELECT
            LTRIM(RTRIM(
                CASE 
                    WHEN CHARINDEX(':', DotChayBooking) > 0 
                        THEN LEFT(DotChayBooking, CHARINDEX(':', DotChayBooking) - 1)
                    ELSE DotChayBooking
                END
            )) AS DotChayBooking,
            SUM(SoLuongThucChay + SoLuongThayDoi)              AS Soluong_TC,
            SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS Thanhtien_TC,
            SUM(SoLuongThucChayKM + SoLuongKMThayDoi)          AS Soluong_KM,
            SUM(ThanhTienKM)                                   AS ThanhTienKM
        FROM dbo.ThucChayDaTinh
        WHERE HopDongChiTietREF = @HopDongChiTietID
        GROUP BY
            LTRIM(RTRIM(
                CASE 
                    WHEN CHARINDEX(':', DotChayBooking) > 0 
                        THEN LEFT(DotChayBooking, CHARINDEX(':', DotChayBooking) - 1)
                    ELSE DotChayBooking
                END
            ))
    ),
    FINAL AS (
        -- Chi tiết
        SELECT
            0 AS SortKey,
            DotChayBooking,
            Soluong_TC,
            Thanhtien_TC,
            Soluong_KM,
            ThanhTienKM
        FROM DATA_NUM

        UNION ALL

        -- Tổng
        SELECT
            1 AS SortKey,
            N'TỔNG' AS DotChayBooking,
            SUM(Soluong_TC),
            SUM(Thanhtien_TC),
            SUM(Soluong_KM),
            SUM(ThanhTienKM)
        FROM DATA_NUM
    )

    SELECT
        DotChayBooking,
        dbo.FormatNumber(Soluong_TC)   AS Soluong_TC,
        dbo.FormatNumber(Thanhtien_TC) AS Thanhtien_TC,
        dbo.FormatNumber(Soluong_KM)   AS Soluong_KM,
        dbo.FormatNumber(ThanhTienKM)  AS ThanhTienKM
    FROM FINAL
    ORDER BY SortKey, DotChayBooking;

END

```
