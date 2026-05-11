# Stored Procedure: `Script_Check_ADX_Detail_ByUser`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-05 11:18:38.063000
- **Ngày sửa cuối**: 2021-03-09 17:31:26.407000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@username` | `nvarchar(100)` | No |
| `@nth1` | `datetime(8)` | No |
| `@nth2` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--Script_Check_ADX_Detail_ByUser 'quocanh','2013-01-01','2020-12-30',585,NULL
CREATE proc [dbo].[Script_Check_ADX_Detail_ByUser]
@username NVARCHAR(50) ,
@nth1 DATETIME,
@nth2 DATETIME,
@DmSanPhamREF INT,
@HopDongID INT
as
begin
  
-----------HopDong ------------ THONG TIN HOP DONG
 SELECT HopDongChiTietID,thanhtien, NhanHopDong,NhanHang,DanhSachNhanHangREF, NgayDanhSoHopDong, TenKhachHang, TenNhanVien 
FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
ON HopDongID = HopDongFK
WHERE  HopDongFK = @HopDongID AND DmSanPhamREF = @DmSanPhamREF AND TK_AdMarket = @username
AND hdct.DeletedStatus <> 1

-----------ThucChayDaTinh----------------THONG TIN THUC CHAY DA TINH THEO HOP DONG
 SELECT tcdt.ThucChayDaTinhID, tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF,NhanHopDong,
 NhanHang, NgayDanhSoHopDong, TenKhachHang, TenNhanVien ,
  convert(Date,tcdt.NgayThucHien)NgayThucHien,
  tcdt.SoLuongThucChay,tcdt.SoLuongThayDoi, tcdt.ThanhTienSauTrietKhauThucChay,
   tcdt.GiaTriThayDoi, tcdt.DmViTriREF, tcdt.TenViTri, tcdt.GhiChu,tcdt.CreatedAt
   FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID =  @HopDongID AND tcdt.DmSanPhamREF = 585-- AND tcdt.NgayThucHien >='2015-05-14'
   AND TrangThaiHopDong <> 3
   and DmHinhThucQuangCao <> 42
    --AND tcdt.HopDongChiTietREF = 96250
   AND HopDongChiTietREF IN (SELECT HopDongChiTietID FROM dbo.HopDongChiTiet WHERE TK_AdMarket = @username AND HopDongFK = @HopDongID)
 ORDER BY tcdt.NgayThucHien, HopDongChiTietREF, tcdt.CreatedAt

-- ----------------
--    SELECT 'ThucChayAdmarket_CPC_ADX_HopDOng', tcdta1.username,user_id, tcdta1.TenViTri, tcdta1.DmViTriREF
----, SUM(ttc) ttc, SUM(ttv) ttv
--, MIN(tcdta1.NgayThucHien) AS TuNgay , MAX(tcdta1.NgayThucHien) NgayThucHienMax
--,sum(CONVERT(FLOAT,tcdta1.domain_tt_money)+ convert(float,tcdta1.domain_tt_promotion)) TienAllVAT
-- ,dbo.FormatNumber(SUM(CONVERT(FLOAT,tcdta1.domain_tt_money))) AS TienChinh_VAT
--, dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT,tcdta1.domain_tt_money)/1.1),0)) AS TienChinh_ChuaVAT
--, ROUND(SUM(CONVERT(FLOAT,tcdta1.domain_tt_promotion))/1.1,0) AS TienKM_ChuaVAT
--, tcdta1.IsNoiBo--, NgayThucHien
-- FROM ThucChayAdmarket_ADX_CPC_HopDong tcdta1   inner join HopDong hd on hd.SoHopDong = tcdta1.contract_number
--WHERE tcdta1.NgayThucHien = @nth2 AND tcdta1.DmSanPhamREF=585 AND tcdta1.username = @username and hd.HopDongID = @HopDongID
--GROUP BY tcdta1.username ,user_id, tcdta1.TenViTri, tcdta1.IsNoiBo , tcdta1.DmViTriREF--, tcdta.NgayThucHien
--ORDER BY tcdta1.DmViTriREF--, NgayThucHien-- desc

 -----ThucChayAdmarket_CPC_ADX_HopDOng_new --THONG TIN THUC CHAY CUA TK THEO THOI GIAN -> TONG THUC CHAY THEO TAI KHOAN
   SELECT 'ThucChayAdmarket_CPC_ADX_HopDOng_All', tcdta1.username,user_id, tcdta1.TenViTri, tcdta1.DmViTriREF
--, SUM(ttc) ttc, SUM(ttv) ttv
, MIN(tcdta1.NgayThucHien) AS TuNgay , MAX(tcdta1.NgayThucHien) NgayThucHienMax
 ,dbo.FormatNumber(SUM(CONVERT(FLOAT,tcdta1.domain_tt_money))) AS TienChinh_VAT
, dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT,tcdta1.domain_tt_money)/1.1),0)) AS TienChinh_ChuaVAT
,sum(CONVERT(FLOAT,tcdta1.domain_tt_money)+ convert(float,tcdta1.domain_tt_promotion)) TienAllVAT
, ROUND(SUM(CONVERT(FLOAT,tcdta1.domain_tt_promotion))/1.1,0) AS TienKM_ChuaVAT
, tcdta1.IsNoiBo--, NgayThucHien
FROM ThucChayAdmarket_ADX_CPC_HopDong tcdta1   inner join HopDong hd on hd.SoHopDong = tcdta1.contract_number
WHERE tcdta1.NgayThucHien BETWEEN @nth1 AND @nth2 AND tcdta1.DmSanPhamREF=585 AND tcdta1.username = @username and hd.HopDongID = @HopDongID
GROUP BY tcdta1.username ,user_id, tcdta1.TenViTri, tcdta1.IsNoiBo , tcdta1.DmViTriREF--, tcdta.NgayThucHien
ORDER BY tcdta1.DmViTriREF--, NgayThucHien-- desc
   SELECT 'ThucChayAdmarket_CPC_ADX_HopDOng_All_TK', tcdta1.username,user_id, tcdta1.TenViTri, tcdta1.DmViTriREF
--, SUM(ttc) ttc, SUM(ttv) ttv
, MIN(tcdta1.NgayThucHien) AS TuNgay , MAX(tcdta1.NgayThucHien) NgayThucHienMax
 ,dbo.FormatNumber(SUM(CONVERT(FLOAT,tcdta1.domain_tt_money))) AS TienChinh_VAT
, dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT,tcdta1.domain_tt_money)/1.1),0)) AS TienChinh_ChuaVAT
,sum(CONVERT(FLOAT,tcdta1.domain_tt_money)+ convert(float,tcdta1.domain_tt_promotion)) TienAllVAT
, ROUND(SUM(CONVERT(FLOAT,tcdta1.domain_tt_promotion))/1.1,0) AS TienKM_ChuaVAT
, tcdta1.IsNoiBo--, NgayThucHien
FROM ThucChayAdmarket_ADX_CPC_HopDong tcdta1 
WHERE tcdta1.NgayThucHien BETWEEN '2017-09-11' AND @nth2 AND tcdta1.DmSanPhamREF=585 AND tcdta1.username = @username 
GROUP BY tcdta1.username ,user_id, tcdta1.TenViTri, tcdta1.IsNoiBo , tcdta1.DmViTriREF--, tcdta.NgayThucHien
ORDER BY tcdta1.DmViTriREF--, NgayThucHien-- desc
 

--ThucChayAdXforUsersAll 
SELECT 'ThucChayAdXforUsersAll', tcdta.username,userid, tcdta.TenViTri, tcdta.DmViTriREF
--, SUM(ttc) ttc, SUM(ttv) ttv
, MIN(tcdta.NgayThucHien) AS TuNgay , MAX(tcdta.NgayThucHien) NgayThucHienMax	   
 ,dbo.FormatNumber(SUM(CONVERT(FLOAT,tcdta.[money]))) AS TienChinh_VAT
, dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT,tcdta.[money])/1.1),0)) AS TienChinh_ChuaVAT,sum(CONVERT(FLOAT,tcdta.[money]+tcdta.pro)) TienAllVAT
, ROUND(SUM(CONVERT(FLOAT,tcdta.pro/1.1)),0) AS TienKM_ChuaVAT
, tcdta.IsNoiBo--, NgayThucHien
FROM ThucChayAdXforUsers tcdta 
WHERE tcdta.NgayThucHien BETWEEN @nth1 AND '2017-09-10' AND tcdta.DmSanPhamREF=585 AND tcdta.username = @username
GROUP BY tcdta.username ,userid, tcdta.TenViTri, tcdta.IsNoiBo , tcdta.DmViTriREF--, tcdta.NgayThucHien
ORDER BY DmViTriREF--, NgayThucHien-- desc


----Kiem tra du lieu lay ve bang nhan hang-----------------
--SELECT 'ThucChayAdmarket_ADX_CPC_NhanHang' [ThucChayAdmarket_ADX_CPC_NhanHang], A.username, A.dmnhanhang_id, A.TenSanPham
--	--, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
--	--, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
--	, dbo.FormatNumber( SUM(convert(float,A.[money]))/1.1) tienchinh,SUM(convert(float,A.[money])) tienchinhvat
--	, SUM(convert(float,A.promotion))/1.1 tienkm
--	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
--	, A.is_noibo
--FROM dbo.ThucChayAdmarket_ADX_CPC_NhanHang A	inner join HopDong hd on hd.SoHopDong = A.contract_number
--WHERE CONVERT(DATE,A.NgayThucHien) = @nth2 AND A.DmSanPhamREF=@DmSanPhamREF 
--	AND A.username = @username
--	and hd.HopDongID = @HopDongID
--GROUP BY A.username, A.is_noibo, A.DmSanPhamREF, A.TenSanPham , A.dmnhanhang_id

----Nhanhangall

--SELECT 'ThucChayAdmarket_ADX_CPC_NhanHang_All' [ThucChayAdmarket_ADX_CPC_NhanHang_All], A.username, A.dmnhanhang_id,isnull(nh.TenNhanHang,0), A.TenSanPham
--	, SUM(CONVERT(BIGINT, A.Total_view)) AS ttv
--	, SUM(CONVERT(BIGINT, A.Total_click)) AS ttc
	
--	, dbo.FormatNumber( SUM(convert(float,A.[money]))/1.1) tienchinh,SUM(convert(float,A.[money])) tienchinhvat
--	, SUM(convert(float,A.promotion))/1.1 tienkm
--	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
--	, A.is_noibo
--FROM dbo.ThucChayAdmarket_ADX_CPC_NhanHang A	inner join HopDong hd on hd.SoHopDong = A.contract_number	 left join [asd14].BRAND.dbo.DmNhanHang nh on nh.DmNhanHangID	= A.dmnhanhang_id
--WHERE CONVERT(DATE,A.NgayThucHien) <= @nth2 AND A.DmSanPhamREF=@DmSanPhamREF 
--	AND A.username = @username
--	and hd.HopDongID = @HopDongID
--GROUP BY A.username, A.is_noibo, A.DmSanPhamREF, A.TenSanPham , A.dmnhanhang_id	, nh.TenNhanHang

----ThucChayAdXforUsers
--SELECT 'ThucChayAdXforUsers', tcdta.username, tcdta.DmViTriREF, tcdta.TenViTri
--, SUM(ttc) ttc, SUM(ttv) ttv
--, MIN(tcdta.NgayThucHien) AS TuNgay , MAX(tcdta.NgayThucHien) NgayThucHienMax
--, dbo.FormatNumber(ROUND(SUM(tcdta.[money])/1.1,0)) AS TienChinh_ChuaVAT ,SUM(tcdta.[money]+tcdta.pro) tienchinh
--, ROUND(SUM(tcdta.pro/1.1),0) AS TienKM_ChuaVAT, tcdta.IsNoiBo
--FROM ThucChayAdXforUsers tcdta 
--WHERE tcdta.NgayThucHien = @nth2 AND tcdta.DmSanPhamREF=585 AND tcdta.username = @username
--GROUP BY tcdta.username , tcdta.TenViTri , tcdta.IsNoiBo, tcdta.DmViTriREF

  
--SELECT tcdta.SoHopDong, tcdta.HopDongChiTietREF, DmViTriREF
--	,tcdta.TenSanpham
--	, tcdta.ThanhTien
--	, SUM(tcdta.TongViewThucChay)TongViewThucChay,SUM( tcdta.SoLuongThucChay)SoLuongThucChay
--	, SUM(tcdta.ThanhTienSauTrietKhauThucChay)ThanhTienSauTrietKhauThucChay
--	, SUM(tcdta.GiaTriThayDoi)GiaTriThayDoi
--	, sum(tcdta.SoLuongThayDoi)SoLuongThayDoi, SUM(tcdta.ThanhTienKM)ThanhTienKM
--	, tcdta.NgayThucHien
--FROM ThucChayDaTinhAdmarket tcdta 
--WHERE tcdta.NgayThucHien = @nth2 AND DmSanPhamREF = 585
-- and DmHinhThucQuangCao <> 42
--	AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID 
--										FROM HopDongChiTiet AS hdct 
--										WHERE hdct.DmSanPhamREF = 585 AND hdct.TK_AdMarket <> ''
--											AND hdct.TK_AdMarket = @username
--											 and DmHinhThucQuangCao <> 42
--	--AND convert(date,hdct.CreatedAt) <= @ngaythuchien
--	AND hdct.DeletedStatus <>1)
--	GROUP BY tcdta.SoHopDong, tcdta.HopDongChiTietREF, DmViTriREF
--	,tcdta.TenSanpham
--	, tcdta.ThanhTien, tcdta.NgayThucHien

 --SELECT A.TenMaHopDong, 
 -- dbo.FormatNumber (SUM(A.TienThucChay_GTTD)*1.1)TienThucChay_VAT,
 --dbo.FormatNumber (SUM(A.TienThucChay_GTTD))TienThucChay_GTTD, 

 --SUM(A.SoLuongTC)sltc,A.DmViTriREF, A.TenViTri--, A.HopDongChiTietREF
 --FROM (
 --SELECT CASE WHEN TenMaHopDong IN ('NB','SH','NBDT')  THEN 'NB' ELSE 'QC' END TenMaHopDong,
 --ROUND(sum(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0) TienThucChay_GTTD,
 --SUM(tcdta.SoLuongThucChay+tcdta.SoLuongThayDoi)SoLuongTC
 --, tcdta.DmViTriREF, tcdta.TenViTri--, HopDongChiTietREF
 --, sum(tcdta.ThanhTienKM) ThanhTienKM
 --  FROM ThucChayDaTinhAdmarket tcdta 
 --WHERE 1=1
	-- AND tcdta.NgayThucHien BETWEEN @nth1 AND @nth2
	-- AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
 --FROM HopDongChiTiet AS hdct WHERE hdct.DmSanPhamREF = 585 AND hdct.TK_AdMarket <> ''
 -- and DmHinhThucQuangCao <> 42
 --AND hdct.TK_AdMarket = @username
 ----AND convert(date,hdct.CreatedAt) <= @ngaythuchien
 --AND hdct.DeletedStatus <>1)
 --GROUP BY tcdta.DmViTriREF, tcdta.TenViTri, TenMaHopDong--,HopDongChiTietREF
 --)A
 --GROUP BY  A.TenMaHopDong,A.DmViTriREF, A.TenViTri--, A.HopDongChiTietREF
 
 -----Du lieu tcdt theo vi tri--------------------------------
 -- SELECT A.TenMaHopDong,A.NhanHang,  dbo.FormatNumber (SUM(A.TienThucChay_GTTD))TienThucChay_GTTD, SUM(A.SoLuongTC)sltc,A.DmViTriREF, A.TenViTri 
 -- FROM (
 --SELECT CASE WHEN TenMaHopDong IN ('NB','SH','NBDT')  THEN 'NB' ELSE 'QC' END TenMaHopDong,Nhanhang,
 --ROUND(sum(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0) TienThucChay_GTTD
 --,SUM(tcdta.SoLuongThucChay+tcdta.SoLuongThayDoi)SoLuongTC
 --, tcdta.DmViTriREF, tcdta.TenViTri
 --, sum(tcdta.ThanhTienKM) ThanhTienKM
 --  FROM ThucChayDaTinhAdmarket tcdta 
 --WHERE 1=1
	-- AND tcdta.NgayThucHien BETWEEN @nth1 AND @nth2
	--  and DmHinhThucQuangCao <> 42
	-- AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
 --FROM HopDongChiTiet AS hdct WHERE hdct.DmSanPhamREF = 585 AND hdct.TK_AdMarket <> ''
 --AND hdct.TK_AdMarket = @username
 ----AND convert(date,hdct.CreatedAt) <= @ngaythuchien
 --AND hdct.DeletedStatus <>1)
 --GROUP BY tcdta.DmViTriREF, tcdta.TenViTri, TenMaHopDong,tcdta.NhanHang
 --)A
 --GROUP BY  A.TenMaHopDong,A.DmViTriREF, A.TenViTri,A.NhanHang
 --ORDER BY A.DmViTriREF--,  CONVERT(INT,A.NhanHang)


----------Chi tiet thuc chay và hop dong ---------------------------------------
--SELECT HD.HopDongID,HD.Hopdongchitietid,TC.tenhinhthucquangcao, HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt,HD.LastModifiedAt, HD.ThanhTien,HD.DonGia,Hd.ChietKhau, HD.TenNhanVien,HD.TenKhachHang, TC.DonViTinh
--	, TC.NgayThucHienMin
--	, TC.NgayThucHienMax	
--	, TC.SL, dbo.FormatNumber(TC.TienThucChay)TienThucChay,
--	 ISNULL(SUM((TV.TienVe * HD.Tyle)/100),0)TienVe
--    ,ROUND((ISNULL(SUM((TV.TienVe * HD.Tyle)/100),0) -TC.TienThucChay),0) AS [TienVe - ThucChay],
--       (HD.ThanhTien -TC.TienThucChay) [ThanhTien - ThucChay]
--FROM
--(
--	SELECT tcdta.HopDongID, tcdta.SoHopDong,(CASE WHEN tcdta.DonViTinh = 'CLICK' THEN 'CPC' ELSE tcdta.DonViTinh END)DonViTinh, tcdta.HopDongChiTietREF	 , tenhinhthucquangcao
--		, MIN(tcdta.NgayThucHien) NgayThucHienMin 
--		, MAX(tcdta.NgayThucHien) NgayThucHienMax
--		, SUM(tcdta.SoLuongThucChay+tcdta.SoLuongThayDoi) AS SL
--		, ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay),0) ThanhTienThucChay 
--		, ROUND(SUM(tcdta.GiaTriThayDoi),0) GiaTriThayDoi
--		, ROUND(SUM(tcdta.ThanhTienSauTrietKhauThucChay+tcdta.GiaTriThayDoi),0) TienThucChay
--		, SUM(tcdta.ThanhTienKM) ThanhTienKM
--	FROM ThucChayDaTinhAdmarket tcdta 
--	WHERE 1=1
--		AND tcdta.NgayThucHien BETWEEN @nth1 AND @nth2
--		AND DmSanPhamREF = 585
--		 and DmHinhThucQuangCao <> 42
--		AND tcdta.HopDongChiTietREF IN (
--							SELECT hdct.HopDongChiTietID
--							FROM HopDongChiTiet AS hdct WHERE hdct.DmSanPhamREF = 585
--								AND hdct.TK_AdMarket = @username
--								--AND convert(date,hdct.CreatedAt) <= @ngaythuchien
--								--AND hdct.DeletedStatus <>1
--								 and DmHinhThucQuangCao <> 42
--						)
--	GROUP BY tcdta.SoHopDong, tcdta.HopDongID, tcdta.DonViTinh, tcdta.HopDongChiTietREF	   , tenhinhthucquangcao
--) TC FULL OUTER JOIN
--(
--	SELECT hd.HopDongID , hd.TenNhanVien,hd.TenKhachHang, hdct.HopDongChiTietID
--		, hd.SoHopDong, DonGia,ChietKhau
--		, CASE WHEN hd.TrangThaiHopDong = 3 THEN 0 ELSE SUM(hdct.ThanhTien) END ThanhTien		
--		, (CASE WHEN GiaTriHopDong <>0 then(SUM(hdct.ThanhTien*1.1))/(hd.GiaTriHopDong)*100 ELSE 0 END) AS Tyle
--		, hdct.TK_AdMarket, hdct.CreatedAt, hdct.LastModifiedAt
--	FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK	
--	WHERE hdct.TK_AdMarket = @username 
--		AND hdct.DeletedStatus =0
--		AND hdct.DmSanPhamREF = 585
--		 and DmLoaiREF <> 42
--		--AND hdct.DmLoaiBannerREF <> 17
--	GROUP BY hd.HopDongID , TenKhachHang, DonGia,ChietKhau
--		, hd.SoHopDong, hdct.TK_AdMarket, hdct.CreatedAt, hdct.LastModifiedAt, hd.TenNhanVien,hd.TrangThaiHopDong, hd.GiaTriHopDong, hdct.ThanhTien,hdct.HopDongChiTietID
--) HD ON HD.HopDongID = TC.HopDongID AND TC.HopDongChiTietREF = HD.HopDongChiTietID
--FULL OUTER JOIN 
--(
--	SELECT tttv.HopDongREF, ROUND(SUM(tttv.GiaTri)/1.1,0) AS TienVe FROM ThongTinTienVe tttv 
--	WHERE tttv.HopDongREF IN (SELECT hd2.HopDongID
--	                         FROM HopDong hd2 INNER JOIN HopDongChiTiet hdct2 ON hd2.HopDongID = hdct2.HopDongFK
--							AND hdct2.TK_AdMarket = @username AND hdct2.DmSanPhamREF = 585
--							 and hdct2.DmLoaiREF <> 42
--							--AND hd2.TrangThaiHopDong <> 3
--							 AND hdct2.DeletedStatus = 0
--		)
--	AND tttv.DeletedStatus = 0
--	GROUP BY tttv.HopDongREF	
--) TV ON HD.HopDongID = TV.HopDongREF

--GROUP BY HD.HopDongID,HD.Hopdongchitietid,HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt,HD.LastModifiedAt, HD.ThanhTien, HD.TenNhanVien, TC.DonViTinh, HD.TenKhachHang
--	, TC.NgayThucHienMin
--	, TC.NgayThucHienMax	,
--	 TC.SL, TC.TienThucChay	 , TC.tenhinhthucquangcao,HD.DonGia,Hd.ChietKhau

--**********************RULE************
       --Check gia tri muon them dam bao rule
	   --1. gia tri them vao hop dong ko vuot qua gia tri phan bo
	   --2. gia tri them + gia tri hien tai theo tk da ghi nhan co sohhopdong <= tong gia tri thuc chay tra ve cua tai  khoan ( theo tk va format)
   end
```
