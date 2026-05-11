# Stored Procedure: `usp_DeleteNhanSuSoYeuLyLichFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:30.117000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteNhanSuSoYeuLyLichFull]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteNhanSuSoYeuLyLichFull]
	@NhanSuSoYeuLyLichID int
AS

SET NOCOUNT ON

Update [dbo].[NhanSuSoYeuLyLichFull]
Set DeletedStatus = 1
WHERE
	[NhanSuSoYeuLyLichID] = @NhanSuSoYeuLyLichID

--endregion

```
