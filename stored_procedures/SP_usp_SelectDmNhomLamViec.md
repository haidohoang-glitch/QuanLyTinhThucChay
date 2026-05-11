# Stored Procedure: `usp_SelectDmNhomLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:11.923000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.720000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmNhomLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNhomLamViec]
	@DmNhomLamViecID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNhomLamViecID],
	[MaNhomLamViec],
	[TenNhomLamViec],
	[DmBoPhanREF],
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
	[dbo].[DmNhomLamViec]
WHERE
		[DmNhomLamViecID] = @DmNhomLamViecID
 and DeletedStatus <> 1

--endregion

```
