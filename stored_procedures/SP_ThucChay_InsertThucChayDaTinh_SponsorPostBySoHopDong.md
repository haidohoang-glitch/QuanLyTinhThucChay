# Stored Procedure: `ThucChay_InsertThucChayDaTinh_SponsorPostBySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-12 09:07:52.877000
- **Ngày sửa cuối**: 2014-11-19 12:25:04.463000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmChienDichREF` | `int(4)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- Stored Procedure

-- USE [ABM_hai]
-- GO
-- /****** Object:  StoredProcedure [dbo].[ThucChay_InsertThucChayDaTinh_SponsorPostBySoHopDong]    Script Date: 06/13/2014 10:15:51 ******/
-- SET ANSI_NULLS ON
-- GO
-- SET QUOTED_IDENTIFIER ON
-- GO
-- -- =============================================
-- -- Author:		<Author,,Name>
-- -- Create date: <Create Date,,>
-- -- Description:	<Description,,>
-- -- =============================================
 /* NB261113	56	dantri.com.vn	257	408
 EXEC dbo.[ThucChay_InsertThucChayDaTinh_SponsorPostBySoHopDong]
 '2014-06-17', --@NgayThucHien
 'DT1180913', --@SoHopDong
 56, --@DmWebsiteREF
 'dantri.com.vn', --@TenWebsite
 132, --@DmChienDichREF
 228, --@DmBannerREF
 'CLICK' --@DonViTinh
 */
 CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_SponsorPostBySoHopDong]
 	@NgayThucHien	DATETIME,
 	@SoHopDong		NVARCHAR(50),
 	@DmWebsiteREF	INT,
 	@TenWebsite		NVARCHAR(50),
 	@DmChienDichREF	INT,
 	@DmBannerREF	INT,
 	@DonViTinh		NVARCHAR(50)
 AS
 BEGIN
 	-- SET NOCOUNT ON added to prevent extra result sets from
 	-- interfering with SELECT statements.
 	SET NOCOUNT ON;

 	DECLARE @PhanBoId		INT, 
 			@IsKhuyenMai	INT,
 			@TypeInsert		INT

 	DECLARE @SoLuongThucChaySP		INT = 0, 
 			@SoLuongDaChay			INT = 0, 
 			@SoLuongThucChay		INT = 0, 
 			@DonViTinhHD			 NVARCHAR(50),
 			@DonViTinhPhanBo		NVARCHAR(50),
 			@DonViTinhPhanBoOld NVARCHAR(50),
 			@DonGiaPhanBo			INT,
 			@NgayKyHopDong			DATETIME,
 			@ExistPhuongPhapSP		INT,
 			@GiaTriChietKhauPhanBo	FLOAT,
 			@ChietKhauPhanBo		INT,
 			@DonGiaSauCK			FLOAT,
 			@DonGiaPhanBoOld FLOAT

 	DECLARE @SoLuongThucChayPhanBo	INT, 
 			@SoLuongPhanBoHopDong	INT

 	DECLARE @ThanhTienThucChaySanPham FLOAT = 0,
 			@ThanhTienPhanBoHopDong		FLOAT = 0,
 			@ThanhTienThucChayPhanBo	FLOAT = 0,
 			@ThanhTienThucChay			FLOAT = 0,
 			@ThanhTienKhuyenMaiPhanBo	FLOAT = 0,
 			@ThanhTienThucChayPhanBoKM	FLOAT = 0,
 			@ThanhTienThucChayKM		FLOAT = 0,
 			@SoLuongThucChayKM			INT = 0,
 			@SoLuongLechTreoHa			INT = 0,
 			@ThanhTienLechTreoHa		FLOAT = 0,
 			@ThanhTienHopDong			FLOAT,
 			@ThanhTienThucChayHopDong	FLOAT,
 			@ThanhTienThucChayTruocCK	FLOAT = 0,
 			@ThanhTienTruocChietKhauHD FLOAT = 0
 		

 	DECLARE @TongViewThucChay		INT = 0,
 			@TongClickThucChay		INT = 0,
 			@DonGiaSanPham			INT = 0,
 			@DonGiaTheoDonViTinhSP	INT = 0

 	IF @DonViTinh = 'CLICK' SET @DonViTinhHD = 'CPC'
 		ELSE SET @DonViTinhHD = 'CPM'
	
	
 	SET @SoLuongThucChaySP = 0;
 	SET @SoLuongThucChaySP = (
 		SELECT	CASE WHEN @DonViTinh = 'VIEW' THEN ISNULL(SUM(tc.TongViewThucChay),0)
 					 ELSE ISNULL(SUM(tc.TongClickThucChay),0)
 				END AS SoLuongThucChay
 		FROM ThucChay AS tc
 		WHERE tc.NgayThucHien = @NgayThucHien 
 			AND tc.SoHopDong = @SoHopDong 
 			AND tc.DmWebsiteREF = @DmWebsiteREF 
 			AND tc.DmBannerREF = @DmBannerREF
 			AND tc.DmChienDichREF = @DmChienDichREF
 			
 	)

 	PRINT 'New---SoLuongSP: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySP)

 	SET @TongViewThucChay = 0;
 	SET @TongViewThucChay = (SELECT ISNULL(SUM(tc.TongViewThucChay),0)
 	                          FROM ThucChay AS tc	                        
 	                          WHERE tc.NgayThucHien = @NgayThucHien
 								AND tc.SoHopDong = @SoHopDong
 								AND tc.DmWebsiteREF = @DmWebsiteREF	
 								AND tc.DmChienDichREF = @DmChienDichREF
 								AND tc.DmBannerREF = @DmBannerREF					 
 	)

 	SET @TongClickThucChay = 0;
 	SET @TongClickThucChay = (SELECT ISNULL(SUM(tc.TongClickThucChay),0)
 	                          FROM ThucChay AS tc	                        
 	                          WHERE tc.NgayThucHien = @NgayThucHien
 								AND tc.SoHopDong = @SoHopDong
 								AND tc.DmWebsiteREF = @DmWebsiteREF	
 								AND tc.DmChienDichREF = @DmChienDichREF
 								AND tc.DmBannerREF = @DmBannerREF						 
 	)

 	SET @DonGiaSanPham = 0;

 	SET @DonGiaSanPham = ISNULL(@DonGiaSanPham,0);

 	SET @DonGiaTheoDonViTinhSP = 0;

 	SET @DonGiaTheoDonViTinhSP = ISNULL(@DonGiaTheoDonViTinhSP,0);

