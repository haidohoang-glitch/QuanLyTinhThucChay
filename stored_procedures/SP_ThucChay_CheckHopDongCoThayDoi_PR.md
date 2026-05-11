# Stored Procedure: `ThucChay_CheckHopDongCoThayDoi_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-08 14:24:22.497000
- **Ngày sửa cuối**: 2014-11-19 12:24:53.660000

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
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongCoThayDoi_PR] 
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
	DECLARE @HopDongChiTietThayDoiGia INT, @HopDongChiTietThayDoiCK INT, @HopDongChiTiet INT
	DECLARE @TongSoLuongThucTreoHT INT, @ChietKhau FLOAT, @DonGia FLOAT, @NgayGioiHanTinh DATETIME
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500)
	DECLARE @CountHDTD INT, @GiaTriThayDoi FLOAT, @DmSanPhamREF INT , @DmWebsiteREF INT, @TenWebsite NVARCHAR(100)
	DECLARE @DonGiaChenhLech FLOAT, @DonGiaLienKeTruoc FLOAT
	DECLARE @TongSoLuongThucTreoDaTinh FLOAT, @DonGiaHienTai FLOAT, @SoluongThucTreoHT INT 

	SET @TongSoLuongThucTreoHT = 0
	SET @NgayGioiHanTinh = '2013-01-01'
	SET @SoluongThucTreoHT = 0
	SET @TongSoLuongThucTreoDaTinh = 0
	SET @GiaTriThayDoi = 0
	SET @CountHDTD = 0
	SET @CONTENT_LOG = ''
	SET @NGUON_LOG = ''
	SET @HopDongChiTietThayDoiGia = 0
	SET @HopDongChiTietThayDoiCK = 0
	--XOA BAN NHUNG BAN GHI DA THUC HIEN INSERT VOI TRUONG HOP CHI CO GIA TRI THAY DOI
		DELETE FROM ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietID
		AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
		AND DotChayHopDong = 'PR_TTR'
		
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
		
		-- CHECK HOPDONGCHITIET CO SU THAY DOI VE SO LUONG THUC TREO PR
		-- GET SO LUONG THUC TREO HIEN TAI
		SET @TongSoLuongThucTreoHT = ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanNgayThucHien_PR(@NgayThucHien,@NgayGioiHanTinh ,@HopDongChiTietID),0)
		
		SELECT @DmSanPhamREF = hdct.DmSanPhamREF, @DmWebsiteREF = hdct.DmWebsiteREF 
		, @TenWebsite = hdct.TenWebsite
		FROM HopDongChiTiet hdct
		WHERE hdct.HopDongChiTietID = @HopDongChiTietID
		
		set @DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
		SET @DmWebsiteREF = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF) 
		set @TenWebsite  = dbo.GetWebsiteLinkByDmWebsiteID(@DmWebsiteREF,@TenWebsite)
		-- GET SO LUONG THUC TREO TRUOC NGAY THUC HIEN
		SET @TongSoLuongThucTreoDaTinh =
		(
			SELECT SUM(ISNULL(tcdt.SoLuongThucChay,0)) 
			FROM ThucChayDaTinh tcdt
			WHERE CONVERT(DATE,TCDT.NgayThucHien) < @NgayThucHien
			AND tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND tcdt.HopDongID = @HopDongREF 
		)
		SET @TongSoLuongThucTreoDaTinh = ISNULL(@TongSoLuongThucTreoDaTinh,0)
		--NEU CO THAY DOI VE GIA
		IF(@HopDongChiTietThayDoiGia <> 0)
		BEGIN
			SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi giá: ' + CONVERT(NVARCHAR(30),@DonGia) + '->' + CONVERT(NVARCHAR(30),@DonGiaHienTai) + ');'
			SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTiet:' + CONVERT(NVARCHAR(30),@HopDongChiTietID) 		
		END
		--NEU CO THAY DOI VE CHIET KHAU
		IF(@HopDongChiTietThayDoiCK <>0)
		BEGIN
			SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi chiết khấu =' + CONVERT(NVARCHAR(30),@ChietKhau) + '->' + CONVERT(NVARCHAR(30),@ChietKhau) + ');'
			SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi: '+ CONVERT(NVARCHAR(30),@HopDongChiTietID) 	
		END
		--NEU SO LUONG THUC TREO CO SU KHAC NHAU
		IF((@TongSoLuongThucTreoHT<> @TongSoLuongThucTreoDaTinh) AND(@TongSoLuongThucTreoDaTinh <> 0))
		BEGIN
			SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi số lượng thực treo =' + Convert(NVARCHAR(20),@TongSoLuongThucTreoDaTinh) + '->' + CONVERT(NVARCHAR(30),@TongSoLuongThucTreoHT) + ');'
			SET @NGUON_LOG = @NGUON_LOG + 'Table:ThucChayHopDongChiTietPR:'	+ CONVERT(NVARCHAR(30),@HopDongChiTietID)
		END
		
		
		IF((@CONTENT_LOG <> '') AND (@TongSoLuongThucTreoDaTinh >0))
		BEGIN
			--GET SO LUONG THUC CHAY TAI THOI DIEM TINH
			SET @SoluongThucTreoHT =
			(
				SELECT tcdt.SoLuongThucChay FROM ThucChayDaTinh tcdt	
				WHERE CONVERT(DATE,TCDT.NgayThucHien) = convert(date,@NgayThucHien)
				AND tcdt.HopDongChiTietREF = @HopDongChiTietID
				AND tcdt.HopDongID = @HopDongREF 
			)
			--GET THANH TIEN TAI THOI DIEM TRUOC THAY DOI
			SET @DonGiaLienKeTruoc =
			(
				SELECT TOP 1
				(CASE when hdcttd.SoLuong = 0 then 0
					else ISNULL(hdcttd.ThanhTien,0)/hdcttd.SoLuong
				  END
				) as DonGiaLienKeTruoc
				FROM HopDongThayDoi hdtd
				INNER JOIN HopDongChiTietThayDoi hdcttd 
				ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
					WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
					AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
					ORDER BY HDCTTD.HopDongChiTietThayDoiID
			)
			SET @DonGiaLienKeTruoc = ISNULL(@DonGiaLienKeTruoc,0)
			--TINH DON GIA SAU TRIET KHAU TRUOC THAY DOI
			
			--TINH DON GIA SAU TRIET KHAU HIEN TAI
			IF(@SoLuongHT = 0)
				SET @DonGiaHienTai = 0;
			ELSE	
				set @DonGiaHienTai = @ThanhTienHDCT/@SoLuongHT
			 							 
			SET @DonGiaChenhLech = @DonGiaHienTai - @DonGiaLienKeTruoc
			
			--TINH SO TIEN THAY DOI KHI THAY DOI DON GIA HOAC CHIET KHAU
			SET @GiaTriThayDoi = @TongSoLuongThucTreoDaTinh * @DonGiaChenhLech
			SET @GiaTriThayDoi = round(ISNULL(@GiaTriThayDoi,0),0)
			
			--VOI TRUONG HOP THUC TREO KHAC SO LUONG
			SET @GiaTriThayDoi = round(@GiaTriThayDoi + (@TongSoLuongThucTreoHT - @SoluongThucTreoHT)*@DonGiaHienTai,0) 
			SET @CONTENT_LOG = @CONTENT_LOG + ';Giá trị thay đổi:' + CONVERT(NVARCHAR(50),convert(bigint,@GiaTriThayDoi)) + ';Website:' + @TenWebsite
			PRINT N'Ngày:' + CONVERT(NVARCHAR(30),@NgayThucHien) + ', HDCT:' + CONVERT(NVARCHAR(30),@HopDongChiTietID) + N', GTTĐ:' + CONVERT(NVARCHAR(30),@GiaTriThayDoi)
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
				@DmSanPhamREF, @DmWebsiteREF,@NgayThucHien,
				@GiaTriThayDoi,@DonGiaHienTai,@TongSoLuongThucTreoHT,@DonGiaLienKeTruoc,@SoluongThucTreoHT,@CONTENT_LOG
				,@NGUON_LOG,'PR',	'ThucChay',	GETDATE(),
				'ThucChay',GETDATE(),0,
				0,0
			  )
			--UPDATE GIA TRI THAY DOI
			UPDATE ThucChayDaTinh
			SET	GiaTriThayDoi = @GiaTriThayDoi,
			LastModifiedAt = GETDATE()
			WHERE HopDongID = @HopDongREF
			AND HopDongChiTietREF = @HopDongChiTietID
			AND NgayThucHien = @NgayThucHien 	
		END
	END
END


```
