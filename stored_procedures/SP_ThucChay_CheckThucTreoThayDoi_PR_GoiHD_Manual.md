# Stored Procedure: `ThucChay_CheckThucTreoThayDoi_PR_GoiHD_Manual`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-07 10:54:35.137000
- **Ngày sửa cuối**: 2017-01-07 14:21:28.973000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThoiGianBDTinh` | `datetime(8)` | No |
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[ThucChay_CheckThucTreoThayDoi_PR_GoiHD_Manual] 
	'2016-12-31', --@NgayThucHien DATETIME,
	'2015-01-01', --@ThoiGianBDTinh DATETIME,
	124556 --@ThucChayHopDongChiTietPRID INT
*/

CREATE PROCEDURE [dbo].[ThucChay_CheckThucTreoThayDoi_PR_GoiHD_Manual] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@ThoiGianBDTinh DATETIME,
	@ThucChayHopDongChiTietPRID INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @HopDongREF INT ,@HopDongChiTietREF INT
	    , @DmHinhThucQuangCaoREF INT
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
               WHERE  1=1
			   AND tchdctp.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
			   
	)A

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
		
			SET @GiaTriThayDoiHT = (((@GiaTien *@SoLuong)*(100  - @ChietKhau))/100)
			SET @SoLuongThayDoi = @SoLuong
			--PRINT @GiaTriThayDoiHT
			--INSERT THONG TIN THAY DOI
			SET @CONTENT_LOG = N'(Có thay đổi thực treo, Thông tin thay đổi:' + CONVERT(NVARCHAR(20),convert(bigint,@ThanhTienThucChayDaTinh)) + '->' + CONVERT(NVARCHAR(20),convert(bigint,@GiaTien*(100-@ChietKhau)/100))
					
			EXEC [dbo].[ThucChay_InsertThucTreoThongTinThayDoi_PR_GoiHD_Manual]  
			@ThucChayHopDongChiTietPRID, @HopDongREF, @NgaythucHien, @GiaTriThayDoiHT, @SoLuongThayDoi	
	  
			----1.3 GHI LOG
			--SET @NGUON_LOG = 'Table:ThucChayHopDongChiTietPR, NgayThucHien:' + CONVERT(NVARCHAR(20),@NgayThucHien) + ', TCHDCTPR:' + CONVERT(NVARCHAR(20),@ThucChayHopDongChiTietPRID)
			----GHI LOG VIEC THAY DOI
			
			--INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
			--	([ThuChay_LogNNTinhGiaTriThayDoiID],
			--	[HopDongREF],[SoHopDong],[HopDongChiTietREF],[DmSanPhamREF],[DmWebsiteREF],
			--	[NgayThucHien],
			--	[GiaTriThayDoi],[GiaSauCK1],[Soluong1],[GiaSauCK2],[Soluong2],
			--	[NoiDungLog],[NguonLog],[GhiChu],[CreatedBy],[CreatedAt],
			--	[LastModifiedBy],[LastModifiedAt],[DeletedStatus],
			--	[PrintStatus],[RecordStatus]
			--	)
			--VALUES
			--	(NEWID(),
			--	@HopDongREF,@SoHopDong,0,@DmSanPhamREF,@DmWebsiteREF, @NgayThucHien,
			--	@GiaTriThayDoiHT,0,0,0,0,@CONTENT_LOG
			--	,@NGUON_LOG,'PR',	'ThucChay',	GETDATE(),
			--	'ThucChay',GETDATE(),0,
			--	0,0
			--	)			
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
