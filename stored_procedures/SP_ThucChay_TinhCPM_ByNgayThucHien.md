# Stored Procedure: `ThucChay_TinhCPM_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-03 13:40:00.283000
- **Ngày sửa cuối**: 2017-09-30 08:37:33.393000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--

/*
EXEC [dbo].[ThucChay_TinhCPM_ByNgayThucHien]  '2017-09-28',  '2017-09-28'
*/
CREATE PROCEDURE [dbo].[ThucChay_TinhCPM_ByNgayThucHien]

	 @dtStart DATETIME, 
	 @dtEnd DATETIME
	
AS
BEGIN
	
	--Tinh Thuc Chay CPM
	EXEC [dbo].[ThucChay_HopDongChiTietAndBanner] @dtEnd
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner] 
		
	EXEC [ThucChay_ExcInsertThucChayDaTinh] @dtStart,@dtEnd
	EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinhCPV] @dtStart,@dtEnd 
	
	--Tinh gia tri thay doi CPM
	--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] @dtStart,@dtEnd
	EXEC [sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM] @dtStart,@dtEnd, NULL
	
	--Tinh gia tri thuc chay CPR voi don vi la Goi
	EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] @dtStart,@dtEnd
	
	--Tinh gia tri thu chay voi don vi la CPR
	EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR] @dtStart,@dtEnd
	
END

```
