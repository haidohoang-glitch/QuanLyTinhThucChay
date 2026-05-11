# Stored Procedure: `usp_DeleteDmTinhThanhPho`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:15.113000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.997000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTinhThanhPhoID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmTinhThanhPho]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmTinhThanhPho]
	@DmTinhThanhPhoID int
AS

SET NOCOUNT ON

Update [dbo].[DmTinhThanhPho]
Set DeletedStatus = 1
WHERE
	[DmTinhThanhPhoID] = @DmTinhThanhPhoID

--endregion

```
