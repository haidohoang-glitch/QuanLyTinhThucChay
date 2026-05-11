# Stored Procedure: `ThucChay_CheckThucChayCPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-07 20:33:12.327000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.470000

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
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_CheckThucChayCPM] '07/01/2013', '07/31/2013'
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayCPM]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @table TABLE 
	        (
	            TypeProduct INT,
	            DmSanPhamREF INT,
	            TenSanPham NVARCHAR(200),
	            SoHopDong NVARCHAR(50),
	            --DonGiaSauCK FLOAT,
	            TongPageView INT,
	            ThanhTien FLOAT
	        )
	
	INSERT INTO @table
	SELECT A.TypeProduct,
			B.DmSanPhamREF,
	       A.TenSanPham,
	       a.SoHopDong,
	       --isnull(b.DonGiaSauCK,0)/1000 DonGiaSauCK,
	       SUM(a.PageView) TongPageView,
	       round(SUM((ISNULL(b.DonGiaSauCK, 0) / 1000) * a.PageView),0) AS ThanhTien
	FROM   (
	           SELECT dbo.GetProductNameByTypeProduct(tc.TypeProduct) AS 
	                  TenSanPham,
	                  tc.TypeProduct,
	                  tc.SoHopDong,
	                  SUM(tc.TongViewThucChay) AS PageView
	           FROM   ThucChay tc
	           WHERE  tc.SoHopDong IN (SELECT hd.SoHopDong
	                                   FROM   HopDong hd
	                                          INNER JOIN HopDongChiTiet hdct
	                                               ON  hd.HopDongID = hdct.HopDongFK
	                                   WHERE  hd.TrangThaiHopDong <> 3
	                                   and hdct.DmSanPhamREF in (231, 238, 239, 240, 337, 339, 370)
	                                   AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3 --Đơn vị của hình thức CPM
	                                   )	               
	                  AND CONVERT(DATE, tc.NgayThucHien) BETWEEN @StartDate AND @EndDate
	                  AND tc.TypeProduct IN (3, 4, 5, 8, 9)
	           GROUP BY					  
	                  tc.TypeProduct,
	                  tc.SoHopDong
	                  --ORDER BY tc.TypeProduct, tc.SoHopDong
	       )A
	       LEFT JOIN (
	                SELECT (
	                           CASE 
	                                WHEN HDCT.DmSanPhamREF = 231 THEN 3
	                                WHEN HDCT.DmSanPhamREF = 238 THEN 4
	                                WHEN HDCT.DmSanPhamREF = 339 THEN 5
	                                WHEN HDCT.DmSanPhamREF = 239 THEN 6
	                                WHEN HDCT.DmSanPhamREF = 337 THEN 7
	                                WHEN HDCT.DmSanPhamREF = 240 THEN 8
	                                WHEN HDCT.DmSanPhamREF = 370 THEN 9
	                                     --else 9
	                           END
	                       ) AS type_product,
	                       hdct.DmSanPhamREF,
	                       hd.SoHopDong,
	                       --max(hdct.ThanhTien/hdct.SoLuong) DonGiaSauCKMax,
	                       SUM(hdct.SoLuong) SoLuong,
	                       SUM(hdct.ThanhTien) ThanhTien,
	                       (SUM(hdct.ThanhTien) / SUM(hdct.SoLuong))DonGiaSauCK
	                       --max((isnull(hdct.ThanhTien,0)/hdct.SoLuong)) DonGiaSauCK
	                FROM   HopDong hd
	                       INNER JOIN HopDongChiTiet hdct
	                            ON  HD.HopDongID = HDCT.HopDongFK
	                            AND HDCT.DmSanPhamREF IN (231, 238, 239, 240, 337, 339, 370)
	                            AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3
	                GROUP BY
	                       HDCT.DmSanPhamREF,
	                       HD.SoHopDong
	            )B
	            ON  UPPER(A.SoHopDong) = B.SoHopDong
	            AND A.TypeProduct = B.type_product
	            AND B.DonGiaSauCK > 0
	                --AND (B.DonGiaSauCKTB <> b.DonGiaSauCKMin
	                --OR B.DonGiaSauCKTB <> b.DonGiaSauCKMax)
	                --and a.TypeProduct = 9
	GROUP BY
	       A.TypeProduct,
	       A.TenSanPham,
	       a.SoHopDong
	       ,b.DmSanPhamREF
	--, a.PageView, 
	--,b.DonGiaSauCK
	--ORDER BY A.TenSanPham ,a.SoHopDong
	SELECT T.TypeProduct, 
			T.TenSanPham, 
			T.SoHopDong,
			T.TongPageView AS ViewThucChay,			
			T.ThanhTien,
			DT.TenSanPham
			,DT.SoHopDong
			--, DT.HopDongChiTietREF
			,DT.TongPageView
			,DT.TongToolTinh	
			, DT.SlMua
			, DT.SlKM
			, DT.Sllech			
			,T.TongPageView- DT.TongToolTinh AS SoViewLech
			,T.ThanhTien - DT.TongTien AS TTLech	
	FROM
	(
	SELECT TypeProduct,DmSanPhamREF ,TenSanPham , SoHopDong ,
	            isnull(TongPageView,0)TongPageView,
	            isnull(ThanhTien,0) ThanhTien
	FROM   @table
	--ORDER BY
	--       TenSanPham,
	--       SoHopDong
	)T
	FULL OUTER JOIN
	(
	SELECT tcdt.DmSanPhamREF,
	       tcdt.TenSanPham,
	       tcdt.SoHopDong,
	       --tcdt.HopDongChiTietREF,
	       SUM(tcdt.TongViewThucChay) TongPageView,
	       SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThucChayKM + tcdt.SoLuongThucChayLechTreoHa) TongToolTinh,
	       SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThucChayKM + tcdt.SoLuongThucChayLechTreoHa) - SUM(tcdt.TongViewThucChay) AS SoLech,	       
	       SUM(tcdt.SoLuongThucChay) slmua,
	       SUM(tcdt.SoLuongThucChayKM) slkm,
	       SUM(tcdt.SoLuongThucChayLechTreoHa) sllech,
	       SUM(tcdt.ThanhTienSauTrietKhauThucChay) AS ThanhTien,
	       SUM(tcdt.ThanhTienKM) ThanhTienKM,
	       SUM(tcdt.ThanhTienLechTreoHa) ThanhTienLechTreoHa,
	       round(SUM(ThanhTienSauTrietKhauThucChay + ThanhTienKM + ThanhTienLechTreoHa),0) AS TongTien
	FROM   ThucChayDaTinh tcdt
	WHERE  tcdt.DmSanPhamREF IN (231, 238, 239, 240, 337, 339, 370)
	       AND CONVERT(date, tcdt.NgayThucHien) BETWEEN @StartDate AND @EndDate
	       AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh) = 3
	GROUP BY
	       tcdt.DmSanPhamREF,
	       tcdt.TenSanPham,
	       tcdt.SoHopDong
	       --,tcdt.HopDongChiTietREF
	       --tcdt.DonGiaTheoDonVi
	--ORDER BY
	--       tcdt.TenSanPham,
	--       tcdt.SoHopDong
	) DT ON T.SoHopdong = DT.SoHopdong AND T.DmSanPhamREF = DT.DmSanPhamREF
	WHERE 
	(T.TongPageView - DT.TongToolTinh) <> 0
	--OR (T.ThanhTien - DT.TongTien) <> 0 or 
	--DT.SoHopDong is null
	ORDER BY T.TenSanPham, T.SoHopDong	
	
	--SELECT A.TenSanPham,A.SoHopDong, 
	--SUM(A.SLMua)SLMua, SUM(A.SLKM)SLKM, 
	--SUM(A.ThanhTien) ThanhTienMua, 
	--MAX(A.DonGiaMua)DonGiaMua, MAX(A.DonGiaKM) DonGiaKM	  
	--FROM 
	--(
	--SELECT hd.SoHopDong, hdct.TenSanPham, 
	--	sum(hdct.SoLuong) as SLMua , 
	--	0 as SLKM, 
	--	sum(hdct.ThanhTien) ThanhTien, 
	--	max(hdct.DonGia) AS DonGiaMua,
	--	0 AS DonGiaKM 
	--FROM   HopDong hd
	--       INNER JOIN HopDongChiTiet hdct
	--            ON  hd.HopDongID = hdct.HopDongFK
	--WHERE  hdct.DmSanPhamREF IN (231, 238, 239, 240, 337, 339, 370)
	--       AND hd.SoHopDong IN (SELECT tc.SoHopDong FROM   ThucChay tc
	--                            WHERE  CONVERT(DATE, tc.NgayThucHien) BETWEEN @StartDate AND @EndDate
	--                                   AND tc.TypeProduct IN (3, 4, 5, 8, 9)
	--                              )
	--	AND hdct.IsKhuyenMai = 0
	--GROUP BY hd.SoHopDong,hdct.TenSanPham
	--UNION ALL
	--SELECT hd.SoHopDong, 
	--		hdct.TenSanPham,
	--		0 as SLMua , 
	--		sum(hdct.SoLuong) as SLKM,  
	--		0 as ThanhTien, 
	--		0 AS DonGiaMua,
	--		max(hdct.DonGia) AS DonGiaKM
	--FROM   HopDong hd
	--       INNER JOIN HopDongChiTiet hdct
	--            ON  hd.HopDongID = hdct.HopDongFK
	--WHERE  hdct.DmSanPhamREF IN (231, 238, 239, 240, 337, 339, 370)
	--       AND hd.SoHopDong IN (SELECT tc.SoHopDong FROM   ThucChay tc
	--                            WHERE  CONVERT(DATE, tc.NgayThucHien) BETWEEN @StartDate AND @EndDate
	--                                   AND tc.TypeProduct IN (3, 4, 5,  8, 9)
	--                             )
	--	AND hdct.IsKhuyenMai = 1  
	--GROUP BY hd.SoHopDong, hdct.TenSanPham
	--)A 
	--GROUP BY A.SoHopDong,A.TenSanPham
	--ORDER BY A.TenSanPham, A.SoHopDong
	                                
END

```
