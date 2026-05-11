# Stored Procedure: `ThucChay_CheckThucTreoThayDoi_PR_GoiHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-01-19 09:50:36.227000
- **Ngày sửa cuối**: 2017-05-15 10:41:17.650000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThoiGianBDTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--[ThucChay_CheckThucTreoThayDoi_PR_GoiHD]  '2017-05-12','2016-01-01'
CREATE PROCEDURE [dbo].[ThucChay_CheckThucTreoThayDoi_PR_GoiHD] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@ThoiGianBDTinh DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @HopDongREF INT ,@HopDongChiTietREF INT
	    , @ThucChayHopDongChiTietPRID INT, @DmHinhThucQuangCaoREF INT
	    , @DmSanPhamREF INT, @DmNhanHangREF INT, @DmViTriREF INT, @SoLuong INT
	    , @ChietKhau INT, @KhuyenMai INT, @DmWebsiteREF INT
	    , @GiaTien FLOAT, @ThoiGianBatDau DATETIME, @DeletedStatus INT
	DECLARE @LoaiThayDoi INT, @GiaTriThayDoiHT FLOAT, @ThanhTienThucChayDaTinh FLOAT, @ThoiGianBatDauCheck DATETIME
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(MAX), @SoHopDong NVARCHAR(100)
	DECLARE @SoLuongThayDoi INT, @SoLuongThucChay INT
	
	SET @LoaiThayDoi = 0 --LOAI THAY DOI : 1 CHI THAY DOI GIA TRI, 2 THAY DOI THONG TIN, 3 THUC TREO BI HUY, 0 KHONG THAY DOI GIA TRI HOAC THONG TIN     
	SET @GiaTriThayDoiHT = 0
	SET @ThanhTienThucChayDaTinh = 0
	SET @ThoiGianBatDauCheck = '2016-01-01'
	SET @SoLuongThayDoi = 0
	
	DECLARE Record_Cursor CURSOR  
	FOR
	    --LAY THONG TIN HOPDONGCHITIET CUA TAT CAC CAC THUC TREO DC NHAP HOAC SUA NGAYTHUCHIEN> THOIGIANBATDAU
	    SELECT DISTINCT A.HopDongREF,A.HopDongChiTietREF
	    , A.ThucChayHopDongChiTietPRID, A.DmHinhThucQuangCaoREF
	    , A.DmSanPhamREF , A.DmNhanHangREF, A.DmViTriREF, A.SoLuong
	    , A.ChietKhau, A.KhuyenMai, A.DmWebsiteREF
	    , A.GiaTien, A.ThoiGianBatDau, A.DeletedStatus
	    FROM(
               SELECT tchdctp.HopDongREF,
                      tchdctp.HopDongChiTietREF, 
                      tchdctp.ThucChayHopDongChiTietPRID, 
                      tchdctp.DmHinhThucQuangCaoREF, 
                      tchdctp.DmSanPhamREF,
                      tchdctp.DmNhanHangREF,
                      tchdctp.DmViTriREF, 
                      tchdctp.SoLuong, 
                      tchdctp.ChietKhau, 
                      tchdctp.KhuyenMai, 
                      dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(tchdctp.DmWebsiteREF) DmWebsiteREF,
                      tchdctp.GiaTien,
                      tchdctp.ThoiGianBatDau, 
                      tchdctp.DeletedStatus
               FROM   ThucChayHopDongChiTietPR tchdctp
               WHERE  tchdctp.ThoiGianBatDau IS NOT NULL --AND tchdctp.HopDongREF = 500395
                      AND (   CASE 
                                   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
                                   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
                              END
                          ) >= CONVERT(DATE,tchdctp.ThoiGianBatDau)--Haidh: Note cho nay dang can nhac 11-10-2013
                      AND (   CASE 
                                   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
                                   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
                              END
                          ) = @NgayThucHien
                      AND Convert(date,tchdctp.CreatedAt) < Convert(date,tchdctp.LastModifiedAt)
                      AND convert(date,tchdctp.ThoiGianBatDau) >= @ThoiGianBDTinh
                      AND tchdctp.RecordStatus = 1
	        )A
			--WHERE A.HopDongREF = 500663
			--AND a.ThucChayHopDongChiTietPRID =77932
	    ORDER BY
	           A.HopDongREF, A.HopDongChiTietREF
	
	OPEN Record_Cursor
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @HopDongREF ,@HopDongChiTietREF 
	    , @ThucChayHopDongChiTietPRID , @DmHinhThucQuangCaoREF 
	    , @DmSanPhamREF , @DmNhanHangREF ,@DmViTriREF, @SoLuong
	    , @ChietKhau , @KhuyenMai , @DmWebsiteREF 
	    , @GiaTien , @ThoiGianBatDau , @DeletedStatus 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @SoHopDong = 
		(
			SELECT hd.SoHopDong FROM HopDong hd
		    WHERE hd.HopDongID = @HopDongREF
		)
		--*********CHECK THONG TIN THAY DOI CUA THUC TREO PR
		--DmHinhThucQuangCaoREF
		--DmSanPhamREF
		--DmNhanHangREF
		--DmWebsiteREF
		--DmViTriREF
		--GiaTien
		--ChietKhau
		--DeletedStatus
		IF(@DeletedStatus = 1)
		BEGIN
			SET @LoaiThayDoi = 3 --HUY THUC TREO
			SET @GiaTriThayDoiHT = 0
			SET @SoLuongThayDoi = 0
			--INSERT GIA TRI THAY DOI 
			SET @CONTENT_LOG = N'(Thực treo hủy:' + CONVERT(NVARCHAR(20),convert(bigint,@ThanhTienThucChayDaTinh)) + '->' + CONVERT(NVARCHAR(20),convert(bigint,@GiaTien*(100-@ChietKhau)/100))
			EXEC [dbo].[ThucChay_InsertThucTreoThongTinThayDoi_PR_GoiHD] 
					@ThucChayHopDongChiTietPRID, @HopDongREF, @NgaythucHien, @GiaTriThayDoiHT, @SoLuongThayDoi			
		END
		ELSE
			BEGIN
				SET @LoaiThayDoi = [dbo].[fn_Check_Loaithaydoi_ThucChayHopDongChiTietPR]
									(
										@ThucChayHopDongChiTietPRID ,
										@HopDongREF ,
										@DmHinhThucQuangCaoREF,
										@DmSanPhamREF,
										@DmNhanHangREF,
										@DmWebsiteREF,
										@DmViTriREF,
										@SoLuong,
										@GiaTien,
										@ChietKhau,
										@NgayThucHien
									)
									
				--PRINT @LoaiThayDoi

				IF(@LoaiThayDoi = 1)
				BEGIN
					--PRINT 'Vao loai thay doi la 1'
					SELECT @ThanhTienThucChayDaTinh = SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
					,@SoLuongThucChay = SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)
					FROM ThucChayDaTinh tcdt
					WHERE 1=1
					AND tcdt.HopDongID = @HopDongREF
					AND tcdt.TrangThaiHopDong <> 3
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCaoREF
					AND tcdt.NgayThucHien <= @NgayThucHien
					AND tcdt.NgayThucHien >= @ThoiGianBatDauCheck
					AND tcdt.DotChayBooking = CONVERT(NVARCHAR(50),@ThucChayHopDongChiTietPRID)
					
					SET @GiaTriThayDoiHT =  (((@GiaTien *@SoLuong)*(100  - @ChietKhau))/100) - @ThanhTienThucChayDaTinh
					SET @SoLuongThayDoi = @SoLuong - @SoLuongThucChay 
					--PRINT @GiaTriThayDoiHT
					--PRINT @SoLuongThayDoi
					--INSERT THONG TIN THAY DOI GIA TRI
					SET @CONTENT_LOG = N'(Có thay đổi thực treo, Giá trị:' + CONVERT(NVARCHAR(20),convert(bigint,@ThanhTienThucChayDaTinh)) + '->' + CONVERT(NVARCHAR(20),convert(bigint,@GiaTien*(100-@ChietKhau)/100))
					
					EXEC  [dbo].[ThucChay_InsertThucTreoThayDoi_PR_GoiHD] @ThucChayHopDongChiTietPRID, @NgaythucHien ,@GiaTriThayDoiHT,@SoLuongThayDoi
						
				END	
				ELSE IF(@LoaiThayDoi = 2)
				BEGIN
					SET @GiaTriThayDoiHT = (((@GiaTien *@SoLuong)*(100  - @ChietKhau))/100)
					SET @SoLuongThayDoi = @SoLuong
					--INSERT THONG TIN THAY DOI
					SET @CONTENT_LOG = N'(Có thay đổi thực treo, Thông tin thay đổi:' + CONVERT(NVARCHAR(20),convert(bigint,@ThanhTienThucChayDaTinh)) + '->' + CONVERT(NVARCHAR(20),convert(bigint,@GiaTien*(100-@ChietKhau)/100))
					--PRINT 'Vao loai thay doi la 2'
					EXEC [dbo].[ThucChay_InsertThucTreoThongTinThayDoi_PR_GoiHD] 
					@ThucChayHopDongChiTietPRID, @HopDongREF, @NgaythucHien, @GiaTriThayDoiHT, @SoLuongThayDoi	
				END					
			END
	  
			--1.3 GHI LOG
			SET @NGUON_LOG = 'Table:ThucChayHopDongChiTietPR, NgayThucHien:' + CONVERT(NVARCHAR(20),@NgayThucHien) + ', TCHDCTPR:' + CONVERT(NVARCHAR(20),@ThucChayHopDongChiTietPRID)
			--GHI LOG VIEC THAY DOI
			
			INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
			  ([ThuChay_LogNNTinhGiaTriThayDoiID],
				[HopDongREF],[SoHopDong],[HopDongChiTietREF],[DmSanPhamREF],[DmWebsiteREF],
				[NgayThucHien],
				[GiaTriThayDoi],[GiaSauCK1],[Soluong1],[GiaSauCK2],[Soluong2],
				[NoiDungLog],[NguonLog],[GhiChu],[CreatedBy],[CreatedAt],
				[LastModifiedBy],[LastModifiedAt],[DeletedStatus],
				[PrintStatus],[RecordStatus]
			  )
			VALUES
			  (NEWID(),
				@HopDongREF,@SoHopDong,0,@DmSanPhamREF,@DmWebsiteREF, @NgayThucHien,
				@GiaTriThayDoiHT,0,0,0,0,@CONTENT_LOG
				,@NGUON_LOG,'PR',	'ThucChay',	GETDATE(),
				'ThucChay',GETDATE(),0,
				0,0
			  )			
	   FETCH NEXT FROM Record_Cursor INTO @HopDongREF ,@HopDongChiTietREF 
	    , @ThucChayHopDongChiTietPRID , @DmHinhThucQuangCaoREF 
	    , @DmSanPhamREF , @DmNhanHangREF , @DmViTriREF, @SoLuong
	    , @ChietKhau , @KhuyenMai , @DmWebsiteREF 
	    , @GiaTien , @ThoiGianBatDau , @DeletedStatus 
	END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
END



```
