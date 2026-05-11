# Stored Procedure: `usp_DeleteNhanSuQuaTrinhCongTacThuongPhat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.543000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.953000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuQuaTrinhCongTacThuongPhatID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteNhanSuQuaTrinhCongTacThuongPhat]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteNhanSuQuaTrinhCongTacThuongPhat]
	@NhanSuQuaTrinhCongTacThuongPhatID int
AS

SET NOCOUNT ON

Update [dbo].[NhanSuQuaTrinhCongTacThuongPhat]
Set DeletedStatus = 1
WHERE
	[NhanSuQuaTrinhCongTacThuongPhatID] = @NhanSuQuaTrinhCongTacThuongPhatID

--endregion

```
