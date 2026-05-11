# Stored Procedure: `usp_SelectNhanSuQuaTrinhCongTacsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.360000
- **Ngày sửa cuối**: 2014-10-14 10:39:41.260000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuQuaTrinhCongTacsAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuQuaTrinhCongTacsAll]
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
Where DeletedStatus <> 1
--endregion


```
