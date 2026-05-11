# Stored Procedure: `AdminGroupMenuPermission_GetDistinct_AdminGroupId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-25 17:01:10.147000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.093000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <24.09.2013>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminGroupMenuPermission_GetDistinct_AdminGroupId]	
AS
BEGIN
	SELECT DISTINCT(AdminGroupId) FROM AdminGroupMenuPermission	
END

```
