# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_CPR_TinhTheoBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-07 11:04:24.800000
- **Ngày sửa cuối**: 2017-11-07 11:04:24.800000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@BannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2015-09-13','2015-09-13'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPR_TinhTheoBanner]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @BannerID INT
AS
    BEGIN
        DECLARE @NgayThucHien DATETIME
          , @Count INT
        DECLARE @SoHopDong NVARCHAR(50)
          , @TypeProduct INT
          , @TenWebsite NVARCHAR(50)
          , @DmWebsiteREF INT
			
        SET @NgayThucHien = @StartDate
        DELETE  FROM dbo.ThucChayTemp
	--Xoa du lieu ThucChayDaTinh truoc khi tinh
        DELETE  FROM ThucChayDaTinh
        WHERE   CONVERT(DATE, NgayThucHien) BETWEEN @StartDate AND @EndDate
                AND DmSanPhamREF IN ( 680 )
				AND DmBannerREF = @BannerID
	
        DELETE  FROM ThucChayCPRTemp
	
        DELETE  FROM dbo.ThucChayTemp
	
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
                        SELECT  ThucChayID
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
                        FROM    ThucChay
                        WHERE   CONVERT(NVARCHAR(50), NgayThucHien, 103) = CONVERT(NVARCHAR(50), @NgayThucHien, 103)
                                AND TypeProduct IN ( 16 )
                                AND DmWebsiteREF != 0
								AND DmBannerREF = @BannerID
		
                INSERT  INTO ThucChayCPRTemp
                        SELECT  *
                        FROM    ThucChayCPR tcc
                        WHERE   CONVERT(NVARCHAR(50), NgayThucHien, 103) = CONVERT(NVARCHAR(50), @NgayThucHien, 103)
								AND tcc.bannerid = @BannerID
		
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
				
				
                        EXEC ThucChay_InsertThucChayDaTinh_CPR_TinhTheoBanner @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @BannerID
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
		--XU LY HD HUY
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
                DELETE  FROM dbo.ThucChayTemp
                DELETE  FROM ThucChayCPRTemp
		--EXEC [ThucChay_UpdateGiaTriThayDoi_CPR] @NgayThucHien
            END 
	
        SELECT  '1'
    END


--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2014-06-03','2014-06-03'

```
