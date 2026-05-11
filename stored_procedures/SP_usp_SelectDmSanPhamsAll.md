# Stored Procedure: `usp_SelectDmSanPhamsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:29:23.560000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.143000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDmSanPhamsAll]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmSanPhamsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmSanPhamID],
	[TenSanPham],
	[GhiChu],
	[Code],
	[DmNhomSanPhamREF],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmSanPham]
Where DeletedStatus <> 1
--endregion

```
