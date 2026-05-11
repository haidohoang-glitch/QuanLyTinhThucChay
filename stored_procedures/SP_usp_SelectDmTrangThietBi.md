# Stored Procedure: `usp_SelectDmTrangThietBi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:17.570000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.770000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTrangThietBiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmTrangThietBi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmTrangThietBi]
	@DmTrangThietBiID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmTrangThietBiID],
	[MaTrangThietBi],
	[TenTrangThietBi],
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
	[dbo].[DmTrangThietBi]
WHERE
		[DmTrangThietBiID] = @DmTrangThietBiID
 and DeletedStatus <> 1

--endregion

```
