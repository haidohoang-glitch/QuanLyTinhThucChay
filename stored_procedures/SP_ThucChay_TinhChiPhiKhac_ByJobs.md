# Stored Procedure: `ThucChay_TinhChiPhiKhac_ByJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-02 23:13:49.170000
- **Ngày sửa cuối**: 2024-11-28 10:33:01.613000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChay_TinhChiPhiKhac_ByJobs]
CREATE PROCEDURE [dbo].[ThucChay_TinhChiPhiKhac_ByJobs]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	
	DECLARE @dtStart DATETIME, @dtEnd DATETIME
	DECLARE @NgayGioiHanTinh DATETIME, @NgayDanhSoGioiHan_Tiktok DATETIME = '2022-01-01'
	
	SET @NgayGioiHanTinh = '2014-01-01';
	
	
	SET @dtStart = (
					SELECT TOP(1) tc.NgayThucHien FROM dbo.ThucChayDaTinh tc
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
					ORDER BY tc.NgayThucHien DESC
	)
	
	IF @dtStart IS NULL
		SET @dtStart = @NgayGioiHanTinh
	ELSE
		SET @dtStart = DATEADD(dd,1, @dtStart)
	
	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)

	SET @dtEnd = CONVERT(DATE,@dtEnd)
	
	------ Update 12/6/2017

	--thay doi vi tri 21/05/2021 haidh comment
	
	PRINT '[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac]'
	EXEC sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac @dtEnd,@dtEnd, NULL
	 --SELECT  @dtStart,@dtEnd

	PRINT '[ThucChay_InsertThucChayDaTinh_ChiPhiKhac]'
	EXEC sp_TC_InsertThucChayDaTinh_ChiPhiKhac @dtEnd,@dtEnd, NULL
	--Tinh gia tri thay doi Chi phí khác

	
	PRINT '[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh]'
	--Tinh gia tri thay doi cho chi phi sanpham chinh
	EXEC [sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh] @dtEnd, @dtEnd, NULL

				
	PRINT '[ThucChay_InsertThucChayDaTinh_ChiPhi_SanPhamChinh]'
	--Tinh Thuc Chay cho cac sanpham Chi phi 
	EXEC [sp_TC_InsertThucChayDaTinh_ChiPhi_SanPhamChinh] @dtEnd, @dtEnd, NULL
	
	--Cap nhat lai thong tin nhan hang bi loi cho cac san pham chi phi
	--EXEC [ThucChay_UpdateThongTinNhanHangThucChayDaTinh] @dtEnd 
	
	
	PRINT '[ThucChay_UpdateGiaTriThayDoi_ThucChay_GiaiPhapCongNghe_SanPhamChinh]'
	--Update gia tri thay doi khi thay doi thong tin thanh tien tren hdct cua GiaiPhapCongNghe_SanPhamChinh
	EXEC [dbo].[sp_TC_UpdateGiaTriThayDoi_ThucChay_GiaiPhapCongNghe_SanPhamChinh] @dtEnd

		PRINT '[ThucChay_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh]'
	--Tinh thuc chay cho cac san pham chinh chay cong nghe (Retargeting & Content base)
	EXEC [sp_TC_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh] @dtEnd, NULL

	--PRINT '[job_UpdateThucChayHopDongChiTiet_ChiPhiKhac]'
	--EXEC [dbo].[job_UpdateThucChayHopDongChiTiet_ChiPhiKhac]  @dtEnd,@dtEnd

	/*TINH CHO SAN PHAM CREATOR CONTENT	
	--AP DUNG CHO HOPDONG DANH SO >= 2021-10-01
	--	Sản phẩm = Content Creator, ID=5184
	--- HTQC= Social Media, id=29
	*/
	--THUC HIEN TINH HANG NGAY
	EXEC [dbo].[sp_ThucChay_ExcInsertThucChayDaTinh_CreatorContent]
    @StartDate = @dtEnd ,
    @EndDate = @dtEnd ,
    @piHopDongID = NULL

	--CHECK VA TINH GIA TRI THAY DOI KHI CO THAY DOI NOI DUNG HOPDONG
	EXEC [dbo].[ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_CreatorContent] 
	@NgayThucHien = @dtEnd

	--CHECK KETQUAVANHANH BI XOA VA THUC HIEN TINH GIA TRI THAY DOI
	--HAIDH COMMENT THAY DOI PHUONG THUC CHECK 20220112
	--EXEC [dbo].[ThucChayDaTinh_CheckKetQuaVanHanhXoa_CreatorContent]
	--@NgayThucHien = @dtEnd

	--20220112 CHECK THAY DOI KET QUA VAN HANH (XOA VA THAY DOI LAI KQVH)
	EXEC [ThucChayDaTinh_CheckKetQuaVanHanhThayDoi_CreatorContent] 
	@NgayThucHien = @dtEnd

	/*END TINH CHO SAN PHAM CREATOR CONTENT	*/

	--CHECK VA XL DULIEU CHI PHI CHO THANGDUGP HAIDH 19/10/2022
	EXEC [dbo].[prc_asd_CheckGTTDChiPhi_With_HopDong_ThangDuGP]
	-- Add the parameters for the stored procedure here
	@NgayThucHien = @dtEnd
END

```
