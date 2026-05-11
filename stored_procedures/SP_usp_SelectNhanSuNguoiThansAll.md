# Stored Procedure: `usp_SelectNhanSuNguoiThansAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.257000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.823000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuNguoiThansAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuNguoiThansAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuNguoiThanID],
	[NhanSuSoYeuLyLichREF],
	[ThongTinCaNhanREF],
	[DmNhanSuQuanHeREF],
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
	[dbo].[NhanSuNguoiThan]
Where DeletedStatus <> 1
--endregion

```
