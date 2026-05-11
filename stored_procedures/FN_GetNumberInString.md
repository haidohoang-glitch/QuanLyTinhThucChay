# Function: `GetNumberInString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-01-28 15:50:31.840000
- **Ngày sửa cuối**: 2015-01-28 16:16:49.753000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(50)` | Yes |
| `@Link` | `varchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetNumberInString]
(
	-- Add the parameters for the function here
	@Link VARCHAR(max)
)
RETURNS VARCHAR(50)
AS
BEGIN
	DECLARE @RecordCount INT
	DECLARE @KetQua VARCHAR(50)
	
	set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Link,'-') 
	WHERE
	ISNUMERIC(items) = 1
	AND LEN(items) >4
	)
	
	IF @RecordCount = 1
		SET @Link = (SELECT items FROM [dbo].[Split](@Link,'-') 
		WHERE
		ISNUMERIC(items) = 1
		AND LEN(items) >4
		)
	ELSE
		BEGIN
			set @RecordCount = (SELECT COUNT(*) FROM [dbo].[Split](@Link,'-') 
			WHERE
			ISNUMERIC(dbo.GetNumberFromString(items))  = 1

			)		
			IF @RecordCount = 1
				SET @Link = (SELECT dbo.GetNumberFromString(items) FROM [dbo].[Split](@Link,'-') 
				WHERE
				ISNUMERIC(dbo.GetNumberFromString(items))  = 1

				)				
		END		
	
	-- Return the result of the function
	RETURN @Link

END


--SELECT [dbo].[GetNumberInString]('dong-nhi-chia-se-bi-quyet-ve-doi-moi-muon-hon-keo-ngot-p5r20140908125337706')
```
