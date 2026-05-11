# Stored Procedure: `CheckAdmarketByUserName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-15 17:33:45.790000
- **Ngày sửa cuối**: 2017-02-15 17:33:45.790000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@username` | `nvarchar(100)` | No |
| `@HopDongID` | `int(4)` | No |
| `@ngaythuchien` | `datetime(8)` | No |
| `@ngaythuchien1` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE CheckAdmarketByUserName
	-- Add the parameters for the stored procedure here
	 @username      NVARCHAR(50), 
 @HopDongID INT,
 @ngaythuchien  DATETIME,
 @ngaythuchien1 DATETIME
AS
BEGIN
	DECLARE @DmSanPhamREF  INT
	SET @DmSanPhamREF = 144
-----***Tien Nap Dau Ngay***--------
SELECT 'Balance' [Balance],
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
ORDER BY abud.NgayThucHien desc
-----***Lan Nap Cuoi cung***--------
SELECT  'LastRecharge' [LastRecharge],
       abud.UserName,
       abud.DmSanPhamREF,
       abud.TenSanPham,
       abud.LastDateRecharge, dbo.FormatNumber(abud.RechargeMoney)RechargeMoney
FROM   AdmarketUserLastRecharge abud
WHERE  UserName = @username
       AND DmSanPhamREF = @DmSanPhamREF
ORDER BY
       abud.LastDateRecharge DESC
 
-----------------------------
SELECT HopDongChiTietID, NhanHang,DanhSachNhanHangREF, NgayDanhSoHopDong, TenKhachHang, TenNhanVien 
FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
ON HopDongID = HopDongFK
WHERE  HopDongFK = @HopDongID AND DmSanPhamREF = @DmSanPhamREF AND TK_AdMarket = @username
AND hdct.DeletedStatus <> 1
SELECT tcdt.ThucChayDaTinhID,NgayDanhSoHopDong, TenKhachHang, TenNhanVien, NhanHang,NhanHopDong,
tcdt.SoHopDong,
       tcdt.HopDongID,
       tcdt.HopDongChiTietREF,
       tcdt.NgayThucHien,
       tcdt.SoLuongThucChay,
       tcdt.SoLuongThayDoi,
       tcdt.ThanhTienSauTrietKhauThucChay,
       tcdt.GiaTriThayDoi,
       tcdt.CreatedAt,
       tcdt.LastModifiedAt, tcdt.DmViTriREF,
       tcdt.TenViTri, tcdt.GhiChu, tcdt.TongViewThucChay, tcdt.TongClickThucChay
FROM   ThucChayDaTinhAdmarket tcdt
WHERE  tcdt.HopDongID = @HopDongID
		AND tcdt.HopDongChiTietREF IN (SELECT HopDongChiTietID FROM HopDongChiTiet hdct WHERE tcdt.HopDongID = @HopDongID AND hdct.TK_AdMarket = @username AND hdct.DeletedStatus <> 1)
       AND tcdt.DmSanPhamREF = 144
       --AND tcdt.NgayThucHien <= @Ngaythuchien
      -- AND TrangThaiHopDong <> 3
ORDER BY  tcdt.NgayThucHien,
       tcdt.HopDongChiTietREF,      
       tcdt.CreatedAt

SELECT 'DuLieuLayVe Ngay' [DuLieuLayVe],
       A.username,
       A.TenSanPham,
       SUM(CONVERT(BIGINT, A.ttv)) AS ttv,
       SUM(CONVERT(BIGINT, A.ttc)) AS ttc,
       dbo.FormatNumber(SUM(A.[money]) / 1.1) tienchinh,
       SUM(A.pro) / 1.1 tienkm,
       MAX(A.NgayThucHien)NgayThucHienMax,
       MIN(A.NgayThucHien)NgayThucHienMin,
       A.IsNoiBo
FROM   ThucChayAdmarketUsers A
WHERE 1=1 AND A.NgayThucHien = @ngaythuchien
       AND A.DmSanPhamREF = @DmSanPhamREF
       AND A.username = @username
           --AND A.NgayThucHien <> '2014-06-20'
GROUP BY
       A.username,
       A.IsNoiBo,
       A.TenSanPham,
       A.NgayThucHien
ORDER BY A.NgayThucHien
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
SELECT 'DuLieuLayVe All' [DuLieuLayVe],
       A.username, userid,
       A.TenSanPham,
       SUM(CONVERT(BIGINT, A.ttv)) AS ttv,
       SUM(CONVERT(BIGINT, A.ttc)) AS ttc,
       dbo.FormatNumber(SUM(A.[money]) / 1.1) tienchinh,
       SUM(A.pro) / 1.1 tienkm,
        dbo.FormatNumber(SUM(A.[money] + A.pro)) tienVAT,
        
          dbo.FormatNumber(SUM(A.[money])) tienchinhVAT,
       dbo.FormatNumber(SUM(A.pro)) tienkmVAT,
       MAX(A.NgayThucHien)NgayThucHienMax,
       MIN(A.NgayThucHien)NgayThucHienMin,
       A.IsNoiBo
FROM   ThucChayAdmarketUsers A
WHERE  A.NgayThucHien  BETWEEN @ngaythuchien1 AND @ngaythuchien
       AND A.DmSanPhamREF = @DmSanPhamREF
       AND A.username = @username
           --AND A.NgayThucHien <> '2014-06-20'
GROUP BY
       A.username,userid,
       A.IsNoiBo,
       A.TenSanPham
--Kiem tra du lieu lay ve bang nhan hang all-----------------
SELECT 'DuLieuLayVeNhanHangAll' DuLieuLayVeNhanHang, A.username, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang
	, SUM(CONVERT(BIGINT, A.ttv)) AS ttv
	, SUM(CONVERT(BIGINT, A.ttc)) AS ttc
	
	, dbo.FormatNumber( SUM(A.[money])/1.1) tienchinh,SUM(A.[money]) tienchinhvat
	, SUM(A.pro)/1.1 tienkm
	, MAX(A.NgayThucHien)NgayThucHienMax, MIN(A.NgayThucHien)NgayThucHienMin
	, A.IsNoiBo
FROM dbo.ThucChayAdmarketUser_NhanHang A
WHERE A.NgayThucHien BETWEEN @ngaythuchien1 AND @ngaythuchien AND A.DmSanPhamREF=@DmSanPhamREF 
	AND A.username = @username
	--AND A.NgayThucHien <> '2014-06-20'
GROUP BY A.username, A.IsNoiBo, A.DmSanPhamREF, A.TenSanPham, A.DmNhanHangREF, A.TenNhanHang
--Kiem tra du lieu lay ve-----------------
--Du lieu bang ThucChayAdmarke
SELECT tcao.ThucChayDaTinhID,
       tcao.NgayThucHien,
       tcao.DmSanPhamREF,
       tcao.TenSanPham, NhanHang,
       ThanhTienSauTrietKhauThucChay, GiaTriThayDoi,
       (ThanhTienSauTrietKhauThucChay+GiaTriThayDoi)ttc, GhiChu

FROM   ThucChayDaTinhAdmarket tcao
WHERE  1 = 1
       AND tcao.NgayThucHien=@ngaythuchien
       AND tcao.DmSanPhamREF = 144
       AND HopDongID = @HopDongID
       
       
       
--ThucChay Từ 2014
SELECT  A.TenMaHopDong, dbo.FormatNumber(sum(A.TongTienNew)) TongTien2014, sum(A.ThanhTienKM)ThanhTienKM FROM (
SELECT  (CASE WHEN tcdta.TenMaHopDong IN ('NB','NBDT','SH') THEN 'NB' ELSE 'QC' END) TenMaHopDong,
           ROUND(
               SUM(tcdta.ThanhTienSauTrietKhauThucChay + tcdta.GiaTriThayDoi),
               0)TongTienNew,
       SUM(tcdta.SoLuongThucChay)SoLuongThucChay,
       SUM(tcdta.ThanhTienKM) ThanhTienKM
FROM   ThucChayDaTinhAdmarket tcdta

WHERE  (tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                   FROM   HopDongChiTiet AS hdct
                                          INNER JOIN HopDong hd
                                               ON  hdct.HopDongFK = hd.HopDongID
                                   WHERE  hdct.DmSanPhamREF = @DmSanPhamREF
                                          AND hdct.TK_AdMarket = @username                                         
                                         -- AND CONVERT(date, hdct.CreatedAt) <= @ngaythuchien
                                          AND hdct.DeletedStatus <> 1                                        
                                        --  AND hd.Nam > 2013
                                          )
                                 
       AND tcdta.NgayThucHien <=  @ngaythuchien
			)
		Group BY TenMaHopDong
)A 
GROUP BY  A.TenMaHopDong
-----------------------Hd - Nhan hang-----------------
SELECT A.NhanHang, A.TenMaHopDong, dbo.FormatNumber(sum(A.TongTienNew)) TongTien2014, sum(A.ThanhTienKM)ThanhTienKM FROM (
SELECT Nhanhang, (CASE WHEN tcdta.TenMaHopDong IN ('NB','NBDT','SH') THEN 'NB' ELSE 'QC' END) TenMaHopDong,
           ROUND(
               SUM(tcdta.ThanhTienSauTrietKhauThucChay + tcdta.GiaTriThayDoi),
               0)TongTienNew,
       SUM(tcdta.SoLuongThucChay)SoLuongThucChay,
       SUM(tcdta.ThanhTienKM) ThanhTienKM
FROM   ThucChayDaTinhAdmarket tcdta

WHERE  (tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                   FROM   HopDongChiTiet AS hdct
                                          INNER JOIN HopDong hd
                                               ON  hdct.HopDongFK = hd.HopDongID
                                   WHERE  hdct.DmSanPhamREF = @DmSanPhamREF
                                          AND hdct.TK_AdMarket = @username                                         
                                         -- AND CONVERT(date, hdct.CreatedAt) <= @ngaythuchien
                                          AND hdct.DeletedStatus <> 1                                        
                                        --  AND hd.Nam > 2013
                                          )
                                 
       AND tcdta.NgayThucHien <=  @ngaythuchien
			)
		Group BY tcdta.NhanHang, TenMaHopDong
)A 
GROUP BY A.TenMaHopDong, A.NhanHang
--

--ThucChay 2013
SELECT A.TenMaHopDong, dbo.FormatNumber(sum(A.TongTienNew)) TongTien2013, sum(A.ThanhTienKM)ThanhTienKM FROM (
SELECT (CASE WHEN tcdta.TenMaHopDong IN ('NB','NBDT','SH') THEN 'NB' ELSE 'QC' END) TenMaHopDong,
           ROUND(
               SUM(tcdta.ThanhTienSauTrietKhauThucChay + tcdta.GiaTriThayDoi),
               0)TongTienNew,
       SUM(tcdta.SoLuongThucChay)SoLuongThucChay,
       SUM(tcdta.ThanhTienKM) ThanhTienKM
FROM   ThucChayDaTinhAdmarket tcdta
WHERE  (tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                   FROM   HopDongChiTiet AS hdct
                                          INNER JOIN HopDong hd
                                               ON  hdct.HopDongFK = hd.HopDongID
                                   WHERE  hdct.DmSanPhamREF = @DmSanPhamREF
                                          AND hdct.TK_AdMarket = @username
                                         -- AND hd.NgayDanhSoHopDong >= 
                                             -- '2013-01-01'
                                          AND CONVERT(date, hdct.CreatedAt) <= @ngaythuchien
                                          AND hdct.DeletedStatus <> 1                                        
                                          AND hd.Nam <= 2013
										  )
                                 
      -- AND tcdta.NgayThucHien BETWEEN '2013-01-01' AND  @ngaythuchien
			)
		Group by TenMaHopDong
)A 
GROUP BY A.TenMaHopDong
--

SELECT  HD.HopDongID, HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt,nhanhang, dbo.FormatNumber(HD.ThanhTien) ThanhTien, HD.TenNhanVien,HD.TenKhachHang,
    
       TC.NgayThucHienMax,
       TC.NgayThucHienMin,
       TC.SoLuongChay,
       TC.SLKM,     
       TC.ThanhTienKM,
		dbo.FormatNumber(TC.TienThucChay)TienThucChay,
	 dbo.FormatNumber(ISNULL(SUM((TV.TienVe * HD.Tyle)/100),0))TienVe
    ,dbo.FormatNumber(ROUND((ISNULL(SUM((TV.TienVe * HD.Tyle)/100),0) -TC.TienThucChay),0)) AS [TienVe - ThucChay],
       dbo.FormatNumber((HD.ThanhTien -TC.TienThucChay)) [ThanhTien - ThucChay]
FROM   (
           SELECT tcdta.SoHopDong,
                  tcdta.HopDongID,
                  tcdta.HopDongChiTietREF,
                  MAX(tcdta.NgayThucHien)NgayThucHienMax,
                  MIN(tcdta.NgayThucHien)NgayThucHienMin,
                  SUM(tcdta.SoLuongThucChay + tcdta.SoLuongThayDoi) AS 
                  SoLuongChay,
                  SUM(tcdta.SoLuongThucChayKM) AS SLKM,
                  ROUND(
                      SUM(tcdta.ThanhTienSauTrietKhauThucChay + tcdta.GiaTriThayDoi),
                      0
                  ) AS TienThucChay,
                  SUM(tcdta.ThanhTienKM) ThanhTienKM
           FROM   ThucChayDaTinhAdmarket tcdta
           WHERE  1 = 1
                  AND tcdta.NgayThucHien <= @ngaythuchien
                  --AND tcdta.NgayThucHien >='2014-01-01'
                  AND tcdta.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
                                                  FROM   HopDong hd
                                                         INNER JOIN 
                                                              HopDongChiTiet 
                                                              hdct
                                                              ON  hd.HopDongID = 
                                                                  hdct.HopDongFK
                                                              --AND hd.TrangThaiHopDong 
                                                              --    <> 3
                                                              AND hdct.DeletedStatus = 
                                                                  0
                                                              AND hdct.DmSanPhamREF = 
                                                                  @DmSanPhamREF
                                                              AND hdct.TK_AdMarket = 
                                                                  @username)
                                                                  --AND tcdta.Nam>=2013
           GROUP BY
                  tcdta.SoHopDong,
                  tcdta.HopDongID,
                  tcdta.HopDongChiTietREF
       ) TC
       FULL OUTER JOIN (
               SELECT hd.HopDongID , hd.TenNhanVien, hd.TenKhachHang
		, hd.SoHopDong, hdct.HopDongChiTietID
		, CASE WHEN hd.TrangThaiHopDong = 3 THEN 0 ELSE SUM(hdct.ThanhTien) END ThanhTien		
		, (CASE WHEN hd.GiaTriHopDong<> 0 then(SUM(hdct.ThanhTien*1.1))/(hd.GiaTriHopDong)*100 ELSE 0 END) AS Tyle
		, hdct.TK_AdMarket, hdct.CreatedAt, NhanHang
                FROM   HopDong hd
                       INNER JOIN HopDongChiTiet hdct
                            ON  hd.HopDongID = hdct.HopDongFK
                WHERE  hdct.TK_AdMarket = @username
                       AND hdct.DeletedStatus = 0
                       AND hdct.DmSanPhamREF = @DmSanPhamREF
                      -- AND hd.Nam >=2013
                GROUP BY
                       hd.HopDongID,
                       hd.SoHopDong,
                       hdct.TK_AdMarket,
                       hdct.CreatedAt,
                       hd.TenNhanVien,
                       hd.TrangThaiHopDong, hd.GiaTriHopDong, hdct.HopDongChiTietID, HDct.NhanHang, hd.TenKhachHang
            ) HD
            ON  HD.SoHopDong = TC.SoHopDong
            AND TC.HopDongChiTietREF = HD.HopDongChiTietID
       FULL OUTER JOIN (
                SELECT tttv.HopDongREF,
                       ROUND(SUM(tttv.GiaTri) / 1.1, 0) AS TienVe
                FROM   ThongTinTienVe tttv
                WHERE  tttv.HopDongREF IN (SELECT hd2.HopDongID
                                           FROM   HopDong hd2
                                                  INNER JOIN HopDongChiTiet 
                                                       hdct2
                                                       ON  hd2.HopDongID = hdct2.HopDongFK
                                                       AND hdct2.TK_AdMarket = @username
                                                       AND hdct2.DmSanPhamREF = 
                                                           @DmSanPhamREF
                                                       --AND hd2.TrangThaiHopDong 
                                                       --    <> 3
                                                       AND hdct2.DeletedStatus = 
                                                           0
                                                      
														--AND hd2.Nam >=2012
														)
                       AND tttv.DeletedStatus = 0
                      -- AND HopDongREF = @HopDongID
                GROUP BY
                       tttv.HopDongREF
            ) TV
            ON  HD.HopDongID = TV.HopDongREF
--WHERE HD.HopDongID =28743
GROUP BY  HD.HopDongID, HD.SoHopDong, HD.TK_AdMarket, HD.CreatedAt, HD.ThanhTien, HD.TenNhanVien,nhanhang, hd.TenKhachHang
,  TC.NgayThucHienMax,
       TC.NgayThucHienMin,
       TC.SoLuongChay,
       TC.SLKM,     
       TC.ThanhTienKM,TC.TienThucChay
ORDER BY
       HD.CreatedAt
END

```
