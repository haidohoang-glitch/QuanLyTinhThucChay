# Stored Procedure: `usp_SelectKhachHangChienDich`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.597000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.647000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangChienDichID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangChienDich]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangChienDich]
	@KhachHangChienDichID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangChienDichID],
	[MaChienDich],
	[TenChienDich],
	[NgayBatDau],
	[NgayKetThuc],
	[NoiDungChienDich],
	[KhachHangREF],
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
	[dbo].[KhachHangChienDich]
WHERE
		[KhachHangChienDichID] = @KhachHangChienDichID
 and DeletedStatus <> 1

--endregion

```
