# Function: `ThucChay_GetSoLuongThucChayByHopDongChiTietID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-28 17:23:10.483000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.933000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayByHopDongChiTietID]
(
	-- Add the parameters for the function here
	@HopDongChiTietID NVARCHAR(50)
)
RETURNS FLOAT
AS
BEGIN

	-- Declare the return variable here
	DECLARE @SoLuongThucChay FLOAT
		
	SET @SoLuongThucChay = (SELECT SUM(A.SoLuongThucChay) FROM dbo.ThucChayDaTinh A WHERE A.HopDongChiTietREF = @HopDongChiTietID)
	--SET @SoLuongThucChay = (SELECT 
	--							CASE WHEN SoLuongThucChayKM > 0 THEN SUM(SoLuongThucChayKM) 
	--								 ELSE SUM(SoLuongThucChay) 
	--							END
	--						FROM dbo.ThucChayDaTinh 
	--						WHERE HopDongChiTietREF = @HopDongChiTietID
	--						GROUP BY SoLuongThucChayKM)
	
	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
	-- Return the result of the function
	RETURN @SoLuongThucChay

END
```
