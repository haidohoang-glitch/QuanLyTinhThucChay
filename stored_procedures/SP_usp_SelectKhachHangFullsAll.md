# Stored Procedure: `usp_SelectKhachHangFullsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:28.897000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.110000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangFullsAll]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangFullsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangID],
	[MaKhachHang],
	[TenKhachHang],
	[TenVietTat],
	[TenTiengAnh],
	[IsDaiLy],
	[TenChuDoanhNghiep],
	[MaSoThue],
	[MaSoDangKyKinhDoanh],
	[SoCMND],
	[NgayCap],
	[NoiCap],
	[NgayNhap],
	[DiaChiTrenHopDong],
	[ChiNhanh],
	[ChiNhanh1],
	[ChiNhanh2],
	[Code],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[KhachHangFull]
Where DeletedStatus <> 1
--endregion

```
