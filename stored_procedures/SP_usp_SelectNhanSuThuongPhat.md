# Stored Procedure: `usp_SelectNhanSuThuongPhat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.923000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.470000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuThuongPhatID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuThuongPhat]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuThuongPhat]
	@NhanSuThuongPhatID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuThuongPhatID],
	[DmNhanSuLoaiThuongPhat],
	[SoHieu],
	[NgayDuyet],
	[NguoiDuyet],
	[NgayBanHanh],
	[QuyetDinhFileName],
	[QuyetDinhFIleNameEncode],
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
	[dbo].[NhanSuThuongPhat]
WHERE
		[NhanSuThuongPhatID] = @NhanSuThuongPhatID
 and DeletedStatus <> 1

--endregion

```
