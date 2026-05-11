# Stored Procedure: `sp_TC_ExcInsertThucChayDaTinh_Single_Mobile_TinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-27 14:58:55.880000
- **Ngày sửa cuối**: 2017-07-05 17:42:55.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmWebsiteID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayTinhThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
exec [dbo].[sp_TC_ExcInsertThucChayDaTinh_Single_Mobile] 519390, '2017-06-03', 'QC0190617', 105

EXEC sp_TC_ExcInsertThucChayDaTinh_Single_Mobile_TinhLai 519229,'2017-06-01 00:00:00.000', 'SH0050617', 79, 109964, '2017-07-03 00:00:00.000'
*/
CREATE PROCEDURE [dbo].[sp_TC_ExcInsertThucChayDaTinh_Single_Mobile_TinhLai]
	-- Add the parameters for the stored procedure here
    @DmBannerID INT ,
    @NgayThucHien DATETIME ,
    @SoHopDong NVARCHAR(50) ,
    @DmWebsiteID INT ,
    @HopDongChiTietID INT,
	@NgayTinhThucHien DATETIME
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
			

	
        DECLARE Record_CursorSM CURSOR
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
            FROM    ThucChay_MobileTemp A
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
	
        OPEN Record_CursorSM

		-- Perform the first fetch.
        FETCH NEXT FROM Record_CursorSM INTO @SoHopDong, @TenWebsite,
            @HopDongChiTietREF, @TypeProduct, @ProductUnitName, @BannerType,
            @DmBannerREF, @TongViewThucChay, @TongClickThucChay
								
        WHILE @@FETCH_STATUS = 0
            BEGIN			
					
																				  			
                EXEC sp_TC_InsertThucChayDaTinh_Mobile_TinhLai @NgayThucHien,
                    @SoHopDong, @TenWebsite, @HopDongChiTietREF, @TypeProduct,
                    @ProductUnitName, @BannerType, @DmBannerREF,
                    @TongViewThucChay, @TongClickThucChay, @NgayTinhThucHien
					
																								
                FETCH NEXT FROM Record_CursorSM INTO @SoHopDong, @TenWebsite,
                    @HopDongChiTietREF, @TypeProduct, @ProductUnitName,
                    @BannerType, @DmBannerREF, @TongViewThucChay,
                    @TongClickThucChay
            END

        CLOSE Record_CursorSM
        DEALLOCATE Record_CursorSM

			 
               
               
        


	
			 
			
    END

```
