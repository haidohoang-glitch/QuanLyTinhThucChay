# Stored Procedure: `ThucChay_CapNhatTTTC_Admatic_NhieuSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-07-03 14:50:29.827000
- **Ngày sửa cuối**: 2017-07-03 14:52:45.960000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_CapNhatTTTC_Admatic_NhieuSanPham] 
CREATE  PROCEDURE [dbo].[ThucChay_CapNhatTTTC_Admatic_NhieuSanPham] 
	
AS
BEGIN
	DECLARE @HopDongID INT, @HopDongChiTietID INT, @NgayThucHien DATETIME
	
	SET @NgayThucHien = '2017-07-02'

	DECLARE Cursor_cptttc CURSOR FOR
		SELECT A.HopDongID, A.HopDongChiTietREF
		FROM
		(
			SELECT HopDongID, HopDongChiTietREF, SUM(ThanhTienSauTrietKhauThucChay +GiaTriThayDoi)thanhtientc 
			, SUM(ThanhTienKM + GiaTriKMThayDoi)thanhtientcKM
			FROM dbo.ThucChayDaTinh
			WHERE DmHinhThucQuangCao = 42
			GROUP BY HopDongID, HopDongChiTietREF
		)A
		LEFT JOIN dbo.AdmaticThuTuChayHopDongChiTiet tt ON a.HopDongID = tt.HopDongFK AND a.HopDongChiTietREF = tt.HopDongChiTietID
		WHERE (ABS(a.thanhtientc - ISNULL(tt.ThanhtienThucChay,0)) >2) 

	OPEN Cursor_cptttc
	FETCH NEXT FROM Cursor_cptttc INTO @HopDongID,@HopDongChiTietID
	WHILE @@FETCH_STATUS =0
	BEGIN
		--Update lai thu tu tinh thuc chay cho hopdongchitiet
		EXEC [ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] @NgayThucHien,@HopDongChiTietID
	FETCH NEXT FROM Cursor_cptttc INTO @HopDongID, @HopDongChiTietID
	END
	CLOSE Cursor_cptttc;
	DEALLOCATE Cursor_cptttc;
	
	--SELECT 1;
END

```
