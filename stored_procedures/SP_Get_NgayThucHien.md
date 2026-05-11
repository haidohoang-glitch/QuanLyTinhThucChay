# Stored Procedure: `Get_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-05 12:04:48.170000
- **Ngày sửa cuối**: 2017-05-05 12:04:48.170000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Get_NgayThucHien]
as
BEGIN
	--SELECT CONVERT(VARCHAR(10),MAX(NgayThucHien) + 1,120) FROM dbo.ThucChayDaTinh\
	SELECT CONVERT(VARCHAR(10), GETDATE()-1,120)

END
```
