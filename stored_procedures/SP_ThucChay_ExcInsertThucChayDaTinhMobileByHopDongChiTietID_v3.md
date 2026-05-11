# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhMobileByHopDongChiTietID_v3`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-01-09 12:06:40.087000
- **Ngày sửa cuối**: 2015-03-03 17:30:33.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@year` | `int(4)` | No |
| `@hdct` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--SELECT * FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongChiTietREF = 68870
--INSERT INTO ThucChayDaTinh SELECT * FROM ThucChayDaTinhMobile tcdt WHERE tcdt.HopDongChiTietREF = 68870

--SELECT * FROM ThucChay_MobileTemp tcmt WHERE tcmt.HopDongChiTietREF = 51001
----EXEC [ThucChay_ExcInsertThucChayDaTinhMobileByHopDongChiTietID_v3] 2014,54902,'2014-12-31'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhMobileByHopDongChiTietID_v3] 
	@year INT,
	@hdct INT,
	@NgayThucHien DATETIME
	
AS
BEGIN
	DECLARE @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @ProductUnitName NVARCHAR(50),@BannerType INT,
			@TenWebsite NVARCHAR(50), @HopDongChiTietREF INT,@TypeProduct INT,
			@TongViewThucChay INT, @TongClickThucChay INT;
	
	
	----Xoa du lieu ThucChayDaTinhMobile truoc khi tinh
	DELETE FROM ThucChayDaTinhMobile 
	WHERE 
	DmSanPhamREF IN (342)
	 AND HopDongChiTietREF = @hdct
    AND YEAR(NgayThucHien) = @year
		
	
				
		DECLARE Record_Cursor CURSOR FOR 
			SELECT dbo.ThucChay_FormatSoHopDong(A.SoHopDong),
			dbo.ThucChay_FormatDomainName(A.TenWebsite)TenWebsite,A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,
			A.BannerType,		
				SUM(A.TongViewThucChay)TongViewThucChay,SUM(A.TongClickThucChay)TongClickThucChay 				
			FROM ThucChay A 
			WHERE 1=1 
			and TypeProduct =10
			AND YEAR(NgayThucHien)= @year									
				AND A.HopDongChiTietREF = @hdct
				--AND A.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
				--                              FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hdct.HopDongFK = hd.HopDongID
				--                            WHERE hdct.DeletedStatus <> 1
				--							AND hd.TrangThaiHopDong <> 3
				--							AND hdct.DmSanPhamREF = 342)	
                           	
			GROUP BY dbo.ThucChay_FormatSoHopDong(A.SoHopDong),dbo.ThucChay_FormatDomainName(A.TenWebsite),A.ProductUnitName
			,A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,A.BannerType
			ORDER BY dbo.ThucChay_FormatSoHopDong(A.SoHopDong), A.HopDongChiTietREF,dbo.ThucChay_FormatDomainName(A.TenWebsite)
	
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
					

	
	SELECT '1'
END



```
