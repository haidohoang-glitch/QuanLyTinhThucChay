# Stored Procedure: `sp_TC_UpdateGiaTriTDTCMobileThucTreoByNgayLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-23 17:58:49.980000
- **Ngày sửa cuối**: 2017-06-23 17:58:49.980000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@CONTENT_LOG` | `nvarchar(1000)` | No |
| `@DmBannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_TC_UpdateGiaTriTDTCMobileThucTreoByNgayLog] 
-- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME ,
    @HopDongREF INT ,
    @DmSanPhamID INT ,
    @HopDongChiTietREF INT ,
    @CONTENT_LOG NVARCHAR(500) ,
    @DmBannerID INT
AS
    BEGIN
        DECLARE @MinDate DATETIME ,
            @SoLuongLechTreoHa BIGINT ,
            @SoLuongThucChayDuocTinh BIGINT
	
        DECLARE @SoLuongThucChay BIGINT ,
            @SoLuongHopDong BIGINT ,
            @TTChenhLechDuocTinh FLOAT ,
            @SoLuongChenhLechDuocTinh INT
	
        DECLARE @count_HDCT INT ,
            @DonGiaTheoDonViTinh FLOAT ,
            @TTThucChaySauChietKhau FLOAT ,
            @GiaTriThayDoi FLOAT ,
            @TongTienThucChay FLOAT ,
            @TongTienHopDong BIGINT ,
            @IsHDFinish INT ,
            @TongSLThucChay INT
	
        SET @TongTienHopDong = 0
        SET @IsHDFinish = 0
        SET @count_HDCT = 0
        SET @SoLuongLechTreoHa = 0
        SET @SoLuongThucChayDuocTinh = 0
        SET @SoLuongThucChay = 0
        SET @SoLuongHopDong = 0
        SET @DonGiaTheoDonViTinh = 0
        SET @TTThucChaySauChietKhau = 0
        SET @GiaTriThayDoi = 0
        SET @TTChenhLechDuocTinh = 0
        SET @TongTienThucChay = 0
        SET @TongSLThucChay = 0
	
        IF ( @count_HDCT = 0 )--T/c tinh theo phuong phap thuc treo
            BEGIN
                SET @MinDate = ( SELECT MIN(tcdt.NgayThucHien)
                                 FROM   ThucChayDaTinh tcdt
                                 WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                        AND tcdt.DmSanPhamREF = @DmSanPhamID
                                        AND tcdt.HopDongID = @HopDongREF
                                        AND tcdt.DmBannerREF = @DmBannerID
                               )
	    

                SET @MinDate = ISNULL(@MinDate, GETDATE())


                IF ( CONVERT(DATE, @MinDate) < CONVERT(DATE, @NgayThucHien) )
                    BEGIN
	        --Tinh s/l thuc chay 
                        SET @SoLuongThucChay = ( SELECT SUM(tcdt.SoLuongThucChay)
                                                        + SUM(tcdt.SoLuongThayDoi)
                                                 FROM   ThucChayDaTinh tcdt
                                                 WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                                        AND tcdt.DmSanPhamREF = @DmSanPhamID
                                                        AND tcdt.HopDongID = @HopDongREF
                                                        AND tcdt.NgayThucHien BETWEEN @MinDate
                                                              AND
                                                              @NgayThucHien
                                                        AND tcdt.DmBannerREF = @DmBannerID
                                               )
	        
                        SET @SoLuongThucChay = ISNULL(@SoLuongThucChay, 0)
	        --Tinh s/l HopDong
                        SET @SoLuongHopDong = ( SELECT  hdct.SoLuong
                                                        * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
                                                FROM    HopDongChiTiet hdct
                                                WHERE   hdct.HopDongChiTietID = @HopDongChiTietREF
                                                        AND hdct.DeletedStatus = 0
                                              )
	        --Tinh DonGiaTheoDonViTinh sau chiet khau
                        SET @DonGiaTheoDonViTinh = ( SELECT ( hdct.DonGia
                                                              / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh) )
                                                            * ( 100
                                                              - hdct.ChietKhau )
                                                            / 100
                                                     FROM   HopDongChiTiet hdct
                                                     WHERE  hdct.HopDongChiTietID = @HopDongChiTietREF
                                                            AND hdct.DmSanPhamREF = @DmSanPhamID
                                                            AND hdct.DeletedStatus = 0
                                                   )
	        
                        SET @DonGiaTheoDonViTinh = ISNULL(@DonGiaTheoDonViTinh,
                                                          0)
	        
	        --Tinh Tong tien t/c sau chiet khau, Gia tri thay doi
                        SELECT  @TTThucChaySauChietKhau = SUM(tcdt.ThanhTienSauTrietKhauThucChay) ,
                                @GiaTriThayDoi = SUM(tcdt.GiaTriThayDoi)
                        FROM    ThucChayDaTinh tcdt
                        WHERE   tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                AND tcdt.DmSanPhamREF = @DmSanPhamID
                                AND tcdt.HopDongID = @HopDongREF
                                AND tcdt.NgayThucHien BETWEEN @MinDate
                                                      AND     @NgayThucHien
                                AND tcdt.DmBannerREF = @DmBannerID


                        SET @TTThucChaySauChietKhau = ISNULL(@TTThucChaySauChietKhau,
                                                             0)
                        SET @GiaTriThayDoi = ISNULL(@GiaTriThayDoi, 0)
				
	        
	        --CHECK TINH S./L THUCCHAY DUOC TINH
                        IF ( @SoLuongThucChay > 0
                             AND @SoLuongThucChay < @SoLuongHopDong
                           )
                            BEGIN
	            --Tinh s/l LechTreoHa
                                SET @SoLuongLechTreoHa = ( SELECT
                                                              SUM(tcdt.SoLuongThucChayLechTreoHa)
                                                           FROM
                                                              ThucChayDaTinh tcdt
                                                           WHERE
                                                              tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                                              AND tcdt.DmSanPhamREF = @DmSanPhamID
                                                              AND tcdt.HopDongID = @HopDongREF
                                                              AND tcdt.NgayThucHien BETWEEN @MinDate
                                                              AND
                                                              @NgayThucHien
                                                              AND tcdt.DmBannerREF = @DmBannerID
                                                         )
	            
                                SET @SoLuongLechTreoHa = ISNULL(@SoLuongLechTreoHa,
                                                              0)
                                IF ( ( @SoLuongLechTreoHa > 0 )
                                     AND ( @SoLuongThucChay
                                           + @SoLuongLechTreoHa <= @SoLuongHopDong )
                                   )
                                    BEGIN
                                        SET @SoLuongThucChayDuocTinh = @SoLuongThucChay
                                            + @SoLuongLechTreoHa
                                    END
                                ELSE
                                    IF ( ( @SoLuongLechTreoHa > 0 )
                                         AND ( @SoLuongThucChay
                                               + @SoLuongLechTreoHa > @SoLuongHopDong )
                                       )
                                        BEGIN
                                            SET @SoLuongThucChayDuocTinh = ( @SoLuongThucChay
                                                              + @SoLuongLechTreoHa )
                                                - ( ( @SoLuongThucChay
                                                      + @SoLuongLechTreoHa )
                                                    - @SoLuongHopDong )
                                        END
                                    ELSE
                                        IF ( @SoLuongLechTreoHa <= 0 )
                                            BEGIN
                                                SET @SoLuongThucChayDuocTinh = @SoLuongThucChay
                                            END
                                SET @TTChenhLechDuocTinh = ( @SoLuongThucChayDuocTinh
                                                             * @DonGiaTheoDonViTinh )
                                    - ( @TTThucChaySauChietKhau
                                        + @GiaTriThayDoi )

                                SET @SoLuongChenhLechDuocTinh = @SoLuongThucChayDuocTinh
                                    - @SoLuongThucChay
                            END
	        --
	        --   
                        IF ( @SoLuongThucChay >= @SoLuongHopDong )
                            BEGIN
                                SET @IsHDFinish = 1
                                SET @TongTienHopDong = ( SELECT
                                                              SUM(hdct.ThanhTien)
                                                         FROM HopDongChiTiet hdct
                                                         WHERE
                                                              hdct.HopDongFK = @HopDongREF
                                                              AND hdct.HopDongChiTietID = @HopDongChiTietREF
                                                              AND hdct.DmSanPhamREF = @DmSanPhamID
                                                              AND hdct.DeletedStatus = 0
                                                              AND hdct.ChietKhau <> 100
                                                       )           
                                SET @TTChenhLechDuocTinh = @TongTienHopDong
                                    - ( @TTThucChaySauChietKhau
                                        + @GiaTriThayDoi )

                                SET @SoLuongChenhLechDuocTinh = @SoLuongHopDong
                                    - @SoLuongThucChay

                                SET @IsHDFinish = 1
                            END

                        IF ( @TTThucChaySauChietKhau + @GiaTriThayDoi = 0 )
                            BEGIN
                                SET @TongTienThucChay = @TTChenhLechDuocTinh
                                SET @TongSLThucChay = @SoLuongThucChayDuocTinh
                            END
				
                        ELSE
                            BEGIN
                                SET @TongTienThucChay = @TTThucChaySauChietKhau
                                    + @GiaTriThayDoi
                                SET @TongSLThucChay = @SoLuongThucChay
                            END
				
                        IF ( @TongTienThucChay = 0 )
                            SET @TongTienThucChay = 1
                        IF @TongSLThucChay = 0
                            SET @TongSLThucChay = 1
				
                        PRINT 'Thanh tien chenh lech :'
                            + CONVERT(NVARCHAR(50), @TTChenhLechDuocTinh)    


                        PRINT @HopDongChiTietREF	
						
						        
                        IF ( @TTChenhLechDuocTinh != 0 )
                            BEGIN
                                PRINT '1'
                                PRINT '@TongTienThucChay: '
                                    + CONVERT(NVARCHAR(50), @TongTienThucChay)     
                                PRINT '@TTChenhLechDuocTinh: '
                                    + CONVERT(NVARCHAR(50), @TTChenhLechDuocTinh)    
                                INSERT  INTO ThucChayDaTinh
                                        SELECT  NEWID() ,
                                                TD.HopDongID ,
                                                TD.SoHopDong ,
                                                TD.DmMaHopDongREF ,
                                                TD.TenMaHopDong ,
                                                TD.NgayDanhSoHopDong ,
                                                TD.NgayKyHopDong ,
                                                TD.NhanHopDong ,
                                                TD.NgayNhanBanFax ,
                                                TD.NgayNhanHopDongBanCung ,
                                                TD.NgayChuyenHopDongChoKeToan ,
                                                TD.So ,
                                                TD.Thang ,
                                                TD.Nam ,
                                                TD.GiaTriHopDong ,
                                                TD.CongNo ,
                                                TD.HopDongChiTietREF ,
                                                TD.DangSuDung ,
                                                TD.IsGiayPhep ,
                                                TD.TrangThaiHopDong ,
                                                TD.IsBanCung ,
                                                TD.DmPhongBanREF ,
                                                TD.TenPhongBan ,
                                                TD.DmBoPhanREF ,
                                                TD.TenBoPhan ,
                                                TD.DmNhomLamViecREF ,
                                                TD.TenNhom ,
                                                TD.DmDiaDiemLamViecREF ,
                                                TD.TenDiaDiemLamViec ,
                                                TD.SysNhanVienREF ,
                                                TD.TenDangNhap ,
                                                TD.TenNhanVien ,
                                                TD.TenKhachHang ,
                                                TD.NhanHang ,
                                                TD.DmNhomNganhREF ,
                                                TD.TenNhomNganh ,
                                                TD.DmHinhThucQuangCao ,
                                                TD.TenHinhThucQuangCao ,
                                                TD.DmSanPhamREF ,
                                                TD.TenSanPham ,
                                                TD.DmNhomWebsiteREF ,
                                                TD.TenNhomWebsite ,
                                                TD.DmChuyenMucREF ,
                                                TD.TenChuyenMuc ,
                                                TD.DmLoaiBannerREF ,
                                                TD.TenLoaiBanner ,
                                                TD.DmViTriREF ,
                                                TD.TenViTri ,
                                                TD.DotChayHopDong ,
                                                TD.SoLuongDotChayHD ,
                                                TD.DotChayBooking ,
                                                TD.SoLuongDotChayBooking ,
                                                TD.SoLuong ,
                                                TD.DonViTinh ,
                                                TD.DonGia ,
                                                TD.DonGiaTheoDonViTinh ,
                                                TD.ChietKhau ,
                                                TD.GiamGia ,
                                                TD.ThanhTien ,
                                                TD.TiLeTuVan ,
                                                TD.ChiPhiTuVan ,
                                                TD.IsKhuyenMai ,
                                                TD.KhuyenMai ,
                                                TD.DmBannerREF ,
                                                TD.DmChienDichREF ,
                                                TD.DmWebsiteREF ,
                                                TD.TenWebsite ,
                                                TD.TongViewThucChay ,
                                                TD.TongClickThucChay ,
                                                TD.TongSoBaiViet ,
                                                TD.SoLuongThucChay ,
                                                TD.NgayThucHien ,
                                                TD.GiaTriThayDoi ,
                                                TD.ThanhTienThucChayTruocTrietKhau ,
                                                0 AS GiaTriTrietKhauThucChay ,
                                                0 AS ThanhTienSauTrietKhauThucChay ,
                                                0 AS GiaTriHoaHongThucChay ,
                                                0 AS ThanhTienThucThu ,
                                                0 AS ThanhTienKM ,
                                                0 AS SoLuongThucChayKM ,
                                                0 AS SoLuongLechTreoHa ,
                                                0 AS ThanhTienLechTreoHa ,
                                                GETDATE() ,
                                                GETDATE() ,
                                                0 IsPheDuyet ,
                                                '' PheDuyetBy ,
                                                '' PheDuyetAt ,
                                                TD.SoLuongThayDoi SoLuongThayDoi ,
                                                0 SoLuongKMThayDoi ,
                                                0 GiaTriKMThayDoi ,
                                                '' GhiChu
                                        FROM    ( SELECT --ID Hop Dong
                                                            D.HopDongID ,
	                              --Thong tin ve ma so 
                                                            D.SoHopDong ,
                                                            D.DmMaHopDongREF ,
                                                            D.TenMaHopDong ,
	                              --Thong tin ve thoi gian
                                                            D.NgayDanhSoHopDong ,
                                                            D.NgayKyHopDong ,
                                                            D.NhanHopDong ,
                                                            D.NgayNhanBanFax ,
                                                            D.NgayNhanHopDongBanCung ,
                                                            D.NgayChuyenHopDongChoKeToan ,
                                                            D.So ,
                                                            D.Thang ,
                                                            D.Nam ,
	                              --Thong tin ve gia tri
                                                            D.GiaTriHopDong ,
                                                            D.CongNo ,
	                              --Thong tin chi tiet phan bo
                                                            A.HopDongChiTietREF ,
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
	                              --Thong tin ve khach hang
	                              --D.DmKhachHangREF, 
                                                            D.TenKhachHang ,
                                                            [dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID,
                                                              @NgayThucHien) NhanHang ,
                                                            C.DmNhomNganhREF ,
                                                            C.TenNhomNganh ,
	                              --Thong tin hinh thuc quang cao
                                                            C.DmLoaiREF AS DmHinhThucQuangCao ,
                                                            C.TenLoai AS TenHinhThucQuangCao ,
	                              --Thong tin San pham
                                                            C.DmSanPhamREF AS DmSanPhamREF ,
                                                            C.TenSanPham AS TenSanPham ,
                                                            C.DmNhomWebsiteREF ,
                                                            C.TenNhomWebsite ,
	                              --C.DmWebsiteREF,
	                              --C.TenWebsite, 
                                                            C.DmChuyenMucREF ,
                                                            C.TenChuyenMuc ,
                                                            C.DmLoaiBannerREF ,
                                                            C.TenLoaiBanner ,
                                                            C.DmViTriREF ,
                                                            C.TenViTri ,
                                                            'Mobile_TTR' DotChayHopDong ,
                                                            C.SoLuong AS SoLuongDotChayHD ,
                                                            'PS THUC TREO Mobile' DotChayBooking ,
                                                            0 SoLuongDotChayBooking ,
                                                            C.SoLuong
                                                            * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
                                                            ( CASE
                                                              WHEN C.TenLoai IN (
                                                              'CPC', 'CPM' )
                                                              THEN dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh)
                                                              ELSE dbo.ThucChay_GetDonViTinhNotCPD(C.TenLoai)
                                                              END ) AS DonViTinh ,
                                                            dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,
                                                              A.HopDongChiTietREF,
                                                              C.DonGia) AS DonGia ,
                                                            ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,
                                                              C.DonViTinh,
                                                              C.DonGia,
                                                              D.NgayKyHopDong,
                                                              @NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                              0) AS DonGiaTheoDonViTinh ,
                                                            C.ChietKhau ,
                                                            C.GiamGia ,
                                                            C.ThanhTien ,
                                                            C.TiLeTuVan ,
                                                            C.ChiPhiTuVan ,
                                                            C.IsKhuyenMai ,
                                                            C.KhuyenMai ,
                                                            @DmBannerID DmBannerREF ,	--A.DmBannerREF,
                                                            0 DmChienDichREF ,	--A.DmChienDichREF,
                                                            A.DmWebsiteREF ,
                                                            A.TenWebsite ,
                                                            0 TongViewThucChay ,
                                                            0 TongClickThucChay ,
                                                            0 TongSoBaiViet ,
                                                            0 AS SoLuongThucChay ,
                                                            @NgayThucHien NgayThucHien ,
                                                            A.GiaTriThayDoi AS GiaTriThayDoi ,
                                                            0 AS ThanhTienThucChayTruocTrietKhau ,
                                                            A.SoLuongThayDoi SoLuongThayDoi
                                                  FROM      ( SELECT
                                                              tcdt.HopDongChiTietREF ,
                                                              tcdt.DmWebsiteREF ,
                                                              tcdt.TenWebsite ,
                                                              ( SUM(tcdt.ThanhTienSauTrietKhauThucChay
                                                              + tcdt.GiaTriThayDoi)
                                                              / @TongTienThucChay )
                                                              * @TTChenhLechDuocTinh GiaTriThayDoi ,
                                                              ( SUM(tcdt.SoLuong
                                                              + tcdt.SoLuongThayDoi)
                                                              / @TongSLThucChay )
                                                              * @SoLuongChenhLechDuocTinh SoLuongThayDoi
                                                              FROM
                                                              ThucChayDaTinh tcdt
                                                              WHERE
                                                              tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                                              AND NgayThucHien <= @NgayThucHien
                                                              AND ( tcdt.GiaTriThayDoi != 0
                                                              OR tcdt.ThanhTienSauTrietKhauThucChay != 0
                                                              )
                                                              GROUP BY tcdt.HopDongChiTietREF ,
                                                              tcdt.DmWebsiteREF ,
                                                              tcdt.TenWebsite
                                                            ) A
                                                            INNER JOIN HopDongChiTiet C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                                            INNER JOIN HopDong D ON D.HopDongID = C.HopDongFK
                                                            INNER JOIN DmWebsite E ON E.DmWebsiteID = C.DmWebsiteREF
                                                  WHERE     ( ( UPPER(C.DonViTinh) = 'CPM' )
                                                              OR ( UPPER(C.DonViTinh) = 'CPC' )
                                                            )
                                                            AND D.TrangThaiHopDong != 3
                                                            AND C.DeletedStatus = 0
                                                            AND C.DmSanPhamREF IN (
                                                            342 )
                                                ) TD
	            
					--HD Finish   
                                IF ( @IsHDFinish = 1 )
                                    BEGIN
                                        PRINT 'HD finish'
                                        SELECT  @TTThucChaySauChietKhau = SUM(tcdt.ThanhTienSauTrietKhauThucChay) ,
                                                @GiaTriThayDoi = SUM(tcdt.GiaTriThayDoi)
                                        FROM    ThucChayDaTinh tcdt
                                        WHERE   tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                                AND tcdt.DmSanPhamREF = @DmSanPhamID
                                                AND tcdt.HopDongID = @HopDongREF
                                                AND tcdt.NgayThucHien BETWEEN @MinDate
                                                              AND
                                                              @NgayThucHien
                                                AND tcdt.DmBannerREF = @DmBannerID
                                        PRINT @TongTienHopDong
                                            - ( @TTThucChaySauChietKhau
                                                + @GiaTriThayDoi )	
                                        PRINT '2'
                                        INSERT  INTO ThucChayDaTinh
                                                SELECT  NEWID() ,
                                                        TD.HopDongID ,
                                                        TD.SoHopDong ,
                                                        TD.DmMaHopDongREF ,
                                                        TD.TenMaHopDong ,
                                                        TD.NgayDanhSoHopDong ,
                                                        TD.NgayKyHopDong ,
                                                        TD.NhanHopDong ,
                                                        TD.NgayNhanBanFax ,
                                                        TD.NgayNhanHopDongBanCung ,
                                                        TD.NgayChuyenHopDongChoKeToan ,
                                                        TD.So ,
                                                        TD.Thang ,
                                                        TD.Nam ,
                                                        TD.GiaTriHopDong ,
                                                        TD.CongNo ,
                                                        TD.HopDongChiTietREF ,
                                                        TD.DangSuDung ,
                                                        TD.IsGiayPhep ,
                                                        TD.TrangThaiHopDong ,
                                                        TD.IsBanCung ,
                                                        TD.DmPhongBanREF ,
                                                        TD.TenPhongBan ,
                                                        TD.DmBoPhanREF ,
                                                        TD.TenBoPhan ,
                                                        TD.DmNhomLamViecREF ,
                                                        TD.TenNhom ,
                                                        TD.DmDiaDiemLamViecREF ,
                                                        TD.TenDiaDiemLamViec ,
                                                        TD.SysNhanVienREF ,
                                                        TD.TenDangNhap ,
                                                        TD.TenNhanVien ,
                                                        TD.TenKhachHang ,
                                                        TD.NhanHang ,
                                                        TD.DmNhomNganhREF ,
                                                        TD.TenNhomNganh ,
                                                        TD.DmHinhThucQuangCao ,
                                                        TD.TenHinhThucQuangCao ,
                                                        TD.DmSanPhamREF ,
                                                        TD.TenSanPham ,
                                                        TD.DmNhomWebsiteREF ,
                                                        TD.TenNhomWebsite ,
                                                        TD.DmChuyenMucREF ,
                                                        TD.TenChuyenMuc ,
                                                        TD.DmLoaiBannerREF ,
                                                        TD.TenLoaiBanner ,
                                                        TD.DmViTriREF ,
                                                        TD.TenViTri ,
                                                        TD.DotChayHopDong ,
                                                        TD.SoLuongDotChayHD ,
                                                        TD.DotChayBooking ,
                                                        TD.SoLuongDotChayBooking ,
                                                        TD.SoLuong ,
                                                        TD.DonViTinh ,
                                                        TD.DonGia ,
                                                        TD.DonGiaTheoDonViTinh ,
                                                        TD.ChietKhau ,
                                                        TD.GiamGia ,
                                                        TD.ThanhTien ,
                                                        TD.TiLeTuVan ,
                                                        TD.ChiPhiTuVan ,
                                                        TD.IsKhuyenMai ,
                                                        TD.KhuyenMai ,
                                                        TD.DmBannerREF ,
                                                        TD.DmChienDichREF ,
                                                        TD.DmWebsiteREF ,
                                                        TD.TenWebsite ,
                                                        TD.TongViewThucChay ,
                                                        TD.TongClickThucChay ,
                                                        TD.TongSoBaiViet ,
                                                        TD.SoLuongThucChay ,
                                                        TD.NgayThucHien ,
                                                        TD.GiaTriThayDoi ,
                                                        TD.ThanhTienThucChayTruocTrietKhau ,
                                                        0 AS GiaTriTrietKhauThucChay ,
                                                        0 AS ThanhTienSauTrietKhauThucChay ,
                                                        0 AS GiaTriHoaHongThucChay ,
                                                        0 AS ThanhTienThucThu ,
                                                        0 AS ThanhTienKM ,
                                                        0 AS SoLuongThucChayKM ,
                                                        0 AS SoLuongLechTreoHa ,
                                                        0 AS ThanhTienLechTreoHa ,
                                                        GETDATE() ,
                                                        GETDATE() ,
                                                        0 IsPheDuyet ,
                                                        '' PheDuyetBy ,
                                                        '' PheDuyetAt ,
                                                        TD.SoLuongThayDoi SoLuongThayDoi ,
                                                        0 SoLuongKMThayDoi ,
                                                        0 GiaTriKMThayDoi ,
                                                        '' GhiChu
                                                FROM    ( SELECT --ID Hop Dong
                                                              D.HopDongID ,
										  --Thong tin ve ma so 
                                                              D.SoHopDong ,
                                                              D.DmMaHopDongREF ,
                                                              D.TenMaHopDong ,
										  --Thong tin ve thoi gian
                                                              D.NgayDanhSoHopDong ,
                                                              D.NgayKyHopDong ,
                                                              D.NhanHopDong ,
                                                              D.NgayNhanBanFax ,
                                                              D.NgayNhanHopDongBanCung ,
                                                              D.NgayChuyenHopDongChoKeToan ,
                                                              D.So ,
                                                              D.Thang ,
                                                              D.Nam ,
										  --Thong tin ve gia tri
                                                              D.GiaTriHopDong ,
                                                              D.CongNo ,
										  --Thong tin chi tiet phan bo
                                                              A.HopDongChiTietREF ,
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
										  --Thong tin ve khach hang
										  --D.DmKhachHangREF, 
                                                              D.TenKhachHang ,
                                                              [dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID,
                                                              @NgayThucHien) NhanHang ,
                                                              C.DmNhomNganhREF ,
                                                              C.TenNhomNganh ,
										  --Thong tin hinh thuc quang cao
                                                              C.DmLoaiREF AS DmHinhThucQuangCao ,
                                                              C.TenLoai AS TenHinhThucQuangCao ,
										  --Thong tin San pham
                                                              C.DmSanPhamREF AS DmSanPhamREF ,
                                                              C.TenSanPham AS TenSanPham ,
                                                              C.DmNhomWebsiteREF ,
                                                              C.TenNhomWebsite ,
										  --C.DmWebsiteREF,
										  --C.TenWebsite, 
                                                              C.DmChuyenMucREF ,
                                                              C.TenChuyenMuc ,
                                                              C.DmLoaiBannerREF ,
                                                              C.TenLoaiBanner ,
                                                              C.DmViTriREF ,
                                                              C.TenViTri ,
                                                              'Mobile_TTR' DotChayHopDong ,
                                                              C.SoLuong AS SoLuongDotChayHD ,
                                                              'PS THUC TREO Mobile' DotChayBooking ,
                                                              0 SoLuongDotChayBooking ,
                                                              C.SoLuong
                                                              * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong ,
                                                              ( CASE
                                                              WHEN C.TenLoai IN (
                                                              'CPC', 'CPM' )
                                                              THEN dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh)
                                                              ELSE dbo.ThucChay_GetDonViTinhNotCPD(C.TenLoai)
                                                              END ) AS DonViTinh ,
                                                              dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,
                                                              A.HopDongChiTietREF,
                                                              C.DonGia) AS DonGia ,
                                                              ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,
                                                              C.DonViTinh,
                                                              C.DonGia,
                                                              D.NgayKyHopDong,
                                                              @NgayThucHien,
                                                              A.HopDongChiTietREF),
                                                              0) AS DonGiaTheoDonViTinh ,
                                                              C.ChietKhau ,
                                                              C.GiamGia ,
                                                              C.ThanhTien ,
                                                              C.TiLeTuVan ,
                                                              C.ChiPhiTuVan ,
                                                              C.IsKhuyenMai ,
                                                              C.KhuyenMai ,
                                                              @DmBannerID DmBannerREF ,	--A.DmBannerREF,
                                                              0 DmChienDichREF ,	--A.DmChienDichREF,
                                                              A.DmWebsiteREF ,
                                                              A.TenWebsite ,
                                                              0 TongViewThucChay ,
                                                              0 TongClickThucChay ,
                                                              0 TongSoBaiViet ,
                                                              0 AS SoLuongThucChay ,
                                                              @NgayThucHien NgayThucHien ,
                                                              A.GiaTriThayDoi AS GiaTriThayDoi ,
                                                              0 AS ThanhTienThucChayTruocTrietKhau ,
                                                              A.SoLuongThayDoi SoLuongThayDoi
                                                          FROM
                                                              ( SELECT TOP 1
                                                              tcdt.HopDongChiTietREF ,
                                                              tcdt.DmWebsiteREF ,
                                                              tcdt.TenWebsite ,
                                                              ( @TongTienHopDong
                                                              - ( @TTThucChaySauChietKhau
                                                              + @GiaTriThayDoi ) ) GiaTriThayDoi ,
                                                              ( @SoLuongHopDong
                                                              - @SoLuongThucChay ) SoLuongThayDoi
                                                              FROM
                                                              ThucChayDaTinh tcdt
                                                              WHERE
                                                              tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                                              AND ( tcdt.GiaTriThayDoi != 0
                                                              OR tcdt.ThanhTienSauTrietKhauThucChay != 0
                                                              )
                                                              AND tcdt.DmBannerREF = @DmBannerID
                                                              GROUP BY tcdt.HopDongChiTietREF ,
                                                              tcdt.DmWebsiteREF ,
                                                              tcdt.TenWebsite
                                                              ) A
                                                              INNER JOIN HopDongChiTiet C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                                              INNER JOIN HopDong D ON D.HopDongID = C.HopDongFK
                                                              INNER JOIN DmWebsite E ON E.DmWebsiteID = C.DmWebsiteREF
                                                          WHERE
                                                              ( ( UPPER(C.DonViTinh) = 'CPM' )
                                                              OR ( UPPER(C.DonViTinh) = 'CPC' )
                                                              )
                                                              AND D.TrangThaiHopDong != 3
                                                              AND C.DeletedStatus = 0
                                                              AND C.DmSanPhamREF IN (
                                                              342 )
                                                        ) TD
                                    END
	            
					--Insert log
                                INSERT  INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
                                        SELECT  NEWID() ,
                                                D.HopDongID ,
	                              --Thong tin ve ma so 
                                                D.SoHopDong ,
                                                A.HopDongChiTietREF ,
                                                C.DmSanPhamREF AS DmSanPhamREF ,
                                                A.DmWebsiteREF ,
                                                @NgayThucHien NgayThucHien ,
                                                ISNULL(A.GiaTriThayDoi, 0) AS GiaTriThayDoi ,
                                                0 AS GiaSauCK1 ,
                                                0 Soluong1 ,
                                                0 AS GiaSauCK2 ,
                                                0 Soluong2 ,
                                                @CONTENT_LOG ,
                                                N'Thay đổi hợp đồng' ,
                                                'Mobile' ,
                                                'ThucChay' ,
                                                GETDATE() ,
                                                'ThucChay' ,
                                                GETDATE() ,
                                                0 ,
                                                0 ,
                                                0
                                        FROM    ( SELECT    tcdt.HopDongChiTietREF ,
                                                            tcdt.DmWebsiteREF ,
                                                            tcdt.TenWebsite ,
                                                            ( ( SUM(tcdt.ThanhTienSauTrietKhauThucChay
                                                              + tcdt.GiaTriThayDoi)
                                                              / @TongTienThucChay )
                                                              * @TTChenhLechDuocTinh ) GiaTriThayDoi
                                                  FROM      ThucChayDaTinh tcdt
                                                  WHERE     tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                                            AND ( tcdt.GiaTriThayDoi != 0
                                                              OR tcdt.ThanhTienSauTrietKhauThucChay != 0
                                                              )
                                                            AND tcdt.DmBannerREF = @DmBannerID
                                                  GROUP BY  tcdt.HopDongChiTietREF ,
                                                            tcdt.DmWebsiteREF ,
                                                            tcdt.TenWebsite
                                                ) A
                                                INNER JOIN HopDongChiTiet C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                                INNER JOIN HopDong D ON D.HopDongID = C.HopDongFK
                                                INNER JOIN DmWebsite E ON E.DmWebsiteID = C.DmWebsiteREF
                                        WHERE   D.TrangThaiHopDong != 3
                                                AND C.DeletedStatus = 0
                                                AND C.DmSanPhamREF IN ( 342 )
	                              --AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](C.DonViTinhREF, C.DonViTinh) = 3      
                            END
                    END
            END
	
        SELECT  2
    END


```
