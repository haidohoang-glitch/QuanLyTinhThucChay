# Stored Procedure: `ThucChay_CheckHopDongXoaPhanBo_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-02 09:59:45.800000
- **Ngày sửa cuối**: 2016-02-18 10:20:45.737000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@BannerType` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongXoaPhanBo_Mobile] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@BannerType INT--,
	--@ProductUnitName NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DonGiaBF INT,
			@CONTENT_DETAIL_LOG NVARCHAR(MAX),@CONTENT_LOG NVARCHAR(MAX),@NGUON_LOG NVARCHAR(MAX), 
			@DmWebsiteREF INT, @TenWebsite NVARCHAR(50), @IsKhuyenMai INT,
	        @SoLuongThucChayByWebiste INT, @GiaTriThayDoi INT,@NgayThayDoiLast DATETIME,@CountHDTD INT;

	SET @CONTENT_DETAIL_LOG = '';
	SET @CONTENT_LOG = '';	        
	SET @NGUON_LOG = '';
	SET @IsKhuyenMai = (SELECT TOP 1 IsKhuyenMai 
							FROM ThucChayDaTinhMobile tcdtm
							WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID
								AND tcdtm.DmSanPhamREF = @DmSanPhamREF
								AND tcdtm.DmViTriREF = @BannerType
							ORDER BY tcdtm.NgayThucHien DESC);
	        
	BEGIN
		--TINH DONGIACHENHLECH 
--		SET @DonGiaChenhLech = @DonGia*(100-@ChietKhau)/100 - @DonGiaLienKeTruoc*(100-@ChietKhauBF)/100
		
		DECLARE Record_Cursor_TCDT CURSOR FOR 
	    
		SELECT distinct tcdt.DmWebsiteREF, tcdt.TenWebsite
		  FROM ThucChayDaTinhMobile tcdt
		WHERE tcdt.SoHopDong = @SoHopDong
		AND tcdt.HopDongChiTietREF = @HopDongChiTietID
		AND tcdt.DmSanPhamREF = @DmSanPhamREF
		--AND tcdt.DmViTriREF = @BannerType
		
		OPEN Record_Cursor_TCDT
		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor_TCDT INTO @DmWebsiteREF, @TenWebsite
			
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
					  FROM ThucChayDaTinhMobile tcdt
					WHERE (convert(date,tcdt.NgayThucHien) < @NgayThucHien)
					AND tcdt.SoHopDong = @SoHopDong
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.SoLuongThucChay <>0
					AND tcdt.GiaTriThayDoi <> 0
					--AND tcdt.DmViTriREF = @BannerType
				)
				IF(@NgayThayDoiLast IS NULL)
				BEGIN
					SET @NgayThayDoiLast =
					(
						SELECT MIN(tcdt.NgayThucHien)
						  FROM ThucChayDaTinhMobile tcdt
						WHERE (convert(date,tcdt.NgayThucHien) < @NgayThucHien)
						AND tcdt.SoHopDong = @SoHopDong
						AND tcdt.HopDongChiTietREF = @HopDongChiTietID
						AND tcdt.DmSanPhamREF = @DmSanPhamREF
						AND tcdt.SoLuongThucChay <>0
						--AND tcdt.DmViTriREF = @BannerType
					)
					SET @NgayThayDoiLast = dateadd(d,-1,@NgayThayDoiLast)
				END 
				
				SELECT @GiaTriThayDoi = -(CASE WHEN @IsKhuyenMai = 0 THEN SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)+ ISNULL(tcdt.GiaTriThayDoi,0))
										      ELSE SUM(ISNULL(tcdt.ThanhTienKM,0)+ ISNULL(tcdt.GiaTriKMThayDoi,0))
										 END)	
					FROM ThucChayDaTinhMobile tcdt
					WHERE ((convert(date,tcdt.NgayThucHien) > @NgayThayDoiLast) AND (convert(date,tcdt.NgayThucHien) <= @NgayThucHien))
					AND tcdt.SoHopDong = @SoHopDong
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.DmWebsiteREF = @DmWebsiteREF
					AND tcdt.SoLuongThucChay <>0	
					--AND tcdt.DmViTriREF = @BannerType
				
				
				SET @CONTENT_DETAIL_LOG = N'Giá trị thay đổi:' + CONVERT(NVARCHAR(30),convert(bigint,@GiaTriThayDoi))
				+ '; Website:' + @TenWebsite 

				set @CountHDTD =
				(
					SELECT COUNT(*) FROM ThucChayDaTinhMobile tcdt
					WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND CONVERT(DATE,tcdt.NgayThucHien) = @NgayThucHien	
					AND tcdt.SoHopDong = @SoHopDong
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.DmWebsiteREF = @DmWebsiteREF
					--AND tcdt.DmViTriREF = @BannerType
				)		
				IF 	(@CountHDTD <> 0)
					--UPDATE GIA TRI THAY DOI
					UPDATE ThucChayDaTinhMobile SET
						GiaTriThayDoi =(CASE WHEN @IsKhuyenMai = 0 THEN  @GiaTriThayDoi
										 ELSE 0
										 END),
					    GiaTriKMThayDoi = (CASE WHEN @IsKhuyenMai = 1 THEN  @GiaTriThayDoi
										   ELSE 0
										   END),
					    LastModifiedAt = GETDATE()
					WHERE HopDongID = @HopDongREF
					AND DmSanPhamREF = @DmSanPhamREF
					AND DmWebsiteREF = @DmWebsiteREF
					AND HopDongChiTietREF = @HopDongChiTietID
					AND convert(date,NgayThucHien) = @NgayThucHien 	
					--AND DmViTriREF = @BannerType
				
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
							@GiaTriThayDoi,
							0,--@DonGiaHienTai,
							0,--@SoLuongHT,
							@DonGiaBF,
							0,--@SoLuongHT,
							@CONTENT_LOG,
							@NGUON_LOG,'Mobile','ThucChay',GETDATE(),'ThucChay',GETDATE(),0,0,0
						  )

					EXEC ThucChay_InsertGiaTriThayDoi_Mobile @HopDongChiTietID,@NgayThucHien,@GiaTriThayDoi,@DmWebsiteREF,@TenWebsite,@BannerType--, @ProductUnitName			
					END
				
			FETCH NEXT FROM Record_Cursor_TCDT into @DmWebsiteREF, @TenWebsite					 
	END
END

```
