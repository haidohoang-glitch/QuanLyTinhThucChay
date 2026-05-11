# Stored Procedure: `ThucChay_TinhLaiThucChay_ByHopDongID_Admatic_NhieuSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-15 18:01:21.903000
- **Ngày sửa cuối**: 2019-10-04 16:05:21.557000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_TinhLaiThucChay_ByHopDongID_Admatic_NhieuSanPham] '2018-06-17', '2018-06-17', 1003734
CREATE  PROCEDURE [dbo].[ThucChay_TinhLaiThucChay_ByHopDongID_Admatic_NhieuSanPham] 
	@FromDate DATETIME, 
	@ToDate DATETIME, 
	@HopDongFK INT,
	@GhiChu NVARCHAR(1000)
AS
BEGIN
	DECLARE  @NgayThucHien DATETIME, @PreFromDate DATETIME
	SET @PreFromDate = DATEADD(DAY,-1, @FromDate)
	SET @NgayThucHien = @FromDate
	--1. Cap nhat banner
	EXEC [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic_ByHopDongID] @HopDongFK
	--2. Cap nhat thu tu thuc chay
	EXEC [dbo].[ThucChay_Update_AdmaticThuTuChayHopDongChiTiet_ByHopDongID] @HopDongFK
	--3. Cap nhat gia tri thuc chay va trang thai cho table admaticthututhucchayhopdongchitiet
	EXEC [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay_ByHopDongID] @HopDongFK, @PreFromDate
	WHILE @NgayThucHien <= @ToDate
	BEGIN
		PRINT @NgayThucHien
		--EXEC [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_NhieuSanPham_ByHopDongID] @HopDongFK, @NgayThucHien
		EXEC [dbo].[ThucChay_Exec_GTTD_ThucChayDaTinh_Admatic_NhieuSanPham_ByHopDongID] 
		@HopDongFK = @HopDongFK,
		@NgayThucHien = @NgayThucHien,
		@NgayGhiNhanThucChay = @NgayThucHien,
		@GhiChu = @GhiChu

		--5.2 Adx - Admatic
		PRINT N'Adx - Admatic'
		--EXEC  [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_Adx_BySoHopDong] @HopDongFK,	@NgayThucHien
		EXEC  [dbo].[ThucChay_Exec_GTTD_ThucChayDaTinh_Admatic_Adx_BySoHopDong] @HopDongFK,	@NgayThucHien, @GhiChu

		 --Chay tinh xu ly lech treo ha
		--EXEC [dbo].[ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug_ByHopDong] @HopDongFK, @NgayThucHien
		
		SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)
	END
	
END

```
