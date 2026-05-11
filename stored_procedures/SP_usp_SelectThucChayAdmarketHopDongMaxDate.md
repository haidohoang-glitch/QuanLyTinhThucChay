# Stored Procedure: `usp_SelectThucChayAdmarketHopDongMaxDate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-26 17:54:50.770000
- **Ngày sửa cuối**: 2014-11-19 12:16:44

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_SelectThucChayAdmarketHopDongMaxDate]
AS
	SET NOCOUNT ON
	SELECT MAX([NgayThucHien])
	FROM   [dbo].[ThucChayAdmarketHopDong]

```
