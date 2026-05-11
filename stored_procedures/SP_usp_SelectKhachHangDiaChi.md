# Stored Procedure: `usp_SelectKhachHangDiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:28.007000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.623000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangDiaChiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangDiaChi]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangDiaChi]
	@KhachHangDiaChiID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangDiaChiID],
	[KhachHangREF],
	[TruSoChinh],
	[ChiNhanh],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[KhachHangDiaChi]
WHERE
		[KhachHangDiaChiID] = @KhachHangDiaChiID
 and DeletedStatus <> 1

--endregion

```
