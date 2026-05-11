# Stored Procedure: `usp_SelectDmLinhVucLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:05.510000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.160000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLinhVucLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmLinhVucLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmLinhVucLamViec]
	@DmLinhVucLamViecID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmLinhVucLamViecID],
	[MaLinhVucLamViec],
	[TenLinhVucLamViec],
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
	[dbo].[DmLinhVucLamViec]
WHERE
		[DmLinhVucLamViecID] = @DmLinhVucLamViecID
 and DeletedStatus <> 1

--endregion

```
