# Stored Procedure: `CompareDongBoDuLieu_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-02-02 14:13:15.067000
- **Ngày sửa cuối**: 2015-02-03 11:40:00.637000

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
--EXEC CompareDongBoDuLieu '2014-01-01','2014-12-30'

--EXEC CompareDongBoDuLieu_v2 '2015-01-03','2015-01-03'
CREATE PROCEDURE [dbo].[CompareDongBoDuLieu_v2]
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @count1 INT, @count2 INT, @count3 INT, @count4 INT, @count5 INT, @count6 INT
	SET @count1 = 1
	SET @count2 = 1
	SET @count3 = 1
	SET @count4 = 1
	SET @count5 = 1
	SET @count6 = 6
	--1. Data chinh 5.38 va 5.210
	--ThucChayDaTinh 5.38 va ThucChayDaTinh 5.210
	BEGIN		
		-- Insert statements for procedure here
		SET @count1 = (SELECT COUNT(*) FROM(
		SELECT A.*, B.*,
		(A.SLTC_Dest - B.SLTC) LechSLTC,
		(A.SLTCTD_Dest - B.SLTCTD) LechSLTCTD,
		(A.SLKM_Dest - B.SLKM) LechSLKM,
		(A.SLKMTD_Dest - B.SLKMTD) LechSLKMTD,  
		(A.TTTC_Dest - B.TTTC) LechTTTC,
		(A.GTTD_Dest - B.GTTD) LechGTTD,
		(A.TTKM_Dest - B.TTKM) LechTTTCKM,
		(A.GTTDKM_Dest - B.GTTDKM) LechGTTDKM
	    
		FROM (
		SELECT 
		tcdt.DmSanPhamREF DmSanPhamREF_Dest, 
		tcdt.TenSanPham TenSanPham_Dest,
		tcdt.SoHopDong SoHopDong_Dest,
		tcdt.HopDongID HopDongID_Dest,
		tcdt.HopDongChiTietREF HopDongChiTietREF_Dest,
        tcdt.DonViTinh DonViTinh_Dest, 
		tcdt.DmHinhThucQuangCao DmHinhThucQuangCao_Dest,
		tcdt.TenHinhThucQuangCao TenHinhThucQuangCao_Dest,
		tcdt.NgayThucHien NgayThucHien_Dest,
		tcdt.IsKhuyenMai IsKhuyenMai_Dest,
		--DmWebsiteREF, TenWebsite,
		SUM(ISNULL(tcdt.SoLuongThucChay,0)) SLTC_Dest,
		SUM(ISNULL(tcdt.SoLuongThayDoi,0)) SLTCTD_Dest,
		SUM(ISNULL (tcdt.SoLuongThucChayKM,0)) SLKM_Dest,
		SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) SLKMTD_Dest,
		SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0))TTTC_Dest,
		SUM(ISNULL(tcdt.GiaTriThayDoi,0)) GTTD_Dest,
		SUM(ISNULL (tcdt.ThanhTienKM,0)) TTKM_Dest,
		SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))GTTDKM_Dest
		FROM [10.3.14.4].ABM_Test.dbo.ThucChayDaTinh tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
		HopDongID,HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao
		,IsKhuyenMai
		)A
		FULL OUTER JOIN
		(
		SELECT tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,HopDongID,HopDongChiTietREF,
		DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,
		NgayThucHien,IsKhuyenMai,--DmWebsiteREF, TenWebsite,
		SUM(ISNULL(tcdt.SoLuongThucChay,0)) SLTC,
		SUM(ISNULL(tcdt.SoLuongThayDoi,0)) SLTCTD,
		SUM(ISNULL (tcdt.SoLuongThucChayKM,0)) SLKM,
		SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) SLKMTD,
		SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0))TTTC,
		SUM(ISNULL(tcdt.GiaTriThayDoi,0)) GTTD,
		SUM(ISNULL (tcdt.ThanhTienKM,0)) TTKM,
		SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))GTTDKM
		FROM ThucChayDaTinh tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,HopDongID,
		HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,IsKhuyenMai
		--,DmWebsiteREF, TenWebsite
		)B
		ON (
		A.DmSanPhamREF_Dest = B.DmSanPhamREF
		AND A.TenSanPham_Dest = B.TenSanPham
		AND A.SoHopDong_Dest = B.SoHopDong
		AND A.NgayThucHien_Dest = B.NgayThucHien
		AND A.HopDongID_Dest = B.HopDongID
		AND A.HopDongChiTietREF_Dest = B.HopDongChiTietREF
		AND A.DonViTinh_Dest = B.DonViTinh
		AND A.DmHinhThucQuangCao_Dest = B.DmHinhThucQuangCao
		AND A.TenHinhThucQuangCao_Dest = B.TenHinhThucQuangCao
		AND A.IsKhuyenMai_Dest = B.IsKhuyenMai
		--AND A.DmWebsiteREF = B.DmWebsiteREF
		--AND A.TenWebsite = B.TenWebsite
		)
		WHERE(
		ROUND(A.SLTC_Dest - B.SLTC,0) <> 0 OR
		ROUND(A.SLTCTD_Dest - B.SLTCTD,0) <> 0 OR
		ROUND(A.SLKM_Dest - B.SLKM,0) <> 0 OR
		ROUND(A.SLKM_Dest - B.SLKM,0) <> 0 OR
		ROUND(A.TTTC_Dest - B.TTTC,0) <> 0 OR
		ROUND(A.GTTD_Dest - B.GTTD,0) <> 0 OR
		ROUND(A.TTKM_Dest - B.TTKM,0) <> 0 OR
		ROUND(A.GTTDKM_Dest - B.GTTDKM,0) <> 0
		) OR (
		A.DmSanPhamREF_Dest IS NULL OR B.DmSanPhamREF IS NULL OR 
		A.TenSanPham_Dest IS NULL OR B.TenSanPham IS NULL OR
		A.SoHopDong_Dest IS NULL OR B.SoHopDong IS NULL OR
		A.HopDongChiTietREF_Dest IS NULL OR B.HopDongChiTietREF IS NULL OR
		A.DonViTinh_Dest IS NULL OR B.DonViTinh IS NULL OR
		A.DmHinhThucQuangCao_Dest IS NULL OR B.DmHinhThucQuangCao IS NULL OR
		A.TenHinhThucQuangCao_Dest IS NULL OR B.TenHinhThucQuangCao IS NULL OR
		A.IsKhuyenMai_Dest IS NULL OR B.IsKhuyenMai IS NULL 
		)
		)TCDT)
		
		IF @count1 = 0 
			PRINT 'Successful ThucChayDaTinh 5.38 - ThucChayDaTinh 5.210'
		ELSE
			PRINT  'Failed ThucChayDaTinh 5.38 - ThucChayDaTinh 5.210'
    END
    --ThucChayDaTinh 5.38 va ThucChayDaTinhTemp 5.210
    BEGIN    	
		SET @count2 = (SELECT COUNT(*) FROM (
		-- Insert statements for procedure here
		SELECT A.*, B.*,
		(A.SLTC_Dest - B.SLTC) LechSLTC,
		(A.SLTCTD_Dest - B.SLTCTD) LechSLTCTD,
		(A.SLKM_Dest - B.SLKM) LechSLKM,
		(A.SLKMTD_Dest - B.SLKMTD) LechSLKMTD,  
		(A.TTTC_Dest - B.TTTC) LechTTTC,
		(A.GTTD_Dest - B.GTTD) LechGTTD,
		(A.TTKM_Dest - B.TTKM) LechTTTCKM,
		(A.GTTDKM_Dest - B.GTTDKM) LechGTTDKM
	    
		FROM (
		SELECT 
		tcdt.DmSanPhamREF DmSanPhamREF_Dest, 
		tcdt.TenSanPham TenSanPham_Dest,
		SoHopDong SoHopDong_Dest,
		HopDongID HopDongID_Dest,
		HopDongChiTietREF HopDongChiTietREF_Dest ,
		DonViTinh DonViTinh_Dest, 
		DmHinhThucQuangCao DmHinhThucQuangCao_Dest,TenHinhThucQuangCao TenHinhThucQuangCao_Dest,
		NgayThucHien NgayThucHien_Dest,
		IsKhuyenMai IsKhuyenMai_Dest,
		SUM(ISNULL(tcdt.SoLuongThucChay,0)) SLTC_Dest,
		SUM(ISNULL(tcdt.SoLuongThayDoi,0)) SLTCTD_Dest,
		SUM(ISNULL (tcdt.SoLuongThucChayKM,0)) SLKM_Dest,
		SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) SLKMTD_Dest,
		SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0))TTTC_Dest,
		SUM(ISNULL(tcdt.GiaTriThayDoi,0)) GTTD_Dest,
		SUM(ISNULL (tcdt.ThanhTienKM,0)) TTKM_Dest,
		SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))GTTDKM_Dest
		FROM [10.3.14.4].ABM_Test.dbo.ThucChayDaTinhTemp tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
		HopDongID,HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao
		,IsKhuyenMai--,DmWebsiteREF, TenWebsite
		)A
		FULL OUTER JOIN
		(
		SELECT tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,HopDongID,HopDongChiTietREF,
		DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,
		NgayThucHien,IsKhuyenMai,--DmWebsiteREF, TenWebsite,
		SUM(ISNULL(tcdt.SoLuongThucChay,0)) SLTC,
		SUM(ISNULL(tcdt.SoLuongThayDoi,0)) SLTCTD,
		SUM(ISNULL (tcdt.SoLuongThucChayKM,0)) SLKM,
		SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) SLKMTD,
		SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0))TTTC,
		SUM(ISNULL(tcdt.GiaTriThayDoi,0)) GTTD,
		SUM(ISNULL (tcdt.ThanhTienKM,0)) TTKM,
		SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))GTTDKM
		FROM ThucChayDaTinh tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,HopDongID,
		HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,IsKhuyenMai
		)B
		ON (
		A.DmSanPhamREF_Dest = B.DmSanPhamREF
		AND A.TenSanPham_Dest = B.TenSanPham
		AND A.SoHopDong_Dest = B.SoHopDong
		AND A.NgayThucHien_Dest = B.NgayThucHien
		AND A.HopDongID_Dest = B.HopDongID
		AND A.HopDongChiTietREF_Dest = B.HopDongChiTietREF
		AND A.DonViTinh_Dest = B.DonViTinh
		AND A.DmHinhThucQuangCao_Dest = B.DmHinhThucQuangCao
		AND A.TenHinhThucQuangCao_Dest = B.TenHinhThucQuangCao
		AND A.IsKhuyenMai_Dest = B.IsKhuyenMai
		)
		WHERE(
		ROUND(A.SLTC_Dest - B.SLTC,0) <> 0 OR
		ROUND(A.SLTCTD_Dest - B.SLTCTD,0) <> 0 OR
		ROUND(A.SLKM_Dest - B.SLKM,0) <> 0 OR
		ROUND(A.SLKM_Dest - B.SLKM,0) <> 0 OR
		ROUND(A.TTTC_Dest - B.TTTC,0) <> 0 OR
		ROUND(A.GTTD_Dest - B.GTTD,0) <> 0 OR
		ROUND(A.TTKM_Dest - B.TTKM,0) <> 0 OR
		ROUND(A.GTTDKM_Dest - B.GTTDKM,0) <> 0
		) OR (
		A.DmSanPhamREF_Dest IS NULL OR B.DmSanPhamREF IS NULL OR 
		A.TenSanPham_Dest IS NULL OR B.TenSanPham IS NULL OR
		A.SoHopDong_Dest IS NULL OR B.SoHopDong IS NULL OR
		A.HopDongChiTietREF_Dest IS NULL OR B.HopDongChiTietREF IS NULL OR
		A.DonViTinh_Dest IS NULL OR B.DonViTinh IS NULL OR
		A.DmHinhThucQuangCao_Dest IS NULL OR B.DmHinhThucQuangCao IS NULL OR
		A.TenHinhThucQuangCao_Dest IS NULL OR B.TenHinhThucQuangCao IS NULL OR
		A.IsKhuyenMai_Dest IS NULL OR B.IsKhuyenMai IS NULL
		)
		)TCDTTemp)
		IF @count2 = 0 
			PRINT 'Successful ThucChayDaTinh 5.38 - ThucChayDaTinhTemp 5.210'
		ELSE
			PRINT  'Failed ThucChayDaTinh 5.38 - ThucChayDaTinhTemp 5.210'			
    END
    --ThucChayDaTinhAdmarket 5.38 va ThucChayDaTinhAdmarket 5.210
    BEGIN
    
    -- Insert statements for procedure here
		SET @count3 = (SELECT COUNT(*) FROM(
		SELECT A.*, B.*,
		(A.SLTC_Dest - B.SLTC) LechSLTC,
		(A.SLTCTD_Dest - B.SLTCTD) LechSLTCTD,
		(A.SLKM_Dest - B.SLKM) LechSLKM,
		(A.SLKMTD_Dest - B.SLKMTD) LechSLKMTD,  
		(A.TTTC_Dest - B.TTTC) LechTTTC,
		(A.GTTD_Dest - B.GTTD) LechGTTD,
		(A.TTKM_Dest - B.TTKM) LechTTTCKM,
		(A.GTTDKM_Dest - B.GTTDKM) LechGTTDKM
	    
		FROM (
		SELECT 
		tcdt.DmSanPhamREF DmSanPhamREF_Dest, 
		tcdt.TenSanPham TenSanPham_Dest,
		tcdt.SoHopDong SoHopDong_Dest,
		tcdt.HopDongID HopDongID_Dest,
		tcdt.HopDongChiTietREF HopDongChiTietREF_Dest,
        tcdt.DonViTinh DonViTinh_Dest, 
		tcdt.DmHinhThucQuangCao DmHinhThucQuangCao_Dest,
		tcdt.TenHinhThucQuangCao TenHinhThucQuangCao_Dest,
		tcdt.NgayThucHien NgayThucHien_Dest,
		tcdt.IsKhuyenMai IsKhuyenMai_Dest,
		--DmWebsiteREF, TenWebsite,
		SUM(ISNULL(tcdt.SoLuongThucChay,0)) SLTC_Dest,
		SUM(ISNULL(tcdt.SoLuongThayDoi,0)) SLTCTD_Dest,
		SUM(ISNULL (tcdt.SoLuongThucChayKM,0)) SLKM_Dest,
		SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) SLKMTD_Dest,
		SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0))TTTC_Dest,
		SUM(ISNULL(tcdt.GiaTriThayDoi,0)) GTTD_Dest,
		SUM(ISNULL (tcdt.ThanhTienKM,0)) TTKM_Dest,
		SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))GTTDKM_Dest
		FROM [10.3.14.4].ABM_Test.dbo.ThucChayDaTinhAdmarket tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
		HopDongID,HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao
		,IsKhuyenMai
		)A
		FULL OUTER JOIN
		(
		SELECT tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,HopDongID,HopDongChiTietREF,
		DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,
		NgayThucHien,IsKhuyenMai,--DmWebsiteREF, TenWebsite,
		SUM(ISNULL(tcdt.SoLuongThucChay,0)) SLTC,
		SUM(ISNULL(tcdt.SoLuongThayDoi,0)) SLTCTD,
		SUM(ISNULL (tcdt.SoLuongThucChayKM,0)) SLKM,
		SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) SLKMTD,
		SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0))TTTC,
		SUM(ISNULL(tcdt.GiaTriThayDoi,0)) GTTD,
		SUM(ISNULL (tcdt.ThanhTienKM,0)) TTKM,
		SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))GTTDKM
		FROM ThucChayDaTinhAdmarket tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,HopDongID,
		HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,IsKhuyenMai
		--,DmWebsiteREF, TenWebsite
		)B
		ON (
		A.DmSanPhamREF_Dest = B.DmSanPhamREF
		AND A.TenSanPham_Dest = B.TenSanPham
		AND A.SoHopDong_Dest = B.SoHopDong
		AND A.NgayThucHien_Dest = B.NgayThucHien
		AND A.HopDongID_Dest = B.HopDongID
		AND A.HopDongChiTietREF_Dest = B.HopDongChiTietREF
		AND A.DonViTinh_Dest = B.DonViTinh
		AND A.DmHinhThucQuangCao_Dest = B.DmHinhThucQuangCao
		AND A.TenHinhThucQuangCao_Dest = B.TenHinhThucQuangCao
		AND A.IsKhuyenMai_Dest = B.IsKhuyenMai
		--AND A.DmWebsiteREF = B.DmWebsiteREF
		--AND A.TenWebsite = B.TenWebsite
		)
		WHERE(
		ROUND(A.SLTC_Dest - B.SLTC,0) <> 0 OR
		ROUND(A.SLTCTD_Dest - B.SLTCTD,0) <> 0 OR
		ROUND(A.SLKM_Dest - B.SLKM,0) <> 0 OR
		ROUND(A.SLKM_Dest - B.SLKM,0) <> 0 OR
		ROUND(A.TTTC_Dest - B.TTTC,0) <> 0 OR
		ROUND(A.GTTD_Dest - B.GTTD,0) <> 0 OR
		ROUND(A.TTKM_Dest - B.TTKM,0) <> 0 OR
		ROUND(A.GTTDKM_Dest - B.GTTDKM,0) <> 0
		) OR (
		A.DmSanPhamREF_Dest IS NULL OR B.DmSanPhamREF IS NULL OR 
		A.TenSanPham_Dest IS NULL OR B.TenSanPham IS NULL OR
		A.SoHopDong_Dest IS NULL OR B.SoHopDong IS NULL OR
		A.HopDongChiTietREF_Dest IS NULL OR B.HopDongChiTietREF IS NULL OR
		A.DonViTinh_Dest IS NULL OR B.DonViTinh IS NULL OR
		A.DmHinhThucQuangCao_Dest IS NULL OR B.DmHinhThucQuangCao IS NULL OR
		A.TenHinhThucQuangCao_Dest IS NULL OR B.TenHinhThucQuangCao IS NULL OR
		A.IsKhuyenMai_Dest IS NULL OR B.IsKhuyenMai IS NULL 
		)
		)TCDT)   
		
		IF @count3 = 0 
			PRINT 'Successful ThucChayDaTinhAdmarket 5.38 - ThucChayDaTinhAdmarket 5.210'
		ELSE
			PRINT  'Failed ThucChayDaTinhAdmarket 5.38 - ThucChayDaTinhAdmarket 5.210'       
    END
    
     --ThucChayDaTinhAdmarket 5.38 va ThucChayDaTinhAdmarket 5.210
    BEGIN
    
    -- Insert statements for procedure here
    SET @count4 = (SELECT COUNT(*) FROM(
		SELECT A.*, B.*,
		(A.SLTC_Dest - B.SLTC) LechSLTC,
		(A.SLTCTD_Dest - B.SLTCTD) LechSLTCTD,
		(A.SLKM_Dest - B.SLKM) LechSLKM,
		(A.SLKMTD_Dest - B.SLKMTD) LechSLKMTD,  
		(A.TTTC_Dest - B.TTTC) LechTTTC,
		(A.GTTD_Dest - B.GTTD) LechGTTD,
		(A.TTKM_Dest - B.TTKM) LechTTTCKM,
		(A.GTTDKM_Dest - B.GTTDKM) LechGTTDKM
	    
		FROM (
		SELECT 
		tcdt.DmSanPhamREF DmSanPhamREF_Dest, 
		tcdt.TenSanPham TenSanPham_Dest,
		tcdt.SoHopDong SoHopDong_Dest,
		tcdt.HopDongID HopDongID_Dest,
		tcdt.HopDongChiTietREF HopDongChiTietREF_Dest,
        tcdt.DonViTinh DonViTinh_Dest, 
		tcdt.DmHinhThucQuangCao DmHinhThucQuangCao_Dest,
		tcdt.TenHinhThucQuangCao TenHinhThucQuangCao_Dest,
		tcdt.NgayThucHien NgayThucHien_Dest,
		tcdt.IsKhuyenMai IsKhuyenMai_Dest,
		--DmWebsiteREF, TenWebsite,
		SUM(ISNULL(tcdt.SoLuongThucChay,0)) SLTC_Dest,
		SUM(ISNULL(tcdt.SoLuongThayDoi,0)) SLTCTD_Dest,
		SUM(ISNULL (tcdt.SoLuongThucChayKM,0)) SLKM_Dest,
		SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) SLKMTD_Dest,
		SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0))TTTC_Dest,
		SUM(ISNULL(tcdt.GiaTriThayDoi,0)) GTTD_Dest,
		SUM(ISNULL (tcdt.ThanhTienKM,0)) TTKM_Dest,
		SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))GTTDKM_Dest
		FROM [10.3.14.4].ABM_Test.dbo.ThucChayDaTinhAdmarket tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
		HopDongID,HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao
		,IsKhuyenMai
		)A
		FULL OUTER JOIN
		(
		SELECT tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,HopDongID,HopDongChiTietREF,
		DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,
		NgayThucHien,IsKhuyenMai,--DmWebsiteREF, TenWebsite,
		SUM(ISNULL(tcdt.SoLuongThucChay,0)) SLTC,
		SUM(ISNULL(tcdt.SoLuongThayDoi,0)) SLTCTD,
		SUM(ISNULL (tcdt.SoLuongThucChayKM,0)) SLKM,
		SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) SLKMTD,
		SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0))TTTC,
		SUM(ISNULL(tcdt.GiaTriThayDoi,0)) GTTD,
		SUM(ISNULL (tcdt.ThanhTienKM,0)) TTKM,
		SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))GTTDKM
		FROM ThucChayDaTinhAdmarket tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,HopDongID,
		HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,IsKhuyenMai
		--,DmWebsiteREF, TenWebsite
		)B
		ON (
		A.DmSanPhamREF_Dest = B.DmSanPhamREF
		AND A.TenSanPham_Dest = B.TenSanPham
		AND A.SoHopDong_Dest = B.SoHopDong
		AND A.NgayThucHien_Dest = B.NgayThucHien
		AND A.HopDongID_Dest = B.HopDongID
		AND A.HopDongChiTietREF_Dest = B.HopDongChiTietREF
		AND A.DonViTinh_Dest = B.DonViTinh
		AND A.DmHinhThucQuangCao_Dest = B.DmHinhThucQuangCao
		AND A.TenHinhThucQuangCao_Dest = B.TenHinhThucQuangCao
		AND A.IsKhuyenMai_Dest = B.IsKhuyenMai
		--AND A.DmWebsiteREF = B.DmWebsiteREF
		--AND A.TenWebsite = B.TenWebsite
		)
		WHERE(
		ROUND(A.SLTC_Dest - B.SLTC,0) <> 0 OR
		ROUND(A.SLTCTD_Dest - B.SLTCTD,0) <> 0 OR
		ROUND(A.SLKM_Dest - B.SLKM,0) <> 0 OR
		ROUND(A.SLKM_Dest - B.SLKM,0) <> 0 OR
		ROUND(A.TTTC_Dest - B.TTTC,0) <> 0 OR
		ROUND(A.GTTD_Dest - B.GTTD,0) <> 0 OR
		ROUND(A.TTKM_Dest - B.TTKM,0) <> 0 OR
		ROUND(A.GTTDKM_Dest - B.GTTDKM,0) <> 0
		) OR (
		A.DmSanPhamREF_Dest IS NULL OR B.DmSanPhamREF IS NULL OR 
		A.TenSanPham_Dest IS NULL OR B.TenSanPham IS NULL OR
		A.SoHopDong_Dest IS NULL OR B.SoHopDong IS NULL OR
		A.HopDongChiTietREF_Dest IS NULL OR B.HopDongChiTietREF IS NULL OR
		A.DonViTinh_Dest IS NULL OR B.DonViTinh IS NULL OR
		A.DmHinhThucQuangCao_Dest IS NULL OR B.DmHinhThucQuangCao IS NULL OR
		A.TenHinhThucQuangCao_Dest IS NULL OR B.TenHinhThucQuangCao IS NULL OR
		A.IsKhuyenMai_Dest IS NULL OR B.IsKhuyenMai IS NULL 
		)
		)TCDT)   
		
		IF @count4 = 0 
			PRINT 'Successful ThucChayDaTinhAdmarket 5.38 - ThucChayDaTinhAdmarketTemp 5.210'
		ELSE
			PRINT  'Failed ThucChayDaTinhAdmarket 5.38 - ThucChayDaTinhAdmarketTemp 5.210'      
    END
    
     --ThucChayDaTinhBySanPhamThoiGian 5.38 va ThucChayDaTinhBySanPhamThoiGian 5.210
    BEGIN
    
    -- Insert statements for procedure here
		SET @count5 = (SELECT COUNT(*) FROM(
		SELECT A.*, B.*,
		(A.SLTCNB_Dest - B.SLTCNB) LechSLTCNB,
		(A.SLTCKM_Dest - B.SLTCKM) LechSLTCKM,
		(A.SLTC_Dest - B.SLTC) LechSLTC,
		(A.TTTCNB_Dest - B.TTTCNB) LechTTTCNB,
		(A.TTTCKM_Dest - B.TTTCKM) LechTTTCKM,
		(A.TTTC_Dest - B.TTTC) LechTTTC,
		(A.GTTDNB_Dest - B.GTTDNB) LechGTTDNB,
		(A.GTTDTC_Dest - B.GTTDTC) LechGTTDTC
	    
		FROM (
		SELECT 
		tcdt.DmSanPhamREF DmSanPhamREF_Dest, tcdt.TenSanPham TenSanPham_Dest,
		tcdt.SoHopDong SoHopDong_Dest,tcdt.HopDongID HopDongID_Dest,
        tcdt.DonViTinh DonViTinh_Dest, 
		tcdt.DmHinhThucQuangCao DmHinhThucQuangCao_Dest,tcdt.TenHinhThucQuangCao TenHinhThucQuangCao_Dest,
		tcdt.DmMaHopDongREF DmMaHopDongREF_Dest,tcdt.TenMaHopDong TenMaHopDong_Dest,
		tcdt.NgayThucHien NgayThucHien_Dest,	
		DmPhongBanREF DmPhongBanREF_Dest,TenPhongBan TenPhongBan_Dest,
		DmBoPhanREF DmBoPhanREF_Dest,TenBoPhan TenBoPhan_Dest,
		DmNhomLamViecREF DmNhomLamViecREF_Dest, TenNhomLamViec TenNhomLamViec_Dest,
		SysNhanVienREF SysNhanVienREF_Dest, TenDangNhap TenDangNhap_Dest, TenNhanVien TenNhanVien_Dest,
		SUM(ISNULL(tcdt.SoLuongThucChayNoiBo,0)) SLTCNB_Dest,
		SUM(ISNULL(tcdt.SoLuongThucChayKhuyenMai,0)) SLTCKM_Dest,
		SUM(ISNULL (tcdt.SoLuongThucChay,0)) SLTC_Dest,
		SUM(ISNULL(tcdt.ThanhTienThucChayNoiBo,0)) TTTCNB_Dest,
		SUM(ISNULL(tcdt.ThanhTienThucChayKhuyenMai,0))TTTCKM_Dest,
		SUM(ISNULL(tcdt.ThanhTienThucChay,0)) TTTC_Dest,
		SUM(ISNULL (tcdt.GiaTriThayDoiNoiBo,0)) GTTDNB_Dest,
		SUM(ISNULL(tcdt.GiaTriThayDoiThucChay,0))GTTDTC_Dest
		FROM [10.3.14.4].ABM_Test.dbo.ThucChayDaTinhBySanPhamThoiGian tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
		HopDongID,DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,
		tcdt.DmMaHopDongREF,
		tcdt.TenMaHopDong,DmPhongBanREF,TenPhongBan,
		DmBoPhanREF,TenBoPhan,
		DmNhomLamViecREF, TenNhomLamViec,
		SysNhanVienREF, TenDangNhap, TenNhanVien
		)A
		FULL OUTER JOIN
		(
		SELECT 
		tcdt.DmSanPhamREF, 
		tcdt.TenSanPham,
		tcdt.SoHopDong,
		tcdt.HopDongID,
        tcdt.DonViTinh, 
		tcdt.DmHinhThucQuangCao,
		tcdt.TenHinhThucQuangCao,
		tcdt.NgayThucHien,	
		tcdt.DmMaHopDongREF,
		tcdt.TenMaHopDong,
		DmPhongBanREF,TenPhongBan,
		DmBoPhanREF,TenBoPhan,
		DmNhomLamViecREF, TenNhomLamViec,
		SysNhanVienREF, TenDangNhap, TenNhanVien,
		SUM(ISNULL(tcdt.SoLuongThucChayNoiBo,0)) SLTCNB,
		SUM(ISNULL(tcdt.SoLuongThucChayKhuyenMai,0)) SLTCKM,
		SUM(ISNULL (tcdt.SoLuongThucChay,0)) SLTC,
		SUM(ISNULL(tcdt.ThanhTienThucChayNoiBo,0)) TTTCNB,
		SUM(ISNULL(tcdt.ThanhTienThucChayKhuyenMai,0))TTTCKM,
		SUM(ISNULL(tcdt.ThanhTienThucChay,0)) TTTC,
		SUM(ISNULL (tcdt.GiaTriThayDoiNoiBo,0)) GTTDNB,
		SUM(ISNULL(tcdt.GiaTriThayDoiThucChay,0))GTTDTC
		FROM dbo.ThucChayDaTinhBySanPhamThoiGian tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
		HopDongID,DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,
		tcdt.DmMaHopDongREF,
		tcdt.TenMaHopDong,DmPhongBanREF,TenPhongBan,
		DmBoPhanREF,TenBoPhan,
		DmNhomLamViecREF, TenNhomLamViec,
		SysNhanVienREF, TenDangNhap, TenNhanVien
		)B
		ON (
		A.DmSanPhamREF_Dest = B.DmSanPhamREF
		AND A.TenSanPham_Dest = B.TenSanPham
		AND A.SoHopDong_Dest = B.SoHopDong
		AND A.NgayThucHien_Dest = B.NgayThucHien
		AND A.HopDongID_Dest = B.HopDongID
		AND A.DonViTinh_Dest = B.DonViTinh
		AND A.DmHinhThucQuangCao_Dest = B.DmHinhThucQuangCao
		AND A.TenHinhThucQuangCao_Dest = B.TenHinhThucQuangCao
		AND A.DmMaHopDongREF_Dest = B.DmMaHopDongREF
		AND A.TenMaHopDong_Dest = B.TenMaHopDong
		AND A.DmPhongBanREF_Dest = B.DmPhongBanREF
		AND A.TenPhongBan_Dest = B.TenPhongBan
		AND A.DmBoPhanREF_Dest = B.DmBoPhanREF AND A.TenBoPhan_Dest = B.TenBoPhan
		AND A.DmNhomLamViecREF_Dest = B.DmNhomLamViecREF AND A.TenNhomLamViec_Dest = B.TenNhomLamViec
		AND A.SysNhanVienREF_Dest = B.SysNhanVienREF 
		AND A.TenDangNhap_Dest = B.TenDangNhap AND A.TenNhanVien_Dest = B.TenNhanVien
		)
		WHERE(
		ROUND(A.SLTCNB_Dest - B.SLTCNB,0) <> 0 OR
		ROUND(A.SLTCKM_Dest - B.SLTCKM,0) <> 0 OR
		ROUND(A.SLTC_Dest - B.SLTC,0) <> 0 OR
		ROUND(A.TTTCNB_Dest - B.TTTCNB,0) <> 0 OR
		ROUND(A.TTTCKM_Dest - B.TTTCKM,0) <> 0 OR
		ROUND(A.TTTC_Dest - B.TTTC,0) <> 0 OR
		ROUND(A.GTTDNB_Dest - B.GTTDNB,0) <> 0 OR
		ROUND(A.GTTDTC_Dest - B.GTTDTC,0) <> 0
		) OR (
		A.DmSanPhamREF_Dest IS NULL OR B.DmSanPhamREF IS NULL OR 
		A.TenSanPham_Dest IS NULL OR B.TenSanPham IS NULL OR
		A.SoHopDong_Dest IS NULL OR B.SoHopDong IS NULL OR
		A.DonViTinh_Dest IS NULL OR B.DonViTinh IS NULL OR
		A.DmHinhThucQuangCao_Dest IS NULL OR B.DmHinhThucQuangCao IS NULL OR
		A.TenHinhThucQuangCao_Dest IS NULL OR B.TenHinhThucQuangCao IS NULL
		)
		)TCDT)   
		
		IF @count5 = 0 
			PRINT 'Successful ThucChayDaTinhBySanPhamThoiGian 5.38 - ThucChayDaTinhBySanPhamThoiGian 5.210'
		ELSE
			PRINT  'Failed ThucChayDaTinhBySanPhamThoiGian 5.38 - ThucChayDaTinhBySanPhamThoiGian 5.210'       
    END
    
     --ThucChayDaTinhAdmarket 5.38 va ThucChayDaTinhAdmarket 5.210
   --ThucChayDaTinhBySanPhamThoiGian 5.38 va ThucChayDaTinhBySanPhamThoiGian 5.210
    BEGIN
    
    -- Insert statements for procedure here
		SET @count6 = (SELECT COUNT(*) FROM(
		SELECT A.*, B.*,
		(A.SLTCNB_Dest - B.SLTCNB) LechSLTCNB,
		(A.SLTCKM_Dest - B.SLTCKM) LechSLTCKM,
		(A.SLTC_Dest - B.SLTC) LechSLTC,
		(A.TTTCNB_Dest - B.TTTCNB) LechTTTCNB,
		(A.TTTCKM_Dest - B.TTTCKM) LechTTTCKM,
		(A.TTTC_Dest - B.TTTC) LechTTTC,
		(A.GTTDNB_Dest - B.GTTDNB) LechGTTDNB,
		(A.GTTDTC_Dest - B.GTTDTC) LechGTTDTC
	    
		FROM (
		SELECT 
		tcdt.DmSanPhamREF DmSanPhamREF_Dest, tcdt.TenSanPham TenSanPham_Dest,
		tcdt.SoHopDong SoHopDong_Dest,tcdt.HopDongID HopDongID_Dest,
        tcdt.DonViTinh DonViTinh_Dest, 
		tcdt.DmHinhThucQuangCao DmHinhThucQuangCao_Dest,tcdt.TenHinhThucQuangCao TenHinhThucQuangCao_Dest,
		tcdt.DmMaHopDongREF DmMaHopDongREF_Dest,tcdt.TenMaHopDong TenMaHopDong_Dest,
		tcdt.NgayThucHien NgayThucHien_Dest,	
		DmPhongBanREF DmPhongBanREF_Dest,TenPhongBan TenPhongBan_Dest,
		DmBoPhanREF DmBoPhanREF_Dest,TenBoPhan TenBoPhan_Dest,
		DmNhomLamViecREF DmNhomLamViecREF_Dest, TenNhomLamViec TenNhomLamViec_Dest,
		SysNhanVienREF SysNhanVienREF_Dest, TenDangNhap TenDangNhap_Dest, TenNhanVien TenNhanVien_Dest,
		SUM(ISNULL(tcdt.SoLuongThucChayNoiBo,0)) SLTCNB_Dest,
		SUM(ISNULL(tcdt.SoLuongThucChayKhuyenMai,0)) SLTCKM_Dest,
		SUM(ISNULL (tcdt.SoLuongThucChay,0)) SLTC_Dest,
		SUM(ISNULL(tcdt.ThanhTienThucChayNoiBo,0)) TTTCNB_Dest,
		SUM(ISNULL(tcdt.ThanhTienThucChayKhuyenMai,0))TTTCKM_Dest,
		SUM(ISNULL(tcdt.ThanhTienThucChay,0)) TTTC_Dest,
		SUM(ISNULL (tcdt.GiaTriThayDoiNoiBo,0)) GTTDNB_Dest,
		SUM(ISNULL(tcdt.GiaTriThayDoiThucChay,0))GTTDTC_Dest
		FROM [10.3.14.4].ABM_Test.dbo.ThucChayDaTinhBySanPhamThoiGianTemp tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
		HopDongID,DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,
		tcdt.DmMaHopDongREF,
		tcdt.TenMaHopDong,DmPhongBanREF,TenPhongBan,
		DmBoPhanREF,TenBoPhan,
		DmNhomLamViecREF, TenNhomLamViec,
		SysNhanVienREF, TenDangNhap, TenNhanVien
		)A
		FULL OUTER JOIN
		(
		SELECT 
		tcdt.DmSanPhamREF, 
		tcdt.TenSanPham,
		tcdt.SoHopDong,
		tcdt.HopDongID,
        tcdt.DonViTinh, 
		tcdt.DmHinhThucQuangCao,
		tcdt.TenHinhThucQuangCao,
		tcdt.NgayThucHien,	
		tcdt.DmMaHopDongREF,
		tcdt.TenMaHopDong,
		DmPhongBanREF,TenPhongBan,
		DmBoPhanREF,TenBoPhan,
		DmNhomLamViecREF, TenNhomLamViec,
		SysNhanVienREF, TenDangNhap, TenNhanVien,
		SUM(ISNULL(tcdt.SoLuongThucChayNoiBo,0)) SLTCNB,
		SUM(ISNULL(tcdt.SoLuongThucChayKhuyenMai,0)) SLTCKM,
		SUM(ISNULL (tcdt.SoLuongThucChay,0)) SLTC,
		SUM(ISNULL(tcdt.ThanhTienThucChayNoiBo,0)) TTTCNB,
		SUM(ISNULL(tcdt.ThanhTienThucChayKhuyenMai,0))TTTCKM,
		SUM(ISNULL(tcdt.ThanhTienThucChay,0)) TTTC,
		SUM(ISNULL (tcdt.GiaTriThayDoiNoiBo,0)) GTTDNB,
		SUM(ISNULL(tcdt.GiaTriThayDoiThucChay,0))GTTDTC
		FROM dbo.ThucChayDaTinhBySanPhamThoiGian tcdt
		WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
		HopDongID,DonViTinh, DmHinhThucQuangCao, TenHinhThucQuangCao,
		tcdt.DmMaHopDongREF,
		tcdt.TenMaHopDong,DmPhongBanREF,TenPhongBan,
		DmBoPhanREF,TenBoPhan,
		DmNhomLamViecREF, TenNhomLamViec,
		SysNhanVienREF, TenDangNhap, TenNhanVien
		)B
		ON (
		A.DmSanPhamREF_Dest = B.DmSanPhamREF
		AND A.TenSanPham_Dest = B.TenSanPham
		AND A.SoHopDong_Dest = B.SoHopDong
		AND A.NgayThucHien_Dest = B.NgayThucHien
		AND A.HopDongID_Dest = B.HopDongID
		AND A.DonViTinh_Dest = B.DonViTinh
		AND A.DmHinhThucQuangCao_Dest = B.DmHinhThucQuangCao
		AND A.TenHinhThucQuangCao_Dest = B.TenHinhThucQuangCao
		AND A.DmMaHopDongREF_Dest = B.DmMaHopDongREF
		AND A.TenMaHopDong_Dest = B.TenMaHopDong
		AND A.DmPhongBanREF_Dest = B.DmPhongBanREF
		AND A.TenPhongBan_Dest = B.TenPhongBan
		AND A.DmBoPhanREF_Dest = B.DmBoPhanREF AND A.TenBoPhan_Dest = B.TenBoPhan
		AND A.DmNhomLamViecREF_Dest = B.DmNhomLamViecREF AND A.TenNhomLamViec_Dest = B.TenNhomLamViec
		AND A.SysNhanVienREF_Dest = B.SysNhanVienREF 
		AND A.TenDangNhap_Dest = B.TenDangNhap AND A.TenNhanVien_Dest = B.TenNhanVien
		)
		WHERE(
		ROUND(A.SLTCNB_Dest - B.SLTCNB,0) <> 0 OR
		ROUND(A.SLTCKM_Dest - B.SLTCKM,0) <> 0 OR
		ROUND(A.SLTC_Dest - B.SLTC,0) <> 0 OR
		ROUND(A.TTTCNB_Dest - B.TTTCNB,0) <> 0 OR
		ROUND(A.TTTCKM_Dest - B.TTTCKM,0) <> 0 OR
		ROUND(A.TTTC_Dest - B.TTTC,0) <> 0 OR
		ROUND(A.GTTDNB_Dest - B.GTTDNB,0) <> 0 OR
		ROUND(A.GTTDTC_Dest - B.GTTDTC,0) <> 0
		) OR (
		A.DmSanPhamREF_Dest IS NULL OR B.DmSanPhamREF IS NULL OR 
		A.TenSanPham_Dest IS NULL OR B.TenSanPham IS NULL OR
		A.SoHopDong_Dest IS NULL OR B.SoHopDong IS NULL OR
		A.DonViTinh_Dest IS NULL OR B.DonViTinh IS NULL OR
		A.DmHinhThucQuangCao_Dest IS NULL OR B.DmHinhThucQuangCao IS NULL OR
		A.TenHinhThucQuangCao_Dest IS NULL OR B.TenHinhThucQuangCao IS NULL
		)
		)TCDT)    
		
		IF @count6 = 0 
			PRINT 'Successful ThucChayDaTinhBySanPhamThoiGian 5.38 - ThucChayDaTinhBySanPhamThoiGianTemp 5.210'
		ELSE
			PRINT  'Failed ThucChayDaTinhBySanPhamThoiGian 5.38 - ThucChayDaTinhBySanPhamThoiGianTemp 5.210'       
    END
    --ABM_Data_Partner.ThucChayAdmarketPublisher
    BEGIN
    	
    
    -- Insert statements for procedure here
    SELECT A.*, B.*
    FROM (
	SELECT tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmWebsiteREF,tcdt.NgayThucHien,
	sum(tcdt.ttClick) tc, sum(tcdt.ttView) tv
	FROM [10.3.14.4].ABM_Data_Partner.dbo.ThucChayAdmarketPublisher tcdt
	WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
	GROUP BY tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmWebsiteREF,tcdt.NgayThucHien	
	)A
	FULL OUTER JOIN
	(		
	SELECT tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmWebsiteREF,tcdt.NgayThucHien,
	sum(tcdt.ttClick) tc, sum(tcdt.ttView) tv
	FROM dbo.ThucChayAdmarketPublisher tcdt 	
	WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
	GROUP BY tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmWebsiteREF,tcdt.NgayThucHien
	)B
	ON ( 
	A.DmHinhThucQuangCao = B.DmHinhThucQuangCao
	AND A.DmWebsiteREF = B.DmWebsiteREF
	AND A.DmSanPhamREF = B.DmSanPhamREF
	AND A.TenSanPham = B.TenSanPham
	AND A.NgayThucHIen = B.NgayThucHien
	)
    WHERE(
    ROUND(A.tc - B.tc,0) <> 0 OR
    ROUND(A.tv - B.tv,0) <> 0) 
    OR (A.DmSanPhamREF IS NULL OR B.DmSanPhamREF IS NULL 
    OR A.DmWebsiteREF IS NULL OR B.DmWebsiteREF IS NULL
    OR A.DmHinhThucQuangCao IS NULL  OR B.DmHinhThucQuangCao IS NULL
    )
    END
END

```
