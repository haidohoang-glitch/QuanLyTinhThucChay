# Stored Procedure: `usp_SelectNhanSuHopDongsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.177000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.870000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuHopDongsAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuHopDongsAll]
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
Where DeletedStatus <> 1
--endregion

```
