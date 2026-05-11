# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_SponsorPost_v3`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-01-08 14:06:07.200000
- **Ngày sửa cuối**: 2015-02-25 16:37:09.763000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Year` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinh_SponsorPost_v3] '2014-01-01','2014-11-04'
--hopdongid 18312: da du tien phan bo
 
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_SponsorPost_v3] 
@Year INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @ProductUnitName NVARCHAR(50),@BannerType INT,
			@TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @HopDongChiTietREF INT,@TypeProduct INT,
			@TongViewThucChay INT, @TongClickThucChay INT;

	
	--Xoa du lieu ThucChayDaTinhSponsorPost truoc khi tinh
	--DELETE FROM ThucChayDaTinhSponsorPost 
	--WHERE 
	--DmSanPhamREF = 381 and DmHinhThucQuangCao <> 13
 --   AND YEAR(NgayThucHien) = 2014
		
	EXEC ThucChay_InsertToTemp_SponsorPost @NgayThucHien
				
		DECLARE Record_Cursor CURSOR FOR 
			SELECT A.SoHopDong,A.DmWebsiteREF, A.TenWebsite,A.HopDongChiTietREF,A.DmSanPhamREF,A.ProductUnitName,A.BannerType,		
				SUM(A.TongViewThucChay)TongViewThucChay,SUM(A.TongClickThucChay)TongClickThucChay 				
			FROM ThucChay_SponsorPostTemp A 
			WHERE year(A.NgayThucHien) = @Year	
			AND A.TypeProduct = -1
			AND A.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
			                            FROM HopDong hd 
			                             INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK 
			                            WHERE hdct.DeletedStatus <> 1 
											AND DmSanPhamREF = 381
											AND hd.TrangThaiHopDong <> 3)
			GROUP BY A.SoHopDong,A.DmWebsiteREF, A.TenWebsite,A.ProductUnitName,A.HopDongChiTietREF,A.DmSanPhamREF,A.ProductUnitName,A.BannerType
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
															@DmWebsiteREF, 
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
					

	SELECT '1'
END



```
