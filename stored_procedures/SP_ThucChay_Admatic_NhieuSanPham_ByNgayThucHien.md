# Stored Procedure: `ThucChay_Admatic_NhieuSanPham_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-07-07 10:12:00.903000
- **Ngày sửa cuối**: 2018-06-18 14:48:42.953000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC  [dbo].[ThucChay_Admatic_NhieuSanPham_ByNgayThucHien] '2018-06-14','2018-06-14'
CREATE  PROCEDURE [dbo].[ThucChay_Admatic_NhieuSanPham_ByNgayThucHien] 
	 @dtStart DATETIME, 
	 @dtEnd DATETIME
AS
BEGIN

	DECLARE  @NgayThucHien DATETIME
	SET @NgayThucHien = @dtStart
	WHILE @NgayThucHien <= @dtEnd
	BEGIN
		--1. Cap nhat banner
		PRINT N'1. Cap nhat banner'
		EXEC [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic] @NgayThucHien = @NgayThucHien

		--2. Tinh Gia tri thay doi khi thay doi Thanh tien hoac chiet khau --CHO NAY CAN XEM LAI
		PRINT N'2. Tinh Gia tri thay doi khi thay doi Thanh tien hoac chiet khau --CHO NAY CAN XEM LAI'
		EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham] @NgayThucHien = @NgayThucHien

		--3. Tinh Gia tri thay doi khi thay doi don gia banner 
		PRINT N'3. Tinh Gia tri thay doi khi thay doi don gia banner'
		EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner] @NgayThucHien = @NgayThucHien

		--4. Cap nhat thu tu thuc chay
		PRINT N'4. Cap nhat thu tu thuc chay'
		EXEC [dbo].[ThucChay_Update_AdmaticThuTuChayHopDongChiTiet] @NgayThucHien = @NgayThucHien

		--5. Tinh thuc chay
		PRINT N'5. Tinh thuc chay'
		EXEC [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_NhieuSanPham]  @NgayThucHien = @NgayThucHien

		--5.2 Adx - Admatic
		PRINT N'Adx - Admatic'
		EXEC [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_Adx] 	@NgayThucHien = @NgayThucHien

		--6. thuc hien xu ly lech treo ha
		PRINT N'7. thuc hien xu ly lech treo ha'
		EXEC [dbo].[ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug] @NgayThucHien = @NgayThucHien

		--7. Tinh gia tri thay doi khi thay doi nhan hang treo 
		PRINT N'8. Tinh gia tri thay doi khi thay doi nhan hang treo'
		EXEC [dbo].[ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham] @NgayThucHien = @NgayThucHien

		--8. Cap nhat gia tri thuc chay va trang thai cho table admaticthututhucchayhopdongchitiet
		PRINT N'6. Cap nhat gia tri thuc chay va trang thai cho table admaticthututhucchayhopdongchitiet'
		EXEC [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay] @NgayThucHien = @NgayThucHien

		SET @NgayThucHien = DATEADD(DAY,1,@NgayThucHien)
	END
END

```
