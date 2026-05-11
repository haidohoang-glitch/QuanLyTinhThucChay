# Stored Procedure: `ThucChay_Insert_ThucChayDaTinh_Admatic_Adx`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-06-04 15:30:00.303000
- **Ngày sửa cuối**: 2018-07-03 12:43:30.487000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@pHopDongChiTiet` | `int(4)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@DmCampaign` | `int(4)` | No |
| `@GiaTriThucChay` | `float(8)` | No |
| `@GiaTriThucChayKM` | `float(8)` | No |
| `@GiaTriLechTreoHa` | `float(8)` | No |
| `@TongViewThucChay` | `bigint(8)` | No |
| `@TongClickThucChay` | `bigint(8)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(200)` | No |
| `@TenWebsite` | `nvarchar(1000)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@SoLuongThucChayKM` | `int(4)` | No |
| `@SoLuongLechTreoha` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(200)` | No |
| `@DonGiaTheoDVT` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


-- sp_TC_Insert_From_DataThucChay_Adx '2017-09-14', '2017-09-16', 'QC5120917', 513663

CREATE  PROCEDURE [dbo].[ThucChay_Insert_ThucChayDaTinh_Admatic_Adx]
    @NgayThucHien DATETIME
  , @HopDongID INT
  , @pHopDongChiTiet INT
  , @DmBannerREF INT
  , @DmCampaign INT
  , @GiaTriThucChay FLOAT
  , @GiaTriThucChayKM FLOAT
  , @GiaTriLechTreoHa FLOAT
  , @TongViewThucChay BIGINT
  , @TongClickThucChay BIGINT
  , @DmViTriREF INT
  , @TenViTri NVARCHAR(100)
  , @TenWebsite NVARCHAR(500)
  , @DmWebsiteREF INT
  , @SoLuongThucChay INT
  , @SoLuongThucChayKM INT
  , @SoLuongLechTreoha INT
  , @DonViTinh NVARCHAR(100)
  , @DonGiaTheoDVT FLOAT
