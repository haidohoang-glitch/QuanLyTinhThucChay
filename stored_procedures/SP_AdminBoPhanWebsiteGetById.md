# Stored Procedure: `AdminBoPhanWebsiteGetById`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 17:39:10.300000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.083000

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
-- dbo.AdminBoPhanWebsiteGetById 4
CREATE PROCEDURE [dbo].[AdminBoPhanWebsiteGetById] 
	-- Add the parameters for the stored procedure here
	@AdminBoPhanWebsiteId int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT * FROM AdminBoPhanWebsite A WHERE A.AdminBoPhanWebsiteID = @AdminBoPhanWebsiteId;
END

```
