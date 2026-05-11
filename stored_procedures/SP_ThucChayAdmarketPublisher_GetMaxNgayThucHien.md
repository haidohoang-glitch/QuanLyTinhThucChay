# Stored Procedure: `ThucChayAdmarketPublisher_GetMaxNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-14 17:57:52.297000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.370000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayAdmarketPublisher_GetMaxNgayThucHien]
AS
BEGIN
	SELECT MAX(NgayThucHien)FROM dbo.ThucChayAdmarketPublisher 
	WHERE DmSanPhamREF = 144
END

```
