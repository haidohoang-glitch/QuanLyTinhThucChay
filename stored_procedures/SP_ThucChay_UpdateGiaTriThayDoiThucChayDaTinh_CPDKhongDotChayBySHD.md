# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChayBySHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-01 15:02:15.913000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.450000

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
--exec [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChayBySHD] 25282,'QC1560414',56778,'2014-06-06'

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChayBySHD] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ChietKhau FLOAT, @DonGia FLOAT, @DonGiaHT FLOAT, @HopDongChiTietThayDoiGia INT, @HopDongChiTietThayDoiCK INT, @HopDongChiTietThayDoiSL INT
	DECLARE @DotChayHopDongChiTietThayDoi INT, @HopDongChiTiet INT, @ChietKhauSauTD INT, @SoLuongHT INT
	DECLARE @SoNgayDotChayThayDoi INT, @SoLuong INT, @DonViTinh NVARCHAR(20), @DonGiaTheoDVTinhHT FLOAT
	DECLARE @soluongpbBF INT, @soluongpbHT INT, @SoLuongThucChayHT INT, @SoLuongThucChayBF INT
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500)
	DECLARE @CountHDTD INT, @GiaTriThayDoi FLOAT, @TongGiaTriThucChayDaTinh FLOAT, @TongGiaTriThucChayDaTinhHT FLOAT
	DECLARE @DonGiaLienKeTruoc FLOAT, @SoLuongThucChay FLOAT, @SoLuongThucChayBfHT INT
	DECLARE @SoNgayLienKeTruoc FLOAT, @ChietKhauHT INT,@DmSanPhamREF INT, @DmWebsiteREF_log INT, @DmWebsiteREF INT, @TenWebsite NVARCHAR(100)

	SET @SoNgayDotChayThayDoi = 0
	SET @DmWebsiteREF_log = 0
	SET @DonGiaLienKeTruoc = 0
	SET @CountHDTD = 0
	SET @CONTENT_LOG = ''
	SET @NGUON_LOG = ''
	SET @DotChayHopDongChiTietThayDoi = 0
	SET @HopDongChiTietThayDoiSL = 0
	SET @HopDongChiTietThayDoiGia = 0
	SET @HopDongChiTietThayDoiCK = 0
	SET @SoLuongThucChayHT = 0
	SET @SoLuongThucChayBF = 0
	set @DonGiaTheoDVTinhHT = 0
	SET @ChietKhauHT = 0
	SET @SoLuongThucChayBfHT = 0
	SET @TongGiaTriThucChayDaTinh = 0
	set @TongGiaTriThucChayDaTinhHT = 0
	SET @CountHDTD = ISNULL(@CountHDTD,0)
	SET @soluongpbHT = 0
	SET @soluongpbBF = 0
	
	--CHECK HOPDONGCHITIET CO SU THAY DOI VE DONGIA
	SELECT @HopDongChiTietThayDoiGia = A.HopDongChiTietThayDoiID
		,@DonGia = A.DonGia, @HopDongChiTiet = A.HopDongChiTietREF 
	  FROM
	(
		SELECT TOP 1 hdcttd.HopDongChiTietThayDoiID, HDCTTD.DonGia , hdcttd.HopDongChiTietREF, hdcttd.SoLuong
		FROM HopDongThayDoi hdtd
		INNER JOIN HopDongChiTietThayDoi hdcttd 
		ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
			WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
			AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
		ORDER BY hdcttd.HopDongChiTietThayDoiID 	
	)A
	INNER JOIN HopDongChiTiet hdct ON HDCT.HopDongChiTietID = A.HopDongChiTietREF
	WHERE (A.DonGia != HDCT.DonGia) OR (A.SoLuong != hdct.SoLuong)

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
	
	--CHECK HOPDONGCHITIET CO SU THAY DOI VE SOLUONGHD
	SELECT @HopDongChiTietThayDoiSL = A.HopDongChiTietThayDoiID
		,@SoLuong = A.SoLuong, @HopDongChiTiet = A.HopDongChiTietREF 
	  FROM
	(
		SELECT TOP 1 hdcttd.HopDongChiTietThayDoiID, HDCTTD.DonGia , hdcttd.HopDongChiTietREF, hdcttd.SoLuong
		FROM HopDongThayDoi hdtd
		INNER JOIN HopDongChiTietThayDoi hdcttd 
		ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
			WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
			AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
		ORDER BY hdcttd.HopDongChiTietThayDoiID 	
	)A
	INNER JOIN HopDongChiTiet hdct ON HDCT.HopDongChiTietID = A.HopDongChiTietREF
	WHERE (A.SoLuong != hdct.SoLuong)
	
	-- CHECK HOPDONGCHITIET CO SU THAY DOI VE SO LUONG TREN DOT CHAY
	--1. GET SO LUONG DOT CHAY CUA LAN THAY DOI TAI NGAY THUC HIEN
	SELECT @SoLuong = hdct.SoLuong, @DonViTinh = hdct.DonViTinh
	,@ChietKhauHT = hdct.ChietKhau, @DmSanPhamREF = hdct.DmSanPhamREF, @DmWebsiteREF = hdct.DmWebsiteREF
	, @TenWebsite = hdct.TenWebsite
	FROM HopDongChiTiet hdct
	WHERE hdct.HopDongChiTietID = @HopDongChiTietID
		
	SET @DonGiaTheoDVTinhHT = ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_CPDKhongDotChay(@SoLuong,@DonViTinh,@DonGiaHT,@NgayThucHien, @NgayThucHien, @HopDongChiTietID),0)
	SET @DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
	SET @DmWebsiteREF_log = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF)
	SET @TenWebsite = dbo.GetWebsiteLinkByDmWebsiteID(@DmWebsiteREF,@TenWebsite)
	SET @SoLuongHT = @SoLuong
	
	
	--GET SO LUONG DOT CHAY BOOKING TAI THOI DIEM TRUOC THAY DOI
	SELECT TOP 1 @SoNgayDotChayThayDoi = tcdt.SoLuongDotChayHD, 
		@DonGiaLienKeTruoc = tcdt.DonGiaTheoDonVi, 
		@ChietKhauSauTD = tcdt.ChietKhau
	  FROM ThucChayDaTinh tcdt
	WHERE CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	ORDER by tcdt.NgayThucHien DESC
	
	SET @SoNgayDotChayThayDoi = ISNULL(@SoNgayDotChayThayDoi,0)
	SET @DonGiaLienKeTruoc = ISNULL(@DonGiaLienKeTruoc,0)
	SET @ChietKhauSauTD = ISNULL(@ChietKhauSauTD,0)
	
	--NEU CO THAY DOI VE GIA
	IF(@HopDongChiTietThayDoiGia <> 0)
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi giá hoặc số lượng hd: ' + CONVERT(NVARCHAR(30),@DonGiaLienKeTruoc) + '->' + CONVERT(NVARCHAR(30),@DonGiaTheoDVTinhHT) + ');'
		SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTiet: ' + CONVERT(NVARCHAR(30),@HopDongChiTietID)		
	END
	--NEU CO THAY DOI VE CHIET KHAU
	IF(@HopDongChiTietThayDoiCK <>0)
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi chiết khấu: ' + CONVERT(NVARCHAR(30),@ChietKhau) + '->' + CONVERT(NVARCHAR(30),@ChietKhauHT) + ');'
		SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTiet'+ CONVERT(NVARCHAR(30),@HopDongChiTietID)
	END
	
	--CHECK HD CO THAY DOI SOLUONGTHUCCHAY HD
	SET @SoLuongThucChayHT =  isnull(dbo.[ThucChay_GetSoLuongThucChayBooking_CPDKhongDotChay](@SoLuong ,@DonViTinh ,@HopDongChiTietID ,@NgayThucHien ),0)
	
	--TINH SO LUONG THUC CHAY
	SELECT @SoLuongThucChay = SUM(ISNULL(tcdt.SoLuongThucChay,0))
	, @TongGiaTriThucChayDaTinh =  
	SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)) +	SUM(ISNULL(tcdt.GiaTriThayDoi,0))
	FROM ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien 
	AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
	
	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
	SET @TongGiaTriThucChayDaTinh = ISNULL(@TongGiaTriThucChayDaTinh,0)
	
	--TINH SO LUONG THUC CHAY DU TREN BOOKING HIEN TAI
	SET @TongGiaTriThucChayDaTinhHT = @SoLuongThucChayHT*((@DonGiaTheoDVTinhHT*(100-@ChietKhauHT))/100)
	
	IF((@SoLuongThucChayHT <> @SoLuongThucChay) AND (round(@TongGiaTriThucChayDaTinh,0) <> round(@TongGiaTriThucChayDaTinhHT,0)))
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi số lượng thực chạy đã chạy :' + Convert(NVARCHAR(50),@SoLuongThucChay) + '->' + CONVERT(NVARCHAR(30),@SoLuongThucChayHT) + ');'
		SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTiet:' + 	CONVERT(NVARCHAR(30),@HopDongChiTietID)		
	END
	--CHECK HOPDONGTHAYDOI CO THAY DOI DOTCHAY(CHUA TINH GIA TRI THAY DOI)
	
	IF(@TongGiaTriThucChayDaTinhHT <> @TongGiaTriThucChayDaTinh)
	BEGIN
		SET @CountHDTD = 
		(
			SELECT COUNT(tcdt.NgayThucHien) FROM ThucChayDaTinh tcdt
			WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
		)
		
		SET @GiaTriThayDoi = @TongGiaTriThucChayDaTinhHT - @TongGiaTriThucChayDaTinh

		PRINT @GiaTriThayDoi								 
		SET @GiaTriThayDoi = ISNULL(@GiaTriThayDoi,0)
		PRINT N'Ngày:' + CONVERT(NVARCHAR(30),@NgayThucHien) + ', Hợp đồng chi tiết:' + CONVERT(NVARCHAR(30),@HopDongChiTietID) + ', Giá trị thay đổi:' + CONVERT(NVARCHAR(30),@GiaTriThayDoi)
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
					@HopDongREF,@SoHopDong,@HopDongChiTietID,
					@DmSanPhamREF, @DmWebsiteREF_log,@NgayThucHien,
					@GiaTriThayDoi,@DonGiaTheoDVTinhHT,@SoLuongHT,@DonGiaLienKeTruoc,@SoNgayLienKeTruoc,@CONTENT_LOG
					,@NGUON_LOG,'CPD',	'ThucChay',	GETDATE(),
					'ThucChay',GETDATE(),0,
					0,0
				  );
				--UPDATE GIA TRI THAY DOI
				UPDATE ThucChayDaTinh
				SET	GiaTriThayDoi = @GiaTriThayDoi
				, LastModifiedAt = GETDATE()
				WHERE HopDongID = @HopDongREF
				AND HopDongChiTietREF = @HopDongChiTietID
				AND NgayThucHien = @NgayThucHien 
			END
		ELSE
		BEGIN
			PRINT 'co ban ghi'
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
					@HopDongREF,@SoHopDong,@HopDongChiTietID
					, @DmSanPhamREF, @DmWebsiteREF_log,@NgayThucHien,
					@GiaTriThayDoi,@DonGiaTheoDVTinhHT,@SoLuongHT,@DonGiaLienKeTruoc,@SoNgayLienKeTruoc,@CONTENT_LOG
					,@NGUON_LOG,'CPD',	'ThucChay',	GETDATE(),
					'ThucChay',GETDATE(),0,
					0,0
				  );
				
				EXEC [dbo].[ThucChay_InsertThucTreoThayDoi_CPDKhongDotChay] @HopDongChiTietID,@NgayThucHien,@GiaTriThayDoi
			END	
	END
	SELECT 1
END

```