AS
    BEGIN
		--INSERT THONG TIN THUC CHAY VAO THUCCHAYDATINH
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
                SELECT  NEWID()
                      , HD.HopDongID
                      , HD.SoHopDong
                      , HD.DmMaHopDongREF
                      , HD.TenMaHopDong
                      , HD.NgayDanhSoHopDong
                      , HD.NgayKyHopDong
					  , HD.NhanHopDong
                      , HD.NgayNhanBanFax
                      , HD.NgayNhanHopDongBanCung
                      , HD.NgayChuyenHopDongChoKeToan
                      , HD.So
                      , HD.Thang
                      , HD.Nam
                      , HD.GiaTriHopDong
                      , HD.CongNo
                      , HDCT.HopDongChiTietID HopDongChiTietREF
                      , HD.DangSuDung
                      , HD.IsGiayPhep
                      , HD.TrangThaiHopDong
                      , HD.IsBanCung
                      , HD.DmPhongBanREF
                      , ISNULL(HD.TenPhongBan,'') AS TenPhongBan
                      , HD.DmBoPhanREF
                      , ISNULL(HD.TenBoPhan,'') AS TenBoPhan
                      , HD.DmNhomLamViecREF
                      , ISNULL(HD.TenNhom, '') AS TenNhom
                      , HD.DmDiaDiemLamViecREF
                      , ISNULL(HD.TenDiaDiemLamViec,'')TenDiaDiemLamViec
                      , HD.SysNhanVienREF
                      , HD.TenDangNhap
                      , ISNULL(HD.TenNhanVien,'') AS TenNhanVien
                      , HD.TenKhachHang
                      , HDCT.DanhSachNhanHangREF
                      , HDCT.DmNhomNganhREF
                      , HDCT.TenNhomNganh
                      , HDCT.DmLoaiREF
                      , HDCT.TenLoai
                      , 585 AS DmSanPhamREF --SAN PHAM ADX
                      , N'AdX' AS TenSanPham
                      , HDCT.DmNhomWebsiteREF
                      , HDCT.TenNhomWebsite
                      , HDCT.DmChuyenMucREF
                      , HDCT.TenChuyenMuc
                      , HDCT.DmLoaiBannerREF
                      , HDCT.TenLoaiBanner
                      , @DmViTriREF AS DmViTriREF
                      , @TenViTri TenViTri
                      , '' DotChayHopDong
                      , 0 SoLuongDotChayHD
                      , '' DotChayBooking
                      , 0 SoLuongDotChayBooking
                      , HDCT.SoLuong
                      , @DonViTinh AS DonViTinh
                      , HDCT.DonGia
                      , @DonGiaTheoDVT AS DonGiaTheoDonVi
                      , HDCT.ChietKhau
                      , HDCT.GiamGia
                      , HDCT.ThanhTien
                      , HDCT.TiLeTuVan
                      , HDCT.ChiPhiTuVan
                      , HDCT.IsKhuyenMai
                      , HDCT.KhuyenMai
                      , @DmBannerREF AS banner_id
                      , @DmCampaign DmChienDichREF
                      , [dbo].[GetWebsiteIDByDomainName](@TenWebsite) DmWebsiteREF
                      , @TenWebsite TenWebsite
                      , @TongViewThucChay AS TongViewThucChay
                      , @TongClickThucChay AS TongClickThucChay
                      , 0 TongSoBaiViet
                      , @SoLuongThucChay AS SoLuongThucChay
                      , @NgayThucHien AS NgayThucHien
                      , 0 GiaTriThayDoi
                      , 0 ThanhTienThucChayTruocTrietKhau
                      , 0 GiaTriTrietKhauThucChay
                      , @GiaTriThucChay ThanhTienSauTrietKhauThucChay
                      , 0 GiaTriHoaHongThucChay
                      , 0 ThanhTienThucThu
                      , @GiaTriThucChayKM ThanhTienKM
                      , @SoLuongThucChayKM SoLuongThucChayKM
                      , @SoLuongLechTreoha SoLuongThucChayLechTreoHa
                      , @GiaTriLechTreoHa ThanhTienLechTreoHa
                      , GETDATE() CreatedAt
                      , GETDATE() LastModifiedAt
                      , 0 IsPheDuyet
                      , N'' PheDuyetBy
                      , GETDATE() PheDuyetAt
                      , 0 SoLuongThayDoi
                      , 0 SoLuongKMThayDoi
                      , 0 GiaTriKMThayDoi
                      , N'ThucChay_Insert_ThucChayDaTinh_Admatic_Adx' GhiChu
                FROM (SELECT * FROM dbo.HopDong HD WHERE HD.HopDongID = @HopDongID AND HD.DeletedStatus = 0 AND HD.TrangThaiHopDong NOT IN (0,3))HD 
                    INNER JOIN (SELECT * FROM dbo.HopDongChiTiet HDCT WHERE HDCT.HopDongChiTietID = @pHopDongChiTiet AND HDCT.DeletedStatus = 0)HDCT ON HDCT.HopDongFK = HD.HopDongID


		--INSERT THONG TIN THUC CHAY VAO THUCCHAYDATINHADMARKET
        INSERT  INTO dbo.ThucChayDaTinhAdmarket
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
                SELECT  NEWID()
                      , HD.HopDongID
                      , HD.SoHopDong
                      , HD.DmMaHopDongREF
                      , HD.TenMaHopDong
                      , HD.NgayDanhSoHopDong
                      , HD.NgayKyHopDong
					  , HD.NhanHopDong
                      , HD.NgayNhanBanFax
                      , HD.NgayNhanHopDongBanCung
                      , HD.NgayChuyenHopDongChoKeToan
                      , HD.So
                      , HD.Thang
                      , HD.Nam
                      , HD.GiaTriHopDong
                      , HD.CongNo
                      , HDCT.HopDongChiTietID HopDongChiTietREF
                      , HD.DangSuDung
                      , HD.IsGiayPhep
                      , HD.TrangThaiHopDong
                      , HD.IsBanCung
                      , HD.DmPhongBanREF
                      , ISNULL(HD.TenPhongBan,'') AS TenPhongBan
                      , HD.DmBoPhanREF
                      , ISNULL(HD.TenBoPhan,'') AS TenBoPhan
                      , HD.DmNhomLamViecREF
                      , ISNULL(HD.TenNhom, '') AS TenNhom
                      , HD.DmDiaDiemLamViecREF
                      , ISNULL(HD.TenDiaDiemLamViec,'')TenDiaDiemLamViec
                      , HD.SysNhanVienREF
                      , HD.TenDangNhap
                      , ISNULL(HD.TenNhanVien,'') AS TenNhanVien
                      , HD.TenKhachHang
                      , HDCT.DanhSachNhanHangREF
                      , HDCT.DmNhomNganhREF
                      , HDCT.TenNhomNganh
                      , HDCT.DmLoaiREF
                      , HDCT.TenLoai
                      , 585 AS DmSanPhamREF --SAN PHAM ADX
                      , N'AdX' AS TenSanPham
                      , HDCT.DmNhomWebsiteREF
                      , HDCT.TenNhomWebsite
                      , HDCT.DmChuyenMucREF
                      , HDCT.TenChuyenMuc
                      , HDCT.DmLoaiBannerREF
                      , HDCT.TenLoaiBanner
                      , @DmViTriREF AS DmViTriREF
                      , @TenViTri TenViTri
                      , '' DotChayHopDong
                      , 0 SoLuongDotChayHD
                      , '' DotChayBooking
                      , 0 SoLuongDotChayBooking
                      , HDCT.SoLuong
                      , @DonViTinh AS DonViTinh
                      , HDCT.DonGia
                      , @DonGiaTheoDVT AS DonGiaTheoDonVi
                      , HDCT.ChietKhau
                      , HDCT.GiamGia
                      , HDCT.ThanhTien
                      , HDCT.TiLeTuVan
                      , HDCT.ChiPhiTuVan
                      , HDCT.IsKhuyenMai
                      , HDCT.KhuyenMai
                      , @DmBannerREF AS banner_id
                      , @DmCampaign DmChienDichREF
                      , [dbo].[GetWebsiteIDByDomainName](@TenWebsite) DmWebsiteREF
                      , @TenWebsite TenWebsite
                      , @TongViewThucChay AS TongViewThucChay
                      , @TongClickThucChay AS TongClickThucChay
                      , 0 TongSoBaiViet
                      , @SoLuongThucChay AS SoLuongThucChay
                      , @NgayThucHien AS NgayThucHien
                      , 0 GiaTriThayDoi
                      , 0 ThanhTienThucChayTruocTrietKhau
                      , 0 GiaTriTrietKhauThucChay
                      , @GiaTriThucChay ThanhTienSauTrietKhauThucChay
                      , 0 GiaTriHoaHongThucChay
                      , 0 ThanhTienThucThu
                      , @GiaTriThucChayKM ThanhTienKM
                      , @SoLuongThucChayKM SoLuongThucChayKM
                      , @SoLuongLechTreoha SoLuongThucChayLechTreoHa
                      , @GiaTriLechTreoHa ThanhTienLechTreoHa
                      , GETDATE() CreatedAt
                      , GETDATE() LastModifiedAt
                      , 0 IsPheDuyet
                      , N'' PheDuyetBy
                      , GETDATE() PheDuyetAt
                      , 0 SoLuongThayDoi
                      , 0 SoLuongKMThayDoi
                      , 0 GiaTriKMThayDoi
                      , N'ThucChay_Insert_ThucChayDaTinh_Admatic_Adx' GhiChu
                FROM (SELECT * FROM dbo.HopDong HD WHERE HD.HopDongID = @HopDongID AND HD.DeletedStatus = 0 AND HD.TrangThaiHopDong NOT IN (0,3))HD 
                    INNER JOIN (SELECT * FROM dbo.HopDongChiTiet HDCT WHERE HDCT.HopDongChiTietID = @pHopDongChiTiet AND HDCT.DeletedStatus = 0)HDCT ON HDCT.HopDongFK = HD.HopDongID

       
    END



```
