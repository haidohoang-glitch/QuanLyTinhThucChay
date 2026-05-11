# Stored Procedure: `Rpt_InsertNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:35.823000
- **Ngày sửa cuối**: 2015-03-06 11:12:13.463000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHang]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate
	WHILE (@NgayThucHien <= @EndDate)
	BEGIN
		--1. Tinh gia tri cho table RptNhanHangThongTinChiTiet
		EXEC [Rpt_InsertNhanHangThongTinChiTiet] @NgayThucHien
		--2. Tinh gia tri cho table RptNhanHangThongTin
		EXEC [Rpt_InsertNhanHangThongTin] @NgayThucHien
		--3. Tinh gia tri cho table RptNhanHangHinhThucKy
		EXEC [Rpt_InsertNhanHangHinhThucKy] @NgayThucHien
		--4. Tính gia tri cho table RptNhanHangKhachHangKy
		EXEC [Rpt_InsertNhanHangKhachHangKy] @NgayThucHien
		--5. Tinh gia tri cho table RptNhanHangKenh
		EXEC [Rpt_InsertNhanHangKenh] @NgayThucHien
		--6. Tinh gia tri cho table RptNhanHangNhanSu
		EXEC [Rpt_InsertNhanHangNhanSu] @NgayThucHien
		--7. Tinh gia tri cho table RptNhanHangSanPham
		EXEC [Rpt_InsertNhanHangSanPham] @NgayThucHien
		
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
		PRINT @NgayThucHien
	END
END

--EXEC [dbo].[Rpt_InsertNhanHang] '2014-01-01', '2015-12-31'

```
