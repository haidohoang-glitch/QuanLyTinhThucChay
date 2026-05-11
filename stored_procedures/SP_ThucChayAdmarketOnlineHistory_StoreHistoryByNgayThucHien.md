# Stored Procedure: `ThucChayAdmarketOnlineHistory_StoreHistoryByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 16:07:02.880000
- **Ngày sửa cuối**: 2015-06-10 16:07:02.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-03-23
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayAdmarketOnlineHistory_StoreHistoryByNgayThucHien]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @DeletedDay	DATETIME
	
	SET @DeletedDay = DATEADD(d, -7, @NgayThucHien);
	
	-- delete date before 7 days
	DELETE ThucChayAdmarketOnlineHistory WHERE DayHistory <= @DeletedDay;
	
    -- Insert statements for procedure here
	INSERT INTO ThucChayAdmarketOnlineHistory
	SELECT
		NEWID(),
		@NgayThucHien,
		A.*
	FROM ThucChayAdmarketOnline A
	WHERE A.NgayThucHien <= @NgayThucHien
		--AND A.TaiKhoan = 'tienganh123'
	
END

```
