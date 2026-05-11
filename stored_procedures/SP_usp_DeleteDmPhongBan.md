# Stored Procedure: `usp_DeleteDmPhongBan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:13.833000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.810000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhongBanID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmPhongBan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmPhongBan]
	@DmPhongBanID int
AS

SET NOCOUNT ON

Update [dbo].[DmPhongBan]
Set DeletedStatus = 1
WHERE
	[DmPhongBanID] = @DmPhongBanID

--endregion

```
