# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhMobile_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-23 09:53:40.173000
- **Ngày sửa cuối**: 2015-05-06 17:29:58.930000

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
--EXEC [ThucChay_ExcInsertThucChayDaTinhMobile_v3] '2015-01-01','2015-02-25',68364


CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhMobile_v2] 
	@StartDate datetime,
	@EndDate DATETIME
	
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @ProductUnitName NVARCHAR(50),@BannerType INT,
			@TenWebsite NVARCHAR(50), @HopDongChiTietREF INT, @TypeProduct INT,
			@TongViewThucChay INT, @TongClickThucChay INT;
	set @NgayThucHien = @StartDate
	
	--Xoa du lieu ThucChayDaTinhMobile truoc khi tinh
	DELETE FROM ThucChayDaTinhMobile WHERE NgayThucHien BETWEEN @StartDate AND @EndDate AND DmSanPhamREF = 342
	AND DmHinhThucQuangCao <> 13
	DELETE FROM ThucChayDaTinh WHERE NgayThucHien BETWEEN @StartDate AND @EndDate AND DmSanPhamREF = 342
	AND DmHinhThucQuangCao <> 13
		
	while(@NgayThucHien <= @EndDate)
	Begin
		-- insert du lieu mobile vao bang temp de tinh
		EXEC ThucChay_InsertToTemp_Mobile @NgayThucHien
				
		DECLARE Record_Cursor CURSOR FOR 
			SELECT A.SoHopDong,
			 A.TenWebsite,
			 A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,A.BannerType,		
			ISNULL(SUM(A.TongViewThucChay),0) TongViewThucChay,
			ISNULL(SUM(A.TongClickThucChay),0) TongClickThucChay 				
			FROM ThucChay_MobileTemp A 
			WHERE 1=1 
			and A.NgayThucHien = @NgayThucHien
			
			AND A.HopDongChiTietREF NOT IN (0,1) AND A.HopDongChiTietREF IS NOT NULL
				--AND A.TypeProduct = 10					
				--AND A.HopDongChiTietREF IN (SELECT distinct tt.HopDongChiTietREF 
				--                            FROM ThucChayHopDongChiTiet tt INNER JOIN HopDongChiTiet hdct ON tt.HopDongChiTietREF = hdct.HopDongChiTietID 
				--                            WHERE tt.DeletedStatus <> 1
				--                            AND hdct.DeletedStatus <> 1 
				--                            AND hdct.DmSanPhamREF = 342
				--                            AND hdct.DmLoaiREF <> 13
				--							AND Hopdongfk IN (SELECT HopDongID
				--							                    FROM hopdong WHERE TrangThaiHopDong <> 3))
				 								            	
			GROUP BY A.SoHopDong, 
			 A.TenWebsite,
			 A.ProductUnitName,A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,A.BannerType
			ORDER BY A.SoHopDong,
			 A.HopDongChiTietREF, A.TenWebsite
	
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, 
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
			FETCH NEXT FROM Record_Cursor into @SoHopDong, 
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
					
		EXEC [ThucChay_InsertThucChayDaTinh_MobileNoContract] @NgayThucHien 
		
		-- Update Gia tri thay doi thuc chay Mobile
		EXEC dbo.ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi_v2 @NgayThucHien, @NgayThucHien			
		
	
		--Insert gia tri vao bang ThucChayDaTinh
		DELETE FROM ThucChayDaTinh WHERE DmSanPhamREF = 342 AND NgayThucHien = @NgayThucHien
		AND DmHinhThucQuangCao <> 13
		INSERT INTO ThucChayDaTinh
		SELECT * FROM ThucChayDaTinhMobile WHERE DmSanPhamREF = 342 AND NgayThucHien = @NgayThucHien
		AND DmHinhThucQuangCao <> 13
		
		set @NgayThucHien = dateadd(d,1,@NgayThucHien)
		--delete from dbo.ThucChay_MobileTemp
		
	end 
	
	SELECT '1'
END



```
