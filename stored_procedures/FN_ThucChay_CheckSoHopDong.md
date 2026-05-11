# Function: `ThucChay_CheckSoHopDong`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-28 18:24:42.373000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.803000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@SoHopDong` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION dbo.ThucChay_CheckSoHopDong 
(
	-- Add the parameters for the function here
	@SoHopDong nvarchar(100)
)
RETURNS int
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue INT;
	
	IF EXISTS(SELECT TenMaHopDong FROM DmMaHopDongChuan WHERE TenMaHopDong = SUBSTRING(@SoHopDong,1,1) AND LEN(@SoHopDong) <= 8)
		SET @ResultValue = 1;
	ELSE IF EXISTS(SELECT TenMaHopDong FROM DmMaHopDongChuan WHERE TenMaHopDong = SUBSTRING(@SoHopDong,1,2))
		SET @ResultValue = 1;
	ELSE IF EXISTS(SELECT TenMaHopDong FROM DmMaHopDongChuan WHERE TenMaHopDong = SUBSTRING(@SoHopDong,1,3))
		SET @ResultValue = 1;
	ELSE IF EXISTS(SELECT TenMaHopDong FROM DmMaHopDongChuan WHERE TenMaHopDong = SUBSTRING(@SoHopDong,1,4))
		SET @ResultValue = 1;
	ELSE IF EXISTS(SELECT TenMaHopDong FROM DmMaHopDongChuan WHERE TenMaHopDong = SUBSTRING(@SoHopDong,1,7))
		SET @ResultValue = 1;
	ELSE
		SET @ResultValue = 0;
	
	-- Return the result of the function
	RETURN @ResultValue

END
```
