# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhCPV_TruongHopTreoSauChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-25 16:14:28.553000
- **Ngày sửa cuối**: 2017-12-13 10:39:07.090000

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

--EXEC [ThucChay_ExcInsertThucChayDaTinhCPV] '2014-10-01','2014-10-01'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhCPV_TruongHopTreoSauChay]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @pDmSanPham INT = NULL
  , @pSoHopDong NVARCHAR(50) = NULL
  , @pDmBannerID INT
  , @pNgayThucHien DATETIME
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME
          , @Count INT
        DECLARE @SoHopDong NVARCHAR(50)
          , @TypeProduct INT
          , @HDLechGiaYN NVARCHAR(50)
          , @TenWebsite NVARCHAR(50)
          , @DmWebsiteREF INT
          , @DmBannerREF INT
        SET @NgayThucHien = @StartDate
	
        TRUNCATE TABLE dbo.ThucChayTemp
        TRUNCATE TABLE dbo.ThucChayCPVTemp
	
	
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
                TRUNCATE TABLE dbo.ThucChayTemp
                TRUNCATE TABLE dbo.ThucChayCPVTemp
		
                INSERT  INTO dbo.ThucChayCPVTemp
                        ( typeproduct
                        , ProductName
                        , bannerid
                        , totalview
                        , percent_rate
                        , CPV
                        , NgayThucHien
		                )
                        SELECT  typeproduct
                              , ProductName
                              , bannerid
                              , totalview
                              , percent_rate
                              , CPV
                              , NgayThucHien
                        FROM    ThucChayCPV tcc
                                INNER JOIN ( SELECT DmBannerID
                                             FROM   ThucChayHopDongChiTietAndBanner
                                             WHERE  CONVERT(DATE, CreatedAt) > @NgayThucHien
                                                    AND CONVERT(DATE, CreatedAt) > CONVERT(DATE, ThoiGianBatDau)
                                                    AND DeletedStatus = 0
                                           ) tchdctab ON CONVERT(NVARCHAR(50), tcc.bannerid) = tchdctab.DmBannerID
                        WHERE   CONVERT(DATE, tcc.NgayThucHien) = @NgayThucHien
                                AND ( @pDmSanPham IS NULL
                                      OR ( CASE WHEN typeproduct = 14 THEN 598
                                                WHEN typeproduct = 15 THEN 613
                                                WHEN typeproduct = 5 THEN 339
                                                WHEN typeproduct = 8 THEN 240
                                                WHEN typeproduct = 9 THEN 370
                                                WHEN typeproduct = 18 THEN 735
                                                ELSE typeproduct
                                           END ) = @pDmSanPham
                                    )
                                AND tcc.bannerid = @pDmBannerID
		
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
                                LEFT JOIN dbo.ThucChayCPV_TruongHopTreoSauChay tcthtsc ON TC.DmBannerREF = tcthtsc.DmBannerID
                                                                                          AND TC.DmWebsiteREF = tcthtsc.DmWebsiteID
                                                                                          AND TC.NgayThucHien = tcthtsc.NgayThucHien
                        WHERE   TC.NgayThucHien = @NgayThucHien
                                AND TypeProduct NOT IN ( 1, 2, 17 )
                                AND DmWebsiteREF != 0
                                AND ( @pDmSanPham IS NULL
                                      OR ( CASE WHEN TypeProduct = 14 THEN 598
                                                WHEN TypeProduct = 15 THEN 613
                                                WHEN TypeProduct = 5 THEN 339
                                                WHEN TypeProduct = 8 THEN 240
                                                WHEN TypeProduct = 9 THEN 370
                                                WHEN TypeProduct = 18 THEN 735
                                                ELSE TypeProduct
                                           END ) = @pDmSanPham
                                    )
                                AND tcthtsc.DmBannerID IS NULL
                                AND tcthtsc.DmWebsiteID IS NULL
                                AND tcthtsc.NgayThucHien IS NULL
                                AND ( @pSoHopDong IS NULL
                                      OR TC.SoHopDong = @pSoHopDong
                                    )
                                AND TC.DmBannerREF = @pDmBannerID






									---- Luu nhung thuc chay da tinh vao bang, de ko tinh lai lan sau

                IF NOT EXISTS ( SELECT  *
                                FROM    ( SELECT    TC.DmBannerREF
                                                  , TC.DmWebsiteREF
                                                  , TC.NgayThucHien
                                          FROM      ThucChay TC
                                                    INNER JOIN ( SELECT DmBannerID
                                                                 FROM   ThucChayHopDongChiTietAndBanner
                                                                 WHERE  CONVERT(DATE, CreatedAt) > @NgayThucHien
                                                                        AND CONVERT(DATE, CreatedAt) > CONVERT(DATE, ThoiGianBatDau)
                                                                        AND DeletedStatus = 0
                                                               ) tchdctab ON CONVERT(NVARCHAR(50), TC.DmBannerREF) = tchdctab.DmBannerID
                                          WHERE     NgayThucHien = @NgayThucHien
                                                    AND TypeProduct NOT IN ( 1, 2, 17 )
                                                    AND DmWebsiteREF != 0
                                                    AND ( @pDmSanPham IS NULL
                                                          OR ( CASE WHEN TypeProduct = 14 THEN 598
                                                                    WHEN TypeProduct = 15 THEN 613
                                                                    WHEN TypeProduct = 5 THEN 339
                                                                    WHEN TypeProduct = 8 THEN 240
                                                                    WHEN TypeProduct = 9 THEN 370
                                                                    WHEN TypeProduct = 18 THEN 735
                                                                    ELSE TypeProduct
                                                               END ) = @pDmSanPham
                                                        )
                                                    AND ( @pSoHopDong IS NULL
                                                          OR TC.SoHopDong = @pSoHopDong
                                                        )
                                                    AND TC.DmBannerREF = @pDmBannerID
                                        ) T1
                                        INNER JOIN dbo.ThucChayCPV_TruongHopTreoSauChay T2 ON T1.DmBannerREF = T2.DmBannerID
                                                                                              AND T1.DmWebsiteREF = T2.DmWebsiteID
                                                                                              AND T1.NgayThucHien = T2.NgayThucHien )
                    BEGIN
                        INSERT  INTO ThucChayCPV_TruongHopTreoSauChay
                                SELECT  TC.DmBannerREF
                                      , TC.DmWebsiteREF
                                      , TC.NgayThucHien
                                FROM    ThucChay TC
                                        INNER JOIN ( SELECT DmBannerID
                                                     FROM   ThucChayHopDongChiTietAndBanner
                                                     WHERE  CONVERT(DATE, CreatedAt) > @NgayThucHien
                                                            AND CONVERT(DATE, CreatedAt) > CONVERT(DATE, ThoiGianBatDau)
                                                            AND DeletedStatus = 0
                                                   ) tchdctab ON CONVERT(NVARCHAR(50), TC.DmBannerREF) = tchdctab.DmBannerID
                                WHERE   NgayThucHien = @NgayThucHien
                                        AND TypeProduct NOT IN ( 1, 2, 17 )
                                        AND DmWebsiteREF != 0
                                        AND ( @pDmSanPham IS NULL
                                              OR ( CASE WHEN TypeProduct = 14 THEN 598
                                                        WHEN TypeProduct = 15 THEN 613
                                                        WHEN TypeProduct = 5 THEN 339
                                                        WHEN TypeProduct = 8 THEN 240
                                                        WHEN TypeProduct = 9 THEN 370
                                                        WHEN TypeProduct = 18 THEN 735
                                                        ELSE TypeProduct
                                                   END ) = @pDmSanPham
                                            )
                                        AND ( @pSoHopDong IS NULL
                                              OR TC.SoHopDong = @pSoHopDong
                                            )
                                        AND TC.DmBannerREF = @pDmBannerID
                    END






                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            A.SoHopDong
                          , A.TypeProduct
                          , A.DmWebsiteREF
                          , A.TenWebsite
                          , A.DmBannerREF
                    FROM    ( SELECT    tct.SoHopDong
                                      , tct.TypeProduct
                                      , tct.DmWebsiteREF
                                      , tct.TenWebsite
                                      , tct.DmBannerREF
                              FROM      ThucChayTemp tct
                                        INNER JOIN ThucChayCPVTemp tcc ON tct.DmBannerREF = tcc.bannerid
                                                                          AND tct.NgayThucHien = tcc.NgayThucHien
																		  AND tcc.typeproduct = tct.TypeProduct
                            ) A
                    ORDER BY A.SoHopDong
                          , A.TypeProduct	
		--WHERE A.HDLechGiaYN = 'Y'
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
				--PRINT 'vao 1'
                        EXEC ThucChay_InsertThucChayDaTinhCPV_TruongHopTreoSauChay @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite,
                            @DmBannerREF
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
		--delete from dbo.ThucChayTemp
            END 




        UPDATE  dbo.ThucChayDaTinh
        SET     NgayThucHien = @pNgayThucHien
        WHERE   SoHopDong = @pSoHopDong
                AND GhiChu = N'CPM: ThucChay_InsertThucChayDaTinhCPV_TruongHopTreoSauChay'
                AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
                AND DmBannerREF = @pDmBannerID
                AND DmSanPhamREF = @pDmSanPham


	
        SELECT  '1'
    END


--EXEC [ThucChay_ExcInsertThucChayDaTinhCPV] '2014-08-12','2014-08-13'

```
