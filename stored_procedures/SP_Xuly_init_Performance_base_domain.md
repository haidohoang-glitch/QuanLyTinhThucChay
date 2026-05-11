# Stored Procedure: `Xuly_init_Performance_base_domain`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-10 17:36:14.680000
- **Ngày sửa cuối**: 2017-01-10 17:44:08.383000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThanhTien` | `int(4)` | No |
| `@DmSanPHamREF` | `int(4)` | No |
| `@TenSanpham` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Xuly_init_Performance_base_domain] 
	@NgayThucHien DATETIME , 
	@ThanhTien INT ,
	@DmSanPHamREF INT, 
	@TenSanpham NVARCHAR(50)
*/
CREATE  PROCEDURE [dbo].[Xuly_init_Performance_base_domain] 
	@NgayThucHien DATETIME , 
	@ThanhTien INT ,
	@DmSanPHamREF INT, 
	@TenSanpham NVARCHAR(50)
AS
BEGIN
	

INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh
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
SELECT 
 NEWID() [ThucChayDaTinhID]
      ,0 [HopDongID]
      ,'-'[SoHopDong]
      ,0 [DmMaHopDongREF]
      ,'' [TenMaHopDong]
      ,'2013-07-17 02:05:51.000' [NgayDanhSoHopDong]
      ,'2013-07-17 02:05:51.000' [NgayKyHopDong]
      ,'' [NhanHopDong]
      ,'2013-07-17 02:05:51.000' [NgayNhanBanFax]
      ,'2013-07-17 02:05:51.000' [NgayNhanHopDongBanCung]
      ,'2013-07-17 02:05:51.000' [NgayChuyenHopDongChoKeToan]
      ,'' [So]
      ,0 [Thang]
      ,0 [Nam]
      ,0 [GiaTriHopDong]
      ,0 [CongNo]
      ,0 [HopDongChiTietREF]
      ,0 [DangSuDung]
      ,0 [IsGiayPhep]
      ,0 [TrangThaiHopDong]
      ,0 [IsBanCung]
      ,-1 [DmPhongBanREF]
      ,'-' [TenPhongBan]
      ,-1 [DmBoPhanREF]
      ,'-' [TenBoPhan]
      ,-1 [DmNhomLamViecREF]
      ,'-' [TenNhomLamViec]
      ,0 [DmDiaDiemLamViecREF]
      ,'' [TenDiaDiemLamViec]
      ,0 [SysNhanVienREF]
      ,'-' [TenDangNhap]
      ,'-' [TenNhanVien]
      ,'' [TenKhachHang]
      ,'0' [NhanHang]
      ,'0' [DmNhomNganhREF]
      ,'' [TenNhomNganh]
      ,7 [DmHinhThucQuangCao]
      ,'CPC' [TenHinhThucQuangCao]
      ,@DmSanPHamREF [DmSanPhamREF]
      ,@TenSanpham [TenSanPham]
      ,0 [DmNhomWebsiteREF]
      ,'' [TenNhomWebsite]
      ,0 [DmChuyenMucREF]
      ,'' [TenChuyenMuc]
      ,0 [DmLoaiBannerREF]
      ,'' [TenLoaiBanner]
      ,0 [DmViTriREF]
      ,'' [TenViTri]
      ,'' [DotChayHopDong]
      ,0 [SoLuongDotChayHD]
      ,'' [DotChayBooking]
      ,'' [SoLuongDotChayBooking]
      ,0 [SoLuong]
      ,'CPC' [DonViTinh]
      ,0 [DonGia]
      ,0 [DonGiaTheoDonVi]
      ,0 [ChietKhau]
      ,0 [GiamGia]
      ,0 [ThanhTien]
      ,0 [TiLeTuVan]
      ,0 [ChiPhiTuVan]
      ,0 [IsKhuyenMai]
      ,'' [KhuyenMai]
      ,0 [DmBannerREF]
      ,0 [DmChienDichREF]
      ,56 [DmWebsiteREF]
      ,'dantri.com.vn' [TenWebsite]
      ,0 [TongViewThucChay]
      ,0 [TongClickThucChay]
      ,0 [TongSoBaiViet]
      ,0 [SoLuongThucChay]
      ,@NgayThucHien [NgayThucHien]
      ,0 [GiaTriThayDoi]
      ,0 [ThanhTienThucChayTruocTrietKhau]
      ,0 [GiaTriTrietKhauThucChay]
      , (@ThanhTien/1.1) [ThanhTienSauTrietKhauThucChay]
      ,0 [GiaTriHoaHongThucChay]
      ,0 [ThanhTienThucThu]
      ,0 [ThanhTienKM]
      ,0 [SoLuongThucChayKM]
      ,0 [SoLuongThucChayLechTreoHa]
      ,0 [ThanhTienLechTreoHa]
      , GETDATE() [CreatedAt]
      , GETDATE() [LastModifiedAt]
      , 0 [IsPheDuyet]
      ,'' [PheDuyetBy]
      ,NULL [PheDuyetAt]
      ,0 [SoLuongThayDoi]
      ,0 [SoLuongKMThayDoi]
      ,0 [GiaTriKMThayDoi]
      ,'SYN VIEWPLUS ADMARKET' [GhiChu]

END

```
