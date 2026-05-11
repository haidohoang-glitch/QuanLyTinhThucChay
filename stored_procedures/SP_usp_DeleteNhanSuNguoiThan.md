# Stored Procedure: `usp_DeleteNhanSuNguoiThan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.227000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.837000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuNguoiThanID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteNhanSuNguoiThan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteNhanSuNguoiThan]
	@NhanSuNguoiThanID int
AS

SET NOCOUNT ON

Update [dbo].[NhanSuNguoiThan]
Set DeletedStatus = 1
WHERE
	[NhanSuNguoiThanID] = @NhanSuNguoiThanID

--endregion

```
