# Stored Procedure: `ThucChay_MKT_FEE_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-07-01 14:16:31.017000
- **Ngày sửa cuối**: 2025-07-01 14:39:38.440000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC  [dbo].[ThucChay_PerformanceBase_Marketing_Fee_Job]
*/

CREATE PROCEDURE [dbo].[ThucChay_MKT_FEE_Job]	
AS
BEGIN
	
	DECLARE @dtEnd DATETIME, 	
	@NgayDanhSoGioiHan_PB_MKT DATETIME = '2025-07-05'
	

	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	SET @dtEnd = CONVERT(DATE,@dtEnd)

	--1. TINH GIA TRI THAY DOI PERFORMANCE BASE - MARKETING FEE
	EXEC [dbo].[ThucChay_MKT_FEE_GhiNhanThayDoi] 
	@NgayThucHien = @dtEnd,
	@NgayDanhSoGioiHan = @NgayDanhSoGioiHan_PB_MKT

	--2. TINH THUC CHAY PERFORMANCE BASE - MARKETING FEE
	EXEC [dbo].[ThucChay_MKT_FEE_GhiNhanPhatSinh] 
	@NgayThucHien = @dtEnd,
	@NgayDanhSoGioiHan = @NgayDanhSoGioiHan_PB_MKT



END



```
