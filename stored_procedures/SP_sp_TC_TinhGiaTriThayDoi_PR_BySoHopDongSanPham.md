# Stored Procedure: `sp_TC_TinhGiaTriThayDoi_PR_BySoHopDongSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-01-16 15:39:02.110000
- **Ngày sửa cuối**: 2018-07-19 14:48:06.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThoiGianBDTinh` | `datetime(8)` | No |
| `@pHopDongID` | `int(4)` | No |
| `@pDmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[sp_TC_TinhGiaTriThayDoi_PR_BySoHopDongSanPham] 
    @NgayThucHien DATETIME ,
    @ThoiGianBDTinh DATETIME,
	@pHopDongID INT,
	@pDmSanPhamREF INT
*/
CREATE PROCEDURE [dbo].[sp_TC_TinhGiaTriThayDoi_PR_BySoHopDongSanPham] 
-- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME ,
    @ThoiGianBDTinh DATETIME,
	@pHopDongID INT,
	@pDmSanPhamREF INT
AS
    BEGIN

		SET @ThoiGianBDTinh = '2016-01-01'
	-- Declare the return variable here
        DECLARE @HopDongREF INT ,
            @HopDongChiTietREF INT ,
            @ThucChayHopDongChiTietPRID INT ,
            @DmHinhThucQuangCaoREF INT ,
            @DmSanPhamREF INT ,
            @DmNhanHangREF INT ,
            @DmViTriREF INT ,
            @SoLuong INT ,
            @ChietKhau FLOAT ,
            @KhuyenMai INT ,
            @DmWebsiteREF INT ,
            @GiaTien FLOAT ,
            @ThoiGianBatDau DATETIME ,
            @DeletedStatus INT;
        DECLARE @LoaiThayDoi INT ,
            @GiaTriThayDoiHT FLOAT ,
            @ThanhTienThucChayDaTinh FLOAT ,
            @ThoiGianBatDauCheck DATETIME;
        DECLARE @CONTENT_LOG NVARCHAR(MAX) = '' ,
            @NGUON_LOG NVARCHAR(MAX) ,
            @SoHopDong NVARCHAR(100);
		DECLARE @TaiSao NVARCHAR(500) = ''
        DECLARE @SoLuongThayDoi INT ,
            @SoLuongThucChay INT;
        DECLARE @NgayDanhSoHopDong DATETIME ,
            @SysNhanVienREF INT ,
            @DmMaHopDongREF INT ,
            @TenDangNhap NVARCHAR(25) ,
            @DmKhachHangREF INT;
        DECLARE @TenKhachHang NVARCHAR(255);
        DECLARE @TrangThaiHopDong INT
        DECLARE @DeletedStatusHDCT INT
	
        SET @LoaiThayDoi = 0; --LOAI THAY DOI : 1 CHI THAY DOI GIA TRI, 2 THAY DOI THONG TIN, 3 THUC TREO BI HUY, 0 KHONG THAY DOI GIA TRI HOAC THONG TIN     
        SET @GiaTriThayDoiHT = 0;
        SET @ThanhTienThucChayDaTinh = 0;
        SET @ThoiGianBatDauCheck = '2016-01-01';
        SET @SoLuongThayDoi = 0;

		
	
        DECLARE Record_Cursor CURSOR
        FOR
            --LAY THONG TIN HOPDONGCHITIET CUA TAT CAC CAC THUC TREO DC NHAP HOAC SUA NGAYTHUCHIEN> THOIGIANBATDAU
	    SELECT DISTINCT
                A.HopDongREF ,
                A.HopDongChiTietREF ,
                A.ThucChayHopDongChiTietPRID ,
                A.DmHinhThucQuangCaoREF ,
                A.DmSanPhamREF ,
                A.DmNhanHangREF ,
                A.DmViTriREF ,
                A.SoLuong ,
                A.ChietKhau ,
                A.KhuyenMai ,
                A.DmWebsiteREF ,
                A.GiaTien ,
                A.ThoiGianBatDau ,
                A.DeletedStatus ,
                A.NgayDanhSoHopDong ,
                A.SysNhanVienREF ,
                A.DmMaHopDongREF ,
                A.TenDangNhap ,
                A.TenKhachHang ,
                A.TrangThaiHopDong ,
                A.DeletedStatusHDCT
        FROM    ( SELECT    tchdctp.HopDongREF ,
                            hdct.HopDongChiTietID HopDongChiTietREF ,
                            tchdctp.ThucChayHopDongChiTietPRID ,
                            tchdctp.DmHinhThucQuangCaoREF ,
                            tchdctp.DmSanPhamREF ,
                            tchdctp.DmNhanHangREF ,
                            tchdctp.DmViTriREF ,
                            tchdctp.SoLuong ,
                            tchdctp.ChietKhau ,
                            tchdctp.KhuyenMai ,
                            dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(tchdctp.DmWebsiteREF) DmWebsiteREF ,
                            tchdctp.GiaTien ,
                            tchdctp.ThoiGianBatDau ,
                            tchdctp.DeletedStatus ,
                            hd.NgayDanhSoHopDong ,
                            hd.SysNhanVienREF ,
                            hd.DmMaHopDongREF ,
                            hd.TenDangNhap ,
                            hd.TenKhachHang ,
                            hd.TrangThaiHopDong ,
                            hdct.DeletedStatus DeletedStatusHDCT
                  FROM      (SELECT * FROM ThucChayHopDongChiTietPR WHERE HopDongREF = @pHopDongID AND DmSanPhamREF = @pDmSanPhamREF)tchdctp
                            INNER JOIN dbo.ThucChay_ThongTinHopDongChiTietID_PR tctthdctip ON tctthdctip.ThucChayHopDongChiTietPRID = tchdctp.ThucChayHopDongChiTietPRID
							--INNER JOIN dbo.ThucChayDaTinh tcdt ON tcdt.DotChayBooking = CONVERT(NVARCHAR(1000), tchdctp.ThucChayHopDongChiTietPRID)
                            INNER JOIN (SELECT * FROM dbo.HopDong WHERE HopDongID = @pHopDongID) hd ON hd.HopDongID = tchdctp.HopDongREF
                            INNER JOIN (SELECT * FROM dbo.HopDongChiTiet WHERE HopDongFK = @pHopDongID AND DmSanPhamREF = @pDmSanPhamREF) hdct ON tctthdctip.HopDongChiTietID = hdct.HopDongChiTietID
                            LEFT JOIN (SELECT * FROM dbo.HopDongThayDoi WHERE HopDongFK = @pHopDongID) hdtd ON hd.HopDongID = hdtd.HopDongFK
                  WHERE     tchdctp.ThoiGianBatDau IS NOT NULL --AND tchdctp.HopDongREF = 500395
                            AND ( CASE WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt
                                       THEN CONVERT(DATE, tchdctp.CreatedAt)
                                       ELSE CONVERT(DATE, tchdctp.LastModifiedAt)
                                  END ) >= CONVERT(DATE, tchdctp.ThoiGianBatDau)--Haidh: Note cho nay dang can nhac 11-10-2013
                            AND ( ( ( CASE WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt
                                           THEN CONVERT(DATE, tchdctp.CreatedAt)
                                           ELSE CONVERT(DATE, tchdctp.LastModifiedAt)
                                      END ) = @NgayThucHien )
                                  OR ( CONVERT(DATE, hdtd.NgayThayDoi) = @NgayThucHien
                                       AND ( CASE WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt
                                                  THEN CONVERT(DATE, tchdctp.CreatedAt)
                                                  ELSE CONVERT(DATE, tchdctp.LastModifiedAt)
                                             END ) < @NgayThucHien
                                     )
									OR ( CONVERT(DATE, hd.LastModifiedAt) = @NgayThucHien )
									OR ( CONVERT(DATE, hdct.LastModifiedAt) = @NgayThucHien )
                                )
                            AND CONVERT(DATE, tchdctp.CreatedAt) <= CONVERT(DATE, tchdctp.LastModifiedAt)
                            AND CONVERT(DATE, tchdctp.ThoiGianBatDau) >= @ThoiGianBDTinh
                            AND tchdctp.RecordStatus = 1
                ) A
        ORDER BY A.HopDongREF ,
                A.HopDongChiTietREF;
	
        OPEN Record_Cursor;
	-- Perform the first fetch.
        FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @HopDongChiTietREF,
            @ThucChayHopDongChiTietPRID, @DmHinhThucQuangCaoREF, @DmSanPhamREF,
            @DmNhanHangREF, @DmViTriREF, @SoLuong, @ChietKhau, @KhuyenMai,
            @DmWebsiteREF, @GiaTien, @ThoiGianBatDau, @DeletedStatus,
            @NgayDanhSoHopDong, @SysNhanVienREF, @DmMaHopDongREF, @TenDangNhap,
            @TenKhachHang, @TrangThaiHopDong, @DeletedStatusHDCT
        WHILE @@FETCH_STATUS = 0
            BEGIN
				
                SET @SoHopDong = ( SELECT   hd.SoHopDong
                                   FROM     HopDong hd
                                   WHERE    hd.HopDongID = @HopDongREF
                                 )

		--*********CHECK THONG TIN THAY DOI CUA THUC TREO PR
                IF ( @DeletedStatus = 1 )
                    BEGIN
						--PRINT '@DeletedStatus = 1'
                        SET @LoaiThayDoi = 3; --HUY THUC TREO
                        SET @GiaTriThayDoiHT = 0
                        SET @SoLuongThayDoi = 0
			--INSERT GIA TRI THAY DOI 
                        SET @CONTENT_LOG = N'Thực treo hủy ' + CONVERT(NVARCHAR(50), @NgayThucHien)
                        EXEC [dbo].[sp_TC_ThucTreoHuy_PR] @ThucChayHopDongChiTietPRID,
                            @HopDongREF, @NgayThucHien, @GiaTriThayDoiHT,
                            @SoLuongThayDoi	, @HopDongChiTietREF	
							
						EXEC  [dbo].[sp_TC_TinhLaiGiaTriThayDoi_ThucChayDaTinh_PR_ByHopDongID]
								@StartDate = @NgayDanhSoHopDong ,
								@EndDate = @NgayThucHien ,
								@NgayThucHien = @NgayThucHien,
								@DmSanPhamREF = @DmSanPhamREF,
								@pHopDongID = @HopDongREF,
								@GhiChu = N'Ghi nhận thực chạy lại của hợp đồng khi thực treo hủy'		
                    END;
                ELSE
                    IF ( @TrangThaiHopDong = 3 )
                        BEGIN
							--PRINT '@TrangThaiHopDong = 3'
                            SET @LoaiThayDoi = 4; --Hủy hợp đồng
                            SET @GiaTriThayDoiHT = 0
                            SET @SoLuongThayDoi = 0

                            SET @CONTENT_LOG = N'Hợp đồng hủy '
                                + CONVERT(NVARCHAR(50), @NgayThucHien)
                            EXEC [dbo].[sp_TC_HopDongHuy_PR] @ThucChayHopDongChiTietPRID,
                                @HopDongREF, @NgayThucHien, @GiaTriThayDoiHT,
                                @SoLuongThayDoi	, @HopDongChiTietREF
                        END
                    ELSE
                        IF ( @DeletedStatusHDCT = 1 )
                            BEGIN
							--PRINT '@DeletedStatusHDCT = 1'
                                SET @LoaiThayDoi = 5; --Hủy hợp đồng chi tiết
                                SET @GiaTriThayDoiHT = 0
                                SET @SoLuongThayDoi = 0

                                SET @CONTENT_LOG = N'Hợp đồng chi tiết hủy '
                                    + CONVERT(NVARCHAR(50), @NgayThucHien)
                                EXEC [dbo].[sp_TC_HopDongChiTietHuy_PR] @ThucChayHopDongChiTietPRID,
                                    @HopDongREF, @NgayThucHien,
                                    @GiaTriThayDoiHT, @SoLuongThayDoi	, @HopDongChiTietREF
                            END
                        ELSE
                            BEGIN



                                DECLARE @DmSanPhamREF_Bf INT ,
                                    @DmHinhThucQuangCaoREF_Bf INT;
                                DECLARE @DmNhanHangREF_Bf INT ,
                                    @DmWebsiteREF_Bf INT;
                                DECLARE @DmViTriREF_Bf INT ,
                                    @GiaTien_Bf FLOAT ,
                                    @ChietKhau_Bf FLOAT ,
                                    @NgayThucHien_Bf DATETIME;
                                DECLARE @SoHopDong_Bf NVARCHAR(50) ,
                                    @NgayDanhSoHopDong_Bf DATETIME ,
                                    @SysNhanVienREF_Bf INT ,
                                    @DmMaHopDongREF_Bf INT ,
                                    @TenDangNhap_Bf NVARCHAR(25);
                                DECLARE @TenKhachHang_Bf NVARCHAR(255);
	
	
                                SELECT TOP 1
                                        @DmHinhThucQuangCaoREF_Bf = tcdt.DmHinhThucQuangCao ,
                                        @DmSanPhamREF_Bf = tcdt.DmSanPhamREF ,
                                        @DmNhanHangREF_Bf = CONVERT(INT, tcdt.NhanHang) ,
                                        @DmWebsiteREF_Bf = tcdt.DmWebsiteREF ,
                                        @DmViTriREF_Bf = tcdt.DmViTriREF ,
                                        @GiaTien_Bf = tcdt.DonGiaTheoDonVi ,
                                        @ChietKhau_Bf = tcdt.ChietKhau ,
                                        @NgayThucHien_Bf = tcdt.NgayThucHien ,
                                        @SoHopDong_Bf = tcdt.SoHopDong ,
                                        @NgayDanhSoHopDong_Bf = tcdt.NgayDanhSoHopDong ,
                                        @SysNhanVienREF_Bf = tcdt.SysNhanVienREF ,
                                        @DmMaHopDongREF_Bf = tcdt.DmMaHopDongREF ,
                                        @TenDangNhap_Bf = tcdt.TenDangNhap ,
                                        @TenKhachHang_Bf = tcdt.TenKhachHang
                                FROM    ThucChayDaTinh tcdt
                                WHERE   tcdt.HopDongID = @HopDongREF
                                        AND tcdt.NgayThucHien < @NgayThucHien
                                        AND tcdt.DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID)
                                        AND tcdt.NgayThucHien >= @ThoiGianBatDauCheck
										AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
										AND ( tcdt.SoLuongThucChay <> 0
											OR tcdt.SoLuongThayDoi <> 0
											OR tcdt.SoLuongThucChayKM <> 0
											OR tcdt.ThanhTienSauTrietKhauThucChay <> 0
											OR tcdt.ThanhTienKM <> 0
											OR tcdt.GiaTriThayDoi <> 0)
                                ORDER BY tcdt.NgayThucHien DESC ,tcdt.CreatedAt DESC;


								--SELECT @ThucChayHopDongChiTietPRID
								--SELECT @HopDongREF

                                IF EXISTS (SELECT TOP 1
												tcdt.DmHinhThucQuangCao ,
												tcdt.DmSanPhamREF ,
												CONVERT(INT, tcdt.NhanHang) ,
												tcdt.DmWebsiteREF ,
												tcdt.DmViTriREF ,
												tcdt.DonGiaTheoDonVi ,
												tcdt.ChietKhau ,
												tcdt.NgayThucHien ,
												tcdt.SoHopDong ,
												tcdt.NgayDanhSoHopDong ,
												tcdt.SysNhanVienREF ,
												tcdt.DmMaHopDongREF ,
												tcdt.TenDangNhap ,
												tcdt.TenKhachHang
										FROM    ThucChayDaTinh tcdt
										WHERE   tcdt.HopDongID = @HopDongREF
												AND tcdt.NgayThucHien < @NgayThucHien
												AND tcdt.DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID)
												AND tcdt.NgayThucHien >= @ThoiGianBatDauCheck
												AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
												AND (tcdt.SoLuongThucChay <> 0
													OR tcdt.SoLuongThayDoi <> 0
													OR tcdt.SoLuongThucChayKM <> 0
													OR tcdt.ThanhTienSauTrietKhauThucChay <> 0
													OR tcdt.ThanhTienKM <> 0
													OR tcdt.GiaTriThayDoi <> 0)
										ORDER BY tcdt.NgayThucHien DESC ,tcdt.CreatedAt DESC)
								BEGIN
								    IF ( @NgayThucHien > @NgayThucHien_Bf )
                                    BEGIN
										
                                        IF ( ( @DmHinhThucQuangCaoREF_Bf <> @DmHinhThucQuangCaoREF )
                                             OR ( @DmSanPhamREF_Bf <> @DmSanPhamREF )
                                             OR ( @DmNhanHangREF_Bf <> @DmNhanHangREF )
                                             OR ( @DmWebsiteREF_Bf <> @DmWebsiteREF )
                                             OR ( @DmViTriREF_Bf <> @DmViTriREF )
                                             OR ( @SoHopDong_Bf <> @SoHopDong )
                                             OR ( @NgayDanhSoHopDong_Bf <> @NgayDanhSoHopDong )
                                             OR ( @SysNhanVienREF_Bf <> @SysNhanVienREF )
                                             OR ( @DmMaHopDongREF_Bf <> @DmMaHopDongREF )
                                             OR ( @TenDangNhap_Bf <> @TenDangNhap )
                                             --OR ( @TenKhachHang_Bf <> @TenKhachHang )
                                           )
                                            BEGIN
												--PRINT @HopDongREF
												--PRINT @ThucChayHopDongChiTietPRID

                                                SET @LoaiThayDoi = 2; --THAY DOI THONG TIN THUC CHAY

                                                SET @CONTENT_LOG = N'(Có thay đổi thực treo, Thông tin thay đổi:'

                                                IF @DmHinhThucQuangCaoREF_Bf <> @DmHinhThucQuangCaoREF
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Hình thức quảng cáo: '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmHinhThucQuangCaoREF_Bf, 'null'))
                                                            + N' -> '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmHinhThucQuangCaoREF, 'null'))
                                                    END
                                                IF @DmSanPhamREF_Bf <> @DmSanPhamREF
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Sản phẩm: '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmSanPhamREF_Bf, 'null'))
                                                            + N' -> '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmSanPhamREF, 'null'))
                                                    END
                                                IF @DmWebsiteREF_Bf <> @DmWebsiteREF
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Website: '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmWebsiteREF_Bf, 'null'))
                                                            + N' -> '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmWebsiteREF, 'null'))
                                                    END
                                                IF @DmViTriREF_Bf <> @DmViTriREF
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Vị trí: '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmViTriREF_Bf, 'null'))
                                                            + N' -> '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmViTriREF, 'null'))
                                                    END
                                                IF @SoHopDong_Bf <> @SoHopDong
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Số hợp đồng: '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@SoHopDong_Bf, 'null'))
                                                            + N' -> '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@SoHopDong, 'null'))
                                                    END
                                                IF @NgayDanhSoHopDong_Bf <> @NgayDanhSoHopDong
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Ngày số hợp đồng: '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@NgayDanhSoHopDong_Bf, 'null'))
                                                            + N' -> '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@NgayDanhSoHopDong, 'null'))
                                                    END
                                                IF @SysNhanVienREF_Bf <> @SysNhanVienREF
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Nhân viên: '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@SysNhanVienREF_Bf, 'null'))
                                                            + N' -> '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@SysNhanVienREF, 'null'))
                                                    END
                                                IF @DmMaHopDongREF_Bf <> @DmMaHopDongREF
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Mã hợp đồng: '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmMaHopDongREF_Bf, 'null'))
                                                            + N' -> '
                                                            + CONVERT(NVARCHAR(500), ISNULL(@DmMaHopDongREF, 'null'))
                                                    END
                                                IF @TenDangNhap_Bf <> @TenDangNhap
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Tên đăng nhập: '
                                                            + ISNULL(@TenDangNhap_Bf, 'null')
                                                            + N' -> '
                                                            + ISNULL(@TenDangNhap, 'null')
                                                    END
                                                IF @TenKhachHang_Bf <> @TenKhachHang
                                                    BEGIN
                                                        SET @CONTENT_LOG = @CONTENT_LOG
                                                            + N'Tên khách hàng: '
                                                            + ISNULL(@TenKhachHang_Bf, 'null')
                                                            + N' -> '
                                                            + ISNULL(@TenKhachHang, 'null')
                                                    END
													--PRINT @CONTENT_LOG
                                            END
                    
                                        ELSE
                                            BEGIN
                                                IF ( ( @GiaTien_Bf <> @GiaTien )
                                                     OR ( @ChietKhau_Bf <> @ChietKhau )
                                                   )
												   BEGIN
														SET @LoaiThayDoi = 1; 
														SET @TaiSao = @TaiSao + CONVERT(NVARCHAR(50), ISNULL(@GiaTien_Bf, 'NULL')) + ' ' + CONVERT(NVARCHAR(50), ISNULL(@GiaTien, 'NULL'))+ ' ' + CONVERT(NVARCHAR(50), ISNULL(@ChietKhau_Bf, 'NULL'))+ ' ' + CONVERT(NVARCHAR(50), ISNULL(@ChietKhau, 'NULL'))
												   END
                                                    
                                            END
                    
                                    END;
								END
								



									
                                IF ( @LoaiThayDoi = 1 )
                                    BEGIN
					
                                        SELECT  @ThanhTienThucChayDaTinh = SUM(tcdt.ThanhTienSauTrietKhauThucChay
                                                              + tcdt.GiaTriThayDoi) ,
                                                @SoLuongThucChay = SUM(tcdt.SoLuongThucChay
                                                              + tcdt.SoLuongThayDoi)
                                        FROM    ThucChayDaTinh tcdt
                                        WHERE   1 = 1
                                                AND tcdt.HopDongID = @HopDongREF
                                                AND tcdt.TrangThaiHopDong <> 3
                                                AND tcdt.DmSanPhamREF = @DmSanPhamREF
                                                AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF
                                                AND tcdt.NgayThucHien <= @NgayThucHien
                                                AND tcdt.NgayThucHien >= @ThoiGianBatDauCheck
                                                AND tcdt.DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID);
					
                                        SET @GiaTriThayDoiHT = ( ( ( @GiaTien
                                                              * @SoLuong )
                                                              * ( 100
                                                              - @ChietKhau ) )
                                                              / 100 )
                                        SET @SoLuongThayDoi = @SoLuong
                                            - @SoLuongThucChay; 
					--INSERT THONG TIN THAY DOI GIA TRI
                                        SET @CONTENT_LOG = N'(Có thay đổi thực treo, Giá trị:'
                                            + CONVERT(NVARCHAR(20), CONVERT(BIGINT, @ThanhTienThucChayDaTinh))
                                            + '->'
                                            + CONVERT(NVARCHAR(20), CONVERT(BIGINT, @GiaTien
                                            * ( 100 - @ChietKhau ) / 100));
					

											SELECT @GiaTriThayDoiHT
                                        --EXEC [dbo].[sp_TC_InsertThucTreoGiaTriThayDoi_PR] @ThucChayHopDongChiTietPRID,
                                        --    @NgayThucHien, @GiaTriThayDoiHT,
                                        --    @SoLuongThayDoi;

										
										EXEC [dbo].[sp_TC_InsertThucTreoThongTinThayDoi_PR] @ThucChayHopDongChiTietPRID,
                                                @HopDongREF, @NgayThucHien,
                                                @GiaTriThayDoiHT,
                                                @SoLuongThayDoi, @TaiSao, @HopDongChiTietREF
						
                                    END;	
                                ELSE
                                    IF ( @LoaiThayDoi = 2 )
                                        BEGIN
                                            SET @GiaTriThayDoiHT = ( ( ( @GiaTien
                                                              * @SoLuong )
                                                              * ( 100
                                                              - @ChietKhau ) )
                                                              / 100 );
                                            SET @SoLuongThayDoi = @SoLuong;

					
                                            EXEC [dbo].[sp_TC_InsertThucTreoThongTinThayDoi_PR] @ThucChayHopDongChiTietPRID,
                                                @HopDongREF, @NgayThucHien,
                                                @GiaTriThayDoiHT,
                                                @SoLuongThayDoi	, @CONTENT_LOG, @HopDongChiTietREF
                                        END;					
                            END;

							
			IF @LoaiThayDoi <> 0
				BEGIN
				    --1.3 GHI LOG
                SET @NGUON_LOG = 'Table:ThucChayHopDongChiTietPR, NgayThucHien:'
                    + CONVERT(NVARCHAR(20), @NgayThucHien) + ', TCHDCTPR:'
                    + CONVERT(NVARCHAR(20), @ThucChayHopDongChiTietPRID)
			--GHI LOG VIEC THAY DOI
			
                INSERT  INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
                        ( [ThuChay_LogNNTinhGiaTriThayDoiID] ,
                          [HopDongREF] ,
                          [SoHopDong] ,
                          [HopDongChiTietREF] ,
                          [DmSanPhamREF] ,
                          [DmWebsiteREF] ,
                          [NgayThucHien] ,
                          [GiaTriThayDoi] ,
                          [GiaSauCK1] ,
                          [Soluong1] ,
                          [GiaSauCK2] ,
                          [Soluong2] ,
                          [NoiDungLog] ,
                          [NguonLog] ,
                          [GhiChu] ,
                          [CreatedBy] ,
                          [CreatedAt] ,
                          [LastModifiedBy] ,
                          [LastModifiedAt] ,
                          [DeletedStatus] ,
                          [PrintStatus] ,
                          [RecordStatus]
			            )
                VALUES  ( NEWID() ,
                          @HopDongREF ,
                          @SoHopDong ,
                          0 ,
                          @DmSanPhamREF ,
                          @DmWebsiteREF ,
                          @NgayThucHien ,
                          @GiaTriThayDoiHT ,
                          0 ,
                          0 ,
                          0 ,
                          0 ,
                          @CONTENT_LOG ,
                          @NGUON_LOG ,
                          'PR' ,
                          'ThucChay' ,
                          GETDATE() ,
                          'ThucChay' ,
                          GETDATE() ,
                          0 ,
                          0 ,
                          0
			            )
				END
			
					
					
					SET @LoaiThayDoi = 0	
					SET @CONTENT_LOG = ''		
					SET @NGUON_LOG = ''
					SET @TaiSao = ''

                FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @HopDongChiTietREF,
            @ThucChayHopDongChiTietPRID, @DmHinhThucQuangCaoREF, @DmSanPhamREF,
            @DmNhanHangREF, @DmViTriREF, @SoLuong, @ChietKhau, @KhuyenMai,
            @DmWebsiteREF, @GiaTien, @ThoiGianBatDau, @DeletedStatus,
            @NgayDanhSoHopDong, @SysNhanVienREF, @DmMaHopDongREF, @TenDangNhap,
            @TenKhachHang, @TrangThaiHopDong, @DeletedStatusHDCT
            END;
        CLOSE Record_Cursor
        DEALLOCATE Record_Cursor
    END;



```
