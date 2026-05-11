# Function: `GetNumberFromString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-01-28 14:53:41.017000
- **Ngày sửa cuối**: 2015-01-28 15:15:49.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(50)` | Yes |
| `@NumberString` | `varchar(500)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetNumberFromString]
(
	-- Add the parameters for the function here
	@NumberString VARCHAR(500)
)
RETURNS VARCHAR(50)
AS
BEGIN

	DECLARE @Flag INT, @Index INT
	declare @items VARCHAR(500)
	SET @items = @NumberString
	DECLARE @KetQua1 VARCHAR(50), @KetQua2 VARCHAR(50)
	
	SET @Flag = 1
	SET @Index = 1
	WHILE @Index <=LEN(@items) AND @Flag = 1
	BEGIN
		
		IF ISNUMERIC(SUBSTRING(@items,@Index,LEN(@items))) = 1
		BEGIN
			SET @items = SUBSTRING(@items,@Index,LEN(@items))
			SET @Flag = 0
		END			
		ELSE
			set @Index = @Index + 1
			
	END
	

	SET @KetQua1 = @items
	
		
	SET @items = @NumberString
	SET @Flag = 1
	SET @Index = 1
	WHILE @Index<=LEN(@items) AND @Flag = 1
	BEGIN
		
		IF ISNUMERIC(SUBSTRING(@items,1,LEN(@items)-@Index)) = 1
		BEGIN
			SET @items = SUBSTRING(@items,1,LEN(@items)-@Index)
			SET @Flag = 0
		END
			
		ELSE
			set @Index = @Index + 1					
	END
				
	SET @KetQua2 = @items
	
	IF ISNUMERIC(@KetQua1) = 1 AND ISNUMERIC(@KetQua2) = 0
		SET @items = @KetQua1
	ELSE
		IF ISNUMERIC(@KetQua1) = 0 AND ISNUMERIC(@KetQua2) = 1
			SET @items = @KetQua2
		ELSE
			 IF ISNUMERIC(@KetQua1) = 1 AND ISNUMERIC(@KetQua2) = 1
				IF CONVERT(BIGINT,@KetQua1) > CONVERT(BIGINT,@KetQua2)
					SET @items = @KetQua1
				ELSE
					SET @items = @KetQua2
		
	RETURN 	@items
END

```
