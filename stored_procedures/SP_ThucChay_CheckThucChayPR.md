# Stored Procedure: `ThucChay_CheckThucChayPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-07 19:57:33.007000
- **Ngày sửa cuối**: 2014-11-19 12:24:54.337000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	Compare data between ThucChayDaTinh and ThucChayHopDongChiTietAndPR
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayPR]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	SELECT a.SoHopDong,
	       a.HopDongChiTietREF,
	       a.ThoiGianBatDau,
	       a.TenWebsite,
	       a.SoLuongChay,
	       a.GiaTien,
	       a.ThanhTienTruocCK,
	       b.SoHopDong,
	       b.HopDongChiTietREF,
	       b.NgayThucHien,
	       ISNULL(b.SoLuongThucChay, 0) slchay,
	       ISNULL(b.SoLuongThucChayKM, 0) slkm,
	       ISNULL(b.DonGia, 0)DonGia,
	       b.ThanhTienTruocCK,
	       (a.SoLuongChay - ISNULL(b.SoLuongThucChay,0) - ISNULL(b.SoLuongThucChayKM, 0)) AS SoLuongChenhLech,
	       (a.GiaTien - ISNULL(b.DonGia, 0)) AS GiaTienChenhLech,
	       (a.ThanhTienTruocCK - b.ThanhTienTruocCK) AS ThanhTienChenhLech
	       --SUM(a.SoLuongChay), SUM(b.SoLuongThucChay)
	       , A.CreatedAt
	FROM   (
	           SELECT (
	                      SELECT hd.SoHopDong
	                      FROM   HopDong hd
	                      WHERE  hd.HopDongID = tchdctp.HopDongREF
	                  )SoHopDong,
	                  --tchdctp.HopDongREF,
	                  tchdctp.HopDongChiTietREF,
	                  tchdctp.ThoiGianBatDau,
	                  tchdctp.TenWebsite,
	                  COUNT(tchdctp.HopDongChiTietREF) SoLuongChay,
	                  tchdctp.GiaTien, 
	                  (tchdctp.GiaTien * COUNT(tchdctp.HopDongChiTietREF)) ThanhTienTruocCK
	                  , tchdctp.CreatedAt
	           FROM   ThucChayHopDongChiTietPR tchdctp
	           WHERE  CONVERT(date, tchdctp.ThoiGianBatDau) BETWEEN @StartDate AND @EndDate
	                  --AND tchdctp.HopDongREF =  ( SELECT hd.HopDongID
	                  --                                FROM HopDong hd WHERE hd.SoHopDong =  'DT870513')
	           GROUP BY
	                  tchdctp.HopDongREF,
	                  tchdctp.ThoiGianBatDau,
	                  tchdctp.HopDongChiTietREF,
	                  tchdctp.GiaTien
	                  , tchdctp.TenWebsite
	                 , tchdctp.CreatedAt
	       ) a
	       FULL OUTER JOIN (
	                SELECT tcdt.SoHopDong,
	                       tcdt.HopDongChiTietREF,
	                       --tcdt.SoLuong, 
	                       tcdt.NgayThucHien,
	                       SUM(tcdt.SoLuongThucChay)SoLuongThucChay,
	                       SUM(tcdt.SoLuongThucChayKM)SoLuongThucChayKM, 
	                       tcdt.DonGia,
	                       SUM(tcdt.ThanhTienThucChayTruocTrietKhau) AS ThanhTienTruocCK,
	                       tcdt.DmSanPhamREF
	                FROM   ThucChayDaTinh tcdt
	                WHERE  tcdt.DmSanPhamREF IN (141, 245, 250)
	                       AND CONVERT(date, tcdt.NgayThucHien) BETWEEN @StartDate 
	                           AND @EndDate
	                GROUP BY
	                       tcdt.SoHopDong,
	                       tcdt.NgayThucHien,
	                       tcdt.HopDongChiTietREF,
	                       tcdt.DonGia,
	                       tcdt.DmSanPhamREF
	                       --tcdt.SoLuong
	                       --ORDER BY tcdt.SoHopDong
	                       --, tcdt.HopDongChiTietREF
	                       --,tcdt.NgayThucHien
	            ) B
	            ON  a.SoHopDong = b.SoHopDong
	            AND a.HopDongChiTietREF = b.HopDongChiTietREF
	            AND B.NgayThucHien = a.ThoiGianBatDau
	WHERE (a.ThanhTienTruocCK - b.ThanhTienTruocCK) <> 0
	OR (a.SoLuongChay - ISNULL(b.SoLuongThucChay,0) - ISNULL(b.SoLuongThucChayKM, 0)) <> 0
	ORDER BY
	       a.ThoiGianBatDau,
	       a.SoHopDong,
	       a.HopDongChiTietREF
END


```
