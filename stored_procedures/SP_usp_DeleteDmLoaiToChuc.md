# Stored Procedure: `usp_DeleteDmLoaiToChuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:08.407000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.317000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiToChucID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmLoaiToChuc]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmLoaiToChuc]
	@DmLoaiToChucID int
AS

SET NOCOUNT ON

Update [dbo].[DmLoaiToChuc]
Set DeletedStatus = 1
WHERE
	[DmLoaiToChucID] = @DmLoaiToChucID

--endregion

```
