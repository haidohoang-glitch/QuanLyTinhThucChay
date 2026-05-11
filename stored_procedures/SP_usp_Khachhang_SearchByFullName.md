# Stored Procedure: `usp_Khachhang_SearchByFullName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:45.323000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.120000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenKhachhang` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Khachhang_SearchByFullName]
	@TenKhachhang NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT TOP 30 KhachHangID, kh.TenKhachHang, kh.MaKhachHang, kh.MaSoThue
	FROM   KhachHangFull kh
	WHERE  kh.TenKhachHang LIKE '%' + @TenKhachhang + '%' AND DeletedStatus <> 1
	ORDER BY
	       kh.TenKhachHang ASC
END

```
