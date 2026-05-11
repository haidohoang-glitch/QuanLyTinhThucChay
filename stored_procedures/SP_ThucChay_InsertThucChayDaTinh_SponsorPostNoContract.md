# Stored Procedure: `ThucChay_InsertThucChayDaTinh_SponsorPostNoContract`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-04 17:07:52.267000
- **Ngày sửa cuối**: 2015-03-02 11:09:20.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-04-25
-- Description:	Insert Thuc chay san pham SponsorPost khong co hop dong
-- =============================================
--
-- EXEC dbo.[ThucChay_InsertThucChayDaTinh_SponsorPostNoContract] '2014-11-20'
--
CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_SponsorPostNoContract] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- Xoa du lieu neu da ton tai
	DELETE FROM ThucChayDaTinhSponsorPost WHERE NgayThucHien = @NgayThucHien 
	AND DmSanPhamREF = 381 AND SoHopDong in ('-')
	AND DmHinhThucQuangCao <> 13
	-- Insert du lieu
	INSERT INTO ThucChayDaTinhSponsorPost
	SELECT 
		NEWID(),
		0 HopDongID,
		'-'SoHopDong,
		(CASE 
			WHEN tc.IsNoiBo = 1 AND tc.UserName <> 'sohagame' THEN 310-- NB
			WHEN tc.IsNoiBo = 1 AND tc.UserName = 'sohagame' THEN 533 -- SH
			WHEN tc.IsNoiBo = 2 THEN ''
		END	) DmMaHopDongREF,
		(CASE 
			WHEN tc.IsNoiBo = 1 AND tc.UserName <> 'sohagame' THEN 'NB'
			WHEN tc.IsNoiBo = 1 AND tc.UserName = 'sohagame' THEN 'SH'
			WHEN tc.IsNoiBo = 2 THEN 'ONLINE'		 
		END) TenMaHopDong,
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
		'Sponsored Post' TenSanPham,
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
		sum(tc.TongViewThucChay) TongView,
		sum(tc.TongClickThucChay) TongClick,
		0 TongSoBaiViet,
		sum(tc.TongClickThucChay) AS SoLuongThucChay,
		@NgayThucHien NgayThucHien,
		0 GiaTriThayDoi,		 
		sum(tc.TongClickThucChay) * dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381)AS ThanhTienThucChayTruocChietKhau,
		0 GiaTriChietKhau,
		sum(tc.TongClickThucChay) * dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381)AS ThanhTienSauTrietKhauThucChay,		
		0 AS GiaTriHoaHongThucChay,		
		sum(tc.TongClickThucChay) * dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381)AS ThanhTienThucThu,
		
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
	FROM ThucChay_SponsorPostTemp AS tc
	WHERE tc.NgayThucHien = @NgayThucHien 	
	AND ((tc.IsNoiBo = 1 and SoHopDong NOT IN (SELECT hd.SoHopDong
	                                                                           FROM HopDong hd))
		OR (tc.IsNoiBo = 2 AND SoHopDong = ''))	
	AND tc.ProductUnitName IN ('CPC')			
	AND tc.DmSanPhamREF = 381
	AND tc.TongClickThucChay > 0 --sponsor chi co don vi tinh la CLICK
	GROUP BY tc.IsNoiBo, 
		tc.UserName, tc.SaleName, tc.DmBannerREF,
		tc.DmChienDichREF,
		tc.DmWebsiteREF,
		tc.TenWebsite, tc.NgayThucHien
END

```
