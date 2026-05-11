# Stored Procedure: `ThucChay_InsertGTTDThucChayDaTinhAdmarket_DoiTruGiam_HopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-29 11:27:44.607000
- **Ngày sửa cuối**: 2018-06-02 08:01:52.947000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@Tk_Admarket` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*

*/
CREATE PROCEDURE [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_DoiTruGiam_HopDong]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@HopDongID INT,
	@DmSanPhamREF INT, 
	@Tk_Admarket NVARCHAR(50)
AS
BEGIN
	 DECLARE @DonViTinh NVARCHAR(100), @TenSanPham NVARCHAR(200)=''
	  , @GhiChu NVARCHAR(MAX) = '', @GhiChu_HD NVARCHAR(MAX) =''
	SET @DonViTinh = 'CPC'
	SET @TenSanPham =''

	SET @GhiChu_HD = N'DoiTruGiam theo hopdong: ' + CONVERT(NVARCHAR(100),@DmSanPhamREF) + '_' + @Tk_Admarket 
	 ------GIAM GIA TRI HOPDONG-------
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
	
	SELECT  NEWID() AS ThucChayDaTinhID,
			tc.HopDongID,
			tc.SoHopDong,
			tc.DmMaHopDongREF,
			tc.TenMaHopDong,
			tc.NgayDanhSoHopDong,
			tc.NgayKyHopDong,
			tc.NhanHopDong,
			tc.NgayNhanBanFax,
			tc.NgayNhanHopDongBanCung,
			tc.NgayChuyenHopDongChoKeToan,
			tc.So,
			tc.Thang,
			tc.Nam,
			tc.GiaTriHopDong,
			tc.CongNo,
			tc.HopDongChiTietREF,
			tc.DangSuDung,
			tc.IsGiayPhep,
			tc.TrangThaiHopDong,
			tc.IsBanCung,
			tc.DmPhongBanREF,
			tc.TenPhongBan,
			tc.DmBoPhanREF,
			tc.TenBoPhan,
			tc.DmNhomLamViecREF,
			tc.TenNhomLamViec,
			tc.DmDiaDiemLamViecREF,
			tc.TenDiaDiemLamViec,
			tc.SysNhanVienREF,
			tc.TenDangNhap,
			tc.TenNhanVien,
			tc.TenKhachHang,
			tc.NhanHang,
			tc.DmNhomNganhREF,
			tc.TenNhomNganh,
			tc.DmHinhThucQuangCao,
			tc.TenHinhThucQuangCao,
			tc.DmSanPhamREF,
			tc.TenSanPham,
			tc.DmNhomWebsiteREF,
			tc.TenNhomWebsite,
			tc.DmChuyenMucREF,
			tc.TenChuyenMuc,
			tc.DmLoaiBannerREF,
			tc.TenLoaiBanner,
			tc.DmViTriREF,
			tc.TenViTri,
			tc.DotChayHopDong,
			tc.SoLuongDotChayHD,
			@Tk_Admarket DotChayBooking,
			tc.SoLuongDotChayBooking,
			tc.SoLuong,
			tc.DonViTinh,
			tc.DonGia,
			tc.DonGiaTheoDonVi,
			tc.ChietKhau,
			tc.GiamGia,
			tc.ThanhTien,
			tc.TiLeTuVan,
			tc.ChiPhiTuVan,
			tc.IsKhuyenMai,
			tc.KhuyenMai,
			tc.DmBannerREF,
			tc.DmChienDichREF,
			tc.DmWebsiteREF,
			tc.TenWebsite,
			0 AS TongViewThucChay,
			0 AS TongClickThucChay,
			0 AS TongSoBaiViet,
			0 AS SoLuongThucChay,
			@NgayThucHien AS NgayThucHien,
			-(tc.ThanhTienSauTrietKhauThucChay + tc.GiaTriThayDoi) AS GiaTriThayDoi,
			0 AS ThanhTienThucChayTruocTrietKhau,
			0 AS GiaTriTrietKhauThucChay,
			0 AS ThanhTienSauTrietKhauThucChay,
			0 AS GiaTriHoaHongThucChay,
			-(tc.ThanhTienSauTrietKhauThucChay + tc.GiaTriThayDoi) AS ThanhTienThucThu,
			0 AS ThanhTienKM,
			0 AS SoLuongThucChayKM,
			0 AS SoLuongThucChayLechTreoHa,
			0 AS ThanhTienLechTreoHa,
			GETDATE() AS CreatedAt,
			GETDATE() AS  LastModifiedAt,
			0 AS IsPheDuyet,
			'' AS PheDuyetBy,
			'' AS PheDuyetAt,
			-(TC.SoLuongThucChay + tc.SoLuongThayDoi) AS SoLuongThayDoi,
			-(tc.SoLuongThucChayKM + tc.SoLuongKMThayDoi) AS SoLuongKMThayDoi,
			-(tc.ThanhTienKM + tc.GiaTriKMThayDoi) AS GiaTriKMThayDoi,
			@GhiChu_HD AS GhiChu
			FROM (SELECT tcdt.* FROM dbo.ThucChayDaTinhAdmarket tcdt 
				WHERE tcdt.HopDongID = @HopDongID
				AND tcdt.DmSanPhamREF = @DmSanPhamREF 
				AND tcdt.NgayThucHien <= @NgayThucHien
			)tc INNER JOIN 
			(SELECT hdct.HopDongChiTietID, hdct.DmSanPhamREF 
				FROM dbo.HopDongChiTiet hdct 
				WHERE hdct.HopDongFK = @HopDongID 
				AND hdct.DmSanPhamREF = @DmSanPhamREF 
				AND hdct.TK_AdMarket = @Tk_Admarket
			)hdct ON tc.HopDongChitietREF = hdct.HopDongChiTietID AND hdct.DmSanPhamREF = tc.DmSanPhamREF
			

	-- ------TANG GIA TRI ONLINE--------
	SET @GhiChu =  N'DoiTruTang theo hopdong ONLINE: ' + CONVERT(NVARCHAR(100),@DmSanPhamREF) + '_' + @Tk_Admarket 
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
	TC.NhanHang		AS		NhanHang,
	0		AS		DmNhomNganhREF,
	''		AS		TenNhomNganh,
	0		AS		DmHinhThucQuangCao,
	''		AS		TenHinhThucQuangCao,
	TC.DmSanPhamREF		AS		DmSanPhamREF,
	TC.TenSanPham		AS		TenSanPham,
	0		AS		DmNhomWebsiteREF,
	''		AS		TenNhomWebsite,
	0		AS		DmChuyenMucREF,
	''		AS		TenChuyenMuc,
	0		AS		DmLoaiBannerREF,
	''		AS		TenLoaiBanner,
	TC.DmViTriREF		AS		DmViTriREF,
	TC.TenViTri		AS		TenViTri,
	'MuaOnline'		AS		DotChayHopDong,
	0		AS		SoLuongDotChayHD,
	@Tk_Admarket		AS		DotChayBooking,
	0		AS		SoLuongDotChayBooking,
	0		AS		SoLuong,
	TC.DonViTinh		AS		DonViTinh,
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
	TC.DmWebsiteREF		AS		DmWebsiteREF,
	TC.TenWebsite		AS		TenWebsite,
	0		AS		TongViewThucChay,
	0		AS		TongClickThucChay,
	0		AS		TongSoBaiViet,
	0		AS		SoLuongThucChay,
	@NgayThucHien		AS		NgayThucHien,
	--(TC.ThanhTienSauTrietKhauThucChay + TC.GiaTriThayDoi)		AS		GiaTriThayDoi,
	-(TC.ThanhTienSauTrietKhauThucChay + TC.GiaTriThayDoi)		AS		GiaTriThayDoi,
	0		AS		ThanhTienThucChayTruocTrietKhau,
	0		AS		GiaTriTrietKhauThucChay,
	0		AS		ThanhTienSauTrietKhauThucChay,
	0		AS		GiaTriHoaHongThucChay,
	--(TC.ThanhTienSauTrietKhauThucChay + TC.GiaTriThayDoi)		AS		ThanhTienThucThu,
	-(TC.ThanhTienSauTrietKhauThucChay + TC.GiaTriThayDoi)		AS		ThanhTienThucThu,
	0		AS		ThanhTienKM,
	0		AS		SoLuongThucChayKM,
	0		AS		SoLuongThucChayLechTreoHa,
	0		AS		ThanhTienLechTreoHa,
	GETDATE()		AS		CreatedAt,
	GETDATE()		AS		LastModifiedAt,
	0		AS		IsPheDuyet,
	''		AS		PheDuyetBy,
	''		AS		PheDuyetAt,
	(TC.SoLuongThucChay + TC.SoLuongThayDoi)		AS		SoLuongThayDoi,
	0		AS		SoLuongKMThayDoi,
	0		AS		GiaTriKMThayDoi,
	@GhiChu		AS		GhiChu
	FROM (SELECT tcdt.* FROM dbo.ThucChayDaTinhAdmarket tcdt 
				WHERE tcdt.HopDongID = @HopDongID
				AND tcdt.DmSanPhamREF = @DmSanPhamREF 
				--AND tcdt.NgayThucHien < @NgayThucHien
				--AND ((tcdt.NgayThucHien = @NgayThucHien) AND (tcdt.GhiChu <> @GhiChu_HD))
				AND ((tcdt.NgayThucHien = @NgayThucHien) AND (tcdt.GhiChu = @GhiChu_HD))
		)tc INNER JOIN 
		(SELECT hdct.HopDongChiTietID, hdct.DmSanPhamREF 
			FROM dbo.HopDongChiTiet hdct 
			WHERE hdct.HopDongFK = @HopDongID 
			AND hdct.DmSanPhamREF = @DmSanPhamREF 
			AND hdct.TK_AdMarket = @Tk_Admarket
		)hdct ON tc.HopDongChitietREF = hdct.HopDongChiTietID AND hdct.DmSanPhamREF = tc.DmSanPhamREF
	
END

```
