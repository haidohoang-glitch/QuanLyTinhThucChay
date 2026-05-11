# Function: `ThucChayMuaNgoai_GetSoLuongByDonViTinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-01-13 17:20:20.080000
- **Ngày sửa cuối**: 2015-01-13 17:20:20.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@soLuong` | `int(4)` | No |
| `@donViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	Get so luong thuc chay mua ngoai theo don vi tinh
-- =============================================
CREATE FUNCTION dbo.ThucChayMuaNgoai_GetSoLuongByDonViTinh
(
	-- Add the parameters for the function here
	@soLuong	INT,
	@donViTinh	NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @resultValue INT

	-- Add the T-SQL statements to compute the return value here
	IF @donViTinh = 'CPM'
		SET @soLuong = (@soLuong*1000)
	ELSE IF @donViTinh = N'Tuần'
		SET @soLuong = (@soLuong*7)
	ELSE IF @donViTinh = N'Tháng'
		SET @soLuong = (@soLuong*30)
	ELSE IF @donViTinh = N'Năm'
		SET @soLuong = (@soLuong*365)

	-- Return the result of the function
	RETURN @soLuong

END

```
