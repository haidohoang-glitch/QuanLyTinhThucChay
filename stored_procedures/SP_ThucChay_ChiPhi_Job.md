# Stored Procedure: `ThucChay_ChiPhi_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-02-06 16:44:38.867000
- **Ngày sửa cuối**: 2025-09-17 10:05:23.867000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql


CREATE PROCEDURE [dbo].[ThucChay_ChiPhi_Job]	
AS
BEGIN
	
	DECLARE @dtStart DATETIME, @dtEnd DATETIME, @NgayDanhSoHopDong DATE
	DECLARE @NgayGioiHanTinh DATETIME = '2010-01-01', @NgayDanhSoGioiHan_Tiktok DATETIME = '2022-01-01', 
	@NgayDanhSoGioiHan_PB_MKT DATETIME = '2025-07-05',
	@NgayDanhSoGioiHan_Admatic_MKT DATETIME = '2025-10-01'
	
	
	SET @dtStart = (
					SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh tc
											WHERE 1=1 AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = tc.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
						AND NOT ( tc.DmHinhThucQuangCao = 13 OR tc.DmLoaiBannerREF in (18))--Khong tinh thuc chay cho HTQC Mua Ngoai	
						AND NOT (tc.DmViTriREF in (100093,100478))	--banner của GGFB,774 --banner của GGFB 28/02/2021
						AND NOT ((tc.DmSanPhamREF = 5188  OR tc.DmViTriREF = 100774) AND  (tc.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok)) --haidh comment 20211026 TikTok tinh theo pp GGFB
						AND tc.GhiChu <> N'HDBAN_INVENTORY'
						AND NOT (tc.DmHinhThucQuangCao IN (26,5010,5000) AND (tc.DmChienDichREF = 3)) --Haidh comment 23/09/2022 Loai ThangduGP cua ben Performance Base
						--HAIDH COMMENT 2025-07-01 THEM DIEU KIEN LOAI CAC SAN PHAM Marketing fee cua Performance Base theo NgayDanhSoHopDong
						AND NOT (tc.DmHinhThucQuangCao = 5038 AND tc.DmSanPhamREF = 817  AND tc.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – PB
						--HAIDH COMMENT 2025-09-17 THEM DIEU KIEN LOAI CAC SAN PHAM Marketing fee cua Admantic theo NgayDanhSoHopDong
						AND NOT (tc.DmHinhThucQuangCao = 42 AND tc.DmSanPhamREF = 817  AND tc.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Admatic_MKT) --Marketing fee – Admantic
	)
	
	SET @dtStart = DATEADD(dd,1, @dtStart)
	SET @dtStart = ISNULL(@dtStart, @NgayGioiHanTinh)

	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	SET @dtEnd = CONVERT(DATE,@dtEnd)

	SET @NgayDanhSoHopDong = DATEFROMPARTS(YEAR(@dtStart) - 3, 1, 1)
	
	

	--=========================================================== Nhóm 1: chi phí khác ===========================
	EXEC [dbo].[ThucChay_ChiPhiKhac] @NgayGhiNhan = @dtEnd, @NgayCheckThayDoi = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoHopDong
	

	----=========================================================== Nhóm 2: Sản phẩm chính: chưa tối ưu và ít phát sinh =========================
	--PRINT '[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh]'
	--EXEC [sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh] @dtEnd, @dtEnd, NULL				
	--PRINT '[ThucChay_InsertThucChayDaTinh_ChiPhi_SanPhamChinh]'
	--EXEC [sp_TC_InsertThucChayDaTinh_ChiPhi_SanPhamChinh] @dtEnd, @dtEnd, NULL
	
	
	----=========================================================== Nhóm 3: giải pháp công nghệ: chưa tối ưu vì ít phát sinh ====================
	--PRINT '[ThucChay_UpdateGiaTriThayDoi_ThucChay_GiaiPhapCongNghe_SanPhamChinh]'
	--EXEC [dbo].[sp_TC_UpdateGiaTriThayDoi_ThucChay_GiaiPhapCongNghe_SanPhamChinh] @dtEnd
	--PRINT '[ThucChay_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh]'
	--EXEC [sp_TC_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh] @dtEnd, NULL

	
	--=========================================================== Nhóm 4: Creator Content: chưa tối ưu vì ít phát sinh 
	EXEC [dbo].[sp_ThucChay_ExcInsertThucChayDaTinh_CreatorContent]
		@StartDate = @dtEnd ,
		@EndDate = @dtEnd ,
		@piHopDongID = NULL
	EXEC [dbo].[ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_CreatorContent] 
		@NgayThucHien = @dtEnd
	EXEC [ThucChayDaTinh_CheckKetQuaVanHanhThayDoi_CreatorContent] 
		@NgayThucHien = @dtEnd

	
	----=========================================================== Nhóm 5: Thặng dư giải pháp: không tối ưu vì không phát sinh
	--EXEC [dbo].[prc_asd_CheckGTTDChiPhi_With_HopDong_ThangDuGP]
	--@NgayThucHien = @dtEnd
END





SET QUOTED_IDENTIFIER ON
SET ANSI_NULLS ON

```