-- 	PRINT 'DonGiaSanPham: ' + CONVERT(NVARCHAR(50),@DonGiaSanPham);
	
 	SET @NgayKyHopDong = (SELECT hd.NgayKyHopDong FROM HopDong AS hd WHERE hd.SoHopDong = @SoHopDong)

 	IF @SoLuongThucChaySP > 0
 	BEGIN	
 		DECLARE hd_cursor CURSOR FOR
 			SELECT hdct.HopDongChiTietID
 			FROM HopDong AS hd 
 				INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
 			WHERE
 				hd.SoHopDong			= @SoHopDong 
 				AND hdct.DmSanPhamREF	= 381 
 				AND hdct.DmLoaiREF		<> 13 -- mua ngoai
 				AND hdct.IsKhuyenMai	= 0
 				--and HopDongChiTietID = 58069-- chu y dang test
 			ORDER BY hdct.HopDongChiTietID

 		OPEN hd_cursor
 		FETCH NEXT FROM hd_cursor INTO @PhanBoId
 		WHILE @@FETCH_STATUS = 0 
 		BEGIN		

 			SELECT	
 					@DonViTinhPhanBo	= DonViTinh,
 					@DonViTinhPhanBoOld = DonViTinh,
 					@DonGiaPhanBo		= DonGia,
 					@ChietKhauPhanBo	= ChietKhau,
 					@SoLuongPhanBoHopDong = ISNULL(SoLuong,0), 
 					@ThanhTienPhanBoHopDong = ISNULL(ThanhTien,0),
 					@DonGiaPhanBo	= ISNULL(hdct.DonGia,0)
 			FROM HopDongChiTiet AS hdct
 			WHERE hdct.HopDongChiTietID = @PhanBoId
 			
 			SET @DonGiaSauCK = @DonGiaPhanBo - (@ChietKhauPhanBo*@DonGiaPhanBo/100)				
 						                         
 			-- Uu tien tinh so luong thuc chay truoc.
 			SET @TypeInsert = 1
				
 			BEGIN
 				IF @DonViTinhPhanBo = 'CPM' 
 					BEGIN
 						SET @SoLuongPhanBoHopDong = @SoLuongPhanBoHopDong*1000  -- 1 CPM = 1000 View
 						SET @DonGiaSauCK = @DonGiaSauCK/1000
 					END
 					
				--***Tuyetnta 					***--
 				IF (@DonViTinhPhanBo <> 'CPC' AND @DonViTinhPhanBo <> 'CPM') 
 					BEGIN 						
 						SET @DonViTinhPhanBo = 'CPC'
 						SET @DonGiaPhanBoOld = @DonGiaPhanBo
 						SET @DonGiaPhanBo = dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381) 						
 						SET @SoLuongPhanBoHopDong = ROUND(@ThanhTienPhanBoHopDong*100/(100-@ChietKhauPhanBo)/@DonGiaPhanBo,0)
 						SET @DonGiaSauCK = @DonGiaPhanBo - (@ChietKhauPhanBo*@DonGiaPhanBo/100)
 					END
 				--PRINT 'SoLuongPhanBoHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBoHopDong);
				--****----
				
 				-- Select so luong thuc chay cua phan bo, thanh tien thuc chay cua phan bo
 				SET @SoLuongThucChayPhanBo = 0;
 				SET @ThanhTienThucChayPhanBo = 0;

 				IF(EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinh AS tcdt WHERE tcdt.HopDongChiTietREF = @PhanBoId))
 				BEGIN
 					SELECT	@SoLuongThucChayPhanBo = ISNULL(sum(SoLuongThucChay),0), 
 							@ThanhTienThucChayPhanBo = ISNULL(sum(ThanhTienSauTrietKhauThucChay),0) + ISNULL(sum(GiaTriThayDoi),0)
 					FROM ThucChayDaTinh AS tcdt
 					WHERE tcdt.HopDongChiTietREF = @PhanBoId 
 						AND tcdt.NgayThucHien <= @NgayThucHien
 				END				
				
				--PRINT 'SoHopDong :' + CONVERT(nvarchar(50),@SoHopDong)
 			--	PRINT 'PhanBoID :' + CONVERT(nvarchar(50),@PhanBoId)
 			--	PRINT 'SoLuongThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayPhanBo);
 			--	PRINT '@DonViTinhPhanBo: ' + CONVERT(NVARCHAR(50), @DonViTinhPhanBo)	
 			--	PRINT '@DonViTinhHD :' + CONVERT(nvarchar(50),@DonViTinhHD)
 			--	PRINT 'SoLuongPhanBoHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBoHopDong);
 			--	PRINT 'WebsiteName :' + CONVERT(nvarchar(50),@DmWebsiteREF)


 				IF(EXISTS(SELECT tcdt.HopDongID FROM ThucChayDaTinh AS tcdt WHERE tcdt.SoHopDong = @SoHopDong AND tcdt.DmSanPhamREF = 381 AND tcdt.HopDongChiTietREF = 0))
 					SET @ExistPhuongPhapSP = 1
 				ELSE
 					SET @ExistPhuongPhapSP = 0

 				PRINT 'ExistPhuongPhapSP: ' + CONVERT(NVARCHAR(50),@ExistPhuongPhapSP)	
 				
 				PRINT '@ThanhTienPhanBoHopDong: ' + CONVERT(NVARCHAR(50),@ThanhTienPhanBoHopDong)			
 				PRINT '@DonGiaPhanBo: ' + CONVERT(NVARCHAR(50),@DonGiaPhanBo)
				PRINT '@SoLuongPhanBoHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBoHopDong)
				PRINT '@SoLuongThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayPhanBo) 
 				
 				IF(@SoLuongPhanBoHopDong > 0 AND @SoLuongThucChayPhanBo < @SoLuongPhanBoHopDong)
 				BEGIN
 					IF @ExistPhuongPhapSP = 0
 					BEGIN
 						PRINT 'SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay)
						PRINT 'DonViTinhPhanBoOld: ' + CONVERT(NVARCHAR(50), @DonViTinhPhanBoOld) 
						IF (@DonViTinhPhanBoOld = 'CPC' OR @DonViTinhPhanBoOld = 'CPM')
							BEGIN
								SET @SoLuongThucChay = ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh(
 									@SoLuongThucChaySP,
 									@SoLuongPhanBoHopDong,
 									@DonViTinhHD, 
 									@NgayThucHien, 
 									@PhanBoId),0)
 								SET @ThanhTienThucChayTruocCK = ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(@SoLuongPhanBoHopDong,@DonViTinhPhanBo,@DonGiaPhanBo,@NgayKyHopDong,@SoLuongThucChay,@SoLuongThucChay,0,@NgayThucHien,@PhanBoId),0)
 								SET @ThanhTienThucChay = @ThanhTienThucChayTruocCK - (@ThanhTienThucChayTruocCK*@ChietKhauPhanBo/100)
 								
 								IF @ThanhTienThucChayPhanBo < @ThanhTienPhanBoHopDong
									BEGIN
										IF @ThanhTienThucChayPhanBo + @ThanhTienThucChay > @ThanhTienPhanBoHopDong
											BEGIN
												SET @ThanhTienThucChay = @ThanhTienPhanBoHopDong - @ThanhTienThucChayPhanBo
												SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK
											END	
										ELSE
											BEGIN
												SET @ThanhTienThucChay = @ThanhTienThucChay
											END

										SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK
									END												
							END
						ELSE -- don vi tinh khac cpc,cpm
							BEGIN									
									SET @SoLuongThucChay = ISNULL(dbo.ThucChay_GetSoLuongThucChay(
 											@SoLuongThucChaySP,
 											@SoLuongPhanBoHopDong,
 											@DonViTinhHD, 
 											@NgayThucHien, 
 											@PhanBoId,
 											@DmwebsiteREF,
 											@DmBannerREF,
 											@DmChienDichREF),0)
 							
								--SET @ThanhTienThucChayTruocCK = @DonGiaPhanBoOld
								SET @ThanhTienThucChay =  @SoLuongThucChay * @DonGiaSauCK
								--@ThanhTienThucChayTruocCK - (@ThanhTienThucChayTruocCK*@ChietKhauPhanBo/100)
								PRINT '---- @ThanhTienThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayPhanBo)
								PRINT '---- @ThanhTienPhanBoHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienPhanBoHopDong)
								IF @ThanhTienThucChayPhanBo < @ThanhTienPhanBoHopDong
									BEGIN
										IF @ThanhTienThucChayPhanBo + @ThanhTienThucChay > @ThanhTienPhanBoHopDong
											BEGIN
												SET @ThanhTienThucChay = @ThanhTienPhanBoHopDong - @ThanhTienThucChayPhanBo												
												SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK												
											END	
										ELSE
											BEGIN
												SET @ThanhTienThucChay = @ThanhTienThucChay
											END
										PRINT '@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay)
										--SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK
									END												
								END												 						
 					END
 					
 					ELSE -- Phuong phap san pham = 1
 						BEGIN -- BAT DAU PHUONG PHAP SAN PHAM 						
 							SET @ThanhTienThucChayHopDong = 0;
 							SET @ThanhTienHopDong = 0;

 							SET @ThanhTienThucChayTruocCK = ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(@SoLuongPhanBoHopDong,@DonViTinhPhanBo,@DonGiaPhanBo,@NgayKyHopDong,@SoLuongThucChaySP,@SoLuongThucChaySP,0,@NgayThucHien,@PhanBoId),0)
 							SET @ThanhTienThucChay = @ThanhTienThucChayTruocCK - (@ThanhTienThucChayTruocCK*@ChietKhauPhanBo/100)					

 							-- SELECT THANH TIEN HOP DONG
 							SELECT @ThanhTienHopDong = SUM(ThanhTien)
 							FROM HopDong AS hd INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
 							WHERE hd.SoHopDong = @SoHopDong AND hdct.DmSanPhamREF = 381 AND hdct.IsKhuyenMai = 0

 							-- SELECT THANH TIEN THUC CHAY THEO HOP DONG
 							SELECT @ThanhTienThucChayHopDong = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
 							FROM ThucChayDaTinh AS tcdt
 							WHERE tcdt.SoHopDong = @SoHopDong AND tcdt.DmSanPhamREF = 381 AND tcdt.NgayThucHien <= @NgayThucHien

 							--PRINT '---- @ThanhTienThucChayHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayHopDong)
 							--PRINT '---- @ThanhTienHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienHopDong)

 							IF @ThanhTienThucChayHopDong < @ThanhTienHopDong 
 								BEGIN
 									IF @ThanhTienThucChayHopDong + @ThanhTienThucChay > @ThanhTienHopDong
 										BEGIN
 											SET @ThanhTienThucChay = @ThanhTienHopDong - @ThanhTienThucChayHopDong;
 										END							
 									ELSE
 										BEGIN
 											SET @ThanhTienThucChay = @ThanhTienThucChay
 										END

 									SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK
 								END
 							END -- KET THUC PHUONG PHAP SAN PHAM = 1
 					
 					IF @SoLuongThucChay > 0
 					BEGIN
 						PRINT 'Insert ThucChay'; 	 
 						PRINT '---- @SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay)
 						PRINT '---- @@TongClickThucChay: ' + CONVERT(NVARCHAR(50), @TongClickThucChay)	 							
 						EXEC dbo.[ThucChayDaTinh_InsertThucChayDaTinh_SponsorBySoHopDongWebsite]
 							@NgayThucHien,
 							@SoHopDong,
 							@PhanBoId,
 							'CLICK',--@DonViTinhHD,
 							@DmWebsiteREF,
 							@TenWebsite,
 							@DmChienDichREF,
 							@DmBannerREF,
 							@TongViewThucChay,
 							@TongClickThucChay,
 							@SoLuongThucChay, 							
 							@DonGiaPhanBo,--@DonGiaTheoDonViTinhSP,
 							@ThanhTienThucChayTruocCK,
 							@SoLuongThucChayKM,
 							@ThanhTienThucChayKM,
 							@SoLuongLechTreoHa,
 							@ThanhTienLechTreoHa,
 							@TypeInsert
 					END
 					SET @SoLuongThucChaySP = @SoLuongThucChaySP - @SoLuongThucChay;
 					PRINT '@SoLuongThucChaySP: ' + CONVERT(NVARCHAR(50),@SoLuongThucChaySP)
 				END
 			END 			
 			FETCH NEXT FROM hd_cursor INTO @PhanBoId
 		END
 		PRINT '---- SoLuongThucChay - con lai: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySP)
 		CLOSE hd_cursor;
 		DEALLOCATE hd_cursor;

 		-- Neu so luong thuc chay con lai van > 0 sau khi tinh cho cac phan bo trong hop dong
 		IF @SoLuongThucChaySP > 0 
 		BEGIN
 			PRINT '---- Bat dau tinh Khuyen Mai: '
 			DECLARE @SoLuongKhuyenMaiPhanBo		INT = 0,
 					@SoLuongThucChayKMPhanBo	INT = 0

 			SET @TypeInsert = 2		
 			SET @SoLuongThucChay = 0;
 			SET @ThanhTienThucChay = 0;
 			SET @SoLuongLechTreoHa = 0;
 			SET @ThanhTienLechTreoHa = 0;

 			DECLARE km_cursor CURSOR FOR
 			SELECT hdct.HopDongChiTietID
 			FROM HopDong AS hd 
 				INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
 			WHERE
 				hd.SoHopDong			= @SoHopDong 
 				AND hdct.DmSanPhamREF	= 381 
 				AND hdct.DmLoaiREF		<> 13 -- Mua ngoai 
 				AND hdct.IsKhuyenMai	= 1
 			ORDER BY hdct.HopDongChiTietID 

 			OPEN km_cursor 
 			FETCH NEXT FROM km_cursor INTO @PhanBoId
 			WHILE @@FETCH_STATUS = 0
 			BEGIN				
 				SET @DonViTinhPhanBo = (
 											SELECT DonViTinh 
 											FROM HopDongChiTiet AS hdct 
 											WHERE hdct.HopDongChiTietID = @PhanBoId
 										)

 				SELECT 
 					@SoLuongKhuyenMaiPhanBo		= ISNULL(SoLuong,0), 
 					@ThanhTienKhuyenMaiPhanBo	= ISNULL(hdct.SoLuong*hdct.DonGia,0)
 				FROM HopDongChiTiet AS hdct
 				WHERE hdct.HopDongChiTietID = @PhanBoId

 				IF @DonViTinhPhanBo = 'CPM'
 					SET @SoLuongKhuyenMaiPhanBo = @SoLuongKhuyenMaiPhanBo*1000 -- 1 CPM = 1000 View

 				IF(EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinh AS tcdt WHERE tcdt.HopDongChiTietREF = @PhanBoId))
 				BEGIN
 					SELECT 
 						@SoLuongThucChayKMPhanBo	= SUM(ISNULL(SoLuongThucChayKM,0)), 
 						@ThanhTienThucChayPhanBoKM	= SUM(ISNULL(ThanhTienKM,0))
 					FROM ThucChayDaTinh AS tcdt
 					WHERE tcdt.HopDongChiTietREF = @PhanBoId AND tcdt.NgayThucHien <= @NgayThucHien
 				END

 				IF (@DonViTinhPhanBo = 'CPM' OR @DonViTinhPhanBo = 'CPC')
 				BEGIN
 					PRINT 'SoLuongKhuyenMaiPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongKhuyenMaiPhanBo);
 					PRINT 'SoLuongThucChayKMPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKMPhanBo);

 					IF @SoLuongKhuyenMaiPhanBo > @SoLuongThucChayKMPhanBo
 					BEGIN
 						PRINT 'Insert ThucChayKhuyenMai';

 						SET @SoLuongThucChayKM = ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh(@SoLuongThucChaySP,@SoLuongKhuyenMaiPhanBo,@DonViTinhHD, @NgayThucHien, @PhanBoId),0)

 						PRINT 'SoLuongThucChayKM: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKM);
 						PRINT 'TypeInsert: ' + CONVERT(NVARCHAR(50),@TypeInsert);

 						EXEC dbo.[ThucChayDaTinh_InsertThucChayDaTinh_SponsorBySoHopDongWebsite]
 							@NgayThucHien,
 							@SoHopDong,
 							@PhanBoId,
 							'CLICK',--@DonViTinhHD,
 							@DmWebsiteREF,
 							@TenWebsite,
 							@DmChienDichREF,
 							@DmBannerREF,
 							@TongViewThucChay,
 							@TongClickThucChay,
 							@SoLuongThucChay,
 							@DonGiaPhanBo,--@DonGiaTheoDonViTinhSP,
 							@ThanhTienThucChayTruocCK,
 							@SoLuongThucChayKM,
 							@ThanhTienThucChayKM,
 							@SoLuongLechTreoHa,
 							@ThanhTienLechTreoHa,
 							@TypeInsert

 						SET @SoLuongThucChaySP = @SoLuongThucChaySP - @SoLuongThucChayKM;
 					END
 				END
 				ELSE
 				BEGIN
 					PRINT 'ThanhTienKhuyenMaiPhanBo: ' + CONVERT(NVARCHAR(50),@ThanhTienKhuyenMaiPhanBo);
 					PRINT 'ThanhTienThucChayKMPhanBo: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChayPhanBoKM);
 					PRINT 'TypeInsert: ' + CONVERT(NVARCHAR(50),@TypeInsert);
 					IF @ThanhTienThucChayPhanBoKM < @ThanhTienKhuyenMaiPhanBo 
 					BEGIN
 						IF @ThanhTienThucChayPhanBoKM + @ThanhTienThucChaySanPham > @ThanhTienKhuyenMaiPhanBo
 							SET @ThanhTienThucChayKM = @ThanhTienThucChayPhanBo - @ThanhTienThucChaySanPham
 						ELSE	
 							SET @ThanhTienThucChayKM = @ThanhTienThucChaySanPham

 						SET @SoLuongThucChayKM = @ThanhTienThucChayKM/@DonGiaSanPham;

 						IF @ThanhTienThucChayKM > 0
 						BEGIN
 							PRINT 'TypeInsert: ' + CONVERT(NVARCHAR(50),@TypeInsert);
 							EXEC dbo.[ThucChayDaTinh_InsertThucChayDaTinh_SponsorBySoHopDongWebsite]
 								@NgayThucHien,
 							@SoHopDong,
 							@PhanBoId,
 							'CLICK',--@DonViTinhHD,
 							@DmWebsiteREF,
 							@TenWebsite,
 							@DmChienDichREF,
 							@DmBannerREF,
 							@TongViewThucChay,
 							@TongClickThucChay,
 							@SoLuongThucChay,
 							@DonGiaPhanBo,--@DonGiaTheoDonViTinhSP,
 							@ThanhTienThucChayTruocCK,
 							@SoLuongThucChayKM,
 							@ThanhTienThucChayKM,
 							@SoLuongLechTreoHa,
 							@ThanhTienLechTreoHa,
 							@TypeInsert

 							SET @ThanhTienThucChaySanPham = @ThanhTienThucChaySanPham - @ThanhTienThucChayKM;
 							SET @SoLuongThucChaySP = @SoLuongThucChaySP - @SoLuongThucChayKM
 						END
 					END
 				END

 				FETCH NEXT FROM km_cursor INTO @PhanBoId
 			END
 			CLOSE km_cursor;
 			DEALLOCATE km_cursor;
 		END

 		-- Neu so luong thuc chay con lai van > 0 sau khi tinh cho cac phan bo trong hop dong thi se insert vao gia tri lech treo ha
 		IF @SoLuongThucChaySP > 0 
 		BEGIN 		
 			SET @TypeInsert = 3
 			SET @PhanBoId = (SELECT TOP 1 hdct.HopDongChiTietID
 								FROM HopDong AS hd 
 									INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
 								WHERE
 									hd.SoHopDong			= @SoHopDong 
 									AND hdct.DmSanPhamREF	= 381 
 									AND hdct.DmLoaiREF		<> 13 
 									AND hdct.IsKhuyenMai	= 0
 								ORDER BY hdct.HopDongChiTietID DESC
 							)   

 			SET @SoLuongLechTreoHa = 0
 			SET @SoLuongThucChayKM = 0				
 			SET @SoLuongLechTreoHa = @SoLuongThucChaySP

 			PRINT 'Insert ThucChayLechTreoHa';
		
 			EXEC dbo.[ThucChayDaTinh_InsertThucChayDaTinh_SponsorBySoHopDongWebsite]
 							@NgayThucHien,
 							@SoHopDong,
 							@PhanBoId,
 							'CLICK',--@DonViTinhHD,
 							@DmWebsiteREF,
 							@TenWebsite,
 							@DmChienDichREF,
 							@DmBannerREF,
 							@TongViewThucChay,
 							@TongClickThucChay, 
 							@SoLuongThucChay,
 							@DonGiaPhanBo,--@DonGiaTheoDonViTinhSP,
 							@ThanhTienThucChayTruocCK,
 							@SoLuongThucChayKM,
 							@ThanhTienThucChayKM,
 							@SoLuongLechTreoHa,
 							@ThanhTienLechTreoHa,
 							@TypeInsert

 		END
 		END
 		
 END


```
