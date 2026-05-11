# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_CoChietKhau_Mobile_DoiTruVaTinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-17 11:26:39.247000
- **Ngày sửa cuối**: 2022-12-01 14:57:54.550000

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
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_CoChietKhau_Mobile_DoiTruVaTinhLai]
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
                    INNER JOIN dbo.HopDongChiTiet hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
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
                        EXEC dbo.sp_TC_InsertThucChayDaTinh_CoChietKhau_Mobile_DoiTruVaTinhLai @NgayThucHien,
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
