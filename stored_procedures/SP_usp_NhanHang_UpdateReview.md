# Stored Procedure: `usp_NhanHang_UpdateReview`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:49.880000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.870000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_UpdateReview]
	@DmNhanHangID INT,
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME
AS
BEGIN
	
	SET NOCOUNT ON;
	
	UPDATE [dbo].[DmNhanHang]
	SET    [LastModidfiedBy]  = @LastModidfiedBy,
	       [LastModifiedAt]   = @LastModifiedAt,
	       [RecordStatus]     = 1
	WHERE  [DmNhanHangID]     = @DmNhanHangID
END

```
