# Function: `GetWebsiteIDByDomainName`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-09-11 15:02:50.133000
- **Ngày sửa cuối**: 2025-09-17 10:57:40.140000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@TenWebsite` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetWebsiteIDByDomainName]
(
	@TenWebsite NVARCHAR(1000)
)
RETURNS int
AS
BEGIN
	DECLARE @ID INT, @DateNow DATETIME
	SET @TenWebsite = IIF(@TenWebsite = N'Blanks' OR @TenWebsite = N'',N'(Blanks)',@TenWebsite)

	SET @ID = (SELECT TOP (1) DmWebsiteReportingdbID 
				FROM dbo.DmWebsiteReportingdb 
					WHERE TenWebsite = @TenWebsite
					ORDER BY DmWebsiteReportingdbID)
	

	-- Return the result of the function
	RETURN @ID

END



```
