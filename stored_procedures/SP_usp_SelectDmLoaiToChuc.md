# Stored Procedure: `usp_SelectDmLoaiToChuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:08.470000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.310000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiToChucID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmLoaiToChuc]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmLoaiToChuc]
	@DmLoaiToChucID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmLoaiToChucID],
	[MaLoaiToChuc],
	[TenLoaiToChuc],
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
	[dbo].[DmLoaiToChuc]
WHERE
		[DmLoaiToChucID] = @DmLoaiToChucID
 and DeletedStatus <> 1

--endregion

```
