# Stored Procedure: `usp_SelectDmNhanSuLoaiThuongPhatsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.520000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.227000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmNhanSuLoaiThuongPhatsAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNhanSuLoaiThuongPhatsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNhanSuLoaiThuongPhatID],
	[MaNhanSuLoaiThuongPhat],
	[TenNhanSuLoaiThuongPhat],
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
	[dbo].[DmNhanSuLoaiThuongPhat]
Where DeletedStatus <> 1
--endregion

```
