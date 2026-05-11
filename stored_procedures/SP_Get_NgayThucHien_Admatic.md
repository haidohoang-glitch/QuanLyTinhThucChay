# Stored Procedure: `Get_NgayThucHien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-28 13:13:31.040000
- **Ngày sửa cuối**: 2017-10-28 13:13:31.040000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Get_NgayThucHien_Admatic]
as
BEGIN
	--SELECT CONVERT(VARCHAR(10),MAX(NgayThucHien) + 1,120) FROM dbo.ThucChayDaTinh\
	SELECT CONVERT(VARCHAR(10), GETDATE(),120)

END
```
