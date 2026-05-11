# Stored Procedure: `usp_SelectNhanSuTinhTrangsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.200000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.040000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuTinhTrangsAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuTinhTrangsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuTinhTrangID],
	[NhanSuSoYeuLyLichREF],
	[NgayBatDau],
	[NgayKetThuc],
	[DmNhanSuTinhTrangREF],
	[DmNhomLamViecREF],
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
	[dbo].[NhanSuTinhTrang]
Where DeletedStatus <> 1
--endregion

```
