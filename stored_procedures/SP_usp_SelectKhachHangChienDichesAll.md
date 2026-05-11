# Stored Procedure: `usp_SelectKhachHangChienDichesAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.797000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.643000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangChienDichesAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangChienDichesAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangChienDichID],
	[MaChienDich],
	[TenChienDich],
	[NgayBatDau],
	[NgayKetThuc],
	[NoiDungChienDich],
	[KhachHangREF],
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
	[dbo].[KhachHangChienDich]
Where DeletedStatus <> 1
--endregion

```
