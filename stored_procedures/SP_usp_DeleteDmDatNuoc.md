# Stored Procedure: `usp_DeleteDmDatNuoc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:03.870000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.900000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmDatNuocID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmDatNuoc]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmDatNuoc]
	@DmDatNuocID int
AS

SET NOCOUNT ON

Update [dbo].[DmDatNuoc]
Set DeletedStatus = 1
WHERE
	[DmDatNuocID] = @DmDatNuocID

--endregion

```
