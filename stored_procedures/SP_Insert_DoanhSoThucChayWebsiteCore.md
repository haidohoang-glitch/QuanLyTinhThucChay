# Stored Procedure: `Insert_DoanhSoThucChayWebsiteCore`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:10.637000
- **Ngày sửa cuối**: 2015-03-27 17:44:10.637000

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

--EXEC [dbo].[Insert_DoanhSoThucChayWebsiteCore] '2013-01-01', '2013-01-31'
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayWebsiteCore] 
		@FromDate DATETIME,
		@ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	DELETE FROM DoanhSoThucChayWebsiteCore
		WHERE 1=1
		AND NgayThucHien BETWEEN @FromDate AND @ToDate
		
	WHILE @NgayThucHien <= @ToDate
	BEGIN
		--TINH DOANH SO THUC CHAY THEO WEBSITE VOI THUC THU VA KHUYEN MAI
		EXEC [dbo].[Insert_DoanhSoThucChayWebsiteCore_ThucThuKhuyenMai] @NgayThucHien
		--TINH DOANH SO THUC CHAY THEO WEBSITE VOI NOI BO
		EXEC [dbo].[Insert_DoanhSoThucChayWebsiteCore_NoiBo] @NgayThucHien
		
		PRINT @NgayThucHien

		SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)	
	END
	
END

```
