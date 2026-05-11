# Stored Procedure: `prc_validate_NativeAds_OnImages`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-12 10:23:01.413000
- **Ngày sửa cuối**: 2026-03-12 10:23:01.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE  PROCEDURE dbo.prc_validate_NativeAds_OnImages
(
    @NgayThucHien DATE
)
AS
BEGIN
SET NOCOUNT ON;

DECLARE @NgayHN DATE = DATEADD(DAY,-1,@NgayThucHien)
DECLARE @NgayHQ DATE = DATEADD(DAY,-2,@NgayThucHien)

IF EXISTS ( 
    SELECT 1
    FROM Thucchay_native_ads
    WHERE NgayThucHien = @NgayHN
)
BEGIN

;WITH HomNay AS (
    SELECT 
        TypeProduct, DmSanPhamREF,
        ROUND(SUM(ISNULL(SoLuongThucchay, 0)), 0)        AS SL_HN,
        ROUND(SUM(ISNULL(ThanhtienthucchaySauCK, 0)), 0) AS TT_HN
    FROM Thucchay_native_ads
    WHERE SoHopdong <> 'TONGSANPHAM'
      AND NgayThucHien = @NgayHN
    GROUP BY TypeProduct, DmSanPhamREF
),

HomQua AS (
    SELECT 
        TypeProduct, DmSanPhamREF,
        ROUND(SUM(ISNULL(SoLuongThucchay, 0)), 0)        AS SL_HQ,
        ROUND(SUM(ISNULL(ThanhtienthucchaySauCK, 0)), 0) AS TT_HQ
    FROM Thucchay_native_ads
    WHERE SoHopdong <> 'TONGSANPHAM'
      AND NgayThucHien = @NgayHQ
    GROUP BY TypeProduct, DmSanPhamREF
),

ToolData AS (
    SELECT 
        TypeProduct, DmSanPhamREF,
        ROUND(SUM(ISNULL(SoLuongThucchay, 0)), 0)        AS SL_Tool,
        ROUND(SUM(ISNULL(ThanhtienthucchaySauCK, 0)), 0) AS TT_Tool
    FROM Thucchay_native_ads
    WHERE SoHopdong = 'TONGSANPHAM'
      AND NgayThucHien = @NgayHN
    GROUP BY TypeProduct, DmSanPhamREF
),

X AS (
    SELECT
        N'Native Ads / On images' AS NativeAds_Onimages,
        COALESCE(HN.TypeProduct, HQ.TypeProduct) AS TypeProduct,
        COALESCE(HN.DmSanPhamREF, HQ.DmSanPhamREF) AS DmSanPhamREF,
        ISNULL(sp.TenSanPham, N'(Không rõ)') AS TenSanPham,

        ROUND(ISNULL(HN.SL_HN,0),0) AS SL_HN,
        ROUND(ISNULL(HN.TT_HN,0),0) AS TT_HN,
        ROUND(ISNULL(HQ.SL_HQ,0),0) AS SL_HQ,
        ROUND(ISNULL(HQ.TT_HQ,0),0) AS TT_HQ,

        ROUND(ISNULL(TL.SL_Tool,0),0) AS SL_Tool,
        ROUND(ISNULL(TL.TT_Tool,0),0) AS TT_Tool,

        CASE WHEN HN.DmSanPhamREF IS NULL THEN 1 ELSE 0 END AS Missing_ASD_HN,
        CASE WHEN TL.DmSanPhamREF IS NULL THEN 1 ELSE 0 END AS Missing_Tool_HN

    FROM HomNay HN
    FULL OUTER JOIN HomQua HQ
        ON HN.TypeProduct  = HQ.TypeProduct
       AND HN.DmSanPhamREF = HQ.DmSanPhamREF

    LEFT JOIN ToolData TL 
        ON COALESCE(HN.TypeProduct,  HQ.TypeProduct)  = TL.TypeProduct
       AND COALESCE(HN.DmSanPhamREF, HQ.DmSanPhamREF) = TL.DmSanPhamREF

    LEFT JOIN DmSanPham sp 
        ON sp.DmSanPhamID = COALESCE(HN.DmSanPhamREF, HQ.DmSanPhamREF)
),

