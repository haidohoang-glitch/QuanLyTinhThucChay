# Stored Procedure: `usp_SelectDmBoPhanNghiepVu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-16 11:39:02.240000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.267000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBoPhanNghiepVuID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDmBoPhanNghiepVu]
-- Create Date: Thursday, December 16, 2010
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmBoPhanNghiepVu]
	@DmBoPhanNghiepVuID nvarchar(50)
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmBoPhanNghiepVuID],
	[DmPhongBanFK],
	[TenBoPhanNghiepVu],
	[DmNgonNguREF],
	[GhiChu],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmBoPhanNghiepVu]
WHERE
		[DmBoPhanNghiepVuID] = @DmBoPhanNghiepVuID
 and DeletedStatus <> 1

--endregion

```
