# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_SponsorPostByHopDongChiTietID_v3`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-01-15 13:38:51.897000
- **Ngày sửa cuối**: 2015-01-15 14:01:00.213000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
| `@Year` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinh_SponsorPostByHopDongChiTietID_v3] 51050,2014
--64983	DT2010914 29004
--65035	DT2010914 29004

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_SponsorPostByHopDongChiTietID_v3] 
	@HopDongChiTietID INT,
	@Year INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @ProductUnitName NVARCHAR(50),@BannerType INT,
			@TenWebsite NVARCHAR(50), @HopDongChiTietREF INT,@TypeProduct INT,
			@TongViewThucChay INT, @TongClickThucChay INT;
	
	--Xoa du lieu ThucChayDaTinhSponsorPost truoc khi tinh
	DELETE FROM ThucChayDaTinhSponsorPost 
	WHERE 
	DmSanPhamREF IN (381)	
	AND HopDongChiTietREF = @HopDongChiTietID	
				
		DECLARE Record_Cursor CURSOR FOR 
			SELECT dbo.ThucChay_FormatSoHopDong(A.SoHopDong) SoHopDong,
				   dbo.ThucChay_FormatDomainName(A.TenWebsite)TenWebsite,A.HopDongChiTietREF,
			A.DmSanPhamREF,A.ProductUnitName,A.BannerType,		
				SUM(A.TongViewThucChay)TongViewThucChay,SUM(A.TongClickThucChay)TongClickThucChay 				
			FROM ThucChay A 
			WHERE Year(A.NgayThucHien) <= @Year
				AND A.TypeProduct = -1					
				AND A.HopDongChiTietREF = @HopDongChiTietID            	
			GROUP BY dbo.ThucChay_FormatSoHopDong(A.SoHopDong),
			    dbo.ThucChay_FormatDomainName(A.TenWebsite),A.ProductUnitName,
				A.HopDongChiTietREF,A.DmSanPhamREF,A.ProductUnitName,A.BannerType
			HAVING SUM(A.TongClickThucChay)>0			
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
				EXEC ThucChay_InsertThucChayDaTinh_SponsorPost
															'2014-12-31',--@NgayThucHien, 
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
	UPDATE ThucChayDaTinhSponsorPost SET TenSanPham = 'Sponsored Post' WHERE DmSanPhamREF = 381
END



```
