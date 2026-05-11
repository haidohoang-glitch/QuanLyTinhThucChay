# Stored Procedure: `ThucChay_ReInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_ByHopDongChiTiet_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-06-10 14:30:38.753000
- **Ngày sửa cuối**: 2021-07-15 16:21:40.280000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayThucHienGhiNhan` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_ReInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_ByHopDongChiTiet_dev]
	'qc2370221',
	611968,
	598,
	'2021-07-14'
*/
CREATE PROCEDURE [dbo].[ThucChay_ReInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_ByHopDongChiTiet_dev] 
	@pSoHopDong NVARCHAR(100),
	@pHopDongChiTietID INT,
	@DmSanPhamREF INT,
	@NgayThucHienGhiNhan DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME,@StartDate DATETIME,	@EndDate DATETIME
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @HopDongChiTietID INT, @TypeProduct INT, @TiLeBannerSiteHDCT FLOAT = 0
	, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT, @TongViewThucChayBanner BIGINT, @TongClickThucChayBanner BIGINT
	, @TenWebsite_HDCN NVARCHAR(200)

	DECLARE @ThucChayHopDong TABLE( SoHopDong NVARCHAR(200) NOT NULL, HopDongID INT NOT NULL, HopDongChiTietID INT NOT NULL, TypeProduct INT NOT NULL, DmWebsiteREF INT NOT NULL, 
									TenWebsite NVARCHAR(500) NOT NULL, DmBannerREF INT NOT NULL, TongViewThucChayBanner BIGINT NOT NULL, TongClickThucChayBanner BIGINT NOT NULL)
	
	SET @SoHopDong = @pSoHopDong
	SET @HopDongChiTietID = @pHopDongChiTietID

	SELECT @StartDate = MIN(NgayThucHien), @EndDate = MAX(NgayThucHien) FROM dbo.ThucChay
	WHERE SoHopDong = @pSoHopDong
	AND TypeProduct = [dbo].[GetDmSanPhamIDByTypeProductID](@DmSanPhamREF)


	SET @StartDate = ISNULL(@StartDate,@NgayThucHienGhiNhan)
	SET @EndDate = ISNULL(@EndDate, @NgayThucHienGhiNhan)

	DELETE from dbo.ThucChayTemp
	WHERE NgayThucHien BETWEEN @StartDate AND @EndDate

	SET @NgayThucHien = @StartDate
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		--PRINT @NgayThucHien
		INSERT INTO dbo.ThucChayTemp
		        ( ThucChayID ,SoHopDong ,DanhsachDmBookingREF ,DmSanPhamREF ,
		          TenSanPham ,DmNhomWebsiteREF ,TenNhomWebsite ,DmWebsiteREF ,
		          TenWebsite ,DmChienDichREF ,TenChienDich ,DmBannerREF ,
		          TenBanner ,NgayThucHien ,TongViewThucChay ,TongClickThucChay ,
		          CreatedBy ,CreatedAt ,LastModifiedBy ,LastModifiedAt ,
		          DeletedStatus ,PrintStatus ,RecordStatus ,TongSoBaiViet ,
		          SoThuTuTheoNgay ,TypeProduct ,BannerType ,UserName ,
		          SaleName ,Email ,LastTimeCalc ,sys_date ,
		          IsReady ,ProductUnitID ,ProductUnitName ,BannerTypeName ,
		          HopDongChiTietREF ,CampainStatus ,BannerStatus ,IsNoiBo
		        )
	
		select  ThucChayID ,SoHopDong ,DanhsachDmBookingREF ,DmSanPhamREF ,
		          TenSanPham ,DmNhomWebsiteREF ,TenNhomWebsite ,DmWebsiteREF ,
		          TenWebsite ,DmChienDichREF ,TenChienDich ,DmBannerREF ,
		          TenBanner ,NgayThucHien ,TongViewThucChay ,TongClickThucChay ,
		          CreatedBy ,CreatedAt ,LastModifiedBy ,LastModifiedAt ,
		          DeletedStatus ,PrintStatus ,RecordStatus ,TongSoBaiViet ,
		          SoThuTuTheoNgay ,TypeProduct ,BannerType ,UserName ,
		          SaleName ,Email ,LastTimeCalc ,sys_date ,
		          IsReady ,ProductUnitID ,ProductUnitName ,BannerTypeName ,
		          HopDongChiTietREF ,CampainStatus ,BannerStatus ,IsNoiBo 
				  FROM dbo.ThucChay 
		WHERE CONVERT(DATE,NgayThucHien) = CONVERT(DATE,@NgayThucHien)
		AND TypeProduct NOT IN (1,2,17, -3)
		AND DmWebsiteREF <> 0
		AND SoHopDong = @pSoHopDong

		INSERT INTO @ThucChayHopDong
		(
		    SoHopDong,
			HopDongID,
		    HopDongChiTietID,
		    TypeProduct,
		    DmWebsiteREF,
		    TenWebsite,
		    DmBannerREF,
			TongViewThucChayBanner,
			TongClickThucChayBanner
		)

		SELECT A.SoHopDong, A.HopDongID, A.HopDongChiTietID, A.TypeProduct, A.DmWebsiteREF
			, A.TenWebsite, A.DmBannerREF , SUM(A.TongViewThucChay)TongViewThucChay
			, SUM(A.TongClickThucChay)TongClickThucChay
		  FROM
			(
				SELECT tct.SoHopDong, hd.HopDongID, hd.HopDongChiTietID,tct.TypeProduct, tct.DmWebsiteREF, tct.TenWebsite, tct.DmBannerREF
				, (tct.TongViewThucChay*hd.TiLeThucChayHDCTSoVoiBanner)/100 AS TongViewThucChay --THUC HIEN TINH TI LE THUC CHAY CUA TUNG BANNER UNG VOI HDCT
				, (tct.TongClickThucChay*hd.TiLeThucChayHDCTSoVoiBanner)/100 AS TongClickThucChay --THUC HIEN TINH TI LE THUC CHAY CUA TUNG BANNER UNG VOI HDCT
				FROM (SELECT * FROM  dbo.ThucChayTemp 
					WHERE 1=1
					AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
					AND TypeProduct NOT IN (1,2,17, -3)
					AND DmWebsiteREF <> 0
				) tct
				INNER JOIN 
				(SELECT hd.SoHopDong, hd.HopDongID, hdct.HopDongChiTietID
					, b.DmBannerID
					, b.TiLeThucChayHDCTSoVoiBanner
					FROM (SELECT * FROM dbo.HopDong WHERE SoHopDong = @pSoHopDong) hd
					INNER JOIN 
					(
						SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.DmNhomWebsiteREF, hdct.DmWebsiteREF, hdct.TenWebsite  
						FROM dbo.HopDongChiTiet hdct 
						WHERE hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342)
						AND hdct.DonViTinhREF in(3,4)--DON VI TINH LA NGAY
						AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
						AND hdct.HopDongChiTietID = @pHopDongChiTietID
					)hdct ON hd.HopDongID = hdct.HopDongFK
					INNER JOIN dbo.ThucChayHopDongChiTietAndBanner b ON hdct.HopDongChiTietID = b.HopDongChiTietREF
				)hd ON hd.SoHopDong = tct.SoHopDong AND CONVERT(NVARCHAR(100),tct.DmBannerREF) = hd.DmBannerID
			)A
			WHERE a.HopDongID = 1030593
			AND A.HopDongChiTietID = 611968
			
			GROUP BY A.SoHopDong, A.HopDongID, A.HopDongChiTietID, A.TypeProduct, A.DmWebsiteREF, A.TenWebsite, A.DmBannerREF 

		DECLARE Record_Cursor_DonViTinh CURSOR FOR 
		--DANH SACH CAC HOP DONG CO PHAT SINH THUC CHAY CUNG SITE VOI HOP DONG KY CHAY THEO NGAY THEO BANNER TREO
		SELECT  SoHopDong, HopDongID,HopDongChiTietID,TypeProduct,DmWebsiteREF,TenWebsite,DmBannerREF, TongViewThucChayBanner, TongClickThucChayBanner
		FROM @ThucChayHopDong
		ORDER BY SoHopDong, TypeProduct	

		OPEN Record_Cursor_DonViTinh

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor_DonViTinh INTO @SoHopDong, @HopDongID, @HopDongChiTietID, @TypeProduct, @DmWebsiteREF
											, @TenWebsite, @DmBannerREF, @TongViewThucChayBanner, @TongClickThucChayBanner
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				-- PRINT 'Tinh thuc chay cho san pham CPM theo ngay'
				

				 DECLARE @soluongthucchayhdct INT = 0, @ThanhTien BIGINT =0
				 IF(EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
							WHERE HopDongChiTietID = @HopDongChiTietID 
							AND DmWebsiteREF <> 265 --Khong phai la website (Blanks)
							AND dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(DmWebsiteREF) = @DmWebsiteREF
					))
					BEGIN
						SET @TenWebsite_HDCN = ISNULL((SELECT dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) 
												FROM dbo.HopDongChiTiet C
												WHERE C.HopDongChiTietID = @HopDongChiTietID),'')
						-- CHECK DOMAIN THUC CHAY VA DOMAIN HOPDONGCHITIET LA CUNG SITE	
						IF(EXISTS(SELECT TOP (1) DmWebsiteReportingdbID
							FROM dbo.DmWebsiteReportingdb
							WHERE (TenWebsite LIKE @TenWebsite + '%' OR TenWebsite LIKE '%.' +  @TenWebsite)
							AND (TenWebsite LIKE @TenWebsite_HDCN + '%' OR TenWebsite LIKE '%.' +  @TenWebsite_HDCN)
							ORDER BY DmWebsiteReportingdbID)
							)
							BEGIN
								SET @soluongthucchayhdct = ISNULL((SELECT SUM(TC.TongViewThucChayBanner) 
															FROM @ThucChayHopDong TC
															WHERE SoHopDong = @SoHopDong 
															AND TC.HopDongChiTietID = @HopDongChiTietID
															AND (
																	(TC.TenWebsite LIKE @TenWebsite + '%' OR TC.TenWebsite LIKE '%.' +  @TenWebsite)
																	OR (TC.TenWebsite LIKE @TenWebsite_HDCN + '%' OR TC.TenWebsite LIKE '%.' +  @TenWebsite_HDCN)
																)
															AND TC.TypeProduct = @TypeProduct),0)
								IF(@soluongthucchayhdct <> 0)
									SET @TiLeBannerSiteHDCT = CONVERT(FLOAT,@TongViewThucChayBanner)/CONVERT(FLOAT,@soluongthucchayhdct)
								ELSE SET @TiLeBannerSiteHDCT = 1

								 PRINT CONVERT(NVARCHAR(100),@TongViewThucChayBanner)
								 PRINT @TenWebsite
								 PRINT CONVERT(NVARCHAR(102),@NgayThucHien,130)
								 PRINT CONVERT(NVARCHAR(100),@TiLeBannerSiteHDCT)

								 --EXEC [dbo].[ThucChay_UpdateGiaTriThayDoiCPM_With_DonViTinh_Ngay_Site] @NgayThucHien = @NgayThucHienGhiNhan,
									--																@SoHopDong = @SoHopDong,
									--																@HopDongChiTietID = @HopDongChiTietID,
									--																@TypeProduct = @TypeProduct,
									--																@DmWebsiteREF = @DmWebsiteREF, 
									--																@TenWebsite = @TenWebsite,
									--																@DmBannerREF = @DmBannerREF,
									--																@TiLeBannerSiteHDCT = @TiLeBannerSiteHDCT,
									--																@TongViewThucChayBanner = @TongViewThucChayBanner, 
									--																@TongClickThucChayBanner = @TongClickThucChayBanner
							END
					END
					 --TINH TI LE THUC CHAY THEO BANNER CHIEM TRONG HDCT
				ELSE
					BEGIN
						IF(EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
							WHERE HopDongChiTietID = @HopDongChiTietID 
							AND DmWebsiteREF = 265 --Khong phai la website (Blanks)
							))
							BEGIN
							    SET @soluongthucchayhdct = ISNULL((SELECT SUM(TC.TongViewThucChayBanner) 
													FROM @ThucChayHopDong TC
													WHERE SoHopDong = @SoHopDong 
													AND TC.HopDongChiTietID = @HopDongChiTietID
													AND TC.TypeProduct = @TypeProduct),0)
								IF(@soluongthucchayhdct <> 0)
									SET @TiLeBannerSiteHDCT = CONVERT(FLOAT,@TongViewThucChayBanner)/CONVERT(FLOAT,@soluongthucchayhdct)
								ELSE SET @TiLeBannerSiteHDCT = 1
								 PRINT CONVERT(NVARCHAR(100),@TongViewThucChayBanner)
								 PRINT @TenWebsite
								 PRINT CONVERT(NVARCHAR(102),@NgayThucHien)
								 PRINT @TiLeBannerSiteHDCT
								 --EXEC [dbo].[ThucChay_UpdateGiaTriThayDoiCPM_With_DonViTinh_Ngay_Site] @NgayThucHien = @NgayThucHienGhiNhan,
									--																@SoHopDong = @SoHopDong,
									--																@HopDongChiTietID = @HopDongChiTietID,
									--																@TypeProduct = @TypeProduct,
									--																@DmWebsiteREF = @DmWebsiteREF, 
									--																@TenWebsite = @TenWebsite,
									--																@DmBannerREF = @DmBannerREF,
									--																@TiLeBannerSiteHDCT = @TiLeBannerSiteHDCT,
									--																@TongViewThucChayBanner = @TongViewThucChayBanner, 
									--																@TongClickThucChayBanner = @TongClickThucChayBanner
							END
						
					END
				
				
				----XAC DINH NGAY PHAT SINH GIA TRI LECH TREO HA MA THIEU TIEN THUC CHAY
				--IF(EXISTS(SELECT TOP (1)  NgayThucHien, ThucChayDaTinhID FROM dbo.ThucChayDaTinh
				--		WHERE HopDongChiTietREF = @HopDongChiTietID
				--		AND SoLuongThucChayLechTreoHa <> 0
				--		AND NgayThucHien = @NgayThucHienGhiNhan
				--		AND ChietKhau <> 100
				--		AND DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342)
				--		AND DonViTinh = N'VIEW'
				--		AND SoHopDong = @SoHopDong
				--		AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
				--		AND DotChayHopDong = N'NGAY'  --HAIDH COMMENT Day la thong tin the hien tinh thuc chay san pham CPM theo ngay 
				--))
				--BEGIN
				--	SET @ThanhTien = (SELECT TOP (1) ThanhTien FROM dbo.HopDongChiTiet
				--					WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)

				--	EXEC [dbo].[ThucChay_Update_ThucChayCPM_With_DonViTinh_Ngay_FixBug_KetThucChay] @NgayThucHien = @NgayThucHienGhiNhan,
				--																					@HopDongID = @HopDongID, 
				--																					@HopDongChiTietID = @HopDongChiTietID,
				--																					@ThanhTienHDCT = @ThanhTien	    
				--END
				FETCH NEXT FROM Record_Cursor_DonViTinh INTO  @SoHopDong, @HopDongID, @HopDongChiTietID, @TypeProduct, @DmWebsiteREF
											, @TenWebsite, @DmBannerREF, @TongViewThucChayBanner, @TongClickThucChayBanner
			END

		CLOSE Record_Cursor_DonViTinh
		DEALLOCATE Record_Cursor_DonViTinh
		
		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		DELETE FROM dbo.ThucChayTemp
		WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
		DELETE FROM @ThucChayHopDong
		
	END 
	
	SELECT '1'
END


```
