# Function: `GetWebsiteNameHDCNByWebsiteIDReportingdb`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-28 16:27:39.500000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.853000

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
CREATE FUNCTION [dbo].[GetWebsiteNameHDCNByWebsiteIDReportingdb]
(
	-- Add the parameters for the function here
	@WebsiteIDReportingdb int
)
RETURNS nvarchar(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @WebsiteName nvarchar(50)
    set @WebsiteName = ''
    SET @WebsiteName =
    (
		SELECT distinct dw.TenWebsite
		FROM DmWebsite dw 
		INNER JOIN dbo.DmMappingWebsiteHDCN_Repotingdb b 
		ON dw.DmWebsiteID = b.DMWebsiteIdHDCN
		AND b.DMWebsiteIdReportingdb = @WebsiteIDReportingdb        
    )
    SET @WebsiteName = ISNULL(@WebsiteName,'')
	RETURN @WebsiteName

END

```
