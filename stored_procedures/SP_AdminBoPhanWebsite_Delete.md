# Stored Procedure: `AdminBoPhanWebsite_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 17:39:10.317000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.117000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminBoPhanWebsiteId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminBoPhanWebsite_Delete] 
	-- Add the parameters for the stored procedure here
	@AdminBoPhanWebsiteId int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DELETE FROM AdminBoPhanWebsite WHERE AdminBoPhanWebsiteID = @AdminBoPhanWebsiteId;
END

```
