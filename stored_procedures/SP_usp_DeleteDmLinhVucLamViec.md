# Stored Procedure: `usp_DeleteDmLinhVucLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:05.460000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLinhVucLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmLinhVucLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmLinhVucLamViec]
	@DmLinhVucLamViecID int
AS

SET NOCOUNT ON

Update [dbo].[DmLinhVucLamViec]
Set DeletedStatus = 1
WHERE
	[DmLinhVucLamViecID] = @DmLinhVucLamViecID

--endregion

```
