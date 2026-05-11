# Stored Procedure: `ThucChay_CheckHopDongXoaPhanBo_CPD_bk20170919`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-19 10:00:51.257000
- **Ngày sửa cuối**: 2017-09-19 10:00:51.257000

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
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongXoaPhanBo_CPD_bk20170919] 
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
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500)
	DECLARE @TenWebste NVARCHAR(100), @TenChuyenMuc NVARCHAR(100), @TenBanner NVARCHAR(100), @GiaTriThayDoi FLOAT
	DECLARE @Soluong INT , @DonGia INT	, @CountHDTD INT, @DmSanPhamREF INT, @DmWebsiteREF INT
	--GET THONG TIN PHAN BO
	SELECT TOP 1 
	@TenWebste = hdcttd.TenWebsite, @TenChuyenMuc = hdcttd.TenChuyenMuc
	,@TenBanner = hdcttd.TenViTri, @Soluong = hdcttd.SoLuong, @DonGia = hdcttd.DonGia
	, @DmSanPhamREF = hdcttd.DmSanPhamREF, @DmWebsiteREF = hdcttd.DmWebsiteREF
	FROM HopDongThayDoi hdtd
	INNER JOIN HopDongChiTietThayDoi hdcttd 
	ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
		WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
		AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
	ORDER BY hdcttd.HopDongChiTietThayDoiID 
	
	SET @TenWebste = ISNULL(@TenWebste,'')
	SET @TenChuyenMuc = ISNULL(@TenChuyenMuc, '')
	SET @TenBanner = ISNULL(@TenBanner,'')
	SET @Soluong = ISNULL(@Soluong, 0)
	SET @DonGia = ISNULL(@DonGia, 0)
	SET @DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
	SET @DmWebsiteREF = ISNULL(@DmWebsiteREF,0)
		
	SET @CONTENT_LOG = @CONTENT_LOG + N'Phân bổ :' + @TenWebste + '->' + @TenChuyenMuc + '->' + @TenBanner
	SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi:' + 	CONVERT(NVARCHAR(30),@HopDongChiTietID)
	
		--TINH SO LUONG THUC CHAY
	SET @GiaTriThayDoi = 	(	
			SELECT SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)) + SUM(ISNULL(tcdt.GiaTriThayDoi,0))  
			FROM ThucChayDaTinh tcdt
			WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien 
			AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
		)
	set @GiaTriThayDoi= ISNULL(@GiaTriThayDoi,0)
	IF((@CONTENT_LOG <> '')AND (@GiaTriThayDoi <>0))
	BEGIN
		SET @CountHDTD = 
		(
			SELECT COUNT(tcdt.NgayThucHien) FROM ThucChayDaTinh tcdt
			WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
		)
		set @GiaTriThayDoi= - @GiaTriThayDoi
		--NEU TON TAI BAN GHI THUCCHAYDATINH CUA HOP DONG CHI TIET NAY THI THUC HIEN UPDATE
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
				@GiaTriThayDoi,0,0,@DonGia,@Soluong,@CONTENT_LOG
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
					@GiaTriThayDoi,0,0,@DonGia,@Soluong,@CONTENT_LOG
					,@NGUON_LOG,'CPD',	'ThucChay',	GETDATE(),
					'ThucChay',GETDATE(),0,
					0,0
				  );
				EXEC [dbo].[ThucChay_InsertThucTreoThayDoi_CPD] @HopDongChiTietID,@NgaythucHien,@GiaTriThayDoi
			END			
	END
END

```
