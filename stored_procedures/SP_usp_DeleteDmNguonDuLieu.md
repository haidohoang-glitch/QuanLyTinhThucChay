# Stored Procedure: `usp_DeleteDmNguonDuLieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:09.997000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.603000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNguonDuLieuID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmNguonDuLieu]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmNguonDuLieu]
	@DmNguonDuLieuID int
AS

SET NOCOUNT ON

Update [dbo].[DmNguonDuLieu]
Set DeletedStatus = 1
WHERE
	[DmNguonDuLieuID] = @DmNguonDuLieuID

--endregion

```
