# Stored Procedure: `RaSoat_DL_PerformanceBase_DoTudong_TangPB  `

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-07-24 17:05:18.767000
- **Ngày sửa cuối**: 2024-07-24 17:05:18.767000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Linhvtt>
-- Create date: <24/07/2024>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[RaSoat_DL_PerformanceBase_DoTudong_TangPB  ]
	-- Add the parameters for the stored procedure here
    @NgayThucHien DATE = NULL
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT A.NgayThucHien,
       A.SoHopDong,
       A.HopDongFK,
       A.HopDongChiTietREF,
       A.DmSanPhamREF,
      A.ThanhTien ,
       A.ThanhTienTC,
       TCOnlineDoTuDong ,
       B.TTThucChayDaghinhan,
       B.TotalTCchuaghinhan
FROM
(
    SELECT K1.NgayThucHien,
           K1.SoHopDong,
           K1.HopDongFK,
           K1.HopDongChiTietREF,
           K1.DmSanPhamREF,
           K1.ThanhTien,
           K1.ThanhTienTC,
           K2.TCOnlineDoTuDong
    FROM
    (
        SELECT hdcttd.NgayThucHien,
               tcdtak.SoHopDong,
               hdcttd.HopDongFK,
               hdcttd.HopDongChiTietREF,
               tcdtak.DmSanPhamREF,
               tcdtak.ThanhTien,
               (CONVERT(FLOAT, ISNULL(tcdtak.ThanhTienTC, 0))) ThanhTienTC
        FROM
        (
            SELECT HopDongFK,
                   HopDongChiTietREF,
                   DmSanPhamREF,
                   CONVERT(DATE, LastModifiedAt) AS NgayThucHien
            FROM dbo.HopDongChiTietThayDoi
            WHERE CONVERT(DATE, LastModifiedAt) = @NgayThucHien
                  AND DmSanPhamREF IN ( 144, 628, 585 )
            GROUP BY HopDongFK,
                     HopDongChiTietREF,
                     DmSanPhamREF,
                     CONVERT(DATE, LastModifiedAt)
        ) hdcttd
            INNER JOIN
            (
                SELECT SoHopDong,
                       HopDongChiTietREF,
                       DmSanPhamREF,
                       NgayThucHien,
                       ThanhTien,
                       SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhTienTC
                FROM dbo.ThucChayDaTinhAdmarket
                WHERE DmHinhThucQuangCao <> 42
                      AND DmSanPhamREF IN ( 144, 628, 585 )
                      AND NgayThucHien = @NgayThucHien
                GROUP BY SoHopDong,
                         HopDongChiTietREF,
                         DmSanPhamREF,
                         ThanhTien,
                         NgayThucHien
            ) tcdtak
                ON tcdtak.NgayThucHien = hdcttd.NgayThucHien
                   AND tcdtak.HopDongChiTietREF = hdcttd.HopDongChiTietREF
                   AND hdcttd.DmSanPhamREF = tcdtak.DmSanPhamREF
    ) K1
        INNER JOIN
        (
            SELECT contract_number,
                   HopDongChiTietREF,
                   DmSanPhamREF,
                   NgayThucHien,
                   SUM(CONVERT(FLOAT, ISNULL(domain_money, 0))) AS TCOnlineDoTuDong
            FROM dbo.ThucChayAdmarket_HopDong_online
            WHERE 1 = 1
                  AND trangthai = 1
                  AND NgayThucHien = @NgayThucHien
            GROUP BY contract_number,
                     HopDongChiTietREF,
                     DmSanPhamREF,
                     NgayThucHien
        ) K2
            ON K2.DmSanPhamREF = K1.DmSanPhamREF
               AND K2.HopDongChiTietREF = K1.HopDongChiTietREF
               AND K2.NgayThucHien = K1.NgayThucHien
) A
    INNER JOIN
    (
        SELECT tcdctotal.SoHopDong,
               tcdctotal.DmSanPhamREF,
               tcdctotal.TTThucChayDaghinhan,
               tccgn.TotalTCchuaghinhan
        FROM
        (
            SELECT SoHopDong,
                   HopDongChiTietREF,
                   DmSanPhamREF,
                   SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS TTThucChayDaghinhan
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE 1 = 1
                  AND NgayThucHien < @NgayThucHien
                  AND DmHinhThucQuangCao <> 42
            GROUP BY SoHopDong,
                     HopDongChiTietREF,
                     DmSanPhamREF
        ) tcdctotal
            INNER JOIN
            (
                SELECT contract_number,
                       HopDongChiTietREF,
                       DmSanPhamREF,
                       SUM(CONVERT(FLOAT, ISNULL(domain_money, 0))) AS TotalTCchuaghinhan
                FROM dbo.ThucChayAdmarket_HopDong_online
                WHERE 1 = 1
                      AND trangthai = 0
                      AND @NgayThucHien <= @NgayThucHien
                GROUP BY contract_number,
                         HopDongChiTietREF,
                         DmSanPhamREF
            ) tccgn
                ON tccgn.DmSanPhamREF = tcdctotal.DmSanPhamREF
                   AND tccgn.HopDongChiTietREF = tcdctotal.HopDongChiTietREF
    ) B
        ON B.DmSanPhamREF = A.DmSanPhamREF
           AND B.SoHopDong = A.SoHopDong
GROUP BY A.NgayThucHien,
       A.SoHopDong,
       A.HopDongFK,
       A.HopDongChiTietREF,
       A.DmSanPhamREF,
      A.ThanhTien ,
       A.ThanhTienTC,
       TCOnlineDoTuDong ,
       B.TTThucChayDaghinhan,
       B.TotalTCchuaghinhan
HAVING (A.ThanhTien-(B.TTThucChayDaghinhan+A.ThanhTienTC) >0 AND B.TotalTCchuaghinhan>0) 
      OR (A.TCOnlineDoTuDong-A.ThanhTienTC<>0 )
END

```
