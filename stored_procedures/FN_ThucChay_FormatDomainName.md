# Function: `ThucChay_FormatDomainName`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-05-21 10:47:38.780000
- **Ngày sửa cuối**: 2018-01-29 11:47:42.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(510)` | Yes |
| `@DomainName` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql
-- ================================================
-- Template generated from Template Explorer using:
-- Create Scalar Function (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the function.
-- ================================================
-- =============================================
-- Author:		NhatMQ
-- Create date: 20214-02-28
-- Description:	Repace subdomain
-- =============================================
/*
select [dbo].[ThucChay_FormatDomainName]
(
	'm.suckhoegiadinh.com.vn'
)

*/
CREATE FUNCTION [dbo].[ThucChay_FormatDomainName]
(
	-- Add the parameters for the function here
	@DomainName nvarchar(255)
)
RETURNS nvarchar(255)
AS
BEGIN
	SET @DomainName = dbo.ReplaceDomainName(@DomainName);
	IF (CHARINDEX('.com.vn',@DomainName) > 0 OR CHARINDEX('.net.vn',@DomainName) > 0 )
	BEGIN
		IF (len(@DomainName)-len(replace(@DomainName,'.',''))>2)
			SET @DomainName =  substring(@DomainName,charindex('.',@DomainName)+1,len(@DomainName)) 
		--else @DomainName
	END
	ELSE
	BEGIN
		IF LEN(@DomainName)-LEN(REPLACE(@DomainName,'.',''))>2
			SET @DomainName = SUBSTRING(@DomainName,CHARINDEX('.',@DomainName)+1,len(@DomainName))
		ELSE IF len(@DomainName)-len(replace(@DomainName,'.',''))>1
			SET @DomainName = substring(@DomainName,charindex('.',@DomainName)+1,len(@DomainName))
	END
	---- Return the result of the function
	RETURN @DomainName

END


```
