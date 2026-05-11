# Stored Procedure: `usp_InsertUpdateDmNghanhHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:32.170000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNghanhHangID` | `int(4)` | No |
| `@TenNghanhHang` | `nvarchar(256)` | No |
| `@DmNghanhHangREF` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertUpdateDmNghanhHang]
	@DmNghanhHangID INT,
	@TenNghanhHang NVARCHAR(128),
	@DmNghanhHangREF INT,
	@CreatedBy NVARCHAR(50),
	@LastModidfiedBy NVARCHAR(50)
AS
	SET NOCOUNT ON;
	
	IF EXISTS(
	       SELECT [DmNghanhHangID]
	       FROM   [dbo].[DmNghanhHang]
	       WHERE  [DmNghanhHangID] = @DmNghanhHangID
	   )
	BEGIN
	    UPDATE [dbo].[DmNghanhHang]
	    SET    [TenNghanhHang]           = @TenNghanhHang,
	           [DmNghanhHangREF]       = @DmNghanhHangREF,
	           [LastModidfiedBy]       = @LastModidfiedBy,
	           [LastModifiedAt]        = GETDATE()
	    WHERE  [DmNghanhHangID]          = @DmNghanhHangID
	END
	ELSE
	BEGIN
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
	        GETDATE(),
	        @CreatedBy,
	        GETDATE(),
	        0,
	        0,
	        1
	      )
	END

```
