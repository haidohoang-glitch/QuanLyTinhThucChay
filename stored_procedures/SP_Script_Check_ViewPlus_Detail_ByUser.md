# Stored Procedure: `Script_Check_ViewPlus_Detail_ByUser`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-05 11:20:51.013000
- **Ngày sửa cuối**: 2021-03-05 11:20:51.013000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@username` | `nvarchar(100)` | No |
| `@nt1` | `datetime(8)` | No |
| `@ngaythuchien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--Script_Check_ViewPlus_Detail_ByUser 'vincom_pmqc','2013-01-01','2020-12-30',585,NULL
create proc Script_Check_ViewPlus_Detail_ByUser
@username NVARCHAR(50) ,
@nt1 DATETIME,
@ngaythuchien DATETIME,
@DmSanPhamREF INT,
@HopDongID INT
as
begin

------HopDong-----       
SELECT hdct.HopDongChiTietID, NhanHang, DanhSachNhanHangREF,NgayDanhSoHopDong, TenKhachHang, TenNhanVien , HopDongChiTietID, SoHopDong
FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
ON HopDongID = HopDongFK
WHERE  HopDongFK = @HopDongID AND DmSanPhamREF = @DmSanPhamREF AND TK_AdMarket = @username
AND hdct.DeletedStatus <> 1
-----ThucChayDaTinh--------
 SELECT tcdt.ThucChayDaTinhID , tcdt.SoHopDong,
NhanHang,  NgayDanhSoHopDong, TenKhachHang, TenNhanVien,
tcdt.SoHopDong,
  tcdt.HopDongID, tcdt.HopDongChiTietREF hdct, tcdt.NgayThucHien, tcdt.SoLuongThucChay sltc, tcdt.ThanhTienSauTrietKhauThucChay ttsck, tcdt.GiaTriThayDoi, tcdt.DmVitriref, tcdt.TenViTri,
  tcdt.GhiChu
   FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID =  @HopDongID AND tcdt.DmSanPhamREF = @DmSanPhamREF
    --AND tcdt.NgayThucHien >= '2015-06-05'
 ORDER BY tcdt.NgayThucHien,tcdt.CreatedAt

 --------- ThucChayAdmarket_Viewplus_HopDong

 SELECT 'ThucChayAdmarket_Viewplus_HopDong' [ThucChayAdmarket_Viewplus_HopDong], A1.username, A1.DmSanPhamREF, A1.TenSanPham
--	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
--	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(convert(float,A1.domain_money))/1.1) tienchinh,SUM(convert(float,A1.domain_money)) tienchinhvat
	, SUM(convert(float,A1.domain_promotion))/1.1 tienkm_chuaVAT
	, MAX(A1.NgayThucHien)NgayThucHienMax, MIN(A1.NgayThucHien)NgayThucHienMin
	, A1.isnoibo
FROM ThucChayAdmarket_Viewplus_HopDong A1	inner join HopDOng hd on hd.SoHopDong = A1.contract_number
WHERE A1.NgayThucHien = @ngaythuchien AND A1.DmSanPhamREF=@DmSanPhamREF 
	AND A1.username = @username
	And hd.HopDongID = @HopDongID 
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A1.username, A1.isnoibo, A1.DmSanPhamREF, A1.TenSanPham

----ALL
 SELECT 'ThucChayAdmarket_Viewplus_HopDong_All' [ThucChayAdmarket_Viewplus_HopDong_All], A1.username, A1.DmSanPhamREF, A1.TenSanPham
--	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
--	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(convert(float,A1.domain_money))/1.1) tienchinh,SUM(convert(float,A1.domain_money)) tienchinhvat
	, SUM(convert(float,A1.domain_promotion))/1.1 tienkm_chuaVAT
	, MAX(A1.NgayThucHien)NgayThucHienMax, MIN(A1.NgayThucHien)NgayThucHienMin
	, A1.isnoibo
FROM ThucChayAdmarket_Viewplus_HopDong A1	inner join HopDOng hd on hd.SoHopDong = A1.contract_number
WHERE (A1.NgayThucHien between @nt1 and  @ngaythuchien) AND A1.DmSanPhamREF=@DmSanPhamREF 
	AND A1.username = @username
	And hd.HopDongID = @HopDongID 
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A1.username, A1.isnoibo, A1.DmSanPhamREF, A1.TenSanPham

 SELECT 'ThucChayAdmarket_Viewplus_HopDong_All_TK' [ThucChayAdmarket_Viewplus_HopDong_All], A1.username, A1.DmSanPhamREF, A1.TenSanPham
--	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
--	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(convert(float,A1.domain_money))/1.1) tienchinh,SUM(convert(float,A1.domain_money)) tienchinhvat
	, SUM(convert(float,A1.domain_promotion))/1.1 tienkm_chuaVAT
	, MAX(A1.NgayThucHien)NgayThucHienMax, MIN(A1.NgayThucHien)NgayThucHienMin
	, A1.isnoibo
