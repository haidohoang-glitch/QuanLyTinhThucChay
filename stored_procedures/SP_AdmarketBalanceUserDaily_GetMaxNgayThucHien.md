# Stored Procedure: `AdmarketBalanceUserDaily_GetMaxNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-25 14:31:05.350000
- **Ngày sửa cuối**: 2015-04-25 14:31:05.350000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [dbo].[AdmarketBalanceUserDaily_GetMaxNgayThucHien]
CREATE PROCEDURE [dbo].[AdmarketBalanceUserDaily_GetMaxNgayThucHien]
AS
BEGIN
	SELECT Isnull(MAX(NgayThucHien),DATEADD(DAY,-2, GETDATE())) FROM dbo.admarketBalanceUserDaily 
END

```
