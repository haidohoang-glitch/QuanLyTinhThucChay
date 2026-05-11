# Stored Procedure: `usp_SelectDmNhom`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:33:06.433000
- **Ngày sửa cuối**: 2014-10-14 10:39:42.597000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomID` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDmNhom]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNhom]
	@DmNhomID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNhomID],
	TenNhom,
	[GhiChu],
	[DmBoPhanREF],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmNhom]
WHERE
		[DmNhomID] = @DmNhomID
 and DeletedStatus <> 1

--endregion


```
