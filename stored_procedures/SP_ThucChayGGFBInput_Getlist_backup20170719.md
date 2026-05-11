# Stored Procedure: `ThucChayGGFBInput_Getlist_backup20170719`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-07-19 15:15:59.350000
- **Ngày sửa cuối**: 2017-07-19 15:15:59.350000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(1000)` | No |
| `@Type` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChayGGFBInput_Getlist] 1,500,'',0
CREATE PROCEDURE [dbo].[ThucChayGGFBInput_Getlist_backup20170719] 
	-- Add the parameters for the stored procedure here
	@PageIndex INT = 1,
	@RecordCount INT = 2,
	@SoHopDong NVARCHAR(500),
	@Type INT 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	-- xác đinh hợp đồng nào đã đươc bình nhập tay
	CREATE TABLE #GoogfacebookByNgay
	(
	NgayDanhSoHopDong datetime,
	HopDongID INT ,
	SoHopDong NVARCHAR(500),
	TenSanPham NVARCHAR(500),
	TK_AdMarket NVARCHAR(500),
	SoLuong int,
	DonViTinh NVARCHAR(500),
	DmLoaiBannerREF INT ,
	TenLoaiBanner NVARCHAR(500),
	NgayThucHien DATETIME ,
	SoLuongThucChay INT ,
	ThanhTienThucChay FLOAT,
	GiaTriThanhToan FLOAT,
	NgayThanhToan DATETIME,
	ChenhLech FLOAT,
	ThanhTienHopDong FLOAT,
	NhanHopDong NVARCHAR(500)
	)
	INSERT INTO #GoogfacebookByNgay
	SELECT 
    hd.NgayDanhSoHopDong,
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
    tcggfb.ThanhTienHopDong,
    CASE WHEN isnull(tcggfb.NhanHopDong,'') ='' Then
    [dbo].[fn_getListNhanHang](hd.SoHopDong,tcggfb.DmSanPhamREF,tcggfb.DonViTinh,tcggfb.DmLoaiBannerREF)
    ELSE tcggfb.NhanHopDong END  NhanHopDong
    FROM ThucChayGGFBInput tcggfb
	INNER JOIN HopDong hd ON tcggfb.SoHopDong = hd.SoHopDong
	WHERE hd.DeletedStatus = 0
	AND hd.RecordStatus <> 3
	AND tcggfb.NgayThucHien = (SELECT MAX(NgayThucHien) FROM ThucChayGGFBInput tc2 WHERE tc2.SoHopDong= tcggfb.SoHopDong)

	CREATE TABLE #tempGF
	(
		HopDongID INT,
		SoHopDong NVARCHAR(500),
		DmSanPhamREF NVARCHAR(500),
		DanhSachTaiKhoan NVARCHAR(200),
		SoLuong INT,
		DonViTinh NVARCHAR(500),
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
		NhanHopDong NVARCHAR(500)
		
	)
	CREATE TABLE #tempGF1
	(
		HopDongID INT,
		SoHopDong NVARCHAR(500),
		DmSanPhamREF NVARCHAR(500),
		DanhSachTaiKhoan NVARCHAR(200),
		SoLuong INT,
		DonViTinh NVARCHAR(500),
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
		NhanHopDong NVARCHAR(500)
	)
	DECLARE @DauNhay NVARCHAR(10) 
	SET @DauNhay = ''''
	DECLARE @SQL NVARCHAR(MAX);
	DECLARE @Review VARCHAR(200);
	IF  @SoHopDong <> ''
	BEGIN
	SET @Review = ' SoHopDong like ' + @DauNhay+'%' + @SoHopDong + '%' + @DauNhay;
	PRINT(@Review)
	END
	ELSE 
    SET @Review = ' 1=1 '
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
    A.NhanHopDong
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
    SUM(t.ChenhLech) AS ChenhLech,
    t.NhanHopDong
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
	0 as ChenhLech,
	[dbo].[fn_getListNhanHang](hd.SoHopDong,hdct.TenSanPham,hdct.DonViTinh,hdct.DmLoaiBannerREF) NhanHopDong
	FROM HopDong hd 
	INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	INNER JOIN DmLoaiBanner dlb ON hdct.DmLoaiBannerREF = dlb.DmLoaiBannerID
	WHERE hdct.DmSanPhamREF IN (306,423)
	AND convert(date,hdct.CreatedAt) >= '2013-01-01'
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
	0 as ChenhLech,
	[dbo].[fn_getListNhanHang](hd.SoHopDong,hdct.TenSanPham,hdct.DonViTinh,hdct.DmLoaiBannerREF) NhanHopDong
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
	AND convert(date,hdct.CreatedAt) >= '2013-01-01'
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
	[dbo].[fn_asd_get_giatrihopdong_ggfb](HopDongID,TenSanPham,DmLoaiBannerREF,DonViTinh) AS ThanhTien ,
	DonViTinh ,
	DmLoaiBannerREF  ,
	TenLoaiBanner ,
	NgayThucHien  ,
	SoLuongThucChay  ,
	ThanhTienThucChay ,
	GiaTriThanhToan ,
	NgayThanhToan,
	ChenhLech ,
    NhanHopDong
	FROM #GoogfacebookByNgay
	
    ) t GROUP BY t.HopDongID, t.SoHopDong,t.DmSanPhamREF,t.DonViTinh,t.NgayThucHien,t.NgayDanhSoHopDong,t.DmLoaiBannerREF,t.TenLoaiBanner,t.NgayThanhToan,t.NhanHopDong
    ) A
    PRINT('doannv')
    IF @Type = 0
    BEGIN
    	
    PRINT('doannv')
    IF(@Review =' 1=1 ')
    BEGIN
    SET @sql = 'SELECT 
				HopDongID,
				SoHopDong,
				DmSanPhamREF,
				DmLoaiBannerREF,
				TenLoaiBanner,
				DanhSachTaiKhoan ,
				dbo.FormatNumber(SoLuong) as SoLuong ,
				DonViTinh ,
				SoLuongThucChay as SoLuongThucChay ,
				ThanhTienThucChay as ThanhTienThucChay ,
				CONVERT(nvarchar(10),NgayThucHien,103) as NgayThucHien ,
				(select count(*) from #tempGF ) as TotalRows,
				GiaTriThanhToan,
				CONVERT(NVARCHAR(10),NgayThanhToan,103) AS NgayThanhToan,
			    ChenhLech,
			    dbo.FormatNumber(ThanhTienHopDong) as ThanhTienHopDong,
			    [dbo].[fn_getListNhanHang](SoHopDong,DmSanPhamREF,DonViTinh,DmLoaiBannerREF) NhanHopDong
                from #tempGF
                where 1=1 AND 
                ' + @Review + 
                ' AND RowNumber BETWEEN ' + CAST(((@PageIndex -1) * @RecordCount + 1) AS NVARCHAR(500)) + ' AND ' + CAST((@PageIndex * @RecordCount) AS NVARCHAR(500)) + ';'; 
     EXEC sp_executesql @SQL
    END
    ELSE
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
				ROW_NUMBER() OVER(ORDER BY RowNumber asc) AS [RowNumber],
				DmLoaiBannerREF,
				TenLoaiBanner,
				GiaTriThanhToan,
				NgayThanhToan,
				ChenhLech,
				ThanhTienHopDong,
				[dbo].[fn_getListNhanHang](SoHopDong,DmSanPhamREF,DonViTinh,DmLoaiBannerREF) NhanHopDong
                from #tempGF where 1=1 and 
				' +@Review ;
				PRINT(@sql) 
	EXEC sp_executesql @SQL
	SET @sql = 'SELECT 
				HopDongID,
				SoHopDong,
				DmSanPhamREF,
				DmLoaiBannerREF,
				TenLoaiBanner,
				DanhSachTaiKhoan ,
				dbo.FormatNumber(SoLuong) as SoLuong ,
				DonViTinh ,
				SoLuongThucChay as SoLuongThucChay ,
				ThanhTienThucChay as ThanhTienThucChay ,
				CONVERT(nvarchar(10),NgayThucHien,103) as NgayThucHien ,
				(select count(*) from #tempGF1 ) as TotalRows,
				GiaTriThanhToan,
				CONVERT(NVARCHAR(10),NgayThanhToan,103) AS NgayThanhToan,
			    ChenhLech,
			    dbo.FormatNumber(ThanhTienHopDong) as ThanhTienHopDong,
			   [dbo].[fn_getListNhanHang](SoHopDong,DmSanPhamREF,DonViTinh,DmLoaiBannerREF) NhanHopDong
                from #tempGF1 where '
                + ' RowNumber BETWEEN ' + CAST(((@PageIndex -1) * @RecordCount + 1) AS NVARCHAR(500)) + ' AND ' + CAST((@PageIndex * @RecordCount) AS NVARCHAR(500)) + ';'; 
                PRINT(@sql)
     EXEC sp_executesql @SQL
    	END
    END
    ELSE
    BEGIN
    	SELECT * FROM 
    	(
			SELECT NgayDanhSoHopDong ,
			HopDongID  ,
			SoHopDong ,
			TenSanPham ,
			TK_AdMarket AS DanhSachTaiKhoan ,
			SoLuong ,
			DonViTinh ,
			DmLoaiBannerREF  ,
			TenLoaiBanner ,
			Convert(nvarchar(10),NgayThucHien,103) AS NgayThucHien,
			SoLuongThucChay  ,
			ThanhTienThucChay ,
			GiaTriThanhToan ,
			ChenhLech ,
			ThanhTienHopDong,
			(SELECT TenNhanHang FROM DmNhanHang dnh WHERE convert(NVARCHAR(500),dnh.DmNhanHangID) = NhanHopDong OR dnh.TenNhanHang =  NhanHopDong) NhanHopDong,
			Convert(nvarchar(10),NgayThanhToan,103) AS NgayThanhToan,
			(SELECT COUNT(*) FROM #GoogfacebookByNgay ) AS TotalRows,
			ROW_NUMBER() OVER(ORDER BY NgayThucHien ) AS [RowNumber]
			FROM #GoogfacebookByNgay
    	) A WHERE RowNumber BETWEEN (@PageIndex -1) * @RecordCount + 1 AND (@PageIndex * @RecordCount)
    	END
    DROP TABLE #tempGF
    DROP TABLE #tempGF1
    DROP TABLE #GoogfacebookByNgay
END




```
