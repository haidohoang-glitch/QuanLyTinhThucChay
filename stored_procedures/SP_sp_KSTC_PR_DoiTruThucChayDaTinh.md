# Stored Procedure: `sp_KSTC_PR_DoiTruThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-19 09:56:28.247000
- **Ngày sửa cuối**: 2020-07-03 15:08:58.240000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DotChayBooking` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_PR_DoiTruThucChayDaTinh] 
	-- Add the parameters for the stored procedure here
	@HopDongID INT,    
    @DmSanPhamREF INT,
	@DotChayBooking int,
	@NgaythucHien Datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	 DECLARE @NgayGioiHanTinh DATETIME ,
            @NoteThongTinThayDoi NVARCHAR(200) 
        SET @NgayGioiHanTinh = '2014-01-01'
        SET @NoteThongTinThayDoi = 'DOITRUGIATRI_PR'
	
        --PRINT @HopDongID
		--1. INSERT THONG TIN GIA TRI THAY DOI TRUOC DO GIAM
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
                        @NoteThongTinThayDoi ,
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
						AND convert(nvarchar(50),DotChayBooking) = convert(nvarchar(50),@DotChayBooking)
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


						update ThucChayHopDongChiTietPR set RecordStatus = 0 where ThucChayHopDongChiTietPRID = @DotChayBooking
END

```
