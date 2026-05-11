# Stored Procedure: `CheckThucChayVuotHopDongAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-01 11:45:49.313000
- **Ngày sửa cuối**: 2016-11-18 18:36:08.540000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiCheck` | `int(4)` | No |
| `@DmSanPhamREF` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--SELECT TenDangNhap FROM hopdong WHERE TenDangNhap ='hieungovan'
--[CheckThucChayVuotHopDongAll] '2016-11-17',13,''
--exec [CheckThucChayVuotHopDongAll] '2016-05-11',7,''
--exec [CheckThucChayVuotHopDongAll] '2016-02-28',8,''
--exec [CheckThucChayVuotHopDongAll] '2016-02-28',9,''
--DongBoDuLieu '2016-02-22','2016-02-22'
--1: check vuot theo hop dong QC790213,QC1170913,DT311013


/*
*/
CREATE PROCEDURE [dbo].[CheckThucChayVuotHopDongAll] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@LoaiCheck INT, 
	--7: check sai, vuot theo tat ca thong tin hd sp cpd
	--8: check sai, vuot theo tat ca thong tin hd sp tru cpd: cpm, google, chi phí, mua ngoài
	--9: check sai, vuot theo tat ca thong tin hd sp admarket
	@DmSanPhamREF NVARCHAR(MAX) 	
AS
BEGIN
	
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
--7. HopDong, Nhan Hang, sanpham, khach hang, nhan vien -- Sản phẩm cpd, cpd chuyen trang, box cpd, box gia vang
	IF @LoaiCheck = 7
BEGIN
	SELECT a.*, b.*, (ISNULL(a.tthd,0) - ISNULL(b.thanhtientc,0)) lechhdtc FROM ( 
	 SELECT hd.HopDongID, hd.SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietID,
	 DmPhongBanREF, /*TenPhongBan,*/ DmBoPhanREF,/* TenBoPhan,*/ DmNhomREF DmNhomLamViecREF, TenNhom TenNhomLamViec, --TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang,DmLoaiREF HTQC, TenLoai TenHTQC,
	hdct.DmSanPhamREF, hdct.TenSanPham, dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(DmWebsiteREF)DmWebsiteREF,
	dbo.GetWebsiteLinkByDmWebsiteID(DmWebsiteREF,TenWebsite) TenWebsite
	 ,SUM(Thanhtien)tthd
	 FROM HopDong hd INNER JOIN HopDongChiTiet hdct 
	 ON hd.HopDongID = hdct.HopDongFK
	 WHERE 1=1-- hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
	AND hd.DeletedStatus <> 1
	 AND hdct.DeletedStatus <> 1
	 AND hd.TrangThaiHopDong <> 3
	 AND DmSanPhamREF NOT IN (144,585,628)
	 AND DmSanPhamREF IN (140,549,228,385)
	 AND HopDongID IN (SELECT HopDongFK FROM dbo.HopDongChiTietLog WHERE LastModifiedAt >'2015-11-07' UNION ALL SELECT HopDongID FROM dbo.HopDongLog WHERE LastModifiedAt >'2015-11-07')
	 --AND DmSanPhamREF IN (549)
	 --AND HopDongChiTietID = 90614
	 --AND SoHopDong =   'QC2700116'--@SoHopDong
	 GROUP BY hd.HopDongID, hd.SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietID,
	 DmPhongBanREF, /*TenPhongBan,*/ DmBoPhanREF,/* TenBoPhan*/ DmNhomREF, TenNhom, --TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, DmLoaiREF, TenLoai,
	hdct.DmSanPhamREF, hdct.TenSanPham,  DmWebsiteREF,  TenWebsite
	 )a
	 RIGHT JOIN
	 (	 	
	 SELECT --B.shdb, 
	 B.HopDongID, B.SoHopDong, B.DmMaHopDongREF, B.TenMaHopDong, B.NgayDanhSoHopDong, B.HopDongChiTietREF,
	B.DmPhongBanREF, /*B.TenPhongBan*/ B.DmBoPhanREF, /*B.TenBoPhan,*/ B.DmNhomLamViecREF,  B.TenNhomLamViec, --B.TenDiaDiemLamViec,
	 	 B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien, TenKhachHang, B.HTQC, B.TenHTQC,
	B.DmSanPhamREF, B.TenSanPham, B.DmWebsiteREF, B.TenWebsite,sum(B.thanhtientc)thanhtientc
	   FROM
	 (
	 SELECT HopDongID, SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietREF,
	 DmPhongBanREF, /*TenPhongBan, */
	 DmBoPhanREF, /*TenBoPhan, */DmNhomLamViecREF, TenNhomLamViec, --TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, DmHinhThucQuangCao HTQC, TenHinhThucQuangCao TenHTQC,
	DmSanPhamREF, TenSanPham, DmWebsiteREF, TenWebsite,
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinh tcdt
	 WHERE 1=1 AND tcdt.NgayThucHien <= @NgayThucHien AND 
	 tcdt.DmSanPhamREF NOT IN (144,585,628)
	 AND DmSanPhamREF IN (140,549,228,385)
	AND  tcdt.TrangThaiHopDong <> 3
	AND TenMaHopDong NOT IN ('NB','SH')
	 AND HopDongID IN (SELECT HopDongFK FROM dbo.HopDongChiTietLog WHERE LastModifiedAt >'2015-11-07' UNION ALL SELECT HopDongID FROM dbo.HopDongLog WHERE LastModifiedAt >'2015-11-07')
	-- AND SoHopDong =   'QC2700116'--@SoHopDong
	 -- AND HopDongChiTietREF = 90614
	 GROUP BY  HopDongID, SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietREF,
	 DmPhongBanREF, --TenPhongBan, 
	 DmBoPhanREF, --TenBoPhan,
	  DmNhomLamViecREF, TenNhomLamViec, --TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang,  DmHinhThucQuangCao, TenHinhThucQuangCao,
	DmSanPhamREF, TenSanPham, DmWebsiteREF, TenWebsite	 
	 )B 	
	 GROUP BY
	  B.HopDongID, B.SoHopDong, B.DmMaHopDongREF, B.TenMaHopDong, B.NgayDanhSoHopDong, B.HopDongChiTietREF,
	B.DmPhongBanREF,-- B.TenPhongBan,
	 B.DmBoPhanREF,-- B.TenBoPhan,
	 B.DmNhomLamViecREF,  B.TenNhomLamViec,-- B.TenDiaDiemLamViec,
	 	 B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien, TenKhachHang, B.HTQC, B.TenHTQC,
	B.DmSanPhamREF, B.TenSanPham, B.DmWebsiteREF, B.TenWebsite
	 )b
	 ON (1=1 	 
	 AND a.HopDongID =  b.HopDongID
	 AND a.SoHopDong = b.SoHopDong
	 AND a.DmMaHopDongREF = b.DmMaHopDongREF
	 AND a.TenMaHopDong = b.TenMaHopDong
	 AND a.NgayDanhSoHopDong = b.NgayDanhSoHopDong
	 AND a.HopDongChiTietID = b.HopDongChiTietREF
	 and a.DmPhongBanREF = b.DmPhongBanREF
	-- AND a.TenPhongBan = b.TenPhongBan
	 AND a.DmBoPhanREF = b.DmBoPhanREF
	 --AND b.TenBoPhan = b.TenBoPhan
	 AND a.DmNhomLamViecREF = b.DmNhomLamViecREF
	 AND a.TenNhomLamViec = b.TenNhomLamViec
	 --AND a.TenDiaDiemLamViec = b.TenDiaDiemLamViec
	 AND a.SysNhanVienREF = b.SysNhanVienREF
	 AND a.TenDangNhap = b.TenDangNhap
	 AND a.TenNhanVien = b.TenNhanVien 
	 AND a.TenKhachHang = b.TenKhachHang
	 --AND a.NhanHang = b.NhanHang
	 AND a.HTQC = b.HTQC
	 AND a.TenHTQC = b.TenHTQC
	 AND a.DmSanPhamREF = b.DmSanPhamREF
	 AND a.TenSanPham = b.TenSanPham
	 AND a.DmWebsiteREF = b.DmWebsiteREF
	 AND a.TenWebsite = b.TenWebsite
	 )	 
	 --WHERE (round(a.tthd - b.thanhtientc,0) <-2 OR (b.thanhtientc <0)OR a.tthd IS null) --AND NOT (a.tthd IS NULL AND b.thanhtientc = 0)
	  WHERE ((b.thanhtientc <0)OR a.tthd IS null) AND NOT (a.tthd IS NULL AND b.thanhtientc = 0)
	  --AND a.DmSanPhamREF IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@DmSanPhamREF, ',')) att)
	--ORDER BY  B.HopDongID, B.SoHopDong, B.DmMaHopDongREF, B.TenMaHopDong, B.NgayDanhSoHopDong, B.NhanHopDong, B.HopDongChiTietREF,
	--B.DmPhongBanREF, B.TenPhongBan, B.DmBoPhanREF, B.TenBoPhan, B.DmNhomLamViecREF,  B.TenNhomLamViec, B.TenDiaDiemLamViec,
	-- 	 B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien, TenKhachHang, B.NhanHang, B.DmNhomNganhREF,TenNhomNganh, B.DmHinhThucQuangCao, B.TenHinhThucQuangCao,
	--B.DmSanPhamREF, B.TenSanPham, B.DmWebsiteREF, B.TenWebsite
	END
	
	--8. HopDong, Nhan Hang, sanpham, khach hang, nhan vien -- tru sp cpd,cpm
	ELSE IF @LoaiCheck =8
BEGIN
	SELECT a.*, b.*, (ISNULL(a.tthd,0) - ISNULL(b.thanhtientc,0)) lechhdtc FROM ( 
	 SELECT hd.HopDongID, hd.SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietID,
	 DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomREF DmNhomLamViecREF, TenNhom TenNhomLamViec, TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang, DmLoaiREF HTQC, TenLoai TenHTQC,
	hdct.DmSanPhamREF, hdct.TenSanPham
	 ,SUM(Thanhtien)tthd
	 FROM HopDong hd INNER JOIN HopDongChiTiet hdct 
	 ON hd.HopDongID = hdct.HopDongFK
	 WHERE 1=1-- hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
	AND hd.DeletedStatus <> 1
	 AND hdct.DeletedStatus <> 1
	 AND hd.TrangThaiHopDong <> 3
	 AND DmSanPhamREF NOT IN (144,585,628)
		 AND DmSanPhamREF NOT IN  (141,305,637,140,549,228,385)
	 AND HopDongID IN (SELECT HopDongFK FROM dbo.HopDongChiTietLog WHERE LastModifiedAt >'2015-11-07' UNION ALL SELECT HopDongID FROM dbo.HopDongLog WHERE LastModifiedAt >'2015-11-07')
	 --AND DmSanPhamREF IN (549)
	 --AND HopDongChiTietID = 90614
	 --AND SoHopDong =   'QC2700116'--@SoHopDong
	 GROUP BY hd.HopDongID, hd.SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietID,
	 DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomREF, TenNhom, TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang,DmLoaiREF, TenLoai,
	hdct.DmSanPhamREF, hdct.TenSanPham
	 )a
	 FULL OUTER JOIN
	 (	 	
	 SELECT --B.shdb, 
	 B.HopDongID, B.SoHopDong, B.DmMaHopDongREF, B.TenMaHopDong, B.NgayDanhSoHopDong, B.HopDongChiTietREF,
	B.DmPhongBanREF, B.TenPhongBan, B.DmBoPhanREF, B.TenBoPhan, B.DmNhomLamViecREF,  B.TenNhomLamViec, B.TenDiaDiemLamViec,
	 	 B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien, TenKhachHang, B.NhanHang,B.HTQC, B.TenHTQC,
	B.DmSanPhamREF, B.TenSanPham,sum(B.thanhtientc)thanhtientc
	   FROM
	 (
	 SELECT HopDongID, SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietREF,
	 DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomLamViecREF, TenNhomLamViec, TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang,  DmHinhThucQuangCao HTQC, TenHinhThucQuangCao TenHTQC,
	DmSanPhamREF, TenSanPham, 
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinh tcdt
	 WHERE 1=1 AND tcdt.NgayThucHien <= @NgayThucHien AND 
	 tcdt.DmSanPhamREF NOT IN (144,585,628)
		 AND DmSanPhamREF NOT IN  (141,305,637,140,549,228,385)
	AND  tcdt.TrangThaiHopDong <> 3
	 AND HopDongID IN (SELECT HopDongFK FROM dbo.HopDongChiTietLog WHERE LastModifiedAt >'2015-11-07' UNION ALL SELECT HopDongID FROM dbo.HopDongLog WHERE LastModifiedAt >'2015-11-07')
	-- AND SoHopDong =   'QC2700116'--@SoHopDong
	 -- AND HopDongChiTietREF = 90614
	 GROUP BY  HopDongID, SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietREF,
	 DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomLamViecREF, TenNhomLamViec, TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang,DmHinhThucQuangCao, TenHinhThucQuangCao,
	DmSanPhamREF, TenSanPham 
	 )B 	
	 GROUP BY
	  B.HopDongID, B.SoHopDong, B.DmMaHopDongREF, B.TenMaHopDong, B.NgayDanhSoHopDong, B.HopDongChiTietREF,
	B.DmPhongBanREF, B.TenPhongBan, B.DmBoPhanREF, B.TenBoPhan, B.DmNhomLamViecREF,  B.TenNhomLamViec, B.TenDiaDiemLamViec,
	 	 B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien, TenKhachHang, B.NhanHang, B.HTQC, B.TenHTQC,
	B.DmSanPhamREF, B.TenSanPham
	 )b
	 ON (1=1 	 
	 AND a.HopDongID =  b.HopDongID
	 AND a.SoHopDong = b.SoHopDong
	 AND a.DmMaHopDongREF = b.DmMaHopDongREF
	 AND a.TenMaHopDong = b.TenMaHopDong
	 AND a.NgayDanhSoHopDong = b.NgayDanhSoHopDong
	 AND a.HopDongChiTietID = b.HopDongChiTietREF
	 and a.DmPhongBanREF = b.DmPhongBanREF
	 AND a.TenPhongBan = b.TenPhongBan
	 AND a.DmBoPhanREF = b.DmBoPhanREF
	 AND b.TenBoPhan = b.TenBoPhan
	 AND a.DmNhomLamViecREF = b.DmNhomLamViecREF
	 AND a.TenNhomLamViec = b.TenNhomLamViec
	 AND a.TenDiaDiemLamViec = b.TenDiaDiemLamViec
	 AND a.SysNhanVienREF = b.SysNhanVienREF
	 AND a.TenDangNhap = b.TenDangNhap
	 AND a.TenNhanVien = b.TenNhanVien 
	 AND a.TenKhachHang = b.TenKhachHang
	 AND a.NhanHang = b.NhanHang
	 AND a.HTQC = b.HTQC
	 AND a.TenHTQC = b.TenHTQC
	 AND a.DmSanPhamREF = b.DmSanPhamREF
	 AND a.TenSanPham = b.TenSanPham
	 )	 
	 WHERE (round(a.tthd - b.thanhtientc,0) <-2 OR (b.thanhtientc <0)OR a.tthd IS null)-- AND NOT (a.tthd IS NULL AND b.thanhtientc = 0)
	  AND a.DmSanPhamREF IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@DmSanPhamREF, ',')) att)
	--ORDER BY  B.HopDongID, B.SoHopDong, B.DmMaHopDongREF, B.TenMaHopDong, B.NgayDanhSoHopDong, B.NhanHopDong, B.HopDongChiTietREF,
	--B.DmPhongBanREF, B.TenPhongBan, B.DmBoPhanREF, B.TenBoPhan, B.DmNhomLamViecREF,  B.TenNhomLamViec, B.TenDiaDiemLamViec,
	-- 	 B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien, TenKhachHang, B.NhanHang, B.DmNhomNganhREF,TenNhomNganh, B.DmHinhThucQuangCao, B.TenHinhThucQuangCao,
	--B.DmSanPhamREF, B.TenSanPham, B.DmWebsiteREF, B.TenWebsite
	END
	
		--9. HopDong, Nhan Hang, sanpham, khach hang, nhan vien --admarket
	ELSE IF @LoaiCheck =9
BEGIN
	SELECT a.*, b.*, (ISNULL(a.tthd,0) - ISNULL(b.thanhtientc,0)) lechhdtc FROM ( 
	 SELECT hd.HopDongID, hd.SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietID,
	 DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomREF DmNhomLamViecREF, TenNhom TenNhomLamViec, TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang, DmLoaiREF HTQC, TenLoai TenHTQC,
	hdct.DmSanPhamREF, hdct.TenSanPham, dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(DmWebsiteREF)DmWebsiteREF,
	dbo.GetWebsiteLinkByDmWebsiteID(DmWebsiteREF,TenWebsite) TenWebsite
	 ,SUM(Thanhtien)tthd
	 FROM HopDong hd INNER JOIN HopDongChiTiet hdct 
	 ON hd.HopDongID = hdct.HopDongFK
	 WHERE 1=1-- hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
	AND hd.DeletedStatus <> 1
	 AND hdct.DeletedStatus <> 1
	 AND hd.TrangThaiHopDong <> 3
	 AND DmSanPhamREF  IN (144,585,628)
	 AND HopDongID IN (SELECT HopDongFK FROM dbo.HopDongChiTietLog WHERE LastModifiedAt >'2015-11-07' UNION ALL SELECT HopDongID FROM dbo.HopDongLog WHERE LastModifiedAt >'2015-11-07')
	 --AND DmSanPhamREF IN (549)
	 --AND HopDongChiTietID = 90614
	 --AND SoHopDong =   'QC2700116'--@SoHopDong
	 GROUP BY hd.HopDongID, hd.SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietID,
	 DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomREF, TenNhom, TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang, DmLoaiREF, TenLoai,
	hdct.DmSanPhamREF, hdct.TenSanPham,  DmWebsiteREF,  TenWebsite
	 )a
	 FULL OUTER JOIN
	 (	 	
	 SELECT --B.shdb, 
	 B.HopDongID, B.SoHopDong, B.DmMaHopDongREF, B.TenMaHopDong, B.NgayDanhSoHopDong, B.HopDongChiTietREF,
	B.DmPhongBanREF, B.TenPhongBan, B.DmBoPhanREF, B.TenBoPhan, B.DmNhomLamViecREF,  B.TenNhomLamViec, B.TenDiaDiemLamViec,
	 	 B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien, TenKhachHang, B.NhanHang, B.HTQC, B.TenHTQC,
	B.DmSanPhamREF, B.TenSanPham, B.DmWebsiteREF, B.TenWebsite,sum(B.thanhtientc)thanhtientc
	   FROM
	 (
	 SELECT HopDongID, SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietREF,
	 DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomLamViecREF, TenNhomLamViec, TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang,  DmHinhThucQuangCao HTQC, TenHinhThucQuangCao TenHTQC,
	DmSanPhamREF, TenSanPham, DmWebsiteREF, TenWebsite,
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinhAdmarket tcdt
	 WHERE 1=1 AND tcdt.NgayThucHien <= @NgayThucHien AND 
	 tcdt.DmSanPhamREF IN (144,585,628)
	AND  tcdt.TrangThaiHopDong <> 3
	 AND HopDongID IN (SELECT HopDongFK FROM dbo.HopDongChiTietLog WHERE LastModifiedAt >'2015-11-07' UNION ALL SELECT HopDongID FROM dbo.HopDongLog WHERE LastModifiedAt >'2015-11-07')
	-- AND SoHopDong =   'QC2700116'--@SoHopDong
	 -- AND HopDongChiTietREF = 90614
	 GROUP BY  HopDongID, SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, HopDongChiTietREF,
	 DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomLamViecREF, TenNhomLamViec, TenDiaDiemLamViec,
	 SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang,  DmHinhThucQuangCao, TenHinhThucQuangCao,
	DmSanPhamREF, TenSanPham, DmWebsiteREF, TenWebsite	 
	 )B 	
	 GROUP BY
	  B.HopDongID, B.SoHopDong, B.DmMaHopDongREF, B.TenMaHopDong, B.NgayDanhSoHopDong, B.HopDongChiTietREF,
	B.DmPhongBanREF, B.TenPhongBan, B.DmBoPhanREF, B.TenBoPhan, B.DmNhomLamViecREF,  B.TenNhomLamViec, B.TenDiaDiemLamViec,
	 	 B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien, TenKhachHang, B.NhanHang,B.HTQC, B.TenHTQC,
	B.DmSanPhamREF, B.TenSanPham, B.DmWebsiteREF, B.TenWebsite
	 )b
	 ON (1=1 	 
	 AND a.HopDongID =  b.HopDongID
	 AND a.SoHopDong = b.SoHopDong
	 AND a.DmMaHopDongREF = b.DmMaHopDongREF
	 AND a.TenMaHopDong = b.TenMaHopDong
	 AND a.NgayDanhSoHopDong = b.NgayDanhSoHopDong
	 AND a.HopDongChiTietID = b.HopDongChiTietREF
	 and a.DmPhongBanREF = b.DmPhongBanREF
	 AND a.TenPhongBan = b.TenPhongBan
	 AND a.DmBoPhanREF = b.DmBoPhanREF
	 AND b.TenBoPhan = b.TenBoPhan
	 AND a.DmNhomLamViecREF = b.DmNhomLamViecREF
	 AND a.TenNhomLamViec = b.TenNhomLamViec
	 AND a.TenDiaDiemLamViec = b.TenDiaDiemLamViec
	 AND a.SysNhanVienREF = b.SysNhanVienREF
	 AND a.TenDangNhap = b.TenDangNhap
	 AND a.TenNhanVien = b.TenNhanVien 
	 AND a.TenKhachHang = b.TenKhachHang
	 AND a.NhanHang = b.NhanHang
	 AND a.HTQC = b.HTQC
	 AND a.TenHTQC = b.TenHTQC
	 AND a.DmSanPhamREF = b.DmSanPhamREF
	 AND a.TenSanPham = b.TenSanPham
	 AND a.DmWebsiteREF = b.DmWebsiteREF
	 AND a.TenWebsite = b.TenWebsite
	 )	 
	 WHERE (round(a.tthd - b.thanhtientc,0) <-2 OR (b.thanhtientc <0)OR a.tthd IS null) AND NOT (a.tthd IS NULL AND b.thanhtientc = 0)
	--ORDER BY  B.HopDongID, B.SoHopDong, B.DmMaHopDongREF, B.TenMaHopDong, B.NgayDanhSoHopDong, B.NhanHopDong, B.HopDongChiTietREF,
	--B.DmPhongBanREF, B.TenPhongBan, B.DmBoPhanREF, B.TenBoPhan, B.DmNhomLamViecREF,  B.TenNhomLamViec, B.TenDiaDiemLamViec,
	-- 	 B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien, TenKhachHang, B.NhanHang, B.DmNhomNganhREF,TenNhomNganh, B.DmHinhThucQuangCao, B.TenHinhThucQuangCao,
	--B.DmSanPhamREF, B.TenSanPham, B.DmWebsiteREF, B.TenWebsite
	END
END

```
