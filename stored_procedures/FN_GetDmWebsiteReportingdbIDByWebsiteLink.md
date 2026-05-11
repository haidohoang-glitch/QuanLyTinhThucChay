# Function: `GetDmWebsiteReportingdbIDByWebsiteLink`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-09-01 15:40:43.617000
- **Ngày sửa cuối**: 2017-09-01 15:40:43.617000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@WebsiteLink` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetDmWebsiteReportingdbIDByWebsiteLink]
(
	@WebsiteLink NVARCHAR(200)
)
RETURNS int
AS
BEGIN
	DECLARE @ID INT
	SET @ID =  (SELECT DmWebsiteReportingdbID FROM dbo.WebsiteMapping_HDCN_Reporting 
				WHERE WebsiteLink = @WebsiteLink)
	
	
	
	RETURN @ID

END



```
