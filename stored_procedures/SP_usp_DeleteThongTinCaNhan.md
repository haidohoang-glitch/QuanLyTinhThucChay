# Stored Procedure: `usp_DeleteThongTinCaNhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:24.547000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.450000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinCaNhanID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteThongTinCaNhan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteThongTinCaNhan]
	@ThongTinCaNhanID int
AS

SET NOCOUNT ON

Update [dbo].[ThongTinCaNhan]
Set DeletedStatus = 1
WHERE
	[ThongTinCaNhanID] = @ThongTinCaNhanID

--endregion

```
