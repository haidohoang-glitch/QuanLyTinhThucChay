# Stored Procedure: `ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDongDotChay_bk20170919`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-19 10:10:48.873000
- **Ngày sửa cuối**: 2017-09-19 10:10:48.873000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoLuongHT` | `int(4)` | No |
| `@ThanhTienHDCT` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDongDotChay 38462,'QC3531015',85478,'2015-12-07',2,110400000
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDongDotChay_bk20170919] 
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@SoLuongHT INT,
	@ThanhTienHDCT FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoNgayDotChayThayDoi INT, @SoLuong INT, @DonViTinh NVARCHAR(20), @DonGiaTheoDVTinhHT FLOAT
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500), @SoLuongThucChayHTBooking INT
	DECLARE @CountHDTD INT, @GiaTriThayDoi FLOAT, @DonGiaHT FLOAT
	DECLARE @DonGiaLienKeTruoc FLOAT, @DmSanPhamREF INT, @DmWebsiteREF INT
	DECLARE @ChietKhauHT INT, @TongGTThanhtienThucChayDatinh FLOAT, @TongGTThanhTienHienTai FLOAT

	SET @SoNgayDotChayThayDoi = 0
	SET @DonGiaLienKeTruoc = 0
	SET @CountHDTD = 0
	SET @CONTENT_LOG = ''
	SET @NGUON_LOG = ''
	SET @SoLuongThucChayHTBooking = 0
	set @DonGiaTheoDVTinhHT = 0
	SET @ChietKhauHT = 0
	SET @TongGTThanhtienThucChayDatinh = 0
	
	SET @CountHDTD = ISNULL(@CountHDTD,0)
	--1. GET SO LUONG DOT CHAY CUA LAN THAY DOI TAI NGAY THUC HIEN
	SELECT @SoLuong = hdct.SoLuong, @DonViTinh = hdct.DonViTinh, @DonGiaHT = hdct.DonGia
			,@ChietKhauHT = hdct.ChietKhau, @DmSanPhamREF = hdct.DmSanPhamREF
			, @DmWebsiteREF = hdct.DmWebsiteREF
	FROM HopDongChiTiet hdct
	WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	
	SET @DonGiaTheoDVTinhHT = ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(@SoLuong,@DonViTinh,@DonGiaHT,@NgayThucHien, @NgayThucHien, @HopDongChiTietID),0)
	--TINH SO LUONG THUC CHAY DU TREN BOOKING HIEN TAI
	set @SoLuongThucChayHTBooking = dbo.[ThucChay_GetSoLuongThucChayBooking_CPDDotChay](@SoLuongHT ,@DonViTinh ,@HopDongChiTietID ,@NgayThucHien )	
	--TONG GIA TRI THUC CHAY HIEN TAI
	SET @TongGTThanhTienHienTai = round(@SoLuongThucChayHTBooking*(@DonGiaTheoDVTinhHT*(100-@ChietKhauHT)/100),0)
	SET @DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
	SET @DmWebsiteREF = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF)
	--TONG GIA TRI THUC CHAY DEN NGAY THUC HIEN
	SET @TongGTThanhtienThucChayDatinh = 	(	
			SELECT sum(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(TCDT.GiaTriThayDoi,0)) 
			FROM ThucChayDaTinh tcdt
			WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien 
			AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
		)
	SET @TongGTThanhtienThucChayDatinh = ISNULL(@TongGTThanhtienThucChayDatinh,0)
	
	SELECT TOP 1 @DonGiaLienKeTruoc = tcdt.DonGiaTheoDonVi 
	  FROM ThucChayDaTinh tcdt
	WHERE CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	ORDER by tcdt.NgayThucHien DESC
	
		
	IF((@TongGTThanhTienHienTai <> @TongGTThanhtienThucChayDatinh) AND (ABS(@ThanhTienHDCT - @TongGTThanhtienThucChayDatinh)>1))
	--IF((@TongGTThanhTienHienTai <> @TongGTThanhtienThucChayDatinh))
	
	BEGIN
		SET @CountHDTD = 
		(
			SELECT COUNT(tcdt.NgayThucHien) FROM ThucChayDaTinh tcdt
			WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
		)
		SET @CONTENT_LOG = @CONTENT_LOG + N'HĐ có sự thay đổi về giá trị thực chạy, Giá trị thực chạy trước:' + convert(nvarchar(50),CONVERT(bigint,@TongGTThanhtienThucChayDatinh))
		 + N' Gia trị thực chạy hiện tại:' + CONVERT(NVARCHAR(50),CONVERT(bigint,@TongGTThanhTienHienTai))
		SET @NGUON_LOG = @NGUON_LOG + 'HopDongSo:' + CONVERT(NVARCHAR(50),@HopDongChiTietID) + ' Ngaythuchien:' + CONVERT(NVARCHAR(50),@NgayThucHien)	
		SET @GiaTriThayDoi = @TongGTThanhTienHienTai - @TongGTThanhtienThucChayDatinh
	
		
		IF(@CountHDTD >0)
		BEGIN
			--GHI LOG VIEC THAY DOI
			INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
			  ([ThuChay_LogNNTinhGiaTriThayDoiID],
				[HopDongREF],[SoHopDong],[HopDongChiTietREF],
				[DmSanPhamREF], [DmWebsiteREF],[NgayThucHien],
				[GiaTriThayDoi],[GiaSauCK1],[Soluong1],[GiaSauCK2],[Soluong2],
				[NoiDungLog],[NguonLog],[GhiChu],[CreatedBy],[CreatedAt],
				[LastModifiedBy],[LastModifiedAt],[DeletedStatus],
				[PrintStatus],[RecordStatus]
			  )
			VALUES
			  (NEWID(),
				@HopDongREF,@SoHopDong,@HopDongChiTietID, @DmSanPhamREF, @DmWebsiteREF,@NgayThucHien,
				@GiaTriThayDoi,0,@SoLuongHT,0,0,@CONTENT_LOG
				,@NGUON_LOG,'CPD',	'ThucChay',	GETDATE(),
				'ThucChay',GETDATE(),0,
				0,0
			  )
			--UPDATE GIA TRI THAY DOI
			UPDATE ThucChayDaTinh
			SET	GiaTriThayDoi = GiaTriThayDoi + @GiaTriThayDoi
			, LastModifiedAt = GETDATE()
			WHERE HopDongID = @HopDongREF
			AND HopDongChiTietREF = @HopDongChiTietID
			AND NgayThucHien = @NgayThucHien 
		END
		ELSE
			BEGIN
				--GHI LOG VIEC THAY DOI
				INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
				  ([ThuChay_LogNNTinhGiaTriThayDoiID],
					[HopDongREF],[SoHopDong],[HopDongChiTietREF],
					[DmSanPhamREF], [DmWebsiteREF],[NgayThucHien],
					[GiaTriThayDoi],[GiaSauCK1],[Soluong1],[GiaSauCK2],[Soluong2],
					[NoiDungLog],[NguonLog],[GhiChu],[CreatedBy],[CreatedAt],
					[LastModifiedBy],[LastModifiedAt],[DeletedStatus],
					[PrintStatus],[RecordStatus]
				  )
				VALUES
				  (NEWID(),
					@HopDongREF,@SoHopDong,@HopDongChiTietID, @DmSanPhamREF, @DmWebsiteREF,@NgayThucHien,
					@GiaTriThayDoi,0,0,0,0,@CONTENT_LOG
					,@NGUON_LOG,'CPD',	'ThucChay',	GETDATE(),
					'ThucChay',GETDATE(),0,
					0,0
				  )
				EXEC [dbo].[ThucChay_InsertThucTreoThayDoi_CPD] @HopDongChiTietID ,@NgaythucHien,@GiaTriThayDoi
			END	
	END
END

```
