# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_CPR_TruongHopTreoSauChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-12 15:45:04.880000
- **Ngày sửa cuối**: 2017-12-12 15:45:04.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
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
--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2015-09-13','2015-09-13'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPR_TruongHopTreoSauChay]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @pSoHopDong NVARCHAR(50) = NULL
  , @pDmBannerID INT
  , @pNgayThucHien DATETIME
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME
          , @Count INT
        DECLARE @SoHopDong NVARCHAR(50)
          , @TypeProduct INT
          , @TenWebsite NVARCHAR(50)
          , @DmWebsiteREF INT
			
        SET @NgayThucHien = @StartDate
	
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
                                LEFT JOIN dbo.ThucChayCPR_TruongHopTreoSauChay tcthtsc ON TC.DmBannerREF = tcthtsc.DmBannerID
                                                              AND TC.DmWebsiteREF = tcthtsc.DmWebsiteID
                                                              AND TC.NgayThucHien = tcthtsc.NgayThucHien
                        WHERE   TC.NgayThucHien = @NgayThucHien
                                AND TypeProduct IN ( 16 )
                                AND DmWebsiteREF != 0
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
                                                    AND TypeProduct IN ( 16 )
                                                    AND DmWebsiteREF != 0
													AND (@pSoHopDong IS NULL OR TC.SoHopDong = @pSoHopDong)
													AND TC.DmBannerREF = @pDmBannerID
                                        ) T1
                                        INNER JOIN dbo.ThucChayCPR_TruongHopTreoSauChay T2 ON T1.DmBannerREF = T2.DmBannerID
                                                              AND T1.DmWebsiteREF = T2.DmWebsiteID
                                                              AND T1.NgayThucHien = T2.NgayThucHien )
                    BEGIN
                        INSERT  INTO ThucChayCPR_TruongHopTreoSauChay
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
                                        AND TypeProduct IN ( 16 )
                                        AND DmWebsiteREF != 0
										AND (@pSoHopDong IS NULL OR TC.SoHopDong = @pSoHopDong)
										AND TC.DmBannerREF = @pDmBannerID
                    END



                INSERT  INTO ThucChayCPRTemp
                        SELECT  *
                        FROM    ThucChayCPR tcc
                        WHERE   NgayThucHien = @NgayThucHien
		
                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            A.SoHopDong
                          , A.TypeProduct
                          , A.DmWebsiteREF
                          , A.TenWebsite
                    FROM    ( SELECT    tct.SoHopDong
                                      , tct.TypeProduct
                                      , tct.DmWebsiteREF
                                      , tct.TenWebsite
                              FROM      ThucChayTemp tct
                            ) A
                    ORDER BY A.SoHopDong
                          , A.TypeProduct	
		--WHERE A.HDLechGiaYN = 'Y'
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
				
				
                        EXEC ThucChay_InsertThucChayDaTinh_CPR_TruongHopTreoSauChay @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
		--XU LY HD HUY
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
                TRUNCATE TABLE dbo.ThucChayTemp
                TRUNCATE TABLE ThucChayCPRTemp
		--EXEC [ThucChay_UpdateGiaTriThayDoi_CPR] @NgayThucHien
            END 




			UPDATE dbo.ThucChayDaTinh SET NgayThucHien = @pNgayThucHien
			WHERE SoHopDong = @pSoHopDong
					AND	GhiChu = N'CPM: ThucChay_InsertThucChayDaTinh_CPR_TruongHopTreoSauChay'
					AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
					AND DmBannerREF = @pDmBannerID
					AND DmSanPhamREF = 680

	
        SELECT  '1'
    END


--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2014-06-03','2014-06-03'

```
