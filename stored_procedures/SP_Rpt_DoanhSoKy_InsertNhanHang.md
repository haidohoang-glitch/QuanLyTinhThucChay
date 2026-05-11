# Stored Procedure: `Rpt_DoanhSoKy_InsertNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-24 09:45:03.470000
- **Ngày sửa cuối**: 2014-12-24 11:09:52.067000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[Rpt_DoanhSoKy_InsertNhanHang] '2013-01-01', '2014-12-24'
CREATE  PROCEDURE [dbo].[Rpt_DoanhSoKy_InsertNhanHang]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate
	WHILE (@NgayThucHien <= @EndDate)
	BEGIN
		--1. Tinh gia tri cho table RptNhanHangThongTinChiTiet
		EXEC [Rpt_Insert_Ky_NhanHangThongTinChiTiet] @NgayThucHien
	
		PRINT @NgayThucHien
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
	END
END


```
