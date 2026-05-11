# Stored Procedure: `sp_TC_InsertThucChayDaTinh_DoiTruGiam_CPM_HDHuy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-16 10:51:07.070000
- **Ngày sửa cuối**: 2017-06-23 17:58:06.930000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTiet` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@SoLuongThucChay` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_PR]


CREATE  PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_DoiTruGiam_CPM_HDHuy]
	@HopDongChiTiet INT,
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(50),
	@NgaythucHien DATETIME,
	@GiaTriThayDoi FLOAT,
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(100),
	@SoLuongThucChay INT
AS
BEGIN
	PRINT @HopDongChiTiet
	DECLARE @Note NVARCHAR(500) = N'HD_HUY đối trừ giảm'
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
	          -sum(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) GiaTriThayDoi ,
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
	          NULL PheDuyetAt ,
	          -SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) SoLuongThayDoi ,
	          0 SoLuongKMThayDoi ,
	          0 GiaTriKMThayDoi ,
	          @Note GhiChu
	        FROM dbo.ThucChayDaTinh tcdt
			WHERE 1=1
			AND tcdt.HopDongChiTietREF = @HopDongChiTiet
			AND tcdt.NgayThucHien < @NgayThucHien
			AND tcdt.DmWebsiteREF = @DmWebsiteREF
			AND tcdt.DmSanPhamREF = @DmSanPhamREF
			GROUP BY
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
	          TenWebsite 

END

```
