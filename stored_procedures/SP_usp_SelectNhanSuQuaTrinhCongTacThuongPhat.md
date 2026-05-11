# Stored Procedure: `usp_SelectNhanSuQuaTrinhCongTacThuongPhat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.567000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.947000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuQuaTrinhCongTacThuongPhatID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuQuaTrinhCongTacThuongPhat]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuQuaTrinhCongTacThuongPhat]
	@NhanSuQuaTrinhCongTacThuongPhatID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuQuaTrinhCongTacThuongPhatID],
	[NhanSuSoYeuLyLichREF],
	[SoHieu],
	[GhiChu],
	[Active],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[NhanSuQuaTrinhCongTacThuongPhat]
WHERE
		[NhanSuQuaTrinhCongTacThuongPhatID] = @NhanSuQuaTrinhCongTacThuongPhatID
 and DeletedStatus <> 1

--endregion

```
