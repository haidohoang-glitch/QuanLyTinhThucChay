# Stored Procedure: `usp_SelectKhachHangsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.250000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.663000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangsAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangID],
	[MaKhachHang],
	[ThongTinCaNhanREF],
	[ThongTinToChucREF],
	[DmHinhThucKhachHangREF],
	[DmLoaiKhachHangREF],
	[NguoiQuanLyREF],
	[IsTruSoChinh],
	[KhachHangREF],
	[DmTrangThaiKhachHangREF],
	[Level],
	[QuyMoCongTy],
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
	[dbo].[KhachHang]
Where DeletedStatus <> 1
--endregion

```
