# Stored Procedure: `ThucChay_CPD_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-10-15 15:14:19.120000
- **Ngày sửa cuối**: 2025-04-10 09:23:15.553000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Created by:	DWH\haidh
-- Optimized date: 20-09-2024 by DWH\trangtth
-- Description:	chốt thực chạy sản phẩm CPD 
-- =============================================


CREATE PROCEDURE [dbo].[ThucChay_CPD_Job]
AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME, @NgayThucHien DATETIME, @NgayDanhSo_GioiHan DATETIME
	
	--SET @dtStart = (
	--				SELECT MAX(NgayThucHien) FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
	--					WHERE DmSanPhamREF IN (140,564,549,5082)  
	--					AND NOT( DmHinhThucQuangCao = 13 OR DmLoaiBannerREF in (17,18))
					
	--				)
	SET @dtStart = DATEADD(dd,-1, GETDATE())--DATEADD(dd,1, @dtStart)
	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
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
