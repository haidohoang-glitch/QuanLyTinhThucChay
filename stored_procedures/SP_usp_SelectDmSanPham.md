# Stored Procedure: `usp_SelectDmSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:29:23.553000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.150000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDmSanPham]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmSanPham]
	@DmSanPhamID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmSanPhamID],
	[TenSanPham],
	[GhiChu],
	[Code],
	[DmNhomSanPhamREF],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmSanPham]
WHERE
		[DmSanPhamID] = @DmSanPhamID
 and DeletedStatus <> 1

--endregion

```
