# Stored Procedure: `ThucChayAdmarketUsers_GetMaxNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-02 18:14:21.147000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.713000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayAdmarketUsers_GetMaxNgayThucHien] 
AS
BEGIN
	SELECT MAX([NgayThucHien]) FROM [dbo].[ThucChayAdmarketUsers]          
END

```
