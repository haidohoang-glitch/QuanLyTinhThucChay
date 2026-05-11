# Stored Procedure: `usp_SelectThucChayAdmarketMaxDate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-26 17:54:50.750000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.400000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_SelectThucChayAdmarketMaxDate]
AS
	SET NOCOUNT ON
	SELECT MAX([CreateDate])
	FROM   [dbo].[ThucChayAdmarket]

```
