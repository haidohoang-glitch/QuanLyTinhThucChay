# Stored Procedure: `CheckViewplusByUserName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-15 17:40:58.337000
- **Ngày sửa cuối**: 2017-02-15 17:40:58.337000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@username` | `nvarchar(100)` | No |
| `@HopDongID` | `int(4)` | No |
| `@nt1` | `datetime(8)` | No |
| `@ngaythuchien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE CheckViewplusByUserName
	------------------**********************---------------------------

  @username NVARCHAR(50), @HopDongID INT, @nt1 DATETIME,@ngaythuchien DATETIME, @DmSanPhamREF INT
AS
BEGIN
 SET @DmSanPhamREF=628

SELECT  'Balance' [Balance],
       abud.UserName,


       abud.DmSanPhamREF,
       abud.TenSanPham,
       abud.UserBalance,
       abud.UserPromotion,
       abud.NgayThucHien
FROM   AdmarketBalanceUserDaily abud
WHERE  abud.UserName = @username
       AND abud.DmSanPhamREF = @DmSanPhamREF
       AND abud.NgayThucHien <= @ngaythuchien
ORDER BY abud.NgayThucHien DESC

-----***Lan Nap Cuoi cung***--------
SELECT  
'LastRecharge' [LastRecharge],
       abud.UserName,
       abud.DmSanPhamREF,
       abud.TenSanPham,
       abud.LastDateRecharge, abud.RechargeMoney
FROM   AdmarketUserLastRecharge abud
WHERE  UserName = @username
       AND DmSanPhamREF = @DmSanPhamREF
ORDER BY
       abud.LastDateRecharge DESC
 
 --select * from 
 --AdmarketUserLastRecharge order by LastDateRecharge desc , dmsanphamref
 ---*********Canh bao**************----

------HopDong-----       
SELECT NhanHang, DanhSachNhanHangREF,NgayDanhSoHopDong, TenKhachHang, TenNhanVien , HopDongChiTietID, SoHopDong
FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
ON HopDongID = HopDongFK
WHERE  HopDongFK = @HopDongID AND DmSanPhamREF = @DmSanPhamREF AND TK_AdMarket = @username
AND hdct.DeletedStatus <> 1
-----ThucChayDaTinh--------
 SELECT tcdt.ThucChayDaTinhID , tcdt.SoHopDong,
NhanHang,  NgayDanhSoHopDong, TenKhachHang, TenNhanVien,
tcdt.SoHopDong,
  tcdt.HopDongID, tcdt.HopDongChiTietREF hdct, tcdt.NgayThucHien, tcdt.SoLuongThucChay sltc, tcdt.ThanhTienSauTrietKhauThucChay ttsck, tcdt.GiaTriThayDoi, tcdt.CreatedAt
 , tcdt.GhiChu
   FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID =  @HopDongID AND tcdt.DmSanPhamREF = @DmSanPhamREF
    --AND tcdt.NgayThucHien >= '2015-06-05'
 ORDER BY tcdt.NgayThucHien,tcdt.CreatedAt

SELECT 'DuLieuLayVe' [DuLieuLayVe], A.username, A.DmSanPhamREF, A.TenSanPham
	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(A.[money])/1.1) tienchinh,SUM(A.[money]) tienchinhvat
	, SUM(A.pro)/1.1 tienkm
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM ThucChayViewPlusForUsers A
WHERE A.NgayThucHien = @ngaythuchien AND A.DmSanPhamREF=@DmSanPhamREF 
	AND A.username = @username
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A.username, A.IsNoiBo, A.DmSanPhamREF, A.TenSanPham
--Kiem tra du lieu lay ve bang nhan hang-----------------
SELECT 'DuLieuLayVeNhanHang' DuLieuLayVeNhanHang, A.username, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang
	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(A.[money])/1.1) tienchinh,SUM(A.[money]) tienchinhvat
	, SUM(A.pro)/1.1 tienkm
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM dbo.ThucChayAdmarketUser_NhanHang A
WHERE A.NgayThucHien = @ngaythuchien AND A.DmSanPhamREF=@DmSanPhamREF 
	AND A.username = @username
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A.username, A.IsNoiBo, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang
--Kiem tra du lieu lay ve-----------------
SELECT 'DuLieuLayVeAll' [DuLieuLayVe], A.username
	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	, dbo.FormatNumber( SUM(A.[money])/1.1) tienchinh,SUM(A.[money]) tienchinhvat
	, SUM(A.pro)/1.1 tienkm
	, dbo.FormatNumber( SUM(A.[money] + A.pro)) tienallvat
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM ThucChayViewPlusForUsers A
WHERE A.NgayThucHien BETWEEN @nt1 and @ngaythuchien AND A.DmSanPhamREF=@DmSanPhamREF 
	AND A.username = @username
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A.username, A.IsNoiBo
------------------------DuLieuVeNhanHangAll----------------------------
SELECT 'DuLieuLayVeNhanHangAll' DuLieuLayVeNhanHang, A.username, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang
	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc	
	, dbo.FormatNumber( SUM(A.[money])/1.1) tienchinh,SUM(A.[money]) tienchinhvat
	, SUM(A.pro)/1.1 tienkm
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM dbo.ThucChayAdmarketUser_NhanHang A
WHERE A.NgayThucHien <= @ngaythuchien AND A.DmSanPhamREF=@DmSanPhamREF 
	AND A.username = @username
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A.username, A.IsNoiBo, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang
--Kiem tra du lieu lay ve-----------------
--------------ThucChayDaTinhAdmarket-----------------------------
SELECT 
	ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0) TongTien 
	, SUM(tcdta.ThanhTienKM) ThanhTienKM	
