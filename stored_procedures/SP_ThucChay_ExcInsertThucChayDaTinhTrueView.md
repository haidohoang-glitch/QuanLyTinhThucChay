# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhTrueView`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-19 10:47:16.030000
- **Ngày sửa cuối**: 2023-08-21 17:37:03.563000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_ExcInsertThucChayDaTinhTrueView '2014-10-01','2014-10-01'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhTrueView]
    @StartDate DATETIME
  , @EndDate DATETIME
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
	
        DELETE  FROM dbo.ThucChayTemp
        DELETE  FROM dbo.ThucChayTrueViewTemp
	
		--Xoa du lieu ThucChayDaTinh truoc khi tinh
        DELETE  FROM ThucChayDaTinh
        WHERE   CONVERT(DATE, NgayThucHien) BETWEEN @StartDate AND @EndDate
                AND DmSanPhamREF IN ( 240 )
                AND (DonViTinh = N'True View' OR DonViTinh = N'TRUE REACH')
                AND DmHinhThucQuangCao <> 42
	
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
                DELETE  FROM dbo.ThucChayTrueViewTemp
		
                INSERT  INTO dbo.ThucChayTrueViewTemp
                        ( SoHopDong
                        , TypeProduct
                        , DmSanPhamREF
                        , TenSanPham
                        , campaignid
                        , bannerid
                        , SiteName
                        , SiteID
                        , True_View
                        , Views
                        , Clicks
                        , NgayThucHien
                        , CreatedBy
                        , CreatedAt
                        , LastModifiedBy
                        , LastModifiedAt
                        , DeletedStatus
                        )
                        SELECT  tcc.SoHopDong
                              , tcc.TypeProduct
                              , tcc.DmSanPhamREF
                              , tcc.TenSanPham
                              , tcc.campaignid
                              , tcc.bannerid
                              , tcc.SiteName
                              , tcc.SiteID
                              , tcc.True_View
                              , tcc.Views
                              , tcc.Clicks
                              , tcc.NgayThucHien
                              , tcc.CreatedBy
                              , tcc.CreatedAt
                              , tcc.LastModifiedBy
                              , tcc.LastModifiedAt
                              , tcc.DeletedStatus
                        FROM    dbo.ThucChayTrueView tcc
                        WHERE   CONVERT(DATE, tcc.NgayThucHien) = @NgayThucHien
		
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
                        FROM    dbo.ThucChay
                        WHERE   CONVERT(NVARCHAR(50), NgayThucHien, 103) = CONVERT(NVARCHAR(50), @NgayThucHien, 103)
					            AND TypeProduct NOT IN ( 1, 2, 17 )
                                AND DmWebsiteREF <> 0

                DECLARE Record_Cursor CURSOR
                FOR
                     SELECT DISTINCT
                            A.SoHopDong
                          , A.TypeProduct
                          , A.DmWebsiteREF
                          , A.TenWebsite
                          , A.DmBannerREF
                    FROM    ( SELECT    tcc.SoHopDong
                                      , tcc.TypeProduct
                                      , tcc.SiteID DmWebsiteREF
                                      , tcc.SiteName TenWebsite
                                      , tcc.bannerid DmBannerREF
                              FROM      dbo.ThucChayTrueViewTemp tcc 
							  WHERE 1=1
                            ) A
                    ORDER BY A.SoHopDong
                          , A.TypeProduct
		
                OPEN Record_Cursor

				-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
				
                        EXEC ThucChay_InsertThucChayDaTinhTrueView @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
		
            END 
	
        
    END


```
