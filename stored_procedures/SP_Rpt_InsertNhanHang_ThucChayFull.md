# Stored Procedure: `Rpt_InsertNhanHang_ThucChayFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:35.573000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.800000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHang_ThucChayFull]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate
	WHILE (@NgayThucHien <= @EndDate)
	BEGIN
		--1. Xoa du lieu cua cac sanpham theo ngay
		DELETE FROM RptNhanHangThucChayFull
		WHERE CONVERT(DATE,NgayThucHien) = @NgayThucHien
		AND DmSanPhamREF NOT IN (144,299,337)
		--(144,299,337,381,305,342,239,253,252,251,243,242,271,385,247,306,423,284,437,375,245,531)
		--2. Tinh du lieu thuc chay cho cac san pham Boxapp self-serving, chi phi khac, Mobile, hosting, facebook..
		EXEC dbo.Rpt_InsertNhanHangThucChayFullKhac	@NgayThucHien	
		--3. Tinh du lieu thuc chay cho cac san pham khong phai la Boxapp SelfServing va Admarket
		EXEC [dbo].[Rpt_InsertNhanHangThucChayFull]	@NgayThucHien
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
		PRINT @NgayThucHien	
	END
END

--EXEC [dbo].[Rpt_InsertNhanHang_ThucChayFull] '2013-01-01', '2014-04-03'

```