FROM ThucChayDaTinhAdmarket tcdta 
WHERE tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
FROM HopDongChiTiet AS hdct WHERE hdct.DmSanPhamREF = @DmSanPhamREF 
	 AND hdct.TK_AdMarket = @username
	 AND convert(date,hdct.CreatedAt) <= @ngaythuchien
	 AND hdct.DeletedStatus <>1)
	 AND tcdta.NgayThucHien <=@ngaythuchien

SELECT 
	dbo.FormatNumber(ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0)) TongTienNew
	,SUM(tcdta.SoLuongThucChay) 
	, SUM(tcdta.ThanhTienKM) ThanhTienKM	
FROM ThucChayDaTinhAdmarket tcdta 
WHERE tcdta.HopDongChiTietREF IN 
(SELECT  hdct.HopDongChiTietID
FROM HopDongChiTiet AS hdct INNER JOIN HopDong hd ON hdct.HopDongFK = hd.HopDongID
 WHERE hdct.DmSanPhamREF = @DmSanPhamREF 
	 AND hdct.TK_AdMarket = @username
	 AND hd.NgayDanhSoHopDong >='2013-01-01'
	 AND convert(date,hdct.CreatedAt) <= @ngaythuchien
	 AND hdct.DeletedStatus <>1
	 AND hd.Nam > 2012
)
	 AND tcdta.NgayThucHien <=@ngaythuchien
	
	 

--------Chi tiet thuc chay và hop dong 
SELECT HD.HopDongID, HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt, HD.ThanhTien, HD.TenNhanVien, TC.DonViTinh
	, TC.NgayThucHienMin
	, TC.NgayThucHienMax	
	, TC.SL, dbo.FormatNumber(TC.TienThucChay)TienThucChay,
	 ISNULL(SUM((TV.TienVe * HD.Tyle)/100),0)TienVe
    ,ROUND((ISNULL(SUM((TV.TienVe * HD.Tyle)/100),0) -TC.TienThucChay),0) AS [TienVe - ThucChay],
       (HD.ThanhTien -TC.TienThucChay) [ThanhTien - ThucChay]
FROM
( 
	SELECT tcdta.HopDongID, tcdta.SoHopDong,(CASE WHEN tcdta.DonViTinh = 'CPC' THEN 'CLICK' ELSE tcdta.DonViTinh END)DonViTinh, tcdta.HopDongChiTietREF
		, MIN(tcdta.NgayThucHien) NgayThucHienMin 
		, MAX(tcdta.NgayThucHien) NgayThucHienMax
		, SUM(tcdta.SoLuongThucChay+tcdta.SoLuongThayDoi) AS SL
		, ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay),0) ThanhTienThucChay 
		, ROUND(SUM(tcdta.GiaTriThayDoi),0) GiaTriThayDoi
		, ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0) TienThucChay
		, SUM(tcdta.ThanhTienKM) ThanhTienKM
	FROM ThucChayDaTinhAdmarket tcdta 
	WHERE 1=1
		AND tcdta.NgayThucHien BETWEEN @nt1 AND @ngaythuchien
		AND tcdta.HopDongChiTietREF IN (
							SELECT hdct.HopDongChiTietID
							FROM HopDongChiTiet AS hdct WHERE hdct.DmSanPhamREF = 628
								AND hdct.TK_AdMarket = @username
								AND convert(date,hdct.CreatedAt) <= @ngaythuchien
								--AND hdct.DeletedStatus <>1
						)
	GROUP BY tcdta.SoHopDong, tcdta.HopDongID, tcdta.DonViTinh, tcdta.HopDongChiTietREF
) TC FULL OUTER JOIN
(
	SELECT hd.HopDongID , hd.TenNhanVien
		, hd.SoHopDong, hdct.HopDongChiTietID
		, CASE WHEN hd.TrangThaiHopDong = 3 THEN 0 ELSE SUM(hdct.ThanhTien) END ThanhTien		
		, (SUM(hdct.ThanhTien*1.1))/(hd.GiaTriHopDong)*100 AS Tyle
		, hdct.TK_AdMarket, hdct.CreatedAt
	FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK	
	WHERE hdct.TK_AdMarket = @username 
		AND hdct.DeletedStatus =0
		AND hdct.DmSanPhamREF = 628
		AND hdct.DmLoaiBannerREF <> 17
	GROUP BY hd.HopDongID 
		, hd.SoHopDong, hdct.TK_AdMarket, hdct.CreatedAt, hd.TenNhanVien,hd.TrangThaiHopDong, hd.GiaTriHopDong, hdct.ThanhTien, hdct.HopDongChiTietID
) HD ON HD.HopDongID = TC.HopDongID AND  TC.HopDongChiTietREF = HD.HopDongChiTietID
FULL OUTER JOIN 
(
	SELECT tttv.HopDongREF, ROUND(SUM(tttv.GiaTri)/1.1,0) AS TienVe FROM ThongTinTienVe tttv 
	WHERE tttv.HopDongREF IN (SELECT hd2.HopDongID
	                         FROM HopDong hd2 INNER JOIN HopDongChiTiet hdct2 ON hd2.HopDongID = hdct2.HopDongFK
							AND hdct2.TK_AdMarket = @username AND hdct2.DmSanPhamREF = 628
							AND hd2.TrangThaiHopDong <> 3 AND hdct2.DeletedStatus = 0
		)
	AND tttv.DeletedStatus = 0
	GROUP BY tttv.HopDongREF	
) TV ON HD.HopDongID = TV.HopDongREF

GROUP BY HD.HopDongID,HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt, HD.ThanhTien, HD.TenNhanVien, TC.DonViTinh
	, TC.NgayThucHienMin
	, TC.NgayThucHienMax	,
	 TC.SL, TC.TienThucChay
end

```
