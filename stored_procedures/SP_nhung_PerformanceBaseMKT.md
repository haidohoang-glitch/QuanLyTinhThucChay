# Stored Procedure: `nhung_PerformanceBaseMKT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 15:53:05.287000
- **Ngày sửa cuối**: 2026-03-05 16:07:51.397000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_PerformanceBaseMKT
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS
    (
        SELECT
            ID,
            contract,
            phanbo,

            CAST(balance AS FLOAT)   AS balance,
            CAST(promotion AS FLOAT) AS promotion,
            CAST(chietkhau AS FLOAT) AS chietkhau,

            DmSanPhamREF,
            NgayThucHien,
            createdBy,
            createdAt
        FROM dbo.ThucChayMarketingFee_PerformanceBaseFinal
        WHERE phanbo = @HopDongChiTietID
    )

    SELECT
        ID,
        contract,
        phanbo,
        dbo.FormatNumber(balance)   AS balance,
        dbo.FormatNumber(promotion) AS promotion,
        dbo.FormatNumber(chietkhau) AS chietkhau,
        DmSanPhamREF,
        NgayThucHien,
        createdBy,
        createdAt
    FROM DATA

    UNION ALL

    SELECT
        NULL,
        NULL,
        NULL,
        dbo.FormatNumber(SUM(balance)),
        dbo.FormatNumber(SUM(promotion)),
        dbo.FormatNumber(SUM(chietkhau)),
        NULL,
        NULL,
        NULL,
        NULL
    FROM DATA
END

```
