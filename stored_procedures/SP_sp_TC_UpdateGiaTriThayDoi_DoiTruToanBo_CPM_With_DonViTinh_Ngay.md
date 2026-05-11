# Stored Procedure: `sp_TC_UpdateGiaTriThayDoi_DoiTruToanBo_CPM_With_DonViTinh_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-03-01 11:45:45.730000
- **Ngày sửa cuối**: 2021-10-07 17:13:36.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
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
Exec [dbo].[sp_TC_UpdateGiaTriThayDoi_DoiTruToanBo_CPM_With_DonViTinh_Ngay]
   @HopDongID = 1036609
  , @HopDongChiTietID = 634186
  , @NgayTinh = '2021-10-06'
*/

CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoi_DoiTruToanBo_CPM_With_DonViTinh_Ngay]
   @HopDongID INT
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
            WHERE   CONVERT(DATE, NgayThucHien) <= @NgayTinh
                    AND DmSanPhamREF IN ( 231, 238, 339, 240, 598, 613, 370, 680, 735 )
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
