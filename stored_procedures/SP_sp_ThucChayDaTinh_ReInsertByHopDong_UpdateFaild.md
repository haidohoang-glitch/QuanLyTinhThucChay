# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong_UpdateFaild`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-05-16 10:48:24.037000
- **Ngày sửa cuối**: 2016-06-24 11:16:55.470000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_UpdateFaild] '2016-06-21','QC1010416',93828
CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_UpdateFaild]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietREF INT
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    declare 
	@HopDongID INT,
	@HopDongChiTietID INT,
	@SoHopDong_new NVARCHAR(50),
	@NgayDanhSo_new DATETIME,
	@DmNhanVienREF_new INT,
	@DmKhachHangREF_new NVARCHAR(200),
	@DmSanPhamREF_new INT,
	@DsNhanHangREF_new NVARCHAR(200),
	@HinhThucQuangCaoREF_new INT, @TenDangNhap_new NVARCHAR(50),
	@MaSoHopDong_new INT , @Note NVARCHAR(50), @IsThayDoi INT,@GiaTriThucChay FLOAT,@GiaTriThucChayAd FLOAT, @IsExistData INT ,@IsExistData1 INT  ;
	
    DECLARE db_cursor CURSOR FOR  
	SELECT DISTINCT
		hd.HopDongID,
		hdct.HopDongChiTietID,
		hd.SoHopDong,
		hd.NgayDanhSoHopDong,
		hd.SysNhanVienREF, 
		hd.TenKhachHang,
		hdct.DmSanPhamREF,
		hdct.NhanHang,
		hdct.DmLoaiREF,
		hd.DmMaHopDongREF,
		hd.TenDangNhap
	FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	AND SoHopDong = 'QC1010416'
	AND HopDongChiTietID = 93828
	--WHERE CONVERT(DATE,hd.LastModifiedAt) = CONVERT(DATE,@NgayThucHien)

	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @HopDongID,
	@HopDongChiTietID ,
	@SoHopDong_new ,
	@NgayDanhSo_new ,
	@DmNhanVienREF_new ,
	@DmKhachHangREF_new ,
	@DmSanPhamREF_new ,
	@DsNhanHangREF_new ,
	@HinhThucQuangCaoREF_new ,
	@MaSoHopDong_new ,
	@TenDangNhap_new

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		SET @IsThayDoi = [dbo].[fn_ThucChay_CheckHopDongThayDoi](   @NgayThucHien,
																	@HopDongID,
																	@HopDongChiTietID ,
																	@SoHopDong_new ,
																	@NgayDanhSo_new ,
																	@DmNhanVienREF_new ,
																	@DmKhachHangREF_new ,
																	@DmSanPhamREF_new ,
																	@DsNhanHangREF_new ,
																	@HinhThucQuangCaoREF_new ,
																	@MaSoHopDong_new,
																	@TenDangNhap_new )
		
		SELECT @GiaTriThucChay = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien
		SELECT @GiaTriThucChay
		SELECT @GiaTriThucChayAd = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien
		SET @GiaTriThucChay = isnull(ROUND(@GiaTriThucChay,0),0)
		SELECT @IsExistData = COUNT(HopDongID) FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien <@NgayThucHien
		SELECT @IsExistData1 = COUNT(HopDongID) FROM ThucChayDaTinhAdmarket tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien <@NgayThucHien
		SELECT @IsExistData, @IsExistData1

		IF(@IsThayDoi <> 0 AND (isnull(@GiaTriThucChay,0) <>0 OR isnull(@GiaTriThucChayAd,0) <> 0) AND (@IsExistData > 0 OR @IsExistData1 > 0))
		BEGIN
			if @IsThayDoi = 1 SET @Note = 'THAY DOI THONG TIN HOP DONG'
			if @IsThayDoi = 2 SET @Note = 'PHAN BO BI XOA'
			if @IsThayDoi = 3 SET @Note = 'THAY DOI DANH SACH NHAN HANG'
			if @IsThayDoi = 4 SET @Note = 'HUY HOP DONG'

		SELECT @Note
		-- cap nhat lai du lieu da tinh
		-- 1. Thuc chay da tinh
		--INSERT INTO ThucChayDaTinh_ThayDoi
			  SELECT newid() AS ID
			  ,[HopDongID]
			  ,[SoHopDong]
			  ,[DmMaHopDongREF]
			  ,[TenMaHopDong]
			  ,[NgayDanhSoHopDong]
			  ,[NgayKyHopDong]
			  ,[NhanHopDong]
			  ,[NgayNhanBanFax]
			  ,[NgayNhanHopDongBanCung]
			  ,[NgayChuyenHopDongChoKeToan]
			  ,[So]
			  ,[Thang]
			  ,[Nam]
			  ,[GiaTriHopDong]
			  ,[CongNo]
			  ,[HopDongChiTietREF]
			  ,[DangSuDung]
			  ,[IsGiayPhep]
			  ,[TrangThaiHopDong]
			  ,[IsBanCung]
			  ,[DmPhongBanREF]
			  ,[TenPhongBan]
			  ,[DmBoPhanREF]
			  ,[TenBoPhan]
			  ,[DmNhomLamViecREF]
			  ,[TenNhomLamViec]
			  ,[DmDiaDiemLamViecREF]
			  ,[TenDiaDiemLamViec]
			  ,[SysNhanVienREF]
			  ,[TenDangNhap]
			  ,[TenNhanVien]
			  ,[TenKhachHang]
			  ,[NhanHang]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,[DmHinhThucQuangCao]
			  ,[TenHinhThucQuangCao]
			  ,[DmSanPhamREF]
			  ,[TenSanPham]
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,[DotChayHopDong]
			  ,[SoLuongDotChayHD]
			  ,[DotChayBooking]
			  ,[SoLuongDotChayBooking]
			  ,[SoLuong]
			  ,[DonViTinh]
			  ,[DonGia]
			  ,[DonGiaTheoDonVi]
			  ,[ChietKhau]
			  ,[GiamGia]
			  ,[ThanhTien]
			  ,[TiLeTuVan]
			  ,[ChiPhiTuVan]
			  ,[IsKhuyenMai]
			  ,[KhuyenMai]
			  ,[DmBannerREF]
			  ,[DmChienDichREF]
			  ,[DmWebsiteREF]
			  ,[TenWebsite]
			  ,0[TongViewThucChay]
			  ,0[TongClickThucChay]
			  ,0[TongSoBaiViet]
			  ,0[SoLuongThucChay]
			  ,@NgayThucHien
			  ,-sum([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) [GiaTriThayDoi]
			  ,0[ThanhTienThucChayTruocTrietKhau]
			  ,0[GiaTriTrietKhauThucChay]
			  ,0[ThanhTienSauTrietKhauThucChay]
			  ,0[GiaTriHoaHongThucChay]
			  ,0[ThanhTienThucThu]
			  ,0[ThanhTienKM]
			  ,0[SoLuongThucChayKM]
			  ,0[SoLuongThucChayLechTreoHa]
			  ,0[ThanhTienLechTreoHa]
			  ,getdate()[CreatedAt]
			  ,getdate()[LastModifiedAt]
			  ,0 [IsPheDuyet]
			  ,''[PheDuyetBy]
			  ,''[PheDuyetAt]
			  ,-sum([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
			  ,-sum([SoLuongThucChayKM]+[SoLuongKMThayDoi])[SoLuongKMThayDoi]
			  ,-sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
			  ,@Note
			  FROM [ThucChayDaTinh]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			  AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG'),'2009-01-01')
			  AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			  AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			  AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			  AND NgayThucHien < @NgayThucHien
			  GROUP BY [HopDongID]
			  ,[SoHopDong]
			  ,[DmMaHopDongREF]
			  ,[TenMaHopDong]
			  ,[NgayDanhSoHopDong]
			  ,[NgayKyHopDong]
			  ,[NhanHopDong]
			  ,[NgayNhanBanFax]
			  ,[NgayNhanHopDongBanCung]
			  ,[NgayChuyenHopDongChoKeToan]
			  ,[So]
			  ,[Thang]
			  ,[Nam]
			  ,[GiaTriHopDong]
			  ,[CongNo]
			  ,[HopDongChiTietREF]
			  ,[DangSuDung]
			  ,[IsGiayPhep]
			  ,[TrangThaiHopDong]
			  ,[IsBanCung]
			  ,[DmPhongBanREF]
			  ,[TenPhongBan]
			  ,[DmBoPhanREF]
			  ,[TenBoPhan]
			  ,[DmNhomLamViecREF]
			  ,[TenNhomLamViec]
			  ,[DmDiaDiemLamViecREF]
			  ,[TenDiaDiemLamViec]
			  ,[SysNhanVienREF]
			  ,[TenDangNhap]
			  ,[TenNhanVien]
			  ,[TenKhachHang]
			  ,[NhanHang]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,[DmHinhThucQuangCao]
			  ,[TenHinhThucQuangCao]
			  ,[DmSanPhamREF]
			  ,[TenSanPham]
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,[DotChayHopDong]
			  ,[SoLuongDotChayHD]
			  ,[DotChayBooking]
			  ,[SoLuongDotChayBooking]
			  ,[SoLuong]
			  ,[DonViTinh]
			  ,[DonGia]
			  ,[DonGiaTheoDonVi]
			  ,[ChietKhau]
			  ,[GiamGia]
			  ,[ThanhTien]
			  ,[TiLeTuVan]
			  ,[ChiPhiTuVan]
			  ,[IsKhuyenMai]
			  ,[KhuyenMai]
			  ,[DmBannerREF]
			  ,[DmChienDichREF]
			  ,[DmWebsiteREF]
			  ,[TenWebsite]
		if @IsThayDoi IN (1,3)	  
	    --INSERT INTO ThucChayDaTinh_ThayDoi
			  SELECT newid() AS ID
			  ,[HopDongID]
			  ,[SoHopDong]
			  ,@MaSoHopDong_new DmMaHopDongREF
			  ,ISNULL((SELECT dmhdc.TenMaHopDong
			               FROM DmMaHopDongChuan dmhdc WHERE dmhdc.DmMaHopDongID = @MaSoHopDong_new),'')TenMaHopDong
			  ,@NgayDanhSo_new
			  ,[NgayKyHopDong]
			  ,[NhanHopDong]
			  ,[NgayNhanBanFax]
			  ,[NgayNhanHopDongBanCung]
			  ,[NgayChuyenHopDongChoKeToan]
			  ,[So]
			  ,[Thang]
			  ,[Nam]
			  ,[GiaTriHopDong]
			  ,[CongNo]
			  ,[HopDongChiTietREF]
			  ,[DangSuDung]
			  ,[IsGiayPhep]
			  ,[TrangThaiHopDong]
			  ,[IsBanCung]
			  ,[DmPhongBanREF]
			  ,[TenPhongBan]
			  ,[DmBoPhanREF]
			  ,[TenBoPhan]
			  ,[DmNhomLamViecREF]
			  ,[TenNhomLamViec]
			  ,[DmDiaDiemLamViecREF]
			  ,[TenDiaDiemLamViec]
			  ,@DmNhanVienREF_new
			  ,(SELECT hd.TenDangNhap
			      FROM HopDong hd WHERE hd.HopDongID = HopDongID )
			  ,(SELECT nssyll.HoVaTen
							FROM NhanSuSoYeuLyLich nssyll WHERE nssyll.NhanSuSoYeuLyLichID = @DmNhanVienREF_new)
			  ,@DmKhachHangREF_new
			  ,(SELECT hdct.Nhanhang 
							FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = HopDongChiTietREF)
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,@HinhThucQuangCaoREF_new
			  ,(SELECT dhtqc.TenHinhThucQuangCao 
							FROM DmHinhThucQuangCao dhtqc WHERE dhtqc.DmHinhThucQuangCaoID = @HinhThucQuangCaoREF_new)
			  ,@DmSanPhamREF_new
			  ,(SELECT dsp.TenSanPham
			                FROM DmSanPham dsp WHERE dsp.DmSanPhamID = @DmSanPhamREF_new)
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,[DotChayHopDong]
			  ,[SoLuongDotChayHD]
			  ,[DotChayBooking]
			  ,[SoLuongDotChayBooking]
			  ,[SoLuong]
			  ,[DonViTinh]
			  ,[DonGia]
			  ,[DonGiaTheoDonVi]
			  ,[ChietKhau]
			  ,[GiamGia]
			  ,[ThanhTien]
			  ,[TiLeTuVan]
			  ,[ChiPhiTuVan]
			  ,[IsKhuyenMai]
			  ,[KhuyenMai]
			  ,[DmBannerREF]
			  ,[DmChienDichREF]
			  ,[DmWebsiteREF]
			  ,[TenWebsite]
			  ,0[TongViewThucChay]
			  ,0[TongClickThucChay]
			  ,0[TongSoBaiViet]
			  ,0 [SoLuongThucChay]
			  ,@NgayThucHien
			  ,SUM([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) GiaTriThayDoi
			  ,0[ThanhTienThucChayTruocTrietKhau]
			  ,0[GiaTriTrietKhauThucChay]
			  ,0 [ThanhTienSauTrietKhauThucChay]
			  ,0[GiaTriHoaHongThucChay]
			  ,0[ThanhTienThucThu]
			  ,SUM([ThanhTienKM]+[GiaTriKMThayDoi]) [ThanhTienKM]
			  ,SUM([SoLuongThucChayKM]+[SoLuongKMThayDoi]) [SoLuongThucChayKM]
			  ,0[SoLuongThucChayLechTreoHa]
			  ,0[ThanhTienLechTreoHa]
			  ,getdate()[CreatedAt]
			  ,getdate()[LastModifiedAt]
			  ,0 [IsPheDuyet]
			  ,''[PheDuyetBy]
			  ,''[PheDuyetAt]
			  ,SUM([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
			  ,0[SoLuongKMThayDoi]
			  ,0[GiaTriKMThayDoi]
			  ,'Chay lai thuc chay'
			  FROM [ThucChayDaTinh]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			   AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG'),'2009-01-01')
			   AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			   AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			   AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			   AND NgayThucHien < @NgayThucHien
			  GROUP BY
			   [HopDongID]
			  ,[SoHopDong]
			  ,[NgayKyHopDong]
			  ,[NhanHopDong]
			  ,[NgayNhanBanFax]
			  ,[NgayNhanHopDongBanCung]
			  ,[NgayChuyenHopDongChoKeToan]
			  ,[So]
			  ,[Thang]
			  ,[Nam]
			  ,[GiaTriHopDong]
			  ,[CongNo]
			  ,[HopDongChiTietREF]
			  ,[DangSuDung]
			  ,[IsGiayPhep]
			  ,[TrangThaiHopDong]
			  ,[IsBanCung]
			  ,[DmPhongBanREF]
			  ,[TenPhongBan]
			  ,[DmBoPhanREF]
			  ,[TenBoPhan]
			  ,[DmNhomLamViecREF]
			  ,[TenNhomLamViec]
			  ,[DmDiaDiemLamViecREF]
			  ,[TenDiaDiemLamViec]
			  ,[TenDangNhap]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,[DotChayHopDong]
			  ,[SoLuongDotChayHD]
			  ,[DotChayBooking]
			  ,[SoLuongDotChayBooking]
			  ,[SoLuong]
			  ,[DonViTinh]
			  ,[DonGia]
			  ,[DonGiaTheoDonVi]
			  ,[ChietKhau]
			  ,[GiamGia]
			  ,[ThanhTien]
			  ,[TiLeTuVan]
			  ,[ChiPhiTuVan]
			  ,[IsKhuyenMai]
			  ,[KhuyenMai]
			  ,[DmBannerREF]
			  ,[DmChienDichREF]
			  ,[DmWebsiteREF]
			  ,[TenWebsite]
		-- 2. Thuc chay da tinh admarket
		--INSERT INTO ThucChayDaTinhAdmarket_ThayDoi
			   SELECT newid() AS ID
			  ,[HopDongID]
			  ,[SoHopDong]
			  ,[DmMaHopDongREF]
			  ,[TenMaHopDong]
			  ,[NgayDanhSoHopDong]
			  ,[NgayKyHopDong]
			  ,[NhanHopDong]
			  ,[NgayNhanBanFax]
			  ,[NgayNhanHopDongBanCung]
			  ,[NgayChuyenHopDongChoKeToan]
			  ,[So]
			  ,[Thang]
			  ,[Nam]
			  ,[GiaTriHopDong]
			  ,[CongNo]
			  ,[HopDongChiTietREF]
			  ,[DangSuDung]
			  ,[IsGiayPhep]
			  ,[TrangThaiHopDong]
			  ,[IsBanCung]
			  ,[DmPhongBanREF]
			  ,[TenPhongBan]
			  ,[DmBoPhanREF]
			  ,[TenBoPhan]
			  ,[DmNhomLamViecREF]
			  ,[TenNhomLamViec]
			  ,[DmDiaDiemLamViecREF]
			  ,[TenDiaDiemLamViec]
			  ,[SysNhanVienREF]
			  ,[TenDangNhap]
			  ,[TenNhanVien]
			  ,[TenKhachHang]
			  ,[NhanHang]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,[DmHinhThucQuangCao]
			  ,[TenHinhThucQuangCao]
			  ,[DmSanPhamREF]
			  ,[TenSanPham]
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,[DotChayHopDong]
			  ,[SoLuongDotChayHD]
			  ,[DotChayBooking]
			  ,[SoLuongDotChayBooking]
			  ,[SoLuong]
			  ,[DonViTinh]
			  ,[DonGia]
			  ,[DonGiaTheoDonVi]
			  ,[ChietKhau]
			  ,[GiamGia]
			  ,[ThanhTien]
			  ,[TiLeTuVan]
			  ,[ChiPhiTuVan]
			  ,[IsKhuyenMai]
			  ,[KhuyenMai]
			  ,[DmBannerREF]
			  ,[DmChienDichREF]
			  ,[DmWebsiteREF]
			  ,[TenWebsite]
			  ,0[TongViewThucChay]
			  ,0[TongClickThucChay]
			  ,0[TongSoBaiViet]
			  ,0[SoLuongThucChay]
			  ,@NgayThucHien
			  ,-sum([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) [GiaTriThayDoi]
			  ,0[ThanhTienThucChayTruocTrietKhau]
			  ,0[GiaTriTrietKhauThucChay]
			  ,0[ThanhTienSauTrietKhauThucChay]
			  ,0[GiaTriHoaHongThucChay]
			  ,0[ThanhTienThucThu]
			  ,0[ThanhTienKM]
			  ,0[SoLuongThucChayKM]
			  ,0[SoLuongThucChayLechTreoHa]
			  ,0[ThanhTienLechTreoHa]
			  ,getdate()[CreatedAt]
			  ,getdate()[LastModifiedAt]
			  ,0 [IsPheDuyet]
			  ,''[PheDuyetBy]
			  ,''[PheDuyetAt]
			  ,-sum([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
			  ,-sum([SoLuongThucChayKM]+[SoLuongKMThayDoi])[SoLuongKMThayDoi]
			  ,-sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
			  ,@Note
			  FROM [ThucChayDaTinhAdmarket]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			  AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG'),'2009-01-01')
			  AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			  AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			  AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			  AND NgayThucHien < @NgayThucHien
			  GROUP BY [HopDongID]
			  ,[SoHopDong]
			  ,[DmMaHopDongREF]
			  ,[TenMaHopDong]
			  ,[NgayDanhSoHopDong]
			  ,[NgayKyHopDong]
			  ,[NhanHopDong]
			  ,[NgayNhanBanFax]
			  ,[NgayNhanHopDongBanCung]
			  ,[NgayChuyenHopDongChoKeToan]
			  ,[So]
			  ,[Thang]
			  ,[Nam]
			  ,[GiaTriHopDong]
			  ,[CongNo]
			  ,[HopDongChiTietREF]
			  ,[DangSuDung]
			  ,[IsGiayPhep]
			  ,[TrangThaiHopDong]
			  ,[IsBanCung]
			  ,[DmPhongBanREF]
			  ,[TenPhongBan]
			  ,[DmBoPhanREF]
			  ,[TenBoPhan]
			  ,[DmNhomLamViecREF]
			  ,[TenNhomLamViec]
			  ,[DmDiaDiemLamViecREF]
			  ,[TenDiaDiemLamViec]
			  ,[SysNhanVienREF]
			  ,[TenDangNhap]
			  ,[TenNhanVien]
			  ,[TenKhachHang]
			  ,[NhanHang]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,[DmHinhThucQuangCao]
			  ,[TenHinhThucQuangCao]
			  ,[DmSanPhamREF]
			  ,[TenSanPham]
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,[DotChayHopDong]
			  ,[SoLuongDotChayHD]
			  ,[DotChayBooking]
			  ,[SoLuongDotChayBooking]
			  ,[SoLuong]
			  ,[DonViTinh]
			  ,[DonGia]
			  ,[DonGiaTheoDonVi]
			  ,[ChietKhau]
			  ,[GiamGia]
			  ,[ThanhTien]
			  ,[TiLeTuVan]
			  ,[ChiPhiTuVan]
			  ,[IsKhuyenMai]
			  ,[KhuyenMai]
			  ,[DmBannerREF]
			  ,[DmChienDichREF]
			  ,[DmWebsiteREF]
			  ,[TenWebsite]
		if @IsThayDoi IN (1,3)	  
	    --INSERT INTO ThucChayDaTinhAdmarket_ThayDoi
			  SELECT newid() AS ID
			  ,[HopDongID]
			  ,[SoHopDong]
			  ,@MaSoHopDong_new
			  ,ISNULL((SELECT dmhdc.TenMaHopDong
			               FROM DmMaHopDongChuan dmhdc WHERE dmhdc.DmMaHopDongID = @MaSoHopDong_new),'')
			  ,@NgayDanhSo_new
			  ,[NgayKyHopDong]
			  ,[NhanHopDong]
			  ,[NgayNhanBanFax]
			  ,[NgayNhanHopDongBanCung]
			  ,[NgayChuyenHopDongChoKeToan]
			  ,[So]
			  ,[Thang]
			  ,[Nam]
			  ,[GiaTriHopDong]
			  ,[CongNo]
			  ,[HopDongChiTietREF]
			  ,[DangSuDung]
			  ,[IsGiayPhep]
			  ,[TrangThaiHopDong]
			  ,[IsBanCung]
			  ,[DmPhongBanREF]
			  ,[TenPhongBan]
			  ,[DmBoPhanREF]
			  ,[TenBoPhan]
			  ,[DmNhomLamViecREF]
			  ,[TenNhomLamViec]
			  ,[DmDiaDiemLamViecREF]
			  ,[TenDiaDiemLamViec]
			  ,@DmNhanVienREF_new
			  ,(SELECT hd.TenDangNhap
			      FROM HopDong hd WHERE hd.HopDongID = HopDongID )
			  ,(SELECT nssyll.HoVaTen
							FROM NhanSuSoYeuLyLich nssyll WHERE nssyll.NhanSuSoYeuLyLichID = @DmNhanVienREF_new)
			  ,@DmKhachHangREF_new
			  ,(SELECT hdct.Nhanhang 
							FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = HopDongChiTietREF)
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,@HinhThucQuangCaoREF_new
			  ,(SELECT dhtqc.TenHinhThucQuangCao 
							FROM DmHinhThucQuangCao dhtqc WHERE dhtqc.DmHinhThucQuangCaoID = @HinhThucQuangCaoREF_new)
			  ,@DmSanPhamREF_new
			  ,(SELECT dsp.TenSanPham
			                FROM DmSanPham dsp WHERE dsp.DmSanPhamID = @DmSanPhamREF_new)
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,[DotChayHopDong]
			  ,[SoLuongDotChayHD]
			  ,[DotChayBooking]
			  ,[SoLuongDotChayBooking]
			  ,[SoLuong]
			  ,[DonViTinh]
			  ,[DonGia]
			  ,[DonGiaTheoDonVi]
			  ,[ChietKhau]
			  ,[GiamGia]
			  ,[ThanhTien]
			  ,[TiLeTuVan]
			  ,[ChiPhiTuVan]
			  ,[IsKhuyenMai]
			  ,[KhuyenMai]
			  ,[DmBannerREF]
			  ,[DmChienDichREF]
			  ,[DmWebsiteREF]
			  ,[TenWebsite]
			  ,0[TongViewThucChay]
			  ,0[TongClickThucChay]
			  ,0[TongSoBaiViet]
			  ,0 [SoLuongThucChay]
			  ,@NgayThucHien
			  ,SUM([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) GiaTriThayDoi
			  ,0[ThanhTienThucChayTruocTrietKhau]
			  ,0[GiaTriTrietKhauThucChay]
			  ,0 [ThanhTienSauTrietKhauThucChay]
			  ,0[GiaTriHoaHongThucChay]
			  ,0[ThanhTienThucThu]
			  ,SUM([ThanhTienKM]+[GiaTriKMThayDoi]) [ThanhTienKM]
			  ,SUM([SoLuongThucChayKM]+[SoLuongKMThayDoi]) [SoLuongThucChayKM]
			  ,0[SoLuongThucChayLechTreoHa]
			  ,0[ThanhTienLechTreoHa]
			  ,getdate()[CreatedAt]
			  ,getdate()[LastModifiedAt]
			  ,0 [IsPheDuyet]
			  ,''[PheDuyetBy]
			  ,''[PheDuyetAt]
			  ,SUM([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
			  ,0[SoLuongKMThayDoi]
			  ,0[GiaTriKMThayDoi]
			  ,'Chay lai thuc chay'
			  FROM [ThucChayDaTinhAdmarket]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			   AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG'),'2009-01-01')
			   AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			   AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			   AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			   AND NgayThucHien < @NgayThucHien
			  GROUP BY
			   [HopDongID]
			  ,[SoHopDong]
			  ,[NgayKyHopDong]
			  ,[NhanHopDong]
			  ,[NgayNhanBanFax]
			  ,[NgayNhanHopDongBanCung]
			  ,[NgayChuyenHopDongChoKeToan]
			  ,[So]
			  ,[Thang]
			  ,[Nam]
			  ,[GiaTriHopDong]
			  ,[CongNo]
			  ,[HopDongChiTietREF]
			  ,[DangSuDung]
			  ,[IsGiayPhep]
			  ,[TrangThaiHopDong]
			  ,[IsBanCung]
			  ,[DmPhongBanREF]
			  ,[TenPhongBan]
			  ,[DmBoPhanREF]
			  ,[TenBoPhan]
			  ,[DmNhomLamViecREF]
			  ,[TenNhomLamViec]
			  ,[DmDiaDiemLamViecREF]
			  ,[TenDiaDiemLamViec]
			  ,[TenDangNhap]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,[DotChayHopDong]
			  ,[SoLuongDotChayHD]
			  ,[DotChayBooking]
			  ,[SoLuongDotChayBooking]
			  ,[SoLuong]
			  ,[DonViTinh]
			  ,[DonGia]
			  ,[DonGiaTheoDonVi]
			  ,[ChietKhau]
			  ,[GiamGia]
			  ,[ThanhTien]
			  ,[TiLeTuVan]
			  ,[ChiPhiTuVan]
			  ,[IsKhuyenMai]
			  ,[KhuyenMai]
			  ,[DmBannerREF]
			  ,[DmChienDichREF]
			  ,[DmWebsiteREF]
			  ,[TenWebsite]
		END

	FETCH NEXT FROM db_cursor INTO @HopDongID,
	@HopDongChiTietID ,
	@SoHopDong_new ,
	@NgayDanhSo_new ,
	@DmNhanVienREF_new ,
	@DmKhachHangREF_new ,
	@DmSanPhamREF_new ,
	@DsNhanHangREF_new ,
	@HinhThucQuangCaoREF_new ,
	@MaSoHopDong_new  ,
	@TenDangNhap_new  
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor
	
	--- Update nhan hang bởi thực chạy hd chi tiết
	DECLARE @NhanHangMoi NVARCHAR(500),@HDID INT, @PhanBoID INT 
	DECLARE cursor_hdct CURSOR FOR  
	
	SELECT HopDongREF,HopDongChiTietREF, DmNhanHangREF
	FROM ThucChayHopDongChiTiet 
	WHERE CONVERT(DATE,LastModifiedAt) = CONVERT(DATE,@NgayThucHien)
	OPEN cursor_hdct   
	FETCH NEXT FROM cursor_hdct INTO @HDID,@PhanBoID,@NhanHangMoi   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		   -----
		   UPDATE ThucChayDaTinh
		   SET
		   NhanHang = @NhanHangMoi
		   WHERE hopdongid = @HDID
		   AND HopDongChiTietREF = @PhanBoID
		   FETCH NEXT FROM cursor_hdct INTO @HDID,@PhanBoID,@NhanHangMoi    
	END   

	CLOSE cursor_hdct   
	DEALLOCATE cursor_hdct
	
END



```
