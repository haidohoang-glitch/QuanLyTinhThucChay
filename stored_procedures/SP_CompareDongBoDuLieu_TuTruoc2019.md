# Stored Procedure: `CompareDongBoDuLieu_TuTruoc2019`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-10-01 11:24:20.233000
- **Ngày sửa cuối**: 2020-10-01 11:24:20.233000

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
--EXEC CompareDongBoDuLieu '2014-01-01','2015-04-12'
create PROCEDURE [dbo].[CompareDongBoDuLieu_TuTruoc2019]
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	--------------------------------------------------------ThucChayDaTinh--------------------------------------------------------
    -- Insert statements for procedure here
    SELECT A.*, B.*,
    (A.SoLuongThucChay - B.SoLuongThucChay) LechSLTC,
    (A.SoLuongKM - B.SoLuongKM) LechSLKM, 
    (A.ThanhTienSauTrietKhauThucChay - B.ThanhTienSauTrietKhauThucChay) LechTTSCK,
    (A.GiaTriThayDoi - B.GiaTriThayDoi) LechGTTD,
    (A.ThanhTienThucChayKM - B.ThanhTienThucChayKM) LechTTTCKM,
	(A.ThanhTienLechTreoHa - B.ThanhTienLechTreoHa) LechTTLechTreoHa
    FROM (
	SELECT tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,HopDongID,HopDongChiTietREF ,
	DonViTinh, DmHinhThucQuangCao,
	NgayThucHien,
	SUM(ISNULL (tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0)) SoLuongThucChay,
	SUM(ISNULL (tcdt.SoLuongThucChayKM,0) + ISNULL(tcdt.SoLuongKMThayDoi,0)) SoLuongKM,
	SUM(ISNULL (tcdt.ThanhTienSauTrietKhauThucChay,0))ThanhTienSauTrietKhauThucChay,
	SUM(ISNULL (tcdt.GiaTriThayDoi,0)) GiaTriThayDoi,
	SUM(ISNULL (tcdt.ThanhTienKM,0) + ISNULL(tcdt.GiaTriKMThayDoi,0)) ThanhTienThucChayKM,
	SUM(ISNULL (tcdt.ThanhTienLechTreoHa,0)) ThanhTienLechTreoHa
	FROM [10.5.1.122].ABM_Data_Release_Backup.dbo.ThucChayDaTinh tcdt
	WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
	GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,HopDongID,HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao
	)A
	FULL OUTER JOIN
	(
	SELECT tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,HopDongID,HopDongChiTietREF,
	DonViTinh, DmHinhThucQuangCao,

	NgayThucHien,
	SUM(ISNULL (tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0)) SoLuongThucChay,
	SUM(ISNULL (tcdt.SoLuongThucChayKM,0) + ISNULL(tcdt.SoLuongKMThayDoi,0)) SoLuongKM,
	SUM(ISNULL (tcdt.ThanhTienSauTrietKhauThucChay,0))ThanhTienSauTrietKhauThucChay,
	SUM(ISNULL (tcdt.GiaTriThayDoi,0)) GiaTriThayDoi,
	SUM(ISNULL (tcdt.ThanhTienKM,0) + ISNULL(tcdt.GiaTriKMThayDoi,0)) ThanhTienThucChayKM,
	SUM(ISNULL (tcdt.ThanhTienLechTreoHa,0)) ThanhTienLechTreoHa
	FROM ThucChayDaTinh tcdt
	WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
	--and DmChienDichREF not in (1,2) -- không lấy ggfb
	GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,HopDongID,HopDongChiTietREF,	DonViTinh, DmHinhThucQuangCao
	)B
	ON (
	A.DmSanPhamREF = B.DmSanPhamREF
	AND A.TenSanPham = B.TenSanPham
	AND A.SoHopDong = B.SoHopDong
	AND A.NgayThucHIen = B.NgayThucHien
	AND A.HopDongID = B.HopDongID
	AND A.HopDongChiTietREF = B.HopDongChiTietREF
	AND ISNULL(A.DonViTinh,'') = ISNULL(B.DonViTinh,'')
	AND A.DmHinhThucQuangCao = B.DmHinhThucQuangCao
	)
    WHERE(
		ROUND(A.SoLuongThucChay - B.SoLuongThucChay,0) <> 0 OR
		ROUND(A.SoLuongKM - B.SoLuongKM,0) <> 0 OR
		ROUND(A.ThanhTienSauTrietKhauThucChay - B.ThanhTienSauTrietKhauThucChay,0) <> 0 OR
		ROUND(A.GiaTriThayDoi,0) - ROUND(B.GiaTriThayDoi,0) <> 0 OR
		ROUND(A.ThanhTienThucChayKM - B.ThanhTienThucChayKM,0) <> 0		
    OR 
		A.DmSanPhamREF IS NULL OR B.DmSanPhamREF IS NULL OR A.SoHopDong IS NULL OR B.SoHopDong IS NULL 
		--OR A.DonViTinh IS NULL OR B.DonViTinh IS NULL OR A.DmHinhThucQuangCao IS NULL OR B.DmHinhThucQuangCao)
    )
    --------------------------------------------------------ThucChayDaTinhAdmarket--------------------------------------------------------
    -- Insert statements for procedure here
    SELECT A.*, B.*,
    (A.SoLuongThucChay - B.SoLuongThucChay) LechSLTC,
    (A.SoLuongKM - B.SoLuongKM) LechSLKM, 
    (A.ThanhTienSauTrietKhauThucChay - B.ThanhTienSauTrietKhauThucChay) LechTTSCK,
    (A.GiaTriThayDoi - B.GiaTriThayDoi) LechGTTD,
    (A.ThanhTienThucChayKM - B.ThanhTienThucChayKM) LechTTTCKM
    FROM (
	SELECT tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
	SUM(ISNULL (tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0)) SoLuongThucChay,
	SUM(ISNULL (tcdt.SoLuongThucChayKM,0) + ISNULL(tcdt.SoLuongKMThayDoi,0)) SoLuongKM,
	SUM(ISNULL (tcdt.ThanhTienSauTrietKhauThucChay,0))ThanhTienSauTrietKhauThucChay,
	SUM(ISNULL (tcdt.GiaTriThayDoi,0)) GiaTriThayDoi,
	SUM(ISNULL (tcdt.ThanhTienKM,0) + ISNULL(tcdt.GiaTriKMThayDoi,0)) ThanhTienThucChayKM
	
	FROM [10.5.1.122].ABM_Data_Release_Backup.dbo.ThucChayDaTinhAdmarket tcdt
	WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
	GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien
	)A
	FULL OUTER JOIN
	(
	SELECT tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien,
	SUM(ISNULL (tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0)) SoLuongThucChay,
	SUM(ISNULL (tcdt.SoLuongThucChayKM,0) + ISNULL(tcdt.SoLuongKMThayDoi,0)) SoLuongKM,
	SUM(ISNULL (tcdt.ThanhTienSauTrietKhauThucChay,0))ThanhTienSauTrietKhauThucChay,
	SUM(ISNULL (tcdt.GiaTriThayDoi,0)) GiaTriThayDoi,
	SUM(ISNULL (tcdt.ThanhTienKM,0) + ISNULL(tcdt.GiaTriKMThayDoi,0)) ThanhTienThucChayKM
	FROM ThucChayDaTinhAdmarket tcdt
	WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
	GROUP BY tcdt.DmSanPhamREF, tcdt.TenSanPham,SoHopDong,NgayThucHien
	)B
	ON ( 
	A.DmSanPhamREF = B.DmSanPhamREF
	AND A.TenSanPham = B.TenSanPham
	AND A.SoHopDong = B.SoHopDong
	AND A.NgayThucHIen = B.NgayThucHien
	)
    WHERE(
    ROUND(A.SoLuongThucChay - B.SoLuongThucChay,0) <> 0 OR
    ROUND(A.SoLuongKM - B.SoLuongKM,0) <> 0 OR
    ROUND(A.ThanhTienSauTrietKhauThucChay - B.ThanhTienSauTrietKhauThucChay,0) <> 0 OR
    ROUND(A.GiaTriThayDoi - B.GiaTriThayDoi,0) <> 0 OR
    ROUND(A.ThanhTienThucChayKM - B.ThanhTienThucChayKM,0) <> 0
    )
     OR (A.DmSanPhamREF IS NULL OR B.DmSanPhamREF IS NULL OR A.SoHopDong IS NULL OR B.SoHopDong IS NULL --
		   
    )
  

		--------------------------------------------------------ThucChayDaTinh_MuaNgoai--------------------------------------------------------
    -- Insert statements for procedure here
    SELECT A.*, B.*,
    (A.SoLuongThucChay - B.SoLuongThucChay) LechSLTC,
    (A.SoLuongKM - B.SoLuongKM) LechSLKM, 
    (A.ThanhTienLaiThucChaySauCK - B.ThanhTienLaiThucChaySauCK) LechLaiSCK,
    (A.GiaTriThayDoiLai - B.GiaTriThayDoiLai) LechLaiGTTD,
    (A.ThanhTienLaiThucChayKM - B.ThanhTienLaiThucChayKM) LechLaiTCKM
    FROM (
	SELECT HopDongREF,SoHopDong,DmNhanVienREF,TenDangNhap,DmKhachHangREF, HopDongChiTietREF ,LstDmNhanHangREF,DmHinhThucQuangCaoREF,tcdt.DmSanPhamREF,
	DmLoaiBannerREF,ThucChayMuaNgoaiChiTietREF ,DmWebsiteREF,
	NgayThucHien,
	SUM(ISNULL (tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0)) SoLuongThucChay,
	SUM(ISNULL (tcdt.SoLuongThucChayKM,0) + ISNULL(tcdt.SoLuongKMThayDoi,0)) SoLuongKM,
	SUM(ISNULL (tcdt.ThanhTienLaiThucChaySauCK,0))ThanhTienLaiThucChaySauCK,
	SUM(ISNULL (tcdt.GiaTriThayDoiLaiSauCK,0)) GiaTriThayDoiLai,
	SUM(ISNULL (tcdt.ThanhTienLaiThucChayKM,0) + ISNULL(tcdt.GiaTriKMLaiThayDoi,0)) ThanhTienLaiThucChayKM
	FROM [10.5.1.122].ABM_Data_Release_Backup.dbo.ThucChayDaTinh_MuaNgoai tcdt
	WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
	GROUP BY  HopDongREF,SoHopDong,DmNhanVienREF,TenDangNhap,DmKhachHangREF, HopDongChiTietREF ,LstDmNhanHangREF,DmHinhThucQuangCaoREF,tcdt.DmSanPhamREF,
	DmLoaiBannerREF,ThucChayMuaNgoaiChiTietREF ,DmWebsiteREF,
	NgayThucHien
	)A
	FULL OUTER JOIN
	(
	SELECT HopDongREF,SoHopDong,DmNhanVienREF,TenDangNhap,DmKhachHangREF, HopDongChiTietREF ,LstDmNhanHangREF,DmHinhThucQuangCaoREF,tcdt.DmSanPhamREF,
	DmLoaiBannerREF,ThucChayMuaNgoaiChiTietREF ,DmWebsiteREF,
	NgayThucHien,
	SUM(ISNULL (tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0)) SoLuongThucChay,
	SUM(ISNULL (tcdt.SoLuongThucChayKM,0) + ISNULL(tcdt.SoLuongKMThayDoi,0)) SoLuongKM,
	SUM(ISNULL (tcdt.ThanhTienLaiThucChaySauCK,0))ThanhTienLaiThucChaySauCK,
	SUM(ISNULL (tcdt.GiaTriThayDoiLaiSauCK,0)) GiaTriThayDoiLai,
	SUM(ISNULL (tcdt.ThanhTienLaiThucChayKM,0) + ISNULL(tcdt.GiaTriKMLaiThayDoi,0)) ThanhTienLaiThucChayKM
	FROM dbo.ThucChayDaTinh_MuaNgoai tcdt
	WHERE tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
	--and DmChienDichREF not in (1,2) -- khong lay ggfb
	GROUP BY  HopDongREF,SoHopDong,DmNhanVienREF,TenDangNhap,DmKhachHangREF, HopDongChiTietREF ,LstDmNhanHangREF,DmHinhThucQuangCaoREF,tcdt.DmSanPhamREF,
	DmLoaiBannerREF,ThucChayMuaNgoaiChiTietREF ,DmWebsiteREF,
	NgayThucHien
	)B
	ON (
	A.HopDongREF = B.HopDongREF	
	AND A.SoHopDong = B.SoHopDong
	AND A.DmNhanVienREF = B.DmNhanVienREF
	AND A.TenDangNhap = B.TenDangNhap
	AND A.DmKhachHangREF = B.DmKhachHangREF
	AND A.HopDongChiTietREF = B.HopDongChiTietREF
	AND A.LstDmNhanHangREF = B.LstDmNhanHangREF	
	AND A.DmHinhThucQuangCaoREF = B.DmHinhThucQuangCaoREF
	AND A.DmLoaiBannerREF = B.DmLoaiBannerREF
	AND A.ThucChayMuaNgoaiChiTietREF = B.ThucChayMuaNgoaiChiTietREF
	AND A.DmWebsiteREF = B.DmWebsiteREF
	AND A.NgayThucHien = B.NgayThucHien
	)
    WHERE(
		ROUND(A.SoLuongThucChay - B.SoLuongThucChay,0) <> 0 OR
		ROUND(A.SoLuongKM - B.SoLuongKM,0) <> 0 OR
		ROUND(A.ThanhTienLaiThucChaySauCK - B.ThanhTienLaiThucChaySauCK,0) <> 0 OR
		ROUND(A.GiaTriThayDoiLai,0) - ROUND(B.GiaTriThayDoiLai,0) <> 0 OR
		ROUND(A.ThanhTienLaiThucChayKM - B.ThanhTienLaiThucChayKM,0) <> 0		
    OR A.DmSanPhamREF IS NULL OR B.DmSanPhamREF IS NULL 
	OR A.SoHopDong IS NULL OR B.SoHopDong IS NULL 
	OR A.ThucChayMuaNgoaiChiTietREF IS NULL OR B.ThucChayMuaNgoaiChiTietREF IS NULL 
		--OR A.DonViTinh IS NULL OR B.DonViTinh IS NULL OR A.DmHinhThucQuangCao IS NULL OR B.DmHinhThucQuangCao)
    )

	
END
--WebsiteMapping_HDCN_Reporting


```
