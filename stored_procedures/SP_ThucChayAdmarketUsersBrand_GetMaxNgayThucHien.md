# Stored Procedure: `ThucChayAdmarketUsersBrand_GetMaxNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-09 14:25:41.523000
- **Ngày sửa cuối**: 2016-03-09 14:25:41.523000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayAdmarketUsersBrand_GetMaxNgayThucHien] 
AS
BEGIN
	SELECT MAX([NgayThucHien]) FROM [dbo].ThucChayAdmarketUser_NhanHang       
END

```
