# Stored Procedure: `Insert_DoanhSoHaiDauNganhHangCore`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-22 16:43:04.350000
- **Ngày sửa cuối**: 2015-04-22 16:43:04.350000

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

--EXEC [dbo].[Insert_DoanhSoHaiDauNganhHangCore] '2015-01-01', '2015-01-05'
CREATE PROCEDURE [dbo].[Insert_DoanhSoHaiDauNganhHangCore] 
		@FromDate DATETIME,
		@ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @NgayThucHien_Bf DATETIME
	SET @NgayThucHien = @FromDate
	SET @NgayThucHien_Bf = DATEADD(DAY,-1,@FromDate)
	DELETE FROM DoanhSoHaiDauNganhHangCore
		WHERE 1=1
		AND NgayThucHien BETWEEN @FromDate AND @ToDate
		
	WHILE @NgayThucHien <= @ToDate
	BEGIN
		---CHAY DOANH SO CHO DU LIEU QUA KHU
		--EXEC Insert_DoanhSoHaiDauNganhHangCore_ThucThuKhuyenMai_History @NgayThucHien
		--EXEC Insert_DoanhSoHaiDauNganhHangCore_NoiBo_History @NgayThucHien
		---END CHAY DOANH SO CHO DU LIEU QUA KHU
		
		---CHAY DOANH SO CHO DU LIEU HIEN TAI
		--SET @NgayThucHien_Bf = DATEADD(DAY,-1,@NgayThucHien)
		EXEC Insert_DoanhSoHaiDauNganhHangCore_ByNgayThucHien @NgayThucHien
		---END CHAY DOANH SO CHO DU LIEU HIEN TAI
		PRINT @NgayThucHien
		SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)	
	END
	
END

```
