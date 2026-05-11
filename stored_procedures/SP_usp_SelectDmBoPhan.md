# Stored Procedure: `usp_SelectDmBoPhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:03.147000
- **Ngày sửa cuối**: 2014-10-14 10:39:43.913000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBoPhanID` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmBoPhan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmBoPhan]
	@DmBoPhanID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmBoPhanID],
	[MaBoPhan],
	[TenBoPhan],
	[DmPhongBanREF],
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
	[dbo].[DmBoPhan]
WHERE
		[DmBoPhanID] = @DmBoPhanID
 and DeletedStatus <> 1

--endregion


```
