# Stored Procedure: `usp_InsertDmNghanhHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:32.383000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.943000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNghanhHangID` | `int(4)` | Yes |
| `@TenNghanhHang` | `nvarchar(100)` | No |
| `@DmNghanhHangREF` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertDmNghanhHang]
	@DmNghanhHangID INT OUTPUT,
	@TenNghanhHang NVARCHAR(50),
	@DmNghanhHangREF INT,
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT
AS
BEGIN
	SET NOCOUNT ON;
	
	INSERT INTO [dbo].[DmNghanhHang]
	  (
	    [TenNghanhHang],
	    [DmNghanhHangREF],
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
	    @TenNghanhHang,
	    @DmNghanhHangREF,
	    @CreatedBy,
	    @CreatedAt,
	    @LastModidfiedBy,
	    @LastModifiedAt,
	    @DeletedStatus,
	    @PrintStatus,
	    @RecordStatus
	  )
	SELECT @DmNghanhHangID = SCOPE_IDENTITY()
END

```
