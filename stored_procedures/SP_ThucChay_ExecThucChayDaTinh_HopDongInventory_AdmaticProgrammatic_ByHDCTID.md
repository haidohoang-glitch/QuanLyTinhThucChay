# Stored Procedure: `ThucChay_ExecThucChayDaTinh_HopDongInventory_AdmaticProgrammatic_ByHDCTID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-04-29 16:44:09.297000
- **Ngày sửa cuối**: 2021-06-08 18:10:07.597000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_ExecThucChayDaTinh_HopDongInventory_AdmaticProgrammatic_ByHDCTID] 
	@NgayThucHien DATETIME,
	@HopDongChiTietID int
AS
BEGIN
	DECLARE @HopDongREF INT, @HopDongChiTietREF INT
	, @DmSanPhamREF INT, @TenSanPham NVARCHAR(200)
	, @CreatedBy NVARCHAR(200)

	SET @NgayThucHien = ISNULL(@NgayThucHien,GETDATE())	

	--1. CHECK VA INSERT THONG TIN HOPDONG BAN INVENTORY MOI
	EXEC [dbo].[ThucChay_InsertThongTinHopDongInventory] @NgayThucHien 

	--2. CHECK VA INSERT THONG TIN THUCCHAYDATINH HOPDONGCHITIET NHAP BAN INVENTORY
	DECLARE Cursor_TCDT_Admatic_Inventory CURSOR FOR

	SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.CreatedBy 
	FROM dbo.HopDongChiTiet hdct
	inner join 
	(SELECT TOP (1) tchdct.HopDongChiTietREF, tchdct.DmSanPhamREF, tchdct.LastModifiedAt FROM dbo.ThucChayHopDongChiTiet tchdct 
		WHERE tchdct.HopDongChiTietREF = @HopDongChiTietID
		--AND tchdct.DmSanPhamREF = hdct.DmSanPhamREF
		AND tchdct.DeletedStatus = 0
		--AND CONVERT(DATE,tchdct.LastModifiedAt) = @NgayThucHien--LAM THEO NGAY THUC TREO HAIDH COMMENT 29/04/2021
		ORDER BY tchdct.HopDongChiTietREF
	) tc on tc.HopDongChiTietREF = hdct.HopDongChiTietID and tc.DmSanPhamREF = hdct.DmSanPhamREF
	WHERE DeletedStatus = 0
	--AND CONVERT(DATE,hdct.CreatedAt) = @NgayThucHien
	AND hdct.HopDongFK IN 
	(	
		SELECT DISTINCT HopDongREF FROM dbo.DmThongTinHopDongBanInventory
		WHERE DeletedStatus = 0
	)
	--AND hdct.HopDongChiTietID NOT IN(
	--	SELECT HopDongChiTietREF FROM DmThongTinHopDongBanInventory	
	--	WHERE ISNULL(DmSanPhamREF,0) <> 0
	--)
	AND (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9 AND hdct.DmSanPhamREF <> 733) --Tinh cho phan bo Admatic , Direct Tag
	AND hdct.HopDongChiTietID = @HopDongChiTietID

	OPEN Cursor_TCDT_Admatic_Inventory
	FETCH NEXT FROM Cursor_TCDT_Admatic_Inventory INTO @HopDongREF, @HopDongChiTietREF, @DmSanPhamREF, @TenSanPham, @CreatedBy

	WHILE @@FETCH_STATUS = 0
	BEGIN

		EXEC [dbo].[ThucChay_InsertThucChayDaTinh_HopDongInventory] 
		@NgayThucHien,
		@HopDongREF,
		@HopDongChiTietREF,
		@DmSanPhamREF,
		@TenSanPham,
		@CreatedBy

		FETCH NEXT FROM Cursor_TCDT_Admatic_Inventory INTO @HopDongREF, @HopDongChiTietREF, @DmSanPhamREF, @TenSanPham, @CreatedBy
	END
	CLOSE Cursor_TCDT_Admatic_Inventory
	DEALLOCATE Cursor_TCDT_Admatic_Inventory

END


```
