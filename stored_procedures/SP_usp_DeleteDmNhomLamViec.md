# Stored Procedure: `usp_DeleteDmNhomLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:11.827000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmNhomLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmNhomLamViec]
	@DmNhomLamViecID int
AS

SET NOCOUNT ON

Update [dbo].[DmNhomLamViec]
Set DeletedStatus = 1
WHERE
	[DmNhomLamViecID] = @DmNhomLamViecID

--endregion

```
