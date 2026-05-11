# Stored Procedure: `sp_InsertThucChayDaTinh_ByThucChayDaTinhID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-16 17:19:51.983000
- **Ngày sửa cuối**: 2021-03-16 17:19:51.983000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayDaTinhID` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create PROCEDURE sp_InsertThucChayDaTinh_ByThucChayDaTinhID
	-- Add the parameters for the stored procedure here
	@ThucChayDaTinhID nvarchar(50),
	@NgayThucHien datetime,
	@HopDongChiTietREF int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
insert into dbo.ThucChayDaTinh
(
[ThucChayDaTinhID]
      ,[HopDongID]
      ,[SoHopDong]
      ,[DmMaHopDongREF]
      ,[TenMaHopDong]
      ,[NgayDanhSoHopDong]
      ,[NgayKyHopDong]
      ,[NhanHopDong]
      ,[NgayNhanBanFax]
      ,[NgayNhanHopDongBanCung]
      ,[NgayChuyenHopDongChoKeToan]
      ,[So]
      ,[Thang]
      ,[Nam]
      ,[GiaTriHopDong]
      ,[CongNo]
      ,[HopDongChiTietREF]
      ,[DangSuDung]
      ,[IsGiayPhep]
      ,[TrangThaiHopDong]
      ,[IsBanCung]
      ,[DmPhongBanREF]
      ,[TenPhongBan]
      ,[DmBoPhanREF]
      ,[TenBoPhan]
      ,[DmNhomLamViecREF]
      ,[TenNhomLamViec]
      ,[DmDiaDiemLamViecREF]
      ,[TenDiaDiemLamViec]
      ,[SysNhanVienREF]
      ,[TenDangNhap]
      ,[TenNhanVien]
      ,[TenKhachHang]
      ,[NhanHang]
      ,[DmNhomNganhREF]
      ,[TenNhomNganh]
      ,[DmHinhThucQuangCao]
      ,[TenHinhThucQuangCao]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmNhomWebsiteREF]
      ,[TenNhomWebsite]
      ,[DmChuyenMucREF]
      ,[TenChuyenMuc]
      ,[DmLoaiBannerREF]
      ,[TenLoaiBanner]
      ,[DmViTriREF]
      ,[TenViTri]
      ,[DotChayHopDong]
      ,[SoLuongDotChayHD]
      ,[DotChayBooking]
      ,[SoLuongDotChayBooking]
      ,[SoLuong]
      ,[DonViTinh]
      ,[DonGia]
      ,[DonGiaTheoDonVi]
      ,[ChietKhau]
      ,[GiamGia]
      ,[ThanhTien]
      ,[TiLeTuVan]
      ,[ChiPhiTuVan]
      ,[IsKhuyenMai]
      ,[KhuyenMai]
      ,[DmBannerREF]
      ,[DmChienDichREF]
      ,[DmWebsiteREF]
      ,[TenWebsite]
      ,[TongViewThucChay]
      ,[TongClickThucChay]
      ,[TongSoBaiViet]
      ,[SoLuongThucChay]
      ,[NgayThucHien]
      ,[GiaTriThayDoi]
      ,[ThanhTienThucChayTruocTrietKhau]
      ,[GiaTriTrietKhauThucChay]
      ,[ThanhTienSauTrietKhauThucChay]
      ,[GiaTriHoaHongThucChay]
      ,[ThanhTienThucThu]
      ,[ThanhTienKM]
      ,[SoLuongThucChayKM]
      ,[SoLuongThucChayLechTreoHa]
      ,[ThanhTienLechTreoHa]
      ,[CreatedAt]
      ,[LastModifiedAt]
      ,[IsPheDuyet]
      ,[PheDuyetBy]
      ,[PheDuyetAt]
      ,[SoLuongThayDoi]
      ,[SoLuongKMThayDoi]
      ,[GiaTriKMThayDoi]
      ,[GhiChu]
	  )
SELECT [ThucChayDaTinhID]
      ,[HopDongID]
      ,[SoHopDong]
      ,[DmMaHopDongREF]
      ,[TenMaHopDong]
      ,[NgayDanhSoHopDong]
      ,[NgayKyHopDong]
      ,[NhanHopDong]
      ,[NgayNhanBanFax]
      ,[NgayNhanHopDongBanCung]
      ,[NgayChuyenHopDongChoKeToan]
      ,[So]
      ,[Thang]
      ,[Nam]
      ,[GiaTriHopDong]
      ,[CongNo]
      ,[HopDongChiTietREF]
      ,[DangSuDung]
      ,[IsGiayPhep]
      ,[TrangThaiHopDong]
      ,[IsBanCung]
      ,[DmPhongBanREF]
      ,[TenPhongBan]
      ,[DmBoPhanREF]
      ,[TenBoPhan]
      ,[DmNhomLamViecREF]
      ,[TenNhomLamViec]
      ,[DmDiaDiemLamViecREF]
      ,[TenDiaDiemLamViec]
      ,[SysNhanVienREF]
      ,[TenDangNhap]
      ,[TenNhanVien]
      ,[TenKhachHang]
      ,[NhanHang]
      ,[DmNhomNganhREF]
      ,[TenNhomNganh]
      ,[DmHinhThucQuangCao]
      ,[TenHinhThucQuangCao]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmNhomWebsiteREF]
      ,[TenNhomWebsite]
      ,[DmChuyenMucREF]
      ,[TenChuyenMuc]
      ,[DmLoaiBannerREF]
      ,[TenLoaiBanner]
      ,[DmViTriREF]
      ,[TenViTri]
      ,[DotChayHopDong]
      ,[SoLuongDotChayHD]
      ,[DotChayBooking]
      ,[SoLuongDotChayBooking]
      ,[SoLuong]
      ,[DonViTinh]
      ,[DonGia]
      ,[DonGiaTheoDonVi]
      ,[ChietKhau]
      ,[GiamGia]
      ,[ThanhTien]
      ,[TiLeTuVan]
      ,[ChiPhiTuVan]
      ,[IsKhuyenMai]
      ,[KhuyenMai]
      ,[DmBannerREF]
      ,[DmChienDichREF]
      ,[DmWebsiteREF]
      ,[TenWebsite]
      ,[TongViewThucChay]
      ,[TongClickThucChay]
      ,[TongSoBaiViet]
      ,[SoLuongThucChay]
      ,[NgayThucHien]
      ,[GiaTriThayDoi]
      ,[ThanhTienThucChayTruocTrietKhau]
      ,[GiaTriTrietKhauThucChay]
      ,[ThanhTienSauTrietKhauThucChay]
      ,[GiaTriHoaHongThucChay]
      ,[ThanhTienThucThu]
      ,[ThanhTienKM]
      ,[SoLuongThucChayKM]
      ,[SoLuongThucChayLechTreoHa]
      ,[ThanhTienLechTreoHa]
      ,[CreatedAt]
      ,[LastModifiedAt]
      ,[IsPheDuyet]
      ,[PheDuyetBy]
      ,[PheDuyetAt]
      ,[SoLuongThayDoi]
      ,[SoLuongKMThayDoi]
      ,[GiaTriKMThayDoi]
      ,[GhiChu]
	 
 FROM	ThucChayDaTinhAdmarket where 1=1 
 and ThucChayDaTinhID = @ThucChayDaTinhID
 and NgayThucHien = @NgayThucHien 
 and HopDongChiTietREF = @HopDongChiTietREF
 and DmSanPhamREF in (585,628,144)
 END

```
