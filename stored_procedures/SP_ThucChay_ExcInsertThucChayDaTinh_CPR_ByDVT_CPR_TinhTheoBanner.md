# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR_TinhTheoBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-07 11:08:41.937000
- **Ngày sửa cuối**: 2017-11-07 11:08:52.747000

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
--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR] '2017-06-12','2017-06-12'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR_TinhTheoBanner]
    @StartDate DATETIME
  , @EndDate DATETIME
  , @BannerID INT
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
	
	--Xoa du lieu ThucChayDaTinh truoc khi tinh
        DELETE  FROM ThucChayDaTinh
        WHERE   CONVERT(DATE, NgayThucHien) BETWEEN @StartDate AND @EndDate
                AND DmSanPhamREF IN ( 680, 598 )
                AND DonViTinh = 'CPR'
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
                                AND TypeProduct IN ( 16, 14 )
                                AND DmWebsiteREF != 0
								AND DmBannerREF = @BannerID

		
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
                        WHERE   CONVERT(NVARCHAR(50), NgayThucHien, 103) = CONVERT(NVARCHAR(50), @NgayThucHien, 103)
								AND tcc.bannerid = @BannerID
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
                        EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR_TinhTheoBanner] @NgayThucHien, @HopDongID, @TypeProduct, @DmWebsiteREF, @TenWebsite , @BannerID
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
		--XU LY HD HUY
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
                DELETE  FROM dbo.ThucChayTemp
                DELETE  FROM ThucChayCPRTemp
            END 
	
        SELECT  '1'
    END


--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2014-06-03','2014-06-03'

```
