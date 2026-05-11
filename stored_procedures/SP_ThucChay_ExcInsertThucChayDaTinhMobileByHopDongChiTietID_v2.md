# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhMobileByHopDongChiTietID_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-22 15:54:32.330000
- **Ngày sửa cuối**: 2015-03-12 18:51:59.093000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@hdct` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--SELECT * FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongChiTietREF = 68870
--INSERT INTO ThucChayDaTinh SELECT * FROM ThucChayDaTinhMobile tcdt WHERE tcdt.HopDongChiTietREF = 68870

--SELECT * FROM ThucChay_MobileTemp tcmt WHERE tcmt.HopDongChiTietREF = 68870
----EXEC [ThucChay_ExcInsertThucChayDaTinhMobileByHopDongChiTietID_v2] '2014-12-25','2015-03-01',70409


CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhMobileByHopDongChiTietID_v2]
	@StartDate DATETIME,
	@EndDate DATETIME,
	@hdct INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME,
	        @Count INT
	
	DECLARE @SoHopDong NVARCHAR(50),
	        @ProductUnitName NVARCHAR(50),
	        @BannerType INT,
	        @TenWebsite NVARCHAR(50),
	        @HopDongChiTietREF INT,
	        @TypeProduct INT,
	        @TongViewThucChay INT,
	        @TongClickThucChay INT;
	SET @NgayThucHien = @StartDate
	
	----Xoa du lieu ThucChayDaTinhMobile truoc khi tinh
	DELETE 
	FROM   ThucChayDaTinhMobile
	WHERE  NgayThucHien BETWEEN @StartDate AND @EndDate 
	       --AND YEAR(NgayThucHien) = 2014
	       AND DmSanPhamREF IN (342)
	       AND HopDongChiTietREF = @hdct  
	
	WHILE (@NgayThucHien <= @EndDate)
	BEGIN
	    -- insert du lieu mobile vao bang temp de tinh
	    EXEC ThucChay_InsertToTemp_MobileByHopDongChiTietID @NgayThucHien,
	         @hdct
	    
	    DECLARE Record_Cursor CURSOR  
	    FOR
	        SELECT A.SoHopDong,
	               A.TenWebsite,
	               A.HopDongChiTietREF,
	               A.TypeProduct,
	               A.ProductUnitName,
	               A.BannerType,
	               SUM(A.TongViewThucChay)TongViewThucChay,
	               SUM(A.TongClickThucChay)TongClickThucChay
	        FROM   ThucChay_MobileTemp A
	        WHERE  A.NgayThucHien = @NgayThucHien
	               AND TypeProduct = 10
	               --AND A.HopDongChiTietREF IN (SELECT DISTINCT tt.HopDongChiTietREF
	               --                            FROM   ThucChayHopDongChiTiet tt
	               --                                   INNER JOIN HopDongChiTiet 
	               --                                        hdct
	               --                                        ON  tt.HopDongChiTietREF = 
	               --                                            hdct.HopDongChiTietID
	               --                            WHERE  tt.DeletedStatus <> 1
	               --                                   AND hdct.DeletedStatus <> 
	               --                                       1
	               --                                   AND hdct.DmSanPhamREF = 
	               --                                       342)
	               AND A.HopDongChiTietREF = @hdct
	        GROUP BY
	               A.SoHopDong,
	               A.TenWebsite,
	               A.ProductUnitName,
	               A.HopDongChiTietREF,
	               A.TypeProduct,
	               A.ProductUnitName,
	               A.BannerType
	        ORDER BY
	               A.SoHopDong,
	               A.HopDongChiTietREF,
	               A.TenWebsite
	    
	    OPEN Record_Cursor
	    
	    -- Perform the first fetch.
	    FETCH NEXT FROM Record_Cursor INTO @SoHopDong, 
	    @TenWebsite,
	    @HopDongChiTietREF,
	    @TypeProduct, 
	    @ProductUnitName,
	    @BannerType,
	    @TongViewThucChay, 
	    @TongClickThucChay			
	    WHILE @@FETCH_STATUS = 0
	    BEGIN
	        EXEC ThucChay_InsertThucChayDaTinh_Mobile
	             @NgayThucHien,
	             @SoHopDong,
	             @TenWebsite,
	             @HopDongChiTietREF,
	             @TypeProduct,
	             @ProductUnitName,
	             @BannerType,
	             @TongViewThucChay,
	             @TongClickThucChay
	        
	        FETCH NEXT FROM Record_Cursor INTO @SoHopDong, 
	        @TenWebsite,
	        @HopDongChiTietREF,
	        @TypeProduct,
	        @ProductUnitName,
	        @BannerType,
	        @TongViewThucChay, 
	        @TongClickThucChay
	    END
	    
	    CLOSE Record_Cursor
	    DEALLOCATE Record_Cursor
	    
	    SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
	        --delete from dbo.ThucChay_MobileTemp
	END 
	
	SELECT '1'
END



```
