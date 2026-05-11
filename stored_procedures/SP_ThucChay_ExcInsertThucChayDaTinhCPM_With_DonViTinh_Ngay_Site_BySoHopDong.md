# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-02-24 11:13:24.997000
- **Ngày sửa cuối**: 2021-03-18 16:15:54.570000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@NgayThucHienGhiNhan` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [ThucChay_ExcInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site_BySoHopDong] 'QC5580619', '2019-06-26', '2019-08-02', '2019-08-29'
*/
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site_BySoHopDong] 
	@pSoHopDong NVARCHAR(100),
	@StartDate datetime,
	@EndDate DATETIME,
	@NgayThucHienGhiNhan DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @HopDongChiTietID INT, @TypeProduct INT, @TiLeBannerSiteHDCT FLOAT = 0
	, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT, @TongViewThucChayBanner BIGINT, @TongClickThucChayBanner BIGINT
	SET @NgayThucHien = @StartDate
	DECLARE @ThucChayHopDong TABLE( SoHopDong NVARCHAR(200) NOT NULL, HopDongID INT NOT NULL, HopDongChiTietID INT NOT NULL, TypeProduct INT NOT NULL, DmWebsiteREF INT NOT NULL, 
									TenWebsite NVARCHAR(500) NOT NULL, DmBannerREF INT NOT NULL, TongViewThucChayBanner BIGINT NOT NULL, TongClickThucChayBanner BIGINT NOT NULL)
	DELETE from dbo.ThucChayTemp
	WHERE NgayThucHien BETWEEN @StartDate AND @EndDate

	--XOA DU LIEU THUC CHAY TRUOC KHI TINH
	DELETE FROM dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien) = @NgayThucHienGhiNhan
	AND DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342,821)
	AND DonViTinh = N'VIEW'
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
	AND DotChayHopDong = N'NGAY'  --HAIDH COMMENT Day la thong tin the hien tinh thuc chay san pham CPM theo ngay
	AND SoHopDong = @pSoHopDong 
	

	--AND DotChayBooking <> N'(Blanks)' --Khong phai chay theo nhieu site
	--AND SoLuongDotChayBooking <> 265 --Khong phai la website (Blanks)


	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		DELETE from dbo.ThucChayTemp
		WHERE NgayThucHien BETWEEN @StartDate AND @EndDate

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
		WHERE CONVERT(DATE,NgayThucHien) = @NgayThucHien
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
						WHERE hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342,821)
						AND hdct.DonViTinhREF IN (3,4) --DON VI TINH LA NGAY
						AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
					)hdct ON hd.HopDongID = hdct.HopDongFK
					INNER JOIN dbo.ThucChayHopDongChiTietAndBanner b ON hdct.HopDongChiTietID = b.HopDongChiTietREF
				)hd ON hd.SoHopDong = tct.SoHopDong AND CONVERT(NVARCHAR(100),tct.DmBannerREF) = hd.DmBannerID
			)A
			--WHERE A.HopDongChiTietID = 528581
			GROUP BY A.SoHopDong, A.HopDongID, A.HopDongChiTietID, A.TypeProduct, A.DmWebsiteREF, A.TenWebsite, A.DmBannerREF 

		SELECT * FROM @ThucChayHopDong

		DECLARE Record_Cursor CURSOR FOR 
		--DANH SACH CAC HOP DONG CO PHAT SINH THUC CHAY CUNG SITE VOI HOP DONG KY CHAY THEO NGAY THEO BANNER TREO
		SELECT  SoHopDong, HopDongID,HopDongChiTietID,TypeProduct,DmWebsiteREF,TenWebsite,DmBannerREF, TongViewThucChayBanner, TongClickThucChayBanner
		FROM @ThucChayHopDong
		ORDER BY SoHopDong, TypeProduct	

		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @HopDongID, @HopDongChiTietID, @TypeProduct, @DmWebsiteREF
											, @TenWebsite, @DmBannerREF, @TongViewThucChayBanner, @TongClickThucChayBanner
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				 --PRINT 'Tinh thuc chay cho san pham CPM theo ngay'
				 --PRINT CONVERT(NVARCHAR(100), @HopDongChiTietID)
				 DECLARE @TenWebsite_HDCN NVARCHAR(300) =''
				 DECLARE @soluongthucchayhdct INT = 0, @ThanhTien BIGINT =0
				 IF(EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
							WHERE HopDongChiTietID = @HopDongChiTietID 
							AND DmWebsiteREF <> 265 --Khong phai la website (Blanks)
							--AND dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(DmWebsiteREF) = @DmWebsiteREF
					))
					BEGIN
						SET @TenWebsite_HDCN = ISNULL((SELECT dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) 
												FROM dbo.HopDongChiTiet C
												WHERE C.HopDongChiTietID = @HopDongChiTietID),'')
						PRINT CONVERT(NVARCHAR(100), @HopDongChiTietID)
						PRINT @TenWebsite_HDCN
						PRINT @TenWebsite
						-- CHECK DOMAIN THUC CHAY VA DOMAIN HOPDONGCHITIET LA CUNG SITE	
						IF(EXISTS(SELECT TOP (1) DmWebsiteReportingdbID
							FROM dbo.DmWebsiteReportingdb
							WHERE (TenWebsite LIKE @TenWebsite + '%' OR TenWebsite LIKE '%.' +  @TenWebsite)
							AND (TenWebsite LIKE @TenWebsite_HDCN + '%' OR TenWebsite LIKE '%.' +  @TenWebsite_HDCN)
							ORDER BY DmWebsiteReportingdbID)
							)
							BEGIN
							--print 'khong phai wbeiste bkl'
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
								 --PRINT CONVERT(NVARCHAR(100),@TiLeBannerSiteHDCT)
								 --PRINT CONVERT(NVARCHAR(100),@TongViewThucChayBanner)
								 --PRINT @soluongthucchayhdct
								 --PRINT @TenWebsite
								 --PRINT CONVERT(NVARCHAR(102),@DmWebsiteREF)
								 EXEC [dbo].[ThucChay_InsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site] @NgayThucHien = @NgayThucHienGhiNhan,
																									@SoHopDong = @SoHopDong,
																									@HopDongChiTietID = @HopDongChiTietID,
																									@TypeProduct = @TypeProduct,
																									@DmWebsiteREF = @DmWebsiteREF, 
																									@TenWebsite = @TenWebsite,
																									@DmBannerREF = @DmBannerREF,
																									@TiLeBannerSiteHDCT = @TiLeBannerSiteHDCT,
																									@TongViewThucChayBanner = @TongViewThucChayBanner, 
																									@TongClickThucChayBanner = @TongClickThucChayBanner
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
							--print'native_ads'
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
								 EXEC [dbo].[ThucChay_InsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site] @NgayThucHien = @NgayThucHienGhiNhan,
																									@SoHopDong = @SoHopDong,
																									@HopDongChiTietID = @HopDongChiTietID,
																									@TypeProduct = @TypeProduct,
																									@DmWebsiteREF = @DmWebsiteREF, 
																									@TenWebsite = @TenWebsite,
																									@DmBannerREF = @DmBannerREF,
																									@TiLeBannerSiteHDCT = @TiLeBannerSiteHDCT,
																									@TongViewThucChayBanner = @TongViewThucChayBanner, 
																									@TongClickThucChayBanner = @TongClickThucChayBanner
							END
						
					END
				
				
				--XAC DINH NGAY PHAT SINH GIA TRI LECH TREO HA MA THIEU TIEN THUC CHAY
				IF(EXISTS(SELECT TOP (1)  NgayThucHien, ThucChayDaTinhID FROM dbo.ThucChayDaTinh
						WHERE HopDongChiTietREF = @HopDongChiTietID
						AND SoLuongThucChayLechTreoHa <> 0
						AND NgayThucHien = @NgayThucHienGhiNhan
						AND ChietKhau <> 100
						AND DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342,821)
						AND DonViTinh = N'VIEW'
						AND SoHopDong = @SoHopDong
						AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
						AND DotChayHopDong = N'NGAY'  --HAIDH COMMENT Day la thong tin the hien tinh thuc chay san pham CPM theo ngay 
				))
				BEGIN
					SET @ThanhTien = (SELECT TOP (1) ThanhTien FROM dbo.HopDongChiTiet
									WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)

					EXEC [dbo].[ThucChay_Update_ThucChayCPM_With_DonViTinh_Ngay_FixBug_KetThucChay] @NgayThucHien = @NgayThucHienGhiNhan,
																									@HopDongID = @HopDongID, 
																									@HopDongChiTietID = @HopDongChiTietID,
																									@ThanhTienHDCT = @ThanhTien	    
				END
				FETCH NEXT FROM Record_Cursor INTO  @SoHopDong, @HopDongID, @HopDongChiTietID, @TypeProduct, @DmWebsiteREF
											, @TenWebsite, @DmBannerREF, @TongViewThucChayBanner, @TongClickThucChayBanner
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		DELETE FROM dbo.ThucChayTemp
		WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
		DELETE FROM @ThucChayHopDong
		
	END 
	
	SELECT '1'
END


```
