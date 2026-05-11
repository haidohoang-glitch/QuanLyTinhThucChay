# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhSponsorSingle`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-01 15:43:28.557000
- **Ngày sửa cuối**: 2015-04-02 14:28:57.063000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhSponsorSingle]
	-- Add the parameters for the stored procedure here
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @SoHopDong NVARCHAR(50), @ProductUnitName NVARCHAR(50),@BannerType INT,
			@TenWebsite NVARCHAR(50), @HopDongChiTietREF INT, @TypeProduct INT,
			@TongViewThucChay INT, @TongClickThucChay INT;
			
	--Delete truoc khi tinh
	DELETE FROM ThucChayDaTinhSponsorPost
	WHERE HopDongChiTietREF = @HopDongChiTietID AND DmSanPhamREF = 381 AND NgayThucHien = @NgayThucHien
	
	DECLARE Record_Cursor CURSOR FOR 
			SELECT A.SoHopDong, A.TenWebsite, A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,A.BannerType,		
			ISNULL(SUM(A.TongViewThucChay),0) TongViewThucChay,
			ISNULL(SUM(A.TongClickThucChay),0) TongClickThucChay 				
			FROM ThucChay_SponsorTemp A 
			WHERE 1=1 
			and A.NgayThucHien = @NgayThucHien			
			AND A.HopDongChiTietREF = @HopDongChiTietID							 								            	
			GROUP BY A.SoHopDong,  A.TenWebsite,  A.ProductUnitName,A.HopDongChiTietREF,A.TypeProduct,A.ProductUnitName,A.BannerType
			ORDER BY A.TenWebsite
	
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
			 
			
END

```
