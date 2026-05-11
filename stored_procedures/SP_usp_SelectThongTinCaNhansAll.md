# Stored Procedure: `usp_SelectThongTinCaNhansAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:25.163000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.440000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectThongTinCaNhansAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectThongTinCaNhansAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[ThongTinCaNhanID],
	[MaThongTinCaNhan],
	[HoVaTen],
	[NgaySinh],
	[GioiTinh],
	[SoChungThucCaNhan],
	[NgayCapChungThucCaNhan],
	[NoiCapChungThucCaNhan],
	[DienThoai],
	[Fax],
	[Email],
	[Website],
	[DmChucDanhREF],
	[DiaChiREF],
	[Email2],
	[DienThoai2],
	[DienThoai3],
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
	[dbo].[ThongTinCaNhan]
Where DeletedStatus <> 1
--endregion

```
