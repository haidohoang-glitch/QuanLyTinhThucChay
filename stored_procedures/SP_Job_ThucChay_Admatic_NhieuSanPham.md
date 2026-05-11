# Stored Procedure: `Job_ThucChay_Admatic_NhieuSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-15 18:08:27.127000
- **Ngày sửa cuối**: 2024-12-16 15:21:02.910000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [dbo].[Job_ThucChay_Admatic_NhieuSanPham]
CREATE  PROCEDURE [dbo].[Job_ThucChay_Admatic_NhieuSanPham] 
AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME

	SET @dtStart = (
						SELECT TOP (1) tcdt.NgayThucHien
						FROM dbo.ThucChayDaTinh tcdt
						LEFT JOIN 
						(SELECT hdct.HopDongChiTietID, hdct.HopDongFK 
							FROM dbo.HopDongChiTiet hdct 
							WHERE hdct.DeletedStatus = 0
							AND ISNULL(hdct.DmLoaiNenTangREF,0) <> 8
							--AND hdct.HopDongChiTietID NOT IN (SELECT HopDongChiTietREF FROM DmThongTinHopDongBanInventory) -- bán inventory
						) hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
							WHERE tcdt.DmHinhThucQuangCao = 42
							AND tcdt.DonViTinh <> N'CPV'
							AND not (tcdt.DmHinhThucQuangCao= 13 OR tcdt.DmLoaiBannerREF IN (17,18))
							AND tcdt.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,821,342,585,5056,5268)
							AND tcdt.DotChayBooking <> N'HDBAN_INVENTORY'
							--AND tcdt.HopDongChiTietREF NOT IN (SELECT HopDongChiTietREF FROM DmThongTinHopDongBanInventory) -- bán inventory
							ORDER BY tcdt.NgayThucHien DESC
	)	

	SET @dtStart = DATEADD(dd,1, @dtStart)
	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)


	
	DECLARE  @NgayThucHien DATETIME
	SET @NgayThucHien = @dtStart
	WHILE @NgayThucHien <= @dtEnd
	BEGIN
	
		--1. Cap nhat banner
		PRINT N'1. Cap nhat banner'
		EXEC [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic] @NgayThucHien = @NgayThucHien

		---****THUC HIEN TINH THUC CHAY THANHTIEN_ADMATIC THEO PHUONG PHAP PHAP DO TIEN THEO BANNER VA HOPDONGCHITIET
		---Ap dung cho hopdong co ngaydanhsohopdong >= 2020-07-20
		-- Thuc hien tinh thuc chay ThanhTien_Admatic
		EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_ThanhTien_Admatic] 
		@StartDate = @NgayThucHien,
		@EndDate = @NgayThucHien

		--Thuc hien check va update gia tri thay doi (co ps thong tin thay doi hopdongthaydoi va thong tin hopdongchitiet bi xoa)
		EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ThanhTien_Admatic] 
		@StartDate = @NgayThucHien ,
		@EndDate = @NgayThucHien

		--Check thong tin thuc treo thay doi (huy thuc treo, hoac treo cham chua duoc tinh) -- haidh comment 2021-06-09
		EXEC [dbo].[sp_TC_UpdateGiaTriThayDoi_ThucTreoThayDoi_ThanhTien_Admatic] 
		-- Add the parameters for the stored procedure here
		@NgayThucHien = @NgayThucHien

		--Thuc hien tinh thuc chay cho DONVIBAI ADMATIC
		EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViBai_Admatic_ThucTreo] 
		@StartDate = @NgayThucHien,
		@EndDate = @NgayThucHien

		--check va thuc hien tinh gia tri thay doi cho DONVIBAI ADMATIC
		EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai_Admatic_ThucTreo] 
		@StartDate = @NgayThucHien ,
		@EndDate = @NgayThucHien

		--Thuc hien day thong tin thucchaydatinh -> thucchaydatinhadmarket voi san pham Adx - 585
		EXEC [dbo].[ThucChay_InsertThucChayDaTinhAdmarket_Adx_ThanhTien_Admatic] 
		@NgayThucHien = @NgayThucHien,
		@DotChayHopDong = N'ThanhTien_Admatic'



		---***END THANHTIEN_ADMATIC

		----. Native ads - Admatic 
		----CHU Y CHI TINH THEO PHUONG PHAP CU VOI NHUNG HOP DONG DANH SO TU NGAY 2020-11-16 TRO VE TRUOC
		--EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_Admatic_Native_Ads] @StartDate = @NgayThucHien, @EndDate = @NgayThucHien
		
		----8. thuc hien xu ly lech treo ha
		--PRINT N'8. thuc hien xu ly lech treo ha'
		--EXEC [dbo].[ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug] @NgayThucHien = @NgayThucHien

		

		--9. Tinh gia tri thay doi khi thay doi nhan hang treo 
		PRINT N'9. Tinh gia tri thay doi khi thay doi nhan hang treo'
		EXEC [dbo].[ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham] @NgayThucHien = @NgayThucHien

		----10. Cap nhat gia tri thuc chay va trang thai cho table admaticthututhucchayhopdongchitiet
		--PRINT N'10. Cap nhat gia tri thuc chay va trang thai cho table admaticthututhucchayhopdongchitiet'
		--EXEC [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay] @NgayThucHien = @NgayThucHien

		
		SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)
	END
END

```
