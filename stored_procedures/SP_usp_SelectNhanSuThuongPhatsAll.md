# Stored Procedure: `usp_SelectNhanSuThuongPhatsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.940000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.457000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuThuongPhatsAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuThuongPhatsAll]
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
Where DeletedStatus <> 1
--endregion

```
