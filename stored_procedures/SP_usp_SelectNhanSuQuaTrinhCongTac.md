# Stored Procedure: `usp_SelectNhanSuQuaTrinhCongTac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.347000
- **Ngày sửa cuối**: 2014-10-14 10:39:41.283000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuQuaTrinhCongTacID` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuQuaTrinhCongTac]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuQuaTrinhCongTac]
	@NhanSuQuaTrinhCongTacID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuQuaTrinhCongTacID],
	[SoHopDongLaoDong],
	[NhanSuSoYeuLyLichREF],
	[HinhThucLaoDong],
	[DmPhongBanREF],
	[DmBoPhanREF],
	[DmNhomLamViecREF],
	[DmDiaDiemLamViecREF],
	[DmChucDanhREF],
	[NgayBatDauLamViec],
	[NgayNghiViec],
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
	[dbo].[NhanSuQuaTrinhCongTac]
WHERE
		[NhanSuQuaTrinhCongTacID] = @NhanSuQuaTrinhCongTacID
 and DeletedStatus <> 1

--endregion


```
