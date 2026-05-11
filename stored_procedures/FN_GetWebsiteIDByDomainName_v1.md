# Function: `GetWebsiteIDByDomainName_v1`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-06-02 11:04:33.100000
- **Ngày sửa cuối**: 2018-10-04 08:04:34.007000

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
CREATE FUNCTION [dbo].[GetWebsiteIDByDomainName_v1]
(
	@TenWebsite NVARCHAR(1000)
)
RETURNS int
AS
BEGIN
	DECLARE @ID INT, @DateNow DATETIME
	
	SET @ID = (SELECT TOP (1) DmWebsiteReportingdbID 
		FROM dbo.DmWebsiteReportingdb WHERE TenWebsite = @TenWebsite
		ORDER BY DmWebsiteReportingdbID)
	--IF(@ID IS NULL)
	--BEGIN
	--	EXEC   [dbo].[GetWebsiteIDByDomainName_v2]	@TenWebsite ,@ID OUTPUT
	--END
	SET @ID = ISNULL(@ID,0)
	-- Return the result of the function
	RETURN @ID

END



```
