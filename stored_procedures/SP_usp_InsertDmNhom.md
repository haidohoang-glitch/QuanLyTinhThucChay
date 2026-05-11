# Stored Procedure: `usp_InsertDmNhom`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:33:05.930000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.920000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomID` | `int(4)` | No |
| `@TenNhom` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_InsertDmNhom]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDmNhom]
	@DmNhomID int,
	@TenNhom nvarchar(200),
	@GhiChu nvarchar(255),
	@DmBoPhanREF int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

if(exists(select * from DmNhom where DmNhomID = @DmNhomID))
UPDATE [dbo].[DmNhom] SET
	TenNhom = @TenNhom,
	[GhiChu] = @GhiChu,
	[DmBoPhanREF] = @DmBoPhanREF,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmNhomID] = @DmNhomID
else
INSERT INTO [dbo].[DmNhom] (
	[DmNhomID],
	TenNhom,
	[GhiChu],
	[DmBoPhanREF],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
) VALUES (
	@DmNhomID,
	@TenNhom,
	@GhiChu,
	@DmBoPhanREF,
	@CreatedBy,
	@CreatedAt,
	@LastModifiedBy,
	@LastModifiedAt,
	@DeletedStatus,
	@PrintStatus,
	@RecordStatus
)

--endregion

```
