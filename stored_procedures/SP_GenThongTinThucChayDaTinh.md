# Stored Procedure: `GenThongTinThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-28 09:25:32.837000
- **Ngày sửa cuối**: 2016-11-28 10:14:10.640000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC GenThongTinThucChayDaTinh
CREATE PROC GenThongTinThucChayDaTinh
AS
BEGIN
------------Thong tin hopdong ---------------
DROP TABLE #ThongTinHopDong
SELECT hd.SoHopDong,hd.TenMaHopDong, hd.HopDongID, hd.DmKhachHangREF, hd.TenKhachHang, hd.SysNhanVienREF, hd.TenDangNhap, 
hd.TenNhanVien, hdct.HopDongChiTietID,
hdct.DmLoaiREF, hdct.TenLoai, hdct.DmLoaiBannerREF, hdct.TenLoaiBanner,
hdct.DmWebsiteREF, hdct.TenWebsite, hdct.DmSanPhamREF, hdct.TenSanPham,
 hd.TrangThaiHopDong, hdct.DeletedStatus,
(CASE WHEN hd.TrangThaiHopDong = 3 THEN 0
		when hdct.DeletedStatus = 1 then 0
		ELSE hdct.ThanhTien end)ThanhTien
		INTO #ThongTinHopDong
FROM hopdong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
WHERE hd.Nam>=2013

------------Thuc chay 2016---------------
DROP TABLE #ThongTinThucChay2016
SELECT A.* INTO #ThongTinThucChay2016 FROM (
SELECT tcdt.SoHopDong,tcdt.TenMaHopDong, tcdt.HopDongID, tcdt.TenKhachHang, tcdt.SysNhanVienREF, tcdt.TenDangNhap, tcdt.TenNhanVien, 
tcdt.HopDongChiTietREF, 
tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao,
tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner,
tcdt.DmWebsiteREF, tcdt.TenWebsite,
tcdt.DmSanPhamREF, tcdt.TenSanPham
,ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi),0)tc
FROM [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.ThucChayDaTinh tcdt
WHERE TrangThaiHopDong <> 3 AND NgayThucHien BETWEEN'2016-01-01' AND '2016-11-26'
AND tcdt.DmSanPhamREF NOT IN (144,585,628)
GROUP BY tcdt.SoHopDong,TenMaHopDong, tcdt.HopDongID, tcdt.TenKhachHang, tcdt.SysNhanVienREF, tcdt.TenDangNhap, tcdt.TenNhanVien, 
tcdt.HopDongChiTietREF,
tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao,tcdt.DmWebsiteREF, tcdt.TenWebsite,tcdt.DmSanPhamREF, tcdt.TenSanPham
,tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner
HAVING ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi),0) <> 0
UNION ALL
SELECT tcdt.SoHopDong,TenMaHopDong, tcdt.HopDongID, tcdt.TenKhachHang, tcdt.SysNhanVienREF, tcdt.TenDangNhap, tcdt.TenNhanVien, 
tcdt.HopDongChiTietREF, 
tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao,
tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner,
tcdt.DmWebsiteREF, tcdt.TenWebsite,
tcdt.DmSanPhamREF, tcdt.TenSanPham
,ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi),0)tc
FROM [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.ThucChayDaTinhAdmarket tcdt
WHERE TrangThaiHopDong <> 3 AND NgayThucHien BETWEEN'2016-01-01' AND '2016-11-26'
GROUP BY tcdt.SoHopDong,TenMaHopDong, tcdt.HopDongID, tcdt.TenKhachHang, tcdt.SysNhanVienREF, tcdt.TenDangNhap, tcdt.TenNhanVien, 
tcdt.HopDongChiTietREF,
tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao,tcdt.DmWebsiteREF, tcdt.TenWebsite,tcdt.DmSanPhamREF, tcdt.TenSanPham
,tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner
HAVING ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi),0) <> 0
)A

