# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhCPV_TinhTheoBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-07 10:58:07.807000
- **Ngày sửa cuối**: 2017-11-07 10:58:07.807000

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

--EXEC [ThucChay_ExcInsertThucChayDaTinhCPV] '2014-10-01','2014-10-01'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhCPV_TinhTheoBanner]
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
	
        DELETE  FROM dbo.ThucChayTemp
        DELETE  FROM dbo.ThucChayCPVTemp
	
	--Xoa du lieu ThucChayDaTinh truoc khi tinh
        DELETE  FROM ThucChayDaTinh
        WHERE   CONVERT(DATE, NgayThucHien) BETWEEN @StartDate AND @EndDate
                AND DmSanPhamREF IN ( 240 )
                AND DonViTinh = 'CPV' --Đơn vị của hình thức CPV	
				AND DmBannerREF = @BannerID
	
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN
                DELETE  FROM dbo.ThucChayTemp
                DELETE  FROM dbo.ThucChayCPVTemp
		
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
                        WHERE   CONVERT(DATE, tcc.NgayThucHien) = @NgayThucHien
								AND tcc.bannerid = @BannerID
		
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
                    FROM    ( SELECT    tct.SoHopDong
                                      , tct.TypeProduct
                                      , tct.DmWebsiteREF
                                      , tct.TenWebsite
                                      , tct.DmBannerREF
                              FROM      ThucChayTemp tct
                                        INNER JOIN ThucChayCPVTemp tcc ON tct.DmBannerREF = tcc.bannerid
                                                                          AND tct.NgayThucHien = tcc.NgayThucHien
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
                        EXEC ThucChay_InsertThucChayDaTinhCPV_TinhTheoBanner @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
		--delete from dbo.ThucChayTemp
            END 
	
        SELECT  '1'
    END


--EXEC [ThucChay_ExcInsertThucChayDaTinhCPV] '2014-08-12','2014-08-13'

```
