# Stored Procedure: `usp_SelectDmHinhThucNhanSu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:04.983000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.177000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmHinhThucNhanSuID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmHinhThucNhanSu]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmHinhThucNhanSu]
	@DmHinhThucNhanSuID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmHinhThucNhanSuID],
	[MaHinhThucNhanSu],
	[TenHinhThucNhanSu],
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
	[dbo].[DmHinhThucNhanSu]
WHERE
		[DmHinhThucNhanSuID] = @DmHinhThucNhanSuID
 and DeletedStatus <> 1

--endregion

```
