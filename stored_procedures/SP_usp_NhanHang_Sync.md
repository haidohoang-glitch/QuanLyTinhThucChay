# Stored Procedure: `usp_NhanHang_Sync`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:49.047000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.047000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |
| `@DmNhanHangThayDoiID` | `int(4)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_Sync]
	@DmNhanHangID INT,
	@DmNhanHangThayDoiID INT,
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME
AS
BEGIN
	
	SET NOCOUNT ON;
	
	UPDATE [dbo].[DmNhanHang]
	SET    [DmNhanHangThayDoiID]   = @DmNhanHangThayDoiID,
	       [LastModidfiedBy]       = @LastModidfiedBy,
	       [LastModifiedAt]        = @LastModifiedAt,
	       [DeletedStatus]         = 1,
	       [RecordStatus]          = 1
	WHERE  [DmNhanHangID]          = @DmNhanHangID
END

```
