# Stored Procedure: `prc_validate_Admarket_Total_vs_SP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-12 10:48:26.387000
- **Ngày sửa cuối**: 2026-03-12 10:48:26.387000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.prc_validate_Admarket_Total_vs_SP
(
    @NgayThucHien DATE
)
AS
BEGIN
SET NOCOUNT ON;

DECLARE @NgayChay DATE = DATEADD(DAY,-1,@NgayThucHien)

;WITH Tong AS (
    SELECT 
        tc.NgayThucHien,
        CASE 
            WHEN tc.product IN (N'adx_pc', N'adx_mobile', N'adx_ecom', N'adx_leadform') THEN '585'
            WHEN tc.product = N'cpc' THEN '144'
            WHEN tc.product = N'mktf' THEN '817'
            ELSE '999'
        END AS DmSanPhamREF,
        CASE 
            WHEN tc.product = N'adx_pc' THEN '1'
            WHEN tc.product = N'adx_mobile' THEN '2'
            WHEN tc.product = N'adx_ecom' THEN '3'
            WHEN tc.product = N'adx_leadform' THEN '4'
            WHEN tc.product = N'cpc' THEN '0'
            WHEN tc.product = N'mktf' THEN NULL
            ELSE '999'
        END AS DmViTriREF,
        CASE 
            WHEN tc.product IN (N'adx_pc', N'adx_mobile', N'adx_ecom', N'adx_leadform') THEN N'ADX'
            WHEN tc.product = N'cpc' THEN N'CPC Admarket'
            WHEN tc.product = N'mktf' THEN N'Marketing fee – Chi phí marketing'
            ELSE N'Không xác định'
        END AS TenSanPham,
        CASE 
            WHEN tc.product = N'adx_pc' THEN N'ADX'
            WHEN tc.product = N'adx_mobile' THEN N'AdX Mobile'
            WHEN tc.product = N'adx_ecom' THEN N'AdX Ecommerce'
            WHEN tc.product = N'adx_leadform' THEN N'Adx Leadform'
            WHEN tc.product = N'cpc' THEN N'CPC Admarket'
            WHEN tc.product = N'mktf' THEN NULL
            ELSE N'Không xác định'
        END AS TenViTri,

        ROUND(CONVERT(FLOAT, tc.tt_view), 0) AS Total_view,
        ROUND(CONVERT(FLOAT, tc.tt_click), 0) AS Total_click,
        ROUND(CONVERT(FLOAT, tc.money), 0) AS TongTienTC,
        ROUND(CONVERT(FLOAT, tc.promotion), 0) AS TongTienKhuyenMai

    FROM dbo.ThucChayAdmarket_Total tc
    WHERE tc.NgayThucHien = @NgayChay
),

ChiTiet AS (
    SELECT 
        pb.NgayThucHien,
        pb.DmSanPhamREF,
        pb.DmViTriREF,
        pb.TenSanPham,
        pb.TenViTri,

        COUNT(DISTINCT pb.username) AS soluonguser_SP,

        ROUND(SUM(CONVERT(FLOAT, pb.domain_tt_view)), 0) AS TotalView_SP,
        ROUND(SUM(CONVERT(FLOAT, pb.domain_tt_click)), 0) AS TotalClick_SP,
        ROUND(SUM(CONVERT(FLOAT, pb.domain_tt_money)), 0) AS TongTienTC_SP,
        ROUND(SUM(CONVERT(FLOAT, pb.domain_tt_promotion)), 0) AS TongTienKhuyenMai_SP

    FROM dbo.ThucChayAdmarket_PhanBo pb
    WHERE pb.NgayThucHien = @NgayChay
    GROUP BY pb.NgayThucHien, pb.DmSanPhamREF, pb.DmViTriREF, pb.TenSanPham, pb.TenViTri

    UNION ALL

    SELECT 
        mkt.NgayThucHien,
        mkt.DmSanPhamREF,
        NULL,
        N'Marketing fee – Chi phí marketing',
        NULL,
        NULL,
        NULL,
        NULL,
        ROUND(SUM(CONVERT(FLOAT, mkt.balance)), 0),
        ROUND(SUM(CONVERT(FLOAT, mkt.promotion)), 0)

    FROM dbo.ThucChayMarketingFee_PerformanceBaseFinal mkt
    WHERE mkt.NgayThucHien = @NgayChay
    GROUP BY mkt.NgayThucHien, mkt.DmSanPhamREF
),

