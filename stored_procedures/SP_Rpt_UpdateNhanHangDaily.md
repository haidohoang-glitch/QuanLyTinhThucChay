# Stored Procedure: `Rpt_UpdateNhanHangDaily`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:36.073000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.173000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_UpdateNhanHangDaily]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @NgayDanhSoHopDong DATETIME
	SET @NgayThucHien = CONVERT(date,@NgayThucHien)
	--TINH DOANH SO CHO NHAN HANG
	DECLARE Record_Cursor_tong CURSOR FOR 
	SELECT distinct hd.NgayDanhSoHopDong
		FROM HopDong hd INNER JOIN  
		HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hd.TrangThaiHopDong <> 3
		AND hd.IsBanCung = 1
		AND CONVERT(date, 
			(
			CASE WHEN hdct.CreatedAt >= hdct.LastModifiedAt THEN hdct.CreatedAt
				ELSE hdct.LastModifiedAt
			END
			)
		) = CONVERT(DATE,@NgayThucHien)
	OPEN Record_Cursor_tong
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_tong into @NgayDanhSoHopDong
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--1. Tinh du lieu doanh so ky 2 dau theo ngay danh so hop dong
		EXEC dbo.Rpt_InsertNhanHang @NgayDanhSoHopDong, @NgayDanhSoHopDong
		FETCH NEXT FROM Record_Cursor_tong into @NgayDanhSoHopDong
	END
	CLOSE Record_Cursor_tong
	DEALLOCATE Record_Cursor_tong
	--TINH THUC CHAY CHO NHAN HANG
	--1. Tinh thuc chay cho cac san pham tren table ThucChayDaTinh
	EXEC [dbo].[Rpt_InsertNhanHang_ThucChayFull] @NgayThucHien, @NgayThucHien
	--2. Tinh thuc chay cho cac san pham cua Admarket tren table ThucChayDaTinhAdmarketHopDong
	EXEC [dbo].[Rpt_InsertNhanHang_ThucChayFullCPC] @NgayThucHien, @NgayThucHien 
END

--EXEC [dbo].[Rpt_UpdateNhanHangDaily] '2014-04-02'

```
