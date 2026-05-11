# Function: `ThucChay_GetQuantityThucChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-12-04 12:12:23.923000
- **Ngày sửa cuối**: 2014-12-04 12:12:23.923000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@sanPhamId` | `int(4)` | No |
| `@soLuongPhanBo` | `int(4)` | No |
| `@donViTinhPhanBo` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-11-18
-- Description:	Get quanlity thuc chay
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetQuantityThucChay]
(
	-- Add the parameters for the function here
	@sanPhamId		INT,
	@soLuongPhanBo	INT,
	@donViTinhPhanBo	NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @donViTinhThucChay	INT

	IF @sanPhamId = 423 -- Google
	BEGIN
		SET @donViTinhThucChay = 
		CASE @donViTinhPhanBo
			WHEN N'TUẦN' THEN @soLuongPhanBo*7
			WHEN N'THÁNG' THEN @soLuongPhanBo*30
			WHEN N'NĂM' THEN @soLuongPhanBo*365
			ELSE 1 
		END
	END

	-- Return the result of the function
	RETURN @donViTinhThucChay

END

```
