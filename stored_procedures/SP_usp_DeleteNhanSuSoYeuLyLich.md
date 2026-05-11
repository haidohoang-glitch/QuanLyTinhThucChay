# Stored Procedure: `usp_DeleteNhanSuSoYeuLyLich`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.810000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.577000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteNhanSuSoYeuLyLich]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteNhanSuSoYeuLyLich]
	@NhanSuSoYeuLyLichID int
AS

SET NOCOUNT ON

Update [dbo].[NhanSuSoYeuLyLich]
Set DeletedStatus = 1
WHERE
	[NhanSuSoYeuLyLichID] = @NhanSuSoYeuLyLichID

--endregion

```
