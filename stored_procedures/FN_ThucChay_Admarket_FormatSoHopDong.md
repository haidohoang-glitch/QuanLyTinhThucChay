# Function: `ThucChay_Admarket_FormatSoHopDong`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-25 16:37:01.663000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.147000

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
-- PRINT dbo.ThucChay_Admarket_FormatSoHopDong('CPC170112/MKP')
CREATE FUNCTION dbo.ThucChay_Admarket_FormatSoHopDong 
(
	-- Add the parameters for the function here
	@SoHopDong NVARCHAR(50)
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	--DECLARE @ReturnValue NVARCHAR(50);
	
	IF CHARINDEX('/AD',@SoHopDong) > 0 
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

	-- Return the result of the function
	RETURN @SoHopDong;

END

```
