# Stored Procedure: `usp_SelectDmHinhThucNhanSusAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:05.083000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.173000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmHinhThucNhanSusAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmHinhThucNhanSusAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmHinhThucNhanSuID],
	[MaHinhThucNhanSu],
	[TenHinhThucNhanSu],
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
	[dbo].[DmHinhThucNhanSu]
Where DeletedStatus <> 1
--endregion

```
