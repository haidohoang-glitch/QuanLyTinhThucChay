# Stored Procedure: `ThucChay_InsertThucChayDaTinh_SponsorPostNotBySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-11 10:42:51.793000
- **Ngày sửa cuối**: 2014-11-19 12:24:53.170000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- Stored Procedure

-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-04-25
-- Description:	Insert Thuc chay san pham Mobile khong co hop dong
-- =============================================
--
-- EXEC dbo.[ThucChay_InsertThucChayDaTinh_SponsorPostNotBySoHopDong] '2014-06-19'
--
CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_SponsorPostNotBySoHopDong] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- Xoa du lieu neu da ton tai
	DELETE FROM ThucChayDaTinh WHERE NgayThucHien = @NgayThucHien AND DmSanPhamREF = 381 AND SoHopDong = '-'

	-- Insert du lieu
	INSERT INTO ThucChayDaTinh
	SELECT 
		NEWID(),
		0 HopDongID,
		'-' SoHopDong,
		0 DmMaHopDongREF,
		'' TenMaHopDong,
		'1900-01-01 00:00:00.000' NgayDanhSoHopDong, 
		'1900-01-01 00:00:00.000' NgayKyHopDong,
		'' NhanHopDong, 
		'1900-01-01 00:00:00.000' NgayNhanBanFax,
		'1900-01-01 00:00:00.000' NgayNhanHopDongBanCung,
		'1900-01-01 00:00:00.000' NgayChuyenHopDongChoKeToan,
		0 So, 0 Thang, 0 Nam,
		0 GiaTriHopDong, 0 CongNo,
		0 HopDongChiTietID,
		0 DangSuDung, 0 IsGiayPhep,
		1 TrangThaiHopDong, 0 IsBanCung,
		0 DmPhongBanREF, '-' TenPhongBan,
		0 DmBoPhanREF, '-' TenBoPhan,
		0 DmNhomLamViecREF, '-' TenNhom,
		0 DmDiaDiemLamViecREF, '-' TenDiaDiemLamViec,
		ISNULL((SELECT TOP 1 NhanSuSoYeuLyLichID FROM AdminPermisionHDCN WHERE TenDangNhap = tc.UserName),0) as SysNhanVienREF, 
		ISNULL(tc.UserName,'-') TenDangNhap, 
		ISNULL(tc.SaleName,'') TenNhanVien,
		'-' TenKhachHang,
		'' NhanHang,
		0 DmNhomNganhREF, '' TenNhomNganh,
		7 DmHinhThucQuangCao,-- CPC	
		'CPC' TenHinhThucQuangCao,                                                                                                                     			 
		381 DmSanPhamREF,
		'Sponsor Post' TenSanPham,
		0 DmNhomWebsiteREF, '' TenNhomWebsite,
		0 DmChuyenMucREF, '' TenChuyenMuc,
		0 DmLoaiBannerREF, '' TenLoaiBanner,
		'' DmViTriREF, 
		'' TenViTri,
		'' DotChayHopDong,
		0 AS SoLuongDotChayHD,
		0  DotChayBooking,
		0 SoLuongDotChayBooking,
		0 SoLuong,
		'CLICK' DonViTinh,
		dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381) AS DonGia,		
		dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381)AS DonGiaTheoDonViTinh,
		0 ChietKhau, 0 GiamGia, 0 ThanhTien,
		0 TiLeTuVan, 0 ChiPhiTuVan,
		0 isKhuyenMai, 0 KhuyenMai,
		--Thuc chay
		tc.DmBannerREF,
		tc.DmChienDichREF,
		tc.DmWebsiteREF,
		tc.TenWebsite,
		tc.TongViewThucChay TongView,
		tc.TongClickThucChay TongClick,
		0 TongSoBaiViet,
		tc.TongClickThucChay AS SoLuongThucChay,
		@NgayThucHien NgayThucHien,
		0 GiaTriThayDoi,
		tc.TongClickThucChay * dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381) AS ThanhTienThucChayTruocChietKhau,
		0 GiaTriChietKhau,
		tc.TongClickThucChay * dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381)	AS ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		tc.TongClickThucChay * dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381) AS ThanhTienThucThu,
		0 as ThanhTienKM,
		0 as SoLuongThucChayKM,
		0 SoLuongLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
 0 SoLuongKMThayDoi,
 0 GiaTriKMThayDoi,
 '' GhiChu
	FROM ThucChay AS tc
	WHERE tc.NgayThucHien = @NgayThucHien 
	AND (tc.SoHopDong = '' OR tc.SohopDong IS NULL)	
	AND tc.DmSanPhamREF = 381
	AND tc.TongClickThucChay > 0 --sponsor chi co don vi tinh la CLICK
END


```