FROM ThucChayAdmarket_Viewplus_HopDong A1	
WHERE (A1.NgayThucHien between '2017-09-11' and  @ngaythuchien) AND A1.DmSanPhamREF=@DmSanPhamREF 
	AND A1.username = @username
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A1.username, A1.isnoibo, A1.DmSanPhamREF, A1.TenSanPham

--Kiem tra du lieu lay ve bang nhan hang-----------------
SELECT 'ThucChayAdmarket_Viewplus_NhanHang' [ThucChayAdmarket_Viewplus_NhanHang], A.username, A.DmSanPhamREF, A.TenSanPham, A.dmnhanhang_id
	--, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	--, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(convert(float,A.[money]))/1.1) tienchinh,SUM(convert(float,A.[money])) tienchinhvat
	, SUM(convert(float,A.promotion))/1.1 tienkm
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM dbo.ThucChayAdmarket_Viewplus_NhanHang A	 inner join HopDong hd on hd.SoHopDong = A.contract_number
WHERE A.NgayThucHien = @ngaythuchien AND A.DmSanPhamREF=@DmSanPhamREF 
	AND A.username = @username
	And hd.HopDongID = @HopDongID
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A.username, A.IsNoiBo, A.DmSanPhamREF, A.TenSanPham, A.dmnhanhang_id
--Kiem tra du lieu lay ve-----------------
SELECT 'DuLieuLayVeAll' [DuLieuLayVeAll], A.username
	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	, dbo.FormatNumber( SUM(A.[money])/1.1) tienchinh,SUM(A.[money]) tienchinhvat
	, SUM(A.pro)/1.1 tienkm
	, dbo.FormatNumber( SUM(A.[money] + A.pro)) tienallvat
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM ThucChayViewPlusForUsers A
WHERE A.NgayThucHien BETWEEN @nt1 and '2017-09-10' 
AND A.DmSanPhamREF=@DmSanPhamREF 
AND A.username = @username
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A.username, A.IsNoiBo
------------------------DuLieuVeNhanHangAll----------------------------
SELECT 'ThucChayAdmarket_Viewplus_NhanHang_All' [ThucChayAdmarket_Viewplus_NhanHang_All], A.username, A.DmSanPhamREF, A.TenSanPham, A.dmnhanhang_id	,  isnull(nh.TenNhanHang,0)
	--, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	--, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(convert(float,A.[money]))/1.1) tienchinh,SUM(convert(float,A.[money])) tienchinhvat
	, SUM(convert(float,A.promotion))/1.1 tienkm
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM dbo.ThucChayAdmarket_Viewplus_NhanHang A	 inner join HopDong hd on hd.SoHopDong = A.contract_number	 
left join [asd14].BRAND.dbo.DmNhanHang nh on nh.DmNhanHangID	= A.dmnhanhang_id
WHERE A.NgayThucHien <= @ngaythuchien AND A.DmSanPhamREF=@DmSanPhamREF 
	AND A.username = @username
	And hd.HopDongID = @HopDongID
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A.username, A.IsNoiBo, A.DmSanPhamREF, A.TenSanPham,  A.dmnhanhang_id ,  nh.TenNhanHang
--Kiem tra du lieu lay ve-----------------
--------------ThucChayDaTinhAdmarket-----------------------------
SELECT 'ThucChayDaTinhAdmarket'[ThucChayDaTinhAdmarket],
	ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0) TongTien 
	, SUM(tcdta.ThanhTienKM) ThanhTienKM	
FROM ThucChayDaTinhAdmarket tcdta 
WHERE tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
FROM HopDongChiTiet AS hdct WHERE hdct.DmSanPhamREF = @DmSanPhamREF 
	 AND hdct.TK_AdMarket = @username
	 AND convert(date,hdct.CreatedAt) <= @ngaythuchien
	 AND hdct.DeletedStatus <>1)
	 AND tcdta.NgayThucHien <=@ngaythuchien

SELECT 'ThucChayDaTinhAdmarket'[ThucChayDaTinhAdmarket],
	dbo.FormatNumber(ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0)) TongTienNew
	,SUM(tcdta.SoLuongThucChay) SoLuongThucChay
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
	
	 

----------Chi tiet thuc chay và hop dong 
SELECT HD.HopDongID, HD.HopDongChiTietID, HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt, HD.ThanhTien, HD.TenNhanVien, TC.DonViTinh
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
		,(CASE WHEN GiaTriHopDong <>0 then(SUM(hdct.ThanhTien*1.1))/(hd.GiaTriHopDong)*100 ELSE 0 END) AS Tyle	
		--, (SUM(hdct.ThanhTien*1.1))/(hd.GiaTriHopDong)*100 AS Tyle
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

GROUP BY HD.HopDongID,HD.HopDongChiTietID, HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt, HD.ThanhTien, HD.TenNhanVien, TC.DonViTinh
	, TC.NgayThucHienMin
	, TC.NgayThucHienMax	,
	 TC.SL, TC.TienThucChay

       
	   end
```
