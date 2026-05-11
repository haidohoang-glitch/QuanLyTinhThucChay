# Stored Procedure: `ThucChay_ExecThucChayDaTinh_HopDongInventory_ByHopDongChiTietID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-01-03 11:54:55.970000
- **Ngày sửa cuối**: 2020-01-03 11:54:55.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_ExecThucChayDaTinh_HopDongInventory_ByHopDongChiTietID] 
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongREF INT, @HopDongChiTietREF INT
	, @DmSanPhamREF INT, @TenSanPham NVARCHAR(200)
	, @CreatedBy NVARCHAR(200)

	SET @NgayThucHien = ISNULL(@NgayThucHien,GETDATE())	

	--1. CHECK VA INSERT THONG TIN HOPDONG BAN INVENTORY MOI
	EXEC [dbo].[ThucChay_InsertThongTinHopDongInventory] @NgayThucHien 

	--2. CHECK VA INSERT THONG TIN THUCCHAYDATINH HOPDONGCHITIET NHAP BAN INVENTORY
	DECLARE Cursor_TCDT_Inventory CURSOR FOR

	SELECT HopDongFK, HopDongChiTietID, DmSanPhamREF, TenSanPham, CreatedBy 
	FROM dbo.HopDongChiTiet 
	WHERE DeletedStatus = 0
	AND CONVERT(DATE,CreatedAt) = @NgayThucHien
	AND HopDongFK IN 
	(	
		SELECT DISTINCT HopDongREF FROM dbo.DmThongTinHopDongBanInventory
		WHERE DeletedStatus = 0
	)
	AND HopDongChiTietID NOT IN(
		SELECT HopDongChiTietREF FROM DmThongTinHopDongBanInventory	
		WHERE ISNULL(DmSanPhamREF,0) <> 0
	)
	AND HopDongChiTietID = @HopDongChiTietID

	OPEN Cursor_TCDT_Inventory
	FETCH NEXT FROM Cursor_TCDT_Inventory INTO @HopDongREF, @HopDongChiTietREF, @DmSanPhamREF, @TenSanPham, @CreatedBy

	WHILE @@FETCH_STATUS = 0
	BEGIN

		EXEC [dbo].[ThucChay_InsertThucChayDaTinh_HopDongInventory] 
		@NgayThucHien,
		@HopDongREF,
		@HopDongChiTietREF,
		@DmSanPhamREF,
		@TenSanPham,
		@CreatedBy

		FETCH NEXT FROM Cursor_TCDT_Inventory INTO @HopDongREF, @HopDongChiTietREF, @DmSanPhamREF, @TenSanPham, @CreatedBy
	END
	CLOSE Cursor_TCDT_Inventory
	DEALLOCATE Cursor_TCDT_Inventory

END


```
