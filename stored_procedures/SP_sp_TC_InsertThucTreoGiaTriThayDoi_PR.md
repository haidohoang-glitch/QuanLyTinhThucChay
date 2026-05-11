# Stored Procedure: `sp_TC_InsertThucTreoGiaTriThayDoi_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 16:00:09.840000
- **Ngày sửa cuối**: 2017-06-17 19:24:43.653000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@SoLuongThayDoi` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_PR]


CREATE PROCEDURE [dbo].[sp_TC_InsertThucTreoGiaTriThayDoi_PR]
    @ThucChayHopDongChiTietPRID INT ,
    @NgaythucHien DATETIME ,
    @GiaTriThayDoi FLOAT ,
    @SoLuongThayDoi INT
AS
    BEGIN
        DECLARE @NgayGioiHanTinh DATETIME;
        SET @NgayGioiHanTinh = '2014-01-01';
	
        PRINT @ThucChayHopDongChiTietPRID;
	
	
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
            @GiaTien INT,
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
                    GiaTien,
					SoLuong
            FROM    ThucChayHopDongChiTietPR
            WHERE   ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID;


        OPEN icursor;  

        FETCH NEXT FROM icursor   
				INTO @ThucChayHopDongChiTietPRID_, @HopDongREF, @ChietKhau,
            @ThucChayHopDongChiTietPrREF, @HopDongChiTietREF,
            @DmHinhThucQuangCaoREF, @DmSanPhamREF, @DmWebsiteREF, @GiaTien,@SoLuong


		-- Lấy danh sách HopDongChiTietID 
        WHILE @@FETCH_STATUS = 0
            BEGIN  
    
                        --IF NOT EXISTS ( SELECT  HopDongChiTietID
                        --                FROM    @Temp
                        --                WHERE   HopDongChiTietID IN (
                        --                        SELECT  HopDongChiTietID
                        --                        FROM    fn_Get_HopDongChiTietID_For_PR_v2_VTung(@ThucChayHopDongChiTietPRID,
                        --                                      @HopDongREF,
                        --                                      @ChietKhau,
                        --                                      @ThucChayHopDongChiTietPrREF,
                        --                                      @HopDongChiTietREF,
                        --                                      @DmHinhThucQuangCaoREF,
                        --                                      @DmSanPhamREF,
                        --                                      @DmWebsiteREF,
                        --                                      @GiaTien) ) )
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
                    @HopDongChiTietREF, @DmHinhThucQuangCaoREF, @DmSanPhamREF,
                    @DmWebsiteREF, @GiaTien, @SoLuong
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
                                    0 AS SoLuongThucChay ,
                                    @NgaythucHien AS NgayThucHien ,
                                    @GiaTriThayDoi AS GiaTriThayDoi ,
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
                                    @SoLuongThayDoi SoLuongThayDoi ,
                                    0 SoLuongKMThayDoi ,
                                    0 GiaTriKMThayDoi ,
                                    N'Thay doi gia tri' GhiChu
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
                          
        --AND hd.HopDongID = 501482; 
                        ) T;            

    END;




--EXEC [ThucChay_InsertThucChayDaTinh_PR] '2013-07-01','2013-07-11'

```
