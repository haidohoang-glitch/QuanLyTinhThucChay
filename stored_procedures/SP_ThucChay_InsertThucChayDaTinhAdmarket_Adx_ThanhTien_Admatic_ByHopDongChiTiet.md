# Stored Procedure: `ThucChay_InsertThucChayDaTinhAdmarket_Adx_ThanhTien_Admatic_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-10-23 15:35:29.433000
- **Ngày sửa cuối**: 2024-10-23 15:44:00.050000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
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
    @SoHopDong NVARCHAR(50),    
    @HopDongChiTietREF INT,     
    @DmSanPhamREF INT,      
  	@NgayThucHien DATETIME,
	@DotChayHopDong NVARCHAR(100)
*/


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinhAdmarket_Adx_ThanhTien_Admatic_ByHopDongChiTiet] 
	@SoHopDong NVARCHAR(50),    
    @HopDongChiTietREF INT,     
    @DmSanPhamREF INT,      
  	@NgayThucHien DATETIME,
	@DotChayHopDong NVARCHAR(100)
AS
BEGIN
	--PRINT 'Insert thuc chay ThanhTien_Admatic'
	DECLARE @NgayDanhSoGioiHan DATETIME = DATEADD(yyyy,-3,GETDATE())
	SET @DotChayHopDong = N'ThanhTien_Admatic'

	IF(EXISTS(SELECT TOP (1) tcdt.HopDongChiTietREF FROM dbo.ThucChayDaTinh tcdt 
	WHERE tcdt.HopDongChiTietREF = @HopDongChiTietREF
	AND tcdt.NgayThucHien = @NgayThucHien
	AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
	AND tcdt.DmHinhThucQuangCao = 42
	and tcdt.DmSanPhamREF = @DmSanPhamREF --Adx
	AND tcdt.NgayDanhSoHopDong >= @NgayDanhSoGioiHan 
	AND tcdt.DotChayHopDong = @DotChayHopDong
	ORDER BY HopDongChiTietREF))
	BEGIN
		--NEU DA TON TAI TRONG dbo.ThucChayDaTinhAdmarket THI THOI
		--PRINT 'VAO CHECK'
		IF(EXISTS(SELECT TOP (1) HopDongChiTietREF FROM dbo.ThucChayDaTinhAdmarket tcdt 
			WHERE tcdt.HopDongChiTietREF = @HopDongChiTietREF
			AND tcdt.NgayThucHien = @NgayThucHien
			AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
			AND tcdt.DmHinhThucQuangCao = 42
			and tcdt.DmSanPhamREF = @DmSanPhamREF --Adx
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
				WHERE tcdt.HopDongChiTietREF = @HopDongChiTietREF
				AND tcdt.DmSanPhamREF = @DmSanPhamREF --Adx
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
