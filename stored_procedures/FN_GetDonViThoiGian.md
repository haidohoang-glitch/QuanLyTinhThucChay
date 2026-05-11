# Function: `GetDonViThoiGian`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-14 12:56:56.267000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.543000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@Ngay` | `date(3)` | No |
| `@LoaiDonVi` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[GetDonViThoiGian]
(
	@Ngay date,
	@LoaiDonVi int -- 0: ngay, 1: Tuan, 2: Thang, 3: Quy, 4: Nam
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max);	
	DECLARE @Week int;
	DECLARE @Month int;
	SET @Month = Month(@Ngay);
	SET @Week = CONVERT(int, DATEPART( Week , @Ngay))

	-- Add the T-SQL statements to compute the return value here
	IF @LoaiDonVi = 3 
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
		--SET @ReturnValue = 		
		--CASE @LoaiDonVi
		--	WHEN 0 THEN
		--		CONVERT(nvarchar(100),DATEPART( DAY , @Ngay)) 
		--	WHEN 1 THEN
		--		BEGIN
		--		CONVERT(nvarchar(100),DATEPART( Week , @Ngay)) + ' - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
		--		END
		--	WHEN 2 THEN
		--		CONVERT(nvarchar(100),DATEPART( Month , @Ngay)) + ' - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
		--	WHEN 4 THEN
		--		CONVERT(nvarchar(50),YEAR(@Ngay))
		--END;
		
		IF @LoaiDonVi = 0 
			SET @ReturnValue = CONVERT(nvarchar(100), @Ngay)
		ELSE IF @LoaiDonVi = 1
			BEGIN
				IF @Week < 10 
					SET @ReturnValue = '0' + CONVERT(nvarchar(100),DATEPART( Week , @Ngay)) + ' - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
				ELSE
					SET @ReturnValue = CONVERT(nvarchar(100),DATEPART( Week , @Ngay)) + ' - ' + CONVERT(nvarchar(50),YEAR(@Ngay))		
			END
		ELSE IF @LoaiDonVi = 2
			BEGIN
				IF @Month < 10 
					SET @ReturnValue = '0' + CONVERT(nvarchar(100),DATEPART( Month , @Ngay)) + ' - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
				ELSE
					SET @ReturnValue = CONVERT(nvarchar(100),DATEPART( Month , @Ngay)) + ' - ' + CONVERT(nvarchar(50),YEAR(@Ngay))		
			END
		ELSE IF @LoaiDonVi = 3
			SET @ReturnValue = CONVERT(nvarchar(100),DATEPART( Month , @Ngay)) + ' - ' + CONVERT(nvarchar(50),YEAR(@Ngay))
		ELSE
			SET @ReturnValue = CONVERT(nvarchar(50),YEAR(@Ngay))
			
	-- Return the result of the function
	RETURN @ReturnValue

END
```
