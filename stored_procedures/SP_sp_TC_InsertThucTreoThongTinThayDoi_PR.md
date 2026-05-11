# Stored Procedure: `sp_TC_InsertThucTreoThongTinThayDoi_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 16:00:15.743000
- **Ngày sửa cuối**: 2020-03-12 16:09:51.883000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@SoLuongThayDoi` | `int(4)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_PR]


CREATE PROCEDURE [dbo].[sp_TC_InsertThucTreoThongTinThayDoi_PR]
    @ThucChayHopDongChiTietPRID INT ,
    @HopDongID INT ,
    @NgaythucHien DATETIME ,
    @GiaTriThayDoi FLOAT ,
    @SoLuongThayDoi INT ,
    @GhiChu NVARCHAR(500) ,
    @HopDongChiTietID INT
AS
    BEGIN
        DECLARE @NgayGioiHanTinh DATETIME ,
            @NoteThongTinThayDoi NVARCHAR(200) 
        SET @NgayGioiHanTinh = '2014-01-01'
        SET @NoteThongTinThayDoi = 'PSGTTD_PR'
	
   
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
                        @GhiChu
                FROM    dbo.ThucChayDaTinh
                WHERE   HopDongID = @HopDongID
                        AND DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID)
                        AND NgayThucHien < @NgaythucHien
                        AND HopDongChiTietREF = @HopDongChiTietID
						AND ChietKhau <> 100
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
						DotChayBooking,
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
                            @GhiChu
                    FROM    dbo.ThucChayDaTinh
                    WHERE   HopDongID = @HopDongID
                            AND DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID)
                            AND NgayThucHien < @NgaythucHien
                            AND HopDongChiTietREF = @HopDongChiTietID
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
                          @GhiChu  -- GhiChu - nvarchar(500)
		                )

        
                DELETE  FROM dbo.ThucChay_ThongTinHopDongChiTietID_PR
                WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                        AND HopDongChiTietID = @HopDongChiTietID
            END
 		
        IF ( @GiaTriThayDoi <> 0 )
            BEGIN
                DECLARE @Temp TABLE
                    (
                      HopDongChiTietID INT ,
                      ThucChayHopDongChiTietPRID INT
                    );


                DECLARE @ThucChayHopDongChiTietPRID_ INT ,
                    @HopDongREF INT ,
                    @ChietKhau FLOAT ,
                    @ThucChayHopDongChiTietPrREF INT ,
                    @HopDongChiTietREF INT ,
                    @DmHinhThucQuangCaoREF INT ,
                    @DmSanPhamREF INT ,
                    @DmWebsiteREF INT ,
                    @GiaTien INT ,
                    @SoLuong INT

                DECLARE icursor CURSOR
                FOR
                    SELECT  ThucChayHopDongChiTietPRID ,
                            HopDongREF ,
                            ChietKhau ,
                            ThucChayHopDongChiTietPrREF ,
                            HopDongChiTietREF ,
                            DmHinhThucQuangCaoREF ,
                            DmSanPhamREF ,
                            DmWebsiteREF ,
                            GiaTien ,
                            SoLuong
                    FROM    dbo.ThucChayHopDongChiTietPR
                    WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                            AND RecordStatus = 0
                            AND DeletedStatus <> 1
                            AND DmHinhThucQuangCaoREF <> 0
                            AND DmSanPhamREF <> 0
                            AND ThoiGianBatDau >= '2014-01-01'


                OPEN icursor;  

                FETCH NEXT FROM icursor   
				INTO @ThucChayHopDongChiTietPRID_, @HopDongREF, @ChietKhau,
                    @ThucChayHopDongChiTietPrREF, @HopDongChiTietREF,
                    @DmHinhThucQuangCaoREF, @DmSanPhamREF, @DmWebsiteREF,
                    @GiaTien, @SoLuong

				-- Lấy danh sách HopDongChiTietID
                WHILE @@FETCH_STATUS = 0
                    BEGIN  
                     
                        BEGIN
                            INSERT  INTO @Temp
                                    SELECT  *
                                    FROM    fn_TC_GetHopDongChiTietID_PR(@ThucChayHopDongChiTietPRID_,
                                                              @HopDongREF,
                                                              @ChietKhau,
                                                              @ThucChayHopDongChiTietPrREF,
                                                              @HopDongChiTietREF,
                                                              @DmHinhThucQuangCaoREF,
                                                              @DmSanPhamREF,
                                                              @DmWebsiteREF,
                                                              @GiaTien,
                                                              @SoLuong);
                        END;
						
	 
                        FETCH NEXT FROM icursor   
						INTO @ThucChayHopDongChiTietPRID_, @HopDongREF,
                            @ChietKhau, @ThucChayHopDongChiTietPrREF,
                            @HopDongChiTietREF, @DmHinhThucQuangCaoREF,
                            @DmSanPhamREF, @DmWebsiteREF, @GiaTien, @SoLuong
                    END;   
                CLOSE icursor;  
                DEALLOCATE icursor;  


                --SELECT  *
                --FROM    @Temp;

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
                                            hd.TenDiaDiemLamViec ,
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
                                            @NoteThongTinThayDoi DotChayHopDong ,
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
                                            0 AS SoLuongThucChay ,
                                            @NgaythucHien AS NgayThucHien ,
                                            ISNULL(tchpctpr.GiaTien, 0)
                                            * ISNULL(tchpctpr.SoLuong, 0)
                                            * ( CONVERT(FLOAT, ( 100
                                                              - tchpctpr.ChietKhau ))
                                                / 100 ) AS GiaTriThayDoi ,
                                            0 ThanhTienThucChayTruocChietKhau ,
                                            0 GiaTriTrietKhauThucChay ,
                                            0 ThanhTienThucChaySauChietKhau ,
                                            0 GiaTriHoaHongThucChay ,
                                            0 ThanhTienThucThu ,
                                            0 ThanhTienKM ,
                                            0 SoLuongThucChayKM ,
                                            0 SoLuongLechTreoHa ,
                                            0 ThanhTienLechTreoHa ,
                                            GETDATE() CreatedAt ,
                                            GETDATE() LastModifiedAt ,
                                            0 IsPheDuyet ,
                                            '' PheDuyetBy ,
                                            '' PheDuyetAt ,
                                            ( CASE WHEN tchpctpr.KhuyenMai = 0
                                                        AND tchpctpr.ChietKhau <> 100
                                                   THEN ISNULL(tchpctpr.SoLuong,
                                                              0)
                                                   ELSE 0
                                              END ) SoLuongThayDoi ,
                                            ( CASE WHEN tchpctpr.KhuyenMai = 1
                                                        OR tchpctpr.ChietKhau = 100
                                                   THEN ISNULL(tchpctpr.SoLuong,
                                                              0)
                                                   ELSE 0
                                              END ) SoLuongKMThayDoi ,
                                            ( CASE WHEN tchpctpr.KhuyenMai = 1
                                                        OR tchpctpr.ChietKhau = 100
                                                   THEN ISNULL(tchpctpr.GiaTien,
                                                              0)
                                                        * ISNULL(tchpctpr.SoLuong,
                                                              0)
                                                   ELSE 0
                                              END ) GiaTriKMThayDoi ,
                                            @GhiChu GhiChu
                                  FROM      ( SELECT    tchpctpr.* ,
                                                        T.HopDongChiTietID HopDongChiTietID
                                              FROM      dbo.ThucChayHopDongChiTietPR tchpctpr
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
                                                              ISNULL(D.TenBoPhan,
                                                              '') AS TenBoPhan ,
                                                              D.DmNhomLamViecREF ,
                                                              ISNULL(D.TenNhom,
                                                              '') AS TenNhom ,
                                                              D.DmDiaDiemLamViecREF ,
                                                              D.TenDiaDiemLamViec ,
                                                              D.SysNhanVienREF ,
                                                              ISNULL(D.TenDangNhap,
                                                              '') AS TenDangNhap ,
                                                              D.TenNhanVien ,
                                                              D.TenKhachHang
                                                         FROM dbo.HopDong D
                                                         WHERE
                                                              D.TrangThaiHopDong <> 3
                                                              AND D.Nam >= 2013
                                                       ) hd ON tchpctpr.HopDongREF = hd.HopDongID
                                            INNER JOIN dbo.HopDongChiTiet hdct ON tchpctpr.HopDongChiTietID = hdct.HopDongChiTietID
                                                              AND hdct.DmLoaiREF = tchpctpr.DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = tchpctpr.DmSanPhamREF
                          
        --AND hd.HopDongID = 501482; 
                                ) T;    
								
								
								
								
								
								
                IF EXISTS ( SELECT  tchpctpr.* ,
                                    T.HopDongChiTietID HopDongChiTietID
                            FROM    ThucChayHopDongChiTietPR tchpctpr
                                    INNER JOIN @Temp T ON tchpctpr.ThucChayHopDongChiTietPRID = T.ThucChayHopDongChiTietPRID
                            WHERE   tchpctpr.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID )
                    BEGIN
                        UPDATE  dbo.ThucChayHopDongChiTietPR
                        SET     RecordStatus = 1
                        WHERE    HopDongREF = @HopDongID 
						AND ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
                               


                        IF NOT EXISTS ( SELECT  *
                                        FROM    dbo.ThucChay_ThongTinHopDongChiTietID_PR
                                        WHERE   ThucChayHopDongChiTietPRID IN (
                                                SELECT  t.ThucChayHopDongChiTietPRID
                                                FROM    @Temp t ) )
                            BEGIN
                                INSERT  INTO dbo.ThucChay_ThongTinHopDongChiTietID_PR
                                        SELECT  t.HopDongChiTietID ,
                                                t.ThucChayHopDongChiTietPRID
                                        FROM    @Temp t
                            END
                    END
			
                DELETE  FROM @Temp
			  
            END
	

    END




--EXEC [ThucChay_InsertThucChayDaTinh_PR] '2013-07-01','2013-07-11'

```
