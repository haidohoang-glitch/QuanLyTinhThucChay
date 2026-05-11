# Stored Procedure: `ThucChay_Update_ThucChayCPM_With_DonViTinh_Ngay_FixBug_KetThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-02-24 10:34:39.870000
- **Ngày sửa cuối**: 2018-09-21 17:46:09.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@ThanhTienHDCT` | `bigint(8)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_Update_ThucChayCPM_With_DonViTinh_Ngay_FixBug_KetThucChay]
   '2018-09-20' ,
 1003722 , 
 528581 ,
 245699999
*/
CREATE  PROCEDURE [dbo].[ThucChay_Update_ThucChayCPM_With_DonViTinh_Ngay_FixBug_KetThucChay]
   @NgayThucHien DATETIME,
	@HopDongID INT, 
	@HopDongChiTietID INT,
	@ThanhTienHDCT BIGINT
AS
  BEGIN
	DECLARE @Note NVARCHAR(500) = N'THUCCHAYCPM_WITH_DONVITINH_NGAY_GTTD xử lý giá trị lệch treo hạ'
	DECLARE @MinNgayThucHienLechTreoHa DATETIME, @ThanhTienTCDT BIGINT, @ThucChayDaTinhID NVARCHAR(200) = ''
	DECLARE @ThanhTienThucChayXuLy BIGINT, @ThanhTienHDCTBf BIGINT, @DonGia FLOAT = 0

	--XAC DINH NGAY PHAT SINH GIA TRI LECH TREO HA
	SELECT TOP (1) @MinNgayThucHienLechTreoHa = NgayThucHien
	, @ThucChayDaTinhID = ThucChayDaTinhID 
	FROM dbo.ThucChayDaTinh
	WHERE HopDongChiTietREF = @HopDongChiTietID
	AND HopDongID = @HopDongID
	AND SoLuongThucChayLechTreoHa <> 0
	ORDER BY CreatedAt ASC

	SELECT TOP (1) @ThanhTienHDCTBf = ThanhTien FROM dbo.ThucChayDaTinh
	WHERE HopDongChiTietREF = @HopDongChiTietID
	AND HopDongID = @HopDongID
	AND NgayThucHien < @NgayThucHien
	ORDER BY CreatedAt ASC

	--TH KHONG CO LECH TREO HA NHUNG HET NGAY CHAY VA TIEN THIEU < DONGIA
	IF(@MinNgayThucHienLechTreoHa IS NULL)
	BEGIN
	    IF(EXISTS(SELECT MAX(ISNULL(ThoiGianKetThuc,'1900-01-01')) FROM dbo.ThucChayHopDongChiTiet
		WHERE HopDongChiTietREF = @HopDongChiTietID
		AND HopDongREF = @HopDongID
		GROUP BY HopDongChiTietREF HAVING MAX(ISNULL(ThoiGianKetThuc,'1900-01-01')) <= @NgayThucHien))
		BEGIN
			 --XAC DINH NGAY GIA TRI THUC CHAY XU LY
			SET @ThanhTienTCDT = (
				SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh
				WHERE HopDongChiTietREF = @HopDongChiTietID
				AND HopDongID = @HopDongID
			)
			SET @ThanhTienThucChayXuLy = @ThanhTienHDCT - @ThanhTienTCDT
			SET @DonGia = ISNULL((SELECT TOP (1) DonGia 
									FROM dbo.HopDongChiTiet
									WHERE HopDongChiTietID = @HopDongChiTietID 
									ORDER BY HopDongChiTietID),0)
			IF (@ThanhTienThucChayXuLy <> 0 AND @ThanhTienThucChayXuLy < @DonGia)
			BEGIN
			    	SELECT TOP (1) @MinNgayThucHienLechTreoHa = NgayThucHien
					, @ThucChayDaTinhID = ThucChayDaTinhID 
					FROM dbo.ThucChayDaTinh
					WHERE HopDongChiTietREF = @HopDongChiTietID
					AND HopDongID = @HopDongID
					ORDER BY NgayThucHien DESC, CreatedAt DESC
			END
		END
	END
	ELSE
	BEGIN
	     --XAC DINH NGAY GIA TRI THUC CHAY XU LY
		SET @ThanhTienTCDT = (
			SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF = @HopDongChiTietID
			AND HopDongID = @HopDongID
		)

		SET @ThanhTienThucChayXuLy = @ThanhTienHDCT - @ThanhTienTCDT
	END
	--CHECK VOI TRUONG HOP XU LY LECH TREO HA (KHONG PHAI LA TH THAY DOI THANHTIEN HOPDONGCHITIET)
	IF(@ThanhTienHDCTBf IS NULL OR @ThanhTienHDCTBf = @ThanhTienHDCT)
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
				  @Note GhiChu
				FROM dbo.ThucChayDaTinh tcdt
				WHERE tcdt.ThucChayDaTinhID = @ThucChayDaTinhID
				AND tcdt.HopDongID = @HopDongID
				AND tcdt.HopDongChiTietREF = @HopDongChiTietID
		END
	END

	
	
			
END
```
