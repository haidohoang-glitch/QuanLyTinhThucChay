# Function: `GetDmWebsiteIDIDByDmWebsiteReportingdb`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-05-19 17:56:07.917000
- **Ngày sửa cuối**: 2015-05-19 17:56:07.917000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DmWebsiteReportingdb` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[GetDmWebsiteIDIDByDmWebsiteReportingdb]
(
	@DmWebsiteReportingdb INT
)
RETURNS int
AS
BEGIN
	DECLARE @ID INT
	SET @ID =  (SELECT DmWebsiteID FROM dbo.WebsiteMapping_HDCN_Reporting 
				WHERE DmWebsiteReportingdbID = @DmWebsiteReportingdb)
	
	SET @ID = ISNULL(@ID,@DmWebsiteReportingdb)
	
	RETURN @ID

END



```
