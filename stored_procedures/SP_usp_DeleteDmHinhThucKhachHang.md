# Stored Procedure: `usp_DeleteDmHinhThucKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:04.390000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.897000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmHinhThucKhachHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmHinhThucKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmHinhThucKhachHang]
	@DmHinhThucKhachHangID int
AS

SET NOCOUNT ON

Update [dbo].[DmHinhThucKhachHang]
Set DeletedStatus = 1
WHERE
	[DmHinhThucKhachHangID] = @DmHinhThucKhachHangID

--endregion

```
