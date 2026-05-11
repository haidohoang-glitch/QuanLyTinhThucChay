# Stored Procedure: `CheckDL_Dauvao_PerformanceBase_Daily_PhanBo_backup_20250728`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-07-28 12:45:23.620000
- **Ngày sửa cuối**: 2025-07-28 12:45:23.620000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngaythuchien` | `date(3)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[CheckDL_Dauvao_PerformanceBase_Daily_PhanBo_backup_20250728] @ngaythuchien DATE = NULL
AS
BEGIN
    SET NOCOUNT ON;
    IF @ngaythuchien IS NULL
        SET @ngaythuchien = CONVERT(DATE, GETDATE());
    EXEC [dbo].[prc_updateDL_Admarket_Daily_Toltal] @ngaythuchien = @ngaythuchien;
-- PHẦN 1
SELECT 
    A.NgayThucHien,
	A.TenSanPham,
    A.DmViTriREF,
    A.TenViTri,
    A.soluonguser_SP,
    dbo.FormatNumber(A.TotalView_SP) AS TotalView_SP,
    dbo.FormatNumber(B.total_view) AS Total_view,
    dbo.FormatNumber(A.TotalClick_SP) AS TotalClick_SP,
    dbo.FormatNumber(B.total_click) AS Total_click,
    dbo.FormatNumber(A.TongTienTC_SP) AS TongTienTC_SP,
    dbo.FormatNumber(B.TongTienTC) AS TongTienTC,
    dbo.FormatNumber(A.TongTienKhuyenMai_SP) AS TongTienKhuyenMai_SP,
    dbo.FormatNumber(B.TongTienKhuyenMai) AS TongTienKhuyenMai,
    (A.TongTienTC_SP - B.TongTienTC) AS ChenhlechTCSP_Toltal,
    (A.TongTienKhuyenMai_SP - B.TongTienKhuyenMai) AS ChenhlechKMSP_Toltal

FROM (
    SELECT 
        tcpb.NgayThucHien,
        tcpb.DmViTriREF,
        tcpb.DmSanPhamREF,
        tcpb.TenSanPham,
        tcpb.TenViTri,
        COUNT(DISTINCT tcpb.username) AS soluonguser_SP,
        ROUND(SUM(CONVERT(FLOAT, tcpb.domain_tt_view)), 0) AS TotalView_SP,
        ROUND(SUM(CONVERT(FLOAT, tcpb.domain_tt_click)), 0) AS TotalClick_SP,
        ROUND(SUM(CONVERT(FLOAT, tcpb.domain_tt_money)), 0) AS TongTienTC_SP,
        ROUND(SUM(CONVERT(FLOAT, tcpb.domain_tt_promotion)), 0) AS TongTienKhuyenMai_SP
    FROM dbo.ThucChayAdmarket_PhanBo tcpb
    WHERE tcpb.NgayThucHien = @ngaythuchien
    GROUP BY tcpb.NgayThucHien, tcpb.TenSanPham, tcpb.TenViTri, tcpb.DmViTriREF, tcpb.DmSanPhamREF
) A
INNER JOIN (
    SELECT 
        tctol.DmViTriREF,
        tctol.DmSanPhamREF,
        ROUND(CONVERT(FLOAT, tctol.tt_click), 0) AS total_click,
        ROUND(CONVERT(FLOAT, tctol.tt_view), 0) AS total_view,
        ROUND(CONVERT(FLOAT, tctol.money), 0) AS TongTienTC,
        ROUND(CONVERT(FLOAT, tctol.promotion), 0) AS TongTienKhuyenMai
    FROM dbo.ThucChayAdmarket_Total tctol
    WHERE tctol.NgayThucHien = @ngaythuchien
) B
ON A.DmViTriREF = B.DmViTriREF AND A.DmSanPhamREF = B.DmSanPhamREF

UNION ALL

-- PHẦN 2
SELECT 
    ISNULL(B.NgayThucHien, A.NgayThucHien) AS NgayThucHien,
	B.TenSanPham,
    NULL AS DmViTriREF,
    NULL AS TenViTri,
    NULL AS soluonguser_SP,
    NULL AS TotalView_SP,
    NULL AS Total_view,
    NULL AS TotalClick_SP,
    NULL AS Total_click,
    dbo.FormatNumber(ISNULL(A.TongTienTC_SP, 0)) AS TongTienTC_SP,
    dbo.FormatNumber(ISNULL(B.TongTienTC, 0)) AS TongTienTC,
    dbo.FormatNumber(ISNULL(A.TongTienKhuyenMai_SP, 0)) AS TongTienKhuyenMai_SP,
    dbo.FormatNumber(ISNULL(B.TongTienKhuyenMai, 0)) AS TongTienKhuyenMai,
    ISNULL(A.TongTienTC_SP, 0) - ISNULL(B.TongTienTC, 0) AS ChenhlechTCSP_Toltal,
    ISNULL(A.TongTienKhuyenMai_SP, 0) - ISNULL(B.TongTienKhuyenMai, 0) AS ChenhlechKMSP_Toltal
FROM (
    SELECT 
        tctol.DmSanPhamREF,
        tctol.TenSanPham,
        tctol.NgayThucHien,
        ROUND(CONVERT(FLOAT, tctol.money), 0) AS TongTienTC,
        ROUND(CONVERT(FLOAT, tctol.promotion), 0) AS TongTienKhuyenMai
    FROM dbo.ThucChayAdmarket_Total tctol
    WHERE tctol.NgayThucHien = @ngaythuchien
) B
FULL JOIN (
    SELECT 
        mktfr.NgayThucHien,
        mktfr.DmSanPhamREF,
        ROUND(SUM(CONVERT(FLOAT, mktfr.balance)), 0) AS TongTienTC_SP,
        ROUND(SUM(CONVERT(FLOAT, mktfr.promotion)), 0) AS TongTienKhuyenMai_SP
    FROM dbo.ThucChayMarketingFee_PerformanceBaseFinal mktfr
    WHERE mktfr.NgayThucHien = @ngaythuchien
    GROUP BY mktfr.NgayThucHien, mktfr.DmSanPhamREF
) A 
ON A.DmSanPhamREF = B.DmSanPhamREF AND A.NgayThucHien = B.NgayThucHien
WHERE ISNULL(B.DmSanPhamREF, A.DmSanPhamREF) = 817

END;

```
