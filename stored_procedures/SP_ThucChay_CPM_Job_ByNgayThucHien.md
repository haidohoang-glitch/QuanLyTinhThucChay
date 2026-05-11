# Stored Procedure: `ThucChay_CPM_Job_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-11-26 09:48:18.287000
- **Ngày sửa cuối**: 2025-10-27 09:40:32.377000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--================================== JOB
/*
 EXEC [dbo].[ThucChay_CPM_Job_ByNgayThucHien]
	@dtStart = '2025-10-26',
	@dtEnd = '2025-10-26'
*/

CREATE PROCEDURE [dbo].[ThucChay_CPM_Job_ByNgayThucHien]
	@dtStart DATETIME,
	@dtEnd DATETIME
AS
BEGIN
	DECLARE @NgayDanhSoGioiHan DATE, @NgayDanhSoGioiHan_DonViBai DATE


		
	SET @NgayDanhSoGioiHan = DATEADD(YEAR, -3, @dtStart)

	EXEC [dbo].[ThucChay_CPM_Update_HopDongChiTietAndBanner] @NgayCheckThayDoi = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan
	EXEC [dbo].[ThucChay_NativeAds_Update_HopDongChiTietAndBanner] @NgayCheckThayDoi = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan

	--============================================== Nhóm 1: CPM thuần, TVC Online, CPV =================================
	EXEC [dbo].[ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh] @NgayGhiNhan = @dtEnd, @NgayCheckThayDoi = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan
	EXEC [dbo].[ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh] @NgayGhiNhan = @dtStart, @NgayPhatSinh_Tu = @dtStart, @NgayPhatSinh_Den = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan

	EXEC [dbo].[ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh]  @NgayGhiNhan = @dtStart, @NgayPhatSinh_Tu = @dtStart, @NgayPhatSinh_Den = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan

	EXEC [dbo].[ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh]  @NgayGhiNhan = @dtEnd, @NgayCheckThayDoi = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan
	EXEC [dbo].[ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh]  @NgayGhiNhan = @dtStart, @NgayPhatSinh_Tu = @dtStart, @NgayPhatSinh_Den = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan

	----============================================== Nhóm 2: CPR hiện tại không phát sinh thực chạy nên chưa tối ưu =================================
	---- CPR gói
	--EXEC dbo.[ThucChay_ExcInsertThucChayDaTinh_CPR] @dtStart,@dtEnd
	---- CPR
	--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR] @dtStart,@dtEnd

	----============================================== Nhóm 3: Native Ads ================================
	EXEC [dbo].[ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh]  @NgayGhiNhan = @dtEnd, @NgayCheckThayDoi = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan
	EXEC [dbo].[ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh]  @NgayGhiNhan = @dtStart, @NgayPhatSinh_Tu = @dtStart, @NgayPhatSinh_Den = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan

	----============================================== Nhóm 4: DonViBai ================================
	---- Hợp đồng đánh số trước '2021-06-10': chưa tối ưu
	--EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViBai] 
	--@StartDate = @dtStart,
	--@EndDate = @dtEnd
	--EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai] 
	--   @StartDate = @dtStart ,
	--   @EndDate = @dtEnd

	---- Hợp đồng đánh số sau '2021-06-10'
	SET @NgayDanhSoGioiHan_DonViBai = IIF(@NgayDanhSoGioiHan >= '2021-06-10', @NgayDanhSoGioiHan, '2021-06-10')
	EXEC [dbo].[ThucChay_CPMDonViBai] @dtEnd, @NgayDanhSoGioiHan_DonViBai

	
	----============================================== Nhóm 5: DonViGoi ================================
	EXEC [dbo].[ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh]  @NgayGhiNhan = @dtEnd, @NgayCheckThayDoi = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan
    EXEC [dbo].[ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh] @NgayGhiNhan = @dtStart, @NgayPhatSinh_Tu = @dtStart, @NgayPhatSinh_Den = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan



END

```
