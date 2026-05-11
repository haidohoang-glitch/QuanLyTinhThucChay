# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_SponsorPost_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-04 16:51:06.453000
- **Ngày sửa cuối**: 2015-04-08 16:04:29.367000

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
--EXEC [ThucChay_ExcInsertThucChayDaTinh_SponsorPost_v2] '2015-03-26','2015-03-26'
--hopdongid 18312: da du tien phan bo
 
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_SponsorPost_v2] 
	@StartDate datetime,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @ProductUnitName NVARCHAR(50),@BannerType INT,
			@TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @HopDongChiTietREF INT,@TypeProduct INT,
			@TongViewThucChay INT, @TongClickThucChay INT;
	set @NgayThucHien = @StartDate
	
	--Xoa du lieu ThucChayDaTinhSponsorPost truoc khi tinh
	DELETE FROM ThucChayDaTinhSponsorPost 
	WHERE NgayThucHien BETWEEN @StartDate AND @EndDate 
    AND DmHinhThucQuangCao <> 13
    
    DELETE FROM ThucChayDaTinh
	WHERE NgayThucHien BETWEEN @StartDate AND @EndDate 
	AND DmSanPhamREF = 381
    AND DmHinhThucQuangCao <> 13
		
	while(@NgayThucHien <= @EndDate)
	Begin
		-- insert du lieu SponsorPost vao bang temp de tinh
		EXEC ThucChay_InsertToTemp_SponsorPost @NgayThucHien
				
		DECLARE Record_Cursor CURSOR FOR 
			SELECT A.SoHopDong,A.DmWebsiteREF, A.TenWebsite,A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,A.BannerType,		
				SUM(A.TongViewThucChay)TongViewThucChay,SUM(A.TongClickThucChay)TongClickThucChay 				
			FROM ThucChay_SponsorPostTemp A 
			WHERE A.NgayThucHien = @NgayThucHien	
			AND A.HopDongChiTietREF in (SELECT distinct tt.HopDongChiTietREF 
			                            FROM ThucChayHopDongChiTiet tt 
											INNER JOIN HopDongChiTiet hdct ON tt.HopDongChiTietREF = hdct.HopDongChiTietID
											INNER JOIN HopDong hd ON hd.HopDongID = tt.HopDongREF 
			                            WHERE tt.DeletedStatus <> 1 AND hdct.DeletedStatus <> 1 
			                            AND hdct.DmSanPhamREF = 381
										AND hdct.DmLoaiREF <> 13
										AND hd.TrangThaiHopDong <> 3)
			GROUP BY A.SoHopDong,A.DmWebsiteREF, A.TenWebsite,A.ProductUnitName,A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,A.BannerType
			HAVING SUM(A.TongClickThucChay)>0		
			ORDER BY A.SoHopDong, A.HopDongChiTietREF,A.TenWebsite
	
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, 
									       @DmWebsiteREF, 
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
									       @DmWebsiteREF, 
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
					
		EXEC [ThucChay_InsertThucChayDaTinh_SponsorPostNoContract] @NgayThucHien 
		
		--XU LY HD HUY
		EXEC [ThucChay_UpdateGiaTriThayDoi_HDHuy] @NgayThucHien, @NgayThucHien
		
		
		set @NgayThucHien = dateadd(d,1,@NgayThucHien)

		
	end 
	
	SELECT '1'
END



```
