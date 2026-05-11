# Stored Procedure: `usp_SelectDiaChisAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:02.733000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.213000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDiaChisAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDiaChisAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DiaChiID],
	[SoNha],
	[DuongPho],
	[DmQuanHuyenREF],
	[DmTinhThanhPhoREF],
	[DmQuocGiaREF],
	[DmLoaiDiaChiREF],
	[IsTruSoChinh],
	[DiaChiText],
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
	[dbo].[DiaChi]
Where DeletedStatus <> 1
--endregion

```
