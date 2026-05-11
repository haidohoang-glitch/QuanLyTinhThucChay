# Stored Procedure: `usp_SelectDmNghanhHangsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:31.643000
- **Ngày sửa cuối**: 2014-10-14 10:39:43.207000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_SelectDmNghanhHangsAll]
-- Create Date: Monday, November 18, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNghanhHangsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNghanhHangID],
	[TenNghanhHang],
	[DmNghanhHangREF],
	[CreatedBy],
	[CreatedAt],
	[LastModidfiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmNghanhHang]
Where DeletedStatus <> 1
--endregion

```
