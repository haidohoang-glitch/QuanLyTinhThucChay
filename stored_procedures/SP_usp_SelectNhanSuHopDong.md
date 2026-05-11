# Stored Procedure: `usp_SelectNhanSuHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.157000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.873000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuHopDong]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuHopDong]
	@NhanSuHopDongID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuHopDongID],
	[NhanSuSoYeuLyLichREF],
	[SoHopDong],
	[NgayKyHopDong],
	[TuNgay],
	[DenNgay],
	[DmNhanSuLoaiHopDongREF],
	[DmHinhThucNhanSuREF],
	[HopDongFileName],
	[HopDongFileNameEncode],
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
	[dbo].[NhanSuHopDong]
WHERE
		[NhanSuHopDongID] = @NhanSuHopDongID
 and DeletedStatus <> 1

--endregion

```
