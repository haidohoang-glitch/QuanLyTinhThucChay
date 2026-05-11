# Stored Procedure: `ThucChay_Max_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-21 17:03:56.590000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.773000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE proc [dbo].[ThucChay_Max_NgayThucHien]
AS
SELECT MAX(NgayThucHien) MaxNgayThucHien, dbo.FormatDate(MAX(NgayThucHien)) AS NgayThucHien FROM ThucChayDaTinh

```
