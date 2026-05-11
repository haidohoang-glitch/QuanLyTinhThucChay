# Stored Procedure: `ThucChay_Insert_GTTD_XuLyLechTreoHa_ThucChayDaTinh_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-27 10:46:26.607000
- **Ngày sửa cuối**: 2018-08-03 15:02:36.307000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@ThanhTienHDCT` | `bigint(8)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
/*
ExEc [dbo].[ThucChay_Insert_GTTD_XuLyLechTreoHa_ThucChayDaTinh_Admatic] 
'2017-06-24',
	502186, 
	505297,
	342,
	117000000

*/
CREATE  PROCEDURE [dbo].[ThucChay_Insert_GTTD_XuLyLechTreoHa_ThucChayDaTinh_Admatic] 
	@NgayThucHien DATETIME,
	@HopDongID INT, 
	@HopDongChiTietID INT,
	@DmSanPhamREF INT,
	@ThanhTienHDCT BIGINT,
	@GhiChu NVARCHAR(500)

AS
BEGIN
	DECLARE @ThanhTienTCDT BIGINT, @ThucChayDaTinhID NVARCHAR(200)
	DECLARE @ThanhTienThucChayXuLy BIGINT, @DonGiaDonViTinh FLOAT, @ChietKhau FLOAT, @ThanhTienThucChay1DVT FLOAT

	--XAC DINH NGAY PHAT SINH GIA TRI LECH TREO HA
	SELECT TOP (1) @DonGiaDonViTinh = DonGiaTheoDonVi,  @ChietKhau = ChietKhau, @ThucChayDaTinhID = ThucChayDaTinhID FROM dbo.ThucChayDaTinh
	WHERE HopDongChiTietREF = @HopDongChiTietID
	AND HopDongID = @HopDongID
	AND NgayThucHien = @NgayThucHien
	AND DmSanPhamREF = @DmSanPhamREF
	AND SoLuongThucChayLechTreoHa <> 0
	ORDER BY CreatedAt ASC

	--XAC DINH NGAY GIA TRI THUC CHAY XU LY
	SET @ThanhTienTCDT = (
		SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietID
		AND HopDongID = @HopDongID
		AND NgayThucHien <= @NgayThucHien
	)

	--XAC DINH GIA TRI TREN 1 DONVI SOLUONG THUC CHAY
	SET @ThanhTienThucChay1DVT = (@DonGiaDonViTinh*(100-@ChietKhau))/100

	SET @ThanhTienThucChayXuLy = @ThanhTienHDCT - @ThanhTienTCDT
	--CHECK VOI TRUONG HOP XU LY LECH TREO HA (KHONG PHAI LA TH THAY DOI THANHTIEN HOPDONGCHITIET)
	IF(@ThanhTienThucChayXuLy <> 0 AND @ThanhTienThucChayXuLy <= @ThanhTienThucChay1DVT)
	BEGIN

		IF(@ThanhTienThucChayXuLy <> 0)
		BEGIN
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
				  0 TongViewThucChay ,
				  0 TongClickThucChay ,
				  0 TongSoBaiViet ,
				  0 SoLuongThucChay ,
				  @NgayThucHien NgayThucHien ,
				  @ThanhTienThucChayXuLy GiaTriThayDoi ,
				  0 ThanhTienThucChayTruocTrietKhau ,
				  0 GiaTriTrietKhauThucChay ,
				  0 ThanhTienSauTrietKhauThucChay ,
				  0 GiaTriHoaHongThucChay ,
				  0 ThanhTienThucThu ,
				  0 ThanhTienKM ,
				  0 SoLuongThucChayKM ,
				  0 SoLuongThucChayLechTreoHa ,
				  0 ThanhTienLechTreoHa ,
				  GETDATE() CreatedAt ,
				  GETDATE() LastModifiedAt ,
				  0 IsPheDuyet ,
				  '' PheDuyetBy ,
				  PheDuyetAt ,
				  0 SoLuongThayDoi ,
				  0 SoLuongKMThayDoi ,
				  0 GiaTriKMThayDoi ,
				  @GhiChu GhiChu
				FROM dbo.ThucChayDaTinh tcdt
				WHERE tcdt.ThucChayDaTinhID = @ThucChayDaTinhID
				AND tcdt.HopDongID = @HopDongID
				AND tcdt.HopDongChiTietREF = @HopDongChiTietID
		END
	END

	
	
			
END



```
