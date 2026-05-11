# Stored Procedure: `CheckDL_Dauvao_PerformanceBase_Daily_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-03-19 18:20:23.197000
- **Ngày sửa cuối**: 2025-08-01 11:17:05.693000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngaythuchien` | `date(3)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[CheckDL_Dauvao_PerformanceBase_Daily_PhanBo] @ngaythuchien DATE = NULL
AS
BEGIN
    SET NOCOUNT ON;
    IF @ngaythuchien IS NULL
        SET @ngaythuchien = CONVERT(DATE, GETDATE());

WITH Tong AS (
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
    WHERE tc.NgayThucHien = @ngaythuchien
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
    WHERE pb.NgayThucHien = @ngaythuchien
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
    WHERE mkt.NgayThucHien = @ngaythuchien
    GROUP BY mkt.NgayThucHien, mkt.DmSanPhamREF
)

SELECT 
    ISNULL(t.NgayThucHien, c.NgayThucHien) AS NgayThucHien,
    ISNULL(t.TenSanPham, c.TenSanPham) AS TenSanPham,
    ISNULL(t.DmViTriREF, c.DmViTriREF) AS DmViTriREF,
    ISNULL(t.TenViTri, c.TenViTri) AS TenViTri,
    dbo.FormatNumber(c.soluonguser_SP) soluonguser_SP,

    dbo.FormatNumber(c.TotalView_SP) TotalView_SP,
    dbo.FormatNumber(t.Total_view) Total_view,
    dbo.FormatNumber(c.TotalClick_SP) TotalClick_SP,
    dbo.FormatNumber(t.Total_click) Total_click,
    dbo.FormatNumber(c.TongTienTC_SP) TongTienTC_SP,
    dbo.FormatNumber(t.TongTienTC) TongTienTC,
    dbo.FormatNumber(c.TongTienKhuyenMai_SP) TongTienKhuyenMai_SP,
    dbo.FormatNumber(t.TongTienKhuyenMai) TongTienKhuyenMai,

    dbo.FormatNumber(ISNULL(c.TongTienTC_SP, 0) - ISNULL(t.TongTienTC, 0)) AS ChenhlechTCSP_Total,
    dbo.FormatNumber(ISNULL(c.TongTienKhuyenMai_SP, 0) - ISNULL(t.TongTienKhuyenMai, 0)) AS ChenhlechKMSP_Total,

	-- ✅ Ghi chú tiền thực chạy
    CASE 
        WHEN ABS(ROUND(ISNULL(c.TongTienTC_SP, 0) - ISNULL(t.TongTienTC, 0), 0)) <= 1000 
            THEN N'✅ DL Tổng = Chi tiết'
        WHEN ROUND(ISNULL(c.TongTienTC_SP, 0), 0) > ROUND(ISNULL(t.TongTienTC, 0), 0) 
            THEN CONCAT(N'⬆ DL Tổng < Chi tiết: ', dbo.FormatNumber(ROUND(c.TongTienTC_SP - t.TongTienTC, 0)))
        WHEN ROUND(ISNULL(c.TongTienTC_SP, 0), 0) < ROUND(ISNULL(t.TongTienTC, 0), 0) 
            THEN CONCAT(N'⬇ DL Tổng > Chi tiết: ', dbo.FormatNumber(ROUND(t.TongTienTC - c.TongTienTC_SP, 0)))
        ELSE N'❌ Không xác định'
    END AS GhiChu_ThucChay,

    -- ✅ Ghi chú tiền khuyến mãi
    CASE 
        WHEN ABS(ROUND(ISNULL(c.TongTienKhuyenMai_SP, 0) - ISNULL(t.TongTienKhuyenMai, 0), 0)) <= 1000 
            THEN N'✅ DL Tổng = Chi tiết'
        WHEN ROUND(ISNULL(c.TongTienKhuyenMai_SP, 0), 0) > ROUND(ISNULL(t.TongTienKhuyenMai, 0), 0) 
            THEN CONCAT(N'⬆ DL Tổng < Chi tiết: ', dbo.FormatNumber(ROUND(c.TongTienKhuyenMai_SP - t.TongTienKhuyenMai, 0)))
        WHEN ROUND(ISNULL(c.TongTienKhuyenMai_SP, 0), 0) < ROUND(ISNULL(t.TongTienKhuyenMai, 0), 0) 
            THEN CONCAT(N'⬇ DL Tổng > Chi tiết: ', dbo.FormatNumber(ROUND(t.TongTienKhuyenMai - c.TongTienKhuyenMai_SP, 0)))
        ELSE N'❌ Không xác định'
    END AS GhiChu_KhuyenMai

FROM Tong t
FULL OUTER JOIN ChiTiet c
    ON t.DmSanPhamREF = c.DmSanPhamREF 
    AND ISNULL(t.DmViTriREF, '') = ISNULL(c.DmViTriREF, '')
    AND t.NgayThucHien = c.NgayThucHien
WHERE ISNULL(t.NgayThucHien, c.NgayThucHien) = @ngaythuchien
ORDER BY c.DmViTriREF

