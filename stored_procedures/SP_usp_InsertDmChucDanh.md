# Stored Procedure: `usp_InsertDmChucDanh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:03.290000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.157000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChucDanhID` | `int(4)` | No |
| `@MaChucDanh` | `nvarchar(100)` | No |
| `@TenChucDanh` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
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
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_InsertDmChucDanh]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDmChucDanh]
	@DmChucDanhID int,
	@MaChucDanh nvarchar(50),
	@TenChucDanh nvarchar(200),
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS
BEGIN
IF(EXISTS(SELECT * FROM dbo.DmChucDanh WHERE DmChucDanhID=@DmChucDanhID AND DeletedStatus <> 1))
UPDATE [dbo].[DmChucDanh] SET
	[MaChucDanh] = @MaChucDanh,
	[TenChucDanh] = @TenChucDanh,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmChucDanhID] = @DmChucDanhID
else
INSERT INTO [dbo].[DmChucDanh] (
	[DmChucDanhID],
	[MaChucDanh],
	[TenChucDanh],
	[GhiChu],
	[Active],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
) VALUES (
	@DmChucDanhID,
	@MaChucDanh,
	@TenChucDanh,
	@GhiChu,
	@Active,
	@CreatedBy,
	@CreatedAt,
	@LastModifiedBy,
	@LastModifiedAt,
	@DeletedStatus,
	@PrintStatus,
	@RecordStatus
)

End

```
