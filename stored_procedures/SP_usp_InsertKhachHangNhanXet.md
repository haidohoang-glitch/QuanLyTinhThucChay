# Stored Procedure: `usp_InsertKhachHangNhanXet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:21.280000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.077000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNhanXetID` | `int(4)` | No |
| `@KhachHangREF` | `int(4)` | No |
| `@NgayNhanXet` | `datetime(8)` | No |
| `@NoiDungNhanXet` | `nvarchar(8000)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertKhachHangNhanXet]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertKhachHangNhanXet]
	@KhachHangNhanXetID int,
	@KhachHangREF int,
	@NgayNhanXet datetime,
	@NoiDungNhanXet nvarchar(4000),
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

INSERT INTO [dbo].[KhachHangNhanXet] (
	[KhachHangNhanXetID],
	[KhachHangREF],
	[NgayNhanXet],
	[NoiDungNhanXet],
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
	@KhachHangNhanXetID,
	@KhachHangREF,
	@NgayNhanXet,
	@NoiDungNhanXet,
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

--endregion

```
