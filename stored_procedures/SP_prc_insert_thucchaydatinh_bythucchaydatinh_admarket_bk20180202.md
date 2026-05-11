# Stored Procedure: `prc_insert_thucchaydatinh_bythucchaydatinh_admarket_bk20180202`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-02-02 15:33:30.880000
- **Ngày sửa cuối**: 2018-02-02 15:33:30.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngaythuchien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- exec [dbo].[prc_insert_thucchaydatinh_bythucchaydatinh_admarket]  '2017-06-06'
CREATE PROCEDURE [dbo].[prc_insert_thucchaydatinh_bythucchaydatinh_admarket_bk20180202] 
	-- Add the parameters for the stored procedure here
	@ngaythuchien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	delete from thucchaydatinh where ngaythuchien = @ngaythuchien and dmsanphamref IN( 628,144,585);
	-- view plus 
	insert into thucchaydatinh
		select
		newid(),
		0 HopDongID,
		'-' SoHopDong,
		0 DmMaHopDongREF,
		'' TenMaHopDong,
		getdate() NgayDanhSoHopDong,
		getdate() NgayKyHopDong,
		'' NhanHopDong,
		getdate() NgayNhanBanFax,
		getdate() NgayNhanHopDongBanCung,
		getdate() NgayChuyenHopDongChoKeToan,
		'0' So,
		0 Thang,
		0 Nam,
		0 GiaTriHopDong,
		0 CongNo,
		0 HopDongChiTietREF,
		5001 DangSuDung,
		0 IsGiayPhep,
		0 TrangThaiHopDong,
		0 IsBanCung,
		-1 DmPhongBanREF,
		'' TenPhongBan,
		-1 DmBoPhanREF,
		'' TenBoPhan,
		-1 DmNhomLamViecREF,
		'-' TenNhomLamViec,
		0 DmDiaDiemLamViecREF,
		'' TenDiaDiemLamViec,
		0 SysNhanVienREF,
		'-' TenDangNhap,
		'-' TenNhanVien,
		'' TenKhachHang,
		'' NhanHang,
		'0' DmNhomNganhREF,
		'' TenNhomNganh,
		7 DmHinhThucQuangCao,
		'CPC' TenHinhThucQuangCao,
		a.DmSanPhamREF,-------------------
		a.TenSanPham,---------------------
		0 DmNhomWebsiteREF,
		'' TenNhomWebsite,
		0 DmChuyenMucREF,
		'' TenChuyenMuc,
		0 DmLoaiBannerREF,
		'' TenLoaiBanner,
		0 DmViTriREF,
		'' TenViTri,
		'' DotChayHopDong,
		0 SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking,
		0 SoLuong,
		'CLICK' DonViTinh,
		0 DonGia,
		0 DonGiaTheoDonVi,
		0 ChietKhau,
		0 GiamGia,
		0 ThanhTien,
		0 TiLeTuVan,
		0 ChiPhiTuVan,
		0 IsKhuyenMai,
		'' KhuyenMai,
		0 DmBannerREF,
		0 DmChienDichREF,
		dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
		a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
		0 TongViewThucChay, -- cai nay dua vao phan moi nhe
		0 TongClickThucChay, -- cai nay dua vao phan moi nhe
		0 TongSoBaiViet,
		sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
		@ngaythuchien NgayThucHien, -- dien ngay vao nhe
		0 GiaTriThayDoi,
		0 ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		SUM(convert(money,a.[domain_money]))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
		0 GiaTriHoaHongThucChay,
		0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
		sum(convert(money,a.[domain_promotion]))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() CreatedAt,
		GETDATE() LastModifiedAt,
		'' IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		'' GhiChu
		from [dbo].[ThucChayAdmarket_ViewPlus_HopDong] a where (convert(money,a.[domain_money]) >0 OR convert(money,a.[domain_promotion]) > 0)
		AND a.NgayThucHien = @ngaythuchien and isnoibo = 0
		group by 
		a.domain_name,
		a.DmSanPhamREF,
		a.TenSanPham

		-- adx cpc 
	insert into thucchaydatinh
		select
		newid(),
		0 HopDongID,
		'-' SoHopDong,
		0 DmMaHopDongREF,
		'' TenMaHopDong,
		getdate() NgayDanhSoHopDong,
		getdate() NgayKyHopDong,
		'' NhanHopDong,
		getdate() NgayNhanBanFax,
		getdate() NgayNhanHopDongBanCung,
		getdate() NgayChuyenHopDongChoKeToan,
		'0' So,
		0 Thang,
		0 Nam,
		0 GiaTriHopDong,
		0 CongNo,
		0 HopDongChiTietREF,
		5001 DangSuDung,
		0 IsGiayPhep,
		0 TrangThaiHopDong,
		0 IsBanCung,
		-1 DmPhongBanREF,
		'' TenPhongBan,
		-1 DmBoPhanREF,
		'' TenBoPhan,
		-1 DmNhomLamViecREF,
		'-' TenNhomLamViec,
		0 DmDiaDiemLamViecREF,
		'' TenDiaDiemLamViec,
		0 SysNhanVienREF,
		'-' TenDangNhap,
		'-' TenNhanVien,
		'' TenKhachHang,
		'' NhanHang,
		'0' DmNhomNganhREF,
		'' TenNhomNganh,
		7 DmHinhThucQuangCao,
		'CPC' TenHinhThucQuangCao,
		a.DmSanPhamREF DmSanPhamREF,-------------------
		a.TenSanPham,---------------------
		0 DmNhomWebsiteREF,
		'' TenNhomWebsite,
		0 DmChuyenMucREF,
		'' TenChuyenMuc,
		0 DmLoaiBannerREF,
		'' TenLoaiBanner,
		DmViTriREF DmViTriREF,
		TenViTri TenViTri,
		'' DotChayHopDong,
		0 SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking,
		0 SoLuong,
		'CLICK' DonViTinh,
		0 DonGia,
		0 DonGiaTheoDonVi,
		0 ChietKhau,
		0 GiamGia,
		0 ThanhTien,
		0 TiLeTuVan,
		0 ChiPhiTuVan,
		0 IsKhuyenMai,
		'' KhuyenMai,
		0 DmBannerREF,
		0 DmChienDichREF,
		dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
		a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
		0 TongViewThucChay, -- cai nay dua vao phan moi nhe
		0 TongClickThucChay, -- cai nay dua vao phan moi nhe
		0 TongSoBaiViet,
		sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
		@ngaythuchien NgayThucHien, -- dien ngay vao nhe
		0 GiaTriThayDoi,
		0 ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		SUM(convert(money,a.domain_tt_money))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
		0 GiaTriHoaHongThucChay,
		0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
		SUM(convert(money,a.domain_tt_promotion))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() CreatedAt,
		GETDATE() LastModifiedAt,
		'' IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		'' GhiChu
		from [dbo].ThucChayAdmarket_ADX_CPC_HopDong a where (convert(money,a.domain_tt_money) > 0 OR convert(money,a.domain_tt_promotion) > 0)
		AND a.NgayThucHien = @ngaythuchien and isnoibo = 0
		GROUP by 
		a.DmSanPhamREF,
		a.TenSanPham,
		a.domain_name,
		a.DmViTriREF,
		a.TenViTri
		------------------------------------------Nội bộ---------------------------------
        insert into thucchaydatinh
		select
		newid(),
		0 HopDongID,
		'-' SoHopDong,
		310 DmMaHopDongREF,
		'NB' TenMaHopDong,
		getdate() NgayDanhSoHopDong,
		getdate() NgayKyHopDong,
		'' NhanHopDong,
		getdate() NgayNhanBanFax,
		getdate() NgayNhanHopDongBanCung,
		getdate() NgayChuyenHopDongChoKeToan,
		'0' So,
		0 Thang,
		0 Nam,
		0 GiaTriHopDong,
		0 CongNo,
		0 HopDongChiTietREF,
		5001 DangSuDung,
		0 IsGiayPhep,
		0 TrangThaiHopDong,
		0 IsBanCung,
		-1 DmPhongBanREF,
		'' TenPhongBan,
		-1 DmBoPhanREF,
		'' TenBoPhan,
		-1 DmNhomLamViecREF,
		'-' TenNhomLamViec,
		0 DmDiaDiemLamViecREF,
		'' TenDiaDiemLamViec,
		0 SysNhanVienREF,
		'-' TenDangNhap,
		'-' TenNhanVien,
		'' TenKhachHang,
		'' NhanHang,
		'0' DmNhomNganhREF,
		'' TenNhomNganh,
		7 DmHinhThucQuangCao,
		'CPC' TenHinhThucQuangCao,
		a.DmSanPhamREF,-------------------
		a.TenSanPham,---------------------
		0 DmNhomWebsiteREF,
		'' TenNhomWebsite,
		0 DmChuyenMucREF,
		'' TenChuyenMuc,
		0 DmLoaiBannerREF,
		'' TenLoaiBanner,
		0 DmViTriREF,
		'' TenViTri,
		'' DotChayHopDong,
		0 SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking,
		0 SoLuong,
		'CLICK' DonViTinh,
		0 DonGia,
		0 DonGiaTheoDonVi,
		0 ChietKhau,
		0 GiamGia,
		0 ThanhTien,
		0 TiLeTuVan,
		0 ChiPhiTuVan,
		0 IsKhuyenMai,
		'' KhuyenMai,
		0 DmBannerREF,
		0 DmChienDichREF,
		dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
		a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
		0 TongViewThucChay, -- cai nay dua vao phan moi nhe
		0 TongClickThucChay, -- cai nay dua vao phan moi nhe
		0 TongSoBaiViet,
		sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
		@ngaythuchien NgayThucHien, -- dien ngay vao nhe
		0 GiaTriThayDoi,
		0 ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		SUM(convert(money,a.[domain_money]))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
		0 GiaTriHoaHongThucChay,
		0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
		sum(convert(money,a.[domain_promotion]))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() CreatedAt,
		GETDATE() LastModifiedAt,
		'' IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		'' GhiChu
		from [dbo].[ThucChayAdmarket_ViewPlus_HopDong] a where (convert(money,a.[domain_money]) >0 OR convert(money,a.[domain_promotion]) > 0)
		AND a.NgayThucHien = @ngaythuchien and isnoibo = 1
		group by 
		a.domain_name,
		a.DmSanPhamREF,
		a.TenSanPham

		-- adx cpc 
	insert into thucchaydatinh
		select
		newid(),
		0 HopDongID,
		'-' SoHopDong,
		310 DmMaHopDongREF,
		'NB' TenMaHopDong,
		getdate() NgayDanhSoHopDong,
		getdate() NgayKyHopDong,
		'' NhanHopDong,
		getdate() NgayNhanBanFax,
		getdate() NgayNhanHopDongBanCung,
		getdate() NgayChuyenHopDongChoKeToan,
		'0' So,
		0 Thang,
		0 Nam,
		0 GiaTriHopDong,
		0 CongNo,
		0 HopDongChiTietREF,
		5001 DangSuDung,
		0 IsGiayPhep,
		0 TrangThaiHopDong,
		0 IsBanCung,
		-1 DmPhongBanREF,
		'' TenPhongBan,
		-1 DmBoPhanREF,
		'' TenBoPhan,
		-1 DmNhomLamViecREF,
		'-' TenNhomLamViec,
		0 DmDiaDiemLamViecREF,
		'' TenDiaDiemLamViec,
		0 SysNhanVienREF,
		'-' TenDangNhap,
		'-' TenNhanVien,
		'' TenKhachHang,
		'' NhanHang,
		'0' DmNhomNganhREF,
		'' TenNhomNganh,
		7 DmHinhThucQuangCao,
		'CPC' TenHinhThucQuangCao,
		a.DmSanPhamREF DmSanPhamREF,-------------------
		a.TenSanPham,---------------------
		0 DmNhomWebsiteREF,
		'' TenNhomWebsite,
		0 DmChuyenMucREF,
		'' TenChuyenMuc,
		0 DmLoaiBannerREF,
		'' TenLoaiBanner,
		DmViTriREF DmViTriREF,
		TenViTri TenViTri,
		'' DotChayHopDong,
		0 SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking,
		0 SoLuong,
		'CLICK' DonViTinh,
		0 DonGia,
		0 DonGiaTheoDonVi,
		0 ChietKhau,
		0 GiamGia,
		0 ThanhTien,
		0 TiLeTuVan,
		0 ChiPhiTuVan,
		0 IsKhuyenMai,
		'' KhuyenMai,
		0 DmBannerREF,
		0 DmChienDichREF,
		dbo.GetWebsiteIDByDomainName(a.domain_name),-- DmWebsiteREF, -- cai nay dua vao phan moi nhe
		a.domain_name TenWebsite,  -- cai nay dua vao phan moi nhe
		0 TongViewThucChay, -- cai nay dua vao phan moi nhe
		0 TongClickThucChay, -- cai nay dua vao phan moi nhe
		0 TongSoBaiViet,
		sum(convert(int,ISNULL(a.domain_tt_click,0))) SoLuongThucChay, -- lay tong click thuc chay nhe 
		@ngaythuchien NgayThucHien, -- dien ngay vao nhe
		0 GiaTriThayDoi,
		0 ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		SUM(convert(money,a.domain_tt_money))/1.1 ThanhTienSauTrietKhauThucChay, -- dien gia tri  tu bang nhe
		0 GiaTriHoaHongThucChay,
		0 ThanhTienThucThu, -- dien gia tri  tu bang nhe
		SUM(convert(money,a.domain_tt_promotion))/1.1 ThanhTienKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayKM, -- dien gia tri  tu bang nhe
		0 SoLuongThucChayLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() CreatedAt,
		GETDATE() LastModifiedAt,
		'' IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		'' GhiChu
		from [dbo].ThucChayAdmarket_ADX_CPC_HopDong a where (convert(money,a.domain_tt_money) > 0 OR convert(money,a.domain_tt_promotion) > 0)
		AND a.NgayThucHien = @ngaythuchien and isnoibo = 1
		GROUP by 
		a.DmSanPhamREF,
		a.TenSanPham,
		a.domain_name,
		a.DmViTriREF,
		a.TenViTri
   --------------------------------------------------------------------------------------------------
END


```
