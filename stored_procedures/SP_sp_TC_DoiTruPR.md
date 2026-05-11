# Stored Procedure: `sp_TC_DoiTruPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-07-03 15:04:19.090000
- **Ngày sửa cuối**: 2020-07-03 15:04:19.090000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayDaTinhID` | `nvarchar(100)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
create proc sp_TC_DoiTruPR
@ThucChayDaTinhID nvarchar(50),
@HopDongID int,
@DmSanPhamREF int,
@NgayThucHien datetime
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
                        'DOITRUGIATRI_PR' ,
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
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        @NgaythucHien ,
                        -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        0 ,
                        GETDATE() ,
                        GETDATE() ,
                        0 ,
                        '' ,
                        GETDATE() ,
                        -SUM(SoLuongThucChay + SoLuongThayDoi) ,
                        -SUM(SoLuongThucChayKM + SoLuongKMThayDoi) ,
                        -SUM(ThanhTienKM + GiaTriKMThayDoi) ,
                        N'Thực hiện đổi trừ giá trị toàn bộ' GhiChu
                FROM    dbo.ThucChayDaTinh
                WHERE   HopDongID = @HopDongID
                        AND NgayThucHien <= @NgaythucHien
                        AND HopDongID = @HopDongID
						AND DmSanPhamREF = @DmSanPhamREF
						AND NOT(DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
						--AND HopDongChiTietREF IN (SELECT CONVERT(INT,[VALUE]) FROM dbo.ASD_SPLIT(',',@List_HopDongChiTietREF))
						and ThucChayDaTinhID = @ThucChayDaTinhID
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
                        DotChayBooking
						end
```
