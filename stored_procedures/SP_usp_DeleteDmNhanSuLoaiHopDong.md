# Stored Procedure: `usp_DeleteDmNhanSuLoaiHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.237000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.257000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanSuLoaiHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmNhanSuLoaiHopDong]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmNhanSuLoaiHopDong]
	@DmNhanSuLoaiHopDongID int
AS

SET NOCOUNT ON

Update [dbo].[DmNhanSuLoaiHopDong]
Set DeletedStatus = 1
WHERE
	[DmNhanSuLoaiHopDongID] = @DmNhanSuLoaiHopDongID

--endregion

```
