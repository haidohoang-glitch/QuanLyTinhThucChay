# Stored Procedure: `CheckThucChayVuotHopDongByNam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-06 17:41:09.093000
- **Ngày sửa cuối**: 2018-08-06 18:09:50.040000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiCheck` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--SELECT ThucChayDaTinhID, NgayThucHien,DmHinhThucQuangCao, DmLoaiBannerREF, ThanhTienSauTrietKhauThucChay, GiaTriThayDoi FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF = 88215
--exec CheckThucChayVuotHopDong '2018-05-02',42,''
--DongBoDuLieu  '2017-03-22', '2017-03-22'
--dbo.CompareDongBoDuLieu '2017-01-01', '2017-03-23'

CREATE PROCEDURE [dbo].[CheckThucChayVuotHopDongByNam] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@LoaiCheck INT --1: Theo San pham,
	                -- 2: Theo san pham va phan bo, --CPC880414 CPC Admarket: mua ngoai, day du lieu vao 2 bang
	                -- 3: theo san pham, phan bo và HTQC
	                -- 4: HopDong,SanPham,HinhThucQuangcao
	--@DmSanPhamREF NVARCHAR(MAX) 
	

AS
BEGIN
	
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	----------------------@ThucChayDaTinh--------------------
	DECLARE @ThucChayDaTinhNow TABLE 
	(HopDongID int,
	HopDongChiTietREF INT,
	SoHopDong nvarchar(50),
	tttc float
	)
	INSERT INTO @ThucChayDaTinhNow

	SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.SoHopDong,round(SUM(tcdt.ThanhTienSauTrietKhauThucChay+ tcdt.GiaTriThayDoi),0) tttc
		  FROM ThucChayDaTinh tcdt where 1=1 AND tcdt.NgayThucHien =@NgayThucHien
		  AND tcdt.DmSanPhamREF NOT IN (144,585,628,337)
		  AND tcdt.TrangThaiHopDong <> 3
		GROUP BY tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF
		UNION ALL
		SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF,tcdt.SoHopDong,round(SUM(tcdt.ThanhTienSauTrietKhauThucChay+ tcdt.GiaTriThayDoi),0) tttc
		  FROM ThucChayDaTinhAdmarket tcdt  where 1=1 AND tcdt.NgayThucHien =@NgayThucHien
		    AND tcdt.TrangThaiHopDong <> 3
		GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.SoHopDong

----------------------@HopDong--------------------
	DECLARE @HopDong TABLE 
	(HopDongID int,
	SoHopDong nvarchar(50),
	ThanhTien float
	)
	
	INSERT INTO @HopDong
	SELECT hd.HopDongID,hd.SoHopDong, 
	CASE WHEN hd.TrangThaiHopDong = 3 THEN 0
	ELSE SUM(hdct.ThanhTien) 
	END ThanhTien
	FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE hdct.DeletedStatus <> 1
	AND hd.Nam >=2015
	AND hd.HopDongID IN (SELECT HopDongID FROM @ThucChayDaTinhNow)
	GROUP BY hd.HopDongID,SoHopDong,TrangThaiHopDong
		----------------------@ThucChayDaTinh--------------------
DECLARE @ThucChayDaTinh TABLE 
	(HopDongID int,
	HopDongChiTietREF INT,
	SoHopDong nvarchar(50),
	tttc float
	)
	INSERT INTO @ThucChayDaTinh

	SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.SoHopDong,round(SUM(tcdt.ThanhTienSauTrietKhauThucChay+ tcdt.GiaTriThayDoi),0) tttc
		  FROM ThucChayDaTinh tcdt where 1=1 AND tcdt.NgayThucHien <=@NgayThucHien
		  AND tcdt.DmSanPhamREF NOT IN (144,585,628,337)
		  AND tcdt.TrangThaiHopDong <> 3
		  --AND tcdt.HopDongID IN (SELECT HopDongID FROM @ThucChayDaTinhNow)
		GROUP BY tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF
		UNION ALL
		SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF,tcdt.SoHopDong,round(SUM(tcdt.ThanhTienSauTrietKhauThucChay+ tcdt.GiaTriThayDoi),0) tttc
		  FROM ThucChayDaTinhAdmarket tcdt  where 1=1 AND tcdt.NgayThucHien <=@NgayThucHien
		    AND tcdt.TrangThaiHopDong <> 3
			--AND tcdt.HopDongID IN (SELECT HopDongID FROM @ThucChayDaTinhNow)
		GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.SoHopDong


IF @LoaiCheck = 1
BEGIN
	--kiem tra all
	SELECT A.*, B.*, (A.ThanhTien - B.tttc)lech FROM
	(
	SELECT HopDongID,SoHopDong, ThanhTien FROM @HopDong 
	)A
	RIGHT JOIN
	(
	SELECT HopDongID,SoHopDong,SUM(tttc)tttc FROM @ThucChayDaTinh
	--WHERE NgayThucHien = '2018-08-03'
	GROUP BY HopDongID,SoHopDong
	)B 

	ON A.HopDongID = B.HopDongID	
	AND A.SoHopDong = B.SoHopDong
	WHERE
	 NOT (A.ThanhTien = 0 AND B.tttc = 0)	
	 and NOT (A.ThanhTien <>0 AND B.tttc IS NULL)
	 AND NOT (A.ThanhTien = B.tttc)	
	 AND A.ThanhTien - B.tttc < -5
	 
	-- A.ThanhTien < (B.tttc-2)
	--AND A.SoHopDong NOT IN (N'Khac-Số-01-0213','Khac011013','QC1711012','K120613')
		ORDER BY B.HopDongID,A.HopDongID	
		
		/*
	--kiem tra theo so hop dong, san pham
	SELECT a.*, b.*, (a.tthd - b.thanhtientc) FROM (
	SELECT sohopdong shda, hd.HopDongID, 
	(CASE WHEN trangthaihopdong = 3 THEN 0 ELSE SUM(Thanhtien)
	end)tthd,
	 hdct.DmSanPhamREF, hdct.TenSanPham
	FROM HopDong hd INNER JOIN HopDongChiTiet hdct
	ON hd.HopDongID = hdct.HopDongFK
	WHERE 1=1 --hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
		AND hd.DeletedStatus <> 1
		AND hdct.DeletedStatus <> 1 AND hdct.DmLoaiREF <> 42
		 AND hd.Nam = @Year
	 GROUP BY hd.SoHopDong, HopDongID,hdct.DmSanPhamREF, hdct.TenSanPham, hd.TrangThaiHopDong
	 )a
	 FULL OUTER JOIN
	 ( 	
	 SELECT B.shdb,
	 B.HopDongID,sum(B.thanhtientc)thanhtientc, B.DmSanPhamREF, B.TenSanPham FROM(
		 SELECT SoHopDong shdb, 
		 tcdt.HopDongID, round(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)),0) AS thanhtientc, tcdt.DmSanPhamREF, tcdt.TenSanPham
		 FROM ThucChayDaTinh tcdt
		 WHERE ngaythuchien<= @NgayThucHien AND 
		 tcdt.TrangThaiHopDong <> 3
		 AND tcdt.DmSanPhamREF NOT IN (144,585,628,337)
		 AND tcdt.DmHinhThucQuangCao <> 42
		 AND tcdt.HopDongID <> 0
		  AND tcdt.Nam = @Year
		 --AND tcdt.SoHopDong IN (SELECT distinct SoHopDong FROM ThucChayDaTinh WHERE YEAR(NgayThucHien)= 2014)
		 GROUP BY sohopdong ,
		  tcdt.HopDongID, tcdt.DmSanPhamREF, tcdt.TenSanPham
	 
		UNION ALL
	 
		 SELECT SoHopDong shdb,
		 HopDongID,round(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)),0) AS thanhtientc, tcdt.DmSanPhamREF, tcdt.TenSanPham
		 FROM ThucChayDaTinhAdmarket tcdt
		 WHERE ngaythuchien<= @NgayThucHien AND 1=1
		 AND HopDongID <> 0
		  AND tcdt.DmHinhThucQuangCao <> 42
		   AND tcdt.Nam = @Year
		  --tcdt.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
		  --and sohopdong in (SELECT distinct SoHopDong FROM ThucChayDaTinhAdmarket WHERE YEAR(NgayThucHien)= 2014)
		 GROUP BY sohopdong, 
		 tcdt.HopDongID, tcdt.DmSanPhamREF, tcdt.TenSanPham
	 )B GROUP BY B.shdb, 
	 B.HopDongID, B.DmSanPhamREF, B.TenSanPham 
	 )b
	 ON (1=1 AND a.shda = b.shdb
	 AND a.HopDongID = b.HopDongID
	 AND a.DmSanPhamREF = b.DmSanPhamREF
	 and a.TenSanPham = b.TenSanPham
	 ) 
	 	 WHERE round(ISNULL(a.tthd,0) - b.thanhtientc,0) <-2	-- OR NOT (a.tthd IS NULL AND b.thanhtientc = 0)
	ORDER BY a.DmSanPhamREF, a.HopDongID
	 --AND a.DmSanPhamREF IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@DmSanPhamREF, ',')) att) 	 			
END
ELSE IF @LoaiCheck = 2
BEGIN
SELECT a.*, b.*, (a.tthd - b.thanhtientc)FROM ( 
 SELECT sohopdong shda, hd.HopDongID, HopDongChiTietID,(CASE WHEN hdct.DeletedStatus = 1 THEN 0 else SUM(Thanhtien)END)tthd, 
 hdct.DmSanPhamREF, hdct.TenSanPham, hdct.DmLoaiREF,hdct.TenLoai
   FROM HopDong hd INNER JOIN HopDongChiTiet hdct
 ON hd.HopDongID = hdct.HopDongFK
 WHERE 1=1--hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
AND DmSanPhamREF NOT IN (141,637,305) 
 AND hd.DeletedStatus <> 1
 AND hd.TrangThaiHopDong <> 3
 AND hd.Nam =@Year
 GROUP BY hd.SoHopDong, HopDongID,hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.DmLoaiREF, hdct.TenLoai, hdct.DeletedStatus, hdct.DmLoaiBannerREF, hdct.TenLoaiBanner
 )a
 FULL OUTER JOIN
 ( 	
 SELECT --B.shdb,
 B.HopDongID, B.HopDongChiTietREF,sum(B.thanhtientc)thanhtientc, B.DmSanPhamREF, B.TenSanPham, B.DmHinhThucQuangCao, B.TenHinhThucQuangCao
   FROM
 (
 SELECT
 tcdt.HopDongID, HopDongChiTietREF, 
 round(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)),0) AS thanhtientc, 
 tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao
 FROM ThucChayDaTinh tcdt
 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 
 tcdt.DmSanPhamREF NOT IN (585,144,628,337,141,305,637) AND
 tcdt.TrangThaiHopDong <> 3
 AND tcdt.Nam =@Year
 
 GROUP BY 
 tcdt.HopDongChiTietREF,tcdt.DmSanPhamREF, tcdt.TenSanPham, HopDongID, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao
 
 UNION ALL
 
 SELECT 
 HopDongID,HopDongChiTietREF,
 round(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)),0) AS thanhtientc,
  tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao
 FROM ThucChayDaTinhAdmarket tcdt
 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 1=1
 AND tcdt.Nam = @Year
 GROUP BY 
  tcdt.HopDongID, HopDongChiTietREF,tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao
 )B GROUP BY 
 HopDongID, B.HopDongChiTietREF,B.DmSanPhamREF, B.TenSanPham, B.DmHinhThucQuangCao, B.TenHinhThucQuangCao
 
 )b
 ON (1=1 
 AND a.HopDongID = b.HopDongID
 AND a.HopDongChiTietID = b.HopDongChiTietREF
 AND a.DmSanPhamREF = b.DmSanPhamREF
 and a.TenSanPham = b.TenSanPham
 AND a.DmLoaiREF = b.DmHinhThucQuangCao
 ) 
	 WHERE (ISNULL(a.tthd,0) - ISNULL(b.thanhtientc,0) <-3	 OR (a.tthd IS NULL)OR b.thanhtientc < 0 )
	 AND a.DmSanPhamREF IN (SELECT  DmSanPhamREF FROM DmSanPhamThucChay WHERE DeletedStatus <> 1) 
	-- AND a.DmSanPhamREF IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@DmSanPhamREF, ',')) att) 	 	
	 	 	--and right(a.shda,2)>=14
 ORDER BY a.HopDongID desc,a.DmSanPhamREF,a.HopDongChiTietID 
 END
ELSE IF @LoaiCheck = 3
BEGIN
	SELECT a.*, b.*, (a.tthd - b.thanhtientc)FROM ( 
	 SELECT sohopdong shda, hd.HopDongID, HopDongChiTietID, hdct.TenLoai, SUM(Thanhtien)tthd, hdct.DmSanPhamREF, hdct.TenSanPham
	 FROM HopDong hd INNER JOIN HopDongChiTiet hdct
	 ON hd.HopDongID = hdct.HopDongFK
	 WHERE 1=1--hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
	AND hd.DeletedStatus <> 1
	 AND hdct.DeletedStatus <> 1
	 AND hd.TrangThaiHopDong <> 3
	 AND hd.Nam = @Year
	 GROUP BY hd.SoHopDong, HopDongID,hdct.HopDongChiTietID, hdct.TenLoai, hdct.DmSanPhamREF, hdct.TenSanPham
	 )a
	 FULL OUTER JOIN
	 (	 	
	 SELECT --B.shdb, 
	 B.HopDongID, B.HopDongChiTietREF,B.TenHinhThucQuangCao,B.DmSanPhamREF,B.TenSanPham,sum(B.thanhtientc)thanhtientc
	   FROM
	 (
	 SELECT --SoHopDong shdb,
	 HopDongID, HopDongChiTietREF,TenHinhThucQuangCao, 
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 tcdt.DmSanPhamREF, tcdt.TenSanPham, MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinh tcdt
	 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 
	 tcdt.DmSanPhamREF NOT IN (144,585,628,337) AND
	 tcdt.TrangThaiHopDong <> 3
	  AND tcdt.Nam = @Year
	 --AND tcdt.SoHopDong IN (SELECT distinct SoHopDong FROM ThucChayDaTinh WHERE YEAR(NgayThucHien)= 2014)
	 GROUP BY --sohopdong,
	  tcdt.HopDongID, tcdt.HopDongChiTietREF,TenHinhThucQuangCao,tcdt.DmSanPhamREF, tcdt.TenSanPham
	 
	 UNION ALL
	 
	 SELECT --SoHopDong shdb, 
	 tcdt.HopDongID,HopDongChiTietREF,TenHinhThucQuangCao,
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 tcdt.DmSanPhamREF, tcdt.TenSanPham, MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinhAdmarket tcdt
	 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 1=1
	   AND tcdt.Nam = @Year
	 -- tcdt.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
	 -- AND sohopdong in (SELECT distinct SoHopDong FROM ThucChayDaTinhAdmarket WHERE YEAR(NgayThucHien)= 2014)
	 GROUP BY --sohopdong, 
	 tcdt.HopDongID,HopDongChiTietREF,TenHinhThucQuangCao,tcdt.DmSanPhamREF, tcdt.TenSanPham
	 )B 
	 --WHERE  YEAR(B.NgayThucHienMax) = 2014
	 GROUP BY --B.shdb,
	 B.HopDongID,B.HopDongChiTietREF,B.TenHinhThucQuangCao,B.DmSanPhamREF, B.TenSanPham
	 )b
	 ON (1=1--a.shda = b.shdb
	 AND a.HopDongID = b.HopDongID
	 AND a.HopDongChiTietID = b.HopDongChiTietREF
	 AND a.DmSanPhamREF = b.DmSanPhamREF
	 and a.TenSanPham = b.TenSanPham
	 AND a.TenLoai = B.TenHinhThucQuangCao
	 )	 
	 WHERE (round(a.tthd - b.thanhtientc,0) <-2 OR (b.thanhtientc <0) 	OR (a.tthd IS NULL))
	 --AND a.DmSanPhamREF NOT IN (240,339,231,238,370,531,598,613)
	 
	 AND a.DmSanPhamREF IN (SELECT  DmSanPhamREF FROM DmSanPhamThucChay WHERE DeletedStatus <> 1) 
	 --AND (a.TenLoai IS NULL OR b.TenHinhThucQuangCao IS NULL)
	 --AND a.DmSanPhamREF IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@DmSanPhamREF, ',')) att)
	ORDER BY a.HopDongChiTietID 
END 
---HopDong,HDCT,SanPham,HinhThucQuangcao
ELSE IF @LoaiCheck = 4
BEGIN
	SELECT a.*, b.*, (a.tthd - b.thanhtientc)FROM ( 
	 SELECT sohopdong shda, hd.HopDongID,SoHopDong,hdct.HopDongChiTietID, hdct.TenLoai, SUM(Thanhtien)tthd, hdct.DmSanPhamREF, hdct.TenSanPham
	 FROM HopDong hd INNER JOIN HopDongChiTiet hdct
	 ON hd.HopDongID = hdct.HopDongFK
	 WHERE 1=1 --hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
	AND hd.DeletedStatus <> 1
	 AND hdct.DeletedStatus <> 1
	 AND hd.TrangThaiHopDong <> 3
	   AND hd.Nam = @Year
	 GROUP BY hd.SoHopDong, HopDongID, HopDongChiTietID, hdct.TenLoai, hdct.DmSanPhamREF, hdct.TenSanPham
	 )a
	 FULL OUTER JOIN
	 (	 	
	 SELECT --B.shdb, 
	 B.HopDongID,B.SoHopDong,B.HopDongChiTietREF,B.TenHinhThucQuangCao,B.DmSanPhamREF,B.TenSanPham,sum(B.thanhtientc)thanhtientc
	   FROM
	 (
	 SELECT --SoHopDong shdb,
	 HopDongID,SoHopDong,HopDongChiTietREF,TenHinhThucQuangCao, 
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 tcdt.DmSanPhamREF, tcdt.TenSanPham, MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinh tcdt
	 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 
	 tcdt.DmSanPhamREF NOT IN (144,585,628,337) AND
	 tcdt.TrangThaiHopDong <> 3
	   AND tcdt.Nam = @Year
	-- AND tcdt.SoHopDong IN (SELECT distinct SoHopDong FROM ThucChayDaTinh WHERE YEAR(NgayThucHien)= 2014)
	 GROUP BY --sohopdong,
	  tcdt.HopDongID,SoHopDong,HopDongChiTietREF,TenHinhThucQuangCao,tcdt.DmSanPhamREF, tcdt.TenSanPham
	 
	 UNION ALL
	 
	 SELECT-- SoHopDong shdb, 
	 tcdt.HopDongID,SoHopDong,HopDongChiTietREF,TenHinhThucQuangCao,
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 tcdt.DmSanPhamREF, tcdt.TenSanPham, MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinhAdmarket tcdt
	 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 1=1
	   AND tcdt.Nam = @Year
	 GROUP BY-- sohopdong, 
	 tcdt.HopDongID,SoHopDong,HopDongChiTietREF,TenHinhThucQuangCao,tcdt.DmSanPhamREF, tcdt.TenSanPham
	 )B 
	-- WHERE  YEAR(B.NgayThucHienMax) = 2014
	 GROUP BY-- B.shdb,
	 B.HopDongID,B.SoHopDong,B.HopDongChiTietREF,B.TenHinhThucQuangCao,B.DmSanPhamREF, B.TenSanPham
	 )b
	 ON (1=1 --a.shda = b.shdb
	 AND a.HopDongID = b.HopDongID
	 AND a.SoHopDong = b.SoHopDong
	 AND a.HopDongChiTietID = b.HopDongChiTietREF
	 AND a.DmSanPhamREF = b.DmSanPhamREF
	 and a.TenSanPham = b.TenSanPham
	 AND a.TenLoai = B.TenHinhThucQuangCao
	 )	 
	 WHERE (
	 round(a.tthd - b.thanhtientc,0) <-2 OR
	  (b.thanhtientc <0)OR 
	  ((a.tthd IS null) AND NOT (a.tthd IS NULL AND b.thanhtientc = 0)) 	 OR
	   (a.tthd IS NULL))
	 --AND a.DmSanPhamREF NOT IN (240,339,231,238,370,531,598,613)
	-- AND a.DmSanPhamREF IN (SELECT  DmSanPhamREF FROM DmSanPhamThucChay WHERE DeletedStatus <> 1) 
	 --AND a.DmSanPhamREF IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@DmSanPhamREF, ',')) att)
	ORDER BY a.DmSanPhamREF, a.HopDongID, a.HopDongChiTietID, b.DmSanPhamREF, b.HopDongID, b.HopDongChiTietREF
	---5: Hopdong, htqc, sp
	END
	ELSE IF @LoaiCheck = 5
BEGIN
	SELECT a.*, b.*, (a.tthd - B.thanhtientc) [HD- tc] FROM ( 
	 SELECT sohopdong shda, hd.HopDongID,SoHopDong,hdct.TenLoai, SUM(Thanhtien)tthd, hdct.DmSanPhamREF, hdct.TenSanPham
	 FROM HopDong hd INNER JOIN HopDongChiTiet hdct
	 ON hd.HopDongID = hdct.HopDongFK
	 WHERE 1= 1 AND hd.Nam =@Year
	AND hd.DeletedStatus <> 1
	 AND hdct.DeletedStatus <> 1
	 AND hd.TrangThaiHopDong <> 3
	 GROUP BY hd.SoHopDong, HopDongID, hdct.TenLoai, hdct.DmSanPhamREF, hdct.TenSanPham
	 )a
	 FULL OUTER JOIN
	 (	 	
	 SELECT --B.shdb, 
	 B.HopDongID,B.SoHopDong,B.TenHinhThucQuangCao,B.DmSanPhamREF,B.TenSanPham,sum(B.thanhtientc)thanhtientc
	   FROM
	 (
	 SELECT --SoHopDong shdb,
	 HopDongID,SoHopDong,TenHinhThucQuangCao, 
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 tcdt.DmSanPhamREF, tcdt.TenSanPham, MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinh tcdt
	 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 
	 tcdt.DmSanPhamREF NOT IN (144,585,628,337) AND
	 tcdt.TrangThaiHopDong <> 3
	  AND tcdt.Nam = @Year
	-- AND tcdt.SoHopDong IN (SELECT distinct SoHopDong FROM ThucChayDaTinh WHERE YEAR(NgayThucHien)= 2014)
	 GROUP BY --sohopdong,
	  tcdt.HopDongID,SoHopDong,TenHinhThucQuangCao,tcdt.DmSanPhamREF, tcdt.TenSanPham
	 
	 UNION ALL
	 
	 SELECT-- SoHopDong shdb, 
	 tcdt.HopDongID,SoHopDong,TenHinhThucQuangCao,
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 tcdt.DmSanPhamREF, tcdt.TenSanPham, MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinhAdmarket tcdt
	 WHERE tcdt.NgayThucHien <= @NgayThucHien
	 AND tcdt.Nam = @Year
	--  AND sohopdong in (SELECT distinct SoHopDong FROM ThucChayDaTinhAdmarket WHERE YEAR(NgayThucHien)= 2014)
	 GROUP BY 
	 tcdt.HopDongID,SoHopDong,TenHinhThucQuangCao,tcdt.DmSanPhamREF, tcdt.TenSanPham
	 )B 
	-- WHERE  YEAR(B.NgayThucHienMax) = 2014
	 GROUP BY-- B.shdb,
	 B.HopDongID,B.SoHopDong,B.TenHinhThucQuangCao,B.DmSanPhamREF, B.TenSanPham
	 )b
	 ON (1=1
	 AND a.HopDongID = b.HopDongID
	 AND a.SoHopDong = b.SoHopDong
	 AND a.DmSanPhamREF = b.DmSanPhamREF
	 AND a.TenLoai = B.TenHinhThucQuangCao
	 )	 
	 WHERE 1=1 AND (round(a.tthd - b.thanhtientc,0) <-2 
					OR (B.thanhtientc <0)
					OR a.tthd IS null
					)
	 AND NOT (a.tthd IS NULL AND b.thanhtientc = 0)
	 --OR (a.tthd  IS NULL)
	ORDER BY  a.HopDongID,a.DmSanPhamREF, b.HopDongID, b.DmSanPhamREF
END 
--6. HopDong, Nhan Hang, sanpham
	ELSE IF @LoaiCheck = 6
BEGIN
	SELECT a.*, b.*, (a.tthd - b.thanhtientc)FROM ( 
	 SELECT sohopdong shda, hd.HopDongID,SoHopDong,hdct.NhanHang, SUM(Thanhtien)tthd, hdct.DmSanPhamREF, hdct.TenSanPham
	 FROM HopDong hd INNER JOIN HopDongChiTiet hdct
	 ON hd.HopDongID = hdct.HopDongFK
	 WHERE 1=1-- hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
	AND hd.DeletedStatus <> 1
	 AND hdct.DeletedStatus <> 1
	 AND hd.TrangThaiHopDong <> 3
	  AND hd.Nam = @Year
	 GROUP BY hd.SoHopDong, HopDongID, hdct.NhanHang, hdct.DmSanPhamREF, hdct.TenSanPham
	 )a
	 FULL OUTER JOIN
	 (	 	
	 SELECT --B.shdb, 
	 B.HopDongID,B.SoHopDong,B.NhanHang,B.DmSanPhamREF,B.TenSanPham,sum(B.thanhtientc)thanhtientc
	   FROM
	 (
	 SELECT --SoHopDong shdb,
	 HopDongID,SoHopDong,NhanHang, 
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 tcdt.DmSanPhamREF, tcdt.TenSanPham, MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinh tcdt
	 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 
	 tcdt.DmSanPhamREF NOT IN (144,585,628,337) AND
	 tcdt.TrangThaiHopDong <> 3
	  AND tcdt.Nam = @Year
	-- AND tcdt.SoHopDong IN (SELECT distinct SoHopDong FROM ThucChayDaTinh WHERE YEAR(NgayThucHien)= 2014)
	 GROUP BY --sohopdong,
	  tcdt.HopDongID,SoHopDong,NhanHang,tcdt.DmSanPhamREF, tcdt.TenSanPham
	 
	 UNION ALL
	 
	 SELECT-- SoHopDong shdb, 
	 tcdt.HopDongID,SoHopDong,NhanHang,
	 ISNULL(round(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0),0) AS thanhtientc, 
	 tcdt.DmSanPhamREF, tcdt.TenSanPham, MAX(tcdt.NgayThucHien) AS NgayThucHienMax 
	 FROM ThucChayDaTinhAdmarket tcdt
	 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 1=1
	  AND tcdt.Nam = @Year
	 GROUP BY 
	 tcdt.HopDongID,SoHopDong,NhanHang,tcdt.DmSanPhamREF, tcdt.TenSanPham
	 )B 
	-- WHERE  YEAR(B.NgayThucHienMax) = 2014
	 GROUP BY-- B.shdb,
	 B.HopDongID,B.SoHopDong,B.NhanHang,B.DmSanPhamREF, B.TenSanPham
	 )b
	 ON (1=1
	 AND a.HopDongID = b.HopDongID
	 AND a.SoHopDong = b.SoHopDong
	 AND a.DmSanPhamREF = b.DmSanPhamREF
	 and a.TenSanPham = b.TenSanPham
	 AND a.NhanHang = b.NhanHang
	 )	 
	 WHERE (round(a.tthd - b.thanhtientc,0) <-2 OR (b.thanhtientc <0)OR a.tthd IS null)
	  AND NOT (a.tthd IS NULL AND b.thanhtientc = 0)
	  	OR (a.tthd IS NULL)
	ORDER BY  a.HopDongID,a.DmSanPhamREF, b.HopDongID, b.DmSanPhamREF
END 


ELSE IF @LoaiCheck = 13
BEGIN
SELECT a.*, b.*, (a.tthd - b.thanhtientc)FROM ( 
 SELECT sohopdong shda, hd.HopDongID, HopDongChiTietID,(CASE WHEN hdct.DeletedStatus = 1 THEN 0 else SUM(Thanhtien)END)tthd, 
 hdct.DmSanPhamREF, hdct.TenSanPham, hdct.DmLoaiREF,hdct.TenLoai, hdct.DmLoaiBannerREF, hdct.TenLoaiBanner
   FROM HopDong hd INNER JOIN HopDongChiTiet hdct
 ON hd.HopDongID = hdct.HopDongFK
 WHERE 1=1--hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
AND DmSanPhamREF NOT IN (141,637,305) 
 AND hd.DeletedStatus <> 1
 AND hd.TrangThaiHopDong <> 3
 AND (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
  AND hd.Nam = @Year
 GROUP BY hd.SoHopDong, HopDongID,hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.DmLoaiREF, hdct.TenLoai, hdct.DeletedStatus, hdct.DmLoaiBannerREF, hdct.TenLoaiBanner
 )a
 left JOIN
 ( 	
 SELECT --B.shdb,
 B.HopDongID, B.HopDongChiTietREF,sum(B.thanhtientc)thanhtientc, B.DmSanPhamREF, B.TenSanPham, B.DmHinhThucQuangCao, B.TenHinhThucQuangCao,B.DmLoaiBannerREF, B.TenLoaiBanner
   FROM
 (
 SELECT --SoHopDong shdb, 
 tcdt.HopDongID, HopDongChiTietREF, 
 round(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)),0) AS thanhtientc, 
 tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner
 FROM ThucChayDaTinh tcdt
 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 
 tcdt.DmSanPhamREF NOT IN (585,144,628,337,141,637,305) AND
 tcdt.TrangThaiHopDong <> 3
  AND tcdt.Nam = @Year
 --AND tcdt.HopDongChiTietREF IN (SELECT distinct HopDongChiTietREF FROM ThucChayDaTinh WHERE YEAR(NgayThucHien)= 2014)
 GROUP BY --sohopdong , 
 tcdt.HopDongChiTietREF,tcdt.DmSanPhamREF, tcdt.TenSanPham, HopDongID, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmLoaiBannerREF, tcdt.TenLoaiBanner
 

 )B GROUP BY --B.shdb,
 HopDongID, B.HopDongChiTietREF,B.DmSanPhamREF, B.TenSanPham, B.DmHinhThucQuangCao, B.TenHinhThucQuangCao,B.DmLoaiBannerREF, B.TenLoaiBanner
 
 )b
 ON (1=1 --a.shda = b.shdb 
 AND a.HopDongID = b.HopDongID
 AND a.HopDongChiTietID = b.HopDongChiTietREF
 AND a.DmSanPhamREF = b.DmSanPhamREF
 and a.TenSanPham = b.TenSanPham
 ) 
	 WHERE round(a.tthd - b.thanhtientc,0) <-2	 OR (a.tthd IS NULL)OR b.thanhtientc < 0 
	 AND a.DmSanPhamREF IN (SELECT  DmSanPhamREF FROM DmSanPhamThucChay WHERE DeletedStatus <> 1)  	
 ORDER BY a.DmSanPhamREF,a.HopDongID,a.HopDongChiTietID 
 END
 
ELSE IF @LoaiCheck = 42
BEGIN
SELECT a.*, b.*, (a.tthd - b.thanhtientc)FROM ( 
 SELECT sohopdong shda, hd.HopDongID, HopDongChiTietID,(CASE WHEN hdct.DeletedStatus = 1 THEN 0 else SUM(Thanhtien)END)tthd
   FROM HopDong hd INNER JOIN HopDongChiTiet hdct
 ON hd.HopDongID = hdct.HopDongFK
 WHERE 1=1--hd.SoHopDong NOT IN ('QC800113','QC2190913','QC1811013','QC1041113','DT1180913','DT151113')
AND DmSanPhamREF NOT IN (141,637,305) 
 AND hd.DeletedStatus <> 1
 AND hd.TrangThaiHopDong <> 3
 AND not (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
 AND DmLoaiREF =42
  AND hd.Nam = @Year
 GROUP BY hd.SoHopDong, HopDongID,hdct.HopDongChiTietID, hdct.DeletedStatus
 )a
 left JOIN
 ( 	
 SELECT --B.shdb,
 B.HopDongID, B.HopDongChiTietREF,sum(B.thanhtientc)thanhtientc
   FROM
 (
 SELECT --SoHopDong shdb, 
 tcdt.HopDongID, HopDongChiTietREF, 
 round(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)),0) AS thanhtientc
 FROM ThucChayDaTinh tcdt
 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 
 tcdt.DmSanPhamREF NOT IN (585,144,628,337,141,637,305) AND
 tcdt.TrangThaiHopDong <> 3
 AND tcdt.DmHinhThucQuangCao = 42
  AND tcdt.Nam = @Year
 --AND tcdt.HopDongChiTietREF IN (SELECT distinct HopDongChiTietREF FROM ThucChayDaTinh WHERE YEAR(NgayThucHien)= 2014)
 GROUP BY --sohopdong , 
 tcdt.HopDongChiTietREF, HopDongID
 
 UNION ALL
 
  SELECT --SoHopDong shdb, 
 tcdt.HopDongID, HopDongChiTietREF, 
 round(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)),0) AS thanhtientc
 FROM dbo.ThucChayDaTinhAdmarket tcdt
 WHERE tcdt.NgayThucHien <= @NgayThucHien AND 
 tcdt.DmSanPhamREF NOT IN (585,144,628,337,141,637,305) AND
 tcdt.TrangThaiHopDong <> 3
 AND tcdt.DmHinhThucQuangCao = 42
  AND tcdt.Nam = @Year
 --AND tcdt.HopDongChiTietREF IN (SELECT distinct HopDongChiTietREF FROM ThucChayDaTinh WHERE YEAR(NgayThucHien)= 2014)
 GROUP BY --sohopdong , 
 tcdt.HopDongChiTietREF, HopDongID
 

 )B GROUP BY --B.shdb,
 HopDongID, B.HopDongChiTietREF
 
 )b
 ON (1=1 --a.shda = b.shdb 
 AND a.HopDongID = b.HopDongID
 AND a.HopDongChiTietID = b.HopDongChiTietREF

 ) 
	 WHERE round(a.tthd - b.thanhtientc,0) <-2	 OR (a.tthd IS NULL)OR b.thanhtientc < 0 
	
 ORDER BY a.HopDongID,a.HopDongChiTietID 
  */END

END

```
