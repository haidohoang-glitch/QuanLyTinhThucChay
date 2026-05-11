# Stored Procedure: `usp_UpdateKhachHangNhanXet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:21.343000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.063000

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
-- Stored Procedure Name: [dbo].[usp_UpdateKhachHangNhanXet]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateKhachHangNhanXet]
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

UPDATE [dbo].[KhachHangNhanXet] SET
	[KhachHangREF] = @KhachHangREF,
	[NgayNhanXet] = @NgayNhanXet,
	[NoiDungNhanXet] = @NoiDungNhanXet,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[KhachHangNhanXetID] = @KhachHangNhanXetID

--endregion

```
