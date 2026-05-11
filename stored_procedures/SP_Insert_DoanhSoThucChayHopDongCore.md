# Stored Procedure: `Insert_DoanhSoThucChayHopDongCore`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:08.860000
- **Ngày sửa cuối**: 2015-03-27 17:44:08.860000

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

--EXEC [dbo].[Insert_DoanhSoThucChayHopDongCore] '2013-01-01', '2014-12-31'
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayHopDongCore] 
	@FromDate DATETIME,
	@ToDate DATETIME	
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	DELETE FROM DoanhSoThucChayHopDongCore
		WHERE 1=1
		AND convert(date,NgayThucHien) BETWEEN @FromDate AND @ToDate
		
	WHILE @NgayThucHien <= @ToDate
	BEGIN
		--TINH DOANH SO THUC CHAY THUC THU, KHUYEN MAI CHO HD CO SO
		EXEC [dbo].[Insert_DoanhSoThucChayHopDongCore_ThucThuKhuyenMai] @NgayThucHien
		--TINH DOANH SO THUC CHAY NOI BO CHO HD CO SO
		EXEC [dbo].[Insert_DoanhSoThucChayHopDongCore_NoiBo] @NgayThucHien
		
		--TINH DOANH SO THUC CHAY THUC THU - KHUYEN MAI CHO HD ONLINE
		EXEC [dbo].[Insert_DoanhSoThucChayHopDongCore_HDOnline_ThucThuKhuyenMai] @NgayThucHien
		--TINH DOANH SO THUC CHAY NOI BO CHO HD ONLINE
		EXEC [dbo].[Insert_DoanhSoThucChayHopDongCore_HDOnline_NoiBo] @NgayThucHien
		PRINT @NgayThucHien
			
		SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)
	END
	
END

```
