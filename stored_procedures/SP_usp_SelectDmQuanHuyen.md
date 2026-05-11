# Stored Procedure: `usp_SelectDmQuanHuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:14.623000
- **Ngày sửa cuối**: 2014-10-14 10:39:42.497000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmQuanHuyenID` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmQuanHuyen]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmQuanHuyen]
	@DmQuanHuyenID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmQuanHuyenID],
	[MaQuanHuyen],
	[TenQuanHuyen],
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
	[dbo].[DmQuanHuyen]
WHERE
		[DmQuanHuyenID] = @DmQuanHuyenID
 and DeletedStatus <> 1

--endregion


```
