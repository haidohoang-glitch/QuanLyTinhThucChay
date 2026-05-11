# Stored Procedure: `GetMaxLastModifiedAtFromBooking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-02 14:52:28.567000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@MaSanPham` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetMaxLastModifiedAtFromBooking]
	-- Add the parameters for the stored procedure here
	@MaSanPham int
AS
BEGIN
	DECLARE @LastModifiedAt DATETIME
	SET @LastModifiedAt = (
							Select Dateadd(day,-1,MAX(LastModifiedAt)) from Booking 
							Where DeletedStatus <> 1 
							AND MaSanPham = @MaSanPham
							)
	IF(@LastModifiedAt IS NULL) SET @LastModifiedAt = CONVERT(DATETIME,'2013-01-01 12:00:00')
	
	SELECT @LastModifiedAt
	
END



--EXEC [GetMaxLastModifiedAt] 'HopDong'

```
