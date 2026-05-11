# Stored Procedure: `ThucChay_UpdateThutuThucChay_Admatic_Adx`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-06-07 15:51:08.600000
- **Ngày sửa cuối**: 2018-06-29 14:04:28.343000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
 EXEC [dbo].[ThucChay_UpdateThutuThucChay_Admatic_Adx]
*/
CREATE  PROCEDURE [dbo].[ThucChay_UpdateThutuThucChay_Admatic_Adx] 
	
AS
BEGIN
	DECLARE @HopDongChiTietID INT,@NgayThucHien DATETIME
	SET @NgayThucHien = '2018-06-27'
	
	DECLARE Cursor_tttc_AdmaticAdx CURSOR FOR
		--1. Xac dinh thuc chay hop dong Admatic Adx
	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet
	WHERE DmLoaiREF = 42
	AND DmSanPhamREF = 585

	OPEN Cursor_tttc_AdmaticAdx
	FETCH NEXT FROM Cursor_tttc_AdmaticAdx INTO @HopDongChiTietID
	WHILE @@FETCH_STATUS =0
	BEGIN
		EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
		@NgayThucHien = @NgayThucHien,
		@HopDongChiTietID = @HopDongChiTietID
	FETCH NEXT FROM Cursor_tttc_AdmaticAdx INTO @HopDongChiTietID
	END
	CLOSE Cursor_tttc_AdmaticAdx;
	DEALLOCATE Cursor_tttc_AdmaticAdx;
	
	--SELECT 1;
END

```
