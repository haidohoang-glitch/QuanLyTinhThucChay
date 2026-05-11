# Stored Procedure: `usp_DeleteNhanSuThuongPhat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.910000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.480000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuThuongPhatID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteNhanSuThuongPhat]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteNhanSuThuongPhat]
	@NhanSuThuongPhatID int
AS

SET NOCOUNT ON

Update [dbo].[NhanSuThuongPhat]
Set DeletedStatus = 1
WHERE
	[NhanSuThuongPhatID] = @NhanSuThuongPhatID

--endregion

```
