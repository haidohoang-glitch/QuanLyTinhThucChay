# Stored Procedure: `usp_SelectDmDatNuoc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:03.943000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.197000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmDatNuocID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmDatNuoc]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmDatNuoc]
	@DmDatNuocID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmDatNuocID],
	[MaDatNuoc],
	[TenDatNuoc],
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
	[dbo].[DmDatNuoc]
WHERE
		[DmDatNuocID] = @DmDatNuocID
 and DeletedStatus <> 1

--endregion

```
