# Stored Procedure: `sp_TC_CheckHopDongCoThayDoi_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-23 17:56:14.727000
- **Ngày sửa cuối**: 2023-05-12 14:40:42.727000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@BannerType` | `int(4)` | No |
| `@DmBannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- [dbo].[sp_TC_CheckHopDongCoThayDoi_Mobile] 47955, 'QC2701216', 342, 107508, '2017-06-24', NULL, 501697
CREATE PROCEDURE [dbo].[sp_TC_CheckHopDongCoThayDoi_Mobile] 
	-- Add the parameters for the stored procedure here
    @HopDongID INT ,
    @SoHopDong NVARCHAR(50) ,
    @DmSanPhamREF INT ,
    @HopDongChiTietID INT ,
    @NgayThucHien DATETIME ,
    @BannerType INT ,
    @DmBannerID INT --Banner thay doi thong tin 
	--@ProductUnitName NVARCHAR(50)
AS
    BEGIN
        DECLARE @ThanhTienTCDTBF FLOAT ,
            @ThanhTienTCDT FLOAT ,
            @IsKhuyenMai INT ,
            @DonViTinh NVARCHAR(50) ,
            @ChietKhauTCDT FLOAT ,
            @DonGiaTheoDonViTinh INT ,
            @SoLuongThucChay INT ,
            @GiaTriThayDoi FLOAT ,
            @SoLuongThayDoi FLOAT ,
            @DonGiaBF FLOAT ,
            @DonGia FLOAT ,
            @ChietKhauBF FLOAT ,
            @ChietKhau FLOAT ,
            @SoLuongHDBF FLOAT ,
            @SoLuongHD FLOAT ,
            @HopDongChiTietThayDoiCK FLOAT ,
            @DonGiaChenhLech FLOAT ,
            @DmWebsiteREF INT ,
            @TenWebsite NVARCHAR(50) ,
            @NgayThayDoiLast DATETIME ,
            @SoLuongThucChayByWebiste FLOAT ,
            @CountHDTD INT ,
            @SoLuongTCDTTheoWebsite FLOAT ,
            @SoLuongTCTheoWebsite FLOAT ,
            @HopDongChiTietThayDoiGia INT;
        DECLARE @CONTENT_LOG NVARCHAR(MAX) ,
            @NGUON_LOG NVARCHAR(500) ,
            @CONTENT_DETAIL_LOG NVARCHAR(MAX)
	
        SET @CONTENT_LOG = '';
        SET @NGUON_LOG = '';
        SET @DonGiaChenhLech = 0;
        SET @HopDongChiTietThayDoiGia = 0; 
        SET @HopDongChiTietThayDoiCK = 0;
        SET @ThanhTienTCDT = 0;
	
        





        DECLARE @SoHopDong_new NVARCHAR(50) ,
            @NgayDanhSo_new DATETIME ,
            @DmNhanVienREF_new INT ,
            @TenKhachHang_new NVARCHAR(500) ,
            @DmSanPhamREF_new INT ,
            @DsTenNhanHang_new NVARCHAR(500) ,
            @HinhThucQuangCaoREF_new INT ,
            @MaSoHopDong_new INT ,
            @TenDangNhap_new NVARCHAR(25) ,
            @SoHopDong_old NVARCHAR(50) ,
            @NgayDanhSo_old DATETIME ,
            @DmNhanVienREF_old INT ,
            @TenKhachHang_old NVARCHAR(500) ,
            @DmSanPhamREF_old INT ,
            @DsTenNhanHang_old NVARCHAR(500) ,
            @HinhThucQuangCaoREF_old INT ,
            @MaSoHopDong_old INT ,
            @TenDangNhap_old NVARCHAR(25)




        SELECT  @IsKhuyenMai = IsKhuyenMai ,
                @ChietKhau = hdct.ChietKhau ,
                @SoLuongHD = ( CASE WHEN hdct.DonViTinh = 'CPM'
                                    THEN hdct.SoLuong * 1000
                                    ELSE hdct.SoLuong
                               END ) ,
                @DonGia = ISNULL(dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(hdct.HopDongChiTietID,--@ProductUnitName,
                                                              ( CASE
                                                              WHEN hdct.DonViTinh IN (
                                                              'CPC', 'CPM' )
                                                              THEN hdct.DonViTinh
                                                              WHEN hdct.DonViTinh = N'Gói'
                                                              AND hdct.TenLoai = 'CPC'
                                                              THEN 'CPC'
                                                              WHEN hdct.DonViTinh = N'Gói'
                                                              AND hdct.TenLoai = 'CPM'
                                                              THEN 'CPM'
                                                              END ), 1,
                                                              @NgayThucHien),
                                 0) ,
                @SoHopDong_new = hd.SoHopDong ,
                @NgayDanhSo_new = hd.NgayDanhSoHopDong ,
                @DmNhanVienREF_new = hd.SysNhanVienREF ,
                @TenKhachHang_new = hd.TenKhachHang ,
                @DmSanPhamREF_new = hdct.DmSanPhamREF ,
				--@DsTenNhanHang_new = hdct.DanhSachNhanHangREF,
                @HinhThucQuangCaoREF_new = hdct.DmLoaiREF ,
                @MaSoHopDong_new = hd.DmMaHopDongREF ,
                @TenDangNhap_new = hd.TenDangNhap
        FROM    HopDongChiTiet hdct
                INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
        WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                AND hdct.DonViTinhREF <> 10



        SELECT  @DsTenNhanHang_new = COALESCE(@DsTenNhanHang_new + ',', '')
                + ISNULL(CAST(T.DmNhanHangREF AS VARCHAR(1000)), '')
        FROM    ( SELECT DISTINCT
                            DmNhanHangREF
                  FROM      dbo.ThucChayHopDongChiTiet
                  WHERE     1 = 1
                            AND HopDongChiTietREF = @HopDongChiTietID
                            AND DeletedStatus = 0
                            --AND DmBannerREF = CONVERT(NVARCHAR(255), @DmBannerID)
                ) T 

        SET @DsTenNhanHang_new = ISNULL(@DsTenNhanHang_new, '');

	

	
        SELECT TOP 1
                @DonGiaBF = DonGia ,
                @ChietKhauBF = ChietKhau ,
                @SoLuongHDBF = SoLuong ,
                @SoHopDong_old = tcdtm.SoHopDong ,
                @NgayDanhSo_old = tcdtm.NgayDanhSoHopDong ,
                @DmNhanVienREF_old = tcdtm.SysNhanVienREF ,
                @TenKhachHang_old = tcdtm.TenKhachHang ,
                @DmSanPhamREF_old = tcdtm.DmSanPhamREF ,
                --@DsTenNhanHang_old = tcdtm.NhanHang ,
                @HinhThucQuangCaoREF_old = tcdtm.DmHinhThucQuangCao ,
                @MaSoHopDong_old = tcdtm.DmMaHopDongREF ,
                @TenDangNhap_old = tcdtm.TenDangNhap
        FROM    ThucChayDaTinh tcdtm
        WHERE   tcdtm.HopDongChiTietREF = @HopDongChiTietID
                AND tcdtm.DmSanPhamREF = @DmSanPhamREF
                AND tcdtm.NgayThucHien < @NgayThucHien
                --AND tcdtm.DmBannerREF = @DmBannerID
        ORDER BY tcdtm.NgayThucHien DESC



         SELECT  @DsTenNhanHang_old = COALESCE(@DsTenNhanHang_old + ',', '')
                + ISNULL(CAST(T.NhanHang AS VARCHAR(1000)), '')
        FROM    ( SELECT DISTINCT
                            T2.NhanHang
                  FROM      ( SELECT    tcdtm.NhanHang ,
                                        SUM(tcdtm.ThanhTienSauTrietKhauThucChay
                                            + tcdtm.GiaTriThayDoi) Tien
										,
										SUM(tcdtm.ThanhTienKM + tcdtm.GiaTriKMThayDoi) TienKM
                              FROM      ThucChayDaTinh tcdtm
                              WHERE     tcdtm.HopDongChiTietREF = @HopDongChiTietID
                                        AND tcdtm.DmSanPhamREF = @DmSanPhamREF
                                        AND tcdtm.NgayThucHien < @NgayThucHien
						--AND tcdtm.DmBannerREF = @DmBannerID
                              GROUP BY  tcdtm.NhanHang
                            ) T2
                  WHERE     T2.Tien <> 0 OR T2.TienKM <> 0
                ) T 



        SET @DsTenNhanHang_old = ISNULL(@DsTenNhanHang_old, '');


		
						
        DECLARE @IsThayDoi INT = 0


        IF EXISTS ( SELECT TOP 1
                            DonGia ,
                            ChietKhau ,
                            SoLuong ,
                            tcdtm.SoHopDong ,
                            tcdtm.NgayDanhSoHopDong ,
                            tcdtm.SysNhanVienREF ,
                            tcdtm.TenKhachHang ,
                            tcdtm.DmSanPhamREF ,
                            tcdtm.NhanHang ,
                            tcdtm.DmHinhThucQuangCao ,
                            tcdtm.DmMaHopDongREF ,
                            tcdtm.TenDangNhap
                    FROM    ThucChayDaTinh tcdtm
                    WHERE   tcdtm.HopDongChiTietREF = @HopDongChiTietID
                            AND tcdtm.DmSanPhamREF = @DmSanPhamREF
                            AND tcdtm.NgayThucHien < @NgayThucHien
                            --AND tcdtm.DmBannerREF = @DmBannerID
                    ORDER BY tcdtm.NgayThucHien DESC )
            AND EXISTS ( SELECT *
                         FROM   HopDongChiTiet hdct
                                INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
                         WHERE  hdct.HopDongChiTietID = @HopDongChiTietID
                                AND hdct.DonViTinhREF <> 10 )
            BEGIN
		    	--NEU CO THAY DOI VE GIA
                IF ( @DonGia <> @DonGiaBF )
                    BEGIN
                        SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi giá:'
                            + ISNULL(CONVERT(NVARCHAR(30), @DonGiaBF), '') + '->'
                            + ISNULL(CONVERT(NVARCHAR(30), @DonGia), '') + ');'
                        SET @NGUON_LOG = @NGUON_LOG
                            + 'Table:HopDongChiTietThayDoi:'
                            + CONVERT(NVARCHAR(50), @HopDongChiTietThayDoiGia)

                        SET @IsThayDoi = 1
                    END		
			
			--NEU CO THAY DOI VE CHIET KHAU
                IF ( @ChietKhau <> @ChietKhauBF )
                    BEGIN
                        SET @CONTENT_LOG = @CONTENT_LOG
                            + N'(HĐ Thay đổi chiết khấu:'
                            + ISNULL(CONVERT(NVARCHAR(30), @ChietKhauBF), '') + '->'
                            + ISNULL(CONVERT(NVARCHAR(30), @ChietKhau), '') + ');'
                        SET @NGUON_LOG = @NGUON_LOG
                            + 'Table:HopDongChiTietThayDoi: '
                            + CONVERT(NVARCHAR(30), @HopDongChiTietThayDoiCK)		
							
                        SET @IsThayDoi = 1		
                    END
			
			--NEU CO THAY DOI VE SO LUONG		
                IF ( @SoLuongHD <> @SoLuongHDBF )
                    BEGIN
                        SET @CONTENT_LOG = @CONTENT_LOG
                            + N'(HĐ Thay đổi số lượng:'
                            + ISNULL(CONVERT(NVARCHAR(30), @SoLuongHDBF), '') + '->'
                            + ISNULL(CONVERT(NVARCHAR(30), @SoLuongHD), '') + ');'
                        SET @NGUON_LOG = @NGUON_LOG
                            + 'Table:HopDongChiTietThayDoi: '
                            + CONVERT(NVARCHAR(30), @HopDongChiTietThayDoiCK)		
							
							
                        SET @IsThayDoi = 1
						
                    END		





                IF @SoHopDong_new <> @SoHopDong_old
                    OR @NgayDanhSo_new <> @NgayDanhSo_old
                    OR @DmNhanVienREF_new <> @DmNhanVienREF_old
                    OR @TenKhachHang_new <> @TenKhachHang_old
                    OR @DmSanPhamREF_new <> @DmSanPhamREF_old
                    OR @DsTenNhanHang_new <> @DsTenNhanHang_old
                    OR @HinhThucQuangCaoREF_new <> @HinhThucQuangCaoREF_old
                    OR @MaSoHopDong_new <> @MaSoHopDong_old
                    OR @TenDangNhap_new <> @TenDangNhap_old
                    BEGIN 
                        SET @IsThayDoi = 1
						SET @CONTENT_LOG = @CONTENT_LOG
                            + N'thong tin'
                    END 






                IF @IsThayDoi = 1
                    BEGIN
                        EXEC [sp_TC_ThayDoiSoLuong_Mobile] @NgayThucHien,
                            @HopDongID, @DmSanPhamREF, @HopDongChiTietID,
                            @CONTENT_LOG, @DmBannerID
                    END
            END
				
													
		




    END

```
