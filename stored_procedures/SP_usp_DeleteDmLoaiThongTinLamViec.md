# Stored Procedure: `usp_DeleteDmLoaiThongTinLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:07.813000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.337000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiThongTinLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmLoaiThongTinLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmLoaiThongTinLamViec]
	@DmLoaiThongTinLamViecID int
AS

SET NOCOUNT ON

Update [dbo].[DmLoaiThongTinLamViec]
Set DeletedStatus = 1
WHERE
	[DmLoaiThongTinLamViecID] = @DmLoaiThongTinLamViecID

--endregion

```
