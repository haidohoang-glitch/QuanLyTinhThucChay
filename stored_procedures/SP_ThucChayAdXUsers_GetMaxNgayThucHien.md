# Stored Procedure: `ThucChayAdXUsers_GetMaxNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:54:00.367000
- **Ngày sửa cuối**: 2015-02-04 15:58:32.363000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayAdXUsers_GetMaxNgayThucHien] 
AS
BEGIN
	SELECT MAX([NgayThucHien]) FROM [dbo].[ThucChayAdXForUsers]          
END

```
