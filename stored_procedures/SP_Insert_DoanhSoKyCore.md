# Stored Procedure: `Insert_DoanhSoKyCore`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-22 16:43:03.380000
- **Ngày sửa cuối**: 2015-04-23 08:39:13.410000

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

--EXEC [dbo].[Insert_DoanhSoKyCore] '2009-01-01', '2015-04-22'
CREATE PROCEDURE [dbo].[Insert_DoanhSoKyCore] 
		@FromDate DATETIME,
		@ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	DELETE FROM DoanhSoKyCore
		WHERE 1=1
		AND NgayThucHien BETWEEN @FromDate AND @ToDate
		
	WHILE @NgayThucHien <= @ToDate
	BEGIN
		---CHAY DOANH SO CHO DU LIEU QUA KHU
		EXEC Insert_DoanhSoKyCore_ThucThuKhuyenMai_History @NgayThucHien
		EXEC Insert_DoanhSoKyCore_NoiBo_History @NgayThucHien
		---END CHAY DOANH SO CHO DU LIEU QUA KHU
		
		---CHAY DOANH SO CHO DU LIEU HIEN TAI
		--EXEC Insert_DoanhSoKyCore_ByNgayThucHien @NgayThucHien
		----END CHAY DOANH SO CHO DU LIEU HIEN TAI
		PRINT @NgayThucHien
		SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)	
	END
	
END

```
