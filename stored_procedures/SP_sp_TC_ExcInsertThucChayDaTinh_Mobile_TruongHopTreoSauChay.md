# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_Mobile_TruongHopTreoSauChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-24 11:06:36.573000
- **Ngày sửa cuối**: 2017-12-09 10:25:34.010000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pDmBannerID` | `int(4)` | No |
| `@pNgayTinh` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--ThucChay_ExcInsertThucChayDaTinhMobile_v4_BySoHopDong '2015-07-15','2015-07-15','QC180615'
--exec [sp_TC_ExcInsertThucChayDaTinh_Mobile] '2017-03-29','2017-03-29'
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_Mobile_TruongHopTreoSauChay]--tinh ca truong hop 1 phan bo nhieu banner
	-- Add the parameters for the stored procedure here
    @StartDate DATETIME ,
    @EndDate DATETIME,
	@pSoHopDong NVARCHAR(50) = NULL,
	@pDmBannerID INT ,
	@pNgayTinh DATETIME
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME ,
            @SoHopDong NVARCHAR(50) ,
            @HopDongChiTietREF INT ,
            @DmBannerREF INT ,
            @DmWebsiteREF INT ,
            @TH INT
	
        SET @NgayThucHien = @StartDate
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
		


		-----------------------------------------------------------------------------------




		  DECLARE @ThucChayHopDongChiTiet_Temp TABLE
                    (
                      SoHopDong NVARCHAR(50) ,
                      DmBannerREF NVARCHAR(50) ,
                      IsKhuyenMai INT ,
                      HopDongChiTietID INT ,
                      HopDongID INT
                    )

                INSERT  INTO @ThucChayHopDongChiTiet_Temp
                        SELECT  hd.SoHopDong ,
                                tc.DmBannerID ,
                                hdct.IsKhuyenMai ,
                                hdct.HopDongChiTietID ,
                                hd.HopDongID
                        FROM    ThucChayHopDongChiTietAndBanner tc
                                INNER JOIN HopDongChiTiet hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
                                INNER JOIN HopDong hd ON tc.HopDongREF = hd.HopDongID
						WHERE CONVERT(DATE, tc.CreatedAt) = @NgayThucHien
                                AND CONVERT(DATE, tc.CreatedAt) > CONVERT(DATE, tc.ThoiGianBatDau)
                                AND tc.DeletedStatus = 0
								AND ( @pSoHopDong IS NULL
									  OR hd.SoHopDong = @pSoHopDong
									)
								AND tc.DmBannerID = @pDmBannerID









		--Insert vao bang temp --danh cho truong hop phanbo



                --XOA DU LIEU TRUOC KHI INSERT
				DELETE 
				FROM ThucChay_MobileTemp 
				WHERE NgayThucHien < @NgayThucHien 
						AND CONVERT(NVARCHAR(50), DmBannerREF) IN (SELECT CONVERT(NVARCHAR(50), DmBannerREF) FROM @ThucChayHopDongChiTiet_Temp)
						AND ThucChay_MobileTemp.SoHopDong IN (SELECT SoHopDong FROM @ThucChayHopDongChiTiet_Temp)
														
				--INSERT DU LIEU
				--SELECT * FROM dbo.ThucChay_MobileTemp	
				--WHERE NgayThucHien = '2016-12-23'

				INSERT INTO ThucChay_MobileTemp	
					select [ThucChayID]
								  ,ISNULL(dbo.ThucChay_FormatSoHopDong(TC.[SoHopDong]),0)SoHopDong
								  ,[DanhsachDmBookingREF]
								  ,[DmSanPhamREF]
								  ,[TenSanPham]
								  ,[DmNhomWebsiteREF]
								  ,[TenNhomWebsite]
								  ,[DmWebsiteREF]
								  ,dbo.ThucChay_FormatDomainName([TenWebsite])[TenWebsite]
								  ,[DmChienDichREF]
								  ,[TenChienDich]
								  ,TC.[DmBannerREF]
								  ,[TenBanner]
								  ,[NgayThucHien]
								  ,[TongViewThucChay]
								  ,[TongClickThucChay]
								  ,[CreatedBy]
								  ,[CreatedAt]
								  ,[LastModifiedBy]
								  ,[LastModifiedAt]
								  ,[DeletedStatus]
								  ,[PrintStatus]
								  ,[RecordStatus]
								  ,[TongSoBaiViet]
								  ,[SoThuTuTheoNgay]
								  ,[TypeProduct]
								  ,[BannerType]
								  ,[UserName]
								  ,[SaleName]
								  ,[Email]
								  ,[LastTimeCalc]
								  ,[sys_date]
								  ,[IsReady]
								  ,[ProductUnitID]
								  ,[ProductUnitName]
								  ,[BannerTypeName]
								  ,[HopDongChiTietREF]
								  ,[CampainStatus]
								  ,[BannerStatus]
								  ,IsNoiBo
					   from ThucChay TC
								INNER JOIN @ThucChayHopDongChiTiet_Temp tchdctt ON	CONVERT(NVARCHAR(50), TC.DmBannerREF) = CONVERT(NVARCHAR(50), tchdctt.DmBannerREF) AND tchdctt.SoHopDong = TC.SoHopDong
						where 
								TypeProduct = 10 AND
								DmWebsiteREF != 0 AND			
								Convert(date,NgayThucHien)  <= Convert(date,@NgayThucHien)





---------------------------------------------------------------------------------------------





		
		--Insert vao bang HopDongChiTietAndBanner
                EXEC ThucChay_HopDongChiTietAndBannerByDmSanPhamREF 342,
                    @StartDate


		----------------------------------------------


				

				DECLARE @Temp TABLE(
					SoHopDong NVARCHAR(50),
					DmBannerREF INT,
					DmWebsiteREF INT
				)
				
				INSERT INTO @Temp
					SELECT DISTINCT
								A.SoHopDong ,
								A.DmBannerREF ,
								A.DmWebsiteREF
						FROM
							ThucChay_MobileTemp A
							LEFT JOIN (SELECT HopDongChiTietID
											FROM dbo.HopDongChiTiet
											WHERE DmSanPhamREF = 342
												AND ( DmLoaiBannerREF = 17
														OR DmLoaiNenTangREF = 8
													)
												AND DeletedStatus <> 1
										) T ON A.HopDongChiTietREF = T.HopDongChiTietID
						WHERE A.NgayThucHien < @NgayThucHien
								AND A.HopDongChiTietREF NOT IN (0, 1 )
								AND A.HopDongChiTietREF IS NOT NULL
								AND T.HopDongChiTietID IS NULL
								AND ( @pSoHopDong IS NULL
									  OR A.SoHopDong = @pSoHopDong
									)
								AND A.DmBannerREF = @pDmBannerID
								--AND HopDongChiTietREF NOT IN (
								--								SELECT
								--								HopDongChiTietID
								--								FROM
								--								dbo.HopDongChiTiet
								--								WHERE
								--									DmSanPhamREF = 342
								--								AND ( DmLoaiBannerREF = 17
								--										OR DmLoaiNenTangREF = 8
								--									)
								--								AND DeletedStatus <> 1 )



				

                DECLARE @Table TABLE
                    (
                      SoHopDong NVARCHAR(50) ,
                      DmBannerID INT ,
                      DmWebsiteID INT ,
                      TH INT
                    )







				-- Xac dinh truong hop can tinh

                INSERT  INTO @Table
                        SELECT DISTINCT
                                T.SoHopDong ,
                                T.DmBannerREF ,
                                T.DmWebsiteREF ,
                                t2.TH
                        FROM    ( SELECT * FROM @Temp
                                ) T
                                INNER JOIN ( SELECT DISTINCT
                                                    t2.DmBannerREF ,
                                                    t2.HopDongChiTietID ,
                                                    t2.SoHopDong ,
                                                    T6.TH
                                             FROM   ( SELECT  T.DmBannerID ,
                                                              CASE
																WHEN T.HopDongChiTietREF = 1
																	THEN 1
																WHEN T.HopDongChiTietREF > 1
																					AND T.KhuyenMai > 0
																	THEN 2
																WHEN T.HopDongChiTietREF > 1
																					AND T.KhuyenMai = 0
																	THEN 3
																ELSE 0
                                                              END TH
                                                      FROM    ( SELECT
																		DmBannerID ,
																		COUNT(DISTINCT HopDongChiTietREF) HopDongChiTietREF ,
																		SUM(T4.IsKhuyenMai) KhuyenMai
                                                              FROM
																  ( SELECT
																			  T1.SoHopDong ,
																			  T1.DmBannerREF DmBannerID ,
																			  t2.DmWebsiteREF ,
																			  T1.HopDongChiTietID HopDongChiTietREF ,
																			  T1.HopDongID ,
																			  T1.IsKhuyenMai
																	  FROM
																		  ( SELECT
																					*
																			 FROM @ThucChayHopDongChiTiet_Temp tchdctt
																		  ) T1
																	  INNER JOIN ( SELECT * FROM @Temp
																				) t2 ON CONVERT(NVARCHAR(50), t2.DmBannerREF) = CONVERT(NVARCHAR(50), T1.DmBannerREF)
																	  AND t2.SoHopDong = T1.SoHopDong
																  ) T4
                                                              GROUP BY DmBannerID
                                                              ) T
                                                    ) T6
                                                    INNER JOIN @ThucChayHopDongChiTiet_Temp t2 ON T6.DmBannerID = t2.DmBannerREF
                                             --WHERE  DmBannerID = 509570
                                           ) t2 ON T.DmBannerREF = t2.DmBannerREF
                                                   AND T.SoHopDong = t2.SoHopDong
                        




		/*
		-----------------------
			DELETE FROM ThucChayDaTinh 
			WHERE NgayThucHien < @NgayThucHien AND DmSanPhamREF = 342 
				AND NOT(DmHinhThucQuangCao IN(42,13) or DmLoaiBannerREF IN (17,18))
				AND HopDongChiTietREF IN (
					SELECT HopDongChiTietID FROM dbo.HopDongChiTiet
					WHERE DmSanPhamREF = 342
					AND DeletedStatus = 0
					AND DmLoaiNenTangREF <> 8
				)
				AND CONVERT(NVARCHAR(50), DmBannerREF) IN (SELECT CONVERT(NVARCHAR(50), DmBannerREF) FROM @ThucChayHopDongChiTiet_Temp)
				AND ThucChayDaTinh.SoHopDong IN (SELECT SoHopDong FROM @ThucChayHopDongChiTiet_Temp)
		*/


				
		--Duyet tung phan bo
                DECLARE vendor_cursor CURSOR
                FOR
                    SELECT  *
                    FROM    @Table t
			

                OPEN vendor_cursor
		
                FETCH NEXT FROM vendor_cursor INTO @SoHopDong, @DmBannerREF,
                    @DmWebsiteREF, @TH

                WHILE @@FETCH_STATUS = 0
                    BEGIN

			-- Truong hop map 1-1 
                        IF @TH = 1
                            BEGIN
                                EXEC sp_TC_ExcInsertThucChayDaTinh_Single_Mobile_TruongHopTreoSauChay @DmBannerREF,
                                    @NgayThucHien, @SoHopDong, @DmWebsiteREF
                            END				
				

			--Tinh cho truong hop 1 banner co tren 2 HĐCT, trong do co HĐ khuyen mai
                        ELSE
                            IF @TH = 2
                                BEGIN
                                    EXEC sp_TC_ExcInsertThucChayDaTinh_CoChietKhau_Mobile_TruongHopTreoSauChay @DmBannerREF,
                                        @NgayThucHien, @SoHopDong,
                                        @DmWebsiteREF
                                END
				

			--Tinh cho truong hop 1 banner co tren 2 HĐCT, trong do ko co HĐ khuyen mai	
                            ELSE
                                IF @TH = 3
                                    BEGIN 
                                        EXEC sp_TC_ExcInsertThucChayDaTinh_KoChietKhau_Mobile_TruongHopTreoSauChay @DmBannerREF,
                                            @NgayThucHien, @SoHopDong,
                                            @DmWebsiteREF
                                    END
                                ELSE
                                    PRINT 'Khong xac dinh case'
			

                        FETCH NEXT FROM vendor_cursor INTO @SoHopDong,
                            @DmBannerREF, @DmWebsiteREF, @TH
                    END 
                CLOSE vendor_cursor;
                DEALLOCATE vendor_cursor;




		--Tinh truong hop khong so hop dong
                --EXEC ThucChay_InsertThucChayDaTinh_MobileNoContract @NgayThucHien 
		
		------ Update Gia tri thay doi thuc chay Mobile
  --              EXEC sp_ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi @NgayThucHien,
  --                  @NgayThucHien			
		
		
		----------************
		----XU LY HD HUY
  --              EXEC sp_TC_UpdateGiaTriThayDoi_HDHuy @NgayThucHien,
  --                  @NgayThucHien				
		
		
		--Insert du lieu tu ThucChayDaTinhMobile -> ThucChayDaTinh 
                --PRINT 'Insert du lieu tu ThucChayDaTinhMobile -> ThucChayDaTinh '
                --EXEC ThucChay_InsertIntoTCDTFromTCDTMobile @NgayThucHien
		------************
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)

		
            END 


			UPDATE dbo.ThucChayDaTinh SET NgayThucHien = @pNgayTinh
			WHERE SoHopDong = @pSoHopDong
					AND	(GhiChu = N'sp_TC_InsertThucChayDaTinh_Mobile_TruongHopTreoSauChay'
							OR GhiChu = N'sp_TC_InsertThucChayDaTinh_CoChietKhau_Mobile_TruongHopTreoSauChay'
							OR GhiChu = N'sp_TC_InsertThucChayDaTinh_KoChietKhau_Mobile_TruongHopTreoSauChay'
							)
					AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
					AND DmBannerREF = @pDmBannerID



    END

```
