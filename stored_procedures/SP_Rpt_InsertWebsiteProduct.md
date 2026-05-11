# Stored Procedure: `Rpt_InsertWebsiteProduct`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-16 15:14:00.290000
- **Ngày sửa cuối**: 2014-11-19 12:17:55.177000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC Rpt_InsertWebsiteProduct '2014-01-01', '2014-10-10'
CREATE PROCEDURE [dbo].[Rpt_InsertWebsiteProduct]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate
	WHILE (@NgayThucHien <= @EndDate)
	BEGIN
		--Delete du lieu
		DELETE FROM rptWebsiteProduct
		WHERE NgayThucHien = @NgayThucHien
		
		EXEC Rpt_InsertWebsiteProductByNgayThucHien	@NgayThucHien
		
		PRINT @NgayThucHien
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
	END
END

--EXEC [dbo].[Rpt_InsertWebsiteProduct] '2013-01-01', '2013-03-01'

```
