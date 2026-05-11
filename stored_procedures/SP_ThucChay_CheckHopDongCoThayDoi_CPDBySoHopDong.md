# Stored Procedure: `ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:30:18.507000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.677000

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
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDong] 
	-- Add the parameters for the stored procedure here
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
	DECLARE @CountHDTD INT, @GiaTriThayDoi FLOAT, @DonGiaHT FLOAT, @HopDongChiTietThayDoiGia INT
	DECLARE @DonGiaLienKeTruoc FLOAT, @SoLuongThucChay FLOAT, @DmSanPhamREF INT, @DmWebsiteREF INT
	DECLARE @SoNgayLienKeTruoc FLOAT, @ChietKhauHT INT, @TongGTThanhtienThucChayDatinh FLOAT, @TongGTThanhTienHienTai FLOAT
	DECLARE @DonGia INT, @HopDongChiTiet INT, @HopDongChiTietThayDoiCK INT, @ChietKhau INT 

	SET @SoNgayDotChayThayDoi = 0
	SET @DonGiaLienKeTruoc = 0
	SET @CountHDTD = 0
	SET @CONTENT_LOG = ''
	SET @NGUON_LOG = ''
	SET @SoLuongThucChayHTBooking = 0
	set @DonGiaTheoDVTinhHT = 0
	SET @ChietKhauHT = 0
	SET @TongGTThanhtienThucChayDatinh = 0
	--CHECK HOPDONGCHITIET CO SU THAY DOI VE GIA
	SELECT @HopDongChiTietThayDoiGia = A.HopDongChiTietThayDoiID
		,@DonGia = A.DonGia, @HopDongChiTiet = A.HopDongChiTietREF 
	  FROM
	(
		SELECT TOP 1 hdcttd.HopDongChiTietThayDoiID, HDCTTD.DonGia , hdcttd.HopDongChiTietREF
		FROM HopDongThayDoi hdtd
		INNER JOIN HopDongChiTietThayDoi hdcttd 
		ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
			WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
			AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
		ORDER BY hdcttd.HopDongChiTietThayDoiID 	
	)A
	INNER JOIN HopDongChiTiet hdct ON HDCT.HopDongChiTietID = A.HopDongChiTietREF
	WHERE (A.DonGia != HDCT.DonGia)

	--CHECK HOPDONGCHITIET CO SU THAY DOI VE CHIET KHAU	
	SELECT @HopDongChiTietThayDoiCK = A.HopDongChiTietThayDoiID,
	@ChietKhau = A.ChietKhau, @HopDongChiTiet = A.HopDongChiTietREF 
	FROM 
	(
		SELECT TOP 1 hdcttd.HopDongChiTietThayDoiID, HDCTTD.HopDongChiTietREF ,HDTD.NgayThayDoi
		, HDCTTD.ChietKhau, HDCTTD.DonGia 
		FROM HopDongThayDoi hdtd
		INNER JOIN HopDongChiTietThayDoi hdcttd 
		ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
			WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
			AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
			ORDER BY HDCTTD.HopDongChiTietThayDoiID 
	)A
	INNER JOIN HopDongChiTiet hdct ON HDCT.HopDongChiTietID = A.HopDongChiTietREF
	WHERE (A.ChietKhau != HDCT.ChietKhau)
	
	--NEU CO THAY DOI VE GIA
	
	
	SET @CountHDTD = ISNULL(@CountHDTD,0)
	--1. GET SO LUONG DOT CHAY CUA LAN THAY DOI TAI NGAY THUC HIEN
	SELECT @SoLuong = hdct.SoLuong, @DonViTinh = hdct.DonViTinh
			,@ChietKhauHT = hdct.ChietKhau, @DmSanPhamREF = hdct.DmSanPhamREF
			, @DmWebsiteREF = hdct.DmWebsiteREF
	FROM HopDongChiTiet hdct
	WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	
	SET @DonGiaTheoDVTinhHT = ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(@SoLuong,@DonViTinh,@DonGiaHT,@NgayThucHien, @NgayThucHien, @HopDongChiTietID),0)
	--TINH SO LUONG THUC CHAY DU TREN BOOKING HIEN TAI
	set @SoLuongThucChayHTBooking = dbo.[ThucChay_GetSoLuongThucChayBooking_CPD](@SoLuongHT ,@DonViTinh ,@HopDongChiTietID ,@NgayThucHien )	
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
	SET @TongGTThanhtienThucChayDatinh = round(ISNULL(@TongGTThanhtienThucChayDatinh,0),0)
	
	SELECT TOP 1 @DonGiaLienKeTruoc = tcdt.DonGiaTheoDonVi 
	  FROM ThucChayDaTinh tcdt
	WHERE CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	ORDER by tcdt.NgayThucHien DESC
	
	--TONG GIA TRI THUC HIEN DEN NGAY HIEN TAI
	IF(@HopDongChiTietThayDoiGia <> 0)
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi giá: ' + CONVERT(NVARCHAR(30),convert(bigint,@DonGiaLienKeTruoc)) + '->' + CONVERT(NVARCHAR(30),convert(bigint,@DonGiaTheoDVTinhHT)) + ');'
		SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTiet: ' + CONVERT(NVARCHAR(30),@HopDongChiTietID)		
	END
	--NEU CO THAY DOI VE CHIET KHAU
	IF(@HopDongChiTietThayDoiCK <>0)
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi chiết khấu: ' + CONVERT(NVARCHAR(30),@ChietKhau) + '->' + CONVERT(NVARCHAR(30),@ChietKhauHT) + ');'
		SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTiet'+ CONVERT(NVARCHAR(30),@HopDongChiTietID)
	END
	IF((@TongGTThanhtienThucChayDatinh <>0) AND (@TongGTThanhTienHienTai <> @TongGTThanhtienThucChayDatinh))
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
		SET @GiaTriThayDoi = round(@TongGTThanhTienHienTai - @TongGTThanhtienThucChayDatinh,0)
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
