# Function: `ThucChay_CheckBeforeInsertThucChayDaTinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-09-29 11:56:13.873000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.117000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@ProductUnitName` | `nvarchar(100)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION ThucChay_CheckBeforeInsertThucChayDaTinh
(
	-- Add the parameters for the function here
	@ProductUnitName NVARCHAR(50),
	@HopDongChiTietREF INT,
	@TongViewThucChay INT, 
	@TongClickThucChay INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue INT, @DonViTinh NVARCHAR(50)
	SET @ResultValue = 0;
	
	-- Add the T-SQL statements to compute the return value here
	SELECT @DonViTinh = DonViTinh 
	FROM HopDongChiTiet hdct 
	WHERE hdct.HopDongChiTietID = @HopDongChiTietREF	
	
	IF (@DonViTinh IN  ('CPC', 'CPV','CPM'))
		BEGIN
			IF((@DonViTinh = 'CPC' AND @TongClickThucChay > 0) OR (@DonViTinh = 'CPM' AND @TongViewThucChay > 0))
				SET @ResultValue = 1		
		END
	ELSE
		BEGIN
			IF((@ProductUnitName = 'CPC' AND @TongClickThucChay > 0) OR (@ProductUnitName = 'CPM' AND @TongViewThucChay > 0))
				SET @ResultValue = 1
		END 
	-- Return the result of the function
	RETURN @ResultValue

END

```