X AS
(
    SELECT 
        ISNULL(t.NgayThucHien, c.NgayThucHien) AS NgayThucHien,
        ISNULL(t.DmSanPhamREF, c.DmSanPhamREF) AS DmSanPhamREF,
        ISNULL(t.TenSanPham, c.TenSanPham) AS TenSanPham,
        ISNULL(t.DmViTriREF, c.DmViTriREF) AS DmViTriREF,
        ISNULL(t.TenViTri, c.TenViTri) AS TenViTri,

        ISNULL(c.soluonguser_SP, 0) AS soluonguser_SP,

        ROUND(ISNULL(c.TotalView_SP, 0), 0) AS View_SP_0,
        ROUND(ISNULL(t.Total_view, 0), 0) AS View_Tong_0,

        ROUND(ISNULL(c.TotalClick_SP, 0), 0) AS Click_SP_0,
        ROUND(ISNULL(t.Total_click, 0), 0) AS Click_Tong_0,

        ROUND(ISNULL(c.TongTienTC_SP, 0), 0) AS TienTC_SP_0,
        ROUND(ISNULL(t.TongTienTC, 0), 0) AS TienTC_Tong_0,

        ROUND(ISNULL(c.TongTienKhuyenMai_SP, 0), 0) AS TienKM_SP_0,
        ROUND(ISNULL(t.TongTienKhuyenMai, 0), 0) AS TienKM_Tong_0

    FROM Tong t
    FULL OUTER JOIN ChiTiet c
        ON t.DmSanPhamREF = c.DmSanPhamREF
        AND ISNULL(t.DmViTriREF,'') = ISNULL(c.DmViTriREF,'')
        AND t.NgayThucHien = c.NgayThucHien
),

Y AS
(
    SELECT
        *,
        CONCAT(
            CASE WHEN View_SP_0  = View_Tong_0  THEN N'' ELSE N'View, ' END,
            CASE WHEN Click_SP_0 = Click_Tong_0 THEN N'' ELSE N'Click, ' END,
            CASE WHEN ABS(TienTC_SP_0 - TienTC_Tong_0) <= 1000 THEN N'' ELSE N'Tiền, ' END,
            CASE WHEN ABS(TienKM_SP_0 - TienKM_Tong_0) <= 1000 THEN N'' ELSE N'KM, ' END
        ) AS LyDoLechRaw
    FROM X
)

SELECT
    NgayThucHien,
    TenSanPham,
    DmViTriREF,
    TenViTri,
    dbo.FormatNumber(soluonguser_SP) AS soluonguser_SP,

    CONCAT(
        CASE WHEN View_SP_0 = View_Tong_0 THEN N'✅ ' ELSE N'❌ ' END,
        dbo.FormatNumber(View_SP_0), N' / ', dbo.FormatNumber(View_Tong_0)
    ) AS [View (SP/Total)],

    CONCAT(
        CASE WHEN Click_SP_0 = Click_Tong_0 THEN N'✅ ' ELSE N'❌ ' END,
        dbo.FormatNumber(Click_SP_0), N' / ', dbo.FormatNumber(Click_Tong_0)
    ) AS [Click (SP/Total)],

    CONCAT(
        CASE WHEN ABS(TienTC_SP_0 - TienTC_Tong_0) <= 1000 THEN N'✅ ' ELSE N'❌ ' END,
        dbo.FormatNumber(TienTC_SP_0), N' / ', dbo.FormatNumber(TienTC_Tong_0)
    ) AS [TienTC (SP/Total)],

    CONCAT(
        CASE WHEN ABS(TienKM_SP_0 - TienKM_Tong_0) <= 1000 THEN N'✅ ' ELSE N'❌ ' END,
        dbo.FormatNumber(TienKM_SP_0), N' / ', dbo.FormatNumber(TienKM_Tong_0)
    ) AS [TienKM (SP/Total)],

    CASE
        WHEN LyDoLechRaw = N'' THEN N'Khớp'
        ELSE CONCAT(N'Lệch: ', LEFT(LyDoLechRaw, LEN(LyDoLechRaw) - 2))
    END AS TrangThai

FROM Y
ORDER BY DmViTriREF;

END

```