---Lệnh cũ thời điểm Linh KS
----    EXEC [dbo].[prc_updateDL_Admarket_Daily_Toltal] @ngaythuchien = @ngaythuchien;
------ PHẦN 1
----SELECT 
----    A.NgayThucHien,
----	A.TenSanPham,
----    A.DmViTriREF,
----    A.TenViTri,
----    A.soluonguser_SP,
----    dbo.FormatNumber(A.TotalView_SP) AS TotalView_SP,
----    dbo.FormatNumber(B.total_view) AS Total_view,
----    dbo.FormatNumber(A.TotalClick_SP) AS TotalClick_SP,
----    dbo.FormatNumber(B.total_click) AS Total_click,
----    dbo.FormatNumber(A.TongTienTC_SP) AS TongTienTC_SP,
----    dbo.FormatNumber(B.TongTienTC) AS TongTienTC,
----    dbo.FormatNumber(A.TongTienKhuyenMai_SP) AS TongTienKhuyenMai_SP,
----    dbo.FormatNumber(B.TongTienKhuyenMai) AS TongTienKhuyenMai,
----    (A.TongTienTC_SP - B.TongTienTC) AS ChenhlechTCSP_Toltal,
----    (A.TongTienKhuyenMai_SP - B.TongTienKhuyenMai) AS ChenhlechKMSP_Toltal

----FROM (
----    SELECT 
----        tcpb.NgayThucHien,
----        tcpb.DmViTriREF,
----        tcpb.DmSanPhamREF,
----        tcpb.TenSanPham,
----        tcpb.TenViTri,
----        COUNT(DISTINCT tcpb.username) AS soluonguser_SP,
----        ROUND(SUM(CONVERT(FLOAT, tcpb.domain_tt_view)), 0) AS TotalView_SP,
----        ROUND(SUM(CONVERT(FLOAT, tcpb.domain_tt_click)), 0) AS TotalClick_SP,
----        ROUND(SUM(CONVERT(FLOAT, tcpb.domain_tt_money)), 0) AS TongTienTC_SP,
----        ROUND(SUM(CONVERT(FLOAT, tcpb.domain_tt_promotion)), 0) AS TongTienKhuyenMai_SP
----    FROM dbo.ThucChayAdmarket_PhanBo tcpb
----    WHERE tcpb.NgayThucHien = @ngaythuchien
----    GROUP BY tcpb.NgayThucHien, tcpb.TenSanPham, tcpb.TenViTri, tcpb.DmViTriREF, tcpb.DmSanPhamREF
----) A
----INNER JOIN (
----    SELECT 
----        tctol.DmViTriREF,
----        tctol.DmSanPhamREF,
----        ROUND(CONVERT(FLOAT, tctol.tt_click), 0) AS total_click,
----        ROUND(CONVERT(FLOAT, tctol.tt_view), 0) AS total_view,
----        ROUND(CONVERT(FLOAT, tctol.money), 0) AS TongTienTC,
----        ROUND(CONVERT(FLOAT, tctol.promotion), 0) AS TongTienKhuyenMai
----    FROM dbo.ThucChayAdmarket_Total tctol
----    WHERE tctol.NgayThucHien = @ngaythuchien
----) B
----ON A.DmViTriREF = B.DmViTriREF AND A.DmSanPhamREF = B.DmSanPhamREF

----UNION ALL

------ PHẦN 2
----SELECT 
----    ISNULL(B.NgayThucHien, A.NgayThucHien) AS NgayThucHien,
----	B.TenSanPham,
----    NULL AS DmViTriREF,
----    NULL AS TenViTri,
----    NULL AS soluonguser_SP,
----    NULL AS TotalView_SP,
----    NULL AS Total_view,
----    NULL AS TotalClick_SP,
----    NULL AS Total_click,
----    dbo.FormatNumber(ISNULL(A.TongTienTC_SP, 0)) AS TongTienTC_SP,
----    dbo.FormatNumber(ISNULL(B.TongTienTC, 0)) AS TongTienTC,
----    dbo.FormatNumber(ISNULL(A.TongTienKhuyenMai_SP, 0)) AS TongTienKhuyenMai_SP,
----    dbo.FormatNumber(ISNULL(B.TongTienKhuyenMai, 0)) AS TongTienKhuyenMai,
----    ISNULL(A.TongTienTC_SP, 0) - ISNULL(B.TongTienTC, 0) AS ChenhlechTCSP_Toltal,
----    ISNULL(A.TongTienKhuyenMai_SP, 0) - ISNULL(B.TongTienKhuyenMai, 0) AS ChenhlechKMSP_Toltal
----FROM (
----    SELECT 
----        tctol.DmSanPhamREF,
----        tctol.TenSanPham,
----        tctol.NgayThucHien,
----        ROUND(CONVERT(FLOAT, tctol.money), 0) AS TongTienTC,
----        ROUND(CONVERT(FLOAT, tctol.promotion), 0) AS TongTienKhuyenMai
----    FROM dbo.ThucChayAdmarket_Total tctol
----    WHERE tctol.NgayThucHien = @ngaythuchien
----) B
----FULL JOIN (
----    SELECT 
----        mktfr.NgayThucHien,
----        mktfr.DmSanPhamREF,
----        ROUND(SUM(CONVERT(FLOAT, mktfr.balance)), 0) AS TongTienTC_SP,
----        ROUND(SUM(CONVERT(FLOAT, mktfr.promotion)), 0) AS TongTienKhuyenMai_SP
----    FROM dbo.ThucChayMarketingFee_PerformanceBaseFinal mktfr
----    WHERE mktfr.NgayThucHien = @ngaythuchien
----    GROUP BY mktfr.NgayThucHien, mktfr.DmSanPhamREF
----) A 
----ON A.DmSanPhamREF = B.DmSanPhamREF AND A.NgayThucHien = B.NgayThucHien
----WHERE ISNULL(B.DmSanPhamREF, A.DmSanPhamREF) = 817

END;

```
