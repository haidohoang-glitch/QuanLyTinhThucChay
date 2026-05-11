# Stored Procedure: `usp_SelectDmMucDoUuTien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:09.857000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.290000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmMucDoUuTienID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmMucDoUuTien]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmMucDoUuTien]
	@DmMucDoUuTienID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmMucDoUuTienID],
	[MaMucDoUuTien],
	[TenMucDoUuTien],
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
	[dbo].[DmMucDoUuTien]
WHERE
		[DmMucDoUuTienID] = @DmMucDoUuTienID
 and DeletedStatus <> 1

--endregion

```
