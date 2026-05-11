# Stored Procedure: `usp_DeleteDmChucDanh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:03.477000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.903000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChucDanhID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmChucDanh]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmChucDanh]
	@DmChucDanhID int
AS

SET NOCOUNT ON

Update [dbo].[DmChucDanh]
Set DeletedStatus = 1
WHERE
	[DmChucDanhID] = @DmChucDanhID

--endregion

```
