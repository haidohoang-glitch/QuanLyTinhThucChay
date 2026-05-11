# Stored Procedure: `sp_TC_CheckThucTreoThayDoi_ChiPhiKhac_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-29 16:50:23.003000
- **Ngày sửa cuối**: 2021-05-21 16:29:43.283000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThoiGianBDTinh` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
Exec [dbo].[sp_TC_CheckThucTreoThayDoi_ChiPhiKhac_ByHopDong] '2019-05-28','2010-01-01', 1013005
*/
CREATE PROCEDURE [dbo].[sp_TC_CheckThucTreoThayDoi_ChiPhiKhac_ByHopDong] 
-- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME ,
    @ThoiGianBDTinh DATETIME,
	@HopDongID INT
AS
    BEGIN
	-- Declare the return variable here
        DECLARE @HopDongREF INT ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietID INT ,
            @DmSanPhamREF INT ,
            @DmWebsiteREF INT
        DECLARE @GiaTien FLOAT ,
            @SoluongThucChay INT ,
            @isKhuyenMai INT ,
            @GiaTriThayDoiBF FLOAT ,
            @GiaTriThayDoi FLOAT ,
            @DonGiaHDCT FLOAT
        DECLARE @ThanhTienDaTinh FLOAT ,
            @ChietKhau INT ,
            @ISEXIST_HDCT INT ,
            @GiaTienSauCK FLOAT ,
            @ThanhTienThucTreo FLOAT
        DECLARE @GiaTriThayDoiHT FLOAT ,
            @CONTENT_LOG NVARCHAR(MAX) ,
            @NGUON_LOG NVARCHAR(MAX) ,
            @ThucChayHopDongChiTietID INT ,
            @SoLuongThayDoi INT ,
            @SoLuongThucTreo INT
	
        DECLARE Record_Cursor CURSOR
        FOR
            --LAY THONG TIN HOPDONGCHITIET CUA TAT CAC CAC THUC TREO DC NHAP HOAC SUA NGAYTHUCHIEN> THOIGIANBATDAU
	    SELECT DISTINCT
                A.HopDongREF ,
                A.SoHopDong ,
                A.HopDongChiTietREF ,
                A.ThucChayHopDongChiTietID
        FROM    ( SELECT    tchdctp.HopDongREF ,
                            hd.SoHopDong ,
                            tchdctp.HopDongChiTietREF ,
                            tchdctp.ThoiGianBatDau ,
                            ( CASE WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt
                                   THEN tchdctp.CreatedAt
                                   ELSE tchdctp.LastModifiedAt
                              END ) NgayThucHien ,
                            tchdctp.ThucChayHopDongChiTietID
                  FROM      (SELECT * FROM dbo.ThucChayHopDongChiTiet tchdctp 
								WHERE tchdctp.ThoiGianBatDau IS NOT NULL
								AND tchdctp.DeletedStatus = 0 --Haidh: check truong hop thucchayhopdongchitiet chua bi xoa (vi da cho truong hop check thuc treo xoa roi)
								AND ( CASE WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt
										   THEN CONVERT(DATE, tchdctp.CreatedAt)
										   ELSE CONVERT(DATE, tchdctp.LastModifiedAt)
									  END ) >= CONVERT(DATE, tchdctp.ThoiGianBatDau)--Haidh: Note cho nay dang can nhac 11-10-2013
								AND ( CASE WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt
										   THEN CONVERT(DATE, tchdctp.CreatedAt)
										   ELSE CONVERT(DATE, tchdctp.LastModifiedAt)
									  END ) = @NgayThucHien
								AND tchdctp.HopDongChiTietREF <> 0
								AND CONVERT(DATE, tchdctp.ThoiGianBatDau) >= @ThoiGianBDTinh
								AND tchdctp.HopDongREF = @HopDongID

							) tchdctp
                            INNER JOIN 
							(SELECT hdct.HopDongChiTietID, hdct.HopDongFK, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.DmLoaiREF, hdct.DmLoaiBannerREF FROM dbo.HopDongChiTiet hdct 
										WHERE 1=1 
										AND NOT ( hdct.DmLoaiREF = 13
												  OR hdct.DmLoaiBannerREF = 18
												)-- khong tinh mua ngoai
										--AND hdct.DmSanPhamREF IN (--- NHOM SP TMDT --------------
										--							242-- Luot up												
										--									--NHOM SP Chi phí--
										--							, 251--Thiết kế, quản lý		
										--							, 252--Hosting		
										--							, 253--Chi phi khac		
										--							, 535--Chi phí quản lý campaign		
										--							, 537--Chi phí viết bài		
										--							, 538--Chi phí thiết kế		
										--							, 539--Chi phí dựng clip		
										--							, 540--Chi phí sáng tạo		
										--							, 541--Chi phí giải thưởng cuộc thi/ Contest		
										--							, 542--Chi phí xây dưng microsite/ tab		
										--							, 555--Chi phí trài trợ		
										--							, 556--Hiệu đính		
										--							, 557--Chèn Clip		
										--							, 558--Chi phí viết bài		
										--							, 559--Chi phí quay clip		
										--							, 560--Chi phí sản xuất		
										--							, 561-- Chi phí khảo sát thị trường online	
										--							, 635-- Quản trị fanpage
										--							, 563-- Forum Seeding	
										--							, 586
										--							, 631-- facebook seeding
										--							, 651-- đăng tin fanpage
										--							, 726--Tư vấn viết đề án truyền thông
										--							, 731--KOL
										--							, 730--- Livestream
										--							, 629--Chi phí tổ chức
										--							, 729--Visual Content
										--							, 633 --Mở fanpage
										--							, 736
										--							, 734
										--							, 771
										--							, 772
										--							,775 --Campaign Audit
										--							,792, 805
										--							, 806,817,5012, 5075 ,5074 ,5073
										--								,5072 ,5071 ,5070, 821
										--								,5097, 5204 ,774 , 5199, 5214 ,5151 ,5057 
										--								,550, 5141, 5142, 5143, 5143
										--								,5160, 5188,5112,5151,5212 , 5223, 5217 )
										AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										)) 	
							)hdct ON hdct.HopDongChiTietID = tchdctp.HopDongChiTietREF
                            INNER JOIN (SELECT * FROM dbo.HopDong hd WHERE 1=1 AND hd.TrangThaiHopDong <> 3)hd ON hd.HopDongID = tchdctp.HopDongREF
							WHERE hd.HopDongID = @HopDongID
                        
                ) A
        ORDER BY A.HopDongREF ,
                A.HopDongChiTietREF
	
        OPEN Record_Cursor
	-- Perform the first fetch.
        FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong,
            @HopDongChiTietID, @ThucChayHopDongChiTietID
        WHILE @@FETCH_STATUS = 0
            BEGIN
                PRINT @HopDongChiTietID
                SET @GiaTien = 0
                SET @SoluongThucChay = 0
                SET @GiaTriThayDoiBF = 0
                SET @GiaTriThayDoiHT = 0
                SET @GiaTienSauCK = 0
                SET @ThanhTienDaTinh = 0
                SET @DonGiaHDCT = 0
                SET @SoLuongThayDoi = 0
	
                SELECT  @ThanhTienThucTreo = SUM((ISNULL(tchdctp.SoLuongThucTreo, 0) * ISNULL(tchdctp.DonGia, 0)) - ((ISNULL(tchdctp.SoLuongThucTreo, 0) * ISNULL(tchdctp.DonGia, 0)) * ISNULL(tchdctp.ChietKhau, 0)) / 100) ,
                        @SoLuongThucTreo = SUM(ISNULL(tchdctp.SoLuongThucTreo, 0))
                FROM    dbo.ThucChayHopDongChiTiet tchdctp
                WHERE   tchdctp.HopDongChiTietREF = @HopDongChiTietID
                        AND tchdctp.ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
                        AND tchdctp.DeletedStatus = 0
                GROUP BY tchdctp.HopDongChiTietREF
		
                SET @ThanhTienThucTreo = ISNULL(@ThanhTienThucTreo, 0)
                SET @SoLuongThucTreo = ISNULL(@SoLuongThucTreo, 0)

                SET @isKhuyenMai = ( SELECT TOP (1) hdct.IsKhuyenMai
                                     FROM   dbo.HopDongChiTiet hdct
                                     WHERE  hdct.HopDongChiTietID = @HopDongChiTietID
									 ORDER BY hdct.HopDongChiTietID
                                   )
				--CHECK NEU LA HOPDONGCHITIET KHUYEN MAI
                IF ( @isKhuyenMai = 1 )
                    BEGIN
						--1. GET THANHTIENKHUYENMAI DA TINH CUA HOPDONGCHITIET
                        SET @ThanhTienDaTinh = ( SELECT SUM(ISNULL(tcdt.ThanhTienKM,0)+ ISNULL(tcdt.GiaTriKMThayDoi,0))
                                                 FROM   dbo.ThucChayDaTinh tcdt
                                                 WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                        AND tcdt.DotChayBooking = CONVERT(NVARCHAR(1000), @ThucChayHopDongChiTietID)
                                                        AND CONVERT(DATE, tcdt.NgayThucHien) <= @NgayThucHien
                                               )
                        SET @ThanhTienDaTinh = ISNULL(@ThanhTienDaTinh, 0)
                        SET @GiaTienSauCK = @DonGiaHDCT
						--HAIDH COMMENT
                        SET @SoluongThucChay = ( SELECT SUM(ISNULL(tcdt.SoLuongThucChayKM,0) + ISNULL(tcdt.SoLuongKMThayDoi,0))
                                                 FROM   dbo.ThucChayDaTinh tcdt
                                                 WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                        AND tcdt.DotChayBooking = CONVERT(NVARCHAR(1000), @ThucChayHopDongChiTietID)
                                                        AND CONVERT(DATE, tcdt.NgayThucHien) <= @NgayThucHien
                                               )
                        SET @SoluongThucChay = ISNULL(@SoluongThucChay, 0)
                    END
	    
				--CHECK NEU LA HOPDONGCHITIET KHONG KHUYEN MAI
                IF ( @isKhuyenMai = 0 )
                    BEGIN
						--1. GET THANHTIENSAUTRIETKHAU DA TINH CUA HOPDONGCHITIET					
                        SET @ThanhTienDaTinh = ( SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
                                                 FROM   dbo.ThucChayDaTinh tcdt
                                                 WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                        AND tcdt.DotChayBooking = CONVERT(NVARCHAR(1000), @ThucChayHopDongChiTietID)
                                                        AND CONVERT(DATE, tcdt.NgayThucHien) <= @NgayThucHien
                                               )

                        SET @SoluongThucChay = ( SELECT SUM(ISNULL(tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0))
                                                 FROM   dbo.ThucChayDaTinh tcdt
                                                 WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                        AND tcdt.DotChayBooking = CONVERT(NVARCHAR(1000), @ThucChayHopDongChiTietID)
                                                        AND CONVERT(DATE, tcdt.NgayThucHien) <= @NgayThucHien
                                               )
                       
						--2. GET CHIET KHAU CUA HOP DONG
                        SET @ChietKhau = ( SELECT TOP (1)  hdct.ChietKhau
                                           FROM     dbo.HopDongChiTiet hdct
                                           WHERE    hdct.HopDongChiTietID = @HopDongChiTietID
										   ORDER BY hdct.HopDongChiTietID
                                         )
                        SET @ChietKhau = ISNULL(@ChietKhau, 0)
                        SET @ThanhTienThucTreo = ISNULL(@ThanhTienThucTreo,0)
						SET @SoluongThucChay = ISNULL(@SoluongThucChay, 0)
						SET @ThanhTienDaTinh = ISNULL(@ThanhTienDaTinh,0)
                    END

                IF (( @ThanhTienDaTinh IS NOT NULL ) AND ( @ThanhTienDaTinh <> @ThanhTienThucTreo ))
                    BEGIN
	    				--PRINT convert(nvarchar(50),@GiaTriThayDoiHT) + ': @GiaTriThayDoiHT'
                        SET @DmSanPhamREF = 0
                        SET @DmWebsiteREF = 0
                        SELECT  @DmSanPhamREF = hdct.DmSanPhamREF ,
                                @DmWebsiteREF = hdct.DmWebsiteREF
                        FROM    dbo.HopDongChiTiet hdct
                        WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
                        SET @DmSanPhamREF = ISNULL(@DmSanPhamREF, 0)
                        SET @DmWebsiteREF = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF)
	
                        SET @GiaTriThayDoi = -1 * @ThanhTienDaTinh
                        SET @SoLuongThayDoi = -1 * @SoluongThucChay
   	    	
					IF ISNULL(@GiaTriThayDoi, 0) <> 0 AND ISNULL(@SoLuongThayDoi, 0) <> 0
						BEGIN
							--1.2 NEU CHUA TON TAI THI TAO BAN GHI MOI CHO HOPDONGCHITIET TAI NGAY HIEN TAI VOI SO TIEN KHUYEN MAI	
							--THUC HIEN DOI TRU GIA TRI
							EXEC sp_TC_InsertThucTreoThayDoi_ChiPhiKhac @HopDongChiTietID,
								@NgayThucHien, @GiaTriThayDoi,
								@ThucChayHopDongChiTietID, @SoLuongThayDoi, N'Thay đổi giá trị thực treo'
							
							DECLARE @KQ INT = 0
							--- TINH LAI GIA TRI
							EXEC [dbo].[sp_TC_Insert_GTTD_ThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi] @ThucChayHopDongChiTietID, @HopDongChiTietID, @NgayThucHien,  @KQ OUTPUT

							IF @KQ = 0
							BEGIN
								UPDATE dbo.ThucChayHopDongChiTiet SET RecordStatus = 0
								WHERE ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
									AND HopDongChiTietREF = @HopDongChiTietID
							END
							--1.3 GHI LOG
							SET @CONTENT_LOG = N'(Có thay đổi thực treo, Giá trị:'
								+ CONVERT(NVARCHAR(20), CONVERT(BIGINT, @ThanhTienDaTinh))
								+ '->'
								+ CONVERT(NVARCHAR(20), CONVERT(BIGINT, @GiaTienSauCK)) 
							SET @NGUON_LOG = 'Table:ThucChayHopDongChiTiet CPK, NgayThucHien:'
								+ CONVERT(NVARCHAR(20), @NgayThucHien) + ', HDCT:'
								+ CONVERT(NVARCHAR(20), @HopDongChiTietID)
							--GHI LOG VIEC THAY DOI
							INSERT  INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
									( [ThuChay_LogNNTinhGiaTriThayDoiID] ,
									  [HopDongREF] ,
									  [SoHopDong] ,
									  [HopDongChiTietREF] ,
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
									  @HopDongChiTietID ,
									  @NgayThucHien ,
									  @GiaTriThayDoiHT ,
									  0 ,
									  0 ,
									  0 ,
									  0 ,
									  @CONTENT_LOG ,
									  @NGUON_LOG ,
									  'CPK' ,
									  'ThucChay' ,
									  GETDATE() ,
									  'ThucChay' ,
									  GETDATE() ,
									  0 ,
									  0 ,
									  0
									)		
						END

                    END
				-------------------THAY DOI THONG TIN NHAN HANG-------------------
                DECLARE @NhanHangTreo NVARCHAR(255)
                DECLARE @NhanHangTinh NVARCHAR(255)

                SELECT  @NhanHangTreo = tchdctp.DmNhanHangREF
                FROM    dbo.ThucChayHopDongChiTiet tchdctp
                WHERE   tchdctp.HopDongChiTietREF = @HopDongChiTietID
                        AND tchdctp.ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID

                SELECT  @NhanHangTinh = tcdt.NhanHang
                FROM    dbo.ThucChayDaTinh tcdt
                WHERE   tcdt.HopDongID = @HopDongREF
                        AND tcdt.DotChayBooking = CONVERT(NVARCHAR(1000), @ThucChayHopDongChiTietID) 
				--CHECK THONG TIN THAY DOI NHAN HANG
				/* --TAM THOI BO RA DO DUOC TINH TREN JOB TINH GIA TRI THAY DOI CHUNG
                IF @NhanHangTreo <> @NhanHangTinh
                    BEGIN
	
                        SET @GiaTriThayDoi = -1 * @ThanhTienDaTinh
                        SET @SoLuongThayDoi = -1 * @SoluongThucChay

                        EXEC sp_TC_InsertThucTreoThayDoi_ChiPhiKhac @HopDongChiTietID,
                            @NgayThucHien, @GiaTriThayDoi,
                            @ThucChayHopDongChiTietID, @SoLuongThayDoi, N'Thay đổi nhãn hàng thực treo'

						DECLARE @KQ2 INT = 0
						--- Tinh lai
						EXEC sp_TC_InsertThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi @ThucChayHopDongChiTietID, @HopDongChiTietID, @NgayThucHien,  @KQ2 OUTPUT

						IF @KQ2 = 0
							BEGIN
								UPDATE dbo.ThucChayHopDongChiTiet SET RecordStatus = 0
								WHERE ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
									AND HopDongChiTietREF = @HopDongChiTietID
							END
                    END
				*/
                FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong,
                    @HopDongChiTietID, @ThucChayHopDongChiTietID
            END
        CLOSE Record_Cursor
        DEALLOCATE Record_Cursor
    END

	--EXEC [ThucChay_CheckThucTreoThayDoi_ChiPhiKhac] '2013-09-29', '2013-01-29'

```
