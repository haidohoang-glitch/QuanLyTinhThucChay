# Stored Procedure: `usp_DeleteAdminPermisionHDCN`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-06 17:01:42.223000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminPermisionHDCNID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_DeleteAdminPermisionHDCN]
-- Create Date: Friday, September 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteAdminPermisionHDCN]
	@AdminPermisionHDCNID int
AS

SET NOCOUNT ON

Update [dbo].[AdminPermisionHDCN]
Set DeletedStatus = 1
WHERE
	[AdminPermisionHDCNID] = @AdminPermisionHDCNID

--endregion

```
