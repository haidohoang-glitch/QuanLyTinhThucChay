# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhTrueView_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-08-22 15:33:13.450000
- **Ngày sửa cuối**: 2023-08-22 16:00:09.467000

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

--EXEC [ThucChay_ExcInsertThucChayDaTinhTrueView_dev] '2023-08-21','2023-08-21'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhTrueView_dev]
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
	
		----Xoa du lieu ThucChayDaTinh truoc khi tinh
  --      DELETE  FROM ThucChayDaTinh
  --      WHERE   CONVERT(DATE, NgayThucHien) BETWEEN @StartDate AND @EndDate
  --              AND DmSanPhamREF IN ( 240 )
  --              AND (DonViTinh = N'True View' OR DonViTinh = N'TRUE REACH')
  --              AND DmHinhThucQuangCao <> 42
	
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
						AND  tcc.SoHopDong = N'QC2940823'
                
				SELECT * FROM dbo.ThucChayTrueViewTemp

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
						PRINT 'TINH THUC CHAY'
						PRINT @SoHopDong
                        --EXEC ThucChay_InsertThucChayDaTinhTrueView @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor
		
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
		
            END 
	
        
    END


```
