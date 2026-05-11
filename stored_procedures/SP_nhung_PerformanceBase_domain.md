# Stored Procedure: `nhung_PerformanceBase_domain`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 15:56:29.937000
- **Ngày sửa cuối**: 2026-03-05 16:08:59.740000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_PerformanceBase_domain
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS
    (
        SELECT 
            domain_name,
            TenSanPham,
            TenViTri,
            nhanhangid,
            tennhanhang,
            SUM(CONVERT(FLOAT,domain_tt_money))      AS thanhtienSP,
            SUM(CONVERT(FLOAT,domain_tt_promotion))  AS thanhtienSP_KM
        FROM dbo.ThucChayAdmarket_PhanBo
        WHERE phanbo = @HopDongChiTietID
        GROUP BY 
            domain_name,
            TenSanPham,
            TenViTri,
            nhanhangid,
            tennhanhang
    )

    -- 🔹 Chi tiết
    SELECT
        domain_name,
        TenSanPham,
        TenViTri,
        nhanhangid,
        tennhanhang,
        dbo.FormatNumber(thanhtienSP)    AS thanhtienSP,
        dbo.FormatNumber(thanhtienSP_KM) AS thanhtienSP_KM
    FROM DATA

    UNION ALL

    -- 🔹 Dòng TỔNG
    SELECT
        N'TỔNG'  AS domain_name,
        NULL     AS TenSanPham,
        NULL     AS TenViTri,
        NULL     AS nhanhangid,
        NULL     AS tennhanhang,
        dbo.FormatNumber(SUM(thanhtienSP)),
        dbo.FormatNumber(SUM(thanhtienSP_KM))
    FROM DATA

END

```
