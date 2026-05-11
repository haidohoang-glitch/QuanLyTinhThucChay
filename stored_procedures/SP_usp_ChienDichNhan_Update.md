# Stored Procedure: `usp_ChienDichNhan_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:57.940000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.407000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChienDichID` | `int(4)` | No |
| `@TenChienDich` | `nvarchar` | No |
| `@Ghichu` | `nvarchar(2048)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_ChienDichNhan_Update]
	@DmChienDichID INT,
	@TenChienDich NVARCHAR(MAX),
	@Ghichu NVARCHAR(1024),
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT
AS
BEGIN
	SET NOCOUNT ON;
	
	UPDATE [dbo].[DmChienDichNhanhang]
	SET    [TenChienDich]     = @TenChienDich,
	       [Ghichu]           = @Ghichu,
	       [LastModidfiedBy]  = @LastModidfiedBy,
	       [LastModifiedAt]   = @LastModifiedAt,
	       [DeletedStatus]    = @DeletedStatus,
	       [PrintStatus]      = @PrintStatus,
	       [RecordStatus]     = @RecordStatus
	WHERE  [DmChienDichID]    = @DmChienDichID
END

```
