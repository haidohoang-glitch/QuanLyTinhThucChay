# Stored Procedure: `usp_UpdateDmNghanhHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:31.390000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.023000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNghanhHangID` | `int(4)` | No |
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
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_UpdateDmNghanhHang]
-- Create Date: Monday, November 18, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmNghanhHang]
	@DmNghanhHangID int,
	@TenNghanhHang nvarchar(50),
	@DmNghanhHangREF int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModidfiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[DmNghanhHang] SET
	[TenNghanhHang] = @TenNghanhHang,
	[DmNghanhHangREF] = @DmNghanhHangREF,
	[LastModidfiedBy] = @LastModidfiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmNghanhHangID] = @DmNghanhHangID

--endregion

```
