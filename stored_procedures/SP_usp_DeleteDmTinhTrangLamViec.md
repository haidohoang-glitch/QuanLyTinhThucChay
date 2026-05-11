# Stored Procedure: `usp_DeleteDmTinhTrangLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:16.050000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.817000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTinhTrangLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmTinhTrangLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmTinhTrangLamViec]
	@DmTinhTrangLamViecID int
AS

SET NOCOUNT ON

Update [dbo].[DmTinhTrangLamViec]
Set DeletedStatus = 1
WHERE
	[DmTinhTrangLamViecID] = @DmTinhTrangLamViecID

--endregion

```
