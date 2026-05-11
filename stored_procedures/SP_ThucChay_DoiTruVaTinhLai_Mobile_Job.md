# Stored Procedure: `ThucChay_DoiTruVaTinhLai_Mobile_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-25 10:03:20.530000
- **Ngày sửa cuối**: 2018-05-30 17:12:43.173000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@NgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
/*
 EXEC [dbo].[ThucChay_DoiTruVaTinhLai_Mobile_Job] '2017-12-30','2018-05-28', 'QC1121217', '2018-05-29'
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_Mobile_Job]
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME 
  , @EndDate DATETIME 
  , @pSoHopDong NVARCHAR(50)
  , @NgayTinh DATETIME
AS
    BEGIN
	
	
        EXEC sp_TC_ExcInsertThucChayDaTinh_Mobile_DoiTruVaTinhLai @StartDate, @EndDate, @pSoHopDong, @NgayTinh

        INSERT  INTO dbo.ThucChayDaTinh
                ( ThucChayDaTinhID
                , HopDongID
                , SoHopDong
                , DmMaHopDongREF
                , TenMaHopDong
                , NgayDanhSoHopDong
                , NgayKyHopDong
                , NhanHopDong
                , NgayNhanBanFax
                , NgayNhanHopDongBanCung
                , NgayChuyenHopDongChoKeToan
                , So
                , Thang
                , Nam
                , GiaTriHopDong
                , CongNo
                , HopDongChiTietREF
                , DangSuDung
                , IsGiayPhep
                , TrangThaiHopDong
                , IsBanCung
                , DmPhongBanREF
                , TenPhongBan
                , DmBoPhanREF
                , TenBoPhan
                , DmNhomLamViecREF
                , TenNhomLamViec
                , DmDiaDiemLamViecREF
                , TenDiaDiemLamViec
                , SysNhanVienREF
                , TenDangNhap
                , TenNhanVien
                , TenKhachHang
                , NhanHang
                , DmNhomNganhREF
                , TenNhomNganh
                , DmHinhThucQuangCao
                , TenHinhThucQuangCao
                , DmSanPhamREF
                , TenSanPham
                , DmNhomWebsiteREF
                , TenNhomWebsite
                , DmChuyenMucREF
                , TenChuyenMuc
                , DmLoaiBannerREF
                , TenLoaiBanner
                , DmViTriREF
                , TenViTri
                , DotChayHopDong
                , SoLuongDotChayHD
                , DotChayBooking
                , SoLuongDotChayBooking
                , SoLuong
                , DonViTinh
                , DonGia
                , DonGiaTheoDonVi
                , ChietKhau
                , GiamGia
                , ThanhTien
                , TiLeTuVan
                , ChiPhiTuVan
                , IsKhuyenMai
                , KhuyenMai
                , DmBannerREF
                , DmChienDichREF
                , DmWebsiteREF
                , TenWebsite
                , TongViewThucChay
                , TongClickThucChay
                , TongSoBaiViet
                , SoLuongThucChay
                , NgayThucHien
                , GiaTriThayDoi
                , ThanhTienThucChayTruocTrietKhau
                , GiaTriTrietKhauThucChay
                , ThanhTienSauTrietKhauThucChay
                , GiaTriHoaHongThucChay
                , ThanhTienThucThu
                , ThanhTienKM
                , SoLuongThucChayKM
                , SoLuongThucChayLechTreoHa
                , ThanhTienLechTreoHa
                , CreatedAt
                , LastModifiedAt
                , IsPheDuyet
                , PheDuyetBy
                , PheDuyetAt
                , SoLuongThayDoi
                , SoLuongKMThayDoi
                , GiaTriKMThayDoi
                , GhiChu
	            )
                SELECT NEWID() ThucChayDaTinhID
                      , HopDongID
                      , SoHopDong
                      , DmMaHopDongREF
                      , TenMaHopDong
                      , NgayDanhSoHopDong
                      , NgayKyHopDong
                      , NhanHopDong
                      , NgayNhanBanFax
                      , NgayNhanHopDongBanCung
                      , NgayChuyenHopDongChoKeToan
                      , So
                      , Thang
                      , Nam
                      , GiaTriHopDong
                      , CongNo
                      , HopDongChiTietREF
                      , DangSuDung
                      , IsGiayPhep
                      , TrangThaiHopDong
                      , IsBanCung
                      , DmPhongBanREF
                      , TenPhongBan
                      , DmBoPhanREF
                      , TenBoPhan
                      , DmNhomLamViecREF
                      , TenNhomLamViec
                      , DmDiaDiemLamViecREF
                      , TenDiaDiemLamViec
                      , SysNhanVienREF
                      , TenDangNhap
                      , TenNhanVien
                      , TenKhachHang
                      , NhanHang
                      , DmNhomNganhREF
                      , TenNhomNganh
                      , DmHinhThucQuangCao
                      , TenHinhThucQuangCao
                      , DmSanPhamREF
                      , TenSanPham
                      , DmNhomWebsiteREF
                      , TenNhomWebsite
                      , DmChuyenMucREF
                      , TenChuyenMuc
                      , DmLoaiBannerREF
                      , TenLoaiBanner
                      , DmViTriREF
                      , TenViTri
                      , DotChayHopDong
                      , SoLuongDotChayHD
                      , DotChayBooking
                      , SoLuongDotChayBooking
                      , SoLuong
                      , DonViTinh
                      , DonGia
                      , DonGiaTheoDonVi
                      , ChietKhau
                      , GiamGia
                      , ThanhTien
                      , TiLeTuVan
                      , ChiPhiTuVan
                      , IsKhuyenMai
                      , KhuyenMai
                      , DmBannerREF
                      , DmChienDichREF
                      , DmWebsiteREF
                      , TenWebsite
                      , TongViewThucChay
                      , TongClickThucChay
                      , TongSoBaiViet
                      , SoLuongThucChay
                      , @NgayTinh
                      , GiaTriThayDoi
                      , ThanhTienThucChayTruocTrietKhau
                      , GiaTriTrietKhauThucChay
                      , ThanhTienSauTrietKhauThucChay
                      , GiaTriHoaHongThucChay
                      , ThanhTienThucThu
                      , ThanhTienKM
                      , SoLuongThucChayKM
                      , SoLuongThucChayLechTreoHa
                      , ThanhTienLechTreoHa
                      , CreatedAt
                      , LastModifiedAt
                      , IsPheDuyet
                      , PheDuyetBy
                      , PheDuyetAt
                      , SoLuongThayDoi
                      , SoLuongKMThayDoi
                      , GiaTriKMThayDoi
                      , GhiChu
                FROM    dbo.ThucChayDaTinh_DoiTruVaTinhLai_Mobile
				WHERE SoHopDong = @pSoHopDong

    END


```
