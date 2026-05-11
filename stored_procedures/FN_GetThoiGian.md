# Function: `GetThoiGian`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-08 12:50:05.587000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.493000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@Ngay` | `date(3)` | No |
| `@DonVi` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetThoiGian]
(
	@Ngay date,
	@DonVi int
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max);	
	DECLARE @Month int;
	SET @Month = Month(@Ngay);

	-- Add the T-SQL statements to compute the return value here
	IF @DonVi = 3 
		BEGIN
			IF(@Month >= 1 AND @Month <= 3 )
				SET @ReturnValue = 'I - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
			ELSE IF (@Month >= 4 AND @Month <= 6 )
				SET @ReturnValue = 'II - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
			ELSE IF (@Month >= 7 AND @Month <= 9 )
				SET @ReturnValue = 'III - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
			ELSE IF (@Month >= 10 AND @Month <= 12 )
				SET @ReturnValue = 'IV - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
		END
	ELSE
		SET @ReturnValue = 		
		CASE @DonVi
			WHEN 1 THEN
				CONVERT(nvarchar(100),DATEPART( Week , @Ngay)) + ' - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
			WHEN 2 THEN
				CONVERT(nvarchar(100),DATEPART( Month , @Ngay)) + ' - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
			WHEN 4 THEN
				CONVERT(nvarchar(50),YEAR(@Ngay))
		END;
		
	-- Return the result of the function
	RETURN @ReturnValue

END

```
