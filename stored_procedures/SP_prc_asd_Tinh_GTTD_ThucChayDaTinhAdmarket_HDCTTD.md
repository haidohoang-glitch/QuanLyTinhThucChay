# Stored Procedure: `prc_asd_Tinh_GTTD_ThucChayDaTinhAdmarket_HDCTTD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-14 10:30:49.897000
- **Ngày sửa cuối**: 2021-06-14 14:36:06.383000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThucChay_PerformanceBase_ThayDoi_ID` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@TongThanhTienThucChayDaTinh` | `float(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@ThucChayDaTinhID_output` | `nvarchar(100)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*

*/
CREATE PROCEDURE [dbo].[prc_asd_Tinh_GTTD_ThucChayDaTinhAdmarket_HDCTTD]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@ThucChay_PerformanceBase_ThayDoi_ID INT,
	@HopDongID INT,
	@HopDongChiTietID INT, 
	@DmSanPhamREF INT, 
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(200),
	@TongThanhTienThucChayDaTinh FLOAT,
	@GiaTriThayDoi FLOAT, 
	@GhiChu nvarchar(200),
	@ThucChayDaTinhID_output NVARCHAR(50) OUTPUT
AS
BEGIN
	 DECLARE @SoLuongThayDoi INT = 0, @DonViTinh NVARCHAR(100), @SoLuongThucChay INT = 0, @TenSanPham NVARCHAR(200)=''
	  , @DanhSachNhanHangREF NVARCHAR(200) = ''
	  , @GhiChuOnline NVARCHAR(500) = N''
	  , @GhiChu_TienThayDoi NVARCHAR(500) = N''
	  , @TenMaHopDong NVARCHAR(100) = ''
	  , @DmMaHopDong int = 0
	SET @DonViTinh = 'CPC'
	SET @TenSanPham =''
	SET @GhiChuOnline = N'Doi Tru Online, ' + @GhiChu
	SET @GhiChu_TienThayDoi = @GhiChu
	
	SELECT top (1) @DmMaHopDong = hd.DmMaHopDongREF
	, @TenMaHopDong = hd.TenMaHopDong FROM dbo.HopDong hd
	WHERE hd.HopDongID = @HopDongID

	SET @DmMaHopDong = ISNULL(@DmMaHopDong,0)
	SET @TenMaHopDong = ISNULL(@TenMaHopDong,'')

	DECLARE @Table_thucchaydatinhAdmarket_id table(
	ThucChayDaTinhID NVARCHAR(50),
	HopDongREF INT,
	HopDongChiTietREF INT
	)

	SELECT TOP 1 @DanhSachNhanHangREF = DanhSachNhanHangREF, @TenSanPham = TenSanPham 
	FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID

	 ------TANG GIA TRI HOPDONG-------
	INSERT INTO dbo.ThucChayDaTinhAdmarket
	(
	    ThucChayDaTinhID,
	    HopDongID,
	    SoHopDong,
	    DmMaHopDongREF,
	    TenMaHopDong,
	    NgayDanhSoHopDong,
	    NgayKyHopDong,
	    NhanHopDong,
	    NgayNhanBanFax,
	    NgayNhanHopDongBanCung,
	    NgayChuyenHopDongChoKeToan,
	    So,
	    Thang,
	    Nam,
	    GiaTriHopDong,
	    CongNo,
	    HopDongChiTietREF,
	    DangSuDung,
	    IsGiayPhep,
	    TrangThaiHopDong,
	    IsBanCung,
	    DmPhongBanREF,
	    TenPhongBan,
	    DmBoPhanREF,
	    TenBoPhan,
	    DmNhomLamViecREF,
	    TenNhomLamViec,
	    DmDiaDiemLamViecREF,
	    TenDiaDiemLamViec,
	    SysNhanVienREF,
	    TenDangNhap,
	    TenNhanVien,
	    TenKhachHang,
	    NhanHang,
	    DmNhomNganhREF,
	    TenNhomNganh,
	    DmHinhThucQuangCao,
	    TenHinhThucQuangCao,
	    DmSanPhamREF,
	    TenSanPham,
	    DmNhomWebsiteREF,
	    TenNhomWebsite,
	    DmChuyenMucREF,
	    TenChuyenMuc,
	    DmLoaiBannerREF,
	    TenLoaiBanner,
	    DmViTriREF,
	    TenViTri,
	    DotChayHopDong,
	    SoLuongDotChayHD,
	    DotChayBooking,
	    SoLuongDotChayBooking,
	    SoLuong,
	    DonViTinh,
	    DonGia,
	    DonGiaTheoDonVi,
	    ChietKhau,
	    GiamGia,
	    ThanhTien,
	    TiLeTuVan,
	    ChiPhiTuVan,
	    IsKhuyenMai,
	    KhuyenMai,
	    DmBannerREF,
	    DmChienDichREF,
	    DmWebsiteREF,
	    TenWebsite,
	    TongViewThucChay,
	    TongClickThucChay,
	    TongSoBaiViet,
	    SoLuongThucChay,
	    NgayThucHien,
	    GiaTriThayDoi,
	    ThanhTienThucChayTruocTrietKhau,
	    GiaTriTrietKhauThucChay,
	    ThanhTienSauTrietKhauThucChay,
	    GiaTriHoaHongThucChay,
	    ThanhTienThucThu,
	    ThanhTienKM,
	    SoLuongThucChayKM,
	    SoLuongThucChayLechTreoHa,
	    ThanhTienLechTreoHa,
	    CreatedAt,
	    LastModifiedAt,
	    IsPheDuyet,
	    PheDuyetBy,
	    PheDuyetAt,
	    SoLuongThayDoi,
	    SoLuongKMThayDoi,
	    GiaTriKMThayDoi,
	    GhiChu
	)
	OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.HopDongID, inserted.HopDongChiTietREF INTO @Table_thucchaydatinhAdmarket_id
	SELECT 
	NEWID() thucchaydatinhid,
		HopDongID,
	    SoHopDong,
	    DmMaHopDongREF,
	    TenMaHopDong,
	    NgayDanhSoHopDong,
	    NgayKyHopDong,
	    NhanHopDong,
	    NgayNhanBanFax,
	    NgayNhanHopDongBanCung,
	    NgayChuyenHopDongChoKeToan,
	    So,
	    Thang,
	    Nam,
	    GiaTriHopDong,
	    CongNo,
	    HopDongChiTietREF,
	    DangSuDung,
	    IsGiayPhep,
	    TrangThaiHopDong,
	    IsBanCung,
	    DmPhongBanREF,
	    TenPhongBan,
	    DmBoPhanREF,
	    TenBoPhan,
	    DmNhomLamViecREF,
	    TenNhomLamViec,
	    DmDiaDiemLamViecREF,
	    TenDiaDiemLamViec,
	    SysNhanVienREF,
	    TenDangNhap,
	    TenNhanVien,
	    TenKhachHang,
	    NhanHang,
	    DmNhomNganhREF,
	    TenNhomNganh,
	    DmHinhThucQuangCao,
	    TenHinhThucQuangCao,
	    DmSanPhamREF,
	    TenSanPham,
	    DmNhomWebsiteREF,
	    TenNhomWebsite,
	    DmChuyenMucREF,
	    TenChuyenMuc,
	    DmLoaiBannerREF,
	    TenLoaiBanner,
	    DmViTriREF,
	    TenViTri,
	    DotChayHopDong,
	    SoLuongDotChayHD,
	    DotChayBooking,
	    SoLuongDotChayBooking,
	    SoLuong,
	    DonViTinh,
	    DonGia,
	    DonGiaTheoDonVi,
	    ChietKhau,
	    GiamGia,
	    ThanhTien,
	    TiLeTuVan,
	    ChiPhiTuVan,
	    IsKhuyenMai,
	    KhuyenMai,
	    DmBannerREF,
	    DmChienDichREF,
	    @DmWebsiteREF AS DmWebsiteREF,
	    @TenWebsite TenWebsite,
	    0 TongViewThucChay,
	    0 TongClickThucChay,
	    0 TongSoBaiViet,
	    0 SoLuongThucChay,
	    @NgayThucHien NgayThucHien,
	    (SUM(GiaTriThayDoi + ThanhTienSauTrietKhauThucChay)/@TongThanhTienThucChayDaTinh)*@GiaTriThayDoi GiaTriThayDoi,
	    0 ThanhTienThucChayTruocTrietKhau,
	    0 GiaTriTrietKhauThucChay,
	    0 ThanhTienSauTrietKhauThucChay,
	    0 GiaTriHoaHongThucChay,
	    0 ThanhTienThucThu,
	    0 ThanhTienKM,
	    0 SoLuongThucChayKM,
	    0 SoLuongThucChayLechTreoHa,
	    0 ThanhTienLechTreoHa,
	    GETDATE() CreatedAt,
	    GETDATE() LastModifiedAt,
	    0 IsPheDuyet,
	    '' PheDuyetBy,
	    GETDATE() PheDuyetAt,
	    0 SoLuongThayDoi,
	    0 SoLuongKMThayDoi,
	    0 GiaTriKMThayDoi,
	    @GhiChu_TienThayDoi GhiChu
		FROM dbo.ThucChayDaTinhAdmarket tcdta
		WHERE tcdta.HopDongID = @HopDongID
		AND tcdta.HopDongChiTietREF = @HopDongChiTietID
		AND tcdta.DmSanPhamREF = @DmSanPhamREF
		AND tcdta.NgayThucHien <= @NgayThucHien
		GROUP BY HopDongID,
	    SoHopDong,
	    DmMaHopDongREF,
	    TenMaHopDong,
	    NgayDanhSoHopDong,
	    NgayKyHopDong,
	    NhanHopDong,
	    NgayNhanBanFax,
	    NgayNhanHopDongBanCung,
	    NgayChuyenHopDongChoKeToan,
	    So,
	    Thang,
	    Nam,
	    GiaTriHopDong,
	    CongNo,
	    HopDongChiTietREF,
	    DangSuDung,
	    IsGiayPhep,
	    TrangThaiHopDong,
	    IsBanCung,
	    DmPhongBanREF,
	    TenPhongBan,
	    DmBoPhanREF,
	    TenBoPhan,
	    DmNhomLamViecREF,
	    TenNhomLamViec,
	    DmDiaDiemLamViecREF,
	    TenDiaDiemLamViec,
	    SysNhanVienREF,
	    TenDangNhap,
	    TenNhanVien,
	    TenKhachHang,
	    NhanHang,
	    DmNhomNganhREF,
	    TenNhomNganh,
	    DmHinhThucQuangCao,
	    TenHinhThucQuangCao,
	    DmSanPhamREF,
	    TenSanPham,
	    DmNhomWebsiteREF,
	    TenNhomWebsite,
	    DmChuyenMucREF,
	    TenChuyenMuc,
	    DmLoaiBannerREF,
	    TenLoaiBanner,
	    DmViTriREF,
	    TenViTri,
	    DotChayHopDong,
	    SoLuongDotChayHD,
	    DotChayBooking,
	    SoLuongDotChayBooking,
	    SoLuong,
	    DonViTinh,
	    DonGia,
	    DonGiaTheoDonVi,
	    ChietKhau,
	    GiamGia,
	    ThanhTien,
	    TiLeTuVan,
	    ChiPhiTuVan,
	    IsKhuyenMai,
	    KhuyenMai,
	    DmBannerREF,
	    DmChienDichREF


	 IF(EXISTS(SELECT ISNULL(ThucChayDaTinhID,'') FROM @Table_thucchaydatinhAdmarket_id ))
	 BEGIN
		 ------GIAM GIA TRI ONLINE--------
		 INSERT INTO dbo.ThucChayDaTinhAdmarket
		(
			ThucChayDaTinhID,
			HopDongID,
			SoHopDong,
			DmMaHopDongREF,
			TenMaHopDong,
			NgayDanhSoHopDong,
			NgayKyHopDong,
			NhanHopDong,
			NgayNhanBanFax,
			NgayNhanHopDongBanCung,
			NgayChuyenHopDongChoKeToan,
			So,
			Thang,
			Nam,
			GiaTriHopDong,
			CongNo,
			HopDongChiTietREF,
			DangSuDung,
			IsGiayPhep,
			TrangThaiHopDong,
			IsBanCung,
			DmPhongBanREF,
			TenPhongBan,
			DmBoPhanREF,
			TenBoPhan,
			DmNhomLamViecREF,
			TenNhomLamViec,
			DmDiaDiemLamViecREF,
			TenDiaDiemLamViec,
			SysNhanVienREF,
			TenDangNhap,
			TenNhanVien,
			TenKhachHang,
			NhanHang,
			DmNhomNganhREF,
			TenNhomNganh,
			DmHinhThucQuangCao,
			TenHinhThucQuangCao,
			DmSanPhamREF,
			TenSanPham,
			DmNhomWebsiteREF,
			TenNhomWebsite,
			DmChuyenMucREF,
			TenChuyenMuc,
			DmLoaiBannerREF,
			TenLoaiBanner,
			DmViTriREF,
			TenViTri,
			DotChayHopDong,
			SoLuongDotChayHD,
			DotChayBooking,
			SoLuongDotChayBooking,
			SoLuong,
			DonViTinh,
			DonGia,
			DonGiaTheoDonVi,
			ChietKhau,
			GiamGia,
			ThanhTien,
			TiLeTuVan,
			ChiPhiTuVan,
			IsKhuyenMai,
			KhuyenMai,
			DmBannerREF,
			DmChienDichREF,
			DmWebsiteREF,
			TenWebsite,
			TongViewThucChay,
			TongClickThucChay,
			TongSoBaiViet,
			SoLuongThucChay,
			NgayThucHien,
			GiaTriThayDoi,
			ThanhTienThucChayTruocTrietKhau,
			GiaTriTrietKhauThucChay,
			ThanhTienSauTrietKhauThucChay,
			GiaTriHoaHongThucChay,
			ThanhTienThucThu,
			ThanhTienKM,
			SoLuongThucChayKM,
			SoLuongThucChayLechTreoHa,
			ThanhTienLechTreoHa,
			CreatedAt,
			LastModifiedAt,
			IsPheDuyet,
			PheDuyetBy,
			PheDuyetAt,
			SoLuongThayDoi,
			SoLuongKMThayDoi,
			GiaTriKMThayDoi,
			GhiChu
		)
	
		SELECT 
			NEWID() ThucChayDaTinhID,
			0		AS		HopDongID,
			'-'		AS		SoHopDong,
			@DmMaHopDong AS DmMaHopDongREF,
			@TenMaHopDong AS TenMaHopDong,
			'1900-01-01'		AS		NgayDanhSoHopDong,
			'1900-01-01'		AS		NgayKyHopDong,
			''		AS		NhanHopDong,
			'1900-01-01'		AS		NgayNhanBanFax,
			'1900-01-01'		AS		NgayNhanHopDongBanCung,
			'1900-01-01'		AS		NgayChuyenHopDongChoKeToan,
			0		AS		So,
			0		AS		Thang,
			0		AS		Nam,
			0		AS		GiaTriHopDong,
			0		AS		CongNo,
			0		AS		HopDongChiTietREF,
			0		AS		DangSuDung,
			0		AS		IsGiayPhep,
			1		AS		TrangThaiHopDong,
			0		AS		IsBanCung,
			0		AS		DmPhongBanREF,
			''		AS		TenPhongBan,
			0		AS		DmBoPhanREF,
			''		AS		TenBoPhan,
			0		AS		DmNhomLamViecREF,
			''		AS		TenNhomLamViec,
			0		AS		DmDiaDiemLamViecREF,
			''		AS		TenDiaDiemLamViec,
			0		AS		SysNhanVienREF,
			''		AS		TenDangNhap,
			''		AS		TenNhanVien,
			''		AS		TenKhachHang,
			''		AS		NhanHang,
			0		AS		DmNhomNganhREF,
			''		AS		TenNhomNganh,
			0		AS		DmHinhThucQuangCao,
			''		AS		TenHinhThucQuangCao,
			DmSanPhamREF		AS		DmSanPhamREF,
			TenSanPham		AS		TenSanPham,
			0		AS		DmNhomWebsiteREF,
			''		AS		TenNhomWebsite,
			0		AS		DmChuyenMucREF,
			''		AS		TenChuyenMuc,
			0		AS		DmLoaiBannerREF,
			''		AS		TenLoaiBanner,
			DmViTriREF,
			TenViTri,
			''		AS		DotChayHopDong,
		    0		AS		SoLuongDotChayHD,
			@ThucChay_PerformanceBase_ThayDoi_ID		AS		DotChayBooking,
			@ThucChay_PerformanceBase_ThayDoi_ID		AS		SoLuongDotChayBooking,
			0		AS		SoLuong,
			@DonViTinh		AS		DonViTinh,
			0		AS		DonGia,
			0		AS		DonGiaTheoDonVi,
			0		AS		ChietKhau,
			0		AS		GiamGia,
			0		AS		ThanhTien,
			0		AS		TiLeTuVan,
			0		AS		ChiPhiTuVan,
			0		AS		IsKhuyenMai,
			''		AS		KhuyenMai,
			0		AS		DmBannerREF,
			0		AS		DmChienDichREF,
			@DmWebsiteREF		AS		DmWebsiteREF,
			@TenWebsite		AS		TenWebsite,
			0		AS		TongViewThucChay,
			0		AS		TongClickThucChay,
			0		AS		TongSoBaiViet,
			0		AS		SoLuongThucChay,
			@NgayThucHien		AS		NgayThucHien,
			-SUM(GiaTriThayDoi + ThanhTienSauTrietKhauThucChay) 		AS		GiaTriThayDoi,
			0		AS		ThanhTienThucChayTruocTrietKhau,
			0		AS		GiaTriTrietKhauThucChay,
			0		AS		ThanhTienSauTrietKhauThucChay,
			0		AS		GiaTriHoaHongThucChay,
			-SUM(GiaTriThayDoi + ThanhTienSauTrietKhauThucChay)		AS		ThanhTienThucThu,
			0		AS		ThanhTienKM,
			0		AS		SoLuongThucChayKM,
			0		AS		SoLuongThucChayLechTreoHa,
			0		AS		ThanhTienLechTreoHa,
			GETDATE()		AS		CreatedAt,
			GETDATE()		AS		LastModifiedAt,
			0		AS		IsPheDuyet,
			''		AS		PheDuyetBy,
			''		AS		PheDuyetAt,
			0		AS		SoLuongThayDoi,
			0		AS		SoLuongKMThayDoi,
			0		AS		GiaTriKMThayDoi,
			@GhiChuOnline		AS		GhiChu
			FROM dbo.ThucChayDaTinhAdmarket tcdto
			INNER JOIN @Table_thucchaydatinhAdmarket_id t on tcdto.ThucChayDaTinhID = t.ThucChayDaTinhID
			WHERE tcdto.HopDongID = @HopDongID
			AND tcdto.DmSanPhamREF = @DmSanPhamREF
			GROUP BY tcdto.DmSanPhamREF, tcdto.TenSanPham, tcdto.DmVitriREF, tcdto.TenViTri
	END

	SELECT top (1) @ThucChayDaTinhID_output = ISNULL(ThucChayDaTinhID,'') FROM @Table_thucchaydatinhAdmarket_id
END

```
