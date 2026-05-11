# Stored Procedure: `Insert_DoanhSoXuatHoaDonCore`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-12 10:47:06.637000
- **Ngày sửa cuối**: 2015-06-12 10:47:06.637000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[Insert_DoanhSoXuatHoaDonCore] '2009-01-01', '2015-04-26'
CREATE PROCEDURE [dbo].[Insert_DoanhSoXuatHoaDonCore] 
		@FromDate DATETIME,
		@ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	DELETE FROM DoanhSoXuatHoaDonCore
		WHERE 1=1
		AND NgayThucHien BETWEEN @FromDate AND @ToDate
		
	WHILE @NgayThucHien <= @ToDate
	BEGIN
		---CHAY DOANH SO CHO DU LIEU QUA KHU
		EXEC Insert_DoanhSoXuatHoaDonCore_ThucThuKhuyenMai_History @NgayThucHien
		EXEC Insert_DoanhSoXuatHoaDonCore_NoiBo_History @NgayThucHien
		---END CHAY DOANH SO CHO DU LIEU QUA KHU
		
		---CHAY DOANH SO CHO DU LIEU HIEN TAI
		--EXEC Insert_DoanhSoXuatHoaDonCore_ByNgayThucHien @NgayThucHien
		----END CHAY DOANH SO CHO DU LIEU HIEN TAI
		--PRINT @NgayThucHien
		SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)	
	END
	
END



```
