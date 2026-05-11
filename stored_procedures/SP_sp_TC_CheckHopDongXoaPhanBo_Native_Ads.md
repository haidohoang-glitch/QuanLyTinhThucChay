# Stored Procedure: `sp_TC_CheckHopDongXoaPhanBo_Native_Ads`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-09-26 15:21:10.447000
- **Ngày sửa cuối**: 2019-11-25 14:30:27.687000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@NgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


/*
EXEC [sp_TC_CheckHopDongXoaPhanBo_Native_Ads] '2018-06-13','2018-08-20','QC5620518',527807,'2018-08-29'
*/

CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongXoaPhanBo_Native_Ads]
   @pSoHopDong NVARCHAR(50)
  , @pHopDongChiTietID INT
  , @NgayTinh DATETIME
AS
    BEGIN
		IF((EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet
		WHERE HopDongChiTietID = @pHopDongChiTietID AND DeletedStatus = 1 
		AND DmSanPhamREF IN (821, 5133)
		AND NOT ( DmLoaiBannerREF IN (17,18)OR DmLoaiBannerREF IN (13,42))
		AND DonViTinhREF <> 3)))
				INSERT  INTO dbo.ThucChayDaTinh
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
                        , 0 TongViewThucChay
                        , 0 TongClickThucChay
                        , 0 TongSoBaiViet
                        , 0 AS SoLuongThucChay
                        , @NgayTinh
                        , -(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi
                        , 0 AS ThanhTienThucChayTruocTrietKhau
                        , 0 AS GiaTriTrietKhauThucChay
                        , 0 AS ThanhTienSauTrietKhauThucChay
                        , 0 AS GiaTriHoaHongThucChay
                        , -(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhTienThucThu
                        , 0 AS ThanhTienKM
                        , 0 AS SoLuongThucChayKM
                        , -SoLuongThucChayLechTreoHa
                        , -ThanhTienLechTreoHa
                        , GETDATE()
                        , GETDATE()
                        , IsPheDuyet
                        , PheDuyetBy
                        , PheDuyetAt
                        , -(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi
                        , -(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi
                        , -(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi
                        , N'Hop dong chi tiet bi huy' GhiChu
                FROM    dbo.ThucChayDaTinh
                WHERE   1=1
                        AND SoHopDong = @pSoHopDong
                        AND HopDongChiTietREF = @pHopDongChiTietID


    END




```
