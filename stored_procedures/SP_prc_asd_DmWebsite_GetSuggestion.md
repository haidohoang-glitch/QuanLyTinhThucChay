# Stored Procedure: `prc_asd_DmWebsite_GetSuggestion`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-28 10:19:00.833000
- **Ngày sửa cuối**: 2017-04-28 16:09:54.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KeyWord` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_DmWebsite_GetSuggestion]
	-- Add the parameters for the stored procedure here
	@KeyWord NVARCHAR(200) = ''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT TOP 50 s.DmWebsiteID id, s.TenWebsite FROM dbo.DmWebsite s WHERE s.TenWebsite LIKE N'%' + @KeyWord + N'%'
	AND s.DeletedStatus = 0
END

```
