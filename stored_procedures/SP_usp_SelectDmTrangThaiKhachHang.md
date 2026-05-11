# Stored Procedure: `usp_SelectDmTrangThaiKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:17.043000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.787000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTrangThaiKhachHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmTrangThaiKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmTrangThaiKhachHang]
	@DmTrangThaiKhachHangID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmTrangThaiKhachHangID],
	[MaTrangThaiKhachHang],
	[TenTrangThaiKhachHang],
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
	[dbo].[DmTrangThaiKhachHang]
WHERE
		[DmTrangThaiKhachHangID] = @DmTrangThaiKhachHangID
 and DeletedStatus <> 1

--endregion

```
