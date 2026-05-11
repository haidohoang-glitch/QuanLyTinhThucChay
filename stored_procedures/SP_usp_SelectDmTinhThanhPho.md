# Stored Procedure: `usp_SelectDmTinhThanhPho`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:15.227000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.947000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTinhThanhPhoID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmTinhThanhPho]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmTinhThanhPho]
	@DmTinhThanhPhoID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmTinhThanhPhoID],
	[MaTinhThanhPho],
	[TenTinhThanhPho],
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
	[dbo].[DmTinhThanhPho]
WHERE
		[DmTinhThanhPhoID] = @DmTinhThanhPhoID
 and DeletedStatus <> 1

--endregion

```
