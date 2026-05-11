# Function: `ThucChay_FormatSoHopDong`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-05-15 15:40:16.657000
- **Ngày sửa cuối**: 2015-01-07 16:26:51.863000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-25
-- Description:	<Description, ,>
-- =============================================
-- PRINT dbo.ThucChay_FormatSoHopDong('tm/qc031213')
CREATE FUNCTION [dbo].[ThucChay_FormatSoHopDong] 
(
	-- Add the parameters for the function here
	@SoHopDong NVARCHAR(50)
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	--DECLARE @ReturnValue NVARCHAR(50);
	DECLARE @position INT = 0;
	
	IF CHARINDEX('/AD -',@SoHopDong) > 0
	BEGIN
		SET @position = (SELECT CHARINDEX('/',@SoHopDong) - 1);
		SET @SoHopDong = LEFT(@SoHopDong,@position);
	END
	ELSE IF CHARINDEX('/AD',@SoHopDong) > 0 
		SET @SoHopDong = REPLACE(@SoHopDong,'/AD','')
	ELSE IF CHARINDEX('-AD',@SoHopDong) > 0 
		SET @SoHopDong = REPLACE(@SoHopDong,'-AD','')		
	ELSE IF CHARINDEX('AD',@SoHopDong) > 0 
		SET @SoHopDong = REPLACE(@SoHopDong,'AD','')
	ELSE IF CHARINDEX('/MKP',@SoHopDong) > 0
	BEGIN
		SET @SoHopDong = REPLACE(@SoHopDong,'/MKP','')
		SET @SoHopDong = 'MKP' + REPLACE(@SoHopDong,'CPC','')
	END
	ELSE IF CHARINDEX('MKP',@SoHopDong) > 0
	BEGIN
		SET @SoHopDong = REPLACE(@SoHopDong,'MKP','')
		SET @SoHopDong = 'MKP' + REPLACE(@SoHopDong,'CPC','')
	END
	ELSE IF CHARINDEX('tm/',@SoHopDong) > 0 
		SET @SoHopDong = REPLACE(@SoHopDong,'tm/','')
	ELSE IF CHARINDEX(' ',@SoHopDong) > 0 
		SET @SoHopDong = REPLACE(@SoHopDong,' ','')	

	-- Return the result of the function
	RETURN UPPER(@SoHopDong);

END


```
