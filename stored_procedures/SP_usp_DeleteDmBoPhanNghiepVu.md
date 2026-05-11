# Stored Procedure: `usp_DeleteDmBoPhanNghiepVu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-16 11:38:36.867000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.277000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBoPhanNghiepVuID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteDmBoPhanNghiepVu]
-- Create Date: Thursday, December 16, 2010
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmBoPhanNghiepVu]
	@DmBoPhanNghiepVuID nvarchar(50)
AS

SET NOCOUNT ON

Update [dbo].[DmBoPhanNghiepVu]
Set DeletedStatus = 1
WHERE
	[DmBoPhanNghiepVuID] = @DmBoPhanNghiepVuID

--endregion

```
