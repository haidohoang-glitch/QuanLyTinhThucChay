# Stored Procedure: `sp_ThucChay_CheckTTTD_ThongTinTreoThayDoi_PR_HDCT_ByThucTreoHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-02-10 14:31:03.740000
- **Ngày sửa cuối**: 2020-02-10 14:39:07.377000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThoiGianBDTinh` | `datetime(8)` | No |
| `@ThucTreoHopdongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[sp_ThucChay_CheckTTTD_ThongTinTreoThayDoi_PR_HDCT_ByThucTreoHopDongChiTietPR] '2020-02-07','2019-01-01',526791
*/

CREATE PROCEDURE [dbo].[sp_ThucChay_CheckTTTD_ThongTinTreoThayDoi_PR_HDCT_ByThucTreoHopDongChiTietPR] 
    @NgayThucHien DATETIME ,
    @ThoiGianBDTinh DATETIME,
	@ThucTreoHopdongChiTietID INT
AS
    BEGIN

		SET @ThoiGianBDTinh = '2019-01-01'
        DECLARE @HopDongREF INT ,@HopDongChiTietREF INT ,@ThucChayHopDongChiTietPRID INT ,@DmHinhThucQuangCaoREF INT ,@DmSanPhamREF INT 
		,@DmNhanHangREF INT ,@DmViTriREF INT ,@SoLuong INT ,@ChietKhau FLOAT ,@KhuyenMai INT ,@DmWebsiteREF INT ,@GiaTien FLOAT 
		,@ThoiGianBatDau DATETIME , @DeletedStatus INT;
        DECLARE @LoaiThayDoi INT , @GiaTriThayDoiHT FLOAT ,@ThanhTienThucChayDaTinh FLOAT ,@ThoiGianBatDauCheck DATETIME;
		DECLARE @CONTENT_LOG NVARCHAR(MAX) = '' ,@NGUON_LOG NVARCHAR(MAX) ,@SoHopDong NVARCHAR(100);
		DECLARE @TaiSao NVARCHAR(500) = ''
        DECLARE @SoLuongThayDoi INT ,@SoLuongThucChay INT;
        DECLARE @NgayDanhSoHopDong DATETIME ,@SysNhanVienREF INT ,@DmMaHopDongREF INT ,@TenDangNhap NVARCHAR(25);
        DECLARE @TenKhachHang NVARCHAR(255);
        DECLARE @TrangThaiHopDong INT
        DECLARE @DeletedStatusHDCT INT
		DECLARE @NgayDanhSoGioiHan DATETIME = '2020-01-01'
	
        SET @LoaiThayDoi = 0; --LOAI THAY DOI : 1 CHI THAY DOI GIA TRI, 2 THAY DOI THONG TIN, 3 THUC TREO BI HUY, 0 KHONG THAY DOI GIA TRI HOAC THONG TIN     
        SET @GiaTriThayDoiHT = 0;
        SET @ThanhTienThucChayDaTinh = 0;
        SET @ThoiGianBatDauCheck = '2019-01-01';
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
                  FROM      dbo.ThucChayHopDongChiTietPR tchdctp
                            INNER JOIN (SELECT * FROM dbo.HopDong hd WHERE hd.TrangThaiHopDong NOT IN (0,3)) hd ON hd.HopDongID = tchdctp.HopDongREF
                            INNER JOIN (SELECT * FROM dbo.HopDongChiTiet hdct WHERE hdct.DeletedStatus = 0)hdct ON tchdctp.HopDongChiTietREF = hdct.HopDongChiTietID
                            LEFT JOIN dbo.HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK
                  WHERE     tchdctp.ThoiGianBatDau IS NOT NULL 
                            AND ( ( CONVERT(DATE, tchdctp.LastModifiedAt) = @NgayThucHien )
									OR ( CONVERT(DATE, hdtd.NgayThayDoi) = @NgayThucHien
										   AND CONVERT(DATE, tchdctp.LastModifiedAt) < @NgayThucHien )
									OR ( CONVERT(DATE, hd.LastModifiedAt) = @NgayThucHien )
									OR ( CONVERT(DATE, hdct.LastModifiedAt) = @NgayThucHien )
                                )
                            AND CONVERT(DATE, tchdctp.ThoiGianBatDau) >= @ThoiGianBDTinh
                            AND tchdctp.RecordStatus = 1
							AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan ---pp mapping hdct chi ap dung voi hd 2020
                ) A
				WHERE A.ThucChayHopDongChiTietPRID = @ThucTreoHopdongChiTietID
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
				
                SET @SoHopDong = ( SELECT   TOP (1) hd.SoHopDong
                                   FROM     dbo.HopDong hd
                                   WHERE    hd.HopDongID = @HopDongREF ORDER BY hd.HopDongID )

				--*********CHECK THONG TIN THAY DOI CUA THUC TREO PR
                IF ( @DeletedStatus = 1 )
                    BEGIN
						PRINT '@DeletedStatus = 1'
                        SET @LoaiThayDoi = 3; --HUY THUC TREO
                        SET @GiaTriThayDoiHT = 0
                        SET @SoLuongThayDoi = 0
						--INSERT GIA TRI THAY DOI 
                        SET @CONTENT_LOG = N'Thực treo hủy ' + CONVERT(NVARCHAR(50), @NgayThucHien)

                        EXEC [dbo].[ThucChay_Insert_GTTD_ThucTreoHuy_PR_HDCT]
							@ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID ,
							@HopDongID = @HopDongREF ,
							@NgaythucHien = @NgayThucHien ,
							@HopDongChiTietREF = @HopDongChiTietREF

                    END;
                ELSE
                    BEGIN

                        DECLARE @DmSanPhamREF_Bf INT , @DmHinhThucQuangCaoREF_Bf INT;
                        DECLARE @DmNhanHangREF_Bf INT , @DmWebsiteREF_Bf INT;
                        DECLARE @DmViTriREF_Bf INT , @GiaTien_Bf FLOAT , @ChietKhau_Bf FLOAT ,
							@SoLuongThucChay_Bf INT, @NgayThucHien_Bf DATETIME;
                        DECLARE @SoHopDong_Bf NVARCHAR(50) , @NgayDanhSoHopDong_Bf DATETIME ,
                            @SysNhanVienREF_Bf INT , @DmMaHopDongREF_Bf INT , @TenDangNhap_Bf NVARCHAR(25);
                        DECLARE @TenKhachHang_Bf NVARCHAR(255), @HopDongChiTietID_Bf INT;

                        SELECT TOP (1)
                                @DmHinhThucQuangCaoREF_Bf = tcdt.DmHinhThucQuangCao ,
                                @DmSanPhamREF_Bf = tcdt.DmSanPhamREF ,
                                @DmNhanHangREF_Bf = CONVERT(INT, tcdt.NhanHang) ,
                                @DmWebsiteREF_Bf = tcdt.DmWebsiteREF ,
                                @DmViTriREF_Bf = tcdt.DmViTriREF ,
                                @GiaTien_Bf = tcdt.DonGiaTheoDonVi ,
                                @ChietKhau_Bf = tcdt.ChietKhau ,
								@SoLuongThucChay_Bf = tcdt.SoLuongThucChay,
                                @NgayThucHien_Bf = tcdt.NgayThucHien ,
                                @SoHopDong_Bf = tcdt.SoHopDong ,
                                @NgayDanhSoHopDong_Bf = tcdt.NgayDanhSoHopDong ,
                                @SysNhanVienREF_Bf = tcdt.SysNhanVienREF ,
                                @DmMaHopDongREF_Bf = tcdt.DmMaHopDongREF ,
                                @TenDangNhap_Bf = tcdt.TenDangNhap ,
                                @TenKhachHang_Bf = tcdt.TenKhachHang,
								@HopDongChiTietID_Bf = tcdt.HopDongChiTietREF
                        FROM    dbo.ThucChayDaTinh tcdt
                        WHERE   tcdt.HopDongID = @HopDongREF
                                AND tcdt.NgayThucHien < @NgayThucHien
                                AND tcdt.DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID)
                                AND tcdt.NgayThucHien >= @ThoiGianBatDauCheck
								--AND tcdt.HopDongChiTietREF = @HopDongChiTietREF -- phuc vu cho viec chekc HopDongChiTietID thay doi
								AND ( tcdt.SoLuongThucChay <> 0
									OR tcdt.SoLuongThayDoi <> 0
									OR tcdt.SoLuongThucChayKM <> 0
									OR tcdt.ThanhTienSauTrietKhauThucChay <> 0
									OR tcdt.ThanhTienKM <> 0
									OR tcdt.GiaTriThayDoi <> 0)
                        ORDER BY tcdt.NgayThucHien DESC ,tcdt.CreatedAt DESC;

                        IF EXISTS (SELECT TOP (1)
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
								FROM    dbo.ThucChayDaTinh tcdt
								WHERE   tcdt.HopDongID = @HopDongREF
										AND tcdt.NgayThucHien < @NgayThucHien
										AND tcdt.DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID)
										AND tcdt.NgayThucHien >= @ThoiGianBatDauCheck
										--AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
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
										
                                    )
                                    BEGIN
										--PRINT @HopDongREF
										--PRINT @ThucChayHopDongChiTietPRID

                                        SET @LoaiThayDoi = 2; --THAY DOI THONG TIN THUC CHAY
										PRINT @LoaiThayDoi;

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
									--NEU THAY DOI GIA TRI
									IF ( ( @GiaTien_Bf <> @GiaTien )
                                                OR ( @ChietKhau_Bf <> @ChietKhau )
												OR (@SoLuongThucChay_Bf <> @SoLuong)
                                            )
											BEGIN
												SET @LoaiThayDoi = 1; 
												SET @TaiSao = N'PR: Thay đổi thông tin Đơn giá hoặc Chiết khấu hoặc Số lượng treo'
											END
								--NEU THAY DOI HOPDONGCHITIET
								IF (@HopDongChiTietID_Bf <> @HopDongChiTietREF)
								BEGIN
									SET @LoaiThayDoi = 4 --THAY DOI HOPDONGCHITIETID
								END
                            END;
						END
						PRINT 'Check va tinh'
						PRINT @LoaiThayDoi
                        IF ( @LoaiThayDoi = 1 )
                            BEGIN
								
								--INSERT THONG TIN THAY DOI GIA TRI
                                SET @CONTENT_LOG = N'(Có thay đổi thực treo, Giá trị'
                                    + CONVERT(NVARCHAR(20), CONVERT(BIGINT, @ThanhTienThucChayDaTinh))
                                    + '->'
                                    + CONVERT(NVARCHAR(20), CONVERT(BIGINT, @GiaTien
                                    * ( 100 - @ChietKhau ) / 100));
					
								EXEC [dbo].[ThucChay_Insert_GTTD_ThucTreoThongTinThayDoi_PR_HDCT]
									@ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID ,
									@HopDongID = @HopDongREF ,
									@NgaythucHien = @NgayThucHien ,
									@GhiChu = @CONTENT_LOG ,
									@HopDongChiTietID = @HopDongChiTietREF
                            END;	
                        ELSE
                            IF ( @LoaiThayDoi = 2 )
                                BEGIN
                                    EXEC [dbo].[ThucChay_Insert_GTTD_ThucTreoThongTinThayDoi_PR_HDCT]
									@ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID ,
									@HopDongID = @HopDongREF ,
									@NgaythucHien = @NgayThucHien ,
									@GhiChu = @CONTENT_LOG ,
									@HopDongChiTietID = @HopDongChiTietREF
                                END;
								ELSE IF(@LoaiThayDoi = 4)
								BEGIN
									PRINT 'vao 4'
									 SET @CONTENT_LOG = N'Có thay đổi thông tin thực treo HDCT: ' + CONVERT(NVARCHAR(20),@HopDongChiTietID_Bf) + ' -> ' 
									 + CONVERT(NVARCHAR(20),@HopDongChiTietREF);
								    --THAY DOI HOPDONGCHITIETID
									 EXEC [dbo].[ThucChay_Insert_GTTD_ThucTreoThongTinThayDoi_HDCT_PR_HDCT]
									@ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID ,
									@HopDongID = @HopDongREF ,
									@NgaythucHien = @NgayThucHien ,
									@GhiChu = @CONTENT_LOG 
								END				
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
