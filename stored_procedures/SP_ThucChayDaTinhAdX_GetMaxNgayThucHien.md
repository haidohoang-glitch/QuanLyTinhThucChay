# Stored Procedure: `ThucChayDaTinhAdX_GetMaxNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:54:00.880000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.150000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdX_GetMaxNgayThucHien] 
AS
BEGIN
	SELECT MAX([NgayThucHien]) FROM dbo.ThucChayDaTinhAdX    
END

```
