# Stored Procedure: `usp_SelectDmTrangThaiKhachHangsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:17.073000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.783000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmTrangThaiKhachHangsAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmTrangThaiKhachHangsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmTrangThaiKhachHangID],
	[MaTrangThaiKhachHang],
	[TenTrangThaiKhachHang],
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
	[dbo].[DmTrangThaiKhachHang]
Where DeletedStatus <> 1
--endregion

```
