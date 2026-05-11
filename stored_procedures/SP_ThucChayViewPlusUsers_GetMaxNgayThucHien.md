# Stored Procedure: `ThucChayViewPlusUsers_GetMaxNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-05-13 18:13:43.643000
- **Ngày sửa cuối**: 2015-05-13 18:13:43.643000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChayViewPlusUsers_GetMaxNgayThucHien] 
AS
BEGIN
	SELECT MAX([NgayThucHien]) FROM [dbo].[ThucChayViewPlusForUsers]          
END


```
