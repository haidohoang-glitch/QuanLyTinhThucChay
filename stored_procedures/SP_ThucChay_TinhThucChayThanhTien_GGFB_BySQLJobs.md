# Stored Procedure: `ThucChay_TinhThucChayThanhTien_GGFB_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-07 17:40:00.677000
- **Ngày sửa cuối**: 2022-04-01 14:05:11.343000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_TinhThucChayThanhTien_GGFB_BySQLJobs] 
	@NgayThucHien DATETIME
AS
BEGIN
	
	-- CHECK VA THUC HIEN TINH DU LIEU THUC CHAY CHO GGFP (...)
	EXEC dbo.[ThucChayDaTinh_ExecThucChay_ThanhTien_GGFB] @NgayThucHien = @NgayThucHien

	print '[ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_ThanhTien_GGFB]'
	-- CHECK VA THUC HIEN TINH GIA TRI THAY DOI TREN CAC TABLE NGHIEP VU GGGP (...)
	EXEC [dbo].[ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_ThanhTien_GGFB] @NgayThucHien = @NgayThucHien
	-- CHECK VA THUC HIEN TINH GIA TRI THAY DOI TREN HOP DONG (...)
	
END;
```