------------Thuc chay all-------------
DROP TABLE #ThongTinThucChayAll
SELECT A.* INTO #ThongTinThucChayAll FROM (
SELECT tcdt.SoHopDong,TenMaHopDong, tcdt.HopDongID, tcdt.TenKhachHang, tcdt.SysNhanVienREF, tcdt.TenDangNhap, tcdt.TenNhanVien, 
tcdt.HopDongChiTietREF, 
tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao,
tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner,
tcdt.DmWebsiteREF, tcdt.TenWebsite,
tcdt.DmSanPhamREF, tcdt.TenSanPham
,ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi),0)tc
FROM [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.ThucChayDaTinh tcdt
WHERE TrangThaiHopDong <> 3 AND NgayThucHien BETWEEN'2013-01-01' AND '2016-11-26'
AND tcdt.DmSanPhamREF NOT IN (144,585,628)
GROUP BY tcdt.SoHopDong,TenMaHopDong, tcdt.HopDongID, tcdt.TenKhachHang, tcdt.SysNhanVienREF, tcdt.TenDangNhap, tcdt.TenNhanVien, 
tcdt.HopDongChiTietREF,
tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao,tcdt.DmWebsiteREF, tcdt.TenWebsite,tcdt.DmSanPhamREF, tcdt.TenSanPham
,tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner
HAVING ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi),0) <> 0
UNION ALL
SELECT tcdt.SoHopDong, TenMaHopDong,tcdt.HopDongID, tcdt.TenKhachHang, tcdt.SysNhanVienREF, tcdt.TenDangNhap, tcdt.TenNhanVien, 
tcdt.HopDongChiTietREF, 
tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao,
tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner,
tcdt.DmWebsiteREF, tcdt.TenWebsite,
tcdt.DmSanPhamREF, tcdt.TenSanPham
,ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi),0)tc
FROM [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.ThucChayDaTinhAdmarket tcdt
WHERE TrangThaiHopDong <> 3 AND NgayThucHien BETWEEN'2013-01-01' AND '2016-11-26'
GROUP BY tcdt.SoHopDong,TenMaHopDong, tcdt.HopDongID, tcdt.TenKhachHang, tcdt.SysNhanVienREF, tcdt.TenDangNhap, tcdt.TenNhanVien, 
tcdt.HopDongChiTietREF,
tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao,tcdt.DmWebsiteREF, tcdt.TenWebsite,tcdt.DmSanPhamREF, tcdt.TenSanPham
,tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner
HAVING ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi),0) <> 0
)A
-----------------------------------------
SELECT * FROM #ThongTinHopDong
SELECT * FROM #ThongTinThucChay2016
SELECT * FROM #ThongTinThucChayAll

--------Thong tin thuc chay---------------
SELECT A.*, B.* FROM (
SELECT HopDongID, SoHopDong, TenMaHopDong,HopDongChiTietID, DmLoaiREF, TenLoai, DmLoaiBannerREF, TenLoaiBanner,
DmSanPhamREF, TenSanPham,
SUM(ThanhTien)ThanhTien
FROM #ThongTinHopDong WHERE DmSanPhamREF not IN (141,637,305)
--AND RIGHT(SoHopDong,2) ='16'
GROUP BY HopDongID, SoHopDong,TenMaHopDong, HopDongChiTietID, DmLoaiREF, TenLoai, DmLoaiBannerREF, TenLoaiBanner,DmSanPhamREF, TenSanPham
)A
FULL OUTER JOIN
(
SELECT HopDongID, SoHopDong, HopDongChiTietREF, DmHinhThucQuangCao, TenHinhThucQuangCao HTQC, DmLoaiBannerREF, TenLoaiBanner 
,DmSanPhamREF, TenSanPham
, SUM(tc)ThucChay
FROM #ThongTinThucChay2016
WHERE DmSanPhamREF  NOT IN (141,637,305)
--AND RIGHT(SoHopDong,2) ='16'
GROUP BY  HopDongID, SoHopDong, HopDongChiTietREF, DmHinhThucQuangCao, TenHinhThucQuangCao, DmLoaiBannerREF, TenLoaiBanner 
,DmSanPhamREF, TenSanPham
)B
ON A.HopDongID =B.HopDongID
AND A.HopDongChiTietID = B.HopDongChiTietREF
WHERE B.ThucChay IS NOT NULL
ORDER BY B.HopDongID, B.HopDongChiTietREF

SELECT A.*, B.* FROM (
SELECT HopDongID, SoHopDong, HopDongChiTietREF, DmHinhThucQuangCao, TenHinhThucQuangCao HTQC, DmLoaiBannerREF, TenLoaiBanner 
,DmSanPhamREF, TenSanPham
, SUM(tc)ThucChayAll
FROM #ThongTinThucChayAll
WHERE DmSanPhamREF  NOT IN (141,637,305)
--AND RIGHT(SoHopDong,2) ='16'
GROUP BY  HopDongID, SoHopDong, HopDongChiTietREF, DmHinhThucQuangCao, TenHinhThucQuangCao, DmLoaiBannerREF, TenLoaiBanner 
,DmSanPhamREF, TenSanPham)A
RIGHT JOIN
(
SELECT HopDongID, SoHopDong, HopDongChiTietREF, DmHinhThucQuangCao, TenHinhThucQuangCao HTQC, DmLoaiBannerREF, TenLoaiBanner 
,DmSanPhamREF, TenSanPham
, SUM(tc)ThucChay
FROM #ThongTinThucChay2016
WHERE DmSanPhamREF  NOT IN (141,637,305)
--AND RIGHT(SoHopDong,2) ='16'
GROUP BY  HopDongID, SoHopDong, HopDongChiTietREF, DmHinhThucQuangCao, TenHinhThucQuangCao, DmLoaiBannerREF, TenLoaiBanner 
,DmSanPhamREF, TenSanPham
)B
ON A.HopDongID =B.HopDongID
AND A.HopDongChiTietREF = B.HopDongChiTietREF
--WHERE A.ThucChay IS NOT NULL
ORDER BY B.HopDongID, B.HopDongChiTietREF
END


```
