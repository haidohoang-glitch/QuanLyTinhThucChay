# Stored Procedure: `CheckViewplusDaily`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-15 17:38:06.327000
- **Ngày sửa cuối**: 2017-02-15 17:38:06.327000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHienSt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE CheckViewplusDaily
	-- Add the parameters for the stored procedure here
  @NgayThucHienSt DATETIME
AS
BEGIN
	DECLARE  @NgayThucHien DATETIME ,
 	 @DmSanPhamREF INT
	 SET @NgayThucHien =@NgayThucHienSt
	 SET @DmSanPhamREF = 628
SELECT T1.*	,T2.username,
        T2.TienThucChay_tcdt,
        T1.moneys - T2.TienThucChay_tcdt AS ChenhLech
        ,T2.TienThucChayOnline
 FROM   (
 SELECT CASE WHEN Users.username IS NULL THEN HD.TK_AdMarket ELSE Users.username END username
 			, Users.DmSanPhamREF
 			, Users.TenSanPham		
 			, Users.NgayThucHienMax	
 			, HD.ThanhTien
 			, Users.moneys			
 			FROM
 			(
 				SELECT 
 					 A.DmSanPhamREF,
 					 A.TenSanPham,
 					 A.username,
 					 --CASE WHEN A.DmSanPhamREF = 337 THEN 'VIEW' ELSE 'CLICK' END DonViTinh,
 					 MAX(A.NgayThucHien) NgayThucHienMax ,
 					 SUM(CONVERT(BIGINT, A.ttv)) AS ttv,
 					 SUM(CONVERT(BIGINT, A.ttc)) AS ttc,     
 					 --CASE A.IsNoiBo WHEN 1 THEN (A.[money] + A.pro) / 1.1 ELSE A.[money] / 1.1 END ThanhTienThucChay,
 					 --CASE A.IsNoiBo WHEN 1 THEN 0 ELSE A.pro / 1.1 END ThanhTienKM        
 					 CASE A.IsNoiBo WHEN 0 THEN ROUND(ISNULL(SUM(A.[money])/1.1,0),0) END moneys,
 					 CASE A.IsNoiBo WHEN 1 THEN ROUND(ISNULL(SUM(A.[money])/1.1,0),0) END moneys_nb,
 					 CASE A.IsNoiBo WHEN 0 THEN ROUND(ISNULL(SUM(A.pro)/1.1,0),0) END km, 
 					 CASE A.IsNoiBo WHEN 1 THEN ROUND(ISNULL(SUM(A.pro)/1.1,0),0) END km_nb     
 				FROM ThucChayViewPlusForUsers A 
 				WHERE 1=1
 					AND CAST(A.NgayThucHien AS DATE) BETWEEN @NgayThucHienSt AND @NgayThucHien                            
 					AND A.DmSanPhamREF = @DmSanPhamREF
 					--AND username = 'lazada'
 				GROUP BY 	
 					A.DmSanPhamREF,
 					A.TenSanPham,
 					A.username, 
 					A.IsNoiBo
 			) Users
 			FULL OUTER JOIN
 			(
 				SELECT T.TK_AdMarket, T.DmSanPhamREF, SUM(T.ThanhTien) ThanhTien FROM
 				(
 					SELECT hdct.TK_AdMarket, hdct.DmSanPhamREF
 						, CASE WHEN hd.TrangThaiHopDong = 3 THEN 0 ELSE SUM(hdct.ThanhTien) END ThanhTien				
 					FROM HopDongChiTiet hdct INNER JOIN HopDong hd ON hdct.HopDongFK = hd.HopDongID 
 					WHERE hdct.DmSanPhamREF = @DmSanPhamREF
 					 
 						AND hdct.DeletedStatus = 0
 							--AND hdct.TK_AdMarket = 'lazada'
 													AND hd.Tenmahopdong NOT IN ('NB','SH','NBDT')
 					GROUP BY hdct.TK_AdMarket , hdct.DmSanPhamREF, hd.TrangThaiHopDong
 				) T	GROUP BY T.TK_AdMarket, T.DmSanPhamREF
 			) HD ON Users.username = HD.TK_AdMarket AND HD.DmSanPhamREF = Users.DmSanPhamREF    
 			
 			)T1
 			
 			 FULL OUTER JOIN (
 				SELECT T.username,
 					   T.DmSanPhamREF,
 					   SUM(T.TongClickThucChay) ttc,
 					   SUM(T.TongViewThucChay) ttv,
 					   SUM(ISNULL(T.SoLuongThucChay, 0)) SoLuongThucChay,
 					   SUM(ISNULL(T.SoLuongThucChayKM, 0)) SoLuongThucChayKM,
 					   SUM(T.ThanhTienKM) AS ThanhTienKM,
 					   ROUND(SUM(T.ThanhTienSauTrietKhauThucChay),0) AS TienThucChay_tcdt,					   
 					   SUM(ISNULL(T.SoLuongThucChayOnline, 0)) SoLuongThucChayOnline,
 					   SUM(T.TienThucChayOnline) AS TienThucChayOnline,
 					   SUM(T.TienKhuyenMaiOnline) AS TienKhuyenMaiOnline,
 					   SUM( T.ThanhTienSauTrietKhauThucChay + T.ThanhTienKM + T.TienThucChayOnline + T.TienKhuyenMaiOnline ) TongTien
 				FROM   (
 						   SELECT A.DmSanPhamREF,
 								  A.TenSanPham,                                  
 								  A.username,
 								  ISNULL(SUM(A.TongClickThucChay), 0) TongClickThucChay,
 								  ISNULL(SUM(A.TongViewThucChay), 0) TongViewThucChay,
 								  ISNULL(SUM(A.SoLuongThucChay), 0) SoLuongThucChay,
 								  ISNULL(SUM(A.SoLuongThucChayKM), 0)SoLuongThucChayKM,
 								  ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay + A.Giatrithaydoi), 0) ThanhTienSauTrietKhauThucChay,
 								  ISNULL(SUM(A.ThanhTienKM), 0) AS ThanhTienKM,
 								  ISNULL(SUM(A.SoLuongThucChayOnline), 0) AS SoLuongThucChayOnline,
 								  ISNULL(SUM(A.TienThucChayOnline), 0) AS TienThucChayOnline,
 								  ISNULL(SUM(A.TienKhuyenMaiOnline), 0) AS TienKhuyenMaiOnline
 						   FROM   (
 									  SELECT tcdta.DmSanPhamREF,
 											 tcdta.TenSanPham,
 											 --A.HopDongChiTietREF,
 											hdct.TK_AdMarket username,
 											 ISNULL(SUM(tcdta.TongClickThucChay), 0) TongClickThucChay,
 											 ISNULL(SUM(tcdta.TongViewThucChay), 0) TongViewThucChay,
 											 ISNULL(SUM(tcdta.SoLuongThucChay), 0) SoLuongThucChay,
 											 ISNULL(SUM(tcdta.SoLuongThucChayKM), 0) SoLuongThucChayKM,
 											 ISNULL(SUM(tcdta.ThanhTienSauTrietKhauThucChay), 0) ThanhTienSauTrietKhauThucChay,
 											 ISNULL(SUM(tcdta.Giatrithaydoi), 0) Giatrithaydoi,
 											 ISNULL(SUM(tcdta.ThanhTienKM), 0) ThanhTienKM,
 											 0 SoLuongThucChayOnline,
 											 0 TienThucChayOnline,
 											 0 TienKhuyenMaiOnline
 									  FROM   ThucChayDaTinhAdmarket tcdta
 									  LEFT JOIN HopDongChiTiet hdct ON  hdct.HopDongChiTietID = tcdta.HopDongChiTietREF
 									  WHERE 1=1 AND tcdta.NgayThucHien BETWEEN @NgayThucHienSt AND @NgayThucHien  
 											 AND tcdta.DmSanPhamREF = @DmSanPhamREF                                          
 											 AND HopDongFK NOT IN (SELECT HopDongID FROM dbo.HopDong hd
 										where hd.Tenmahopdong IN ('NB','SH','NBDT'))
 									  GROUP BY
 											 tcdta.DmSanPhamREF,
 											 tcdta.TenSanPham,
 											 tcdta.HopDongChiTietREF 	  , TK_AdMarket                                 								
 								  ) A
 						   GROUP BY
 								  A.DmSanPhamREF,
 								  A.TenSanPham,
 								  A.username
 					   )T
 				WHERE  T.username IS NOT NULL
 				GROUP BY
 					   T.username,
 					   T.DmSanPhamREF
             )T2
             ON  T1.username = T2.username
             AND T1.DmSanPhamREF = T2.DmSanPhamREF           
