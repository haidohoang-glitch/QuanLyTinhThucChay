# Stored Procedure: `sp_TC_CheckHopDongXoaPhanBo_ThanhTien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-06-24 16:24:15.937000
- **Ngày sửa cuối**: 2021-05-14 17:55:06.757000

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
EXEC [sp_TC_CheckHopDongXoaPhanBo_ThanhTien_Admatic] '2018-06-13','2018-08-20','QC5620518',527807,'2018-08-29'
*/

CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongXoaPhanBo_ThanhTien_Admatic]
   @pSoHopDong NVARCHAR(50)
  , @pHopDongChiTietID INT
  , @NgayTinh DATETIME
AS
    BEGIN
		IF((EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet
		WHERE HopDongChiTietID = @pHopDongChiTietID AND DeletedStatus = 1 
		AND DmLoaiREF = 42
		AND NOT ( DmLoaiBannerREF IN (17,18)OR DmLoaiBannerREF IN (13))
		AND NOT (DmLoaiREF = 42 AND DmLoaiNenTangREF = 9) --INVENTORY ADMATIC
		AND NOT DonViTinhREF IN (3,4))))

		INSERT INTO dbo.ThucChayDaTinh
           ([ThucChayDaTinhID]
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
           ,[GhiChu])
  
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
                    , '' AS DotChayHopDong
                    , 0 AS SoLuongDotChayHD
                    , '' AS DotChayBooking
                    , 0 AS SoLuongDotChayBooking
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
                    , -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi
                    , 0 AS ThanhTienThucChayTruocTrietKhau
                    , 0 AS GiaTriTrietKhauThucChay
                    , 0 AS ThanhTienSauTrietKhauThucChay
                    , 0 AS GiaTriHoaHongThucChay
                    , -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhTienThucThu
                    , 0 AS ThanhTienKM
                    , 0 AS SoLuongThucChayKM
                    , -SUM(SoLuongThucChayLechTreoHa)
                    , -SUM(ThanhTienLechTreoHa)
                    , GETDATE()
                    , GETDATE()
                    , 0 ASIsPheDuyet
                    , '' AS PheDuyetBy
                    , GETDATE() AS PheDuyetAt
                    , -SUM(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi
                    , -SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi
                    , -SUM(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi
                    , N'Hop dong chi tiet bi huy thanhtien_admatic' GhiChu
            FROM    dbo.ThucChayDaTinh
            WHERE   1=1
                    AND SoHopDong = @pSoHopDong
                    AND HopDongChiTietREF = @pHopDongChiTietID
			GROUP BY 
					 HopDongID
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

END




```
