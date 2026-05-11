# Stored Procedure: `sp_KSTC_CheckTCDT_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-04-13 14:26:10.283000
- **Ngày sửa cuối**: 2024-01-11 14:45:47.037000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC sp_KSTC_CheckTCDT_PR '2023-01-01', '2023-12-03'
CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_PR]
    -- Add the parameters for the stored procedure here
    @FromDate DATETIME,
    @ToDate DATETIME
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Insert statements for procedure here
    SELECT DISTINCT
           kt.*
    FROM
    (
        SELECT A.*,
               B.*
        FROM
        (
            SELECT tchdctp.DmNhanHangREF,
                   dbo.GetSoHopDongByID(tchdctp.HopDongREF) SoHopDong,
                   HopDongREF,
                   tchdctp.DmSanPhamREF,
                   tchdctp.HopDongChiTietREF,
                   CONVERT(NVARCHAR(50), ThucChayHopDongChiTietPRID) id,
                   tchdctp.DeletedStatus,
                   tchdctp.RecordStatus,
                   CONVERT(DATE, ThoiGianBatDau) ThoiGianBatDau,
                   tchdctp.CreatedAt,
                   tchdctp.LastModifiedAt,
                   tchdctp.TenWebsite,
                   tchdctp.TenChuyenMuc,
                   tchdctp.SoLuong,
                   tchdctp.GiaTien,
                   tchdctp.ChietKhau,
                   (CASE
                        WHEN tchdctp.DeletedStatus = 0 THEN
                   (CONVERT(FLOAT, tchdctp.GiaTien) * tchdctp.SoLuong * (100 - tchdctp.ChietKhau) / 100)
                        ELSE
                            0
                    END
                   ) TTSauCk,
                   tchdctp.Link,
                   tchdctp.ThucChayHopDongChiTietPrREF ttid_cha
            FROM dbo.ThucChayHopDongChiTietPR tchdctp
                LEFT JOIN DmSanPham sp
                    ON tchdctp.DmSanPhamREF = sp.DmSanPhamID
            WHERE 1 = 1
                  AND CONVERT(DATE, ThoiGianBatDau) >= '2018-01-01'
                  --or 
                  AND ISNULL(CONVERT(DATE, tchdctp.LastModifiedAt), tchdctp.CreatedAt) --between'2020-03-29' and '2020-04-24'
                  BETWEEN @FromDate AND @ToDate
        --AND hopdongref =1013046
        --AND tchdctp.ThucChayHopDongChiTietPrID =135313

        ) A
            LEFT JOIN
            (
                SELECT HopDongID,
                       DmSanPhamREF DmSanPhamREF_tcdt,
                       NhanHang,
                       DotChayBooking,
                       SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) tc
                FROM dbo.ThucChayDaTinh
                WHERE DmSanPhamREF IN ( 141, 637, 305 )
                      AND NOT (
                                  DmLoaiBannerREF = 18
                                  OR DmHinhThucQuangCao = 13
                              )
                --AND HopDongID =1013046 AND DotChayBooking ='135313'
                GROUP BY HopDongID,
                         DmSanPhamREF,
                         DotChayBooking,
                         NhanHang
                HAVING ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) <> 0
            ) B
                ON A.HopDongREF = B.HopDongID
                   AND A.DmSanPhamREF = B.DmSanPhamREF_tcdt
                   AND CONVERT(NVARCHAR(100), A.id) = B.DotChayBooking
        WHERE 1 = 1
              AND
              (
                  (ROUND(ABS(ISNULL(A.TTSauCk, 0)), 0) - ROUND(ISNULL(B.tc, 0), 0) <> 0 --OR B.HopDongID IS NULL
                  )
                  OR CONVERT(NVARCHAR(50), A.DmNhanHangREF) <> CONVERT(NVARCHAR(50), B.NhanHang)
              )
        UNION ALL
        SELECT A.*,
               B.*
        FROM
        (
            SELECT tchdctp.DmNhanHangREF,
                   --dbo.GetSoHopDongByID(tchdctp.HopDongREF) SoHopDong,
                   hd.SoHopDong,
                   HopDongREF,
                   DmSanPhamREF,
                   tchdctp.HopDongChiTietREF,
                   CONVERT(NVARCHAR(50), ThucChayHopDongChiTietPRID) id,
                   tchdctp.DeletedStatus,
                   tchdctp.RecordStatus,
                   CONVERT(DATE, ThoiGianBatDau) ThoiGianBatDau,
                   tchdctp.CreatedAt,
                   tchdctp.LastModifiedAt,
                   tchdctp.TenWebsite,
                   tchdctp.TenChuyenMuc,
                   tchdctp.SoLuong,
                   tchdctp.GiaTien,
                   tchdctp.ChietKhau,
                   (CASE
                        WHEN tchdctp.DeletedStatus = 0 THEN
                   (CONVERT(FLOAT, tchdctp.GiaTien) * tchdctp.SoLuong * (100 - tchdctp.ChietKhau) / 100)
                        ELSE
                            0
                    END
                   ) TTSauCk,
                   tchdctp.Link,
                   tchdctp.ThucChayHopDongChiTietPrREF ttid_cha
            FROM dbo.ThucChayHopDongChiTietPR tchdctp
                INNER JOIN
                (
                    SELECT HopDongID,
                           SoHopDong,
                           LastModifiedAt
                    FROM dbo.HopDong
                    WHERE Nam >= 2021
                          AND CONVERT(DATE, LastModifiedAt)
                          BETWEEN @FromDate AND @ToDate
                ) hd
                    ON tchdctp.HopDongREF = hd.HopDongID
                LEFT JOIN DmSanPham sp
                    ON tchdctp.DmSanPhamREF = sp.DmSanPhamID
            --LEFT JOIN HopDong hd
            --    ON HopDongID = HopDongREF
            WHERE 1 = 1

                  --AND CONVERT(DATE,ThoiGianBatDau)  >= '2018-01-01'
                  --or 

                  AND CONVERT(DATE, tchdctp.LastModifiedAt) < CONVERT(DATE, GETDATE())
        --AND hopdongref =1013046
        --AND tchdctp.ThucChayHopDongChiTietPrID =135313

        ) A
            LEFT JOIN
            (
                SELECT HopDongID,
                       DmSanPhamREF DmSanPhamREF_tcdt,
                       NhanHang,
                       DotChayBooking,
                       SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) tc
                FROM dbo.ThucChayDaTinh
                WHERE DmSanPhamREF IN ( 141, 637, 305 )
                      AND NOT (
                                  DmLoaiBannerREF = 18
                                  OR DmHinhThucQuangCao = 13
                              )
                --AND HopDongID =1013046 AND DotChayBooking ='135313'
                GROUP BY HopDongID,
                         DmSanPhamREF,
                         DotChayBooking,
                         NhanHang
                HAVING ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) <> 0
            ) B
                ON A.HopDongREF = B.HopDongID
                   AND A.DmSanPhamREF = B.DmSanPhamREF_tcdt
                   AND CONVERT(NVARCHAR(100), A.id) = B.DotChayBooking
        WHERE 1 = 1
              AND
              (
                  (ABS(ISNULL(A.TTSauCk, 0) - ISNULL(B.tc, 0)) > 10 --OR B.HopDongID IS NULL
                  )
                  OR CONVERT(NVARCHAR(50), A.DmNhanHangREF) <> CONVERT(NVARCHAR(50), B.NhanHang)
              )
    ) kt
    --INNER JOIN (
    --             SELECT SoHopDong FROM dbo.HopDong WHERE Nam >= 2021
    --         ) hd ON kt.SoHopDong = hd.SoHopDong
    WHERE kt.SoHopDong IN
          (
              SELECT SoHopDong FROM dbo.HopDong WHERE Nam >= 2022
          )
    ORDER BY kt.HopDongChiTietREF DESC;
END;

```
