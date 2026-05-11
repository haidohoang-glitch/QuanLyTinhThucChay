# Stored Procedure: `usp_DeleteDmLoaiTrangThietBi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:09.413000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.870000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiTrangThietBiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmLoaiTrangThietBi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmLoaiTrangThietBi]
	@DmLoaiTrangThietBiID int
AS

SET NOCOUNT ON

Update [dbo].[DmLoaiTrangThietBi]
Set DeletedStatus = 1
WHERE
	[DmLoaiTrangThietBiID] = @DmLoaiTrangThietBiID

--endregion

```
