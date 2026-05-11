# Stored Procedure: `ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi_ManualByHopDongChiTietID_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-26 11:32:13.457000
- **Ngày sửa cuối**: 2017-07-06 09:47:31.893000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- 
-- EXEC [dbo].[ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi_ManualByHopDongChiTietID_v2]  '2017-03-23', 'QC0110117',108489,342

CREATE PROCEDURE [dbo].[ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi_ManualByHopDongChiTietID_v2] 
	-- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @HopDongChiTietREF INT ,
    @DmSanPhamREF INT
AS
    BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
        SET NOCOUNT ON;
	
        DECLARE @DmHinhThucQuangCao INT ,
            @DonViTinh NVARCHAR(50) ,
            @HopDongID INT

        DECLARE @TongTienThucChay FLOAT = 0 ,
            @GiaTriHopDong FLOAT = 0 ,
            @GiaTriThucChayVuot FLOAT = 0 ,
            @Count INT	  = 0 ,
            @ThucChayTheoSite FLOAT = 0 ,
            @TyLe FLOAT = 0 ,
            @SoLuongThucChay INT = 0 ,
            @TyLePhanBo FLOAT = 0 ,
            @SoLuongHopDong INT = 0 ,
            @SoluongVuot INT = 0
			
        DECLARE @DmWebsiteREF INT ,
            @TenWebsite NVARCHAR(50) ,
            @DonViTinhPB NVARCHAR(50) ,
            @DanhSachNhanHangReF NVARCHAR(200) ,
            @DmBannerREF INT

	--get danh sach nhan tren thuc treo

        SELECT  @DanhSachNhanHangReF = COALESCE(@DanhSachNhanHangReF + N', ',
                                                N'') + A.DmNhanHangREF
        FROM    ( SELECT DISTINCT
                            DmNhanHangREF
                  FROM      dbo.ThucChayHopDongChiTiet
                  WHERE     HopDongChiTietREF = @HopDongChiTietREF
                            AND DeletedStatus = 0
                ) A
	
        SET @DanhSachNhanHangReF = ISNULL(@DanhSachNhanHangReF, '')				
        DECLARE record_cursor CURSOR
        FOR
            SELECT DISTINCT
                    DmHinhThucQuangCao ,
                    DonViTinh
            FROM    --ThucChayDaTinhMobile
                    ThucChayDaTinh
            WHERE   SoHopDong = @SoHopDong
                    AND HopDongChiTietREF = @HopDongChiTietREF
                    AND NgayThucHien <= @NgayThucHien
                    AND DmSanPhamREF = @DmSanPhamREF
                    AND TrangThaiHopDong <> 3
		
        OPEN record_cursor
	
        FETCH NEXT FROM record_cursor INTO @DmHinhThucQuangCao, @DonViTinh
	
        WHILE @@FETCH_STATUS = 0
            BEGIN
			
                SELECT  @TongTienThucChay = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,
                                                       0)
                                                + ISNULL(GiaTriThayDoi, 0)) ,
                        @SoLuongThucChay = SUM(ISNULL(tcdt.SoLuongThucChay, 0)
                                               + ISNULL(tcdt.SoLuongThayDoi, 0)) ,
                        @HopDongID = MAX(HopDongID)
                FROM    --ThucChayDaTinhMobile AS tcdt
                        ThucChayDaTinh tcdt
                WHERE   tcdt.SoHopDong = @SoHopDong
                        AND tcdt.DmSanPhamREF = @DmSanPhamREF
                        AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
                        AND tcdt.DonViTinh = @DonViTinh
                        AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
		
                SET @TongTienThucChay = ISNULL(@TongTienThucChay, 0);
			
                PRINT 'TongTienThucChay: '
                    + CONVERT(NVARCHAR(50), @TongTienThucChay);	
		
		

                SELECT  @GiaTriHopDong = ISNULL(SUM(ThanhTien), 0) ,
                        @SoLuongHopDong = ISNULL(SUM(hdct.SoLuong), 0)
                FROM    HopDong AS hd
                        INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
                WHERE   hdct.DmSanPhamREF = @DmSanPhamREF
                        AND hd.SoHopDong = @SoHopDong
                        AND hdct.IsKhuyenMai = 0
                        AND hdct.DeletedStatus = 0
                        AND hdct.DmLoaiREF = @DmHinhThucQuangCao
                        AND hdct.HopDongChiTietID = @HopDongChiTietREF
			
                PRINT 'GiaTriHopDong: ' + CONVERT(NVARCHAR(50), @GiaTriHopDong);	

                DECLARE @DVT NVARCHAR(50)

                SELECT  @DVT = hdct.DonViTinh
                FROM    dbo.HopDongChiTiet hdct
                WHERE   hdct.HopDongChiTietID = @HopDongChiTietREF
                        AND hdct.DmSanPhamREF = @DmSanPhamREF
                        AND hdct.IsKhuyenMai = 0
                        AND hdct.DeletedStatus = 0
                        AND hdct.DmLoaiREF = @DmHinhThucQuangCao

                IF @DVT = 'CPM'
                    BEGIN
                        SET @SoLuongHopDong = @SoLuongHopDong * 1000
                    END
                ELSE
                    BEGIN
                        SET @SoLuongHopDong = @SoLuongHopDong
                    END
		
                SET @GiaTriThucChayVuot = @TongTienThucChay - @GiaTriHopDong
                PRINT 'GiaTriThucChayVuot: '
                    + CONVERT(NVARCHAR(50), @GiaTriThucChayVuot);	
		


                SET @SoluongVuot = @SoLuongThucChay - @SoLuongHopDong
					
				
                SELECT  @Count = COUNT(DISTINCT DmWebsiteREF) 
		--FROM ThucChayDaTinhMobile AS tcdt
                FROM    ThucChayDaTinh AS tcdt
                WHERE   tcdt.SoHopDong = @SoHopDong
                        AND tcdt.DmSanPhamREF = @DmSanPhamREF
                        AND tcdt.TrangThaiHopDong <> 3
                        AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
                        AND tcdt.DonViTinh = @DonViTinh
                        AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
		
                PRINT 'SoLuongWebsite: ' + CONVERT(NVARCHAR(50), @Count);	
		
                DECLARE td_cursor CURSOR
                FOR
                    SELECT DISTINCT
                            DmWebsiteREF ,
                            TenWebsite ,
                            tcdt.DmBannerREF
		--FROM ThucChayDaTinhMobile AS tcdt
                    FROM    ThucChayDaTinh AS tcdt
                    WHERE   tcdt.SoHopDong = @SoHopDong
                            AND tcdt.DmSanPhamREF = @DmSanPhamREF
                            AND tcdt.TrangThaiHopDong <> 3
                            AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
                            AND tcdt.DonViTinh = @DonViTinh
                            AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
		
                OPEN td_cursor
		
                FETCH NEXT FROM td_cursor INTO @DmWebsiteREF, @TenWebsite,
                    @DmBannerREF
                WHILE @@FETCH_STATUS = 0
                    BEGIN
                        SELECT  @ThucChayTheoSite = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,
                                                              0)
                                                        + ISNULL(GiaTriThayDoi,
                                                              0))
                        FROM    --ThucChayDaTinhMobile AS tcdt
                                ThucChayDaTinh AS tcdt
                        WHERE   tcdt.SoHopDong = @SoHopDong
                                AND tcdt.DmSanPhamREF = @DmSanPhamREF
                                AND tcdt.DmWebsiteREF = @DmWebsiteREF
                                AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
                                AND tcdt.DonViTinh = @DonViTinh
                                AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                AND tcdt.DmBannerREF = @DmBannerREF
                        IF ( @TongTienThucChay <> 0 )
                            SET @TyLe = @ThucChayTheoSite / @TongTienThucChay
                                * 100
                        ELSE
                            SET @TyLe = 0
				
                        PRINT 'Website: ' + @TenWebsite;
                        PRINT 'TyLe: ' + CONVERT(NVARCHAR(50), @TyLe);
			
			
                        IF ( @TyLe > 0 
				--AND @DmWebsiteREF > 0
                             )
                            BEGIN
                                PRINT 'OK'
				
                               -- INSERT  INTO ThucChayDaTinh
                                        SELECT  NEWID() ,
                                                TD.* ,
                                                0 GiaTriTrietKhauThucChay ,
                                                0 AS ThanhTienSauTrietKhauThucChay ,
                                                0 AS GiaTriHoaHongThucChay ,
                                                0 AS ThanhTienThucThu ,
                                                0 AS ThanhTienKM ,
                                                0 AS SoLuongThucChayKM ,
                                                0 SoLuongLechTreoHa ,
                                                0 ThanhTienLechTreoHa ,
                                                GETDATE() ,
                                                GETDATE() ,
                                                0 IsPheDuyet ,
                                                '' PheDuyetBy ,
                                                '' PheDuyetAt ,
                                                -( @SoluongVuot * @TyLe / 100 ) SoLuongThayDoi ,
                                                0 SoLuongKMThayDoi ,
                                                0 GiaTriKMThayDoi ,
                                                '' GhiChu
                                        FROM    ( SELECT DISTINCT
						 --ID Hop Dong
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
						 --Thong tin chi tiet phan bo
                                                            @HopDongChiTietREF HopDongChiTietID ,
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
                                                            @DanhSachNhanHangReF NhanHang ,
                                                            0 DmNhomNganhREF ,
                                                            0 TenNhomNganh , 
						 --Thong tin hinh thuc quang cao
                                                            @DmHinhThucQuangCao AS DmHinhThucQuangCao ,
                                                            CASE
                                                              WHEN @DmHinhThucQuangCao = 6
                                                              THEN 'CPM'
                                                              WHEN @DmHinhThucQuangCao = 7
                                                              THEN 'CPC'
                                                            END AS TenHinhThucQuangCao , 
						 --Thong tin San pham
                                                            @DmSanPhamREF AS DmSanPhamREF ,
                                                            ( SELECT TOP 1
                                                              dsptc.TenSanPham
                                                              FROM
                                                              DmSanPhamThucChay dsptc
                                                              WHERE
                                                              dsptc.DmSanPhamREF = @DmSanPhamREF
                                                              AND dsptc.DeletedStatus = 0
                                                              AND dsptc.RecordStatus = 1
                                                            ) TenSanPham ,
                                                            0 DmNhomWebsiteREF ,
                                                            0 TenNhomWebsite , 
						 --C.DmWebsiteREF, 
						 --C.TenWebsite, 
                                                            0 DmChuyenMucREF ,
                                                            0 TenChuyenMuc ,
                                                            C.DmLoaiBannerREF DmLoaiBannerREF ,
                                                            C.TenLoaiBanner TenLoaiBanner ,
                                                            C.DmViTriREF DmViTriREF ,
                                                            C.TenViTri TenViTri ,
                                                            CASE @DmSanPhamREF
                                                              WHEN 342
                                                              THEN 'Mobile_Update'
                                                              WHEN 381
                                                              THEN 'Sponsor_Update'
                                                            END AS DotChayHopDong ,
                                                            0 AS SoLuongDotChayHD ,
                                                            CASE @DmSanPhamREF
                                                              WHEN 342
                                                              THEN 'PS Mobile Update thuc chay vuot gia tri hop dong'
                                                              WHEN 381
                                                              THEN 'PS Sponsor Update thuc chay vuot gia tri hop dong'
                                                            END AS DotChayBooking ,
                                                            0 AS SoLuongDotChayBooking , 
						 --Thong tin ve Tien
                                                            ( CASE WHEN C.DonViTinh = 'CPM'
																THEN C.SoLuong * 1000
																ELSE C.SoLuong
														   END ) AS SoLuong ,
                                                            @DonViTinh DonViTinh ,
                                                            ISNULL(dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,--@ProductUnitName,
                                                              ( CASE
                                                              WHEN C.DonViTinh IN (
                                                              'CPC', 'CPM' )
                                                              THEN C.DonViTinh
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPC'
                                                              THEN 'CPC'
                                                              WHEN C.DonViTinh = N'Gói'
                                                              AND C.TenLoai = 'CPM'
                                                              THEN 'CPM'
                                                              END ), 1,
                                                              @NgayThucHien),
															0) AS DonGia , 
						 --ISNULL(dbo.ThucChay_GetDonGiaThucTreo_PR(D.NgayKyHopDong, '2014-05-14', C.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
                                                            0 AS DonGiaTheoDonViTinh ,
                                                            C.ChietKhau ChietKhau ,
                                                            0 GiamGia ,
                                                            0 ThanhTien ,
                                                            0 TiLeTuVan ,
                                                            0 ChiPhiTuVan ,
                                                            C.IsKhuyenMai IsKhuyenMai ,
                                                            '' KhuyenMai ,
						 --Thuc chay
                                                            @DmBannerREF DmBannerREF ,--A.DmBannerREF,
                                                            0 DmChienDichREF ,--A.DmChienDichREF,
                                                            @DmWebsiteREF DmWebsiteREF ,
                                                            @TenWebsite TenWebsite ,
                                                            0 TongViewThucChay ,
                                                            0 TongClickThucChay ,
                                                            0 TongSoBaiViet ,
                                                            0 SoLuongThucChay ,
						 --Thanhuc Tien Thuc Chay
                                                            @NgayThucHien AS NgayThucHien ,
                                                            0
                                                            - ( @GiaTriThucChayVuot
                                                              * @TyLe / 100 ) AS GiaTriThayDoi ,
						 --(@GiaTriThucChayVuot*@TyLe/100) as GiaTriThayDoi,
                                                            0 AS ThanhTienThucChayTruocTrietKhau
                                                  FROM      HopDong D
                                                            INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
                                                  WHERE     D.SoHopDong = @SoHopDong
                                                            AND C.HopDongChiTietID = @HopDongChiTietREF
						--AND C.DmSanPhamREF = @DmSanPhamREF
						--AND C.IsKhuyenMai = 0
                                                ) TD
				
				 --Insert Log gia tri thay doi
                                --EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert @HopDongID,
                                --    @SoHopDong, @HopDongChiTietREF,
                                --    @DmSanPhamREF, @DmWebsiteREF,
                                --    @NgayThucHien, @GiaTriThucChayVuot, 0, 0,
                                --    0, 0,
                                --    'PS Mobile Update thuc chay vuot gia tri hop dong',
                                --    'HopDongChiTiet',
                                --    'PS Mobile Update thuc chay vuot gia tri hop dong'
                            END
			
                        FETCH NEXT FROM td_cursor INTO @DmWebsiteREF,
                            @TenWebsite, @DmBannerREF
                    END
		
                CLOSE td_cursor
                DEALLOCATE td_cursor
	
                FETCH NEXT FROM record_cursor INTO @DmHinhThucQuangCao,
                    @DonViTinh
            END
        CLOSE record_cursor
        DEALLOCATE record_cursor
    END


```
