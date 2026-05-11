# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_SponsorPostByHopDongChiTietID_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-04 17:21:25.760000
- **Ngày sửa cuối**: 2015-03-28 09:48:59.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinh_SponsorPostByHopDongChiTietID_v2] '2015-01-30','2015-02-14',72523
--64983	DT2010914 29004
--65035	DT2010914 29004

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_SponsorPostByHopDongChiTietID_v2] 
	@StartDate datetime,
	@EndDate DATETIME,
	@HopDongChiTietID INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @ProductUnitName NVARCHAR(50),@BannerType INT,
			@TenWebsite NVARCHAR(50), @HopDongChiTietREF INT,@TypeProduct INT,
			@TongViewThucChay INT, @TongClickThucChay INT;
	set @NgayThucHien = @StartDate
	
	--Xoa du lieu ThucChayDaTinhSponsorPost truoc khi tinh
	DELETE FROM ThucChayDaTinhSponsorPost 
	WHERE NgayThucHien BETWEEN @StartDate AND @EndDate 
	AND 
	DmSanPhamREF IN (381)
	AND HopDongChiTietREF = @HopDongChiTietID	
		
	while(@NgayThucHien <= @EndDate)
	Begin
		-- insert du lieu SponsorPost vao bang temp de tinh
		EXEC ThucChay_InsertToTemp_SponsorPostByHopDongChiTietID @NgayThucHien,@HopDongChiTietID
				
		DECLARE Record_Cursor CURSOR FOR 
			SELECT A.SoHopDong,A.TenWebsite,A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,A.BannerType,		
				SUM(A.TongViewThucChay)TongViewThucChay,SUM(A.TongClickThucChay)TongClickThucChay 				
			FROM ThucChay_SponsorPostTemp A 
			WHERE A.NgayThucHien =@NgayThucHien	
				AND A.HopDongChiTietREF in (SELECT distinct tt.HopDongChiTietREF 
			                            FROM ThucChayHopDongChiTiet tt 
											INNER JOIN HopDongChiTiet hdct ON tt.HopDongChiTietREF = hdct.HopDongChiTietID
											INNER JOIN HopDong hd ON hd.HopDongID = tt.HopDongREF 
			                            WHERE tt.DeletedStatus <> 1 AND hdct.DeletedStatus <> 1 
			                            AND hdct.DmSanPhamREF = 381
										AND hdct.DmLoaiREF <> 13
										AND hd.TrangThaiHopDong <> 3)
				AND A.HopDongChiTietREF = @HopDongChiTietID            	
			GROUP BY A.SoHopDong,A.TenWebsite,A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,A.BannerType
			HAVING SUM(A.TongClickThucChay)>0			
			ORDER BY A.SoHopDong, A.HopDongChiTietREF,A.TenWebsite
	
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
				EXEC ThucChay_InsertThucChayDaTinh_SponsorPost
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
							
		set @NgayThucHien = dateadd(d,1,@NgayThucHien)

		
	end 
	
	SELECT '1'
	UPDATE ThucChayDaTinhSponsorPost SET TenSanPham = 'Sponsored Post' WHERE DmSanPhamREF = 381
END



```
