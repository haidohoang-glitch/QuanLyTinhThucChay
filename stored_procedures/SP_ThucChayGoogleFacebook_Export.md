# Stored Procedure: `ThucChayGoogleFacebook_Export`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-07-08 17:52:03.630000
- **Ngày sửa cuối**: 2015-07-08 17:52:03.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Type` | `int(4)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[ThucChayGoogleFacebook_Export] 0,'2015-05-01','2015-05-31',1,500,''
CREATE PROCEDURE [dbo].[ThucChayGoogleFacebook_Export]
	-- Add the parameters for the stored procedure here
	-- =0 là tìm theo ngày đanh số, băng 1 tìm theo ngày thanh toán
	@Type INT,
	@FromDate DATETIME,
	@ToDate DATETIME,
	@PageIndex INT = 1,
	@RecordCount INT = 2,
	@SoHopDong NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    -- Insert statements for procedure here
    
  CREATE TABLE #GoogfacebookByNgay
	(
	NgayDanhSoHopDong datetime,
	HopDongID INT ,
	SoHopDong NVARCHAR(50),
	TenSanPham NVARCHAR(50),
	TK_AdMarket NVARCHAR(50),
	SoLuong int,
	DonViTinh NVARCHAR(50),
	DmLoaiBannerREF INT ,
	TenLoaiBanner NVARCHAR(50),
	NgayThucHien DATETIME ,
	SoLuongThucChay INT ,
	ThanhTienThucChay FLOAT,
	GiaTriThanhToan FLOAT,
	NgayThanhToan DATETIME,
	ChenhLech FLOAT,
	ThanhTienHopDong float
	)
	PRINT ('1')
	INSERT INTO #GoogfacebookByNgay
	SELECT 
    isnull(hd.NgayDanhSoHopDong,'1900-01-01'),
    hd.HopDongID,
    hd.SoHopDong,
    tcggfb.DmSanPhamREF,
    tcggfb.DanhSachTaiKhoan,
    tcggfb.SoLuongHopDong,
    tcggfb.DonViTinh,
    tcggfb.DmLoaiBannerREF,
    tcggfb.TenLoaiBanner,
    tcggfb.NgayThucHien,
    tcggfb.SoLuongThucChay,
    tcggfb.ThanhTienThucChay,
    tcggfb.GiaTriThanhToan,
    tcggfb.NgayThanhToan,
    tcggfb.ChenhLech,
    tcggfb.ThanhTienHopDong
    FROM ThucChayGGFBInput tcggfb
	INNER JOIN HopDong hd ON tcggfb.SoHopDong = hd.SoHopDong
	WHERE hd.DeletedStatus = 0
	AND hd.RecordStatus <> 3
	AND tcggfb.NgayThucHien = (SELECT MAX(NgayThucHien) FROM ThucChayGGFBInput tc2 WHERE tc2.SoHopDong= tcggfb.SoHopDong)

	CREATE TABLE #tempGF
	(
		HopDongID INT,
		SoHopDong NVARCHAR(50),
		DmSanPhamREF NVARCHAR(50),
		DanhSachTaiKhoan NVARCHAR(200),
		SoLuong INT,
		DonViTinh NVARCHAR(50),
		SoLuongThucChay FLOAT,
		ThanhTienThucChay FLOAT,
		NgayThucHien DATETIME,
		RowNumber INT ,
		DmLoaiBannerREF INT,
		TenLoaiBanner NVARCHAR(100),
		GiaTriThanhToan FLOAT,
		NgayThanhToan DATETIME,
		ChenhLech FLOAT,
		ThanhTienHopDong FLOAT,
		NgayDanhSoHopDong DATETIME
		
	)
	CREATE TABLE #tempGF1
	(
		HopDongID INT,
		SoHopDong NVARCHAR(50),
		DmSanPhamREF NVARCHAR(50),
		DanhSachTaiKhoan NVARCHAR(200),
		SoLuong INT,
		DonViTinh NVARCHAR(50),
		SoLuongThucChay FLOAT,
		ThanhTienThucChay FLOAT,
		NgayThucHien DATETIME,
		RowNumber INT ,
		DmLoaiBannerREF INT,
		TenLoaiBanner NVARCHAR(100),
		GiaTriThanhToan FLOAT,
		NgayThanhToan DATETIME,
		ChenhLech FLOAT,
		ThanhTienHopDong FLOAT,
		NgayDanhSoHopDong DATETIME
	)
    DECLARE @swhere NVARCHAR(200)
	DECLARE @DauNhay NVARCHAR(10) 
	SET @DauNhay = ''''
	DECLARE @SQL NVARCHAR(MAX);
	DECLARE @Review VARCHAR(200);
	IF(@SoHopDong<> '')
	BEGIN
		SET @swhere = ' AND SoHopDong like ' + @DauNhay+'%' + @SoHopDong + '%' + @DauNhay;	
	END
	ELSE SET @swhere =' AND 1=1 '
	SET @Review = ' NgayDanhSoHopDong between ' + @DauNhay + '' + Convert(nvarchar(10),@FromDate,111) + ''  + @DauNhay + ' AND ' + @DauNhay + '' + Convert(nvarchar(10),@ToDate,111) + ''  + @DauNhay;
	SET @Review = REPLACE(@Review,'/','-')
	PRINT(@Review)
    -- Insert statements for procedure here
    INSERT INTO #tempGF
    SELECT 
    A.HopDongID,
    A.SoHopDong,
    A.DmSanPhamREF,
    [dbo].[fn_GetListTK_GoogleFacebook](A.HopDongID,A.DonViTinh) AS DanhSachTaiKhoan,
    A.SoLuong,
    A.DonViTinh,
    A.SoLuongThucChay,
    A.ThanhTienThucChay,
    A.NgayThucHien,
    ROW_NUMBER() OVER(ORDER BY A.NgayDanhSoHopDong DESC,A.SoHopDong asc) AS [RowNumber],
    A.DmLoaiBannerREF,
    A.TenLoaiBanner,
    A.GiaTriThanhToan,
    A.NgayThanhToan,
    A.ChenhLech,
    A.ThanhTien,
    A.NgayDanhSoHopDong
     FROM 
    (
    SELECT 
    t.SoHopDong,
    t.DmSanPhamREF,
    t.HopDongID,
    SUM(t.SoLuong) AS SoLuong,
    SUM(t.ThanhTien) AS ThanhTien,
    t.DonViTinh,
    SUM(t.SoLuongThucChay) AS SoLuongThucChay,
    SUM(t.ThanhTienThucChay) AS ThanhTienThucChay,
    t.NgayThucHien,
    t.NgayDanhSoHopDong,
    t.DmLoaiBannerREF,
    t.TenLoaiBanner,
    SUM(t.GiaTriThanhToan) AS GiaTriThanhToan,
    t.NgayThanhToan AS NgayThanhToan,
    SUM(t.ChenhLech) AS ChenhLech
    FROM 
    (
	SELECT 
	hd.NgayDanhSoHopDong,
	hd.HopDongID,
	hd.SoHopDong,
	hdct.TenSanPham AS DmSanPhamREF,
	hdct.TK_AdMarket,
	hdct.SoLuong,
	hdct.ThanhTien,
	hdct.DonViTinh,
	hdct.DmLoaiBannerREF,
	dlb.TenLoaiBanner,
	CONVERT(DATE,GETDATE()) AS NgayThucHien,
	(SELECT isnull(SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)),0)
	        FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = hd.HopDongID AND tcdt.HopDongChiTietREF = hdct.HopDongChiTietID) AS SoLuongThucChay,
	(SELECT isnull(SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)),0)
	        FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = hd.HopDongID AND tcdt.HopDongChiTietREF = hdct.HopDongChiTietID) AS ThanhTienThucChay,      
	0 as GiaTriThanhToan,
	GETDATE() as NgayThanhToan,
	(SELECT isnull(SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)),0)
	        FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = hd.HopDongID AND tcdt.HopDongChiTietREF = hdct.HopDongChiTietID) as ChenhLech
	FROM HopDong hd 
	INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	INNER JOIN DmLoaiBanner dlb ON hdct.DmLoaiBannerREF = dlb.DmLoaiBannerID
	WHERE hdct.DmSanPhamREF IN (306,423)
	AND convert(date,hdct.CreatedAt) >= '2014-01-01'
	AND hd.TrangThaiHopDong <> 3
	AND hd.DeletedStatus <> 1
	--AND hdct.TrangThaiThucChay <> 3
	AND hdct.DeletedStatus <> 1
	AND hdct.DmLoaiREF <> 13
	AND NOT exists (SELECT #GoogfacebookByNgay.SoHopDong
	                                  FROM #GoogfacebookByNgay WHERE #GoogfacebookByNgay.SoHopDong = hd.SoHopDong
	AND hdct.TenSanPham =#GoogfacebookByNgay.TenSanPham 
	AND hdct.DonViTinh = #GoogfacebookByNgay.DonViTinh
	AND hdct.DmLoaiBannerREF = #GoogfacebookByNgay.DmLoaiBannerREF)
	
	UNION all
	SELECT 
	hd.NgayDanhSoHopDong,
	hd.HopDongID,
	hd.SoHopDong,
	hdct.TenSanPham AS DmSanPhamREF,
	hdct.TK_AdMarket,
	hdct.SoLuong,
	hdct.ThanhTien,
	hdct.DonViTinh,
	hdct.DmLoaiBannerREF,
	dlb.TenLoaiBanner,
	CONVERT(DATE,GETDATE()) AS NgayThucHien,
	(SELECT isnull(SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)),0)
	        FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = hd.HopDongID AND tcdt.HopDongChiTietREF = hdct.HopDongChiTietID) AS SoLuongThucChay,
	(SELECT isnull(SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)),0)
	        FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = hd.HopDongID AND tcdt.HopDongChiTietREF = hdct.HopDongChiTietID) AS ThanhTienThucChay ,     
	0 as GiaTriThanhToan,
	GETDATE() as NgayThanhToan,
	(SELECT isnull(SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)),0)
	        FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = hd.HopDongID AND tcdt.HopDongChiTietREF = hdct.HopDongChiTietID) as ChenhLech
	FROM HopDong hd 
	INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	INNER JOIN DmLoaiBanner dlb ON hdct.DmLoaiBannerREF = dlb.DmLoaiBannerID
	WHERE hdct.DmSanPhamREF IN (535)
	AND hd.TrangThaiHopDong <> 3
	AND hd.DeletedStatus <> 1
	--AND hdct.TrangThaiThucChay <> 3
	AND hdct.DeletedStatus <> 1
	AND hdct.DmWebsiteREF IN (285,307)
	AND hdct.DmLoaiREF <> 13
	AND convert(date,hdct.CreatedAt) >= '2014-01-01'
	AND NOT exists (SELECT #GoogfacebookByNgay.SoHopDong
	                                  FROM #GoogfacebookByNgay WHERE #GoogfacebookByNgay.SoHopDong = hd.SoHopDong
	AND hdct.TenSanPham =#GoogfacebookByNgay.TenSanPham 
	AND hdct.DonViTinh = #GoogfacebookByNgay.DonViTinh
	AND hdct.DmLoaiBannerREF = #GoogfacebookByNgay.DmLoaiBannerREF)
	--ORDER BY hd.CreatedAt DESC
	UNION all
	SELECT NgayDanhSoHopDong ,
	HopDongID  ,
	SoHopDong ,
	TenSanPham ,
	TK_AdMarket ,
	SoLuong ,
	ThanhTienHopDong AS ThanhTien ,
	DonViTinh ,
	DmLoaiBannerREF  ,
	TenLoaiBanner ,
	NgayThucHien  ,
	SoLuongThucChay  ,
	ThanhTienThucChay ,
	GiaTriThanhToan ,
	NgayThanhToan,
	ChenhLech 
    
	FROM #GoogfacebookByNgay
	
    ) t GROUP BY t.HopDongID, t.SoHopDong,t.DmSanPhamREF,t.DonViTinh,t.NgayThucHien,t.NgayDanhSoHopDong,t.DmLoaiBannerREF,t.TenLoaiBanner,t.NgayThanhToan
    ) A
    PRINT('doannv')
    IF @Type = 0
    BEGIN
    	
    SET @sql =' insert into #tempGF1
    select  
    HopDongID,
				SoHopDong,
				DmSanPhamREF ,
				DanhSachTaiKhoan ,
				SoLuong ,
				DonViTinh ,
			    SoLuongThucChay ,
				ThanhTienThucChay ,
				NgayThucHien,
				ROW_NUMBER() OVER(ORDER BY HopDongID,SoHopDong ) AS [RowNumber],
				DmLoaiBannerREF,
				TenLoaiBanner,
				GiaTriThanhToan,
				NgayThanhToan,
				ChenhLech,
				ThanhTienHopDong,
				NgayDanhSoHopDong
    from 
    (
				select 
				HopDongID,
				SoHopDong,
				DmSanPhamREF ,
				DanhSachTaiKhoan ,
				SoLuong ,
				DonViTinh ,
			    SoLuongThucChay ,
				ThanhTienThucChay ,
				NgayThucHien,
				DmLoaiBannerREF,
				TenLoaiBanner,
				GiaTriThanhToan,
				NgayThanhToan,
				ChenhLech,
				ThanhTienHopDong,
				NgayDanhSoHopDong
				
                from #tempGF where 1=1 and 
				' +@Review +  @swhere +
				--'union all'
				--+
				--' select 
				--HopDongID,
				--N''Tong'',
				--'''' ,
				--'''' ,
				--SUM(SoLuong) as SoLuong ,
				--'''' ,
			 --   SUM(SoLuongThucChay) ,
				--SUM(ThanhTienThucChay) ,
				--MAX(NgayThucHien),
				--NULL as DmLoaiBannerREF,
				--'''',
				--SUM(GiaTriThanhToan) as GiaTriThanhToan,
				--MAX(NgayThanhToan),
				--SUM(ChenhLech) as ChenhLech,
				--SUM(ThanhTienHopDong) as ThanhTienHopDong,
				--MAX(NgayDanhSoHopDong)
				
    --            from #tempGF where 1=1 and 
				--' +@Review + @swhere + 'group by HopDongID '
				+ 'union all'
				+ ' select 
			    99999999 as	HopDongID,
				N''Tongcong'',
				'''' ,
				'''' ,
				null as SoLuong ,
				'''' ,
			    null as SoLuongThucChay ,
				SUM(ThanhTienThucChay) ,
				null as NgayThucHien,
				NULL as DmLoaiBannerREF,
				'''',
				SUM(GiaTriThanhToan) as GiaTriThanhToan,
				null NgayThanhToan,
				SUM(ChenhLech) as ChenhLech,
				SUM(ThanhTienHopDong) as ThanhTienHopDong,
				null as NgayDanhSoHopDong
				
                from #tempGF where 1=1 and 
				' +@Review + @swhere + ' '
				+ ') A '

				PRINT(@sql) 
	EXEC sp_executesql @SQL
	UPDATE #tempGF1
	SET SoHopDong = N'Tổng cộng' WHERE SoHopDong = 'TongCong'
	UPDATE #tempGF1
	SET SoHopDong = N'Tổng' WHERE SoHopDong = 'Tong'
	SET @sql = 'SELECT
				HopDongID,
				SoHopDong,
				DmSanPhamREF,
				DmLoaiBannerREF,
				TenLoaiBanner,
				DanhSachTaiKhoan ,
				dbo.FormatNumber(SoLuong) as SoLuong ,
				DonViTinh ,
				dbo.FormatNumber(SoLuongThucChay) as SoLuongThucChay ,
				dbo.FormatNumber(ThanhTienThucChay) as ThanhTienThucChay ,
				CONVERT(nvarchar(10),NgayThucHien,103) as NgayThucHien ,
				(select count(*) from #tempGF1 ) -1 as TotalRows,
				dbo.FormatNumber(GiaTriThanhToan) as GiaTriThanhToan,
				CONVERT(NVARCHAR(10),NgayThanhToan,103) AS NgayThanhToan,
			    dbo.FormatNumber(ChenhLech) as ChenhLech,
			    dbo.FormatNumber(ThanhTienHopDong) as ThanhTienHopDong
                from #tempGF1 where HopDongID <> 99999999 AND '
                + ' RowNumber BETWEEN ' + CAST(((@PageIndex -1) * @RecordCount + 1) AS NVARCHAR(50)) + ' AND ' + CAST((@PageIndex * @RecordCount) AS NVARCHAR(50)) + ''
                +'  union all  '
                +'SELECT
				HopDongID,
				SoHopDong,
				DmSanPhamREF,
				DmLoaiBannerREF,
				TenLoaiBanner,
				DanhSachTaiKhoan ,
				dbo.FormatNumber(SoLuong) as SoLuong ,
				DonViTinh ,
				dbo.FormatNumber(SoLuongThucChay) as SoLuongThucChay ,
				dbo.FormatNumber(ThanhTienThucChay) as ThanhTienThucChay ,
				CONVERT(nvarchar(10),NgayThucHien,103) as NgayThucHien ,
				(select count(*) from #tempGF1 ) - 1 as TotalRows,
				dbo.FormatNumber(GiaTriThanhToan) as GiaTriThanhToan,
				CONVERT(NVARCHAR(10),NgayThanhToan,103) AS NgayThanhToan,
			    dbo.FormatNumber(ChenhLech) as ChenhLech,
			    dbo.FormatNumber(ThanhTienHopDong) as ThanhTienHopDong
                from #tempGF1 where HopDongID = 99999999'
                PRINT(@sql)
     EXEC sp_executesql @SQL
    	
    END
    ELSE
    BEGIN
    DECLARE @check INT 
    IF(@SoHopDong <>'') SET @check =1 ELSE SET @check = 0	

    SELECT 
    NgayDanhSoHopDong,
    HopDongID,
    SoHopDong ,
	TenSanPham ,
	DanhSachTaiKhoan,
	SoLuong,
	DonViTinh,
	DmLoaiBannerREF  ,
	TenLoaiBanner ,
	NgayThucHien,
	SoLuongThucChay  ,
	ThanhTienThucChay ,
	GiaTriThanhToan ,
	ChenhLech ,
	ThanhTienHopDong,
	NgayThanhToan,
	TotalRows,
	RowNumber
    FROM 
    (
    SELECT  NgayDanhSoHopDong ,
			HopDongID  ,
			SoHopDong ,
			TenSanPham ,
			DanhSachTaiKhoan ,
			dbo.FormatNumber(SoLuong) AS SoLuong ,
			DonViTinh ,
			DmLoaiBannerREF  ,
			TenLoaiBanner ,
			Convert(nvarchar(10),NgayThucHien,103) AS NgayThucHien,
			dbo.FormatNumber(SoLuongThucChay) AS SoLuongThucChay  ,
			dbo.FormatNumber(ThanhTienThucChay) AS ThanhTienThucChay ,
			dbo.FormatNumber(GiaTriThanhToan) AS GiaTriThanhToan ,
			dbo.FormatNumber(ChenhLech) AS ChenhLech ,
			dbo.FormatNumber(ThanhTienHopDong) AS ThanhTienHopDong,
			Convert(nvarchar(10),NgayThanhToan,103) AS NgayThanhToan,
			(SELECT COUNT(*) FROM #GoogfacebookByNgay  WHERE NgayThanhToan BETWEEN @FromDate AND @ToDate)
			--+ (SELECT COUNT(DISTINCT SoHopDong)   FROM #GoogfacebookByNgay where NgayThanhToan BETWEEN @FromDate AND @ToDate
			--AND (@check = 0 OR SoHopDong = @SoHopDong)) 
			 AS TotalRows,
			ROW_NUMBER() OVER(ORDER BY HopDongID,SoHopDong ) AS [RowNumber]
    	FROM
    	(
            SELECT NgayDanhSoHopDong ,
			HopDongID  ,
			SoHopDong ,
			TenSanPham ,
			TK_AdMarket AS DanhSachTaiKhoan ,
			SoLuong AS SoLuong ,
			DonViTinh ,
			DmLoaiBannerREF  ,
			TenLoaiBanner ,
			Convert(nvarchar(10),NgayThucHien,103) AS NgayThucHien,
			SoLuongThucChay AS SoLuongThucChay  ,
			ThanhTienThucChay AS ThanhTienThucChay ,
			GiaTriThanhToan AS GiaTriThanhToan ,
			ChenhLech AS ChenhLech ,
			ThanhTienHopDong AS ThanhTienHopDong,
			Convert(nvarchar(10),NgayThanhToan,103) AS NgayThanhToan
	
			FROM #GoogfacebookByNgay WHERE NgayThanhToan BETWEEN @FromDate AND @ToDate
			AND (@check = 0 OR SoHopDong = @SoHopDong)
		--UNION ALL
	 -- SELECT max(NgayDanhSoHopDong) AS NgayDanhSoHopDong ,
		--	HopDongID  ,
		--	N'Tổng' AS SoHopDong,
		--	'' ,
		--	'' AS DanhSachTaiKhoan ,
		--	sum(SoLuong) AS SoLuong ,
		--	'' ,
		--	null  ,
		--	'' ,
		--	Convert(nvarchar(10),MAX(NgayThucHien),103) AS NgayThucHien,
		--	sum(SoLuongThucChay) AS SoLuongThucChay  ,
		--	sum(ThanhTienThucChay) AS ThanhTienThucChay ,
		--	sum(GiaTriThanhToan) AS GiaTriThanhToan ,
		--	sum(ChenhLech) AS ChenhLech ,
		--	sum(ThanhTienHopDong) AS ThanhTienHopDong,
		--	Convert(nvarchar(10),MAX(NgayThanhToan),103) AS NgayThanhToan
		--	FROM #GoogfacebookByNgay 
	 --       WHERE NgayThanhToan BETWEEN @FromDate AND @ToDate
		--	AND (@check = 0 OR SoHopDong = @SoHopDong)
	 -- GROUP BY NgayDanhSoHopDong,HopDongID
    	) A 
    ) t WHERE RowNumber BETWEEN (@PageIndex -1) * @RecordCount + 1 AND (@PageIndex * @RecordCount)
  UNION ALL
	  SELECT max(NgayDanhSoHopDong) AS NgayDanhSoHopDong ,
			99999999 as HopDongID  ,
			N'Tổng cộng' AS SoHopDong,
			'' AS TenSanPham,
			'' AS DanhSachTaiKhoan ,
			null AS SoLuong ,
			'' AS DonViTinh,
			null AS DmLoaiBannerREF ,
			'' AS TenLoaiBanner,
			null AS NgayThucHien,
			null AS SoLuongThucChay  ,
			dbo.FormatNumber(sum(ThanhTienThucChay)) AS ThanhTienThucChay ,
			dbo.FormatNumber(sum(GiaTriThanhToan)) AS GiaTriThanhToan ,
			dbo.FormatNumber(sum(ChenhLech)) AS ChenhLech ,
			dbo.FormatNumber(sum(ThanhTienHopDong)) AS ThanhTienHopDong,
			null AS NgayThanhToan,
			0 TotalRows,
			0 RowNumber
			FROM #GoogfacebookByNgay 
	        WHERE NgayThanhToan BETWEEN @FromDate AND @ToDate
			AND (@check = 0 OR SoHopDong = @SoHopDong)
	
    
    END 	
    DROP TABLE #tempGF
    DROP TABLE #tempGF1
    DROP TABLE #GoogfacebookByNgay
	
END

```