Y AS (
    SELECT
        *,
        (SL_HN - SL_Tool) AS Diff_SL_ASD_Tool,
        (TT_HN - TT_Tool) AS Diff_TT_ASD_Tool,
        (SL_HN - SL_HQ)   AS Diff_SL_HN_HQ,
        (TT_HN - TT_HQ)   AS Diff_TT_HN_HQ,

        CONCAT(
            CASE WHEN Missing_ASD_HN  = 1 THEN N'Thiếu ASD, '  END,
            CASE WHEN Missing_Tool_HN = 1 THEN N'Thiếu Tool, ' END,
            CASE WHEN Missing_ASD_HN = 0 AND Missing_Tool_HN = 0 AND SL_HN <> SL_Tool THEN N'SL, ' END,
            CASE WHEN Missing_ASD_HN = 0 AND Missing_Tool_HN = 0 AND TT_HN <> TT_Tool THEN N'Tiền, ' END
        ) AS LyDoLechRaw
    FROM X
),

Z AS (
    SELECT
        y.*,
        CASE 
            WHEN y.LyDoLechRaw IS NULL OR y.LyDoLechRaw = N'' THEN N''
            ELSE LEFT(
                    y.LyDoLechRaw,
                    LEN(y.LyDoLechRaw) - (PATINDEX('%[^, ]%', REVERSE(y.LyDoLechRaw)) - 1)
                 )
        END AS LyDoLech
    FROM Y y
)

SELECT
    NativeAds_Onimages,
    TypeProduct,
    TenSanPham,
    DmSanPhamREF,

    CONCAT(
        CASE 
            WHEN Missing_ASD_HN = 1 OR Missing_Tool_HN = 1 THEN N'⚠ '
            WHEN SL_HN = SL_Tool THEN N'✅ '
            ELSE N'❌ '
        END,
        dbo.FormatNumber(SL_HN), N' / ', dbo.FormatNumber(SL_Tool),
        N' (',
        CASE WHEN Diff_SL_ASD_Tool > 0 THEN N'+' WHEN Diff_SL_ASD_Tool < 0 THEN N'-' ELSE N'±' END,
        dbo.FormatNumber(ABS(Diff_SL_ASD_Tool)),
        N')'
    ) AS [SL HN (ASD/Tool)],

    CONCAT(
        CASE 
            WHEN Missing_ASD_HN = 1 OR Missing_Tool_HN = 1 THEN N'⚠ '
            WHEN TT_HN = TT_Tool THEN N'✅ '
            ELSE N'❌ '
        END,
        dbo.FormatNumber(TT_HN), N' / ', dbo.FormatNumber(TT_Tool),
        N' (',
        CASE WHEN Diff_TT_ASD_Tool > 0 THEN N'+' WHEN Diff_TT_ASD_Tool < 0 THEN N'-' ELSE N'±' END,
        dbo.FormatNumber(ABS(Diff_TT_ASD_Tool)),
        N')'
    ) AS [TT HN (ASD/Tool)],

    CONCAT(
        CASE 
            WHEN Diff_SL_HN_HQ > 0 THEN N'⬆ '
            WHEN Diff_SL_HN_HQ < 0 THEN N'⬇ '
            ELSE N'➡ '
        END,
        FORMAT(
            CASE WHEN SL_HQ = 0 THEN 0 ELSE ABS(Diff_SL_HN_HQ)*100.0/NULLIF(SL_HQ,0) END,'N2'
        ),
        N'% (', dbo.FormatNumber(ABS(Diff_SL_HN_HQ)), N')'
    ) AS [SL % (HN vs HQ)],

    CONCAT(
        CASE 
            WHEN Diff_TT_HN_HQ > 0 THEN N'⬆ '
            WHEN Diff_TT_HN_HQ < 0 THEN N'⬇ '
            ELSE N'➡ '
        END,
        FORMAT(
            CASE WHEN TT_HQ = 0 THEN 0 ELSE ABS(Diff_TT_HN_HQ)*100.0/NULLIF(TT_HQ,0) END,'N2'
        ),
        N'% (', dbo.FormatNumber(ABS(Diff_TT_HN_HQ)), N')'
    ) AS [TT % (HN vs HQ)],

    COALESCE(
        CASE WHEN LyDoLech IS NULL OR LyDoLech = N'' THEN N'Khớp' END,
        CASE WHEN LyDoLech <> N'' THEN CONCAT(N'Lệch: ', LyDoLech) END
    ) AS TrangThai

FROM Z
ORDER BY TypeProduct, DmSanPhamREF;

END
END

```
