# Function: `GetDmWebsiteReportingdbIDByDmWebsiteID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-30 13:28:57.157000
- **Ngày sửa cuối**: 2015-05-12 17:42:02.740000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DmWebsiteID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetDmWebsiteReportingdbIDByDmWebsiteID]
(
	@DmWebsiteID INT
)
RETURNS int
AS
BEGIN
	DECLARE @ID INT
	SET @ID =  (SELECT DmWebsiteReportingdbID FROM dbo.WebsiteMapping_HDCN_Reporting 
				WHERE DmWebsiteID = @DmWebsiteID)
	
	SET @ID = ISNULL(@ID,@DmWebsiteID)
	
	RETURN @ID

END



```
