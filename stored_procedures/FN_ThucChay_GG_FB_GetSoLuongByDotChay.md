# Function: `ThucChay_GG_FB_GetSoLuongByDotChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-12-27 12:17:13.530000
- **Ngày sửa cuối**: 2014-12-27 12:17:13.530000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@phanBoId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-12-26
-- Description:	<Description, ,>
-- =============================================

/*
	PRINT dbo.ThucChay_GG_FB_GetSoLuongByDotChay(59092) 
*/

CREATE FUNCTION [dbo].[ThucChay_GG_FB_GetSoLuongByDotChay] 
(
	-- Add the parameters for the function here
	@phanBoId	INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @resultValue INT = 0
	
	SET @resultValue = (
	SELECT 
		SUM(T.TotalDay)
	FROM
	(
		SELECT 
			A.DotChayHopDongChiTietID, (DATEDIFF(d,A.ThoiGianBatDau, A.ThoiGianKetThuc) + 1) TotalDay 
		FROM DotChayHopDongChiTiet A
		WHERE A.HopDongChiTietREF = @phanBoId
			AND A.DeletedStatus = 0
	)T
	)
	
	SET @resultValue = ISNULL(@resultValue,0);
	
	-- Return the result of the function
	RETURN @resultValue

END

```
