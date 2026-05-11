# Stored Procedure: `Insert_RptNhanHangThucChayFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-02-12 10:46:52.733000
- **Ngày sửa cuối**: 2015-03-05 15:04:35.723000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE  PROCEDURE [dbo].[Insert_RptNhanHangThucChayFull] 
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
		
		EXEC [dbo].[Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai] @NgayThucHien
		EXEC [dbo].[Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai_BySanPham] @NgayThucHien
		EXEC [dbo].[Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai_KhongHD] @NgayThucHien
		
		PRINT @NgayThucHien
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
	END
END

--EXEC [Insert_RptNhanHangThucChayFull] '2014-01-01','2014-12-30'

```
