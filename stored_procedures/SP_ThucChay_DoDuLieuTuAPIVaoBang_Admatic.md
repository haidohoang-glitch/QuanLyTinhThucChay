# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-22 10:40:27.123000
- **Ngày sửa cuối**: 2017-11-22 15:12:32.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--EXEC [dbo].[job_UpdateThucChayHopDongChiTiet_ChiPhiKhac]
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Admatic] 
-- Add the parameters for the stored procedure here
    @ID INT
  , @NgayThucHien DATETIME
AS
    BEGIN

        IF @NgayThucHien IS NULL
            BEGIN
                SET @NgayThucHien = DATEADD(dd, -1, GETDATE())	

                SET @NgayThucHien = CONVERT(DATE, @NgayThucHien)
            END
        

        DECLARE @Count INT= 0
        DECLARE @slsite INT = 0
        DECLARE @v_TenWebsite NVARCHAR(1000)

	
        IF NOT EXISTS ( SELECT  *
                        FROM    dbo.ThucChay
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND TypeProduct = @ID
                                AND CreatedBy LIKE N'From API_Admatic' )
            BEGIN

                SET @Count = 0
                SET @slsite = 0
                SET @v_TenWebsite = ''

                SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
                                FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](TenWebsite) DmWebsiteREF
                                                  , TenWebsite
                                          FROM      dbo.DataThucChay_Admatic
                                          WHERE     CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                    AND TypeProduct = @ID
                                        ) a
                                WHERE   a.DmWebsiteREF IS NULL
                              )
                IF ( @slsite > 0 )
                    WHILE @Count < @slsite
                        BEGIN
                            SET @v_TenWebsite = ( SELECT TOP 1
                                                            TenWebsite
                                                  FROM      ( SELECT    [dbo].[GetWebsiteIDByDomainName](TenWebsite) DmWebsiteREF
                                                                      , TenWebsite
                                                              FROM      dbo.DataThucChay_Admatic
                                                              WHERE     CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                                                        AND TypeProduct = @ID
                                                            ) a
                                                  WHERE     a.DmWebsiteREF IS NULL
                                                )
									
                            IF @v_TenWebsite IS NOT NULL
                                BEGIN
                                    INSERT  INTO dbo.DmWebsiteReportingdb
                                            ( TenWebsite
                                            , CreatedBy
                                            , CreatedAt
                                            , LastModifiedBy
                                            , LastModifiedAt
                                            , DeletedStatus
                                            , PrintStatus
                                            , RecordStatus
                                            , ID
													
                                            )
                                    VALUES  ( @v_TenWebsite
                                            ,	-- TenWebsite - nvarchar(200)
                                              N'asd'
                                            ,	-- CreatedBy - nvarchar(50)
                                              GETDATE()
                                            ,	-- CreatedAt - datetime
                                              N'asd'
                                            ,	-- LastModifiedBy - nvarchar(50)
                                              GETDATE()
                                            ,	-- LastModifiedAt - datetime
                                              0
                                            ,	-- DeletedStatus - int
                                              0
                                            ,	-- PrintStatus - int
                                              0
                                            ,	-- RecordStatus - int
                                              N'New' -- ID - nvarchar(50)
													
                                            )	
                                END
                                    

                            SET @Count = @Count + 1
                        END


                INSERT  INTO dbo.ThucChay
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
                              , ISNULL([dbo].[GetWebsiteIDByDomainName](TenWebsite), 0)
                              , TenWebsite
                              , DmChienDichREF
                              , TenChienDich
                              , DmBannerREF
                              , TenBanner
                              , NgayThucHien
                              , TongViewThucChay
                              , TongClickThucChay
                              , N'From API_Admatic'
                              , createdAt
                              , N'From API_Admatic'
                              , createdAt
                              , ISNULL(DeletedStatus, 0)
                              , ISNULL(PrintStatus, 0)
                              , ISNULL(RecordStatus, 0)
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
                              , CASE WHEN IsNoiBo = N'True' THEN 1
                                     WHEN IsNoiBo = N'False' THEN 0
                                     ELSE NULL
                                END
                        FROM    dbo.DataThucChay_Admatic
                        WHERE   CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND TypeProduct = @ID
            END
            

  
  


    END




```
