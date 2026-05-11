# Stored Procedure: `usp_DeleteDmQuanHuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:14.547000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.783000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmQuanHuyenID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmQuanHuyen]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmQuanHuyen]
	@DmQuanHuyenID int
AS

SET NOCOUNT ON

Update [dbo].[DmQuanHuyen]
Set DeletedStatus = 1
WHERE
	[DmQuanHuyenID] = @DmQuanHuyenID

--endregion

```