WHERE 1=1	
   --dieu kien 1, cac tk khong co hd
 --AND ( T1.ThanhTien IS NULL or t1.ThanhTien =0) AND T1.moneys <> 0 
 -----------------------------------------------------------
 --dieu kien 2: các tai khoan chua gán hết thực chạy và thanh tien hd <> thanh tien thuc chay
 AND t1.ThanhTien > 0  AND (ABS(T1.moneys - ISNULL(T2.TienThucChay_tcdt,0)) > 0) AND (ABS(T1.ThanhTien -T2.TienThucChay_tcdt) > 2  )
 -----------------------------------------------------------
 --dieu kien 3: check hang ngay
-- and((T1.moneys <> 0 AND (ABS(T1.moneys - ISNULL(T2.TienThucChay_tcdt,0)) > 2)) OR (ISNULL(T1.moneys,0)=0 AND T2.TienThucChay_tcdt <> 0))
 --WHERE 1=1 AND T1.moneys <> T2.TongTien-AND T1.thanhtien IS NOT NULL AND (T1.thanhtien <> T2.TienThucChay_tcdt)
 -- AND T1.username IN (SELECT TK_AdMarket FROM dbo.HopDongChiTiet WHERE DmSanPhamREF = 585 AND DeletedStatus <> 1 AND TK_AdMarket = 'habeco1')
  ORDER BY  T1.NgayThucHienMax
  -- chu ý check Chenh Lech > 0
end

```
