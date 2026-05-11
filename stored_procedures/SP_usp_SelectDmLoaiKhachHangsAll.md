# Stored Procedure: `usp_SelectDmLoaiKhachHangsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:06.827000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.137000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmLoaiKhachHangsAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmLoaiKhachHangsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmLoaiKhachHangID],
	[MaLoaiKhachHang],
	[TenLoaiKhachHang],
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
	[dbo].[DmLoaiKhachHang]
Where DeletedStatus <> 1
--endregion

```
