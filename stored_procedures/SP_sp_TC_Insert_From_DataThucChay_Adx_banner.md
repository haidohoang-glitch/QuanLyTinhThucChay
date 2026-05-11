# Stored Procedure: `sp_TC_Insert_From_DataThucChay_Adx_banner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-29 17:35:31.153000
- **Ngày sửa cuối**: 2018-03-27 17:22:26.127000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pHopDongChiTiet` | `int(4)` | No |
| `@banner_id` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


-- sp_TC_Insert_From_DataThucChay_Adx '2017-09-14', '2017-09-16', 'QC5120917', 513663

CREATE  PROCEDURE [dbo].[sp_TC_Insert_From_DataThucChay_Adx_banner]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @pSoHopDong NVARCHAR(50)
  , @pHopDongChiTiet INT
  ,@banner_id int
AS
    BEGIN
		
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
                      , ADX.contract_number
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
                      , @pHopDongChiTiet HopDongChiTietREF
                      , HD.DangSuDung
                      , HD.IsGiayPhep
                      , HD.TrangThaiHopDong
                      , HD.IsBanCung
                      , HD.DmPhongBanREF
                      , HD.TenPhongBan
                      , HD.DmBoPhanREF
                      , HD.TenBoPhan
                      , HD.DmNhomLamViecREF
                      , ISNULL(HD.TenNhom, '')
                      , HD.DmDiaDiemLamViecREF
                      , HD.TenDiaDiemLamViec
                      , HD.SysNhanVienREF
                      , HD.TenDangNhap
                      , HD.TenNhanVien
                      , HD.TenKhachHang
                      , HDCT.DanhSachNhanHangREF
                      , HDCT.DmNhomNganhREF
                      , HDCT.TenNhomNganh
                      , HDCT.DmLoaiREF
                      , HDCT.TenLoai
                      , ADX.DmSanPhamREF
                      , ADX.TenSanPham
                      , HDCT.DmNhomWebsiteREF
                      , HDCT.TenNhomWebsite
                      , HDCT.DmChuyenMucREF
                      , HDCT.TenChuyenMuc
                      , HDCT.DmLoaiBannerREF
                      , HDCT.TenLoaiBanner
                      , ADX.DmViTriREF
                      , ADX.TenViTri
                      , '' DotChayHopDong
                      , 0 SoLuongDotChayHD
                      , '' DotChayBooking
                      , 0 SoLuongDotChayBooking
                      , HDCT.SoLuong
                      , HDCT.DonViTinh
                      , HDCT.DonGia
                      , HDCT.DonGia DonGiaTheoDonVi
                      , HDCT.ChietKhau
                      , HDCT.GiamGia
                      , HDCT.ThanhTien
                      , HDCT.TiLeTuVan
                      , HDCT.ChiPhiTuVan
                      , HDCT.IsKhuyenMai
                      , HDCT.KhuyenMai
                      , ADX.banner_id
                      , ADX.campaign_id DmChienDichREF
                      , [dbo].[GetWebsiteIDByDomainName](ADX.domain_name) DmWebsiteREF
                      , ADX.domain_name TenWebsite
                      , CONVERT(FLOAT, ADX.domain_tt_view) TongViewThucChay
                      , CONVERT(FLOAT, ADX.domain_tt_click) TongClickThucChay
                      , 0 TongSoBaiViet
                      , ADX.domain_tt_click SoLuongThucChay
                      , ADX.NgayThucHien
                      , 0 GiaTriThayDoi
                      , 0 ThanhTienThucChayTruocTrietKhau
                      , 0 GiaTriTrietKhauThucChay
                      , CONVERT(FLOAT, ADX.domain_tt_money) / 1.1 ThanhTienSauTrietKhauThucChay
                      , 0 GiaTriHoaHongThucChay
                      , 0 ThanhTienThucThu
                      , CONVERT(FLOAT, ADX.domain_tt_promotion) / 1.1 ThanhTienKM
                      , 0 SoLuongThucChayKM
                      , 0 SoLuongThucChayLechTreoHa
                      , 0 ThanhTienLechTreoHa
                      , GETDATE() CreatedAt
                      , GETDATE() LastModifiedAt
                      , 0 IsPheDuyet
                      , N'' PheDuyetBy
                      , GETDATE() PheDuyetAt
                      , 0 SoLuongThayDoi
                      , 0 SoLuongKMThayDoi
                      , 0 GiaTriKMThayDoi
                      , N'sp_TC_Insert_From_DataThucChay_Adx' GhiChu
                FROM    dbo.DataThucChay_Adx ADX
                        INNER JOIN dbo.HopDong HD ON ADX.contract_number = HD.SoHopDong
                        INNER JOIN dbo.HopDongChiTiet HDCT ON HDCT.HopDongFK = HD.HopDongID
                WHERE   contract_number = @pSoHopDong
                        AND NgayThucHien BETWEEN @StartDate AND @EndDate
                        AND HDCT.HopDongChiTietID = @pHopDongChiTiet
						and ADX.banner_id = @banner_id



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
                      , ADX.contract_number
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
                      , @pHopDongChiTiet HopDongChiTietREF
                      , HD.DangSuDung
                      , HD.IsGiayPhep
                      , HD.TrangThaiHopDong
                      , HD.IsBanCung
                      , HD.DmPhongBanREF
                      , HD.TenPhongBan
                      , HD.DmBoPhanREF
                      , HD.TenBoPhan
                      , HD.DmNhomLamViecREF
                      , ISNULL(HD.TenNhom, '')
                      , HD.DmDiaDiemLamViecREF
                      , HD.TenDiaDiemLamViec
                      , HD.SysNhanVienREF
                      , HD.TenDangNhap
                      , HD.TenNhanVien
                      , HD.TenKhachHang
                      , HDCT.DanhSachNhanHangREF
                      , HDCT.DmNhomNganhREF
                      , HDCT.TenNhomNganh
                      , HDCT.DmLoaiREF
                      , HDCT.TenLoai
                      , ADX.DmSanPhamREF
                      , ADX.TenSanPham
                      , HDCT.DmNhomWebsiteREF
                      , HDCT.TenNhomWebsite
                      , HDCT.DmChuyenMucREF
                      , HDCT.TenChuyenMuc
                      , HDCT.DmLoaiBannerREF
                      , HDCT.TenLoaiBanner
                      , ADX.DmViTriREF
                      , ADX.TenViTri
                      , '' DotChayHopDong
                      , 0 SoLuongDotChayHD
                      , '' DotChayBooking
                      , 0 SoLuongDotChayBooking
                      , HDCT.SoLuong
                      , HDCT.DonViTinh
                      , HDCT.DonGia
                      , HDCT.DonGia DonGiaTheoDonVi
                      , HDCT.ChietKhau
                      , HDCT.GiamGia
                      , HDCT.ThanhTien
                      , HDCT.TiLeTuVan
                      , HDCT.ChiPhiTuVan
                      , HDCT.IsKhuyenMai
                      , HDCT.KhuyenMai
                      , ADX.banner_id
                      , ADX.campaign_id DmChienDichREF
                      , [dbo].[GetWebsiteIDByDomainName](ADX.domain_name) DmWebsiteREF
                      , ADX.domain_name TenWebsite
                      , CONVERT(FLOAT, ADX.domain_tt_view) TongViewThucChay
                      , CONVERT(FLOAT, ADX.domain_tt_click) TongClickThucChay
                      , 0 TongSoBaiViet
                      , ADX.domain_tt_click SoLuongThucChay
                      , ADX.NgayThucHien
                      , 0 GiaTriThayDoi
                      , 0 ThanhTienThucChayTruocTrietKhau
                      , 0 GiaTriTrietKhauThucChay
                      , CONVERT(FLOAT, ADX.domain_tt_money) / 1.1 ThanhTienSauTrietKhauThucChay
                      , 0 GiaTriHoaHongThucChay
                      , 0 ThanhTienThucThu
                      , CONVERT(FLOAT, ADX.domain_tt_promotion) / 1.1 ThanhTienKM
                      , 0 SoLuongThucChayKM
                      , 0 SoLuongThucChayLechTreoHa
                      , 0 ThanhTienLechTreoHa
                      , GETDATE() CreatedAt
                      , GETDATE() LastModifiedAt
                      , 0 IsPheDuyet
                      , N'' PheDuyetBy
                      , GETDATE() PheDuyetAt
                      , 0 SoLuongThayDoi
                      , 0 SoLuongKMThayDoi
                      , 0 GiaTriKMThayDoi
                      , N'sp_TC_Insert_From_DataThucChay_Adx' GhiChu
                FROM    dbo.DataThucChay_Adx ADX
                        INNER JOIN dbo.HopDong HD ON ADX.contract_number = HD.SoHopDong
                        INNER JOIN dbo.HopDongChiTiet HDCT ON HDCT.HopDongFK = HD.HopDongID
                WHERE   contract_number = @pSoHopDong
                        AND NgayThucHien BETWEEN @StartDate AND @EndDate
                        AND HDCT.HopDongChiTietID = @pHopDongChiTiet
						and ADX.banner_id = @banner_id
       
    END



```
