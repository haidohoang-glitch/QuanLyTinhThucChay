# Stored Procedure: `usp_SelectDmNguonDuLieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.027000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.527000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNguonDuLieuID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmNguonDuLieu]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNguonDuLieu]
	@DmNguonDuLieuID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNguonDuLieuID],
	[MaNguonDuLieu],
	[TenNguonDuLieu],
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
	[dbo].[DmNguonDuLieu]
WHERE
		[DmNguonDuLieuID] = @DmNguonDuLieuID
 and DeletedStatus <> 1

--endregion

```
