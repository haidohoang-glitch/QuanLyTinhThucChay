# Stored Procedure: `RaSoat_DL_PerformanceBase_HN_TCSP_MuaOnlinePB `

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-07-18 12:01:47.120000
- **Ngày sửa cuối**: 2024-07-24 09:41:58.370000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Startdate` | `date(3)` | No |
| `@Todate` | `date(3)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<linhvtt>
-- Create date: <18/07/2024>
-- Description:	<Description,,>
-- =============================================
-- kiểm soát thực chạy sản phẩm  trả về để ghi nhận online
-- tH này xét có tiền thực chạy và có thể không ghi nhận thực chạy cho phân bổ => ghi nhận hết vào online
-- kiểm tra ghi nhận từng ngày 


CREATE PROCEDURE [dbo].[RaSoat_DL_PerformanceBase_HN_TCSP_MuaOnlinePB ]
	-- Add the parameters for the stored procedure here
    @Startdate DATE = NULL,
    @Todate DATE = NULL
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT K1.NgayThucHien,
K1.contract_number,
K1.phanbo,
K1.username,
K1.DmSanPhamREF,
K1.DmViTriREF,
K1.TenViTri,
(CONVERT(FLOAT,ISNULL(K1.ThucchaySanPham,0))) ThucchaySanPham,
(CONVERT(FLOAT,ISNULL(K1.ThanhTienThucChay,0))) ThanhTienThucChay,
(CONVERT(FLOAT,ISNULL(K2.TTThucChayOnlinePB,0))) TTThucChayOnlinePB,
(CONVERT(FLOAT,ISNULL(K2.TCLuuOnlinePB,0))) TCLuuOnlinePB
--ISNULL(K1.ThanhTienThucChay,0) ThanhTienThucChay,
--ISNULL(K2.TTThucChayOnlinePB,0) TTThucChayOnlinePB,
--ISNULL(K2.TCLuuOnlinePB,0) TCLuuOnlinePB
FROM
(
    SELECT tctk.NgayThucHien,
           tctk.contract_number,
           tctk.phanbo,
           tctk.DmSanPhamREF,
           tctk.username,
           tctk.DmViTriREF,
           tctk.TenViTri,
           tctk.ThucchaySanPham,
           tcad.ThanhTienThucChay
    FROM
    (
        SELECT contract_number,
               phanbo,
               DmSanPhamREF,
               username,
               DmViTriREF,
               TenViTri,
               NgayThucHien,
               SUM(CONVERT(FLOAT, ISNULL (domain_tt_money,0))) AS ThucchaySanPham
        FROM dbo.ThucChayAdmarket_PhanBo
        WHERE NgayThucHien
        BETWEEN @Startdate AND @Todate
        GROUP BY contract_number,
                 phanbo,
                 DmSanPhamREF,
                 DmViTriREF,
                 TenViTri,
                 NgayThucHien,
                 username
    ) tctk
        FULL OUTER JOIN
        (
            SELECT SoHopDong,
                   HopDongChiTietREF,
                   DmSanPhamREF,
                   DmViTriREF,
                   TenViTri,
                   NgayThucHien,
                   ThanhTien,
				   SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) AS ThanhTienThucChay
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE NgayThucHien
                  BETWEEN @Startdate AND @Todate
                  AND DmHinhThucQuangCao <> 42
            GROUP BY SoHopDong,
                     HopDongChiTietREF,
                     DmSanPhamREF,
                     DmViTriREF,
                     TenViTri,
                     NgayThucHien,
                     ThanhTien
        ) tcad
            ON tcad.DmSanPhamREF = tctk.DmSanPhamREF
               AND tcad.DmViTriREF = tctk.DmViTriREF
               AND tcad.NgayThucHien = tctk.NgayThucHien
               AND tcad.HopDongChiTietREF = tctk.phanbo
               AND tcad.SoHopDong = tctk.contract_number
--WHERE tctk.phanbo=731724
) K1
    FULL OUTER JOIN
    (
        SELECT tcdoOnline.contract_number,
               tcadon.SoLuongDotChayHD AS PhanBoOnline,
               tcdoOnline.username,
               tcadon.DmSanPhamREF,
               tcadon.DmViTriREF,
               tcadon.TenViTri,
               tcadon.NgayThucHien,
               tcadon.TTThucChayOnlinePB,
               tcdoOnline.TCLuuOnlinePB
        FROM
        (
            SELECT SoLuongDotChayHD,
                   DmSanPhamREF,
                   DmViTriREF,
                   TenViTri,
                   NgayThucHien,
				   SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) AS TTThucChayOnlinePB           
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE NgayThucHien
                  BETWEEN @Startdate AND @Todate
                  AND DmHinhThucQuangCao <> 42
            GROUP BY SoLuongDotChayHD,
                     DmSanPhamREF,
                     DmViTriREF,
                     TenViTri,
                     NgayThucHien
        ) tcadon
            FULL OUTER JOIN
            (
                SELECT contract_number,
                       HopDongChiTietREF,
                       username,
                       DmSanPhamREF,
                       DmViTriREF,
                       TenViTri,
                       NgayThucHien,
					   SUM(CONVERT(FLOAT, ISNULL (domain_money,0))) AS TCLuuOnlinePB
                       --dbo.FormatNumber(ISNULL(SUM(CONVERT(FLOAT, domain_money)) / 1, 0)) AS TCLuuOnlinePB
                FROM dbo.ThucChayAdmarket_HopDong_online
                WHERE 1=1
				AND trangthai=0
				  AND CONVERT(DATE, createdAt) BETWEEN @Startdate AND @Todate
                GROUP BY contract_number,
                         HopDongChiTietREF,
                         username,
                         DmSanPhamREF,
                         DmViTriREF,
                         TenViTri,
                         NgayThucHien
            ) tcdoOnline
                ON tcadon.SoLuongDotChayHD = tcdoOnline.HopDongChiTietREF
                   AND tcadon.DmSanPhamREF = tcdoOnline.DmSanPhamREF
                   AND tcadon.DmViTriREF = tcdoOnline.DmViTriREF
                   AND tcadon.NgayThucHien = tcdoOnline.NgayThucHien
                   AND tcadon.TenViTri = tcdoOnline.TenViTri
    ) K2
        ON K2.contract_number = K1.contract_number
           AND K1.phanbo = K2.PhanBoOnline
           AND K1.DmSanPhamREF = K2.DmSanPhamREF
           AND K1.DmViTriREF = K2.DmViTriREF
           AND K1.TenViTri = K2.TenViTri
           AND K1.NgayThucHien = K2.NgayThucHien
		   WHERE K1.contract_number IS NOT NULL AND K1.contract_number<> N'BLANK' AND K1.contract_number<> N''
		  --AND (((K2.TTThucChayOnlinePB-K2.TCLuuOnlinePB)<>0) OR( K1.ThucchaySanPham-(K1.ThanhTienThucChay+K2.TTThucChayOnlinePB)<>0))

GROUP BY 
K1.NgayThucHien,
K1.contract_number,
K1.phanbo,
K1.username,
K1.DmSanPhamREF,
K1.DmViTriREF,
K1.TenViTri,
K1.ThucchaySanPham,
K1.ThanhTienThucChay,
K2.TTThucChayOnlinePB,
K2.TCLuuOnlinePB
HAVING ((TTThucChayOnlinePB-TCLuuOnlinePB)<>0)
OR( K1.ThucchaySanPham-(K1.ThanhTienThucChay+K2.TTThucChayOnlinePB)<>0)
END

```
