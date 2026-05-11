# Stored Procedure: `usp_DeleteDiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:02.553000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.907000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DiaChiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDiaChi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDiaChi]
	@DiaChiID int
AS

SET NOCOUNT ON

Update [dbo].[DiaChi]
Set DeletedStatus = 1
WHERE
	[DiaChiID] = @DiaChiID

--endregion

```
