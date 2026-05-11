# Stored Procedure: `KiemTraThucChayDaTinhCPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-14 17:06:00.970000
- **Ngày sửa cuối**: 2017-04-06 21:59:21.963000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPHamREf` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@typeproduct` | `int(4)` | No |
| `@NgayThucHien1` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =====================[KiemTraThucChayDaTinhCPM]========================
--exec [KiemTraThucChayDaTinhCPM] 'QC0410217',598,'2013-04-04',14,'2017-04-04'
CREATE PROCEDURE [dbo].[KiemTraThucChayDaTinhCPM]
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(50), @DmSanPHamREf INT, @NgayThucHien DATETIME, @typeproduct INT,@NgayThucHien1 DATETIME
AS
BEGIN

SELECT  hd.TrangThaiHopDong, hd.hopdongID,hd.sohopdong,hdct.DmSanPhamREF,hdct.TenSanPham,hdct.TenLoai,hdct.HopDongChiTietID, hdct.DmLoaiREF, hdct.DmLoaiBannerREF,
NhanHang,DanhSachNhanHangREF,hdct.TenBanner, TenLoai, TenLoaiBanner
,hdct.SoLuong, hdct.DonViTinh, hdct.DonViTinhREF,hdct.DonGia,hdct.ChietKhau,hdct.ThanhTien,hdct.TK_AdMarket, hdct.ThanhTienThucChay, hdct.LastModifiedAt
  FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
WHERE hd.SoHopDong = @SoHopDong
AND (hdct.DmSanPhamREF = @DmSanPHamREF)
AND hdct.DeletedStatus <> 1
AND NOT (hdct.DmLoaiREF IN (13,42) OR hdct.DmLoaiBannerREF = 18)
ORDER BY hdct.HopDongChiTietID

