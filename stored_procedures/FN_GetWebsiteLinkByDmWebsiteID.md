# Function: `GetWebsiteLinkByDmWebsiteID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-30 13:30:48.470000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.883000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(400)` | Yes |
| `@DmWebsiteID` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION GetWebsiteLinkByDmWebsiteID
(
	@DmWebsiteID INT,
	@TenWebsite NVARCHAR(50)
)
RETURNS NVARCHAR(200)
AS
BEGIN
	DECLARE @DomainName NVARCHAR(200)
	SET @DomainName =  (SELECT WebsiteLink FROM dbo.WebsiteMapping_HDCN_Reporting 
				WHERE DmWebsiteID = @DmWebsiteID)
	
	SET @DomainName = ISNULL(@DomainName,@TenWebsite)
	
	RETURN @DomainName

END

```
