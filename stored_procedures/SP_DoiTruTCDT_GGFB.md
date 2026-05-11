# Stored Procedure: `DoiTruTCDT_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-12-25 19:03:17.457000
- **Ngày sửa cuối**: 2020-12-25 19:03:17.457000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
      create Procedure [dbo].[DoiTruTCDT_GGFB]
	
	  @NgayThucHien datetime,
	  @HopDongID int, @HopDongChiTietID int, @GhiChu nvarchar(200)
	  as
	  begin
	
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
                SELECT  NEWID() ,
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
                         0 TongViewThucChay
                , 0 TongClickThucChay
                , 0 TongSoBaiViet
                , 0 SoLuongThucChay
                , @NgayThucHien
                , -sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi)GiaTriThayDoi
                , 0 ThanhTienThucChayTruocTrietKhau
                , 0 GiaTriTrietKhauThucChay
                , 0 ThanhTienSauTrietKhauThucChay
                , 0 GiaTriHoaHongThucChay
                , 0 ThanhTienThucThu
                , 0 ThanhTienKM
                , 0 SoLuongThucChayKM
                , 0 SoLuongThucChayLechTreoHa
                , 0 ThanhTienLechTreoHa
                , getdate()CreatedAt
                , getdate()LastModifiedAt
                , 0 IsPheDuyet
                , 0 PheDuyetBy
                , 0 PheDuyetAt
                , -sum(SoLuongthucchay+SoLuongthaydoi)SoLuongThayDoi
                , -sum(SoLuongThucChayKM+SoLuongKMThayDoi)SoLuongKMThayDoi
                , -sum(ThanhTienKM+GiaTriKMThayDoi)GiaTriKMThayDoi
                 ,       @GhiChu GhiChu
                FROM    dbo.ThucChayDaTinh
                WHERE   HopDongID = @HopDongID
                        AND NgayThucHien <= @NgaythucHien
                        AND HopDongChiTietREF = @HopDongChiTietID
						AND DmChienDichREF = 0
						--AND NOT(DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
						
                GROUP BY HopDongID ,
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
                        SoLuongDotChayHD ,
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
                        DotChayBooking,
						DotChayHopDong

						end
```
