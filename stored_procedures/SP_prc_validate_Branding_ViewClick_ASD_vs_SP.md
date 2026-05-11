# Stored Procedure: `prc_validate_Branding_ViewClick_ASD_vs_SP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-12 10:16:05.480000
- **Ngày sửa cuối**: 2026-03-12 10:16:05.480000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.prc_validate_Branding_ViewClick_ASD_vs_SP
(
    @NgayThucHien DATE
)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @NgayHN DATE = DATEADD(DAY,-1,@NgayThucHien)
    DECLARE @NgayHQ DATE = DATEADD(DAY,-1,@NgayHN)

    ;WITH HomNay_SP AS 
    (
        SELECT 
            tc.TypeProduct, tc.DmSanPhamREF,
            SUM(ISNULL(tc.TongViewThucChay, 0))  AS View_SP_HN,
            SUM(ISNULL(tc.TongClickThucChay, 0)) AS Click_SP_HN
        FROM ThucChay tc
        WHERE tc.SoHopdong = 'TONGSANPHAM'
          AND tc.CreatedBy NOT LIKE N'%From API_Admatic%'
          AND tc.NgayThucHien = @NgayHN
        GROUP BY tc.TypeProduct, tc.DmSanPhamREF
    ),

    HomNay_ASD AS 
    (
        SELECT 
            tc.TypeProduct, tc.DmSanPhamREF,
            SUM(ISNULL(tc.TongViewThucChay, 0))  AS View_ASD_HN,
            SUM(ISNULL(tc.TongClickThucChay, 0)) AS Click_ASD_HN
        FROM ThucChay tc
        WHERE tc.SoHopdong <> 'TONGSANPHAM'
          AND tc.CreatedBy NOT LIKE N'%From API_Admatic%'
          AND tc.NgayThucHien = @NgayHN
        GROUP BY tc.TypeProduct, tc.DmSanPhamREF
    ),

    HomQua_ASD AS 
    (
        SELECT 
            tc.TypeProduct, tc.DmSanPhamREF,
            SUM(ISNULL(tc.TongViewThucChay, 0))  AS View_ASD_HQ,
            SUM(ISNULL(tc.TongClickThucChay, 0)) AS Click_ASD_HQ
        FROM ThucChay tc
        WHERE tc.SoHopdong <> 'TONGSANPHAM'
          AND tc.CreatedBy NOT LIKE N'%From API_Admatic%'
          AND tc.NgayThucHien = @NgayHQ
        GROUP BY tc.TypeProduct, tc.DmSanPhamREF
    ),

    X AS 
    (
        SELECT
            N'Branding' AS Branding,
            dsp.TenSanPham,
            ISNULL(n_asd.DmSanPhamREF, ISNULL(n_sp.DmSanPhamREF, q_asd.DmSanPhamREF)) AS DmSanPhamREF,
            ISNULL(n_asd.TypeProduct, ISNULL(n_sp.TypeProduct, q_asd.TypeProduct))     AS TypeProduct,

            ROUND(ISNULL(n_asd.View_ASD_HN, 0), 0)  AS View_ASD_HN,
            ROUND(ISNULL(n_sp.View_SP_HN, 0), 0)    AS View_SP_HN,
            ROUND(ISNULL(n_asd.Click_ASD_HN, 0), 0) AS Click_ASD_HN,
            ROUND(ISNULL(n_sp.Click_SP_HN, 0), 0)   AS Click_SP_HN,

            ROUND(ISNULL(q_asd.View_ASD_HQ, 0), 0)  AS View_ASD_HQ,
            ROUND(ISNULL(q_asd.Click_ASD_HQ, 0), 0) AS Click_ASD_HQ,

            CASE WHEN n_asd.DmSanPhamREF IS NULL THEN 1 ELSE 0 END AS Missing_ASD_HN,
            CASE WHEN n_sp.DmSanPhamREF  IS NULL THEN 1 ELSE 0 END AS Missing_SP_HN
        FROM HomNay_ASD n_asd
        FULL OUTER JOIN HomNay_SP n_sp 
            ON n_asd.TypeProduct  = n_sp.TypeProduct 
           AND n_asd.DmSanPhamREF = n_sp.DmSanPhamREF
        FULL OUTER JOIN HomQua_ASD q_asd 
            ON ISNULL(n_asd.TypeProduct, n_sp.TypeProduct)   = q_asd.TypeProduct 
           AND ISNULL(n_asd.DmSanPhamREF, n_sp.DmSanPhamREF) = q_asd.DmSanPhamREF
        LEFT JOIN dbo.DmSanPham dsp 
            ON dsp.DmSanPhamID = ISNULL(n_asd.DmSanPhamREF, ISNULL(n_sp.DmSanPhamREF, q_asd.DmSanPhamREF))
    ),

    Y AS 
    (
        SELECT
            *,
            (View_ASD_HN  - View_SP_HN)    AS Diff_View_ASD_SP,
            (Click_ASD_HN - Click_SP_HN)   AS Diff_Click_ASD_SP,
            (View_ASD_HN  - View_ASD_HQ)   AS Diff_View_HN_HQ,
            (Click_ASD_HN - Click_ASD_HQ)  AS Diff_Click_HN_HQ,

            CONCAT(
                CASE WHEN Missing_ASD_HN = 1 THEN N'Thiếu ASD, ' ELSE N'' END,
                CASE WHEN Missing_SP_HN  = 1 THEN N'Thiếu SP, '  ELSE N'' END,
                CASE WHEN Missing_ASD_HN = 0 AND Missing_SP_HN = 0 AND View_ASD_HN  <> View_SP_HN  THEN N'View, '  ELSE N'' END,
                CASE WHEN Missing_ASD_HN = 0 AND Missing_SP_HN = 0 AND Click_ASD_HN <> Click_SP_HN THEN N'Click, ' ELSE N'' END
            ) AS LyDoLechRaw
        FROM X
    ),

    Z AS 
    (
        SELECT
            y.*,
            CASE 
                WHEN y.LyDoLechRaw = N'' THEN N''
                ELSE LEFT(
                        y.LyDoLechRaw,
                        LEN(y.LyDoLechRaw) - (PATINDEX('%[^, ]%', REVERSE(y.LyDoLechRaw)) - 1)
                     )
            END AS LyDoLech
        FROM Y y
    )

    SELECT
        Branding,
        TenSanPham,
        DmSanPhamREF,
        TypeProduct,

        CONCAT(
            CASE 
                WHEN Missing_ASD_HN = 1 OR Missing_SP_HN = 1 THEN N'⚠ '
                WHEN View_ASD_HN = View_SP_HN THEN N'✅ '
                ELSE N'❌ '
            END,
            dbo.FormatNumber(View_ASD_HN), N' / ', dbo.FormatNumber(View_SP_HN),
            N' (',
            CASE WHEN Diff_View_ASD_SP > 0 THEN N'+' WHEN Diff_View_ASD_SP < 0 THEN N'-' ELSE N'±' END,
            dbo.FormatNumber(ABS(Diff_View_ASD_SP)),
            N')'
        ) AS [View HN (ASD/SP)],

        CONCAT(
            CASE 
                WHEN Missing_ASD_HN = 1 OR Missing_SP_HN = 1 THEN N'⚠ '
                WHEN Click_ASD_HN = Click_SP_HN THEN N'✅ '
                ELSE N'❌ '
            END,
            dbo.FormatNumber(Click_ASD_HN), N' / ', dbo.FormatNumber(Click_SP_HN),
            N' (',
            CASE WHEN Diff_Click_ASD_SP > 0 THEN N'+' WHEN Diff_Click_ASD_SP < 0 THEN N'-' ELSE N'±' END,
            dbo.FormatNumber(ABS(Diff_Click_ASD_SP)),
            N')'
        ) AS [Click HN (ASD/SP)],

        CONCAT(
            CASE 
                WHEN Diff_View_HN_HQ > 0 THEN N'⬆ '
                WHEN Diff_View_HN_HQ < 0 THEN N'⬇ '
                ELSE N'➡ '
            END,
            dbo.FormatNumber(View_ASD_HQ),
            N' → ',
            dbo.FormatNumber(View_ASD_HN),
            N' (',
            CASE WHEN Diff_View_HN_HQ > 0 THEN N'+' WHEN Diff_View_HN_HQ < 0 THEN N'-' ELSE N'0' END,
            dbo.FormatNumber(ABS(Diff_View_HN_HQ)),
            N')'
        ) AS [View HQ → HN (ASD)],

        CONCAT(
            CASE 
                WHEN Diff_Click_HN_HQ > 0 THEN N'⬆ '
                WHEN Diff_Click_HN_HQ < 0 THEN N'⬇ '
                ELSE N'➡ '
            END,
            dbo.FormatNumber(Click_ASD_HQ),
            N' → ',
            dbo.FormatNumber(Click_ASD_HN),
            N' (',
            CASE WHEN Diff_Click_HN_HQ > 0 THEN N'+' WHEN Diff_Click_HN_HQ < 0 THEN N'-' ELSE N'0' END,
            dbo.FormatNumber(ABS(Diff_Click_HN_HQ)),
            N')'
        ) AS [Click HQ → HN (ASD)],

        CASE
            WHEN LyDoLech = N'' THEN N'Khớp'
            ELSE CONCAT(N'Lệch: ', LyDoLech)
        END AS TrangThai

    FROM Z
    ORDER BY TypeProduct;

END

```
