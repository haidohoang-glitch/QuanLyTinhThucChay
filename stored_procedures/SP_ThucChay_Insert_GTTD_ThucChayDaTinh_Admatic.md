# Stored Procedure: `ThucChay_Insert_GTTD_ThucChayDaTinh_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-12 15:57:25.230000
- **Ngày sửa cuối**: 2017-01-12 15:58:00.523000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@ThucChayDaTinhID` | `nvarchar(1000)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |

## Definition (Source Code)

```sql

CREATE  PROCEDURE [dbo].[ThucChay_Insert_GTTD_ThucChayDaTinh_Admatic] 
	@NgayThucHien DATETIME,
	@HopDongID INT, 
	@HopDongChiTietID INT,
	@DmSanPhamREF INT, 
	@ThucChayDaTinhID NVARCHAR(500),
	@GiaTriThayDoi FLOAT
AS
BEGIN
	--INSERT INTO dbo.ThucChayDaTinh 
	
	SELECT ThucChayDaTinhID ,
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
	        FROM dbo.ThucChayDaTinh
			WHERE ThucChayDaTinhID = @ThucChayDaTinhID
			AND HopDongID = @HopDongID
			AND HopDongChiTietREF = @HopDongChiTietID
			AND DmSanPhamREF = @DmSanPhamREF
			AND NgayThucHien <= @NgayThucHien
END



```
