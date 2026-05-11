# Stored Procedure: `usp_SelectDmNghanhHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:31.917000
- **Ngày sửa cuối**: 2014-10-14 10:39:43.233000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNghanhHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_SelectDmNghanhHang]
-- Create Date: Monday, November 18, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNghanhHang]
	@DmNghanhHangID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNghanhHangID],
	[TenNghanhHang],
	[DmNghanhHangREF],
	[CreatedBy],
	[CreatedAt],
	[LastModidfiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmNghanhHang]
WHERE
		[DmNghanhHangID] = @DmNghanhHangID
 and DeletedStatus <> 1

--endregion

```
