# Stored Procedure: `usp_SelectDmLoaiDiaChisAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:06.207000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.477000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmLoaiDiaChisAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmLoaiDiaChisAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmLoaiDiaChiID],
	[MaLoaiDiaChi],
	[TenLoaiDiaChi],
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
	[dbo].[DmLoaiDiaChi]
Where DeletedStatus <> 1
--endregion

```
