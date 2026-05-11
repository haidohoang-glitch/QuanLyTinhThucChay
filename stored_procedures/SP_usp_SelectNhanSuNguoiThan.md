# Stored Procedure: `usp_SelectNhanSuNguoiThan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.243000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.830000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuNguoiThanID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuNguoiThan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuNguoiThan]
	@NhanSuNguoiThanID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuNguoiThanID],
	[NhanSuSoYeuLyLichREF],
	[ThongTinCaNhanREF],
	[DmNhanSuQuanHeREF],
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
	[dbo].[NhanSuNguoiThan]
WHERE
		[NhanSuNguoiThanID] = @NhanSuNguoiThanID
 and DeletedStatus <> 1

--endregion

```
