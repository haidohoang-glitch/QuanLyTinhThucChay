# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_TinhTheoBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-31 14:32:43.950000
- **Ngày sửa cuối**: 2017-11-07 10:56:54.630000

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


CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_TinhTheoBanner]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @BannerID INT
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

	--Xoa du lieu ThucChayDaTinh truoc khi tinh
        DELETE  FROM ThucChayDaTinh
        WHERE   CONVERT(DATE, NgayThucHien) BETWEEN @StartDate AND @EndDate
                AND DmSanPhamREF IN ( 231, 238, 339, 240, 598, 613, 370, 680, 735 )
                AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	 --Đơn vị của hình thức CPM, TRUE REACH
                AND NOT ( DmLoaiBannerREF IN ( 17, 18 )
                          OR DmHinhThucQuangCao IN ( 13, 42 )
                        )
				AND DmBannerREF = @BannerID


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
                                AND TypeProduct NOT IN ( 1, 2, 17 )
                                AND DmWebsiteREF != 0
								AND DmBannerREF = @BannerID


                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT DISTINCT
                            A.SoHopDong
                          , A.TypeProduct
                          , A.DmWebsiteREF
                          , A.TenWebsite
                          , A.DmBannerREF
                          , A.HDLechGiaYN
                    FROM    ( SELECT    tct.SoHopDong
                                      , tct.TypeProduct
                                      , tct.DmWebsiteREF
                                      , tct.TenWebsite
                                      , tct.DmBannerREF
                                      , 'Y' HDLechGiaYN
                              FROM      ThucChayTemp tct
                            ) A
                    ORDER BY A.SoHopDong
                          , A.TypeProduct	
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
			
                WHILE @@FETCH_STATUS = 0
                    BEGIN
                        IF ( @HDLechGiaYN = 'Y' )
                            BEGIN
                                EXEC ThucChay_InsertThucChayDaTinh_TinhTheoBanner @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
					
                            END
			
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
                TRUNCATE TABLE dbo.ThucChayTemp
            END 
	
    END


--EXEC [ThucChay_ExcInsertThucChayDaTinh] '2014-06-03','2014-06-03'

```
