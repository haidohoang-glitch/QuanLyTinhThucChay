# Stored Procedure: `nhung_PerformanceBase_SHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 15:57:50.903000
- **Ngày sửa cuối**: 2026-03-05 16:17:31.363000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_PerformanceBase_SHD
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS
    (
        SELECT 
            contract_number,
            phanbo,
            username,
            TenSanPham,
            TenViTri,
            nhanhangid,
            tennhanhang,

            SUM(CONVERT(FLOAT,tt_view))            AS SL_view,
            SUM(CONVERT(FLOAT,tt_click))           AS SL_click,
            SUM(CONVERT(FLOAT,domain_tt_view))     AS SLVH_view,
            SUM(CONVERT(FLOAT,domain_tt_click))    AS SLVH_Click,
            SUM(CONVERT(FLOAT,domain_tt_money))    AS thanhtienSP,
            SUM(CONVERT(FLOAT,domain_tt_promotion)) AS thanhtienSP_KM

        FROM dbo.ThucChayAdmarket_PhanBo
        WHERE phanbo = @HopDongChiTietID
        GROUP BY 
            contract_number,
            phanbo,
            username,
            TenSanPham,
            TenViTri,
            nhanhangid,
            tennhanhang
    )

    -- 🔹 Chi tiết
    SELECT
        contract_number,
        phanbo,
        username,
        TenSanPham,
        TenViTri,
        nhanhangid,
        tennhanhang,
        dbo.FormatNumber(SL_view)       AS SL_view,
        dbo.FormatNumber(SL_click)      AS SL_click,
        dbo.FormatNumber(SLVH_view)     AS SLVH_view,
        dbo.FormatNumber(SLVH_Click)    AS SLVH_Click,
        dbo.FormatNumber(thanhtienSP)   AS thanhtienSP,
        dbo.FormatNumber(thanhtienSP_KM) AS thanhtienSP_KM
    FROM DATA

    UNION ALL

    -- 🔹 Dòng tổng
    SELECT
        N'TỔNG',
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        dbo.FormatNumber(SUM(SL_view)),
        dbo.FormatNumber(SUM(SL_click)),
        dbo.FormatNumber(SUM(SLVH_view)),
        dbo.FormatNumber(SUM(SLVH_Click)),
        dbo.FormatNumber(SUM(thanhtienSP)),
        dbo.FormatNumber(SUM(thanhtienSP_KM))
    FROM DATA

END

```
