# Stored Procedure: `ThucChay_Admatic_Adx_Insert_ThucChayDaTinhAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-10 17:07:30.663000
- **Ngày sửa cuối**: 2025-04-10 16:47:59.837000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[ThucChay_InsertThucChayDaTinhAdmarket_Adx_ThanhTien_Admatic] 
	@NgayThucHien = '2020-07-29',
	@DotChayHopDong = N'ThanhTien_Admatic'
*/


CREATE PROCEDURE [dbo].[ThucChay_Admatic_Adx_Insert_ThucChayDaTinhAdmarket] 
	@NgayThucHien DATE,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN

	DELETE tcdt
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinhAdmarket tcdt 
	WHERE tcdt.NgayThucHien = @NgayThucHien
	AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
	AND tcdt.DmHinhThucQuangCao = 42
	AND tcdt.DmSanPhamREF = 585 --Adx
	AND tcdt.DotChayHopDong IN (N'ThanhTien_Admatic', 
											N'Tính mới Admatic', N'Tính thay đổi Admatic', N'Đối trừ Admatic',N'Tính lại Admatic',
											N'Tính mới Admatic donvibai', N'Tính thay đổi Admatic donvibai', N'Đối trừ Admatic donvibai')
								 
	AND (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong)
	AND (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID)

	INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinhAdmarket
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
	SELECT ThucChayDaTinhID,
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
		FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
		WHERE	cast(tcdt.NgayThucHien as date) = @NgayThucHien
				AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
				AND tcdt.DmHinhThucQuangCao = 42
				AND tcdt.DmSanPhamREF = 585 --Adx
				AND tcdt.DotChayHopDong IN (N'ThanhTien_Admatic', 
											N'Tính mới Admatic', N'Tính thay đổi Admatic', N'Đối trừ Admatic',N'Tính lại Admatic',
											N'Tính mới Admatic donvibai', N'Tính thay đổi Admatic donvibai', N'Đối trừ Admatic donvibai')

				AND (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong)
				AND (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID)

END


```
