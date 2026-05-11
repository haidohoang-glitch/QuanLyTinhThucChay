# Stored Procedure: `usp_DeleteNhanSuHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.137000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.887000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteNhanSuHopDong]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteNhanSuHopDong]
	@NhanSuHopDongID int
AS

SET NOCOUNT ON

Update [dbo].[NhanSuHopDong]
Set DeletedStatus = 1
WHERE
	[NhanSuHopDongID] = @NhanSuHopDongID

--endregion

```