-------------ThucchayDaTinh NhanHang--------------------
SELECT  tcdt.HopDongChiTietREF,tcdt.DonViTinh, NhanHang, DmSanPhamREF, tcdt.TenSanPham, tcdt.DmHinhThucQuangCao, tcdt.DmLoaiBannerREF
	,MIN(tcdt.NgayThucHien) minngaythuchien,--tcdt.TenWebsite,
	SUM(tcdt.SoLuongThucChay+SoLuongThayDoi)sltc
	, SUM(tcdt.SoLuongThucChayKM+SoLuongKMThayDoi) sltckm
	, SUM(tcdt.SoLuongThucChayLechTreoHa) AS SLLechTreoHa
	, sum(tcdt.TongViewThucChay)tvtc
	, (SUM(tcdt.SoLuongThucChay) + SUM(tcdt.SoLuongThucChayKM) + SUM(tcdt.SoLuongThucChayLechTreoHa)) tongVIew 
	, round(sum(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) TTienTC
	,SUM(tcdt.ThanhTienLechTreoHa) ttlechth
	,SUM(tcdt.GiaTriThayDoi) GiaTriThayDoi, SUM(tcdt.ThanhTienKM+tcdt.GiaTriKMThayDoi)km
	,MAX(tcdt.NgayThucHien) maxngay--, GhiChu
	--, NgayThucHien
FROM ThucChayDaTinh tcdt
WHERE tcdt.SoHopDong = @SoHopDong
AND tcdt.DmSanPhamREF = @DmSanPHamREf
AND CONVERT(DATE,tcdt.NgayThucHien) BETWEEN @NgayThucHien AND @NgayThucHien1
AND tcdt.TrangThaiHopDong <> 3
AND NOT (tcdt.DmHinhThucQuangCao IN (13,42) OR tcdt.DmLoaiBannerREF = 18)
GROUP BY  tcdt.HopDongChiTietREF,tcdt.DonViTinh, NhanHang, DmSanPhamREF, tcdt.DmHinhThucQuangCao, tcdt.DmLoaiBannerREF, tcdt.TenSanPham
--,NgayThucHien
--HAVING ROUND(sum(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) <> 0
ORDER BY tcdt.HopDongChiTietREF--,NgayThucHien

-------------ThucchayDaTinhMobile --------------------
SELECT 'tcdtmobile'tcdtmobile, tcdt.HopDongChiTietREF,tcdt.DonViTinh, NhanHang, DmSanPhamREF, tcdt.TenSanPham, tcdt.DmHinhThucQuangCao, tcdt.DmLoaiBannerREF
	,MIN(tcdt.NgayThucHien) minngaythuchien, 
	SUM(tcdt.SoLuongThucChay+SoLuongThayDoi)sltc
	, SUM(tcdt.SoLuongThucChayKM+SoLuongKMThayDoi) sltckm
	, SUM(tcdt.SoLuongThucChayLechTreoHa) AS SLLechTreoHa
	, sum(tcdt.TongViewThucChay)tvtc
	, (SUM(tcdt.SoLuongThucChay) + SUM(tcdt.SoLuongThucChayKM) + SUM(tcdt.SoLuongThucChayLechTreoHa)) tongVIew 
	, round(sum(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) TTienTC
	,SUM(tcdt.ThanhTienLechTreoHa) ttlechth
	,SUM(tcdt.GiaTriThayDoi) GiaTriThayDoi, SUM(tcdt.ThanhTienKM+tcdt.GiaTriKMThayDoi)km
	,MAX(tcdt.NgayThucHien) maxngay--, GhiChu
	--, NgayThucHien
FROM ThucChayDaTinhMobile tcdt
WHERE tcdt.SoHopDong = @SoHopDong
AND tcdt.DmSanPhamREF = @DmSanPHamREf
AND CONVERT(DATE,tcdt.NgayThucHien) BETWEEN @NgayThucHien AND @NgayThucHien1
AND tcdt.TrangThaiHopDong <> 3
AND NOT (tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18)
GROUP BY  tcdt.HopDongChiTietREF,tcdt.DonViTinh, NhanHang, DmSanPhamREF, tcdt.DmHinhThucQuangCao, tcdt.DmLoaiBannerREF, tcdt.TenSanPham
--,NgayThucHien
--HAVING ROUND(sum(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) <> 0
ORDER BY tcdt.HopDongChiTietREF--,NgayThucHien
------ThucChay ----------
SELECT  tc.DmBannerREF, tc.TypeProduct,--tc.TenWebsite,
SUM(tc.TongViewThucChay) TongViewThucChay, SUM(tc.TongClickThucChay) TongClickThucChay,
 MIN(tc.NgayThucHien) minngay,
MAX(tc.NgayThucHien) maxngay--, NgayThucHien
FROM ThucChay tc
WHERE tc.SoHopDong = @SoHopDong
AND tc.TypeProduct = @typeproduct
--AND tc.DmBannerREF = 395647
AND tc.NgayThucHien BETWEEN @NgayThucHien AND @NgayThucHien1
GROUP BY tc.DmBannerREF, tc.TypeProduct--, tc.NgayThucHien
ORDER BY tc.DmBannerREF--,NgayThucHien
-------------------------------------Thuc chay ngay ----------------------------------------
SELECT  tc.DmBannerREF, tc.TypeProduct, SUM(tc.TongViewThucChay) TongViewThucChay, SUM(tc.TongClickThucChay) TongClickThucChay,
 MIN(tc.NgayThucHien) minngay,
MAX(tc.NgayThucHien) maxngay--, NgayThucHien
FROM ThucChay tc
WHERE tc.SoHopDong = @SoHopDong
AND tc.TypeProduct = @typeproduct
AND tc.NgayThucHien = @NgayThucHien1
GROUP BY tc.DmBannerREF,tc.TypeProduct
ORDER BY tc.DmBannerREF--,NgayThucHien
-------------------------------------Thuc treo ----------------------------------------
SELECT DISTINCT 'TT'[Thuctreo],  tchdctab.DmBannerID, tchdctab.HopDongChiTietREF, tchdctab.TiLeThucChayHDCTSoVoiBanner
, tchdctab.DaThucHienUpdateTiLe,tchdctab.DsNhanHangREF, tchdctab.DsNhanHangREF
  FROM ThucChayHopDongChiTietAndBanner tchdctab
  INNER JOIN HopDong hd ON hd.HopDongID = tchdctab.HopDongREF
  INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
WHERE hd.SoHopDong = @SoHopDong
AND hdct.DmSanPhamREF = @DmSanPHamREf
AND tchdctab.DeletedStatus = 0
ORDER BY tchdctab.DmBannerID

---------------Thuc treo-----------------------------
SELECT tchdct.ThucChayHopDongChiTietID, tchdct.DeletedStatus, tchdct.HopDongChiTietREF, tchdct.DmBannerREF , hdct.DanhSachNhanHangREF,  tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc,
tchdct.ThucChayHopDongChiTietID IDTT, DmNhanHangREF DmNhanHangtt, tchdct.NhanHang NhanHangtt, tchdct.DmBannerREF, tchdct.CreatedAt,tchdct.LastModifiedAt, tchdct.CreatedBy, tchdct.LastModifiedBy
FROM ThucChayHopDongChiTiet tchdct
INNER JOIN  HopDong hd ON hd.HopDongID = tchdct.HopDongREF
INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
WHERE hd.SoHopDong = @SoHopDong AND hdct.dmsanphamref = @DmSanPHamREf
AND tchdct.deletedstatus <> 1
---

END

```
