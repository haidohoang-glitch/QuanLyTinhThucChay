# Stored Procedure: `usp_DeleteDmHinhThucNhanSu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:04.933000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.183000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmHinhThucNhanSuID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmHinhThucNhanSu]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmHinhThucNhanSu]
	@DmHinhThucNhanSuID int
AS

SET NOCOUNT ON

Update [dbo].[DmHinhThucNhanSu]
Set DeletedStatus = 1
WHERE
	[DmHinhThucNhanSuID] = @DmHinhThucNhanSuID

--endregion

```
