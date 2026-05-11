# Stored Procedure: `Rpt_InsertNhanHang_ThucChayFullCPC`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:32.787000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.797000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHang_ThucChayFullCPC]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate
	WHILE (@NgayThucHien <= @EndDate)
	BEGIN
		--1. Tinh gia tri thuc chay cho tung nhan
		DELETE FROM RptNhanHangThucChayFull
		WHERE CONVERT(DATE,NgayThucHien) = @NgayThucHien
		AND DmSanPhamREF IN (144,299,337)
		
		EXEC [dbo].[Rpt_InsertNhanHangThucChayFullCPC]	@NgayThucHien
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
		PRINT @NgayThucHien	
	END
END

--EXEC [dbo].[Rpt_InsertNhanHang_ThucChayFullCPC] '2013-01-01', '2014-02-10'

```
