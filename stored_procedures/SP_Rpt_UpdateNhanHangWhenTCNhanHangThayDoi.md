# Stored Procedure: `Rpt_UpdateNhanHangWhenTCNhanHangThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:35.107000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.787000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_UpdateNhanHangWhenTCNhanHangThayDoi]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @DmNhanHang INT
	SET @NgayThucHien = CONVERT(date,@NgayThucHien)
	
	--TINH DU LIEU THONG TIN NHAN HANG
	DECLARE Record_Cursor CURSOR FOR
	SELECT distinct dnh.DmNhanHangID FROM DmNhanHang dnh
	WHERE dnh.RecordStatus = 1
	AND dnh.DeletedStatus = 0
	AND CONVERT(date,
		( 
			CASE WHEN dnh.CreatedAt >= dnh.LastModifiedAt THEN dnh.CreatedAt 
				ELSE dnh.LastModifiedAt
			END
		)
	) = @NgayThucHien 
		
	OPEN Record_Cursor
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @DmNhanHang 
	WHILE @@FETCH_STATUS = 0
		BEGIN
		--XOA DANH SO THUC CHAY CUA NHAN
		DELETE FROM RptNhanHangThucChayFull
		WHERE DmNhanHangREF = @DmNhanHang
		--TINH DOANH SO THUC CHAY CHO NHAN
		--1. Tinh Thuc chay cho	cac san pham khong phai la Admarket va Boxapp SelfServing, hosting, facebook
		EXEC  dbo.Rpt_InsertNhanHangThucChayFullByNhanHang @DmNhanHang
		--2. Tinh thuc chay cho cac san pham la Boxapp Selfserving, hosting, facebook
		EXEC  dbo.Rpt_InsertNhanHangThucChayFullKhacByNhanHang @DmNhanHang
		--3. Tinh thuc chay cho cac san pham la CPC
		EXEC dbo.Rpt_InsertNhanHangThucChayFullCPCByNhanHang @DmNhanHang
		FETCH NEXT FROM Record_Cursor INTO @DmNhanHang 
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	--SELECT '1'
END

--EXEC [dbo].[Rpt_UpdateNhanHangWhenTCNhanHangThayDoi] '2013-01-01'

```
