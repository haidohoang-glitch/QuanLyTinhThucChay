# Stored Procedure: `usp_Khachhang_SearchKhachhangKyHopdong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:45.070000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.297000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenKhachhang` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Khachhang_SearchKhachhangKyHopdong]
	@TenKhachhang NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT DISTINCT TOP 20 hd.DmKhachHangREF,
	       kh.TenKhachHang
	FROM   HopDong hd
	       INNER JOIN KhachHangFull kh
	            ON  hd.DmKhachHangREF = kh.KhachHangID
	WHERE  kh.TenKhachHang LIKE '%' + @TenKhachhang + '%'
END

```
