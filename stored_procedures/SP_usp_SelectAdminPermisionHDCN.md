# Stored Procedure: `usp_SelectAdminPermisionHDCN`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-06 17:01:41.760000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.437000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminPermisionHDCNID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_SelectAdminPermisionHDCN]
-- Create Date: Friday, September 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectAdminPermisionHDCN]
	@AdminPermisionHDCNID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[AdminPermisionHDCNID],
	[NhanSuSoYeuLyLichID],
	[TenDangNhap],
	[AdminGroupId],
	[KhoaNguoiDung],
	[ThoiGianDangNhap],
	[SalerID],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[AdminPermisionHDCN]
WHERE
		[AdminPermisionHDCNID] = @AdminPermisionHDCNID
 and DeletedStatus <> 1

--endregion

```
