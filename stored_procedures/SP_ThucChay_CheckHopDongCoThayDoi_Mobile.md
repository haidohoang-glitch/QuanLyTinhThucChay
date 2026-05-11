# Stored Procedure: `ThucChay_CheckHopDongCoThayDoi_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-30 11:24:16.887000
- **Ngày sửa cuối**: 2016-02-18 13:01:17.657000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
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
--ThucChay_CheckHopDongCoThayDoi_Mobile 40887,'QC0480216',342,91102,'2016-02-15',3
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongCoThayDoi_Mobile] 
	-- Add the parameters for the stored procedure here
	@HopDongID INT,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@BannerType INT--,
	--@ProductUnitName NVARCHAR(50)
	
AS
BEGIN
	DECLARE @ThanhTienTCDTBF FLOAT, @ThanhTienTCDT FLOAT, @IsKhuyenMai INT,
			@DonViTinh NVARCHAR(50),@ChietKhauTCDT FLOAT,
			@DonGiaTheoDonViTinh INT, @SoLuongThucChay INT,
			@GiaTriThayDoi FLOAT, @SoLuongThayDoi FLOAT,
			@DonGiaBF FLOAT, @DonGia FLOAT,
			@ChietKhauBF FLOAT, @ChietKhau FLOAT,
			@SoLuongHDBF FLOAT,@SoLuongHD FLOAT,
			@HopDongChiTietThayDoiCK FLOAT,
			@DonGiaChenhLech FLOAT,@DmWebsiteREF INT, @TenWebsite NVARCHAR(50),
			@NgayThayDoiLast DATETIME,@SoLuongThucChayByWebiste FLOAT,@CountHDTD INT,
			@SoLuongTCDTTheoWebsite FLOAT, @SoLuongTCTheoWebsite FLOAT, 
			@HopDongChiTietThayDoiGia INT
			;
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500), @CONTENT_DETAIL_LOG NVARCHAR(MAX)
	
	SET @CONTENT_LOG = '';
	SET @NGUON_LOG = '';
	SET @DonGiaChenhLech  = 0;
	SET @HopDongChiTietThayDoiGia = 0; 
	SET @HopDongChiTietThayDoiCK = 0;
	SET @ThanhTienTCDT = 0;
	
	SELECT @IsKhuyenMai = IsKhuyenMai,		  
		   @ChietKhau   = hdct.ChietKhau,
		   @SoLuongHD     = hdct.SoLuong		   
	FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	
	--I. Tinh thanh tien thuc chay da tinh den ngay hien tai 
	SELECT @ThanhTienTCDTBF = (CASE WHEN @IsKhuyenMai = 0 THEN SUM(ISNULL(tcdtm.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdtm.GiaTriThayDoi,0))
									ELSE SUM(ISNULL(tcdtm.ThanhTienKM,0) + ISNULL(tcdtm.GiaTriKMThayDoi,0))
								END)
	FROM ThucChayDaTinhMobile tcdtm
	WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID
	AND tcdtm.DmSanPhamREF  =  @DmSanPhamREF
	AND tcdtm.NgayThucHien <= @NgayThucHien
	--AND tcdtm.DmViTriREF = @BannerType
		
	--II. Tinh thanh tien thuc chay <= NgayThucHien theo du lieu NgayThucHien						   
	--II.1 Don gia
	SET @DonGiaTheoDonViTinh = (SELECT dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(@HopDongChiTietID,dbo.ThucChay_GetDonViTinhMobileByHopDongChiTietID(@HopDongChiTietID,@NgayThucHien),@BannerType,@NgayThucHien))
	        
	SET @DonGiaTheoDonViTinh = ISNULL(@DonGiaTheoDonViTinh, 0)
	--II.2 SoLuongThucChay	<= NgayThucHien
	SELECT @SoLuongThucChay = (CASE WHEN @IsKhuyenMai = 0 THEN SUM(ISNULL(tcdtm.SoLuongThucChay,0) + ISNULL(tcdtm.SoLuongThayDoi,0))
									ELSE   SUM(ISNULL(tcdtm.SoLuongThucChayKM,0) + ISNULL(tcdtm.SoLuongKMThayDoi,0))
							   END
							   )	
	FROM ThucChayDaTinhMobile tcdtm
	WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID AND
		tcdtm.DmSanPhamREF = @DmSanPhamREF
	-- II.3 Chiet khau
	SELECT @ChietKhauTCDT = (CASE WHEN @IsKhuyenMai = 0 THEN @ChietKhau
									ELSE 0
							   END
							   )	
	-- Ket qua:
	SET @ThanhTienTCDT = @SoLuongThucChay * @DonGiaTheoDonViTinh * (100 - @ChietKhauTCDT)/100
	-- kiem tra
	IF (@ThanhTienTCDTBF <> @ThanhTienTCDT)
		BEGIN
			--Kiem tra thay doi thong tin gia
			SET @DonGiaBF = (SELECT TOP 1 DonGia
							FROM ThucChayDaTinhMobile tcdtm 
							WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID 
								AND tcdtm.DmSanPhamREF = @DmSanPhamREF
								AND tcdtm.NgayThucHien < @NgayThucHien
								--AND tcdtm.DmViTriREF = @BannerType
							ORDER BY tcdtm.NgayThucHien DESC);
							
			SET @ChietKhauBF = (SELECT TOP 1 ChietKhau
							FROM ThucChayDaTinhMobile tcdtm 
							WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID 
								AND tcdtm.DmSanPhamREF = @DmSanPhamREF
								AND tcdtm.NgayThucHien < @NgayThucHien
								--AND tcdtm.DmViTriREF = @BannerType
							ORDER BY tcdtm.NgayThucHien DESC);
			
			SET @SoLuongHDBF = (SELECT TOP 1 SoLuong
							FROM ThucChayDaTinhMobile tcdtm 
							WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID 
								AND tcdtm.DmSanPhamREF = @DmSanPhamREF
								AND tcdtm.NgayThucHien < @NgayThucHien
								--AND tcdtm.DmViTriREF = @BannerType
							ORDER BY tcdtm.NgayThucHien DESC);	
													
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
			
			--NEU CO THAY DOI VE SO LUONG		
			IF(@SoLuongHD <> @SoLuongHDBF)
				BEGIN
					SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi số lượng:' + CONVERT(NVARCHAR(30),@SoLuongHDBF) + '->' + CONVERT(NVARCHAR(30),@SoLuongHD) + ');'
					SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi: ' + CONVERT(NVARCHAR(30),@HopDongChiTietThayDoiCK)					
					EXEC [ThucChay_UpdateGiaTriTDTCMobileThucTreoByNgayLog] @NgayThucHien ,@HopDongID ,	@DmSanPhamREF ,	@HopDongChiTietID, @CONTENT_LOG	
					END																						
				END		
			ELSE --Khong thay doi so luong
			BEGIN
				--TINH DONGIACHENHLECH 
		    SELECT @DonGiaChenhLech = @DonGia*(100-@ChietKhau)/100 - @DonGiaBF*(100-@ChietKhauBF)/100

			DECLARE Record_Cursor_TCDT CURSOR FOR 
			    
				SELECT DISTINCT tcdt.DmWebsiteREF, tcdt.TenWebsite
				  FROM ThucChayDaTinhMobile tcdt
				WHERE tcdt.HopDongID = @HopDongID
				AND tcdt.HopDongChiTietREF = @HopDongChiTietID
				AND tcdt.DmSanPhamREF = @DmSanPhamREF
				--AND tcdt.DmViTriREF = @BannerType
				
				OPEN Record_Cursor_TCDT
				-- Perform the first fetch.
				FETCH NEXT FROM Record_Cursor_TCDT INTO @DmWebsiteREF, @TenWebsite	
				WHILE @@FETCH_STATUS = 0
					BEGIN
						SET @SoLuongTCDTTheoWebsite = (SELECT SUM(ISNULL(tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0))
						                                     FROM ThucChayDaTinhMobile tcdt 
						                                     WHERE tcdt.HopDongID = @HopDongID 
						                                     AND tcdt.HopDongChiTietREF = @HopDongChiTietID
						                                     AND tcdt.DmWebsiteREF = @DmWebsiteREF 
						                                     AND tcdt.TenWebsite = @TenWebsite
						                                     AND tcdt.NgayThucHien <=@NgayThucHien	
						                                    -- AND tcdt.DmViTriREF = @BannerType												 
													  )
				 
						
						SELECT @SoLuongTCTheoWebsite =  (SELECT SUM(ISNULL(tcdt.TongClickThucChay,0))
						                                     FROM ThucChay tcdt
															 WHERE tcdt.TypeProduct = 10 
															 AND dbo.ThucChay_FormatSoHopDong(tcdt.SoHopDong) = @SoHopDong 
						                                     AND tcdt.HopDongChiTietREF = @HopDongChiTietID
						                                     AND tcdt.DmWebsiteREF = @DmWebsiteREF 
						                                     AND dbo.ThucChay_FormatDomainName(TenWebsite) = @TenWebsite
						                                     AND tcdt.NgayThucHien <=@NgayThucHien
						                                    -- AND tcdt.BannerType = @BannerType
													   )
						set @SoLuongThucChayByWebiste = @SoLuongTCDTTheoWebsite - @SoLuongTCTheoWebsite
						SET @GiaTriThayDoi = @SoLuongThucChayByWebiste * @DonGiaChenhLech
						SET @GiaTriThayDoi = ISNULL(@GiaTriThayDoi,0)
						--SET @GiaTriThayDoi = ROUND(ISNULL(@GiaTriThayDoi,0),0) + @GiaTriThayDoi_HDTD_SL
						SET @CONTENT_DETAIL_LOG = N'Giá trị thay đổi:' + CONVERT(NVARCHAR(30),convert(bigint,@GiaTriThayDoi))
						+ '; Website:' + @TenWebsite
						--
						set @CountHDTD =
						(
							SELECT COUNT(*) FROM ThucChayDaTinhMobile tcdt
							WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
							AND CONVERT(DATE,tcdt.NgayThucHien) = @NgayThucHien	
							AND tcdt.HopDongID         = @HopDongID
							AND tcdt.HopDongChiTietREF = @HopDongChiTietID
							AND tcdt.DmSanPhamREF      = @DmSanPhamREF
							AND tcdt.DmWebsiteREF      = @DmWebsiteREF
							--AND tcdt.DmViTriREF = @BannerType
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
								@HopDongID,@SoHopDong,@HopDongChiTietID, @DmSanPhamREF, @DmWebsiteREF,@NgayThucHien,
								@GiaTriThayDoi,@DonGia*(100-@ChietKhau)/100,0,@DonGiaBF*(100-@ChietKhauBF)/100,0
								,@CONTENT_LOG + @CONTENT_DETAIL_LOG
								,@NGUON_LOG,'Mobile','ThucChay',GETDATE(),'ThucChay',GETDATE(),0,0,0
							  )
							--UPDATE GIA TRI THAY DOI
							UPDATE ThucChayDaTinhMobile
							SET	GiaTriThayDoi = @GiaTriThayDoi
							WHERE HopDongID = @HopDongID
							AND DmSanPhamREF = @DmSanPhamREF
							AND DmWebsiteREF = @DmWebsiteREF
							AND HopDongChiTietREF = @HopDongChiTietID
							AND convert(date,NgayThucHien) = @NgayThucHien
							--AND DmViTriREF = @BannerType 	
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
									@HopDongID,@SoHopDong,@HopDongChiTietID, @DmSanPhamREF, @DmWebsiteREF,@NgayThucHien,
									@GiaTriThayDoi,@DonGia,@SoLuongHD,@DonGiaBF,0,@CONTENT_LOG
									,@NGUON_LOG,'Mobile','ThucChay',GETDATE(),'ThucChay',GETDATE(),0,0,0
								  )
								
								EXEC ThucChay_InsertGiaTriThayDoi_Mobile @HopDongChiTietID,@NgayThucHien,@GiaTriThayDoi,@DmWebsiteREF,@TenWebsite, @BannerType--, @ProductUnitName										
							END							
						FETCH NEXT FROM Record_Cursor_TCDT into @DmWebsiteREF, @TenWebsite
					END
				CLOSE Record_Cursor_TCDT
				DEALLOCATE Record_Cursor_TCDT 
			END 	
SELECT '1'
END

```
