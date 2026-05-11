# Stored Procedure: `sp_TC_TinhLaiGiaTriThayDoi_ThucChayDaTinh_PR_ByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-19 11:44:49.633000
- **Ngày sửa cuối**: 2018-09-11 16:24:14.030000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@pHopDongID` | `int(4)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[sp_TC_TinhLaiGiaTriThayDoi_ThucChayDaTinh_PR_ByHopDongID]
    '2018-09-10' ,
    '2018-09-10''  ,
	'2018-09-10'' ,
	637,
    1000953,
	''
*/


CREATE PROCEDURE [dbo].[sp_TC_TinhLaiGiaTriThayDoi_ThucChayDaTinh_PR_ByHopDongID]
    @StartDate DATETIME ,
    @EndDate DATETIME ,
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT,
    @pHopDongID INT = NULL,
	@GhiChu NVARCHAR(1000)
AS
    BEGIN

        DECLARE  @NgayGioiHanTinh DATETIME;
        SET @NgayGioiHanTinh = '2014-01-01';
	

                DECLARE @Temp TABLE
                    (
                      HopDongChiTietID INT ,
                      ThucChayHopDongChiTietPRID INT
                    );


                DECLARE @ThucChayHopDongChiTietPRID INT ,
                    @HopDongREF INT ,
                    @ChietKhau FLOAT ,
                    @ThucChayHopDongChiTietPrREF INT ,
                    @HopDongChiTietREF INT ,
                    @DmHinhThucQuangCaoREF INT ,
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
                    WHERE   DeletedStatus <> 1
							AND HopDongREF = @pHopDongID
							AND DmSanPhamREF = @DmSanPhamREF
                            AND RecordStatus = 0
                            AND DmHinhThucQuangCaoREF <> 0
                            AND ThoiGianBatDau >= '2014-01-01'
                            AND ( CASE WHEN CreatedAt >= LastModifiedAt
                                       THEN CONVERT(DATE, CreatedAt)
                                       ELSE CONVERT(DATE, LastModifiedAt)
                                  END ) <= @EndDate

                OPEN icursor;  

                FETCH NEXT FROM icursor   
				INTO @ThucChayHopDongChiTietPRID, @HopDongREF, @ChietKhau,
                    @ThucChayHopDongChiTietPrREF, @HopDongChiTietREF,
                    @DmHinhThucQuangCaoREF, @DmSanPhamREF, @DmWebsiteREF,
                    @GiaTien, @SoLuong

                WHILE @@FETCH_STATUS = 0
                    BEGIN  
                        BEGIN
                            INSERT  INTO @Temp
                                    SELECT  *
                                    FROM    dbo.fn_TC_GetHopDongChiTietID_PR(@ThucChayHopDongChiTietPRID,
                                                              @HopDongREF,
                                                              @ChietKhau,
                                                              @ThucChayHopDongChiTietPrREF,
                                                              @HopDongChiTietREF,
                                                              @DmHinhThucQuangCaoREF,
                                                              @DmSanPhamREF,
                                                              @DmWebsiteREF,
                                                              @GiaTien,
                                                              @SoLuong);



							SELECT * FROM @Temp

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
                                    SELECT  NEWID() ,
                                            T.HopDongID ,T.SoHopDong ,T.DmMaHopDongREF ,T.TenMaHopDong ,
                                            T.NgayDanhSoHopDong ,T.NgayKyHopDong ,T.NhanHopDong ,T.NgayNhanBanFax ,T.NgayNhanHopDongBanCung ,
                                            T.NgayChuyenHopDongChoKeToan ,
                                            T.So ,T.Thang ,T.Nam , 
                                            T.GiaTriHopDong ,T.CongNo ,T.HopDongChiTietID ,
                                            T.DangSuDung ,
                                            T.IsGiayPhep ,
                                            T.TrangThaiHopDong ,
                                            T.IsBanCung , 
                                            T.DmPhongBanREF ,
                                            T.TenPhongBan ,
                                            T.DmBoPhanREF ,
                                            T.TenBoPhan ,
                                            T.DmNhomLamViecREF ,
                                            T.TenNhom ,
                                            T.DmDiaDiemLamViecREF ,
                                            T.TenDiaDiemLamViec ,
                                            T.SysNhanVienREF ,
                                            T.TenDangNhap ,
                                            T.TenNhanVien ,
                                            T.TenKhachHang ,
                                            T.NhanHang ,
                                            T.DmNhomNganhREF ,
                                            T.TenNhomNganh , 
											T.DmHinhThucQuangCao ,
											T.TenHinhThucQuangCao , 
											T.DmSanPhamREF ,
											T.TenSanPham ,
											T.DmNhomWebsiteREF ,
											T.TenNhomWebsite ,
											T.DmChuyenMucREF ,
											T.TenChuyenMuc ,
											T.DmLoaiBannerREF ,
											T.TenLoaiBanner ,
											T.DmViTriREF ,
											T.TenViTri ,
											T.DotChayHopDong ,
											T.SoLuongDotChayHD ,
											T.DotChayBooking ,
											T.SoLuongDotChayBooking , 
											T.SoLuong ,
											T.DonViTinh ,
											T.DonGia ,
											T.DonGiaTheoDonViTinh ,
											T.ChietKhau ,
											T.GiamGia ,
											T.ThanhTien ,
											T.TiLeTuVan ,
											T.ChiPhiTuVan ,
											T.IsKhuyenMai ,
											T.KhuyenMai ,
											T.DmBannerREF ,
											T.DmChienDichREF ,
											T.DmWebsiteREF ,
											T.TenWebsite ,
											T.TongViewThucChay ,
											T.TongClickThucChay ,
											T.TongSoBaiViet ,
											T.SoLuongThucChay ,
											T.NgayThucHien ,
											T.GiaTriThayDoi ,
											T.ThanhTienThucChayTruocChietKhau ,
											T.GiaTriTrietKhauThucChay ,
											T.ThanhTienThucChaySauChietKhau ,
											T.GiaTriHoaHongThucChay ,
											T.ThanhTienThucThu ,
											T.ThanhTienKM ,
											T.SoLuongThucChayKM ,
											T.SoLuongLechTreoHa ,
											T.ThanhTienLechTreoHa ,
											T.CreatedAt ,
											T.LastModifiedAt ,
											T.IsPheDuyet ,
											T.PheDuyetBy ,
											T.PheDuyetAt ,
											T.SoLuongThayDoi ,
											T.SoLuongKMThayDoi ,
											T.GiaTriKMThayDoi ,
											T.GhiChu
                                    FROM    ( SELECT  DISTINCT
                                                        hd.HopDongID ,
                                                        hd.SoHopDong ,
                                                        hd.DmMaHopDongREF ,
                                                        hd.TenMaHopDong ,
                                                        hd.NgayDanhSoHopDong ,
                                                        hd.NgayKyHopDong ,
                                                        ISNULL(hd.NhanHopDong,
                                                              '') AS NhanHopDong ,
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
                                                        ISNULL(hd.TenPhongBan,
                                                              '') AS TenPhongBan ,
                                                        hd.DmBoPhanREF ,
                                                        ISNULL(hd.TenBoPhan,
                                                              '') AS TenBoPhan ,
                                                        hd.DmNhomLamViecREF ,
                                                        ISNULL(hd.TenNhom, '') AS TenNhom ,
                                                        hd.DmDiaDiemLamViecREF ,
                                                        ISNULL(hd.TenDiaDiemLamViec,
                                                              '') AS TenDiaDiemLamViec ,
                                                        hd.SysNhanVienREF ,
                                                        ISNULL(hd.TenDangNhap,
                                                              '') AS TenDangNhap ,
                                                        hd.TenNhanVien ,
                                                        hd.TenKhachHang ,
                                                        tchpctpr.DmNhanHangREF AS NhanHang ,
                                                        0 DmNhomNganhREF ,
                                                        '' TenNhomNganh , 
		                                                hdct.DmLoaiREF AS DmHinhThucQuangCao ,
                                                        hdct.TenLoai AS TenHinhThucQuangCao , 
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
		                                                tchpctpr.ThucChayHopDongChiTietPRID DotChayBooking ,
                                                        0 AS SoLuongDotChayBooking , 
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
		                                                0 DmBannerREF ,--A.DmBannerREF,
                                                        0 DmChienDichREF ,--A.DmChienDichREF,
                                                        dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(tchpctpr.DmWebsiteREF) DmWebsiteREF ,
                                                        dbo.GetWebsiteLinkByDmWebsiteID(tchpctpr.DmWebsiteREF,
                                                              tchpctpr.TenWebsite) TenWebsite ,
                                                        0 TongViewThucChay ,
                                                        0 TongClickThucChay ,
                                                        0 TongSoBaiViet ,
                                                        ( CASE
                                                              WHEN tchpctpr.KhuyenMai = 0
                                                              AND tchpctpr.ChietKhau <> 100
                                                              THEN ISNULL(tchpctpr.SoLuong,
                                                              0)
                                                              ELSE 0
                                                          END ) AS SoLuongThucChay ,
                                                        @NgayThucHien AS NgayThucHien ,
                                                        0 AS GiaTriThayDoi ,
                                                        ISNULL(tchpctpr.GiaTien,
                                                              0)
                                                        * ISNULL(tchpctpr.SoLuong,
                                                              0) AS ThanhTienThucChayTruocChietKhau ,
                                                        ISNULL(( CONVERT(FLOAT, ISNULL(tchpctpr.GiaTien,
                                                              0))
                                                              * CONVERT(FLOAT, ISNULL(tchpctpr.SoLuong,
                                                              0))
                                                              * CONVERT(FLOAT, tchpctpr.ChietKhau) )
                                                              / 100, 0) AS GiaTriTrietKhauThucChay ,
                                                        ISNULL(tchpctpr.GiaTien,
                                                              0)
                                                        * ISNULL(tchpctpr.SoLuong,
                                                              0)
                                                        * ( CONVERT(FLOAT, ( 100
                                                              - tchpctpr.ChietKhau ))
                                                            / 100 ) AS ThanhTienThucChaySauChietKhau ,
                                                        ( CONVERT(FLOAT, ( 100
                                                              - tchpctpr.ChietKhau ))
                                                          * CONVERT(FLOAT, ( ISNULL(tchpctpr.GiaTien,
                                                              0)
                                                              * ISNULL(tchpctpr.SoLuong,
                                                              0) )) / 100 )
                                                        * ISNULL(hdct.TiLeTuVan,
                                                              0) / 100 AS GiaTriHoaHongThucChay ,
                                                        ( CASE
                                                              WHEN ( tchpctpr.KhuyenMai = 1
                                                              OR tchpctpr.ChietKhau = 100
                                                              OR tchpctpr.GiaTien = 0
                                                              OR tchpctpr.SoLuong = 0
                                                              ) THEN 0
                                                              ELSE ( 100
                                                              - hdct.TiLeTuVan )
                                                              / ( ISNULL(tchpctpr.GiaTien,
                                                              0)
                                                              * ISNULL(tchpctpr.SoLuong,
                                                              0)
                                                              * ( CONVERT(FLOAT, ( 100
                                                              - tchpctpr.ChietKhau ))
                                                              / 100 ) )
                                                          END ) AS ThanhTienThucThu ,
                                                        ( CASE
                                                              WHEN tchpctpr.KhuyenMai = 1
                                                              OR tchpctpr.ChietKhau = 100
                                                              THEN ISNULL(tchpctpr.GiaTien,
                                                              0)
                                                              * ISNULL(tchpctpr.SoLuong,
                                                              0)
                                                              ELSE 0
                                                          END ) AS ThanhTienKM ,
                                                        ( CASE
                                                              WHEN tchpctpr.KhuyenMai = 1
                                                              OR tchpctpr.ChietKhau = 100
                                                              THEN ISNULL(tchpctpr.SoLuong,
                                                              0)
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
                                                        @GhiChu GhiChu
                                              FROM      ( SELECT
                                                              tchpctpr.* ,
                                                              T.HopDongChiTietID HopDongChiTietID 
                                                          FROM
                                                             (SELECT * FROM  dbo.ThucChayHopDongChiTietPR WHERE HopDongREF = @pHopDongID) tchpctpr
                                                              INNER JOIN @Temp T ON tchpctpr.ThucChayHopDongChiTietPRID = T.ThucChayHopDongChiTietPRID
                                                        ) tchpctpr
                                                        INNER JOIN ( SELECT
                                                              D.HopDongID ,
				                                              D.SoHopDong ,
                                                              D.DmMaHopDongREF ,
                                                              D.TenMaHopDong , 
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
				                                              D.GiaTriHopDong ,
                                                              D.CongNo ,
				                                              D.DangSuDung ,
                                                              D.IsGiayPhep ,
                                                              D.TrangThaiHopDong ,
                                                              D.IsBanCung , 
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
                                                              WHERE D.TrangThaiHopDong <> 3
																  AND D.Nam >= 2013
																  AND D.HopDongID = @pHopDongID
                                                              ) hd ON tchpctpr.HopDongREF = hd.HopDongID
                                                        INNER JOIN (SELECT * FROM dbo.HopDongChiTiet WHERE HopDongFK = @pHopDongID) hdct ON tchpctpr.HopDongChiTietID = hdct.HopDongChiTietID
                                                              AND hdct.DmLoaiREF = tchpctpr.DmHinhThucQuangCaoREF
                                                              AND hdct.DmSanPhamREF = tchpctpr.DmSanPhamREF
                                            ) T;            
	

				
				-- Insert HopDongChiTietID vao bang de dung khi tinh thay doi

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

                            DELETE  FROM @Temp;
                        END;
	 
                        FETCH NEXT FROM icursor   
						INTO @ThucChayHopDongChiTietPRID, @HopDongREF,
                            @ChietKhau, @ThucChayHopDongChiTietPrREF,
                            @HopDongChiTietREF, @DmHinhThucQuangCaoREF,
                            @DmSanPhamREF, @DmWebsiteREF, @GiaTien, @SoLuong
                    END;   
                CLOSE icursor;  
                DEALLOCATE icursor;  


                EXEC [dbo].[sp_TC_UpdateRecordStatus_ThucChayHopDongChiTietPR_NotBy_NgayThucHien]  @NgayThucHien, @pHopDongID , @DmSanPhamREF  
     
  END;


```
