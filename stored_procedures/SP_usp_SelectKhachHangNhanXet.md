# Stored Procedure: `usp_SelectKhachHangNhanXet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:21.457000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.070000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNhanXetID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangNhanXet]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangNhanXet]
	@KhachHangNhanXetID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
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
FROM
	[dbo].[KhachHangNhanXet]
WHERE
		[KhachHangNhanXetID] = @KhachHangNhanXetID
 and DeletedStatus <> 1

--endregion

```
