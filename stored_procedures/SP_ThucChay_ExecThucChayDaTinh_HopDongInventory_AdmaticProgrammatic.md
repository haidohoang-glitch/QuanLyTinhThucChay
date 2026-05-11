# Stored Procedure: `ThucChay_ExecThucChayDaTinh_HopDongInventory_AdmaticProgrammatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-04-14 11:33:19.650000
- **Ngày sửa cuối**: 2025-12-22 09:39:59.560000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_ExecThucChayDaTinh_HopDongInventory_AdmaticProgrammatic] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongREF INT, @HopDongChiTietREF INT, @NgayDanhSoGioiHanMKT_FEE_PRO DATETIME = '2025-10-10'
	, @DmSanPhamREF INT, @TenSanPham NVARCHAR(200)
	, @CreatedBy NVARCHAR(200)
	, @BfDate DATETIME

	SET @BfDate = convert(date,dateadd(day,-1,GETDATE()))
	SET @NgayThucHien = ISNULL(@NgayThucHien,@BfDate)	

	--1. CHECK VA INSERT THONG TIN HOPDONG BAN INVENTORY MOI
	EXEC [dbo].[ThucChay_InsertThongTinHopDongInventory] @NgayThucHien 

	--2. CHECK VA INSERT THONG TIN THUCCHAYDATINH HOPDONGCHITIET NHAP BAN INVENTORY
	DECLARE Cursor_TCDT_Admatic_Inventory CURSOR FOR

	SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.CreatedBy 
	FROM dbo.HopDongChiTiet hdct
	INNER JOIN dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID
	WHERE hdct.DeletedStatus = 0
	AND hdct.HopDongFK IN 
	(	
		SELECT DISTINCT HopDongREF FROM dbo.DmThongTinHopDongBanInventory
		WHERE DeletedStatus = 0
	)
	AND hdct.HopDongChiTietID NOT IN(
		SELECT HopDongChiTietREF FROM DmThongTinHopDongBanInventory	
		WHERE ISNULL(DmSanPhamREF,0) <> 0
	)
	AND (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9 AND (hdct.DmSanPhamREF NOT IN (733,817) or ((hdct.DmSanPhamREF = 817)   AND (hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHanMKT_FEE_PRO)))
	) --Tinh cho phan bo Admatic , Direct Tag
	--AND (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9 AND (hdct.DmSanPhamREF NOT IN (733,817))) --Tinh cho phan bo Admatic , Direct Tag
	--AND (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9 AND (hdct.DmSanPhamREF NOT IN (733))) --Tinh cho phan bo Admatic , Direct Tag, Them viec tinh cho MKT-FEE ngày 02/12/2025
	
	AND (EXISTS(SELECT TOP (1) tchdct.HopDongChiTietREF FROM dbo.ThucChayHopDongChiTiet tchdct 
		WHERE tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
		AND tchdct.DmSanPhamREF = hdct.DmSanPhamREF
		AND tchdct.DeletedStatus = 0
		AND (
			CONVERT(DATE,tchdct.LastModifiedAt) = @NgayThucHien--LAM THEO NGAY THUC TREO HAIDH COMMENT 29/04/2021
			OR(Convert(date,hdct.LastModifiedAt) = @NgayThucHien) --HAIDH COMMENT CO THE BAT THEO CA NGAY HOPDONGCHITIET THAY DOI
			)--HAIDH COMMENT FIX LOI TU NGAY 28/06/2021
		ORDER BY tchdct.HopDongChiTietREF
		)
	)
	OPEN Cursor_TCDT_Admatic_Inventory
	FETCH NEXT FROM Cursor_TCDT_Admatic_Inventory INTO @HopDongREF, @HopDongChiTietREF, @DmSanPhamREF, @TenSanPham, @CreatedBy

	WHILE @@FETCH_STATUS = 0
	BEGIN
		IF(EXISTS(SELECT top (1) * FROM dbo.ThucChayDaTinh tcdt
		WHERE tcdt.HopDongID = @HopDongREF 
		AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
		AND tcdt.NgayThucHien = @NgayThucHien
		AND tcdt.DotChayBooking <> N'HDBAN_INVENTORY'
		ORDER BY tcdt.HopDongChiTietREF))
		BEGIN
			DELETE FROM dbo.ThucChayDaTinh
			WHERE HopDongID = @HopDongREF
			AND HopDongChiTietREF = @HopDongChiTietREF
			AND NgayThucHien = @NgayThucHien
			AND DotChayBooking <> N'HDBAN_INVENTORY'
			AND  DmHinhThucQuangCao = 42
		END
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
