# Stored Procedure: `Rpt_InsertNhanHang_ThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:33.973000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.803000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHang_ThucChay]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate
	WHILE (@NgayThucHien <= @EndDate)
	BEGIN
		--1. Tinh gia tri thuc chay cho tung nhan
		DELETE FROM RptNhanHangThucChay
		WHERE CONVERT(DATE,NgayThucHien) = @NgayThucHien
		
		EXEC [dbo].[Rpt_InsertNhanHangThucChay]	@NgayThucHien
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
	END
END

--EXEC [dbo].[Rpt_InsertNhanHang_ThucChay] '2013-01-01', '2014-02-10'

```
