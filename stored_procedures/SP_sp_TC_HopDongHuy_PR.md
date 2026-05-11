# Stored Procedure: `sp_TC_HopDongHuy_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-16 15:12:46.850000
- **Ngày sửa cuối**: 2017-12-08 09:54:40.503000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@SoLuongThayDoi` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_PR]


CREATE PROCEDURE [dbo].[sp_TC_HopDongHuy_PR]
    @ThucChayHopDongChiTietPRID INT ,
    @HopDongID INT ,
    @NgaythucHien DATETIME ,
    @GiaTriThayDoi FLOAT ,
    @SoLuongThayDoi INT ,
    @HopDongChiTietREF INT
AS
    BEGIN
        DECLARE @NgayGioiHanTinh DATETIME ,
            @NoteThongTinThayDoi NVARCHAR(200) 
        SET @NgayGioiHanTinh = '2014-01-01'
        SET @NoteThongTinThayDoi = 'PSGTTD_PR'
	
        PRINT @ThucChayHopDongChiTietPRID
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
                        CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID) ,
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
                        N'Hợp đồng hủy'
                FROM    ThucChayDaTinh
                WHERE   HopDongID = @HopDongID
                        AND DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID)
                        AND NgayThucHien < @NgaythucHien
                        AND HopDongChiTietREF = @HopDongChiTietREF
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
	
        
	


        IF EXISTS ( SELECT  NEWID() ,
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
                            CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID) ,
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
                            N'Hợp đồng hủy'
                    FROM    ThucChayDaTinh
                    WHERE   HopDongID = @HopDongID
                            AND DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID)
                            AND NgayThucHien < @NgaythucHien
                            AND HopDongChiTietREF = @HopDongChiTietREF
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
                            DotChayBooking )
            BEGIN
                UPDATE  dbo.ThucChayHopDongChiTietPR
                SET     RecordStatus = 0
                WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                        AND HopDongREF = @HopDongID


                INSERT  INTO dbo.ThucChay_Temp_CheckLoi
                        ( HopDongID ,
                          ThucChayHopDongChiTietPRID ,
                          NgayTao ,
                          GhiChu
		                )
                VALUES  ( @HopDongID , -- HopDongID - int
                          @ThucChayHopDongChiTietPRID , -- ThucChayHopDongChiTietPRID - int
                          GETDATE() , -- NgayTao - datetime
                          N'Hợp đồng hủy'  -- GhiChu - nvarchar(500)
		                )

	

                DELETE  FROM ThucChay_ThongTinHopDongChiTietID_PR
                WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                        AND HopDongChiTietID = @HopDongChiTietREF
            END
        
        









		---------------------- Tinh lai


        DECLARE @Temp TABLE
            (
              HopDongChiTietID INT ,
              ThucChayHopDongChiTietPRID INT
            );


        DECLARE @ThucChayHopDongChiTietPRID_Temp INT ,
            @HopDongREF_Temp INT ,
            @ChietKhau_Temp FLOAT ,
            @ThucChayHopDongChiTietPrREF_Temp INT ,
            @HopDongChiTietREF_Temp INT ,
            @DmHinhThucQuangCaoREF_Temp INT ,
            @DmSanPhamREF_Temp INT ,
            @DmWebsiteREF_Temp INT ,
            @GiaTien_Temp INT ,
            @SoLuong_Temp INT

					



        SELECT  @ThucChayHopDongChiTietPRID_Temp = ThucChayHopDongChiTietPRID ,
                @HopDongREF_Temp = HopDongREF ,
                @ChietKhau_Temp = ChietKhau ,
                @ThucChayHopDongChiTietPrREF_Temp = ThucChayHopDongChiTietPrREF ,
                @HopDongChiTietREF_Temp = HopDongChiTietREF ,
                @DmHinhThucQuangCaoREF_Temp = DmHinhThucQuangCaoREF ,
                @DmSanPhamREF_Temp = DmSanPhamREF ,
                @DmWebsiteREF_Temp = DmWebsiteREF ,
                @GiaTien_Temp = GiaTien ,
                @SoLuong_Temp = SoLuong
        FROM    ThucChayHopDongChiTietPR
        WHERE   DeletedStatus <> 1
                AND RecordStatus = 0
                AND DmHinhThucQuangCaoREF <> 0
                AND DmSanPhamREF <> 0
                AND ThoiGianBatDau >= '2014-01-01'
                AND ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID





        INSERT  INTO @Temp
                SELECT  *
                FROM    fn_TC_GetHopDongChiTietID_PR(@ThucChayHopDongChiTietPRID_Temp,
                                                     @HopDongREF_Temp,
                                                     @ChietKhau_Temp,
                                                     @ThucChayHopDongChiTietPrREF_Temp,
                                                     @HopDongChiTietREF_Temp,
                                                     @DmHinhThucQuangCaoREF_Temp,
                                                     @DmSanPhamREF_Temp,
                                                     @DmWebsiteREF_Temp,
                                                     @GiaTien_Temp,
                                                     @SoLuong_Temp);






        INSERT  INTO dbo.ThucChayDaTinh
                SELECT  NEWID() ,
                        T.*
                FROM    ( SELECT  DISTINCT
                                    hd.HopDongID ,
                                    hd.SoHopDong ,
                                    hd.DmMaHopDongREF ,
                                    hd.TenMaHopDong ,
                                    hd.NgayDanhSoHopDong ,
                                    hd.NgayKyHopDong ,
                                    ISNULL(hd.NhanHopDong, '') AS NhanHopDong ,
                                    hd.NgayNhanBanFax ,
                                    hd.NgayNhanHopDongBanCung ,
                                    hd.NgayChuyenHopDongChoKeToan ,
                                    hd.So ,
                                    hd.Thang ,
                                    hd.Nam , 
		--Thong tin ve gia tri
                                    hd.GiaTriHopDong ,
                                    hd.CongNo ,
		--Thong tin chi tiet phan bo
                                    tchpctpr.HopDongChiTietID ,
		--Thong tin ve trang thai
                                    hd.DangSuDung ,
                                    hd.IsGiayPhep ,
                                    hd.TrangThaiHopDong ,
                                    hd.IsBanCung , 
		--Thong tin ve Nhan vien kinh doanh
                                    hd.DmPhongBanREF ,
                                    ISNULL(hd.TenPhongBan, '') AS TenPhongBan ,
                                    hd.DmBoPhanREF ,
                                    ISNULL(hd.TenBoPhan, '') AS TenBoPhan ,
                                    hd.DmNhomLamViecREF ,
                                    ISNULL(hd.TenNhom, '') AS TenNhom ,
                                    hd.DmDiaDiemLamViecREF ,
                                    ISNULL(hd.TenDiaDiemLamViec, '') AS TenDiaDiemLamViec ,
                                    hd.SysNhanVienREF ,
                                    ISNULL(hd.TenDangNhap, '') AS TenDangNhap ,
                                    hd.TenNhanVien ,
                                    hd.TenKhachHang ,
                                    tchpctpr.DmNhanHangREF AS NhanHang ,
                                    0 DmNhomNganhREF ,
                                    '' TenNhomNganh , 
		--Thong tin hinh thuc quang cao
                                    hdct.DmLoaiREF AS DmHinhThucQuangCao ,
                                    hdct.TenLoai AS TenHinhThucQuangCao , 
		--Thong tin San pham
                                    hdct.DmSanPhamREF AS DmSanPhamREF ,
                                    hdct.TenSanPham ,
                                    0 DmNhomWebsiteREF ,
                                    '' TenNhomWebsite ,
                                    tchpctpr.DmChuyenMucREF ,
                                    tchpctpr.TenChuyenMuc ,
                                    hdct.DmLoaiBannerREF ,
                                    hdct.TenLoaiBanner ,
                                    tchpctpr.DmViTriREF ,
                                    tchpctpr.TenViTri ,
                                    '' DotChayHopDong ,
                                    0 AS SoLuongDotChayHD ,
		--'' DotChayBooking,
                                    tchpctpr.ThucChayHopDongChiTietPRID DotChayBooking ,
                                    0 AS SoLuongDotChayBooking , 
		--Thong tin ve Tien
                                    hdct.SoLuong AS SoLuong ,
                                    dbo.FormatDonViTinh(hdct.DonViTinh) DonViTinh ,
                                    hdct.DonGia AS DonGia ,
                                    tchpctpr.GiaTien AS DonGiaTheoDonViTinh ,
                                    tchpctpr.ChietKhau ,
                                    hdct.GiamGia ,
                                    hdct.ThanhTien ,
                                    hdct.TiLeTuVan ,
                                    hdct.ChiPhiTuVan ,
                                    tchpctpr.KhuyenMai IsKhuyenMai ,
                                    '' KhuyenMai ,
		--Thuc chay
                                    0 DmBannerREF ,--A.DmBannerREF,
                                    0 DmChienDichREF ,--A.DmChienDichREF,
                                    dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(tchpctpr.DmWebsiteREF) DmWebsiteREF ,
                                    dbo.GetWebsiteLinkByDmWebsiteID(tchpctpr.DmWebsiteREF,
                                                              tchpctpr.TenWebsite) TenWebsite ,
                                    0 TongViewThucChay ,
                                    0 TongClickThucChay ,
                                    0 TongSoBaiViet ,
                                    ( CASE WHEN tchpctpr.KhuyenMai = 0
                                                AND tchpctpr.ChietKhau <> 100
                                           THEN ISNULL(tchpctpr.SoLuong, 0)
                                           ELSE 0
                                      END ) AS SoLuongThucChay ,
                                    @NgaythucHien AS NgayThucHien ,
                                    0 AS GiaTriThayDoi ,
                                    ISNULL(tchpctpr.GiaTien, 0)
                                    * ISNULL(tchpctpr.SoLuong, 0) AS ThanhTienThucChayTruocChietKhau ,
                                    ISNULL(( CONVERT(FLOAT, ISNULL(tchpctpr.GiaTien,
                                                              0))
                                             * CONVERT(FLOAT, ISNULL(tchpctpr.SoLuong,
                                                              0))
                                             * CONVERT(FLOAT, tchpctpr.ChietKhau) )
                                           / 100, 0) AS GiaTriTrietKhauThucChay ,
                                    ISNULL(tchpctpr.GiaTien, 0)
                                    * ISNULL(tchpctpr.SoLuong, 0)
                                    * ( CONVERT(FLOAT, ( 100
                                                         - tchpctpr.ChietKhau ))
                                        / 100 ) AS ThanhTienThucChaySauChietKhau ,
                                    ( CONVERT(FLOAT, ( 100
                                                       - tchpctpr.ChietKhau ))
                                      * CONVERT(FLOAT, ( ISNULL(tchpctpr.GiaTien,
                                                              0)
                                                         * ISNULL(tchpctpr.SoLuong,
                                                              0) )) / 100 )
                                    * ISNULL(hdct.TiLeTuVan, 0) / 100 AS GiaTriHoaHongThucChay ,
                                    ( CASE WHEN ( tchpctpr.KhuyenMai = 1
                                                  OR tchpctpr.ChietKhau = 100
                                                  OR tchpctpr.GiaTien = 0
                                                  OR tchpctpr.SoLuong = 0
                                                ) THEN 0
                                           ELSE ( 100 - hdct.TiLeTuVan )
                                                / ( ISNULL(tchpctpr.GiaTien, 0)
                                                    * ISNULL(tchpctpr.SoLuong,
                                                             0)
                                                    * ( CONVERT(FLOAT, ( 100
                                                              - tchpctpr.ChietKhau ))
                                                        / 100 ) )
                                      END ) AS ThanhTienThucThu ,
                                    ( CASE WHEN tchpctpr.KhuyenMai = 1
                                                OR tchpctpr.ChietKhau = 100
                                           THEN ISNULL(tchpctpr.GiaTien, 0)
                                                * ISNULL(tchpctpr.SoLuong, 0)
                                           ELSE 0
                                      END ) AS ThanhTienKM ,
                                    ( CASE WHEN tchpctpr.KhuyenMai = 1
                                                OR tchpctpr.ChietKhau = 100
                                           THEN ISNULL(tchpctpr.SoLuong, 0)
                                           ELSE 0
                                      END ) AS SoLuongThucChayKM ,
                                    0 SoLuongLechTreoHa ,
                                    0 ThanhTienLechTreoHa ,
                                    GETDATE() CreatedAt ,
                                    GETDATE() LastModifiedAt ,
                                    0 IsPheDuyet ,
                                    '' PheDuyetBy ,
                                    '' PheDuyetAt ,
                                    0 SoLuongThayDoi ,
                                    0 SoLuongKMThayDoi ,
                                    0 GiaTriKMThayDoi ,
                                    N'Tính lại HD hủy' GhiChu
                          FROM      ( SELECT    tchpctpr.* ,
                                                T.HopDongChiTietID HopDongChiTietID
                                      FROM      ThucChayHopDongChiTietPR tchpctpr
                                                INNER JOIN @Temp T ON tchpctpr.ThucChayHopDongChiTietPRID = T.ThucChayHopDongChiTietPRID
                                      WHERE     tchpctpr.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                                    ) tchpctpr
                                    INNER JOIN ( SELECT --ID Hop Dong
                                                        D.HopDongID ,
				--Thong tin ve ma so 
                                                        D.SoHopDong ,
                                                        D.DmMaHopDongREF ,
                                                        D.TenMaHopDong , 
				--Thong tin ve thoi gian
                                                        D.NgayDanhSoHopDong ,
                                                        D.NgayKyHopDong ,
                                                        ISNULL(D.NhanHopDong,
                                                              '') AS NhanHopDong ,
                                                        D.NgayNhanBanFax ,
                                                        D.NgayNhanHopDongBanCung ,
                                                        D.NgayChuyenHopDongChoKeToan ,
                                                        D.So ,
                                                        D.Thang ,
                                                        D.Nam , 
				--Thong tin ve gia tri
                                                        D.GiaTriHopDong ,
                                                        D.CongNo ,
				--Thong tin ve trang thai
                                                        D.DangSuDung ,
                                                        D.IsGiayPhep ,
                                                        D.TrangThaiHopDong ,
                                                        D.IsBanCung , 
				--Thong tin ve Nhan vien kinh doanh
                                                        D.DmPhongBanREF ,
                                                        ISNULL(D.TenPhongBan,
                                                              '') AS TenPhongBan ,
                                                        D.DmBoPhanREF ,
                                                        ISNULL(D.TenBoPhan, '') AS TenBoPhan ,
                                                        D.DmNhomLamViecREF ,
                                                        ISNULL(D.TenNhom, '') AS TenNhom ,
                                                        D.DmDiaDiemLamViecREF ,
                                                        D.TenDiaDiemLamViec ,
                                                        D.SysNhanVienREF ,
                                                        ISNULL(D.TenDangNhap,
                                                              '') AS TenDangNhap ,
                                                        D.TenNhanVien ,
                                                        D.TenKhachHang
                                                 FROM   HopDong D
                                                 WHERE  D.TrangThaiHopDong != 3
                                                        AND D.Nam >= 2013
                                               ) hd ON tchpctpr.HopDongREF = hd.HopDongID
                                    INNER JOIN dbo.HopDongChiTiet hdct ON tchpctpr.HopDongChiTietID = hdct.HopDongChiTietID
                                                              AND hdct.DmLoaiREF = tchpctpr.DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = tchpctpr.DmSanPhamREF
                          WHERE     hdct.IsKhuyenMai = 0
                        ) T;      

				


        IF EXISTS ( SELECT  tchpctpr.* ,
                            T.HopDongChiTietID HopDongChiTietID
                    FROM    ThucChayHopDongChiTietPR tchpctpr
                            INNER JOIN @Temp T ON tchpctpr.ThucChayHopDongChiTietPRID = T.ThucChayHopDongChiTietPRID
                    WHERE   tchpctpr.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID )
            BEGIN
                UPDATE  dbo.ThucChayHopDongChiTietPR
                SET     RecordStatus = 1
                WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                        AND HopDongREF = @HopDongID


                IF NOT EXISTS ( SELECT  *
                                FROM    ThucChay_ThongTinHopDongChiTietID_PR
                                WHERE   ThucChayHopDongChiTietPRID IN (
                                        SELECT  t.ThucChayHopDongChiTietPRID
                                        FROM    @Temp t ) )
                    BEGIN
                        INSERT  INTO ThucChay_ThongTinHopDongChiTietID_PR
                                SELECT  t.HopDongChiTietID ,
                                        t.ThucChayHopDongChiTietPRID
                                FROM    @Temp t
                    END
            END

		




        DELETE  FROM @Temp




    END




--EXEC [ThucChay_InsertThucChayDaTinh_PR] '2013-07-01','2013-07-11'

```
