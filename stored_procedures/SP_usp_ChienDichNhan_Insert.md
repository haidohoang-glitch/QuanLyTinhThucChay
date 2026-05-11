# Stored Procedure: `usp_ChienDichNhan_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:57.640000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenChienDich` | `nvarchar(1024)` | No |
| `@Ghichu` | `nvarchar(2048)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@DmChienDichID` | `int(4)` | Yes |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_ChienDichNhan_Insert]
	@TenChienDich NVARCHAR(512),
	@Ghichu NVARCHAR(1024),
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT,
	@DmChienDichID INT OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	
	INSERT INTO [dbo].[DmChienDichNhanhang]
	  (
	    [TenChienDich],
	    [Ghichu],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModidfiedBy],
	    [LastModifiedAt],
	    [DeletedStatus],
	    [PrintStatus],
	    [RecordStatus]
	  )
	VALUES
	  (
	    @TenChienDich,
	    @Ghichu,
	    @CreatedBy,
	    @CreatedAt,
	    @LastModidfiedBy,
	    @LastModifiedAt,
	    @DeletedStatus,
	    @PrintStatus,
	    @RecordStatus
	  )
	
	SET @DmChienDichID = SCOPE_IDENTITY()
END

```
