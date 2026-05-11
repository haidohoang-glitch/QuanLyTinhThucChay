# Stored Procedure: `usp_NhanHang_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:45.827000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.147000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_Delete]
	@DmNhanHangID INT
AS
	SET NOCOUNT ON;
	BEGIN
		UPDATE [dbo].[DmNhanHang]
		SET    DeletedStatus   = 1
		WHERE  [DmNhanHangID]  = @DmNhanHangID
	END

```
