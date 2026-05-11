# Stored Procedure: `ThucChay_CheckHopDongCoThayDoi_CPD_bk`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-15 10:46:16.510000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.950000

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
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongCoThayDoi_CPD_bk] 
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
	DECLARE @ChietKhau FLOAT, @DonGia FLOAT, @HopDongChiTietThayDoiGia INT, @HopDongChiTietThayDoiCK INT
	DECLARE @DotChayHopDongChiTietThayDoi INT, @HopDongChiTiet INT
	DECLARE @SoNgayDotChayThayDoi INT
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500)
	DECLARE @CountHDTD INT, @GiaTriThayDoi FLOAT, @NgayTinhGiaTTDLast DATETIME
	DECLARE @DonGiaChenhLech FLOAT, @DonGiaLienKeTruoc FLOAT, @SoLuongThucChay FLOAT
	DECLARE @ThanhTienSauTrietKhauLKTruoc FLOAT
	DECLARE @SoNgayLienKeTruoc FLOAT, @DonGiaHienTai FLOAT

	SET @NgayTinhGiaTTDLast = '2013-09-01'
	SET @SoNgayDotChayThayDoi = 0
	SET @CountHDTD = 0
	SET @CONTENT_LOG = ''
	SET @NGUON_LOG = ''
	SET @DotChayHopDongChiTietThayDoi = 0
	SET @HopDongChiTietThayDoiGia = 0
	SET @HopDongChiTietThayDoiCK = 0
	--CHECK HOP DONG CO SU THAY DOI KHONG
	SET @CountHDTD = 
	(
		SELECT COUNT(*) FROM HopDongThayDoi hdtd
		WHERE hdtd.HopDongFK = @HopDongREF
		AND Convert(date,hdtd.NgayThayDoi) = @NgayThucHien
	)
	SET @CountHDTD = ISNULL(@CountHDTD,0)
	--NEU HOP DONG CO SU THAY DOI
	IF(@CountHDTD >0)
	BEGIN
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
		
		-- CHECK HOPDONGCHITIET CO SU THAY DOI VE SO LUONG TREN DOT CHAY
		--1. GET SO LUONG DOT CHAY CUA LAN THAY DOI TAI NGAY THUC HIEN
		SET @SoNgayDotChayThayDoi = [dbo].[ThucChay_GetSoLuongNgayThayDoiTheoDonViTinh_CPD](@HopDongChiTietID,@NgayThucHien)
		--NEU CO THAY DOI VE GIA
		IF(@HopDongChiTietThayDoiGia <> 0)
		BEGIN
			SET @CONTENT_LOG = @CONTENT_LOG + 'HD co td Gia(idthaydoi =' + CONVERT(NVARCHAR(30),@HopDongChiTietThayDoiGia) + 'Gia cu=' + CONVERT(NVARCHAR(30),@DonGia) + ');'
			SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi, HopDongThayDoi, '		
		END
		--NEU CO THAY DOI VE CHIET KHAU
		IF(@HopDongChiTietThayDoiCK <>0)
		BEGIN
			SET @CONTENT_LOG = @CONTENT_LOG + 'HD co td CK(idthaydoi =' + CONVERT(NVARCHAR(30),@HopDongChiTietThayDoiCK) + 'CK cu=' + CONVERT(NVARCHAR(30),@ChietKhau) + ');'
			SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi, HopDongThayDoi, '
		END
		--NEU CO THAY DOI DOT CHAY
		IF((@SoNgayDotChayThayDoi<> @SoLuongHT) AND(@SoNgayDotChayThayDoi <> 0))
		BEGIN
			SET @CONTENT_LOG = @CONTENT_LOG + 'HD co td DotChay(@ngaythaydoi =' + Convert(NVARCHAR(20),@NgayThucHien) + 'HopDongChiTiet=' + CONVERT(NVARCHAR(30),@HopDongChiTietID) + ');'
			SET @NGUON_LOG = @NGUON_LOG + 'Table:DotChayHopDongChiTietThayDoi, HopDongThayDoi, Booking, '	
		END
		SET @NgayTinhGiaTTDLast =
		(
			SELECT MAX(tcdt.NgayThucHien) 
			FROM ThucChayDaTinh tcdt
			WHERE tcdt.NgayThucHien < @NgayThucHien
			AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
			AND tcdt.GiaTriThayDoi <> 0
		)
		SET @NgayTinhGiaTTDLast = ISNULL(@NgayTinhGiaTTDLast, '2013-09-01')
		--TINH SO LUONG THUC CHAY
		SET @SoLuongThucChay = 	(	
				SELECT ISNULL(sum(tcdt.SoLuongThucChay),0) 
				FROM ThucChayDaTinh tcdt
				WHERE (tcdt.NgayThucHien < @NgayThucHien AND tcdt.NgayThucHien >= @NgayTinhGiaTTDLast)
				AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
			)
		SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
			
		IF((@CONTENT_LOG <> '') AND (@SoLuongThucChay >0))
		BEGIN
			SET @CONTENT_LOG = @CONTENT_LOG + ', Ngay Td truoc day: '+ CONVERT(NVARCHAR(50), @NgayTinhGiaTTDLast)
			--	GET SO LUONG THEO DON VI TINH
			--GET THANH TIEN TAI THOI DIEM TRUOC THAY DOI
			SET @ThanhTienSauTrietKhauLKTruoc =
			(
				SELECT TOP 1 hdcttd.ThanhTien 
				FROM HopDongThayDoi hdtd
				INNER JOIN HopDongChiTietThayDoi hdcttd 
				ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
					WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
					AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
					ORDER BY HDCTTD.HopDongChiTietThayDoiID
			)
			SET @ThanhTienSauTrietKhauLKTruoc = ISNULL(@ThanhTienSauTrietKhauLKTruoc,0)
			--GET SO NGAY TAI THOI DIEM TRUOC THAY DOI
			SET @SoNgayLienKeTruoc = @SoNgayDotChayThayDoi--[dbo].[ThucChay_GetSoLuongNgayThayDoiTheoDonViTinh_CPD](@HopDongChiTietID,@NgayThucHien)
			SET @SoNgayLienKeTruoc = ISNULL(@SoNgayLienKeTruoc,0)
			--TINH DON GIA SAU TRIET KHAU TRUOC THAY DOI
			IF(@SoNgayLienKeTruoc = 0)
				SET @DonGiaLienKeTruoc = 0
			ELSE
				SET @DonGiaLienKeTruoc = @ThanhTienSauTrietKhauLKTruoc/@SoNgayLienKeTruoc
			
			--TINH DON GIA SAU TRIET KHAU HIEN TAI
			IF(@SoLuongHT = 0)
				SET @DonGiaHienTai = 0;
			ELSE	
				set @DonGiaHienTai = @ThanhTienHDCT/@SoLuongHT
			 							 
			SET @DonGiaChenhLech = @DonGiaHienTai - @DonGiaLienKeTruoc
			--TINH SO TIEN THAY DOI
			SET @GiaTriThayDoi = @SoLuongThucChay * @DonGiaChenhLech
			SET @GiaTriThayDoi = ISNULL(@GiaTriThayDoi,0)
			PRINT 'Ngay:' + CONVERT(NVARCHAR(30),@NgayThucHien) + ', HDCT:' + CONVERT(NVARCHAR(30),@HopDongChiTietID) + ', Gia tri td:' + CONVERT(NVARCHAR(30),@GiaTriThayDoi)
			--GHI LOG VIEC THAY DOI
			INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
			  ([ThuChay_LogNNTinhGiaTriThayDoiID],
				[HopDongREF],[SoHopDong],[HopDongChiTietREF],[NgayThucHien],
				[GiaTriThayDoi],[GiaSauCK1],[Soluong1],[GiaSauCK2],[Soluong2],
				[NoiDungLog],[NguonLog],[GhiChu],[CreatedBy],[CreatedAt],
				[LastModifiedBy],[LastModifiedAt],[DeletedStatus],
				[PrintStatus],[RecordStatus]
			  )
			VALUES
			  (NEWID(),
				@HopDongREF,@SoHopDong,@HopDongChiTietID,@NgayThucHien,
				@GiaTriThayDoi,@DonGiaHienTai,@SoLuongHT,@DonGiaLienKeTruoc,@SoNgayLienKeTruoc,@CONTENT_LOG
				,@NGUON_LOG,'CPD',	'ThucChay',	GETDATE(),
				'ThucChay',GETDATE(),0,
				0,0
			  )
			--UPDATE GIA TRI THAY DOI
			UPDATE ThucChayDaTinh
			SET	GiaTriThayDoi = @GiaTriThayDoi
			WHERE HopDongID = @HopDongREF
			AND HopDongChiTietREF = @HopDongChiTietID
			AND NgayThucHien = @NgayThucHien 	
		END
	END
END

```
