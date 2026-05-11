# Stored Procedure: `usp_SelectDmChucDanh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:03.540000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChucDanhID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmChucDanh]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmChucDanh]
	@DmChucDanhID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmChucDanhID],
	[MaChucDanh],
	[TenChucDanh],
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
	[dbo].[DmChucDanh]
WHERE
		[DmChucDanhID] = @DmChucDanhID
 and DeletedStatus <> 1

--endregion

```
