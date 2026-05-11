# Stored Procedure: `Job_ThucChay_Admatic_NhieuSanPham_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-08-07 14:19:04.457000
- **Ngày sửa cuối**: 2023-01-09 10:16:48.157000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Job_ThucChay_Admatic_NhieuSanPham_ByNgayThucHien] 
	@NgayThucHien = '2023-01-07'
	*/
CREATE  PROCEDURE [dbo].[Job_ThucChay_Admatic_NhieuSanPham_ByNgayThucHien] 
	@NgayThucHien DATETIME
AS
BEGIN
	

		SET @NgayThucHien = ISNULL(@NgayThucHien,DATEADD(DAY,-1, GETDATE()))
	
		--1. Cap nhat banner
		PRINT N'1. Cap nhat banner'
		EXEC [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic] @NgayThucHien = @NgayThucHien

		--2. Tinh Gia tri thay doi khi thay doi Thanh tien hoac chiet khau --CHO NAY CAN XEM LAI
		PRINT N'2. Tinh Gia tri thay doi khi thay doi Thanh tien hoac chiet khau --CHO NAY CAN XEM LAI'
		--EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham] @NgayThucHien = @NgayThucHien
		--EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_v1] @NgayThucHien = @NgayThucHien
		EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_v2] @NgayThucHien = @NgayThucHien
		
		--3. Tinh Gia tri thay doi khi thay doi don gia banner 
		PRINT N'3. Tinh Gia tri thay doi khi thay doi don gia banner'
		EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner] @NgayThucHien = @NgayThucHien

		----4. Thuc hien check hdct bi xoa va thuc hien doi tru va tinh lai toan bo
		--PRINT N'4. Thuc hien check hdct bi xoa va thuc hien doi tru va tinh lai toan bo'
		--EXEC [dbo].[sp_ThucChay_CheckXoaHDCTVaUpdateGTTD_Admatic_NhieuSanPham] 	@NgayThucHien = @NgayThucHien

		--5. Cap nhat thu tu thuc chay
		PRINT N'5. Cap nhat thu tu thuc chay'
		EXEC [dbo].[ThucChay_Update_AdmaticThuTuChayHopDongChiTiet] @NgayThucHien = @NgayThucHien

		--6. Tinh thuc chay
		PRINT N'6. Tinh thuc chay'
		EXEC [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_NhieuSanPham]  @NgayThucHien = @NgayThucHien

		--7. Adx - Admatic
		PRINT N'7. Adx - Admatic'
		EXEC [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_Adx] 	@NgayThucHien = @NgayThucHien

		---THUC HIEN TINH THUC CHAY THANHTIEN_ADMATIC THEO PHUONG PHAP PHAP DO TIEN THEO BANNER VA HOPDONGCHITIET
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



		---END THANHTIEN_ADMATIC

		--. Native ads - Admatic 
		--CHU Y CHI TINH THEO PHUONG PHAP CU VOI NHUNG HOP DONG DANH SO TU NGAY 2020-11-16 TRO VE TRUOC
		EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_Admatic_Native_Ads] @StartDate = @NgayThucHien, @EndDate = @NgayThucHien
		
		--8. thuc hien xu ly lech treo ha
		PRINT N'8. thuc hien xu ly lech treo ha'
		EXEC [dbo].[ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug] @NgayThucHien = @NgayThucHien

		

		--9. Tinh gia tri thay doi khi thay doi nhan hang treo 
		PRINT N'9. Tinh gia tri thay doi khi thay doi nhan hang treo'
		EXEC [dbo].[ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham] @NgayThucHien = @NgayThucHien

		--10. Cap nhat gia tri thuc chay va trang thai cho table admaticthututhucchayhopdongchitiet
		PRINT N'10. Cap nhat gia tri thuc chay va trang thai cho table admaticthututhucchayhopdongchitiet'
		EXEC [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay] @NgayThucHien = @NgayThucHien


END

```
