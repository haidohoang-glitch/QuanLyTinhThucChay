# Stored Procedure: `Job_Insert_Update_HopDongChiTietAndBanner_CPM_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-10 11:08:59.297000
- **Ngày sửa cuối**: 2025-10-10 11:09:14.053000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

--================================== JOB

CREATE PROCEDURE [dbo].[Job_Insert_Update_HopDongChiTietAndBanner_CPM_Admatic]
AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME
	DECLARE @NgayDanhSoGioiHan DATE

	

	SET @dtEnd = CONVERT(DATE,GETDATE())
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	
	SET @NgayDanhSoGioiHan = DATEADD(YEAR, -3, @dtStart)

	EXEC [dbo].[ThucChay_CPM_Update_HopDongChiTietAndBanner] @NgayCheckThayDoi = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan
	EXEC [dbo].[ThucChay_NativeAds_Update_HopDongChiTietAndBanner] @NgayCheckThayDoi = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan
	EXEC [dbo].[ThucChay_Admatic_Update_HopDongChiTietAndBanner] @dtEnd, @NgayDanhSoGioiHan

END

```
