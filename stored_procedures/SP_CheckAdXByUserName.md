# Stored Procedure: `CheckAdXByUserName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-15 17:23:01.773000
- **Ngày sửa cuối**: 2017-04-06 21:55:50.810000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@username` | `nvarchar(100)` | No |
| `@ngaythuchien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@nth1` | `datetime(8)` | No |
| `@nth2` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--exec [CheckAdXByUserName] 'ngoan28987','2017-04-04',48869, '2014-01-01','2017-04-04'
--update thucchaydatinhadmarket set thanhtiensautrietkhauthucchay =thanhtiensautrietkhauthucchay-404545.363635086 where thucchaydatinhid = '29E06051-5A76-4E65-860F-7FBFDD20AD1A'
CREATE PROCEDURE [dbo].[CheckAdXByUserName]

@username NVARCHAR(50) ,@ngaythuchien DATETIME,
@HopDongID INT, @nth1 DATETIME, @nth2 DATETIME

/*
EXEC InsertManualThucChayDaTinhAdmarket
	'2017-02-06',--@NgayThucHien DATETIME, 
	'QC1120117',--@SoHopDong NVARCHAR(50), 
	500608,--@HopDongChiTietID INT, 
	15455636,--@GiaTriThayDoi INT, 
	585,--@DmSanPhamREF INT, 
	0,--@ThanhTienSTCK FLOAT, 
	'lantran',--@Tk NVARCHAR(50), 
	2,--@DmViTriREF int, 
	'36895'--@NhanHang nvarchar(50)


	*/
--SET @username= 'fpt_city'--,thanh_ctl ,
----imperiagarden: dongnampromotion nhận theo tiền nạp vào tk
--SET @nth1 = '2017-01-01'
--SET @nth2 = '2017-01-31'
AS BEGIN
DECLARE @DmSanPhamREF INT
SET @DmSanPhamREF = 585
--SET @HopDongID =40357

  SELECT  distinct abud.UserName, dmSanPhamREF, abud.NgayThucHien, (abud.UserBalance/1.1) UserBalance, (abud.UserPromotion/1.1) UserPromotion
   FROM AdmarketBalanceUserDaily abud WHERE abud.UserName = @username 
   AND abud.DmSanPhamREF = @DmSanPhamREF
 AND abud.NgayThucHien <= @nth2
 ORDER BY abud.NgayThucHien DESC
 
  SELECT DISTINCT 'LastRecharge'[LastRecharge], abud.UserName, UserID, abud.DmSanPhamREF, abud.TenSanPham, abud.LastDateRecharge,abud.RechargeMoney
   FROM AdmarketUserLastRecharge abud 
  WHERE abud.UserName = @username
    AND abud.DmSanPhamREF = @DmSanPhamREF
 --AND convert(date,abud.LastDateRecharge) <= @ngaythuchien
 ORDER BY abud.LastDateRecharge DESC
  
 -----------HopDong ------------
 SELECT HopDongChiTietID,thanhtien, NhanHopDong,NhanHang,DanhSachNhanHangREF, NgayDanhSoHopDong, TenKhachHang, TenNhanVien 
FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
ON HopDongID = HopDongFK
WHERE  HopDongFK = @HopDongID AND DmSanPhamREF = @DmSanPhamREF AND TK_AdMarket = @username
AND hdct.DeletedStatus <> 1
-----------ThucChayDaTinh----------------
 SELECT tcdt.ThucChayDaTinhID, tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF,NhanHopDong,
 NhanHang, NgayDanhSoHopDong, TenKhachHang, TenNhanVien ,
  convert(Date,tcdt.NgayThucHien)NgayThucHien,
  tcdt.SoLuongThucChay,tcdt.SoLuongThayDoi, tcdt.ThanhTienSauTrietKhauThucChay,
   tcdt.GiaTriThayDoi, tcdt.DmViTriREF, tcdt.TenViTri, tcdt.GhiChu,tcdt.CreatedAt
   FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID =  @HopDongID AND tcdt.DmSanPhamREF = 585-- AND tcdt.NgayThucHien >='2015-05-14'
   AND TrangThaiHopDong <> 3
    --AND tcdt.HopDongChiTietREF = 96250
   AND HopDongChiTietREF IN (SELECT HopDongChiTietID FROM dbo.HopDongChiTiet WHERE TK_AdMarket = @username AND HopDongFK = @HopDongID)
 ORDER BY tcdt.NgayThucHien, HopDongChiTietREF, tcdt.CreatedAt
 

--ThucChayAdXforUsersAll
SELECT 'ThucChayAdXforUsersAll', tcdta.username,userid, tcdta.TenViTri, tcdta.DmViTriREF
--, SUM(ttc) ttc, SUM(ttv) ttv
, MIN(tcdta.NgayThucHien) AS TuNgay , MAX(tcdta.NgayThucHien) NgayThucHienMax
 ,dbo.FormatNumber(SUM(CONVERT(FLOAT,tcdta.[money]))) AS TienChinh_VAT
, dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT,tcdta.[money])/1.1),0)) AS TienChinh_ChuaVAT,sum(CONVERT(FLOAT,tcdta.[money]+tcdta.pro)) TienAllVAT
, ROUND(SUM(CONVERT(FLOAT,tcdta.pro/1.1)),0) AS TienKM_ChuaVAT
, tcdta.IsNoiBo--, NgayThucHien
FROM ThucChayAdXforUsers tcdta 
WHERE tcdta.NgayThucHien BETWEEN @nth1 AND @nth2 AND tcdta.DmSanPhamREF=585 AND tcdta.username = @username
GROUP BY tcdta.username ,userid, tcdta.TenViTri, tcdta.IsNoiBo , tcdta.DmViTriREF--, tcdta.NgayThucHien
ORDER BY DmViTriREF--, NgayThucHien desc
--Kiem tra du lieu lay ve bang nhan hang-----------------
SELECT 'DuLieuLayVeNhanHang' DuLieuLayVeNhanHang, A.username, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang
	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(A.[money])/1.1) tienchinh,SUM(A.[money]) tienchinhvat
	, SUM(A.pro)/1.1 tienkm
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM dbo.ThucChayAdmarketUser_NhanHang A
WHERE CONVERT(DATE,A.NgayThucHien) = @nth2 AND A.DmSanPhamREF=@DmSanPhamREF 
	AND A.username = @username
GROUP BY A.username, A.IsNoiBo, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang

--Nhanhangall
SELECT 'DuLieuLayVeNhanHangAll' DuLieuLayVeNhanHang, A.username, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang
	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(A.[money])/1.1) tienchinh,SUM(A.[money]) tienchinhvat
	, SUM(A.pro)/1.1 tienkm
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM dbo.ThucChayAdmarketUser_NhanHang A
WHERE CONVERT(DATE,A.NgayThucHien) <= @nth2 AND A.DmSanPhamREF=@DmSanPhamREF 
	AND A.username = @username
GROUP BY A.username, A.IsNoiBo, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang
--ThucChayAdXforUsers
SELECT 'ThucChayAdXforUsers', tcdta.username, tcdta.DmViTriREF, tcdta.TenViTri
, SUM(ttc) ttc, SUM(ttv) ttv
, MIN(tcdta.NgayThucHien) AS TuNgay , MAX(tcdta.NgayThucHien) NgayThucHienMax
, dbo.FormatNumber(ROUND(SUM(tcdta.[money])/1.1,0)) AS TienChinh_ChuaVAT ,SUM(tcdta.[money]+tcdta.pro) tienchinh
, ROUND(SUM(tcdta.pro/1.1),0) AS TienKM_ChuaVAT, tcdta.IsNoiBo
FROM ThucChayAdXforUsers tcdta 
WHERE tcdta.NgayThucHien = @nth2 AND tcdta.DmSanPhamREF=585 AND tcdta.username = @username
GROUP BY tcdta.username , tcdta.TenViTri , tcdta.IsNoiBo, tcdta.DmViTriREF

  
SELECT tcdta.SoHopDong, tcdta.HopDongChiTietREF, DmViTriREF
	,tcdta.TenSanpham
	, tcdta.ThanhTien
	, SUM(tcdta.TongViewThucChay)TongViewThucChay,SUM( tcdta.SoLuongThucChay)SoLuongThucChay
	, SUM(tcdta.ThanhTienSauTrietKhauThucChay)ThanhTienSauTrietKhauThucChay
	, SUM(tcdta.GiaTriThayDoi)GiaTriThayDoi
	, sum(tcdta.SoLuongThayDoi)SoLuongThayDoi, SUM(tcdta.ThanhTienKM)ThanhTienKM
	, tcdta.NgayThucHien
FROM ThucChayDaTinhAdmarket tcdta 
WHERE tcdta.NgayThucHien = @nth2 AND DmSanPhamREF = 585
	AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID 
										FROM HopDongChiTiet AS hdct 
										WHERE hdct.DmSanPhamREF = 585 AND hdct.TK_AdMarket <> ''
											AND hdct.TK_AdMarket = @username
	--AND convert(date,hdct.CreatedAt) <= @ngaythuchien
	AND hdct.DeletedStatus <>1)
	GROUP BY tcdta.SoHopDong, tcdta.HopDongChiTietREF, DmViTriREF
	,tcdta.TenSanpham
	, tcdta.ThanhTien, tcdta.NgayThucHien

 SELECT A.TenMaHopDong, dbo.FormatNumber (SUM(A.TienThucChay_GTTD))TienThucChay_GTTD, SUM(A.SoLuongTC)sltc,A.DmViTriREF, A.TenViTri--, A.HopDongChiTietREF
 FROM (
 SELECT CASE WHEN TenMaHopDong IN ('NB','SH','NBDT')  THEN 'NB' ELSE 'QC' END TenMaHopDong,
 ROUND(sum(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0) TienThucChay_GTTD
 ,SUM(tcdta.SoLuongThucChay+tcdta.SoLuongThayDoi)SoLuongTC
 , tcdta.DmViTriREF, tcdta.TenViTri--, HopDongChiTietREF
 , sum(tcdta.ThanhTienKM) ThanhTienKM
   FROM ThucChayDaTinhAdmarket tcdta 
 WHERE 1=1
	 AND tcdta.NgayThucHien BETWEEN @nth1 AND @nth2
	 AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
 FROM HopDongChiTiet AS hdct WHERE hdct.DmSanPhamREF = 585 AND hdct.TK_AdMarket <> ''
 AND hdct.TK_AdMarket = @username
 --AND convert(date,hdct.CreatedAt) <= @ngaythuchien
 AND hdct.DeletedStatus <>1)
 GROUP BY tcdta.DmViTriREF, tcdta.TenViTri, TenMaHopDong--,HopDongChiTietREF
 )A
 GROUP BY  A.TenMaHopDong,A.DmViTriREF, A.TenViTri--, A.HopDongChiTietREF
 
 ---Du lieu tcdt theo vi tri--------------------------------
  SELECT A.TenMaHopDong,A.NhanHang,  dbo.FormatNumber (SUM(A.TienThucChay_GTTD))TienThucChay_GTTD, SUM(A.SoLuongTC)sltc,A.DmViTriREF, A.TenViTri 
  FROM (
 SELECT CASE WHEN TenMaHopDong IN ('NB','SH','NBDT')  THEN 'NB' ELSE 'QC' END TenMaHopDong,Nhanhang,
 ROUND(sum(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0) TienThucChay_GTTD
 ,SUM(tcdta.SoLuongThucChay+tcdta.SoLuongThayDoi)SoLuongTC
 , tcdta.DmViTriREF, tcdta.TenViTri
 , sum(tcdta.ThanhTienKM) ThanhTienKM
   FROM ThucChayDaTinhAdmarket tcdta 
 WHERE 1=1
	 AND tcdta.NgayThucHien BETWEEN @nth1 AND @nth2
	 AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
 FROM HopDongChiTiet AS hdct WHERE hdct.DmSanPhamREF = 585 AND hdct.TK_AdMarket <> ''
 AND hdct.TK_AdMarket = @username
 --AND convert(date,hdct.CreatedAt) <= @ngaythuchien
 AND hdct.DeletedStatus <>1)
 GROUP BY tcdta.DmViTriREF, tcdta.TenViTri, TenMaHopDong,tcdta.NhanHang
 )A
 GROUP BY  A.TenMaHopDong,A.DmViTriREF, A.TenViTri,A.NhanHang
 ORDER BY A.DmViTriREF,  CONVERT(INT,A.NhanHang)
--------Chi tiet thuc chay và hop dong ---------------------------------------
SELECT HD.HopDongID, HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt, HD.ThanhTien, HD.TenNhanVien,HD.TenKhachHang, TC.DonViTinh
	, TC.NgayThucHienMin
	, TC.NgayThucHienMax	
	, TC.SL, dbo.FormatNumber(TC.TienThucChay)TienThucChay,
	 ISNULL(SUM((TV.TienVe * HD.Tyle)/100),0)TienVe
    ,ROUND((ISNULL(SUM((TV.TienVe * HD.Tyle)/100),0) -TC.TienThucChay),0) AS [TienVe - ThucChay],
       (HD.ThanhTien -TC.TienThucChay) [ThanhTien - ThucChay]
FROM
(
	SELECT tcdta.HopDongID, tcdta.SoHopDong, tcdta.DonViTinh, tcdta.HopDongChiTietREF
		, MIN(tcdta.NgayThucHien) NgayThucHienMin 
		, MAX(tcdta.NgayThucHien) NgayThucHienMax
		, SUM(tcdta.SoLuongThucChay+tcdta.SoLuongThayDoi) AS SL
		, ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay),0) ThanhTienThucChay 
		, ROUND(SUM(tcdta.GiaTriThayDoi),0) GiaTriThayDoi
		, ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0) TienThucChay
		, SUM(tcdta.ThanhTienKM) ThanhTienKM
	FROM ThucChayDaTinhAdmarket tcdta 
	WHERE 1=1
		AND tcdta.NgayThucHien BETWEEN @nth1 AND @nth2
		AND DmSanPhamREF = 585
		AND tcdta.HopDongChiTietREF IN (
							SELECT hdct.HopDongChiTietID
							FROM HopDongChiTiet AS hdct WHERE hdct.DmSanPhamREF = 585
								AND hdct.TK_AdMarket = @username
								--AND convert(date,hdct.CreatedAt) <= @ngaythuchien
								--AND hdct.DeletedStatus <>1
						)
	GROUP BY tcdta.SoHopDong, tcdta.HopDongID, tcdta.DonViTinh, tcdta.HopDongChiTietREF
) TC FULL OUTER JOIN
(
	SELECT hd.HopDongID , hd.TenNhanVien,hd.TenKhachHang, hdct.HopDongChiTietID
		, hd.SoHopDong
		, CASE WHEN hd.TrangThaiHopDong = 3 THEN 0 ELSE SUM(hdct.ThanhTien) END ThanhTien		
		, (CASE WHEN GiaTriHopDong <>0 then(SUM(hdct.ThanhTien*1.1))/(hd.GiaTriHopDong)*100 ELSE 0 END) AS Tyle
		, hdct.TK_AdMarket, hdct.CreatedAt
	FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK	
	WHERE hdct.TK_AdMarket = @username 
		AND hdct.DeletedStatus =0
		AND hdct.DmSanPhamREF = 585
		--AND hdct.DmLoaiBannerREF <> 17
	GROUP BY hd.HopDongID , TenKhachHang
		, hd.SoHopDong, hdct.TK_AdMarket, hdct.CreatedAt, hd.TenNhanVien,hd.TrangThaiHopDong, hd.GiaTriHopDong, hdct.ThanhTien,hdct.HopDongChiTietID
) HD ON HD.HopDongID = TC.HopDongID AND TC.HopDongChiTietREF = HD.HopDongChiTietID
FULL OUTER JOIN 
(
	SELECT tttv.HopDongREF, ROUND(SUM(tttv.GiaTri)/1.1,0) AS TienVe FROM ThongTinTienVe tttv 
	WHERE tttv.HopDongREF IN (SELECT hd2.HopDongID
	                         FROM HopDong hd2 INNER JOIN HopDongChiTiet hdct2 ON hd2.HopDongID = hdct2.HopDongFK
							AND hdct2.TK_AdMarket = @username AND hdct2.DmSanPhamREF = 585
							--AND hd2.TrangThaiHopDong <> 3
							 AND hdct2.DeletedStatus = 0
		)
	AND tttv.DeletedStatus = 0
	GROUP BY tttv.HopDongREF	
) TV ON HD.HopDongID = TV.HopDongREF

GROUP BY HD.HopDongID,HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt, HD.ThanhTien, HD.TenNhanVien, TC.DonViTinh, HD.TenKhachHang
	, TC.NgayThucHienMin
	, TC.NgayThucHienMax	,
	 TC.SL, TC.TienThucChay
end
```
