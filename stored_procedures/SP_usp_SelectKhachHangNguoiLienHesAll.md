# Stored Procedure: `usp_SelectKhachHangNguoiLienHesAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:21.167000
- **Ngày sửa cuối**: 2014-10-14 10:39:41.537000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangNguoiLienHesAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangNguoiLienHesAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangNguoiLienHeID],
	[KhachHangREF],
	[ThongTinCaNhanREF],
	[DmNguonDuLieuREF],
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
	[dbo].[KhachHangNguoiLienHe]
Where DeletedStatus <> 1
--endregion


```
