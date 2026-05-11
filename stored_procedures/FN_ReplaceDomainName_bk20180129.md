# Function: `ReplaceDomainName_bk20180129`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2018-01-29 11:42:49.450000
- **Ngày sửa cuối**: 2018-01-29 11:42:49.450000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(510)` | Yes |
| `@DomainName` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ReplaceDomainName_bk20180129]
(
	-- Add the parameters for the function here
	@DomainName nvarchar(255)
)
RETURNS nvarchar(255)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @MobileDomain nvarchar(255);
	DECLARE @TabletDomain nvarchar(255);

	SET @MobileDomain = SUBSTRING(@DoMainName,1,2);
	SET @TabletDomain = SUBSTRING(@DoMainName,1,6);

	IF @MobileDomain = 'm.' 
		SET @DomainName = SUBSTRING(@DoMainName,3,LEN(@DomainName));
	ELSE IF @TabletDomain = 'touch.' 
		SET @DomainName = SUBSTRING(@DoMainName,7,LEN(@DomainName));

	-- Return the result of the function
	RETURN @DomainName

END

```
