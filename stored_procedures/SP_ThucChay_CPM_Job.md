# Stored Procedure: `ThucChay_CPM_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-11-22 16:14:34.010000
- **Ngày sửa cuối**: 2025-03-08 08:53:18.863000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

--================================== JOB

CREATE PROCEDURE [dbo].[ThucChay_CPM_Job]
AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME
	DECLARE @NgayThucHien DATETIME, @NgayDanhSoGioiHan DATE, @NgayDanhSoGioiHan_DonViBai DATE

	SET @dtStart = (
					SELECT TOP 1 tcdt.NgayThucHien
					FROM ABM_Data_ThucChay.dbo.thucchaydatinh tcdt
					WHERE (EXISTS(SELECT TOP (1) ch.ID	FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
														WHERE ch.DmSanPhamREF = tcdt.DmSanPhamREF
																AND ch.NhomTinhDoanhSoThucChay = 2 
																AND ch.DeletedStatus = 0 ORDER BY ch.ID
						   ))
						  AND NOT (tcdt.DmHinhThucQuangCao IN(13,42) OR tcdt.DmLoaiBannerREF IN (17,18))
						  AND NOT (tcdt.DmHinhThucQuangCao IN (26,5010,5000) AND (tcdt.DmChienDichREF = 3)) 
						  AND tcdt.DotChayHopDong <> N'NGAY'
					ORDER BY tcdt.NgayThucHien desc
				   )	
	SET @dtStart = DATEADD(dd,1, @dtStart)
	SET @dtStart = CONVERT(DATE, @dtStart)

	SET @dtEnd = CONVERT(DATE,GETDATE())
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	
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
