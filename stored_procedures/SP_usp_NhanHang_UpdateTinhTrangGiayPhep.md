# Stored Procedure: `usp_NhanHang_UpdateTinhTrangGiayPhep`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:27:02.950000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanhangID` | `int(4)` | No |
| `@TinhTrangGiayPhep` | `smallint(2)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_UpdateTinhTrangGiayPhep]
	@DmNhanhangID INT,
	@TinhTrangGiayPhep SMALLINT
AS
BEGIN
	UPDATE DmNhanHang 
	SET TinhTrangGiayPhep = @TinhTrangGiayPhep,
		LastModifiedAt = GETDATE()
	WHERE DmNhanHangID = @DmNhanhangID
END

```
