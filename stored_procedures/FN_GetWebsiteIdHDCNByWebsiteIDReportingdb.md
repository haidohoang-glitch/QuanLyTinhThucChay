# Function: `GetWebsiteIdHDCNByWebsiteIDReportingdb`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-14 09:10:41.407000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.913000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@WebsiteIDReportingdb` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetWebsiteIdHDCNByWebsiteIDReportingdb]
(
	-- Add the parameters for the function here
	@WebsiteIDReportingdb int
)
RETURNS nvarchar(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @WebsiteId INT
    set @WebsiteId = 0
    SET @WebsiteId =
    (
		SELECT distinct b.DMWebsiteIdHDCN
		FROM dbo.DmMappingWebsiteHDCN_Repotingdb b 
		WHERE b.DMWebsiteIdReportingdb = @WebsiteIDReportingdb        
    )
    SET @WebsiteId = ISNULL(@WebsiteId,0)
	RETURN @WebsiteId

END

```
