# Stored Procedure: `usp_SelectDmTinhTrangLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:16.137000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.807000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTinhTrangLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmTinhTrangLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmTinhTrangLamViec]
	@DmTinhTrangLamViecID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmTinhTrangLamViecID],
	[MaTinhTrangLamViec],
	[TenTinhTrangLamViec],
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
	[dbo].[DmTinhTrangLamViec]
WHERE
		[DmTinhTrangLamViecID] = @DmTinhTrangLamViecID
 and DeletedStatus <> 1

--endregion

```
