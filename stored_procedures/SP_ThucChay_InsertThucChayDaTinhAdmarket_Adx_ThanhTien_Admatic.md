# Stored Procedure: `ThucChay_InsertThucChayDaTinhAdmarket_Adx_ThanhTien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-07-14 09:55:27.680000
- **Ngày sửa cuối**: 2020-07-30 14:48:47.267000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DotChayHopDong` | `nvarchar(200)` | No |

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


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinhAdmarket_Adx_ThanhTien_Admatic] 
	@NgayThucHien DATETIME,
	@DotChayHopDong Nvarchar(100)
AS
BEGIN
	--PRINT 'Insert thuc chay ThanhTien_Admatic'
	DECLARE @NgayDanhSoGioiHan DATETIME = '2020-07-20'
	SET @DotChayHopDong = N'ThanhTien_Admatic'

	IF(EXISTS(SELECT TOP (1) tcdt.HopDongChiTietREF FROM dbo.ThucChayDaTinh tcdt 
	WHERE tcdt.NgayThucHien = @NgayThucHien
	AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
	AND tcdt.DmHinhThucQuangCao = 42
	and tcdt.DmSanPhamREF = 585 --Adx
	AND tcdt.NgayDanhSoHopDong >= @NgayDanhSoGioiHan 
	AND tcdt.DotChayHopDong = @DotChayHopDong
	ORDER BY HopDongChiTietREF))
	BEGIN
		--NEU DA TON TAI TRONG dbo.ThucChayDaTinhAdmarket THI THOI
		--PRINT 'VAO CHECK'
		IF(EXISTS(SELECT TOP (1) HopDongChiTietREF FROM dbo.ThucChayDaTinhAdmarket tcdt 
			WHERE tcdt.NgayThucHien = @NgayThucHien
			AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
			AND tcdt.DmHinhThucQuangCao = 42
			and tcdt.DmSanPhamREF = 585 --Adx
			AND tcdt.NgayDanhSoHopDong >= @NgayDanhSoGioiHan 
			AND tcdt.DotChayHopDong = @DotChayHopDong
			ORDER BY HopDongChiTietREF))
			BEGIN
				PRINT'Xac dinh xem gia tri ben 02 ben co bang nhau ko'
			END
		ELSE
		BEGIN
			BEGIN
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
				FROM ThucChayDaTinh tcdt
				WHERE tcdt.DmSanPhamREF = 585 --Adx
				AND tcdt.DmHinhThucQuangCao = 42
				AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
				and tcdt.NgayThucHien = @NgayThucHien
				AND tcdt.NgayDanhSoHopDong >= @NgayDanhSoGioiHan 
				AND tcdt.DotChayHopDong = @DotChayHopDong
			END

		END
	END
	--ELSE
	--	PRINT 'KO CO GI'
		
END


```
