# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR_TruongHopTreoSauChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-12 15:59:55.920000
- **Ngày sửa cuối**: 2017-12-12 15:59:55.920000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pDmSanPham` | `int(4)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pDmBannerID` | `int(4)` | No |
| `@pNgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR] '2017-06-12','2017-06-12'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR_TruongHopTreoSauChay]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @pDmSanPham INT = NULL
  , @pSoHopDong NVARCHAR(50) = NULL
  , @pDmBannerID INT
  , @pNgayThucHien DATETIME
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME
        DECLARE @SoHopDong NVARCHAR(50)
          , @HopDongID INT
          , @TypeProduct INT
          , @TenWebsite NVARCHAR(50)
          , @DmWebsiteREF INT
			
        SET @NgayThucHien = @StartDate
        SET @TenWebsite = '(Blanks)'
        SET @DmWebsiteREF = 826
	
	
	
        TRUNCATE TABLE ThucChayCPRTemp
	
        TRUNCATE TABLE dbo.ThucChayTemp
	
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
		
                INSERT  INTO dbo.ThucChayTemp
                        ( ThucChayID
                        , SoHopDong
                        , DanhsachDmBookingREF
                        , DmSanPhamREF
                        , TenSanPham
                        , DmNhomWebsiteREF
                        , TenNhomWebsite
                        , DmWebsiteREF
                        , TenWebsite
                        , DmChienDichREF
                        , TenChienDich
                        , DmBannerREF
                        , TenBanner
                        , NgayThucHien
                        , TongViewThucChay
                        , TongClickThucChay
                        , CreatedBy
                        , CreatedAt
                        , LastModifiedBy
                        , LastModifiedAt
                        , DeletedStatus
                        , PrintStatus
                        , RecordStatus
                        , TongSoBaiViet
                        , SoThuTuTheoNgay
                        , TypeProduct
                        , BannerType
                        , UserName
                        , SaleName
                        , Email
                        , LastTimeCalc
                        , sys_date
                        , IsReady
                        , ProductUnitID
                        , ProductUnitName
                        , BannerTypeName
                        , HopDongChiTietREF
                        , CampainStatus
                        , BannerStatus
                        , IsNoiBo
		                )
                        SELECT  TC.ThucChayID
                              , TC.SoHopDong
                              , TC.DanhsachDmBookingREF
                              , TC.DmSanPhamREF
                              , TC.TenSanPham
                              , TC.DmNhomWebsiteREF
                              , TC.TenNhomWebsite
                              , TC.DmWebsiteREF
                              , TC.TenWebsite
                              , TC.DmChienDichREF
                              , TC.TenChienDich
                              , TC.DmBannerREF
                              , TC.TenBanner
                              , TC.NgayThucHien
                              , TC.TongViewThucChay
                              , TC.TongClickThucChay
                              , TC.CreatedBy
                              , TC.CreatedAt
                              , TC.LastModifiedBy
                              , TC.LastModifiedAt
                              , TC.DeletedStatus
                              , TC.PrintStatus
                              , TC.RecordStatus
                              , TC.TongSoBaiViet
                              , TC.SoThuTuTheoNgay
                              , TC.TypeProduct
                              , TC.BannerType
                              , TC.UserName
                              , TC.SaleName
                              , TC.Email
                              , TC.LastTimeCalc
                              , TC.sys_date
                              , TC.IsReady
                              , TC.ProductUnitID
                              , TC.ProductUnitName
                              , TC.BannerTypeName
                              , TC.HopDongChiTietREF
                              , TC.CampainStatus
                              , TC.BannerStatus
                              , TC.IsNoiBo
                        FROM    ThucChay TC
                                INNER JOIN ( SELECT DmBannerID
                                             FROM   ThucChayHopDongChiTietAndBanner
                                             WHERE  CONVERT(DATE, CreatedAt) > @NgayThucHien
                                                    AND CONVERT(DATE, CreatedAt) > CONVERT(DATE, ThoiGianBatDau)
                                                    AND DeletedStatus = 0
                                           ) tchdctab ON CONVERT(NVARCHAR(50), TC.DmBannerREF) = tchdctab.DmBannerID
                                LEFT JOIN dbo.ThucChayByDVT_CPR_TruongHopTreoSauChay tcthtsc ON TC.DmBannerREF = tcthtsc.DmBannerID
                                                              AND TC.DmWebsiteREF = tcthtsc.DmWebsiteID
                                                              AND TC.NgayThucHien = tcthtsc.NgayThucHien
                        WHERE   TC.NgayThucHien = @NgayThucHien
                                AND TypeProduct IN ( 16, 14 )
                                AND DmWebsiteREF != 0
								AND ( @pDmSanPham IS NULL
                                      OR ( CASE WHEN TypeProduct = 14 THEN 598
												WHEN TypeProduct = 16 THEN 680
                                                ELSE TypeProduct
                                           END ) = @pDmSanPham
                                    )
                                AND tcthtsc.DmBannerID IS NULL
                                AND tcthtsc.DmWebsiteID IS NULL
                                AND tcthtsc.NgayThucHien IS NULL
								AND (@pSoHopDong IS NULL OR TC.SoHopDong = @pSoHopDong)
								AND TC.DmBannerREF = @pDmBannerID




								---- Luu nhung thuc chay da tinh vao bang, de ko tinh lai lan sau

				IF NOT EXISTS ( SELECT  *
                                FROM    ( SELECT    TC.DmBannerREF ,
                                                    TC.DmWebsiteREF ,
                                                    TC.NgayThucHien
                                          FROM      ThucChay TC
                                                    INNER JOIN ( SELECT
                                                              DmBannerID
                                                              FROM
                                                              ThucChayHopDongChiTietAndBanner
                                                              WHERE
                                                              CONVERT(DATE, CreatedAt) > @NgayThucHien
                                                              AND CONVERT(DATE, CreatedAt) > CONVERT(DATE, ThoiGianBatDau)
                                                              AND DeletedStatus = 0
                                                              ) tchdctab ON CONVERT(NVARCHAR(50), TC.DmBannerREF) = tchdctab.DmBannerID
                                          WHERE     NgayThucHien = @NgayThucHien
                                                    AND TypeProduct IN ( 16, 14 )
													AND DmWebsiteREF != 0
													AND ( @pDmSanPham IS NULL
														  OR ( CASE WHEN TypeProduct = 14 THEN 598
																	WHEN TypeProduct = 16 THEN 680
																	ELSE TypeProduct
															   END ) = @pDmSanPham
														)
													AND (@pSoHopDong IS NULL OR TC.SoHopDong = @pSoHopDong)
													AND TC.DmBannerREF = @pDmBannerID
                                        ) T1
                                        INNER JOIN dbo.ThucChayByDVT_CPR_TruongHopTreoSauChay T2 ON T1.DmBannerREF = T2.DmBannerID
                                                              AND T1.DmWebsiteREF = T2.DmWebsiteID
                                                              AND T1.NgayThucHien = T2.NgayThucHien )
                    BEGIN
                        INSERT  INTO ThucChayByDVT_CPR_TruongHopTreoSauChay
                                SELECT  TC.DmBannerREF ,
                                        TC.DmWebsiteREF ,
                                        TC.NgayThucHien
                                FROM    ThucChay TC
                                        INNER JOIN ( SELECT DmBannerID
                                                     FROM   ThucChayHopDongChiTietAndBanner
                                                     WHERE  CONVERT(DATE, CreatedAt) > @NgayThucHien
                                                            AND CONVERT(DATE, CreatedAt) > CONVERT(DATE, ThoiGianBatDau)
                                                            AND DeletedStatus = 0
                                                   ) tchdctab ON CONVERT(NVARCHAR(50), TC.DmBannerREF) = tchdctab.DmBannerID
                                WHERE   NgayThucHien = @NgayThucHien
                                        AND TypeProduct IN ( 16, 14 )
										AND DmWebsiteREF != 0
										AND ( @pDmSanPham IS NULL
												OR ( CASE WHEN TypeProduct = 14 THEN 598
														WHEN TypeProduct = 16 THEN 680
														ELSE TypeProduct
													END ) = @pDmSanPham
											)
										AND (@pSoHopDong IS NULL OR TC.SoHopDong = @pSoHopDong)
										AND TC.DmBannerREF = @pDmBannerID
                    END




		
                INSERT  INTO dbo.ThucChayCPRTemp
                        ( bannerid
                        , uvngay
                        , uv
                        , typeproduct
                        , ProductName
                        , NgayThucHien
                        , ThoiGianTao
                        , uvhour
                        , TVDenNgay
                        , TCDenNgay
		                )
                        SELECT  bannerid
                              , uvNgay
                              , uv
                              , typeproduct
                              , ProductName
                              , NgayThucHien
                              , ThoiGianTao
                              , uvhour
                              , TVDenNgay
                              , TCDenNgay
                        FROM    ThucChayCPR tcc
                        WHERE   NgayThucHien = @NgayThucHien
		--where NgayThucHien = @NgayThucHien
		--SELECT * FROM ThucChayCPR tcc
		--where Convert(date,NgayThucHien) = Convert(date,@NgayThucHien)
		

		
                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            A.SoHopDong
                          , A.TypeProduct
                    FROM    ( SELECT    tct.SoHopDong
                                      , tct.TypeProduct
                                      , tct.DmBannerREF
                              FROM      ( SELECT DISTINCT
                                                    tct.SoHopDong
                                                  , tct.TypeProduct
                                                  , tct.DmBannerREF
                                          FROM      ThucChayTemp tct
                                                    INNER JOIN ( SELECT hd.SoHopDong
                                                                 FROM   HopDong hd
                                                                        INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
                                                                 WHERE  hdct.DmSanPhamREF IN ( 680, 598 )
                                                                        AND hdct.DonViTinhREF = 30
                                                                        AND hd.TrangThaiHopDong <> 3
                                                                        AND hdct.DeletedStatus = 0
					    --AND SoHopDong = @shd
                                                               ) hd ON hd.SoHopDong = tct.SoHopDong
                                        ) tct
                                        INNER JOIN ThucChayCPRTemp tcc ON tcc.typeproduct = tct.TypeProduct
                                                                          AND tcc.bannerid = tct.DmBannerREF
                            ) A
                    ORDER BY A.SoHopDong
                          , A.TypeProduct	
		--WHERE A.HDLechGiaYN = 'Y'
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
                        SET @HopDongID = ISNULL(( SELECT TOP 1
                                                            hd.HopDongID
                                                  FROM      HopDong hd
                                                  WHERE     hd.SoHopDong = @SoHopDong
                                                ), 0)

                        PRINT @SoHopDong
                        EXEC ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR_TruongHopTreoSauChay @NgayThucHien, @HopDongID, @TypeProduct, @DmWebsiteREF, @TenWebsite 
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
		--XU LY HD HUY
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
                TRUNCATE TABLE dbo.ThucChayTemp
                TRUNCATE TABLE ThucChayCPRTemp
            END 


			UPDATE dbo.ThucChayDaTinh SET NgayThucHien = @pNgayThucHien
			WHERE SoHopDong = @pSoHopDong
					AND	GhiChu = N'CPM: ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR_TruongHopTreoSauChay'
					AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
					AND DmBannerREF = @pDmBannerID
					AND DmSanPhamREF = @pDmSanPham


	
        SELECT  '1'
    END


--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2014-06-03','2014-06-03'

```
