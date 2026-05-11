# Stored Procedure: `usp_SelectAdminPermisionHDCNsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-06 17:01:41.557000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.347000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_SelectAdminPermisionHDCNsAll]
-- Create Date: Friday, September 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectAdminPermisionHDCNsAll]
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
Where DeletedStatus <> 1
--endregion

```
