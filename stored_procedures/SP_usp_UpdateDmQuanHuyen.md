# Stored Procedure: `usp_UpdateDmQuanHuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:14.380000
- **Ngày sửa cuối**: 2014-10-14 10:39:39.387000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmQuanHuyenID` | `int(4)` | No |
| `@MaQuanHuyen` | `nvarchar(100)` | No |
| `@TenQuanHuyen` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateDmQuanHuyen]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmQuanHuyen]
	@DmQuanHuyenID int,
	@MaQuanHuyen nvarchar(50),
	@TenQuanHuyen nvarchar(200),
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[DmQuanHuyen] SET
	[MaQuanHuyen] = @MaQuanHuyen,
	[TenQuanHuyen] = @TenQuanHuyen,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmQuanHuyenID] = @DmQuanHuyenID

--endregion


```
