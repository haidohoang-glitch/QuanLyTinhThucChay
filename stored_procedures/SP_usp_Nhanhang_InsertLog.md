# Stored Procedure: `usp_Nhanhang_InsertLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:49.333000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.690000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@LastLogTime` | `datetime(8)` | No |
| `@LastLogSystem` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Nhanhang_InsertLog]
	@DmNhanHangID INT,
	@PrintStatus INT,
	@LastLogTime DATETIME,
	@LastLogSystem NVARCHAR(50)
AS
BEGIN
	SET NOCOUNT ON;
	UPDATE DmNhanHang
	SET    PrintStatus = @PrintStatus,
	       LastLogTime = @LastLogSystem,
	       LastLogSystem = @LastLogSystem
	WHERE  DmNhanHangID = @DmNhanHangID
END

```
