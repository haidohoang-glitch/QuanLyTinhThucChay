# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_CoChietKhau_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-23 17:54:17.920000
- **Ngày sửa cuối**: 2023-09-22 15:44:45.133000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmWebsiteID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[sp_TC_ExcInsertThucChayDaTinh_CoChietKhau_Mobile]
	-- Add the parameters for the stored procedure here
    @DmBannerID INT ,
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @DmWebsiteID INT 
*/
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_CoChietKhau_Mobile]
	-- Add the parameters for the stored procedure here
    @DmBannerID INT ,
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @DmWebsiteID INT 
AS
    BEGIN
        DECLARE @ProductUnitName NVARCHAR(50) ,
            @BannerType INT ,
            @TenWebsite NVARCHAR(50) ,
            @HopDongChiTietREF INT ,
            @TypeProduct INT ,
            @TongViewThucChay INT ,
            @TongClickThucChay INT ,
            @DmBannerREF INT



        DECLARE @HopDongChiTietID INT
		
        DECLARE icursor CURSOR
        FOR
            SELECT DISTINCT
                    hdct.HopDongChiTietID
            FROM    dbo.ThucChayHopDongChiTietAndBanner tc
                    INNER JOIN (SELECT * FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 AND DonViTinhREF <> 3) hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
                    INNER JOIN dbo.HopDong hd ON tc.HopDongREF = hd.HopDongID
            WHERE   CONVERT(NVARCHAR(50), tc.DmBannerID) = CONVERT(NVARCHAR(50), @DmBannerID)
                    AND hd.SoHopDong = @SoHopDong
					AND tc.DeletedStatus = 0
            ORDER BY hdct.HopDongChiTietID
		
        OPEN icursor  
		
        FETCH NEXT FROM icursor   
		INTO @HopDongChiTietID
		
        WHILE @@FETCH_STATUS = 0
            BEGIN  
		    
                DECLARE Record_Cursor CURSOR
                FOR
                    SELECT  A.SoHopDong ,
                            A.TenWebsite ,
                            @HopDongChiTietID ,
                            A.TypeProduct ,
                            A.ProductUnitName ,
                            A.BannerType ,
                            A.DmBannerREF ,
                            ISNULL(SUM(A.TongViewThucChay), 0) TongViewThucChay ,
                            ISNULL(SUM(A.TongClickThucChay), 0) TongClickThucChay
                    FROM    dbo.ThucChay_MobileTemp A
                    WHERE   1 = 1
                            AND A.NgayThucHien = @NgayThucHien
                            AND A.DmBannerREF = @DmBannerID
                            AND A.SoHopDong = @SoHopDong
                            AND A.DmWebsiteREF = @DmWebsiteID
                    GROUP BY A.SoHopDong ,
                            A.TenWebsite ,
                            A.ProductUnitName ,
                            A.HopDongChiTietREF ,
                            A.TypeProduct ,
                            A.ProductUnitName ,
                            A.BannerType ,
                            A.DmBannerREF
	
                OPEN Record_Cursor

		-- Perform the first fetch.
                FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TenWebsite,
                    @HopDongChiTietREF, @TypeProduct, @ProductUnitName,
                    @BannerType, @DmBannerREF, @TongViewThucChay,
                    @TongClickThucChay			
                WHILE @@FETCH_STATUS = 0
                    BEGIN		
						--PRINT  @SoHopDong
						--PRINT @TenWebsite
						--PRINT CONVERT(NVARCHAR(50),@HopDongChiTietREF)
      --                  PRINT CONVERT(NVARCHAR(50),@TypeProduct)   
						--PRINT @ProductUnitName
						--PRINT CONVERT(NVARCHAR(50),@BannerType)
						--PRINT CONVERT(NVARCHAR(50),@DmBannerREF)
						--PRINT CONVERT(NVARCHAR(50),@TongViewThucChay)
						--PRINT CONVERT(NVARCHAR(50),@TongClickThucChay)
						                            															  			
                        EXEC sp_TC_InsertThucChayDaTinh_CoChietKhau_Mobile @NgayThucHien,
                            @SoHopDong, @TenWebsite, @HopDongChiTietREF,
                            @TypeProduct, @ProductUnitName, @BannerType,
                            @DmBannerREF, @TongViewThucChay,
                            @TongClickThucChay	
					
																								
                        FETCH NEXT FROM Record_Cursor INTO @SoHopDong,
                            @TenWebsite, @HopDongChiTietREF, @TypeProduct,
                            @ProductUnitName, @BannerType, @DmBannerREF,
                            @TongViewThucChay, @TongClickThucChay
                    END

                CLOSE Record_Cursor
                DEALLOCATE Record_Cursor

			 
                FETCH NEXT FROM icursor   
		    INTO @HopDongChiTietID 
            END   
        CLOSE icursor;  
        DEALLOCATE icursor;  


			
	
			 
			
    END

```
