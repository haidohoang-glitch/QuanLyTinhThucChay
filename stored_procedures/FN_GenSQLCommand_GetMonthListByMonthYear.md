# Function: `GenSQLCommand_GetMonthListByMonthYear`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-08-01 13:36:04.720000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.087000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@FromMonth` | `int(4)` | No |
| `@FromYear` | `int(4)` | No |
| `@ToMonth` | `int(4)` | No |
| `@ToYear` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-08-01
-- Description:	<Description, ,>
-- =============================================
-- PRINT dbo.GenSQLCommand_GetMonthListByMonthYear(6, 2013, 2, 2014)
CREATE FUNCTION dbo.GenSQLCommand_GetMonthListByMonthYear
(
	@FromMonth	INT,
	@FromYear	INT,
	@ToMonth	INT,
	@ToYear		INT
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @MonthList NVARCHAR(MAX);
	DECLARE @Month		INT,
			@Year		INT;
			
	SET @MonthList = '';

	IF @FromYear = @ToYear
	BEGIN
		SET @Month = @FromMonth;
		SET @Year = @FromYear;
		
		WHILE @Month <= @ToMonth
		BEGIN
			IF @MonthList <> ''
				SET @MonthList += ',[' + CONVERT(NVARCHAR(10), @Month) + '-' + CONVERT(NVARCHAR(10), @Year) + ']';
			ELSE
				SET @MonthList += '[' + CONVERT(NVARCHAR(10), @Month) + '-' + CONVERT(NVARCHAR(10), @Year) + ']';
			
			SET @Month += 1;
		END
	END
	ELSE
	BEGIN
		SET @Year = @FromYear;
		SET @Month = @FromMonth;
		
		WHILE @Month <= 12
		BEGIN
			IF @MonthList <> ''
				SET @MonthList += ',[' + CONVERT(NVARCHAR(10), @Month) + '-' + CONVERT(NVARCHAR(10), @Year) + ']';
			ELSE
				SET @MonthList += '[' + CONVERT(NVARCHAR(10), @Month) + '-' + CONVERT(NVARCHAR(10), @Year) + ']';
			
			SET @Month += 1;
		END;
		
		SET @Year = @ToYear;
		SET @Month = 1;
		
		WHILE @Month <= @ToMonth
		BEGIN
			SET @MonthList += ',[' + CONVERT(NVARCHAR(10), @Month) + '-' + CONVERT(NVARCHAR(10), @Year) + ']';
			
			SET @Month += 1;
		END
	END

	-- Return the result of the function
	RETURN @MonthList

END

```
