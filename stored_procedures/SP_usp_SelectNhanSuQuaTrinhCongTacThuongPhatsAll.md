# Stored Procedure: `usp_SelectNhanSuQuaTrinhCongTacThuongPhatsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.583000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.930000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuQuaTrinhCongTacThuongPhatsAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuQuaTrinhCongTacThuongPhatsAll]
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
Where DeletedStatus <> 1
--endregion

```
