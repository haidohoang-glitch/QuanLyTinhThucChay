# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_CPR_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-09-14 14:36:24.977000
- **Ngày sửa cuối**: 2015-09-14 14:36:24.977000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPR_BySoHopDong] 'QC1223333',680,'2015-08-14','2015-08-14'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPR_BySoHopDong]
	@SoHopDong NVARCHAR(100),
	@DmSanPhamREF INT, 
	@StartDate datetime,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE  @TypeProduct INT
			, @TenWebsite NVARCHAR(50)
			, @DmWebsiteREF INT
			
	set @NgayThucHien = @StartDate
	delete from dbo.ThucChayTemp
	
	--Xoa du lieu ThucChayDaTinh truoc khi tinh
	DELETE FROM ThucChayDaTinh
	WHERE 1=1
	AND DmSanPhamREF = @DmSanPhamREF 
	AND convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
	AND SoHopDong = @SoHopDong
	
	DELETE FROM ThucChayCPRTemp
	
	DELETE FROM dbo.ThucChayTemp
	
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN

		Insert into dbo.ThucChayTemp
		select * from ThucChay 
		where Convert(nvarchar(50),NgayThucHien,103) = Convert(nvarchar(50),@NgayThucHien,103)
		AND TypeProduct = @TypeProduct
		AND SoHopDong = @SoHopDong
		AND DmWebsiteREF != 0
		
		INSERT INTO ThucChayCPRTemp
		SELECT * FROM ThucChayCPR tcc
		where Convert(nvarchar(50),NgayThucHien,103) = Convert(nvarchar(50),@NgayThucHien,103)
		AND TypeProduct = @TypeProduct
				
		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong,A.TypeProduct,A.DmWebsiteREF, A.TenWebsite 
		  FROM
			(
				SELECT tct.SoHopDong,tct.TypeProduct, tct.DmWebsiteREF, tct.TenWebsite
				FROM ThucChayTemp tct
			)A
		WHERE A.SoHopDong = @SoHopDong
		ORDER BY A.SoHopDong, A.TypeProduct	
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				EXEC [ThucChay_InsertThucChayDaTinh_CPR] @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		set @NgayThucHien = dateadd(d,1,@NgayThucHien)
		delete from dbo.ThucChayTemp
		DELETE FROM ThucChayCPRTemp
	end 
	
	SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2014-06-03','2014-06-03'

```
