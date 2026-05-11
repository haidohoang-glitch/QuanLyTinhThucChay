# Function: `ThucChay_GetSoLuongTheoHopDong`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-01 12:10:35.773000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.233000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@NgayHopDong` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.ThucChay_GetSoLuongTheoHopDong
(
	-- Add the parameters for the function here
	@SoHopDong nvarchar(50),
	@NgayHopDong datetime
)
RETURNS bigint
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue bigint;
	DECLARE @Count int;

	-- Add the T-SQL statements to compute the return value here
	SET @Count = (SELECT COUNT(1) FROM ThucChayDaTinh WHERE SoHopDong = @SoHopDong AND CONVERT(Date,NgayThucHien) = @NgayHopDong)
	
	IF (@Count > 1) 
		SET @ResultValue = (SELECT SUM(CONVERT(bigint, Soluong))
							FROM ThucChayDaTinh
							WHERE SoHopDong = @SoHopDong AND CONVERT(Date,NgayThucHien) = @NgayHopDong
							)
	ELSE
		SET @ResultValue = (SELECT (CONVERT(bigint, Soluong))
							FROM ThucChayDaTinh
							WHERE SoHopDong = @SoHopDong AND CONVERT(Date,NgayThucHien) = @NgayHopDong
							)
	-- Return the result of the function
	RETURN @ResultValue;

END

```
