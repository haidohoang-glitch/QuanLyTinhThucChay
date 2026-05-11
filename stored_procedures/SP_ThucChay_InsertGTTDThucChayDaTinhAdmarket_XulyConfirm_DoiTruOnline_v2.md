# Stored Procedure: `ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-12-29 16:30:27.733000
- **Ngày sửa cuối**: 2025-04-03 14:40:22.433000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThucChay_PerformanceBase_ThayDoi_ID` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@Tk` | `nvarchar(100)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(200)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@GiaTriKMThayDoi` | `float(8)` | No |
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
CREATE PROCEDURE [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirm_DoiTruOnline_v2]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@ThucChay_PerformanceBase_ThayDoi_ID INT,
	@HopDongID INT,
	@HopDongChiTietID INT, 
	@DmSanPhamREF INT, 
	@Tk NVARCHAR(50),
	@DmViTriREF INT,
	@TenViTri NVARCHAR(100),
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(200),
	@GiaTriThayDoi FLOAT, 
	@GiaTriKMThayDoi float,
	@GhiChu nvarchar(200),
	@ThucChayDaTinhID_output NVARCHAR(50) OUTPUT
AS
BEGIN
	 DECLARE @SoLuongThayDoi INT = 0, @DonViTinh NVARCHAR(100), @SoLuongThucChay INT = 0, @TenSanPham NVARCHAR(200)=''
	  , @DanhSachNhanHangREF NVARCHAR(200) = ''
	  , @GhiChuOnline NVARCHAR(500) = N''
	  , @GhiChu_TienThayDoi NVARCHAR(500) = N''
	SET @DonViTinh = 'CPC'
	SET @TenSanPham =''
	SET @GhiChuOnline = N'MuaOnline, Tk:' +@Tk + ', HDCT: ' + Convert(nvarchar(100),@HopDongChiTietID) + ', ThucChay_ThayDoi_ID: '+ Convert(NVARCHAR(100),@ThucChay_PerformanceBase_ThayDoi_ID)
	SET @GhiChu_TienThayDoi = N'ThaydoitheoHopDong, Tk:' +@Tk + ', HDCT: ' + Convert(nvarchar(100),@HopDongChiTietID) + ', ThucChay_ThayDoi_ID: '+ Convert(NVARCHAR(100),@ThucChay_PerformanceBase_ThayDoi_ID)

	DECLARE @Table_thucchaydatinhAdmarket_id table(
	ThucChayDaTinhID NVARCHAR(50),
	HopDongREF INT
	)

	SELECT TOP 1 @DanhSachNhanHangREF = DanhSachNhanHangREF, @TenSanPham = TenSanPham 
	FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID

	SET @GhiChu = N'XulyConfirm_DoiTruOnline: ' + CONVERT(NVARCHAR(100),@DmSanPhamREF) + '_' + @Tk+ '_Bosung/Giamgiatri'
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
	OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.HopDongID INTO @Table_thucchaydatinhAdmarket_id
	SELECT 
	NEWID() thucchaydatinhid,
	--ID Hop Dong
	D.HopDongID,
	--Thong tin ve ma so 
	D.SoHopDong, 
	D.DmMaHopDongREF, 
	D.TenMaHopDong, 
	--Thong tin ve thoi gian
	D.NgayDanhSoHopDong, D.NgayKyHopDong, 
	D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
	D.So, D.Thang, D.Nam, 
	--Thong tin ve gia tri
	D.GiaTriHopDong, D.CongNo,
	--Thong tin chi tiet phan bo
	C.HopDongChiTietID,
	--Thong tin ve trang thai
	D.DangSuDung, D.IsGiayPhep, 2 TrangThaiHopDong,D.IsBanCung, 
	--Thong tin ve Nhan vien kinh doanh
	D.DmPhongBanREF, 
	ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
	D.DmBoPhanREF, 
	ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
	D.DmNhomLamViecREF, 
	ISNULL(D.TenNhom, '') AS TenNhom, 
	D.DmDiaDiemLamViecREF, 
	D.TenDiaDiemLamViec, 
	D.SysNhanVienREF, 
	ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
	D.TenNhanVien, 
	D.TenKhachHang, 
	C.DanhSachNhanHangREF NhanHang, 
	C.DmNhomNganhREF, 
	C.TenNhomNganh, 
	C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
	c.DmSanPhamREF as DmSanPhamREF,
	C.TenSanPham,  
	C.DmNhomWebsiteREF, 
	C.TenNhomWebsite, 
	C.DmChuyenMucREF, 
	C.TenChuyenMuc,
	C.DmLoaiBannerREF, 
	C.TenLoaiBanner, 
	@DmViTriREF DmViTriREF, 
	@TenViTri TenViTri, 
	@Tk DotChayHopDong,
	0 AS SoLuongDotChayHD,
	@ThucChay_PerformanceBase_ThayDoi_ID DotChayBooking,
	@ThucChay_PerformanceBase_ThayDoi_ID AS SoLuongDotChayBooking, 
	C.SoLuong AS SoLuong, 
	@DonViTinh as DonViTinh, 
	C.DonGia as DonGia, 
	C.DonGia AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	0 DmBannerREF,
	0 DmChienDichREF,
	@DmWebsiteREF DmWebsiteREF,
	@TenWebsite TenWebsite,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	@SoLuongThucChay SoLuongThucChay,
	@NgayThucHien AS NgayThucHien,
	@GiaTriThayDoi as GiaTriThayDoi,	 
	0 as ThanhTienThucChayTruocTrietKhau,
	0 AS GiaTriTrietKhauThucChay,
	0 AS ThanhTienSauTrietKhauThucChay,	
	0 AS GiaTriHoaHongThucChay,
	@GiaTriThayDoi AS ThanhTienThucThu,
	@GiaTriKMThayDoi as ThanhTienKM,
	0 as SoLuongThucChayKM,
	0 SoLuongLechTreoHa,
	0 ThanhTienLechTreoHa,
	GETDATE() createdat,
	GETDATE() lastmodifiedat,
	0 IsPheDuyet,
	'' PheDuyetBy,
	'' PheDuyetAt,
	@SoLuongThayDoi SoLuongThayDoi,
	0 SoLuongKMThayDoi,
	0 GiaTriKMThayDoi,
    @GhiChu_TienThayDoi GhiChu	
	
	FROM 
	(
		SELECT * FROM dbo.HopDongChiTiet 
			WHERE HopDongChiTietID = @HopDongChiTietID
						AND DmSanPhamREF = @DmSanPhamREF
						AND TK_AdMarket = @Tk
				AND RecordStatus = 0
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM dbo.HopDong hd 
	 	WHERE 1=1-- hd.TrangThaiHopDong <> 3	    
	       AND hd.HopDongID = @HopDongID
	       AND hd.DeletedStatus = 0
	 ) D on D.HopDongID = C.HopDongFK


	 SELECT top (1) @ThucChayDaTinhID_output = ISNULL(ThucChayDaTinhID,'') FROM @Table_thucchaydatinhAdmarket_id 

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
	0		AS		DmMaHopDongREF,
	''		AS		TenMaHopDong,
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
	@DanhSachNhanHangREF		AS		NhanHang,
	0		AS		DmNhomNganhREF,
	''		AS		TenNhomNganh,
	0		AS		DmHinhThucQuangCao,
	''		AS		TenHinhThucQuangCao,
	@DmSanPhamREF		AS		DmSanPhamREF,
	@TenSanPham		AS		TenSanPham,
	0		AS		DmNhomWebsiteREF,
	''		AS		TenNhomWebsite,
	0		AS		DmChuyenMucREF,
	''		AS		TenChuyenMuc,
	0		AS		DmLoaiBannerREF,
	''		AS		TenLoaiBanner,
	@DmViTriREF		AS		DmViTriREF,
	@TenViTri		AS		TenViTri,
	@Tk    		AS		DotChayHopDong,
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
	-@GiaTriThayDoi		AS		GiaTriThayDoi,
	0		AS		ThanhTienThucChayTruocTrietKhau,
	0		AS		GiaTriTrietKhauThucChay,
	0		AS		ThanhTienSauTrietKhauThucChay,
	0		AS		GiaTriHoaHongThucChay,
	-@GiaTriThayDoi		AS		ThanhTienThucThu,
	-@GiaTriKMThayDoi		AS		ThanhTienKM,
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

	
END

```
