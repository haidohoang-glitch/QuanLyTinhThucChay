# Stored Procedure: `usp_SelectThongTinCaNhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:25.033000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.443000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinCaNhanID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectThongTinCaNhan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectThongTinCaNhan]
	@ThongTinCaNhanID int
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
WHERE
		[ThongTinCaNhanID] = @ThongTinCaNhanID
 and DeletedStatus <> 1

--endregion

```
