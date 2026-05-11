# Stored Procedure: `ThucChay_Insert_GTTD_Tang_ThucChayDaTinh_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-09 17:09:39.047000
- **Ngày sửa cuối**: 2018-07-26 10:24:41.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayDaTinhID` | `nvarchar(1000)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GiaTriThucChayTang` | `float(8)` | No |
| `@SoLuongThucChayTang` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE  PROCEDURE [dbo].[ThucChay_Insert_GTTD_Tang_ThucChayDaTinh_Admatic] 
	@ThucChayDaTinhID NVARCHAR(500),
	@NgayThucHien DATETIME,
	@HopDongID INT, 
	@HopDongChiTietID INT,
	@DmSanPhamREF INT,
	@GiaTriThucChayTang FLOAT,
	@SoLuongThucChayTang INT
	
AS
BEGIN
	DECLARE @Note NVARCHAR(500) = N'ADMATIC_THANHTIEN_TD_GTTD tăng từ ThucChayDaTinhID =' + @ThucChayDaTinhID
	INSERT INTO dbo.ThucChayDaTinh
	        ( ThucChayDaTinhID ,
	          HopDongID ,
	          SoHopDong ,
	          DmMaHopDongREF ,
	          TenMaHopDong ,
	          NgayDanhSoHopDong ,
	          NgayKyHopDong ,
	          NhanHopDong ,
	          NgayNhanBanFax ,
	          NgayNhanHopDongBanCung ,
	          NgayChuyenHopDongChoKeToan ,
	          So ,
	          Thang ,
	          Nam ,
	          GiaTriHopDong ,
	          CongNo ,
	          HopDongChiTietREF ,
	          DangSuDung ,
	          IsGiayPhep ,
	          TrangThaiHopDong ,
	          IsBanCung ,
	          DmPhongBanREF ,
	          TenPhongBan ,
	          DmBoPhanREF ,
	          TenBoPhan ,
	          DmNhomLamViecREF ,
	          TenNhomLamViec ,
	          DmDiaDiemLamViecREF ,
	          TenDiaDiemLamViec ,
	          SysNhanVienREF ,
	          TenDangNhap ,
	          TenNhanVien ,
	          TenKhachHang ,
	          NhanHang ,
	          DmNhomNganhREF ,
	          TenNhomNganh ,
	          DmHinhThucQuangCao ,
	          TenHinhThucQuangCao ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          DmNhomWebsiteREF ,
	          TenNhomWebsite ,
	          DmChuyenMucREF ,
	          TenChuyenMuc ,
	          DmLoaiBannerREF ,
	          TenLoaiBanner ,
	          DmViTriREF ,
	          TenViTri ,
	          DotChayHopDong ,
	          SoLuongDotChayHD ,
	          DotChayBooking ,
	          SoLuongDotChayBooking ,
	          SoLuong ,
	          DonViTinh ,
	          DonGia ,
	          DonGiaTheoDonVi ,
	          ChietKhau ,
	          GiamGia ,
	          ThanhTien ,
	          TiLeTuVan ,
	          ChiPhiTuVan ,
	          IsKhuyenMai ,
	          KhuyenMai ,
	          DmBannerREF ,
	          DmChienDichREF ,
	          DmWebsiteREF ,
	          TenWebsite ,
	          TongViewThucChay ,
	          TongClickThucChay ,
	          TongSoBaiViet ,
	          SoLuongThucChay ,
	          NgayThucHien ,
	          GiaTriThayDoi ,
	          ThanhTienThucChayTruocTrietKhau ,
	          GiaTriTrietKhauThucChay ,
	          ThanhTienSauTrietKhauThucChay ,
	          GiaTriHoaHongThucChay ,
	          ThanhTienThucThu ,
	          ThanhTienKM ,
	          SoLuongThucChayKM ,
	          SoLuongThucChayLechTreoHa ,
	          ThanhTienLechTreoHa ,
	          CreatedAt ,
	          LastModifiedAt ,
	          IsPheDuyet ,
	          PheDuyetBy ,
	          PheDuyetAt ,
	          SoLuongThayDoi ,
	          SoLuongKMThayDoi ,
	          GiaTriKMThayDoi ,
	          GhiChu
	        )
	SELECT  NEWID() ThucChayDaTinhID ,
	          HopDongID ,
	          SoHopDong ,
	          DmMaHopDongREF ,
	          TenMaHopDong ,
	          NgayDanhSoHopDong ,
	          NgayKyHopDong ,
	          NhanHopDong ,
	          NgayNhanBanFax ,
	          NgayNhanHopDongBanCung ,
	          NgayChuyenHopDongChoKeToan ,
	          So ,
	          Thang ,
	          Nam ,
	          GiaTriHopDong ,
	          CongNo ,
	          HopDongChiTietREF ,
	          DangSuDung ,
	          IsGiayPhep ,
	          TrangThaiHopDong ,
	          IsBanCung ,
	          DmPhongBanREF ,
	          TenPhongBan ,
	          DmBoPhanREF ,
	          TenBoPhan ,
	          DmNhomLamViecREF ,
	          TenNhomLamViec ,
	          DmDiaDiemLamViecREF ,
	          TenDiaDiemLamViec ,
	          SysNhanVienREF ,
	          TenDangNhap ,
	          TenNhanVien ,
	          TenKhachHang ,
	          NhanHang ,
	          DmNhomNganhREF ,
	          TenNhomNganh ,
	          DmHinhThucQuangCao ,
	          TenHinhThucQuangCao ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          DmNhomWebsiteREF ,
	          TenNhomWebsite ,
	          DmChuyenMucREF ,
	          TenChuyenMuc ,
	          DmLoaiBannerREF ,
	          TenLoaiBanner ,
	          DmViTriREF ,
	          TenViTri ,
	          DotChayHopDong ,
	          SoLuongDotChayHD ,
	          DotChayBooking ,
	          SoLuongDotChayBooking ,
	          (SELECT TOP (1) SoLuong FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID) AS SoLuong ,
	          DonViTinh ,
	          DonGia ,
	          DonGiaTheoDonVi ,
	          (SELECT TOP (1) ChietKhau FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID) AS ChietKhau ,
	          GiamGia ,
	          (SELECT TOP (1) ThanhTien FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID) AS ThanhTien ,
	          TiLeTuVan ,
	          ChiPhiTuVan ,
	          IsKhuyenMai ,
	          KhuyenMai ,
	          DmBannerREF ,
	          DmChienDichREF ,
	          DmWebsiteREF ,
	          TenWebsite ,
	          0 TongViewThucChay ,
	          0 TongClickThucChay ,
	          0 TongSoBaiViet ,
	          0 SoLuongThucChay ,
	          @NgayThucHien NgayThucHien ,
	          @GiaTriThucChayTang GiaTriThayDoi ,
	          0 ThanhTienThucChayTruocTrietKhau ,
	          0 GiaTriTrietKhauThucChay ,
	          0 ThanhTienSauTrietKhauThucChay ,
	          0 GiaTriHoaHongThucChay ,
	          0 ThanhTienThucThu ,
	          0 ThanhTienKM ,
	          0 SoLuongThucChayKM ,
	          -tcdt.SoLuongThucChayLechTreoHa SoLuongThucChayLechTreoHa ,
	          -tcdt.ThanhTienLechTreoHa ThanhTienLechTreoHa ,
	          GETDATE() CreatedAt ,
	          GETDATE() LastModifiedAt ,
	          0 IsPheDuyet ,
	          '' PheDuyetBy ,
	          PheDuyetAt ,
	          @SoLuongThucChayTang SoLuongThayDoi ,
	          0 SoLuongKMThayDoi ,
	          0 GiaTriKMThayDoi ,
	          @Note GhiChu
	        FROM dbo.ThucChayDaTinh tcdt
			WHERE tcdt.ThucChayDaTinhID = @ThucChayDaTinhID
			AND tcdt.HopDongID = @HopDongID
			AND tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND tcdt.DmSanPhamREF = @DmSanPhamREF

	--NEU LA SAN PHAM ADX
	IF(@DmSanPhamREF = 585)
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
      
		SELECT  NEWID() ThucChayDaTinhID ,
	          HopDongID ,
	          SoHopDong ,
	          DmMaHopDongREF ,
	          TenMaHopDong ,
	          NgayDanhSoHopDong ,
	          NgayKyHopDong ,
	          NhanHopDong ,
	          NgayNhanBanFax ,
	          NgayNhanHopDongBanCung ,
	          NgayChuyenHopDongChoKeToan ,
	          So ,
	          Thang ,
	          Nam ,
	          GiaTriHopDong ,
	          CongNo ,
	          HopDongChiTietREF ,
	          DangSuDung ,
	          IsGiayPhep ,
	          TrangThaiHopDong ,
	          IsBanCung ,
	          DmPhongBanREF ,
	          TenPhongBan ,
	          DmBoPhanREF ,
	          TenBoPhan ,
	          DmNhomLamViecREF ,
	          TenNhomLamViec ,
	          DmDiaDiemLamViecREF ,
	          TenDiaDiemLamViec ,
	          SysNhanVienREF ,
	          TenDangNhap ,
	          TenNhanVien ,
	          TenKhachHang ,
	          NhanHang ,
	          DmNhomNganhREF ,
	          TenNhomNganh ,
	          DmHinhThucQuangCao ,
	          TenHinhThucQuangCao ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          DmNhomWebsiteREF ,
	          TenNhomWebsite ,
	          DmChuyenMucREF ,
	          TenChuyenMuc ,
	          DmLoaiBannerREF ,
	          TenLoaiBanner ,
	          DmViTriREF ,
	          TenViTri ,
	          DotChayHopDong ,
	          SoLuongDotChayHD ,
	          DotChayBooking ,
	          SoLuongDotChayBooking ,
	          (SELECT TOP (1) SoLuong FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID) AS SoLuong ,
	          DonViTinh ,
	          DonGia ,
	          DonGiaTheoDonVi ,
	          (SELECT TOP (1) ChietKhau FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID) AS ChietKhau ,
	          GiamGia ,
	          (SELECT TOP (1) ThanhTien FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID) AS ThanhTien ,
	          TiLeTuVan ,
	          ChiPhiTuVan ,
	          IsKhuyenMai ,
	          KhuyenMai ,
	          DmBannerREF ,
	          DmChienDichREF ,
	          DmWebsiteREF ,
	          TenWebsite ,
	          0 TongViewThucChay ,
	          0 TongClickThucChay ,
	          0 TongSoBaiViet ,
	          0 SoLuongThucChay ,
	          @NgayThucHien NgayThucHien ,
	          @GiaTriThucChayTang GiaTriThayDoi ,
	          0 ThanhTienThucChayTruocTrietKhau ,
	          0 GiaTriTrietKhauThucChay ,
	          0 ThanhTienSauTrietKhauThucChay ,
	          0 GiaTriHoaHongThucChay ,
	          0 ThanhTienThucThu ,
	          0 ThanhTienKM ,
	          0 SoLuongThucChayKM ,
	          -tcdt.SoLuongThucChayLechTreoHa SoLuongThucChayLechTreoHa ,
	          -tcdt.ThanhTienLechTreoHa ThanhTienLechTreoHa ,
	          GETDATE() CreatedAt ,
	          GETDATE() LastModifiedAt ,
	          0 IsPheDuyet ,
	          '' PheDuyetBy ,
	          PheDuyetAt ,
	          @SoLuongThucChayTang SoLuongThayDoi ,
	          0 SoLuongKMThayDoi ,
	          0 GiaTriKMThayDoi ,
	          @Note GhiChu
	        FROM dbo.ThucChayDaTinhAdmarket tcdt
			WHERE tcdt.ThucChayDaTinhID = @ThucChayDaTinhID
			AND tcdt.HopDongID = @HopDongID
			AND tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND tcdt.DmSanPhamREF = @DmSanPhamREF
	END
	
END



```
