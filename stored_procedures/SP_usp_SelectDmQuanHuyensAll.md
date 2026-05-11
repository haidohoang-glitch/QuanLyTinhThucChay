# Stored Procedure: `usp_SelectDmQuanHuyensAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:14.797000
- **Ngày sửa cuối**: 2014-10-14 10:39:42.470000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmQuanHuyensAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmQuanHuyensAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmQuanHuyenID],
	[MaQuanHuyen],
	[TenQuanHuyen],
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
	[dbo].[DmQuanHuyen]
Where DeletedStatus <> 1
--endregion


```
