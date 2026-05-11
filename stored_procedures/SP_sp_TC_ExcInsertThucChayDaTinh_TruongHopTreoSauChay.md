# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_TruongHopTreoSauChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-24 10:54:54.727000
- **Ngày sửa cuối**: 2017-12-12 14:55:38.900000

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

-- sp_TC_ExcInsertThucChayDaTinh_TruongHopTreoSauChay '2017-10-20', '2017-10-24',240,'QC3311017', '2017-10-24'
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_TruongHopTreoSauChay]
    @StartDate DATETIME ,
    @EndDate DATETIME ,
    @pDmSanPham INT = NULL,
	@pSoHopDong NVARCHAR(50) = NULL,
	@pDmBannerID INT ,
	@pNgayThucHien DATETIME
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME ,
            @Count INT
        DECLARE @SoHopDong NVARCHAR(50) ,
            @TypeProduct INT ,
            @HDLechGiaYN NVARCHAR(50) ,
            @TenWebsite NVARCHAR(50) ,
            @DmWebsiteREF INT ,
            @DmBannerREF INT
        SET @NgayThucHien = @StartDate


        TRUNCATE TABLE dbo.ThucChayTemp




        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN

				

                INSERT  INTO dbo.ThucChayTemp
                        SELECT  TC.ThucChayID ,
                                TC.SoHopDong ,
                                TC.DanhsachDmBookingREF ,
                                TC.DmSanPhamREF ,
                                TC.TenSanPham ,
                                TC.DmNhomWebsiteREF ,
                                TC.TenNhomWebsite ,
                                TC.DmWebsiteREF ,
                                TC.TenWebsite ,
                                TC.DmChienDichREF ,
                                TC.TenChienDich ,
                                TC.DmBannerREF ,
                                TC.TenBanner ,
                                TC.NgayThucHien ,
                                TC.TongViewThucChay ,
                                TC.TongClickThucChay ,
                                TC.CreatedBy ,
                                TC.CreatedAt ,
                                TC.LastModifiedBy ,
                                TC.LastModifiedAt ,
                                TC.DeletedStatus ,
                                TC.PrintStatus ,
                                TC.RecordStatus ,
                                TC.TongSoBaiViet ,
                                TC.SoThuTuTheoNgay ,
                                TC.TypeProduct ,
                                TC.BannerType ,
                                TC.UserName ,
                                TC.SaleName ,
                                TC.Email ,
                                TC.LastTimeCalc ,
                                TC.sys_date ,
                                TC.IsReady ,
                                TC.ProductUnitID ,
                                TC.ProductUnitName ,
                                TC.BannerTypeName ,
                                TC.HopDongChiTietREF ,
                                TC.CampainStatus ,
                                TC.BannerStatus ,
                                TC.IsNoiBo 
                        FROM    ThucChay TC
                                INNER JOIN ( SELECT DmBannerID
                                             FROM   ThucChayHopDongChiTietAndBanner
                                             WHERE  CONVERT(DATE, CreatedAt) > @NgayThucHien
                                                    AND CONVERT(DATE, CreatedAt) > CONVERT(DATE, ThoiGianBatDau)
                                                    AND DeletedStatus = 0
                                           ) tchdctab ON CONVERT(NVARCHAR(50), TC.DmBannerREF) = tchdctab.DmBannerID
                                LEFT JOIN dbo.ThucChay_TruongHopTreoSauChay tcthtsc ON TC.DmBannerREF = tcthtsc.DmBannerID
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
                                                    AND TypeProduct NOT IN ( 1, 2, 17 )
                                                    AND DmWebsiteREF != 0
                                                    AND ( @pDmSanPham IS NULL
                                                          OR ( CASE
                                                              WHEN TypeProduct = 14
                                                              THEN 598
                                                              WHEN TypeProduct = 15
                                                              THEN 613
                                                              WHEN TypeProduct = 5
                                                              THEN 339
                                                              WHEN TypeProduct = 8
                                                              THEN 240
                                                              WHEN TypeProduct = 9
                                                              THEN 370
															  WHEN TypeProduct = 18 THEN 735
                                                              ELSE TypeProduct
                                                              END ) = @pDmSanPham
                                                        )
													AND (@pSoHopDong IS NULL OR TC.SoHopDong = @pSoHopDong)
													AND TC.DmBannerREF = @pDmBannerID
                                        ) T1
                                        INNER JOIN dbo.ThucChay_TruongHopTreoSauChay T2 ON T1.DmBannerREF = T2.DmBannerID
                                                              AND T1.DmWebsiteREF = T2.DmWebsiteID
                                                              AND T1.NgayThucHien = T2.NgayThucHien )
                    BEGIN
                        INSERT  INTO ThucChay_TruongHopTreoSauChay
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
                                        AND TypeProduct NOT IN ( 1, 2, 17 )
                                        AND DmWebsiteREF != 0
                                        AND ( @pDmSanPham IS NULL
                                              OR ( CASE WHEN TypeProduct = 14
                                                        THEN 598
                                                        WHEN TypeProduct = 15
                                                        THEN 613
                                                        WHEN TypeProduct = 5
                                                        THEN 339
                                                        WHEN TypeProduct = 8
                                                        THEN 240
                                                        WHEN TypeProduct = 9
                                                        THEN 370
														WHEN TypeProduct = 18 THEN 735
                                                        ELSE TypeProduct
                                                   END ) = @pDmSanPham
                                            )
										AND (@pSoHopDong IS NULL OR TC.SoHopDong = @pSoHopDong)
										AND TC.DmBannerREF = @pDmBannerID
                    END





                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            A.SoHopDong ,
                            A.TypeProduct ,
                            A.DmWebsiteREF ,
                            A.TenWebsite ,
                            A.DmBannerREF ,
                            A.HDLechGiaYN
                    FROM    ( SELECT    tct.SoHopDong ,
                                        tct.TypeProduct ,
                                        tct.DmWebsiteREF ,
                                        tct.TenWebsite ,
                                        tct.DmBannerREF ,
				--dbo.ThucChay_CheckHopDongCoSanPhamLechDonGiaYN(tct.TypeProduct,tct.SoHopDong) HDLechGiaYN 
                                        'Y' HDLechGiaYN
                              FROM      ThucChayTemp tct
                            ) A
                    ORDER BY A.SoHopDong ,
                            A.TypeProduct	
		--WHERE A.HDLechGiaYN = 'Y'
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct,
                    @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
                        
                        EXEC sp_TC_InsertThucChayDaTinh_TruongHopTreoSauChay @NgayThucHien,
                            @SoHopDong, @TypeProduct, @DmWebsiteREF,
                            @TenWebsite, @DmBannerREF, @pNgayThucHien
			
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong,
                            @TypeProduct, @DmWebsiteREF, @TenWebsite,
                            @DmBannerREF, @HDLechGiaYN
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
		--XU LY HD HUY
		--HAIDH COMMENT PHAN CHUC NANG KIEM SOAT HOPDONG HUY
		--EXEC [ThucChay_UpdateGiaTriThayDoi_HDHuy] @NgayThucHien, @NgayThucHien
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
                TRUNCATE TABLE dbo.ThucChayTemp
            END 


			UPDATE dbo.ThucChayDaTinh SET NgayThucHien = @pNgayThucHien
			WHERE SoHopDong = @pSoHopDong
					AND	GhiChu = N'CPM: sp_TC_InsertThucChayDaTinh_TruongHopTreoSauChay'
					AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
					AND DmBannerREF = @pDmBannerID
					AND DmSanPhamREF = @pDmSanPham


	
        SELECT  '1'
    END


--EXEC [ThucChay_ExcInsertThucChayDaTinh] '2014-06-03','2014-06-03'

```
