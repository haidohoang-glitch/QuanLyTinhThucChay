# Stored Procedure: `sp_TC_CheckHopDongXoaPhanBo_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-19 16:20:20.657000
- **Ngày sửa cuối**: 2022-12-21 15:32:21.693000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongXoaPhanBo_CPM] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ChietKhauBF FLOAT, @ChietKhau FLOAT,@DonGiaBF FLOAT, @DonGia FLOAT, @HopDongChiTietThayDoiGia INT, @HopDongChiTietThayDoiCK INT
	DECLARE @DotChayHopDongChiTietThayDoi INT, @NgayThayDoiMax DATETIME
	DECLARE @SoNgayDotChayThayDoi INT, @DmWebsiteREF INT,@TenWebsite NVARCHAR(100) , @SoLuongHT INT, @DmBannerID INT
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500), @CONTENT_DETAIL_LOG NVARCHAR(MAX)
	DECLARE @CountHDTD INT, @GiaTriThayDoi FLOAT, @SoLuongThucChayByWebiste INT
	DECLARE @DonGiaChenhLech FLOAT, @DonGiaLienKeTruoc FLOAT, @SoLuongThucChay FLOAT
	DECLARE @DonGiaHienTai FLOAT, @TenSanPham NVARCHAR(50), @NgayThayDoiLast DATETIME

	SET @SoNgayDotChayThayDoi = 0
	SET @SoLuongThucChayByWebiste = 0
	SET @CountHDTD = 0
	SET @CONTENT_LOG = ''
	SET @NGUON_LOG = ''
	SET @DotChayHopDongChiTietThayDoi = 0
	SET @HopDongChiTietThayDoiGia = 0
	SET @HopDongChiTietThayDoiCK = 0
	--GET DONGIA VA CHIETKHAU HIEN TAI
	SET @NgayThayDoiMax = 
	(
		SELECT convert(date,MAX(B.NgayThayDoi))
		FROM dbo.HopDongChiTietThayDoi A
		INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
		WHERE 
		A.DeletedStatus <> 1 AND 
		B.DeletedStatus <> 1 AND
		A.HopDongChiTietREF = @HopDongChiTietID
	)
	SET @NgayThayDoiMax = ISNULL(@NgayThayDoiMax,@NgayThucHien)
	IF(@NgayThucHien >= @NgayThayDoiMax)
	BEGIN
			SELECT Top 1 
			@DonGia = hdct.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh), @ChietKhau = hdct.ChietKhau,
			@TenSanPham = HDCT.TenSanPham
			FROM dbo.HopDongChiTiet hdct
			WHERE hdct.DeletedStatus <> 1 AND 
			hdct.HopDongChiTietID = @HopDongChiTietID 
	END
	ELSE
	BEGIN
		SET @NgayThayDoiMax = 
		(
			SELECT Top 1 Convert(date,b.NgayThayDoi)
			FROM dbo.HopDongChiTietThayDoi A
			INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
			WHERE 
			A.DeletedStatus <> 1 AND B.DeletedStatus <> 1 AND
			A.HopDongChiTietREF = @HopDongChiTietID AND	convert(date,B.NgayThayDoi) >=  @NgayThucHien
			Order by B.NgayThayDoi asc
		)	
		
		SELECT TOP 1 
			@DonGia = A.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(A.DonViTinh), @ChietKhau = A.ChietKhau
			,@TenSanPham = A.TenSanPham
			FROM dbo.HopDongChiTietThayDoi A
			INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
			WHERE 
			A.DeletedStatus <> 1 AND B.DeletedStatus <> 1 
			AND a.HopDongChiTietREF <> 0 AND A.HopDongChiTietREF = @HopDongChiTietID 
			AND	convert(date,B.NgayThayDoi) = @NgayThayDoiMax
			Order by A.HopDongChiTietThayDoiID desc

	END
	set @DonGia = ISNULL(@DonGia,0)
	SET @ChietKhau = ISNULL(@ChietKhau,0)
	--GET DONGIA VA CHIETKHAU TRUOC NGAY HIEN TAI
	SELECT  TOP 1 
	@DonGiaLienKeTruoc  = ISNULL(tcdt.DonGiaTheoDonVi,0),
	@ChietKhauBF = ISNULL(tcdt.ChietKhau,0) 
	FROM ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) < @NgayThucHien
	AND tcdt.HopDongID = @HopDongREF
	AND tcdt.DmSanPhamREF = tcdt.DmSanPhamREF
	AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
	ORDER BY tcdt.NgayThucHien desc

	SET @DonGiaLienKeTruoc = ISNULL(@DonGiaLienKeTruoc,0)
	SET @ChietKhauBF = ISNULL(@ChietKhauBF,0)
	--TINH SO LUONG THUC CHAY
	SET @SoLuongThucChay = 	(	
		SELECT ISNULL(sum(tcdt.SoLuongThucChay),0) + SUM(ISNULL(tcdt.SoLuongThayDoi,0))
		FROM ThucChayDaTinh tcdt
		WHERE convert(date,tcdt.NgayThucHien) < @NgayThucHien
		AND tcdt.HopDongID = @HopDongREF
		AND tcdt.DmSanPhamREF = tcdt.DmSanPhamREF
		AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
	)
	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
	--NEU CO THAY DOI VE GIA
	IF(@DonGia <> @DonGiaBF)
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi giá:' + CONVERT(NVARCHAR(30),@DonGiaBF) + '->' + CONVERT(NVARCHAR(30),@DonGia) + ');'
		SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi:'	+ CONVERT(NVARCHAR(50),@HopDongChiTietThayDoiGia)	
	END
	--NEU CO THAY DOI VE CHIET KHAU
	IF(@ChietKhau <> @ChietKhauBF)
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi chiết khấu:' + CONVERT(NVARCHAR(30),@ChietKhauBF) + '->' + CONVERT(NVARCHAR(30),@ChietKhau) + ');'
		SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi: ' + CONVERT(NVARCHAR(30),@HopDongChiTietThayDoiCK)
	END
	
	IF((@CONTENT_LOG <> '')AND (@SoLuongThucChay >0))
	BEGIN
		--TINH DONGIACHENHLECH 
		SET @DonGiaChenhLech = @DonGia*(100-@ChietKhau)/100 - @DonGiaLienKeTruoc*(100-@ChietKhauBF)/100
		
		DECLARE Record_Cursor_TCDT CURSOR FOR 
	    
		SELECT distinct tcdt.DmWebsiteREF, tcdt.TenWebsite, tcdt.DmBannerREF
		  FROM ThucChayDaTinh tcdt
		WHERE tcdt.SoHopDong = @SoHopDong
		AND tcdt.HopDongChiTietREF = @HopDongChiTietID
		AND tcdt.DmSanPhamREF = @DmSanPhamREF
		
		OPEN Record_Cursor_TCDT
		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor_TCDT INTO @DmWebsiteREF, @TenWebsite, @DmBannerID
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--UPDATE GIA TRI THAY DOI CHO TUNG WEBSITE
				SET @CONTENT_DETAIL_LOG = ''	
				SET @SoLuongThucChayByWebiste = 0
				SET @GiaTriThayDoi = 0
				--GET THONG TIN THƯC CHAY THEO WEBSITE
				set @NgayThayDoiLast =
				(
					SELECT max(tcdt.NgayThucHien)
					  FROM ThucChayDaTinh tcdt
					WHERE (convert(date,tcdt.NgayThucHien) < @NgayThucHien)
					AND tcdt.SoHopDong = @SoHopDong
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.SoLuongThucChay <>0
					AND tcdt.GiaTriThayDoi <> 0
				)
				IF(@NgayThayDoiLast IS NULL)
				BEGIN
					SET @NgayThayDoiLast =
					(
						SELECT MIN(tcdt.NgayThucHien)
						  FROM ThucChayDaTinh tcdt
						WHERE (convert(date,tcdt.NgayThucHien) < @NgayThucHien)
						AND tcdt.SoHopDong = @SoHopDong
						AND tcdt.HopDongChiTietREF = @HopDongChiTietID
						AND tcdt.DmSanPhamREF = @DmSanPhamREF
						AND tcdt.SoLuongThucChay <>0
					)
					SET @NgayThayDoiLast = dateadd(d,-1,@NgayThayDoiLast)
				END 
				SET @SoLuongThucChayByWebiste = 
				(
					SELECT sum(isnull(tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0))  FROM ThucChayDaTinh tcdt
					WHERE ((convert(date,tcdt.NgayThucHien) > @NgayThayDoiLast) AND (convert(date,tcdt.NgayThucHien) <= @NgayThucHien))
					AND tcdt.SoHopDong = @SoHopDong
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.DmWebsiteREF = @DmWebsiteREF
					AND tcdt.DmBannerREF = @DmBannerID
					AND tcdt.SoLuongThucChay <>0	
				)
				SET @GiaTriThayDoi = @SoLuongThucChayByWebiste * @DonGiaChenhLech
				SET @GiaTriThayDoi = ROUND(ISNULL(@GiaTriThayDoi,0),0)
				SET @CONTENT_DETAIL_LOG = N'Giá trị thay đổi:' + CONVERT(NVARCHAR(30),convert(bigint,@GiaTriThayDoi))
				+ '; Website:' + @TenWebsite 
				PRINT @CONTENT_LOG
				set @CountHDTD =
				(
					SELECT COUNT(*) FROM ThucChayDaTinh tcdt
					WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND CONVERT(DATE,tcdt.NgayThucHien) = @NgayThucHien	
					AND tcdt.SoHopDong = @SoHopDong
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.DmWebsiteREF = @DmWebsiteREF
					AND tcdt.DmBannerREF = @DmBannerID
				)
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
						@GiaTriThayDoi,@DonGia*(100-@ChietKhau)/100,@SoLuongHT,@DonGiaBF*(100-@ChietKhauBF)/100,@SoLuongHT
						,@CONTENT_LOG + @CONTENT_DETAIL_LOG
						,@NGUON_LOG,'CPM',	'ThucChay',	GETDATE(),
						'ThucChay',GETDATE(),0,
						0,0
					  )
					--UPDATE GIA TRI THAY DOI
					UPDATE ThucChayDaTinh
					SET	GiaTriThayDoi = @GiaTriThayDoi
					, LastModifiedAt = GETDATE()
					WHERE HopDongID = @HopDongREF
					AND DmSanPhamREF = @DmSanPhamREF
					AND DmWebsiteREF = @DmWebsiteREF
					AND DmBannerREF = @DmBannerID
					AND HopDongChiTietREF = @HopDongChiTietID
					AND convert(date,NgayThucHien) = @NgayThucHien 	
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
							@GiaTriThayDoi,@DonGiaHienTai,@SoLuongHT,@DonGiaLienKeTruoc,@SoLuongHT,@CONTENT_LOG
							,@NGUON_LOG,'CPM',	'ThucChay',	GETDATE(),
							'ThucChay',GETDATE(),0,
							0,0
						  )
						IF(@HopDongChiTietID <> 0)
						BEGIN
							EXEC sp_TC_InsertThucTreoThayDoi_CPM @HopDongChiTietID, @NgayThucHien,	@GiaTriThayDoi,	@DmWebsiteREF ,	@TenWebsite, @DmBannerID
						END
						ELSE
							BEGIN
							     EXEC	sp_TC_InsertThucTreoThayDoi_CPMBySoHopDong	@HopDongREF ,@SoHopDong ,	@DmSanphamREF ,	@TenSanPham ,@HopDongChiTietID,	@NgaythucHien,	@GiaTriThayDoi,	@DmWebsiteREF,	@TenWebsite , @DmBannerID
							END
					END
				
			FETCH NEXT FROM Record_Cursor_TCDT into @DmWebsiteREF, @TenWebsite, @DmBannerID
			END
		CLOSE Record_Cursor_TCDT
		DEALLOCATE Record_Cursor_TCDT 							 
	END
END

```
