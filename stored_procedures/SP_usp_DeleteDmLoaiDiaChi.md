# Stored Procedure: `usp_DeleteDmLoaiDiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:06.013000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.867000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiDiaChiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmLoaiDiaChi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmLoaiDiaChi]
	@DmLoaiDiaChiID int
AS

SET NOCOUNT ON

Update [dbo].[DmLoaiDiaChi]
Set DeletedStatus = 1
WHERE
	[DmLoaiDiaChiID] = @DmLoaiDiaChiID

--endregion

```
