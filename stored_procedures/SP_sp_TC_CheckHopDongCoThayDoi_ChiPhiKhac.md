# Stored Procedure: `sp_TC_CheckHopDongCoThayDoi_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:20:32.687000
- **Ngày sửa cuối**: 2024-09-09 16:00:16.520000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [ThucChay_CheckHopDongCoThayDoi_ChiPhiKhac] 42795, 'QC2790416', 96074, '2017-02-16'
-- EXEC sp_TC_CheckHopDongCoThayDoi_ChiPhiKhac 502184, 'QC0720517', 505295, '2017-06-19'
CREATE PROCEDURE [dbo].[sp_TC_CheckHopDongCoThayDoi_ChiPhiKhac] 
	-- Add the parameters for the stored procedure here
    @HopDongREF INT ,
    @SoHopDong NVARCHAR(50) ,
    @HopDongChiTietID INT ,
    @NgayThucHien DATETIME
AS
    BEGIN
        DECLARE @CountHDTD INT ,
            @CountHDED INT ,
            @HopDongChiTietThayDoiCK INT ,
            @ChietKhau INT ,
            @HopDongChiTiet INT
        DECLARE @DmSanPhamREF INT ,
            @DmWebsiteREF INT ,
            @TenWebsite NVARCHAR(100) ,
            @CONTENT_LOG NVARCHAR(200) ,
            @NGUON_LOG NVARCHAR(200)
        DECLARE @GiaTien BIGINT ,
            @SoluongThucChay INT ,
            @GiaTienSauCK BIGINT ,
            @NgayGioiHanTinh DATETIME
        DECLARE @isKhuyenMai INT ,
            @ThanhTienDaTinh FLOAT ,
            @GiaTriThayDoiHT FLOAT ,
            @ISEXIST_HDCT INT ,
            @GiaTriThayDoiBF FLOAT ,
            @ThanhTienHDCT FLOAT ,
            @TrangThaiHopDong INT ,
            @DeletedStatus INT ,
            @GiaTriThayDoi FLOAT ,
            @SoLuongThayDoi INT,
			@HopDongHuy INT
	
        SET @CountHDTD = 0
        SET @CountHDED = 0
        SET @ThanhTienDaTinh = 0
        SET @NgayGioiHanTinh = '2013-01-01'
        SET @GiaTien = 0
        SET @SoluongThucChay = 0 
        SET @GiaTienSauCK = 0
        SET @ISEXIST_HDCT = 0
        SET @GiaTriThayDoiHT = 0
        SET @ThanhTienDaTinh = 0
        SET @GiaTriThayDoiBF = 0
        SET @GiaTriThayDoi = 0
        SET @SoLuongThayDoi = 0

	
		--XOA BAN NHUNG BAN GHI DA THUC HIEN INSERT VOI TRUONG HOP CHI CO GIA TRI THAY DOI
        DELETE  FROM dbo.ThucChayDaTinh
        WHERE   HopDongChiTietREF = @HopDongChiTietID
                AND CONVERT(DATE, NgayThucHien) = @NgayThucHien
                AND DotChayHopDong = 'CPK_TTR'
		
		--CHECK HOP DONG CO SU THAY DOI KHONG
		SELECT @HopDongHuy = hd.TrangThaiHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongREF AND hd.SoHopDong = @SoHopDong


        SET @CountHDTD = (
	                       SELECT   COUNT(*)
                           FROM     (
										SELECT hdtd.HopDongThayDoiID, hdtd.HopDongFK 
										FROM dbo.HopDongThayDoi hdtd 
										WHERE hdtd.HopDongFK = @HopDongREF
										AND CONVERT(DATE, hdtd.NgayThayDoi) = @NgayThucHien
									) hdtd
                                    INNER JOIN 
									(SELECT hdcttd.HopDongChiTietThayDoiID, hdcttd.HopDongChiTietREF, hdcttd.HopDongFK, hdcttd.HopDongThayDoiREF 
									FROM  dbo.HopDongChiTietThayDoi hdcttd WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID )
									 hdcttd ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
                         )

		------------Tuyetnta bổ sung ------------------
        SET @CountHDED = ( SELECT   COUNT(*)
                           FROM     (
										SELECT hdctl.HopDongChiTietLogID, hdctl.HopDongChiTietREF, hdctl.HopDongFK, hdctl.ThoiGianLog, hdctl.LoaiLog 
										FROM dbo.HopDongChiTietLog hdctl 
										WHERE hdctl.HopDongChiTietREF = @HopDongChiTietID
										AND CONVERT(DATE, hdctl.ThoiGianLog) = @NgayThucHien
									)hdctl
                                    INNER JOIN 
									(
										SELECT hd.HopDongID, hd.SoHopDong, hd.TrangThaiHopDong 
										FROM dbo.HopDong hd 
										WHERE hd.HopDongID = @HopDongREF
										AND hd.TrangThaiHopDong <> 3
									) hd ON hdctl.HopDongFK = hd.HopDongID
                                    INNER JOIN 
									(
										SELECT hdct.HopDongChiTietID, hdct.HopDongFK, hdct.DmSanPhamREF, hdct.DmLoaiREF, hdct.DmLoaiBannerREF, hdct.DeletedStatus 
										FROM dbo.HopDongChiTiet hdct 
										WHERE hdct.HopDongChiTietID = @HopDongChiTietID
									
									AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										)) 	
                                    AND hdct.DmWebsiteREF NOT IN ( 285, 307 ) --loai tru phan bo co website GG,FB
                                    AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF IN ( 18 ))
									)hdct ON hdct.HopDongChiTietID = hdctl.HopDongChiTietREF
                         )

        SET @CountHDTD = ISNULL(@CountHDTD, 0)
        SET @CountHDED = ISNULL(@CountHDED, 0)
		--NEU HOP DONG CO SU THAY DOI
        IF ( @CountHDTD > 0
             OR @CountHDED > 0
			 OR @HopDongHuy = 3
           )
            BEGIN
				-- Lay thanh tien cua HDCT
                SELECT  @ThanhTienHDCT = CASE WHEN hdct.IsKhuyenMai = 1 THEN ISNULL(hdct.SoLuong, 0) * ISNULL(hdct.DonGia, 0)
											ELSE ISNULL(hdct.ThanhTien, 0)
											END--da co chiet khau
                FROM    dbo.HopDongChiTiet hdct
                        INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
                WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                        AND hdct.DeletedStatus = 0

                --SELECT  @DeletedStatus = hdct.DeletedStatus
                --FROM    dbo.HopDongChiTiet hdct
                --WHERE   hdct.HopDongChiTietID = @HopDongChiTietID

				--GET HOPDONGCHITIET LA KHUYEN MAI ?     
                SET @isKhuyenMai = ( SELECT TOP (1) hdct.IsKhuyenMai
                                     FROM   dbo.HopDongChiTiet hdct
                                     WHERE  hdct.HopDongChiTietID = @HopDongChiTietID
									 ORDER BY hdct.HopDongChiTietID
                                   )

                DECLARE @ThucTreoID NVARCHAR(1000)
		
                DECLARE icursor CURSOR
                FOR
                    SELECT DISTINCT
                            tcdt.DotChayBooking
                    FROM    dbo.ThucChayDaTinh tcdt
                    WHERE   tcdt.HopDongChiTietREF = @HopDongChiTietID
                            AND CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
                OPEN icursor  
		
                FETCH NEXT FROM icursor   INTO @ThucTreoID
		
                WHILE @@FETCH_STATUS = 0
                BEGIN  

					--CHECK NEU LA HOPDONGCHITIET KHUYEN MAI
                    IF ( @isKhuyenMai = 1 )
                        BEGIN
							--1. GET THANHTIENKHUYENMAI DA TINH CUA HOPDONGCHITIET
                            SET @ThanhTienDaTinh = ( SELECT SUM(ISNULL(tcdt.ThanhTienKM, 0) + ISNULL(tcdt.GiaTriKMThayDoi, 0))
                                                        FROM dbo.ThucChayDaTinh tcdt
                                                        WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                            AND tcdt.DotChayBooking = @ThucTreoID
                                                            AND CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
                                                    )
                            SET @ThanhTienDaTinh = ISNULL(@ThanhTienDaTinh, 0)

                            SET @SoluongThucChay = ( SELECT SUM(ISNULL(tcdt.SoLuongThucChayKM, 0) + ISNULL(tcdt.SoLuongKMThayDoi, 0))
                                                        FROM dbo.ThucChayDaTinh tcdt
                                                        WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                            AND tcdt.DotChayBooking = @ThucTreoID
                                                            AND CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
                                                    )
                            SET @SoluongThucChay = ISNULL(@SoluongThucChay, 0)

                        END
	    
					--CHECK NEU LA HOPDONGCHITIET KHONG KHUYEN MAI
                    IF ( @isKhuyenMai = 0 )
                        BEGIN
							--1. GET THANHTIENSAUTRIETKHAU DA TINH CUA HOPDONGCHITIET					
                            SET @ThanhTienDaTinh = ( SELECT SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) + ISNULL(tcdt.GiaTriThayDoi, 0))
                                                        FROM dbo.ThucChayDaTinh tcdt
                                                        WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                            AND tcdt.DotChayBooking = @ThucTreoID
                                                            AND CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
                                                    )
                            SET @ThanhTienDaTinh = ISNULL(@ThanhTienDaTinh, 0)

                            SET @SoluongThucChay = ( SELECT SUM(ISNULL(tcdt.SoLuongThucChay, 0) + ISNULL(tcdt.SoLuongThayDoi, 0))
                                                        FROM dbo.ThucChayDaTinh tcdt
                                                        WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                            AND tcdt.DotChayBooking = @ThucTreoID
                                                            AND CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
                                                    )
                            SET @SoluongThucChay = ISNULL(@SoluongThucChay, 0)
			
                        END

					SET @DmSanPhamREF = 0
					SET @DmWebsiteREF = 0

					SELECT  @DmSanPhamREF = hdct.DmSanPhamREF ,
							@DmWebsiteREF = hdct.DmWebsiteREF
					FROM    dbo.HopDongChiTiet hdct
					WHERE   hdct.HopDongChiTietID = @HopDongChiTietID

					SET @DmSanPhamREF = ISNULL(@DmSanPhamREF, 0)
					SET @DmWebsiteREF = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF)

					--Hủy hợp đồng
					IF ( @HopDongHuy = 3 )
						BEGIN
							SET @CONTENT_LOG = N'Hợp đồng hủy '
								+ CONVERT(NVARCHAR(50), @NgayThucHien)


							SET @ISEXIST_HDCT = ( SELECT  COUNT(tcdt.HopDongChiTietREF)
													FROM    dbo.ThucChayDaTinh tcdt
													WHERE   tcdt.HopDongChiTietREF = @HopDongChiTietID
															AND tcdt.DotChayBooking = @ThucTreoID
															AND CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
												)

							SET @GiaTriThayDoi = -1 * @ThanhTienDaTinh
							SET @SoLuongThayDoi = -1 * @SoluongThucChay
							--1.1 NEU DA TON TAI BAN GHI CUA HOPDONGCHITIET TAI NGAY HIEN TAI THI THUC HIEN UPDATE GIA TRI THAY DOI
							IF ( @ISEXIST_HDCT > 0 )
								BEGIN
									UPDATE  dbo.ThucChayDaTinh
									SET     GiaTriThayDoi = @GiaTriThayDoi ,
											SoLuongThayDoi = @SoLuongThayDoi ,
											LastModifiedAt = GETDATE()
									WHERE   HopDongChiTietREF = @HopDongChiTietID
											AND DotChayBooking = @ThucTreoID
											AND CONVERT(DATE, NgayThucHien) = @NgayThucHien
								END

							--1.2 NEU CHUA TON TAI THI TAO BAN GHI MOI CHO HOPDONGCHITIET TAI NGAY HIEN TAI VOI SO TIEN KHUYEN MAI	
							IF ( @ISEXIST_HDCT = 0 )
								BEGIN

									EXEC dbo.sp_TC_InsertThucTreoThayDoi_ChiPhiKhac @HopDongChiTietID,
										@NgayThucHien, @GiaTriThayDoi,
										@ThucTreoID, @SoLuongThayDoi, @CONTENT_LOG
								END
	
								UPDATE  dbo.ThucChayHopDongChiTiet
								SET     RecordStatus = 0
								WHERE   CONVERT(NVARCHAR(1000), ThucChayHopDongChiTietID) = @ThucTreoID
						END

					DECLARE @TongThanhTienDaTinh FLOAT
					--CHECK NEU LA HOPDONGCHITIET KHUYEN MAI
					IF ( @isKhuyenMai = 1 )
						BEGIN
							SET @TongThanhTienDaTinh = ( SELECT
															SUM(ISNULL(tcdt.ThanhTienKM,0)+ ISNULL(tcdt.GiaTriKMThayDoi,0))
															FROM dbo.ThucChayDaTinh tcdt
															WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
															AND CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
														)
							SET @TongThanhTienDaTinh = ISNULL(@TongThanhTienDaTinh,0)
						END
	    
					--CHECK NEU LA HOPDONGCHITIET KHONG KHUYEN MAI
					IF ( @isKhuyenMai = 0 )
						BEGIN				
							SET @TongThanhTienDaTinh = ( SELECT
															SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)+ ISNULL(tcdt.GiaTriThayDoi,0))
															FROM dbo.ThucChayDaTinh tcdt
															WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
															AND CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
														)
							SET @TongThanhTienDaTinh = ISNULL(@TongThanhTienDaTinh,0)

						END

					--1 IF THANHTIEN DA TINH = 0 HOAC = SO TIEN HIEN TAI THI KHONG LAM GI CA
					--1 IF THANHTIEN DA TINH <>0 VA <> SO TIEN HIEN TAI THI THUC HIEN TINH
					IF ( ( @TongThanhTienDaTinh <> 0 )
                             AND ( @TongThanhTienDaTinh > @ThanhTienHDCT )
                           )
                            BEGIN
						        SET @GiaTriThayDoi = -1 * @ThanhTienDaTinh
                                SET @SoLuongThayDoi = -1 * @SoluongThucChay
								DECLARE @TongTienTreo FLOAT = 0

								SET @TongTienTreo = ISNULL((SELECT SUM(tchdct.DonGia*tchdct.SoLuongThucTreo*(100-tchdct.ChietKhau)/100) FROM dbo.ThucchayHopDongChiTiet tchdct 
													WHERE tchdct.HopDongChiTietREF = @HopDongChiTietID
													AND tchdct.DeletedStatus = 0),0)

								--Haidh Comment 2022/08/02 TH: Gia tri treo ko thay doi , co them gia tri treo <0 
								--Neu tong gia tri thuc treo co gia tri <0 = thanhtienhdct thi ko phai doi tru
								IF((EXISTS(SELECT TOP (1) tchdct.ThucchayHopDongChiTietID FROM dbo.ThucchayHopDongChiTiet tchdct 
													WHERE tchdct.HopDongChiTietREF = @HopDongChiTietID
													AND tchdct.DonGia <0 
													ORDER BY tchdct.HopDongChiTietREF)
								) AND (@TongTienTreo<= @ThanhTienHDCT))
								BEGIN 
									PRINT 'KO PHAI DOI TRU'
								END
								ELSE --THUC HIEN DOI TRU
								BEGIN
									EXEC dbo.sp_TC_InsertThucTreoThayDoi_ChiPhiKhac @HopDongChiTietID,
                                            @NgayThucHien, @GiaTriThayDoi,
                                            @ThucTreoID, @SoLuongThayDoi, N'Thay đổi giá trị hợp đồng'
									DECLARE @KQ INT = 0
								 
									--- Tinh lai
									EXEC dbo.sp_TC_InsertThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi @ThucTreoID, @HopDongChiTietID, @NgayThucHien,  @KQ OUTPUT

									IF @KQ = 0
									BEGIN
									    UPDATE dbo.ThucChayHopDongChiTiet SET RecordStatus = 0
										WHERE ThucChayHopDongChiTietID = @ThucTreoID
											AND HopDongChiTietREF = @HopDongChiTietID
									END
								END

								----1.3 GHI LOG
        --                        SET @CONTENT_LOG = @CONTENT_LOG
        --                            + N' (Có thay đổi hợp đồng, Giá trị thực chạy cao hơn HĐCT:'
        --                            + CONVERT(NVARCHAR(20), CONVERT(BIGINT, @ThanhTienDaTinh))
        --                            + '>'
        --                            + CONVERT(NVARCHAR(20), CONVERT(BIGINT, @ThanhTienHDCT)) 
        --                        SET @NGUON_LOG = 'Table:ThucChayHopDongChiTiet CPK, NgayThucHien:'
        --                            + CONVERT(NVARCHAR(20), @NgayThucHien)
        --                            + ', HDCT:'
        --                            + CONVERT(NVARCHAR(20), @HopDongChiTietID)
												
                    END
		 
                FETCH NEXT FROM icursor  INTO @ThucTreoID 
                END   
                CLOSE icursor;  
                DEALLOCATE icursor;  

            END
    END


```
