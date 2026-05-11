# Stored Procedure: `sp_TC_UpdateGiaTriThayDoi_DoiTruToanBo_CPM_With_DonViTinh_Ngay_ByHopDongChiTietAndNgay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-06-29 10:23:30.373000
- **Ngày sửa cuối**: 2018-10-26 14:59:05.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


/*
EXEC [dbo].[sp_TC_UpdateGiaTriThayDoi_DoiTruToanBo_CPM_With_DonViTinh_Ngay_ByHopDongChiTietAndNgay]
	@FromDate DATETIME
  , @ToDate DATETIME
  , @HopDongID INT
  , @HopDongChiTietID INT
  , @NgayTinh DATETIME
*/

CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoi_DoiTruToanBo_CPM_With_DonViTinh_Ngay_ByHopDongChiTietAndNgay]
	@FromDate DATETIME
  , @ToDate DATETIME
  , @HopDongID INT
  , @HopDongChiTietID INT
  , @NgayTinh DATETIME
AS
    BEGIN

         INSERT  INTO dbo.ThucChayDaTinh
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
            SELECT  NEWID()
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
                    , 0 DonGiaTheoDonVi
                    , ChietKhau
                    , 0 GiamGia
                    , ThanhTien
                    , TiLeTuVan
                    , ChiPhiTuVan
                    , IsKhuyenMai
                    , KhuyenMai
                    , DmBannerREF
                    , DmChienDichREF
                    , DmWebsiteREF
                    , TenWebsite
                    , 0 TongViewThucChay
                    , 0 TongClickThucChay
                    , 0 TongSoBaiViet
                    , 0 SoLuongThucChay
                    , @NgayTinh
                    , -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) GiaTriThayDoi
                    , 0 ThanhTienThucChayTruocTrietKhau
                    , 0 GiaTriTrietKhauThucChay
                    , 0 ThanhTienSauTrietKhauThucChay
                    , 0 GiaTriHoaHongThucChay
                    , -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) ThanhTienThucThu
                    , 0 ThanhTienKM
                    , 0 SoLuongThucChayKM
                    , 0 SoLuongThucChayLechTreoHa
                    , 0 ThanhTienLechTreoHa
                    , GETDATE()
                    , GETDATE()
                    , 0 IsPheDuyet
                    , '' PheDuyetBy
                    , GETDATE() PheDuyetAt
                    , -SUM(SoLuongThucChay) SoLuongThayDoi
                    , -SUM(SoLuongThucChayKM)SoLuongKMThayDoi
                    , -SUM(ThanhTienKM)GiaTriKMThayDoi
                    , N'sp_TC_UpdateGiaTriThayDoi_DoiTruToanBo_CPM_With_DonViTinh_Ngay' GhiChu
            FROM    dbo.ThucChayDaTinh
            WHERE   CONVERT(DATE, NgayThucHien) BETWEEN @FromDate AND @ToDate
                    AND DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342)
                    AND DotChayHopDong = N'NGAY'
                    AND NOT (DmLoaiBannerREF IN ( 17, 18 ) OR DmHinhThucQuangCao IN ( 13, 42 ))
                    AND HopDongID = @HopDongID
                    AND HopDongChiTietREF = @HopDongChiTietID
			GROUP BY HopDongID
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
					, SoLuong
                    , DotChayHopDong
					, SoLuongDotChayHD
				    , DotChayBooking
                    , SoLuongDotChayBooking
					, DmBannerREF
                    , DmChienDichREF
                    , DmWebsiteREF
                    , TenWebsite
					, DonViTinh
					, DonGia
					 , ChietKhau
					 , ThanhTien
                    , TiLeTuVan
                    , ChiPhiTuVan
                    , IsKhuyenMai
                    , KhuyenMai
END



```
