# Stored Procedure: `ThucChay_CPD_Job_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-27 09:30:35.517000
- **Ngày sửa cuối**: 2025-10-27 09:31:56.580000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Created by:	DWH\haidh
-- Optimized date: 20-09-2024 by DWH\trangtth
-- Description:	chốt thực chạy sản phẩm CPD 
-- =============================================

/*
EXEC [dbo].[ThucChay_CPD_Job_ByNgayThucHien]
	@dtStart = '2025-10-25',
	@dtEnd = '2025-10-25'
*/

CREATE PROCEDURE [dbo].[ThucChay_CPD_Job_ByNgayThucHien]
	@dtStart datetime,
	@dtEnd datetime
AS
BEGIN
	DECLARE @NgayDanhSo_GioiHan DATETIME, @NgayThucHien datetime
	
	

	SET @NgayThucHien = CONVERT(date,@dtEnd)

	SET @NgayDanhSo_GioiHan = DATEADD(YEAR, -3, @dtStart)

	EXEC [dbo].[ThucChay_CPDdotchay_PhatSinhThucChay_ThucChayDaTinh] @dtStart,@dtEnd,@NgayDanhSo_GioiHan
	EXEC [dbo].[ThucChay_CPDkhongdotchay_PhatSinhThucChay_ThucChayDaTinh] @dtStart,@dtEnd,@NgayDanhSo_GioiHan
	EXEC [dbo].[ThucChay_CPDdonvigoi_PhatSinhThucChay_ThucChayDaTinh] @NgayThucHien, @NgayDanhSo_GioiHan

	EXEC [dbo].[ThucChay_CPDdotchay_GhiNhanThayDoi_ThucChayDaTinh] @NgayThucHien, @NgayThucHien, @NgayDanhSo_GioiHan
	EXEC [dbo].[ThucChay_CPDkhongdotchay_GhiNhanThayDoi_ThucChayDaTinh] @NgayThucHien, @NgayThucHien, @NgayDanhSo_GioiHan
	EXEC [dbo].[ThucChay_CPDdonvigoi_GhiNhanThayDoi_ThucChayDaTinh] @NgayThucHien, @NgayThucHien, @NgayDanhSo_GioiHan

END





```
