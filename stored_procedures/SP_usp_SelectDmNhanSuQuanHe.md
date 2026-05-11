# Stored Procedure: `usp_SelectDmNhanSuQuanHe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.660000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanSuQuanHeID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmNhanSuQuanHe]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNhanSuQuanHe]
	@DmNhanSuQuanHeID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNhanSuQuanHeID],
	[MaNhanSuQuanHe],
	[TenNhanSuQuanHe],
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
	[dbo].[DmNhanSuQuanHe]
WHERE
		[DmNhanSuQuanHeID] = @DmNhanSuQuanHeID
 and DeletedStatus <> 1

--endregion

```
