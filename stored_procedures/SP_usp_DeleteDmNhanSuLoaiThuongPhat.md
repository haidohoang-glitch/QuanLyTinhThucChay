# Stored Procedure: `usp_DeleteDmNhanSuLoaiThuongPhat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.460000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.240000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanSuLoaiThuongPhatID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmNhanSuLoaiThuongPhat]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmNhanSuLoaiThuongPhat]
	@DmNhanSuLoaiThuongPhatID int
AS

SET NOCOUNT ON

Update [dbo].[DmNhanSuLoaiThuongPhat]
Set DeletedStatus = 1
WHERE
	[DmNhanSuLoaiThuongPhatID] = @DmNhanSuLoaiThuongPhatID

--endregion

```
